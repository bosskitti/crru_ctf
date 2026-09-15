import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
with app.app_context():
    db = app.db
    l = TutorialLesson.query.get(166)
    blocks = json.loads(l.content) if l.content else []
    for i in [2, 5, 8, 10]:
        print(f"Block {i} dict: {blocks[i]}")
