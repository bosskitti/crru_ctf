"""
Migration + fix script:
1. Create tutorial_quiz_answer table
2. Extract data-correct from all lesson HTML -> store in DB
3. Remove data-correct from HTML
4. Update JS to call server API instead of client-side check
"""
import sys, re, json
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
app = create_app()

with app.app_context():
    from CTFd.models import db
    from CTFd.plugins.tutorials import TutorialLesson

    # ── 1. Create table ──────────────────────────────────────────────────────
    db.engine.execute("""
        CREATE TABLE IF NOT EXISTS tutorial_quiz_answer (
            id          INT AUTO_INCREMENT PRIMARY KEY,
            lesson_id   INT NOT NULL,
            q_index     INT NOT NULL,
            correct_val VARCHAR(10) NOT NULL,
            INDEX idx_lesson (lesson_id)
        )
    """)
    print("[1] Table tutorial_quiz_answer ready")

    # ── 2 & 3. Extract answers + strip data-correct from HTML ────────────────
    lessons = TutorialLesson.query.all()
    lesson_updated = 0
    answer_rows = 0

    for lesson in lessons:
        if not lesson.content:
            continue
        raw = lesson.content

        # Parse JSON cell array
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

            # Collect correct answers in order
            answers = re.findall(r'data-correct=["\'](\w+)["\']', val)
            if not answers:
                continue

            # Delete old answers for this lesson (re-run safe)
            db.engine.execute(
                "DELETE FROM tutorial_quiz_answer WHERE lesson_id = %s",
                (lesson.id,)
            )

            # Insert new answers
            for idx, correct_val in enumerate(answers):
                db.engine.execute(
                    "INSERT INTO tutorial_quiz_answer (lesson_id, q_index, correct_val) VALUES (%s, %s, %s)",
                    (lesson.id, idx, correct_val)
                )
                answer_rows += 1

            # Remove data-correct from HTML
            new_val = re.sub(r'\s*data-correct=["\'][^"\']*["\']', '', val)
            cell['value'] = new_val
            changed = True

        if changed:
            lesson.content = json.dumps(cells, ensure_ascii=False)
            lesson_updated += 1

    db.session.commit()
    print(f"[2] Migrated {answer_rows} answers from {lesson_updated} lessons to DB")
    print(f"[3] Removed data-correct from HTML in {lesson_updated} lessons")

    # ── 4. Rewrite JS: replace local check with API call ─────────────────────
    # Old pattern (client-side check):
    #   var correctVal = g.getAttribute('data-correct');
    #   ...
    #   if (selectedVal === correctVal) score++;
    #
    # New: send answers[] to API, get back score

    OLD_CHECK_JS = re.compile(
        r"groups\.forEach\(function\(g\)\s*\{.*?"    # groups.forEach start
        r"if\s*\(selectedVal\s*===\s*correctVal\)\s*score\+\+;"  # score counting
        r".*?\}\);"                                  # end forEach
        r".*?"                                       # gap
        r"fetch\('/api/v1/tutorials/progress'.*?\}\)\.catch.*?;",  # old fetch
        re.DOTALL
    )

    for lesson in lessons:
        if not lesson.content:
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
            # find the script tag containing checkMiniQuiz
            scripts = re.findall(r'(<script[^>]*>)(.*?)(</script>)', val, re.DOTALL)
            new_val = val
            for (open_tag, body, close_tag) in scripts:
                if 'checkMiniQuiz' not in body:
                    continue

                # Extract lesson number from function name checkMiniQuizNNN
                lnum_match = re.search(r'checkMiniQuiz(\d+)', body)
                if not lnum_match:
                    continue
                lnum = lnum_match.group(1)

                # Build new body replacing the answer-check + fetch section
                new_body = re.sub(
                    # Match: groups.forEach that checks correctVal ... then old fetch
                    r"(groups\.forEach\(function\(g\)\s*\{)"
                    r"(\s*var correctVal = g\.getAttribute\('data-correct'\);)"
                    r"(.*?)"
                    r"(if\s*\(selectedVal\s*===\s*correctVal\)\s*score\+\+;)",
                    # Replace: remove data-correct line, keep rest, collect answer
                    r"\1"
                    r"\n    var selectedVal_\2 = selected.getAttribute('data-val');"
                    r"\3"
                    r"    answers.push(selectedVal_\2);",
                    body,
                    flags=re.DOTALL
                )

                # Simpler targeted replacement:
                # Replace the entire groups.forEach check block + old fetch with new API call
                NEW_CHECK = (
                    f"  var answers = [];\n"
                    f"  groups.forEach(function(g) {{\n"
                    f"    var selected = g.querySelector('.mini-opt.selected');\n"
                    f"    answers.push(selected ? selected.getAttribute('data-val') : null);\n"
                    f"  }});\n\n"
                    f"  fetch('/api/v1/tutorials/quiz/submit', {{\n"
                    f"    method: 'POST',\n"
                    f"    headers: {{'Content-Type': 'application/json', 'CSRF-Token': window.init.csrfNonce}},\n"
                    f"    body: JSON.stringify({{lesson_id: {lnum}, answers: answers}})\n"
                    f"  }}).then(r => r.json()).then(function(res) {{\n"
                    f"    if (!res.success) {{ alert('เกิดข้อผิดพลาด: ' + (res.message || '')); return; }}\n"
                    f"    var score = res.score;\n"
                    f"    var results = res.results; // [true, false, ...]\n\n"
                    f"    // Show per-question feedback\n"
                    f"    groups.forEach(function(g, i) {{\n"
                    f"      var is_correct = results[i];\n"
                    f"      var selected_opt = g.querySelector('.mini-opt.selected');\n"
                    f"      g.querySelectorAll('.mini-opt').forEach(function(o) {{\n"
                    f"        o.classList.remove('correct', 'incorrect');\n"
                    f"        o.style.pointerEvents = 'none';\n"
                    f"      }});\n"
                    f"      if (selected_opt) {{\n"
                    f"        selected_opt.classList.add(is_correct ? 'correct' : 'incorrect');\n"
                    f"      }}\n"
                    f"    }});\n\n"
                    f"    var fill = document.getElementById('lesson-gauge-fill-' + {lnum});\n"
                    f"    var text = document.getElementById('lesson-gauge-text-' + {lnum});\n"
                    f"    var status_txt = document.getElementById('lesson-status-txt-' + {lnum});\n"
                    f"    var status = document.getElementById('mq-status-' + {lnum});\n"
                    f"    status.style.display = 'block';\n\n"
                    f"    if (fill) {{ fill.setAttribute('stroke-dasharray', '100, 100'); fill.style.stroke = '#3ddc84'; }}\n"
                    f"    if (text) text.textContent = '100%';\n"
                    f"    if (status_txt) status_txt.innerHTML = '<span style=\"color:#3ddc84; font-weight:bold;\"><i class=\"fas fa-check-circle mr-1\"></i> ส่งคำตอบสำเร็จ</span>';\n\n"
                    f"    status.style.background = 'rgba(61,220,132,0.08)';\n"
                    f"    status.style.border = '1px solid rgba(61,220,132,0.25)';\n"
                    f"    status.style.color = '#3ddc84';\n"
                    f"    status.innerHTML = `🏆 <strong>ประเมินผลสำเร็จ!</strong> คะแนนของคุณ: ${{score}}/{lnum_groups} ข้อ`;\n\n"
                    f"    localStorage.setItem('solved_lesson_{lnum}', 'solved');\n"
                    f"    if (typeof updateProgressUI === 'function') updateProgressUI();\n"
                    f"    box.querySelector('.mq-btn-check').disabled = true;\n"
                    f"  }}).catch(e => console.error('Quiz submit error:', e));\n"
                )

                # Replace the check function body after allAnswered check
                # Pattern: everything from "  groups.forEach" after the allAnswered check to end of function
                old_check_pattern = re.compile(
                    r"(if\s*\(!allAnswered\)\s*\{[^}]+\})"  # allAnswered guard
                    r"(.+)"                                   # all the check logic
                    r"(box\.querySelector\('\.mq-btn-check'\)\.disabled\s*=\s*true;)",
                    re.DOTALL
                )

                # Count groups for the status message
                mq_q_count = len(re.findall(r'class="mq-q"', val))

                def make_replacement(m):
                    return (
                        m.group(1) +
                        "\n\n" +
                        "  var answers = [];\n"
                        "  groups.forEach(function(g) {\n"
                        "    var selected = g.querySelector('.mini-opt.selected');\n"
                        "    answers.push(selected ? selected.getAttribute('data-val') : null);\n"
                        "  });\n\n"
                        f"  fetch('/api/v1/tutorials/quiz/submit', {{\n"
                        "    method: 'POST',\n"
                        "    headers: {'Content-Type': 'application/json', 'CSRF-Token': window.init.csrfNonce},\n"
                        f"    body: JSON.stringify({{lesson_id: {lnum}, answers: answers}})\n"
                        "  }).then(r => r.json()).then(function(res) {\n"
                        "    if (!res.success) { alert('เกิดข้อผิดพลาด: ' + (res.message || '')); return; }\n"
                        "    var score = res.score;\n"
                        "    var results = res.results;\n\n"
                        "    groups.forEach(function(g, i) {\n"
                        "      var is_correct = results[i];\n"
                        "      var selected_opt = g.querySelector('.mini-opt.selected');\n"
                        "      g.querySelectorAll('.mini-opt').forEach(function(o) {\n"
                        "        o.classList.remove('correct', 'incorrect');\n"
                        "        o.style.pointerEvents = 'none';\n"
                        "      });\n"
                        "      if (selected_opt) {\n"
                        "        selected_opt.classList.add(is_correct ? 'correct' : 'incorrect');\n"
                        "      }\n"
                        "    });\n\n"
                        f"    var fill = document.getElementById('lesson-gauge-fill-{lnum}');\n"
                        f"    var text = document.getElementById('lesson-gauge-text-{lnum}');\n"
                        f"    var status_txt = document.getElementById('lesson-status-txt-{lnum}');\n"
                        f"    var status = document.getElementById('mq-status-{lnum}');\n"
                        "    status.style.display = 'block';\n"
                        "    if (fill) { fill.setAttribute('stroke-dasharray', '100, 100'); fill.style.stroke = '#3ddc84'; }\n"
                        "    if (text) text.textContent = '100%';\n"
                        f"    if (status_txt) status_txt.innerHTML = '<span style=\"color:#3ddc84;font-weight:bold;\"><i class=\"fas fa-check-circle mr-1\"></i> ส่งคำตอบสำเร็จ</span>';\n"
                        "    status.style.background = 'rgba(61,220,132,0.08)';\n"
                        "    status.style.border = '1px solid rgba(61,220,132,0.25)';\n"
                        "    status.style.color = '#3ddc84';\n"
                        f"    status.innerHTML = `🏆 <strong>ประเมินผลสำเร็จ!</strong> คะแนนของคุณ: ${{score}}/{mq_q_count} ข้อ`;\n"
                        f"    localStorage.setItem('solved_lesson_{lnum}', 'solved');\n"
                        "    if (typeof updateProgressUI === 'function') updateProgressUI();\n"
                        "    box.querySelector('.mq-btn-check').disabled = true;\n"
                        "  }).catch(e => console.error('Quiz submit error:', e));\n"
                    )

                new_body = old_check_pattern.sub(make_replacement, body)
                if new_body != body:
                    new_val = new_val.replace(open_tag + body + close_tag,
                                              open_tag + new_body + close_tag, 1)
                    changed = True
                    print(f"  JS updated for lesson {lesson.id} (lnum={lnum})")

            if changed:
                cell['value'] = new_val

        if changed:
            lesson.content = json.dumps(cells, ensure_ascii=False)

    db.session.commit()
    print("[4] JS updated to call server API")
    print("Done!")
