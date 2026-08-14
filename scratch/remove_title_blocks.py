import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

# Query lesson 165
lesson = db.session.query(TutorialLesson).filter_by(id=165).first()
if not lesson:
    print("Lesson not found!")
    exit(1)

blocks = json.loads(lesson.content)

# Clear redundant slide title blocks (set to empty strings so they don't render)
redundant_title_indices = [0, 2, 4, 6, 8, 10, 22, 38, 40, 42]

for idx in redundant_title_indices:
    if idx < len(blocks):
        blocks[idx]['value'] = ""

# Save and Commit
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
db.session.commit()
print("All duplicate slide title blocks cleared successfully!")
