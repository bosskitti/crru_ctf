"""
Final patch: inject fetch/quiz/submit after answers collection in lessons 164-201
that have answers[] but no fetch call
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
            if 'quiz/submit' in val:
                continue  # already fixed

            # Find lnum
            lnum_m = re.search(r"solved_lesson_(\d+)", val)
            if not lnum_m:
                lnum_m = re.search(r"mq-box-(\d+)", val)
            if not lnum_m:
                continue
            lnum = lnum_m.group(1)
            total_q = TutorialQuizAnswer.query.filter_by(lesson_id=int(lnum)).count()

            # The script has collected answers[] but then goes straight to fill/text/status
            # We need to inject fetch BEFORE the fill/text/status section
            # Find: "var fill = document.getElementById('lesson-gauge-fill-' + lnum);"
            # and inject fetch BEFORE it

            FETCH_BLOCK = f"""fetch('/api/v1/tutorials/quiz/submit', {{
    method: 'POST',
    headers: {{'Content-Type': 'application/json', 'CSRF-Token': window.init.csrfNonce}},
    body: JSON.stringify({{lesson_id: {lnum}, answers: answers}})
  }}).then(function(r) {{ return r.json(); }}).then(function(res) {{
    if (!res.success) {{ alert('เกิดข้อผิดพลาด: ' + (res.message || '')); return; }}
    var score = res.score;
    var results = res.results;
    groups.forEach(function(g, i) {{
      var selected_opt = g.querySelector('.mini-opt.selected');
      g.querySelectorAll('.mini-opt').forEach(function(o) {{
        o.classList.remove('correct', 'incorrect');
        o.style.pointerEvents = 'none';
      }});
      if (selected_opt) selected_opt.classList.add(results[i] ? 'correct' : 'incorrect');
    }});
    var fill = document.getElementById('lesson-gauge-fill-{lnum}');
    var text = document.getElementById('lesson-gauge-text-{lnum}');
    var status_txt = document.getElementById('lesson-status-txt-{lnum}');
    var status = document.getElementById('mq-status-{lnum}');
    if (fill) {{ fill.setAttribute('stroke-dasharray', '100, 100'); fill.style.stroke = '#3ddc84'; }}
    if (text) text.textContent = '100%';
    if (status_txt) status_txt.innerHTML = '<span style="color:#3ddc84;font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ส่งคำตอบสำเร็จ</span>';
    if (status) {{
      status.style.display = 'block';
      status.style.background = 'rgba(61,220,132,0.08)';
      status.style.border = '1px solid rgba(61,220,132,0.25)';
      status.style.color = '#3ddc84';
      status.innerHTML = '🏆 <strong>ประเมินผลสำเร็จ!</strong> คะแนนของคุณ: ' + score + '/{total_q} ข้อ';
    }}
    localStorage.setItem('solved_lesson_{lnum}', 'solved');
    if (typeof updateProgressUI === 'function') updateProgressUI();
    box.querySelector('.mq-btn-check').disabled = true;
  }}).catch(function(e) {{ console.error('Quiz submit error:', e); }});"""

            # Remove the old fill/text/status/localStorage block from check function
            # and replace with fetch + those inside the .then()
            OLD_TAIL = re.compile(
                r"(  var fill = document\.getElementById\('lesson-gauge-fill-' \+ lnum\);)"
                r".*?"
                r"(box\.querySelector\('\.mq-btn-check'\)\.disabled\s*=\s*true;\s*\n})",
                re.DOTALL
            )

            def inject(m_t):
                return FETCH_BLOCK + "\n}"

            # Only do this inside the check function, not in setTimeout
            # Use script-level replacement
            def patch_script(ms):
                open_tag = ms.group(1)
                body = ms.group(2)
                close_tag = ms.group(3)
                if 'quiz/submit' in body:
                    return ms.group(0)
                if 'answers.push' not in body:
                    return ms.group(0)
                if "var fill = document.getElementById('lesson-gauge-fill-' + lnum)" not in body:
                    return ms.group(0)
                new_body = OLD_TAIL.sub(inject, body, count=1)
                if new_body != body:
                    return open_tag + new_body + close_tag
                return ms.group(0)

            new_val = re.sub(
                r'(<script[^>]*>)(.*?)(</script>)',
                patch_script,
                val,
                flags=re.DOTALL
            )
            if new_val != val:
                cell['value'] = new_val
                changed = True
                print(f"  Injected fetch: lesson {lid}")

        if changed:
            lesson.content = json.dumps(cells, ensure_ascii=False)
            fixed += 1

    db.session.commit()
    print(f"\nFixed: {fixed} lessons")

    # Final verify
    print("\n--- Final verification ---")
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
            if 'checkMiniQuiz' not in val and 'mq-btn-check' not in val:
                continue
            if 'quiz/submit' in val:
                ok += 1
            else:
                missing.append(lesson.id)
    print(f"  OK (quiz/submit): {ok} lessons")
    if missing:
        print(f"  Still missing: {missing}")
    else:
        print("  ALL DONE — every quiz calls /api/v1/tutorials/quiz/submit ✓")
