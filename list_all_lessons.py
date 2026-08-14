import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    lessons = TutorialLesson.query.all()
    for l in lessons:
        try:
            blocks = json.loads(l.content) if l.content else []
            print(f"ID: {l.id} | Title: {l.title} | Blocks: {len(blocks)}")
        except Exception as e:
            print(f"ID: {l.id} | Title: {l.title} | Error: {e}")
