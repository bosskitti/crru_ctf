import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with open("/opt/CTFd/lesson_177_block_0.txt", "r", encoding="utf-8") as f:
    backup_value = f.read()

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        blocks = json.loads(l.content)
        blocks[0]["value"] = backup_value
        l.content = json.dumps(blocks, ensure_ascii=False)
        app.db.session.commit()
        print("Successfully restored Lesson 177 Block 0 to the exact 2 AM backup version!")
    else:
        print("Error: Lesson 177 not found in DB.")
