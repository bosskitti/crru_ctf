"""
Direct string injection: find "answers.push(...)" block end
then insert fetch + move the fill/text/status/localStorage into the .then()
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
                continue

            # Find lnum from mq-box-N
            lnum_m = re.search(r"#mq-box-(\d+)", val)
            if not lnum_m:
                lnum_m = re.search(r"solved_lesson_(\d+)", val)
            if not lnum_m:
                print(f"  Cannot find lnum for L{lid}")
                continue
            lnum = lnum_m.group(1)
            total_q = TutorialQuizAnswer.query.filter_by(lesson_id=int(lnum)).count()

            def patch_script(ms):
                open_tag = ms.group(1)
                body = ms.group(2)
                close_tag = ms.group(3)

                if 'quiz/submit' in body or 'answers.push' not in body:
                    return ms.group(0)

                # Strategy: 
                # 1. Find "  var answers = [];" ... "  });"  (the collect block)
                # 2. Everything AFTER that collect block and BEFORE the closing } of the function
                #    becomes the old UI code we want to move into .then()
                # 3. Wrap with fetch

                # Find end of answers collection: the "  });" after groups.forEach
                collect_end = re.search(
                    r"(  var answers = \[\];.*?  \}\);)\s*\n"
                    r"(  (?:var|const) fill = )",
                    body, re.DOTALL
                )
                if not collect_end:
                    print(f"  Cannot find collect_end pattern in L{lid}")
                    return ms.group(0)

                split_at = collect_end.end(1)
                before = body[:split_at]
                after = body[split_at:]  # starts with "\n  var fill = ..."

                # 'after' is the old UI update code + localStorage + disabled
                # Remove the closing } of the enclosing function from 'after'
                # and wrap everything in fetch.then()

                # Find the last } that closes the check function
                # We look for "box.querySelector('.mq-btn-check').disabled = true;"
                disabled_idx = after.find("box.querySelector('.mq-btn-check').disabled = true;")
                if disabled_idx < 0:
                    print(f"  Cannot find disabled marker in L{lid}")
                    return ms.group(0)

                # Include past the disabled line and any closing braces
                end_of_disabled = after.find('\n', disabled_idx) + 1
                ui_code = after[:end_of_disabled].strip()
                rest_of_body = after[end_of_disabled:]  # closing } of function etc.

                new_body = (
                    before + "\n\n"
                    f"  fetch('/api/v1/tutorials/quiz/submit', {{\n"
                    f"    method: 'POST',\n"
                    f"    headers: {{'Content-Type': 'application/json', 'CSRF-Token': window.init.csrfNonce}},\n"
                    f"    body: JSON.stringify({{lesson_id: {lnum}, answers: answers}})\n"
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
                    f"    var fill = document.getElementById('lesson-gauge-fill-' + {lnum});\n"
                    f"    var text = document.getElementById('lesson-gauge-text-' + {lnum});\n"
                    f"    var status_txt = document.getElementById('lesson-status-txt-' + {lnum});\n"
                    f"    var status = document.getElementById('mq-status-' + {lnum});\n"
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
                    f"    localStorage.setItem('solved_lesson_{lnum}', 'solved');\n"
                    f"    if (typeof updateProgressUI === 'function') updateProgressUI();\n"
                    f"    box.querySelector('.mq-btn-check').disabled = true;\n"
                    f"  }}).catch(function(e) {{ console.error('Quiz submit error:', e); }});"
                    + "\n" + rest_of_body
                )

                return open_tag + new_body + close_tag

            new_val = re.sub(
                r'(<script[^>]*>)(.*?)(</script>)',
                patch_script, val, flags=re.DOTALL
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
    print("\n--- Final check ---")
    missing = []
    ok = 0
    data_c_remain = []
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
            if 'data-correct' in val:
                data_c_remain.append(lesson.id)

    print(f"  quiz/submit OK: {ok} lessons")
    if missing:
        print(f"  MISSING quiz/submit: {missing}")
    else:
        print("  ALL lessons have quiz/submit ✓")
    if data_c_remain:
        print(f"  data-correct still in: {data_c_remain}")
    else:
        print("  No data-correct in HTML ✓")
