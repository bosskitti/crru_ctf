import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        blocks = json.loads(l.content)
        val = blocks[2]["value"]
        print("Slice of Block 2:")
        print(val[33000:33500])
    else:
        print("Lesson 177 not found.")
