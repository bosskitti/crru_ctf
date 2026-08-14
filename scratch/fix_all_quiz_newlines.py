import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    lessons = app.db.session.query(TutorialLesson).all()
    updated_count = 0
    for l in lessons:
        if not l.content:
            continue
        try:
            blocks = json.loads(l.content)
            modified = False
            for b in blocks:
                val = b.get("value", "")
                # Check for literal backslash-n
                if "\\n" in val:
                    val = val.replace("\\n", "\n")
                    b["value"] = val
                    modified = True
            
            if modified:
                l.content = json.dumps(blocks, ensure_ascii=False)
                updated_count += 1
                print(f"Successfully cleaned quiz newlines in Lesson {l.id}: '{l.title}'")
        except Exception as e:
            print(f"Error processing Lesson {l.id}: {e}")
            
    if updated_count > 0:
        app.db.session.commit()
        print(f"Total lessons updated: {updated_count}")
    else:
        print("No lessons with literal newline leaks were found or updated.")
