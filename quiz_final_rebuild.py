"""
Final fix: Rebuild checkMiniQuizNNN function correctly for lessons 173-208
that were broken by step3 over-replacing the check block.
"""
import sys, re, json
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
app = create_app()

with app.app_context():
    from CTFd.models import db
    from CTFd.plugins.tutorials import TutorialLesson, TutorialQuizAnswer

    fixed = 0
    for lesson in TutorialLesson.query.all():
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

            # Find all scripts with checkMiniQuizNNN
            def fix_script(m):
                open_tag = m.group(1)
                body = m.group(2)
                close_tag = m.group(3)

                lnum_m = re.search(r'checkMiniQuiz(\d+)', body)
                if not lnum_m:
                    return m.group(0)
                lnum = lnum_m.group(1)

                # Get total questions from DB
                total_q = TutorialQuizAnswer.query.filter_by(lesson_id=int(lnum)).count()

                # Check if the function body is broken (restore-lock instead of API call)
                # Signature: the function has "just lock options on restore" comment or no fetch call
                func_pat = re.compile(
                    r'(function\s+checkMiniQuiz' + lnum + r'\s*\(\w+\)\s*\{)'
                    r'(.*?)'
                    r'(\n\}(?!\s*\.))',
                    re.DOTALL
                )

                def replace_func(fm):
                    func_header = fm.group(1)
                    func_body = fm.group(2)
                    func_close = fm.group(3)

                    # Only fix if it doesn't already call quiz/submit
                    if 'quiz/submit' in func_body:
                        return fm.group(0)

                    # Extract the allAnswered check block (keep it)
                    keep_pat = re.compile(
                        r'^(.*?'
                        r'if\s*\(!allAnswered\)\s*\{[^}]+\})',
                        re.DOTALL
                    )
                    keep_m = keep_pat.match(func_body)
                    if not keep_m:
                        # Try alternate: keep up to groups.forEach check
                        keep_m2 = re.match(r'^(.*?groups\.forEach)', func_body, re.DOTALL)
                        if not keep_m2:
                            return fm.group(0)
                        kept = keep_m2.group(1).rstrip()
                        # Remove the broken forEach that was injected
                        kept = re.sub(
                            r'groups\.forEach.*',
                            '',
                            kept,
                            flags=re.DOTALL
                        ).rstrip()
                    else:
                        kept = keep_m.group(1)

                    new_func_body = kept + f"""

  var answers = [];
  groups.forEach(function(g) {{
    var sel = g.querySelector('.mini-opt.selected');
    answers.push(sel ? sel.getAttribute('data-val') : null);
  }});

  fetch('/api/v1/tutorials/quiz/submit', {{
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
  }}).catch(function(e) {{ console.error('Quiz submit error:', e); }});
"""
                    return func_header + new_func_body + func_close

                new_body = func_pat.sub(replace_func, body)
                if new_body != body:
                    return open_tag + new_body + close_tag
                return m.group(0)

            new_val = re.sub(
                r'(<script[^>]*>)(.*?)(</script>)',
                fix_script,
                val,
                flags=re.DOTALL
            )
            if new_val != val:
                cell['value'] = new_val
                changed = True
                print(f"  Rebuilt checkMiniQuiz: lesson {lesson.id}")

        if changed:
            lesson.content = json.dumps(cells, ensure_ascii=False)
            fixed += 1

    db.session.commit()
    print(f"\nRebuilt {fixed} lessons")

    # Final verify
    print("\n--- Verify quiz/submit calls ---")
    ok = 0
    miss = []
    for lesson in TutorialLesson.query.all():
        if not lesson.content or not lesson.content.strip().startswith('['):
            continue
        try:
            cells = json.loads(lesson.content)
        except:
            continue
        for cell in cells:
            val = cell.get('value', '')
            if 'checkMiniQuiz' in val:
                if 'quiz/submit' in val:
                    ok += 1
                else:
                    miss.append(lesson.id)
    print(f"  Lessons with quiz/submit: {ok}")
    if miss:
        print(f"  MISSING quiz/submit: {miss}")
    else:
        print("  All quiz lessons now call /api/v1/tutorials/quiz/submit ✓")
