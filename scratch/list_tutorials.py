import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialModule, TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

# Inspect columns of TutorialModule
print("Module columns:", [c.name for c in TutorialModule.__table__.columns])
# Inspect columns of TutorialLesson
print("Lesson columns:", [c.name for c in TutorialLesson.__table__.columns])

# Print actual data
modules = db.session.query(TutorialModule).order_by(TutorialModule.id).all()
print("\n=== Modules ===")
for m in modules:
    print(f"Module ID: {m.id} | Title: {m.title}")

lessons = db.session.query(TutorialLesson).order_by(TutorialLesson.module_id, TutorialLesson.position).all()
print("\n=== Lessons ===")
for l in lessons:
    print(f"Lesson ID: {l.id} | Module ID: {l.module_id} | Title: {l.title} | Position: {l.position}")

ctx.pop()
