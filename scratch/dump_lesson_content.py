import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()

lesson = app.db.session.query(TutorialLesson).filter_by(id=165).first()
if lesson:
    with open("/opt/CTFd/lesson_165_dump.json", "w", encoding="utf-8") as f:
        f.write(lesson.content)
    print("Lesson content dumped successfully to /opt/CTFd/lesson_165_dump.json")
else:
    print("Lesson not found!")
