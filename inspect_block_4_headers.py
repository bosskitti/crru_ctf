import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        blocks = json.loads(l.content)
        val = blocks[4]["value"]
        print("Block 4 Headers:")
        import re
        headers = re.findall(r"### .*", val)
        for h in headers:
            print("  ", h)
    else:
        print("Lesson 177 not found.")
