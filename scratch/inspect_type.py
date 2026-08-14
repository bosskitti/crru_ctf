import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

for lid in range(177, 185):
    l = db.session.query(TutorialLesson).filter_by(id=lid).first()
    if l:
        print(f"--- Lesson {lid} ---")
        print("Type of content:", type(l.content))
        try:
            val = json.loads(l.content)
            print("Is JSON! Number of elements:", len(val))
        except Exception as e:
            print("Is NOT JSON! Length:", len(l.content) if l.content else 0)
            print("Snippet:", l.content[:200] if l.content else "")

ctx.pop()
