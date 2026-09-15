import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson, TutorialModule

app = create_app()
with app.app_context():
    db = app.db
    # Modules 32, 33, 34, 35, 36
    modules = db.session.query(TutorialModule).filter(TutorialModule.id.in_([32, 33, 34, 35, 36])).all()
    for m in modules:
        print(f"\n==========================================")
        print(f"MODULE {m.id}: {m.title}")
        print(f"==========================================")
        for l in m.lessons.all():
            has_stickers = "stickers/" in (l.content or "")
            has_mascots = "kid_" in (l.content or "") or "skill_" in (l.content or "")
            blocks_count = len(json.loads(l.content)) if l.content else 0
            print(f"  Lesson {l.id} (Pos {l.position}): {l.title[:45]} | Blocks: {blocks_count} | Mascots: {has_mascots} | Stickers: {has_stickers}")
