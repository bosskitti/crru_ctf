import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    lesson = db.session.query(TutorialLesson).filter_by(id=165).first()
    if lesson:
        blocks = json.loads(lesson.content)
        question_blocks = [b for b in blocks if b.get('type') == 'question']
        print(f"Number of question blocks: {len(question_blocks)}")
        for i, qb in enumerate(question_blocks):
            print(f"\n--- QUESTION BLOCK {i} ---")
            print(json.dumps(qb, indent=2, ensure_ascii=False))
    else:
        print("Lesson 165 not found!")
