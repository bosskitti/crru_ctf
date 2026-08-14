import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        blocks = json.loads(l.content)
        val = blocks[0]["value"]
        print("Block 0 Length:", len(val))
        print("Last 1000 chars of Block 0:")
        print(val[-1000:])
    else:
        print("Lesson 177 not found.")
