import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    lesson = db.session.query(TutorialLesson).filter_by(id=165).first()
    if lesson:
        blocks = json.loads(lesson.content)
        with open("/opt/CTFd/block20_full.txt", "w", encoding="utf-8") as f:
            f.write(blocks[20]['value'])
        print("Written block 20 to /opt/CTFd/block20_full.txt")
    else:
        print("Lesson 165 not found!")
