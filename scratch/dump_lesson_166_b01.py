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
        # Write block 0 and 1 full content to file
        with open("/opt/CTFd/block0_full.txt", "w") as f:
            f.write(f"=== BLOCK 0 ===\n{blocks[0]['value']}\n\n=== BLOCK 1 ===\n{blocks[1]['value']}")
        print("Written blocks 0 and 1")
    else:
        print("Not found")
