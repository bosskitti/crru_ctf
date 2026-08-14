import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    lessons = TutorialLesson.query.all()
    for l in lessons:
        try:
            blocks = json.loads(l.content)
            for i, b in enumerate(blocks):
                val = b.get("value", "")
                if "Sub-Trees" in val or "Important Files" in val or "passwd" in val or "etc/passwd" in val:
                    print(f"FOUND in Lesson {l.id} Block {i}:")
                    # print first 200 chars of match
                    idx = val.find("passwd") if "passwd" in val else val.find("Sub-Trees")
                    print(val[max(0, idx-100):idx+300])
                    print("-" * 50)
        except Exception as e:
            pass
