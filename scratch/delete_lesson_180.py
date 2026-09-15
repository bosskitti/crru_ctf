import sys
sys.path.insert(0, "/opt/CTFd")
import json
import os
from CTFd import create_app
from CTFd.models import db
from CTFd.plugins.tutorials import TutorialLesson, TutorialQuizAnswer

app = create_app()
with app.app_context():
    lesson = TutorialLesson.query.get(180)
    if not lesson:
        print("[!] Lesson 180 not found!")
        sys.exit(0)

    print(f"[*] Found Lesson 180: '{lesson.title}' (module_id={lesson.module_id}, pos={lesson.position})")

    # Backup to json
    backup_path = "/opt/CTFd/lesson_180_deleted_backup.json"
    backup_data = {
        "id": lesson.id,
        "module_id": lesson.module_id,
        "title": lesson.title,
        "position": lesson.position,
        "content": lesson.content
    }
    with open(backup_path, "w", encoding="utf-8") as f:
        json.dump(backup_data, f, ensure_ascii=False, indent=2)
    print(f"[+] Backed up Lesson 180 to {backup_path}")

    # Delete quiz answers for lesson 180
    deleted_answers = TutorialQuizAnswer.query.filter_by(lesson_id=180).delete()
    print(f"[+] Deleted {deleted_answers} quiz answers for lesson 180")

    # Delete lesson 180
    db.session.delete(lesson)
    db.session.commit()
    print("[+] Successfully deleted Lesson 180 from database!")

    # Verify remaining lessons in Module 36
    remaining = TutorialLesson.query.filter_by(module_id=36).order_by(TutorialLesson.position.asc()).all()
    print("\n=== Remaining Lessons in Module 36 ===")
    for idx, l in enumerate(remaining):
        print(f"Index {idx} (URL Pos: {idx+1}) -> ID: {l.id:3d}, Pos: {l.position:2d}, Title: {l.title}")
