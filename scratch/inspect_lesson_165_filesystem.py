import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    lesson = db.session.query(TutorialLesson).filter_by(id=165).first()
    if lesson:
        blocks = json.loads(lesson.content)
        print("=== BLOCK 7 ===")
        print(blocks[7].get('value'))
        print("\n=== BLOCK 9 ===")
        print(blocks[9].get('value'))
        print("\n=== BLOCK 11 ===")
        print(blocks[11].get('value'))
    else:
        print("Lesson 165 not found!")
