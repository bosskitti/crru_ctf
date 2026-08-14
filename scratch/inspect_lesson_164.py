import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    lesson = db.session.query(TutorialLesson).filter_by(id=164).first()
    if lesson:
        blocks = json.loads(lesson.content)
        for i, b in enumerate(blocks):
            print(f"Block {i} type: {b.get('type')}")
            # Print first 200 chars of value if text/html
            val = b.get('value', '')
            print(f"  Snippet: {val[:200]}")
    else:
        print("Lesson not found!")
