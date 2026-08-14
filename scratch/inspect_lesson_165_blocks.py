import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    lesson = db.session.query(TutorialLesson).filter_by(id=165).first()
    if lesson:
        blocks = json.loads(lesson.content)
        print(f"Lesson 165 has {len(blocks)} blocks.")
        for idx, block in enumerate(blocks):
            print(f"Block {idx} (type {block.get('type')}): {str(block.get('value'))[:120]}...")
    else:
        print("Lesson 165 not found!")
