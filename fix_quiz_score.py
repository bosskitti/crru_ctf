import sys, re, json
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
app = create_app()
with app.app_context():
    from CTFd.models import db
    from CTFd.plugins.tutorials import TutorialLesson

    # Pattern to find quick_quiz fetch without score
    OLD = (
        r"body:\s*JSON\.stringify\(\{\s*"
        r"lesson_id:\s*(\d+),\s*"
        r"type:\s*'quiz',\s*"
        r"item_key:\s*'quick_quiz',\s*"
        r"solved:\s*true\s*"
        r"\}\)"
    )

    lessons = TutorialLesson.query.all()
    updated = 0

    for lesson in lessons:
        if not lesson.content:
            continue

        raw = lesson.content
        changed = False

        # Try parse as JSON array (cells)
        if raw.strip().startswith('['):
            try:
                cells = json.loads(raw)
                for cell in cells:
                    if cell.get('type') in ('markdown',) and cell.get('value'):
                        val = cell['value']
                        def replacer(m):
                            lid = m.group(1)
                            return (
                                "body: JSON.stringify({\n"
                                f"      lesson_id: {lid},\n"
                                "      type: 'quiz',\n"
                                "      item_key: 'quick_quiz',\n"
                                "      solved: true,\n"
                                "      score: score,\n"
                                "      total: groups.length\n"
                                "    })"
                            )
                        new_val = re.sub(OLD, replacer, val, flags=re.DOTALL)
                        if new_val != val:
                            cell['value'] = new_val
                            changed = True
                if changed:
                    lesson.content = json.dumps(cells, ensure_ascii=False)
                    updated += 1
                    print(f'Updated lesson {lesson.id}: {lesson.title[:60]}')
            except Exception as e:
                print(f'Error lesson {lesson.id}: {e}')
        else:
            # Plain markdown
            def replacer(m):
                lid = m.group(1)
                return (
                    "body: JSON.stringify({\n"
                    f"      lesson_id: {lid},\n"
                    "      type: 'quiz',\n"
                    "      item_key: 'quick_quiz',\n"
                    "      solved: true,\n"
                    "      score: score,\n"
                    "      total: groups.length\n"
                    "    })"
                )
            new_raw = re.sub(OLD, replacer, raw, flags=re.DOTALL)
            if new_raw != raw:
                lesson.content = new_raw
                updated += 1
                print(f'Updated plain lesson {lesson.id}: {lesson.title[:60]}')

    db.session.commit()
    print(f'Total updated: {updated}')
