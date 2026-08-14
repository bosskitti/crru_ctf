import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        blocks = json.loads(l.content)
        for i, b in enumerate(blocks):
            if b.get("type") == "markdown":
                val = b.get("value", "")
                idx = val.find("Web Page Source Inspections")
                if idx != -1:
                    print(f"FOUND in Block {i} around index {idx}:")
                    print(val[idx:idx+400])
    else:
        print("Lesson 177 not found.")
