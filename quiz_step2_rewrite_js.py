"""
Step 2: Rewrite checkMiniQuizNNN() in all lesson scripts
to call /api/v1/tutorials/quiz/submit instead of local data-correct check
"""
import sys, re, json
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
app = create_app()

with app.app_context():
    from CTFd.models import db
    from CTFd.plugins.tutorials import TutorialLesson

    lessons = TutorialLesson.query.all()
    js_updated = 0

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
            if 'checkMiniQuiz' not in val:
                continue

            # Find all <script>...</script> blocks
            def rewrite_script(m):
                open_tag = m.group(1)
                body = m.group(2)
                close_tag = m.group(3)

                if 'checkMiniQuiz' not in body:
                    return m.group(0)

                # Extract lesson number
                lnum_m = re.search(r'checkMiniQuiz(\d+)', body)
                if not lnum_m:
                    return m.group(0)
                lnum = lnum_m.group(1)

                # Count mq-q divs in cell to know total questions
                total_q = len(re.findall(r'class="mq-q"', val))

                # Build new checkMiniQuizNNN function body
                # We replace everything inside the function after the allAnswered guard
                # Pattern: function checkMiniQuizNNN(lnum) { ... }
                func_pattern = re.compile(
                    r'(function\s+checkMiniQuiz' + lnum + r'\s*\(\w+\)\s*\{)'  # function header
                    r'(.+?)'                                                      # body
                    r'(\n\})',                                                    # closing }
                    re.DOTALL
                )

                def replace_func(fm):
                    func_header = fm.group(1)
                    func_body = fm.group(2)
                    func_close = fm.group(3)

                    # Keep: box selection, groups selection, allAnswered check
                    # Replace: everything after allAnswered check
                    keep_pattern = re.compile(
                        r'^(.*?'
                        r'if\s*\(!allAnswered\)\s*\{[^}]+\})',
                        re.DOTALL
                    )
                    keep_m = keep_pattern.match(func_body)
                    if not keep_m:
                        return fm.group(0)

                    kept_part = keep_m.group(1)

                    new_body = kept_part + f"""

  // Collect answers and send to server for validation
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
    if (!res.success) {{
      alert('เกิดข้อผิดพลาด: ' + (res.message || 'Unknown error'));
      return;
    }}
    var score = res.score;
    var results = res.results;

    // Show per-question correct/incorrect highlighting
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
  }}).catch(function(e) {{ console.error('Quiz submit error:', e); }});
"""
                    return func_header + new_body + func_close

                new_body_text = func_pattern.sub(replace_func, body)
                if new_body_text != body:
                    return open_tag + new_body_text + close_tag
                return m.group(0)

            new_val = re.sub(
                r'(<script[^>]*>)(.*?)(</script>)',
                rewrite_script,
                val,
                flags=re.DOTALL
            )
            if new_val != val:
                cell['value'] = new_val
                changed = True
                print(f"  JS rewritten: lesson {lesson.id}")

        if changed:
            lesson.content = json.dumps(cells, ensure_ascii=False)
            js_updated += 1

    db.session.commit()
    print(f"\nDone: JS updated in {js_updated} lessons")
