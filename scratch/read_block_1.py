import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l176 = db.session.query(TutorialLesson).filter_by(id=176).first()
blocks = json.loads(l176.content)
print(blocks[1]['value'])

ctx.pop()
