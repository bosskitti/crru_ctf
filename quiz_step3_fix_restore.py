"""
Step 3: Fix remaining data-correct references in setTimeout restore blocks.
Replace: var correctVal = g.getAttribute('data-correct'); ... if (val === correctVal) ...
With: just lock all options (no correct answer highlight on restore - answers stay hidden)
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
            if "data-correct" not in val:
                continue

            def fix_script(m):
                open_tag = m.group(1)
                body = m.group(2)
                close_tag = m.group(3)

                if "data-correct" not in body:
                    return m.group(0)

                # Replace the groups.forEach in setTimeout that uses data-correct
                # Old pattern:
                #   groups.forEach(function(g) {
                #     var correctVal = g.getAttribute('data-correct');
                #     g.querySelectorAll('.mini-opt').forEach(function(o) {
                #       var val = o.getAttribute('data-val');
                #       if (val === correctVal) {
                #         o.classList.add('selected', 'correct');
                #       }
                #       o.style.pointerEvents = 'none';
                #     });
                #   });
                OLD = re.compile(
                    r"groups\.forEach\(function\(g\)\s*\{"
                    r".*?var correctVal\s*=\s*g\.getAttribute\('data-correct'\);"
                    r".*?g\.querySelectorAll\('\.mini-opt'\)\.forEach\(function\(o\)\s*\{"
                    r".*?if\s*\(val\s*===\s*correctVal\)\s*\{"
                    r".*?o\.classList\.add\('selected',\s*'correct'\);"
                    r".*?\}"
                    r".*?o\.style\.pointerEvents\s*=\s*'none';"
                    r".*?\}\);"
                    r".*?\}\);",
                    re.DOTALL
                )

                NEW = (
                    "groups.forEach(function(g) {\n"
                    "      // Answers are stored server-side; just lock options on restore\n"
                    "      g.querySelectorAll('.mini-opt').forEach(function(o) {\n"
                    "        o.style.pointerEvents = 'none';\n"
                    "        o.style.opacity = '0.7';\n"
                    "      });\n"
                    "    });"
                )

                new_body = OLD.sub(NEW, body)
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
                print(f"  Fixed restore block: lesson {lesson.id}")

        if changed:
            lesson.content = json.dumps(cells, ensure_ascii=False)
            fixed += 1

    db.session.commit()
    print(f"\nDone: {fixed} lessons fixed")

    # Final verification
    print("\n--- Final check (should be 0) ---")
    lessons2 = TutorialLesson.query.all()
    total_remaining = 0
    for lesson in lessons2:
        if not lesson.content:
            continue
        raw = lesson.content
        if not raw.strip().startswith('['):
            continue
        try:
            cells = json.loads(raw)
        except Exception:
            continue
        for cell in cells:
            val = cell.get('value', '')
            count = len(re.findall(r'data-correct', val))
            if count:
                print(f"  STILL has data-correct: lesson {lesson.id} ({count} occurrences)")
                total_remaining += count
    if total_remaining == 0:
        print("  All clear! No data-correct left in HTML.")
