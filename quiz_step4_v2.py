"""
Step 4 v2: Fix lessons 164-201 that use arrow functions and 'lnum' variable
Use targeted string replacement instead of regex for the check block
"""
import sys, re, json
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
app = create_app()

with app.app_context():
    from CTFd.models import db
    from CTFd.plugins.tutorials import TutorialLesson

    target_lesson_ids = [164,165,166,167,168,169,170,171,172,195,196,198,199,200,201]
    fixed = 0

    for lid in target_lesson_ids:
        lesson = TutorialLesson.query.get(lid)
        if not lesson or not lesson.content:
            continue
        raw = lesson.content
        if not raw.strip().startswith('['):
            continue
        try:
            cells = json.loads(raw)
        except Exception:
            continue

        changed = False
        for cell in cells:
            if cell.get('type') != 'markdown':
                continue
            val = cell.get('value', '')
            if 'data-correct' not in val:
                continue

            # Extract lesson number from mq-box-NNN or checkMiniQuizNNN or solved_lesson_NNN
            lnum_m = re.search(r'solved_lesson_(\d+)', val)
            if not lnum_m:
                lnum_m = re.search(r"mq-box-(\d+)", val)
            if not lnum_m:
                print(f"  Cannot find lnum for lesson {lid}, skipping")
                continue
            lnum = lnum_m.group(1)

            # Count questions in this lesson from DB
            from CTFd.plugins.tutorials import TutorialQuizAnswer
            total_q = TutorialQuizAnswer.query.filter_by(lesson_id=int(lnum)).count()
            if total_q == 0:
                total_q = len(re.findall(r'class="mq-q"', val))

            # ── Replace the check block (groups.forEach with data-correct) ──
            # Pattern: groups.forEach(g => { const correctVal ... if (selectedVal === correctVal) score++; });
            OLD_CHECK = re.compile(
                r"groups\.forEach\(g\s*=>\s*\{[^}]*?"
                r"const correctVal\s*=\s*g\.getAttribute\('data-correct'\);.*?"
                r"if\s*\(selectedVal\s*===\s*correctVal\)\s*score\+\+;"
                r".*?\}\);",
                re.DOTALL
            )

            NEW_COLLECT = (
                "var answers = [];\n"
                "  groups.forEach(g => {\n"
                "    const sel = g.querySelector('.mini-opt.selected');\n"
                "    answers.push(sel ? sel.getAttribute('data-val') : null);\n"
                "  });"
            )

            # ── Replace old fetch (quick_quiz without score/answers) ──
            # Find and replace the whole fetch('/api/v1/tutorials/progress'...) block with new quiz/submit
            OLD_FETCH = re.compile(
                r"fetch\('/api/v1/tutorials/progress'.*?"
                r"\}\)\.catch\(e\s*=>\s*console\.error\(.*?\)\);",
                re.DOTALL
            )

            NEW_FETCH = (
                f"fetch('/api/v1/tutorials/quiz/submit', {{\n"
                f"    method: 'POST',\n"
                f"    headers: {{'Content-Type': 'application/json', 'CSRF-Token': window.init.csrfNonce}},\n"
                f"    body: JSON.stringify({{lesson_id: {lnum}, answers: answers}})\n"
                f"  }}).then(r => r.json()).then(function(res) {{\n"
                f"    if (!res.success) {{ alert('เกิดข้อผิดพลาด: ' + (res.message || '')); return; }}\n"
                f"    var score = res.score;\n"
                f"    var results = res.results;\n"
                f"    groups.forEach(function(g, i) {{\n"
                f"      var selected_opt = g.querySelector('.mini-opt.selected');\n"
                f"      g.querySelectorAll('.mini-opt').forEach(function(o) {{\n"
                f"        o.classList.remove('correct', 'incorrect');\n"
                f"        o.style.pointerEvents = 'none';\n"
                f"      }});\n"
                f"      if (selected_opt) selected_opt.classList.add(results[i] ? 'correct' : 'incorrect');\n"
                f"    }});\n"
                f"    var fill = document.getElementById('lesson-gauge-fill-' + lnum);\n"
                f"    var text = document.getElementById('lesson-gauge-text-' + lnum);\n"
                f"    var status_txt = document.getElementById('lesson-status-txt-' + lnum);\n"
                f"    var status = document.getElementById('mq-status-' + lnum);\n"
                f"    if (fill) {{ fill.setAttribute('stroke-dasharray', '100, 100'); fill.style.stroke = '#3ddc84'; }}\n"
                f"    if (text) text.textContent = '100%';\n"
                f"    if (status_txt) status_txt.innerHTML = '<span style=\"color:#3ddc84;font-weight:bold;\"><i class=\"fas fa-check-circle mr-1\"></i> ส่งคำตอบสำเร็จ</span>';\n"
                f"    if (status) {{\n"
                f"      status.style.display = 'block';\n"
                f"      status.style.background = 'rgba(61,220,132,0.08)';\n"
                f"      status.style.border = '1px solid rgba(61,220,132,0.25)';\n"
                f"      status.style.color = '#3ddc84';\n"
                f"      status.innerHTML = '🏆 <strong>ประเมินผลสำเร็จ!</strong> คะแนนของคุณ: ' + score + '/{total_q} ข้อ';\n"
                f"    }}\n"
                f"    localStorage.setItem('solved_lesson_' + lnum, 'solved');\n"
                f"    if (typeof updateProgressUI === 'function') updateProgressUI();\n"
                f"    box.querySelector('.mq-btn-check').disabled = true;\n"
                f"  }}).catch(e => console.error('Quiz submit error:', e));"
            )

            # Also fix restore block (groups.forEach with data-correct in setTimeout)
            OLD_RESTORE = re.compile(
                r"groups\.forEach\([^\)]*=>\s*\{[^{]*?"
                r"(?:const|var)\s+correctVal\s*=\s*g\.getAttribute\('data-correct'\);"
                r".*?o\.style\.pointerEvents\s*=\s*'none';"
                r".*?\}\);\s*\}\);",
                re.DOTALL
            )
            RESTORE_NEW = (
                "groups.forEach(g => {\n"
                "      g.querySelectorAll('.mini-opt').forEach(o => {\n"
                "        o.style.pointerEvents = 'none';\n"
                "        o.style.opacity = '0.7';\n"
                "      });\n"
                "    }); });"
            )

            def fix_script_block(m):
                open_tag = m.group(1)
                body = m.group(2)
                close_tag = m.group(3)
                if 'data-correct' not in body:
                    return m.group(0)
                nb = body
                # Replace check block
                nb2 = OLD_CHECK.sub(NEW_COLLECT, nb)
                # Replace old fetch
                nb3 = OLD_FETCH.sub(NEW_FETCH, nb2)
                # Fix restore block
                nb4 = OLD_RESTORE.sub(RESTORE_NEW, nb3)
                if nb4 != body:
                    return open_tag + nb4 + close_tag
                return m.group(0)

            new_val = re.sub(
                r'(<script[^>]*>)(.*?)(</script>)',
                fix_script_block,
                val,
                flags=re.DOTALL
            )
            if new_val != val:
                cell['value'] = new_val
                changed = True
                print(f"  Fixed lesson {lid}")

        if changed:
            lesson.content = json.dumps(cells, ensure_ascii=False)
            fixed += 1

    db.session.commit()
    print(f"\nFixed: {fixed} lessons")

    # Final verification
    print("\n--- Final check ---")
    total_remaining = 0
    for lesson in TutorialLesson.query.all():
        if not lesson.content or not lesson.content.strip().startswith('['):
            continue
        try:
            cells = json.loads(lesson.content)
        except:
            continue
        for cell in cells:
            val = cell.get('value', '')
            cnt = len(re.findall(r'data-correct', val))
            if cnt:
                print(f"  L{lesson.id}: {cnt} remaining")
                total_remaining += cnt
    if total_remaining == 0:
        print("  ALL CLEAR — no data-correct left in any HTML!")
    else:
        print(f"  Total remaining: {total_remaining}")
