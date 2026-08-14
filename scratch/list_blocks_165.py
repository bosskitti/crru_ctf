import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    lesson = db.session.query(TutorialLesson).filter_by(id=165).first()
    if lesson:
        blocks = json.loads(lesson.content)
        print(f"Total blocks in Lesson 165: {len(blocks)}")
        for i, b in enumerate(blocks):
            val = b.get('value', '')
            print(f"Block {i}: type={b.get('type')} length={len(val)} snippet={val[:100].replace(chr(10), ' ')}")
    else:
        print("Lesson 165 not found!")
