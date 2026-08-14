"""
Restore Lesson 177 Block 0 to the exact baseline state saved in
/home/kali/crru_ctf/CTFd/lesson_177_block_0.txt before any graphic edits.
"""
import json, sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app

app = create_app()

# Read the clean baseline file from /opt/CTFd/lesson_177_block_0.txt inside the container
try:
    with open('/opt/CTFd/lesson_177_block_0.txt') as f:
        baseline_content = f.read()
except FileNotFoundError:
    print("[!] Failed to locate lesson_177_block_0.txt backup inside container path /opt/CTFd/")
    sys.exit(1)

with app.app_context():
    from CTFd.plugins.tutorials import TutorialLesson
    db = app.db
    lesson = db.session.query(TutorialLesson).filter_by(id=177).first()
    if lesson:
        blocks = json.loads(lesson.content)
        blocks[0]["value"] = baseline_content
        lesson.content = json.dumps(blocks, ensure_ascii=False)
        db.session.commit()
        print("[OK] Lesson 177 Block 0 successfully restored to the exact original layout!")
    else:
        print("[!] Lesson 177 not found in DB")
