import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

# Query lesson 164
lesson = db.session.query(TutorialLesson).filter_by(id=164).first()
if not lesson:
    print("Lesson not found!")
    exit(1)

blocks = json.loads(lesson.content)
block_3 = blocks[3]
val_3 = block_3['value']

# Replace max-width:500px with max-width:820px
modified_val_3 = val_3.replace("max-width:500px", "max-width:820px")

block_3['value'] = modified_val_3
blocks[3] = block_3

# Save and Commit database
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=164).update({"content": lesson.content})
db.session.commit()
print("Successfully expanded the second diagram and description panel to 820px!")
