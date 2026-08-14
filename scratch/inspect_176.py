import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l176 = db.session.query(TutorialLesson).filter_by(id=176).first()
blocks = json.loads(l176.content)
print("Number of blocks in Lesson 176:", len(blocks))
for idx, b in enumerate(blocks):
    print(f"--- Block {idx} (Type: {b.get('type')}) ---")
    print(b.get('value')[:300])

ctx.pop()
