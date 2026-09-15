import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson, TutorialModule

app = create_app()
with app.app_context():
    db = app.db
    print("=== MODULES ===")
    modules = db.session.query(TutorialModule).order_by(TutorialModule.position.asc(), TutorialModule.id.asc()).all()
    for m in modules:
        print(f"Module ID: {m.id}, Pos: {m.position}, Category: {m.category}, Title: {m.title}")
        
    print("\n=== LESSONS IN ALL MODULES ===")
    for m in modules:
        print(f"\n--- Module {m.id}: {m.title} ---")
        lessons = m.lessons.all()
        for l in lessons:
            print(f"  Lesson ID: {l.id}, Pos: {l.position}, Title: {l.title}")
