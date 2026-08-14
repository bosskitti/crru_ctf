"""
Step 4: Fix remaining data-correct in lessons with arrow function syntax
AND lessons that checkMiniQuiz uses arrow functions (not yet rewritten)
"""
import sys, re, json
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
app = create_app()

with app.app_context():
    from CTFd.models import db
    from CTFd.plugins.tutorials import TutorialLesson

    lessons = TutorialLesson.query.all()
    fixed = 0

    # Pattern A: arrow function style checkMiniQuiz with data-correct
    # groups.forEach(g => { const correctVal = g.getAttribute('data-correct'); ... })
    OLD_CHECK_ARROW = re.compile(
        r"groups\.forEach\(g\s*=>\s*\{.*?"
        r"const correctVal\s*=\s*g\.getAttribute\('data-correct'\);"
        r".*?\}\);",
        re.DOTALL
    )

    # Pattern B: arrow-style setTimeout restore block with data-correct
    OLD_RESTORE_ARROW = re.compile(
        r"groups\.forEach\(g\s*=>\s*\{.*?"
        r"(?:const|var) correctVal\s*=\s*g\.getAttribute\('data-correct'\);"
        r".*?o\.style\.pointerEvents\s*=\s*'none';"
        r".*?\}\);\s*\}\);",
        re.DOTALL
    )

    RESTORE_REPLACEMENT = (
        "groups.forEach(g => {\n"
        "      // Answers are stored server-side; just lock on restore\n"
        "      g.querySelectorAll('.mini-opt').forEach(o => {\n"
        "        o.style.pointerEvents = 'none';\n"
        "        o.style.opacity = '0.7';\n"
        "      });\n"
        "    }); });"
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
            if 'data-correct' not in val:
                continue

            def fix_scripts(m):
                open_tag = m.group(1)
                body = m.group(2)
                close_tag = m.group(3)
                if 'data-correct' not in body:
                    return m.group(0)

                new_body = body
                lnum_m = re.search(r'checkMiniQuiz(\d+)', body)
                lnum = lnum_m.group(1) if lnum_m else None
                total_q = len(re.findall(r'class="mq-q"', val)) or len(re.findall(r'class=\\"mq-q\\"', val))

                # --- Fix checkMiniQuiz function: arrow style ---
                if lnum:
                    func_pattern = re.compile(
                        r'(function\s+checkMiniQuiz' + lnum + r'\s*\(\w+\)\s*\{)'
                        r'(.+?)'
                        r'(\n\})',
                        re.DOTALL
                    )
                    def replace_func(fm):
                        func_header = fm.group(1)
                        func_body = fm.group(2)
                        func_close = fm.group(3)
                        keep_pattern = re.compile(
                            r'^(.*?if\s*\(!allAnswered\)\s*\{[^}]+\})',
                            re.DOTALL
                        )
                        keep_m = keep_pattern.match(func_body)
                        if not keep_m:
                            return fm.group(0)
                        kept_part = keep_m.group(1)
                        new_part = kept_part + f"""

  var answers = [];
  groups.forEach(g => {{
    var sel = g.querySelector('.mini-opt.selected');
    answers.push(sel ? sel.getAttribute('data-val') : null);
  }});

  fetch('/api/v1/tutorials/quiz/submit', {{
    method: 'POST',
    headers: {{'Content-Type': 'application/json', 'CSRF-Token': window.init.csrfNonce}},
    body: JSON.stringify({{lesson_id: {lnum}, answers: answers}})
  }}).then(r => r.json()).then(function(res) {{
    if (!res.success) {{ alert('เกิดข้อผิดพลาด: ' + (res.message || '')); return; }}
    var score = res.score;
    var results = res.results;

    groups.forEach(function(g, i) {{
      var selected_opt = g.querySelector('.mini-opt.selected');
      g.querySelectorAll('.mini-opt').forEach(function(o) {{
        o.classList.remove('correct', 'incorrect');
        o.style.pointerEvents = 'none';
      }});
      if (selected_opt) {{
        selected_opt.classList.add(results[i] ? 'correct' : 'incorrect');
      }}
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
  }}).catch(e => console.error('Quiz submit error:', e));
"""
                        return func_header + new_part + func_close

                    new_body = func_pattern.sub(replace_func, new_body)

                # --- Fix restore block (setTimeout): both arrow and regular ---
                # Pattern for arrow-style restore forEach
                OLD_RESTORE = re.compile(
                    r"(groups\.forEach\([^\)]*=>\s*\{)"   # groups.forEach(g => {
                    r"(.*?)"
                    r"(?:const|var)\s+correctVal\s*=\s*g\.getAttribute\('data-correct'\);"
                    r".*?"
                    r"o\.style\.pointerEvents\s*=\s*['\"]none['\"];"
                    r".*?"
                    r"\}\);\s*"       # end inner forEach
                    r"\}\);",         # end outer forEach
                    re.DOTALL
                )

                RESTORE_NEW = (
                    "groups.forEach(g => {\n"
                    "      // Answers are server-side only — just lock on restore\n"
                    "      g.querySelectorAll('.mini-opt').forEach(o => {\n"
                    "        o.style.pointerEvents = 'none';\n"
                    "        o.style.opacity = '0.7';\n"
                    "      });\n"
                    "    });"
                )

                new_body2 = OLD_RESTORE.sub(RESTORE_NEW, new_body)
                if new_body2 != new_body:
                    new_body = new_body2

                if new_body != body:
                    return open_tag + new_body + close_tag
                return m.group(0)

            new_val = re.sub(
                r'(<script[^>]*>)(.*?)(</script>)',
                fix_scripts,
                val,
                flags=re.DOTALL
            )
            if new_val != val:
                cell['value'] = new_val
                changed = True
                print(f"  Fixed lesson {lesson.id}")

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
        print("  ALL CLEAR — no data-correct left in HTML!")
    else:
        print(f"  Total remaining: {total_remaining}")
