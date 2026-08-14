import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    lesson = db.session.query(TutorialLesson).filter_by(id=164).first()
    if lesson:
        blocks = json.loads(lesson.content)
        print("=== BLOCK 14 ===")
        print(blocks[14].get('value'))
    else:
        print("Lesson 164 not found!")
