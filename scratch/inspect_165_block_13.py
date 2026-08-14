import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=165).first()
    if l:
        blocks = json.loads(l.content)
        print("Lesson 165 Block 13:")
        print(blocks[13]["value"])
    else:
        print("Lesson 165 not found.")
