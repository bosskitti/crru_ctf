import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    lesson = db.session.query(TutorialLesson).filter_by(id=166).first()
    if lesson:
        blocks = json.loads(lesson.content)
        # Dump blocks 0, 3, 5, 6, 10 to files for inspection
        for i in [0, 3, 5, 6, 10]:
            with open(f"/opt/CTFd/block{i}_l166.txt", "w") as f:
                f.write(blocks[i]['value'])
            print(f"Written block {i} ({len(blocks[i]['value'])} bytes)")
    else:
        print("Not found")
