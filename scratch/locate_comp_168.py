import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l168 = db.session.query(TutorialLesson).filter_by(id=168).first()
blocks = json.loads(l168.content)

# ─── Find block comparison index (it should be index 19 in the new 23-block list of Lesson 168) ───
# Let's write code to verify and rewrite comparison block
print("Current Blocks of restructuring 168:")
for idx, b in enumerate(blocks):
    val = b.get("value", "")
    fl = val.split("\n")[0] if val else ""
    print(f"  {idx}: {fl[:60]}")
