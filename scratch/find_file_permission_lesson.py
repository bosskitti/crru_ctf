import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    # Find lesson 03 - Linux File & Permission Commands
    lessons = db.session.query(TutorialLesson).all()
    for l in lessons:
        if 'Permission' in l.title or 'permission' in l.title or 'File' in l.title or 'คำสั่ง' in (l.title or ''):
            print(f"ID: {l.id} | Title: {l.title}")
