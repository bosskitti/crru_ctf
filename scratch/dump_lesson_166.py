import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    lesson = db.session.query(TutorialLesson).filter_by(id=166).first()
    if lesson:
        blocks = json.loads(lesson.content)
        print(f"Total blocks: {len(blocks)}")
        for i, b in enumerate(blocks):
            val = b.get('value', '')
            print(f"\n--- Block {i} (type={b.get('type','?')}) ---")
            print(val[:300])
            print("...")
    else:
        print("Lesson 166 not found!")
