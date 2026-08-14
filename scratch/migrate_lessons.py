import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l166 = db.session.query(TutorialLesson).filter_by(id=166).first()
l167 = db.session.query(TutorialLesson).filter_by(id=167).first()

b166 = json.loads(l166.content)
b167 = json.loads(l167.content)

# The content to move (Block 13 through 16 from Lesson 166)
# Block 13: separator (---)
# Block 14: Control Keys
# Block 15: Redirections & Env Vars
# Block 16: Regex & Wildcards
blocks_to_move = b166[13:]

# Keep only Block 0 to 12 in Lesson 166
b166_new = b166[:13]
l166.content = json.dumps(b166_new, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=166).update({"content": l166.content})

# Replace/Rebuild Lesson 167 blocks
# Let's create Lesson 167 with a clean header block followed by the moved high-fidelity blocks
header_block = {
    "type": "markdown",
    "value": "## 🛡️ การจัดการตัวแปร คีย์ควบคุม และ Regex ใน Linux (Linux Environment, Controls & Regex)"
}

b167_new = [header_block] + blocks_to_move
l167.content = json.dumps(b167_new, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=167).update({"content": l167.content})

db.session.commit()

print("Migration completed!")
print(f"Lesson 166 blocks: {len(b166_new)}")
print(f"Lesson 167 blocks: {len(b167_new)}")
