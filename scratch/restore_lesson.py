import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

try:
    original_content = open('/opt/CTFd/lesson_165_backup.txt').read()
    json.loads(original_content)
    print("Backup is valid JSON!")
    db.session.query(TutorialLesson).filter_by(id=165).update({'content': original_content})
    db.session.commit()
    print("Database restored successfully!")
except Exception as e:
    print("Restoration failed:", e)
