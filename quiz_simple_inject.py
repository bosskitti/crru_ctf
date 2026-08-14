"""
Simple string replacement: find answers.push block end -> inject fetch call
using exact string matching
"""
import sys, re, json
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
app = create_app()

with app.app_context():
    from CTFd.models import db
    from CTFd.plugins.tutorials import TutorialLesson, TutorialQuizAnswer

    target_ids = [164,165,166,167,168,169,170,171,172,195,196,198,199,200,201]
    fixed = 0

    # The old tail (what comes after answers collection):
    # "  var fill = document.getElementById('lesson-gauge-fill-' + lnum);"
    # ... old score-based UI ... 
    # "  box.querySelector('.mq-btn-check').disabled = true;\n}"
    #
    # Strategy: replace from "  var fill = ..." to the end of the function
    # with a fetch call that contains the UI code inside .then()

    for lid in target_ids:
        lesson = TutorialLesson.query.get(lid)
        if not lesson or not lesson.content:
            continue
        try:
            cells = json.loads(lesson.content)
        except:
            continue

        changed = False
        for cell in cells:
            if cell.get('type') != 'markdown':
                continue
            val = cell.get('value', '')
            if 'quiz/submit' in val or 'answers.push' not in val:
                continue

            # Extract lesson_id that was used in mq-box from the mq-box-N pattern
            # (these lessons use lnum=1 in mq-box, but actual lesson id is 'lid')
            total_q = TutorialQuizAnswer.query.filter_by(lesson_id=lid).count()

            def patch_script(ms):
                open_tag = ms.group(1)
                body = ms.group(2)
                close_tag = ms.group(3)

                if 'quiz/submit' in body or 'answers.push' not in body:
                    return ms.group(0)

                # Find: "  });\n  var fill = " — the split point between answers collect and old UI
                SPLIT = "  });\n  var fill = "
                idx = body.find(SPLIT)
                if idx < 0:
                    # Try alternate split
                    SPLIT = "  });\n  var fill ="
                    idx = body.find(SPLIT)
                if idx < 0:
                    print(f"  No split point in L{lid}")
                    return ms.group(0)

                # Keep everything up to and including "}); " (end of answers.forEach)
                before = body[:idx + 4]  # up to "  });"

                # The 'after' is from "\n  var fill = ..." to end of body
                after = body[idx + 4:]

                # Find end marker: closing } of the check function
                # Look for "box.querySelector('.mq-btn-check').disabled = true;"
                DISABLED = "box.querySelector('.mq-btn-check').disabled = true;"
                dis_idx = after.find(DISABLED)
                if dis_idx < 0:
                    print(f"  No disabled marker in L{lid}")
                    return ms.group(0)
                
                # Find the line end after disabled
                line_end = after.find('\n', dis_idx)
                if line_end < 0:
                    line_end = len(after)
                
                # rest = everything after the disabled line (closing braces of function, setTimeout etc.)
                rest = after[line_end:]

                new_fetch = (
                    f"\n\n  fetch('/api/v1/tutorials/quiz/submit', {{\n"
                    f"    method: 'POST',\n"
                    f"    headers: {{'Content-Type': 'application/json', 'CSRF-Token': window.init.csrfNonce}},\n"
                    f"    body: JSON.stringify({{lesson_id: {lid}, answers: answers}})\n"
                    f"  }}).then(function(r) {{ return r.json(); }}).then(function(res) {{\n"
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
                    f"  }}).catch(function(e) {{ console.error('Quiz submit error:', e); }});"
                )

                new_body = before + new_fetch + rest
                return open_tag + new_body + close_tag

            new_val = re.sub(
                r'(<script[^>]*>)(.*?)(</script>)',
                patch_script, val, flags=re.DOTALL
            )
            if new_val != val:
                cell['value'] = new_val
                changed = True
                print(f"  Fixed: lesson {lid}")

        if changed:
            lesson.content = json.dumps(cells, ensure_ascii=False)
            fixed += 1

    db.session.commit()
    print(f"\nFixed: {fixed} lessons")

    # Verify
    missing = []
    ok = 0
    for lesson in TutorialLesson.query.all():
        if not lesson.content or not lesson.content.strip().startswith('['):
            continue
        try:
            cells = json.loads(lesson.content)
        except:
            continue
        for cell in cells:
            val = cell.get('value', '')
            if 'mq-btn-check' in val:
                if 'quiz/submit' in val:
                    ok += 1
                else:
                    missing.append(lesson.id)
    print(f"  quiz/submit OK: {ok}")
    if missing:
        print(f"  MISSING: {missing}")
    else:
        print("  ALL DONE ✓")
