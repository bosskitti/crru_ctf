import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    lesson = db.session.query(TutorialLesson).filter_by(id=164).first()
    if lesson:
        blocks = json.loads(lesson.content)
        # Write Block 3 value to a temporary text file so we can view/edit it easily
        with open("/opt/CTFd/scratch/block3_content.txt", "w") as f:
            f.write(blocks[3]['value'])
        print("Block 3 content exported to /opt/CTFd/scratch/block3_content.txt")
    else:
        print("Lesson not found!")
