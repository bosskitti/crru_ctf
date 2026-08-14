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
        filename = f"/tmp/lesson_{lid}_raw.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(l.content)
        print(f"Extracted Lesson {lid} to {filename}")

ctx.pop()
