"""
Final fix for L164-201: use 'var fill = ' as split and end of function as boundary.
Simply replace from 'var fill = ' to end of closing '}' of function.
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

        total_q = TutorialQuizAnswer.query.filter_by(lesson_id=lid).count()
        changed = False

        for cell in cells:
            if cell.get('type') != 'markdown':
                continue
            val = cell.get('value', '')
            if 'quiz/submit' in val or 'answers.push' not in val:
                continue

            # Find split: right after the answers collect forEach closes
            # Try patterns:
            split_marker = None
            split_pos = -1
            for marker in ["});\n  var fill", "});\n\n  var fill"]:
                p = val.find(marker)
                if p >= 0:
                    split_marker = marker
                    split_pos = p
                    break

            if split_pos < 0:
                print(f"  L{lid}: no split found")
                continue

            # Everything before the split (keep answers collection)
            end_of_collect = split_pos + 3  # length of "});"
            before = val[:end_of_collect]

            # Everything after = old UI code we want to replace
            # Find end of the enclosing function
            # The check function ends with "\n}" followed by a newline/setTimeout or script end
            # Strategy: find "\n}" after the split that's at zero indent (first char of line = '}')
            rest_of_function = val[end_of_collect:]

            # Find the end of function: look for "\n}" at the start of a line
            func_end_pattern = re.compile(r'\n\}(?=\n|$)')
            func_end_m = func_end_pattern.search(rest_of_function)
            if not func_end_m:
                print(f"  L{lid}: no function end found")
                continue

            func_end_pos = func_end_m.end()  # includes the "}"
            old_ui = rest_of_function[:func_end_pos]
            tail = rest_of_function[func_end_pos:]

            FETCH = (
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
                f"    if (box.querySelector('.mq-btn-check')) box.querySelector('.mq-btn-check').disabled = true;\n"
                f"  }}).catch(function(e) {{ console.error('Quiz submit error:', e); }});\n"
                f"}}"
            )

            cell['value'] = before + FETCH + tail
            changed = True
            print(f"  Fixed: lesson {lid} (tail starts: {repr(tail[:50])})")

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
            if 'mq-btn-check' in val or 'checkMiniQuiz' in val:
                if 'quiz/submit' in val:
                    ok += 1
                else:
                    missing.append(lesson.id)
    print(f"  quiz/submit OK: {ok}")
    if missing:
        print(f"  STILL MISSING: {missing}")
    else:
        print("  ALL DONE — all quizzes use server-side validation ✓")
