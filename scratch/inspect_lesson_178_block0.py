import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    l = TutorialLesson.query.get(178)
    blocks = json.loads(l.content) if l.content else []
    if blocks:
        print(blocks[0].get('value', ''))
