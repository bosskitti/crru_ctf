import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    lesson = db.session.query(TutorialLesson).filter_by(id=164).first()
    if lesson:
        blocks = json.loads(lesson.content)
        print("=== BLOCK 11 ===")
        print(blocks[11].get('value'))
        print("\n=== BLOCK 13 ===")
        print(blocks[13].get('value'))
    else:
        print("Lesson 164 not found!")
