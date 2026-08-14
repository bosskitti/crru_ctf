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

# 1. Update Block 5 (Architecture Blueprint)
# Change max-width:820px to max-width:100%
blocks[5]['value'] = blocks[5]['value'].replace(
    "max-width:820px;", "max-width:100%;"
).replace(
    "max-width: 820px;", "max-width: 100%;"
)

# 2. Update Block 11 (Directory Tree)
blocks[11]['value'] = blocks[11]['value'].replace(
    "max-width:820px;", "max-width:100%;"
).replace(
    "max-width: 820px;", "max-width: 100%;"
)

# 3. Update Block 13 (5 Flat-Tree Sub-trees)
blocks[13]['value'] = blocks[13]['value'].replace(
    "max-width:820px;", "max-width:100%;"
).replace(
    "max-width: 820px;", "max-width: 100%;"
).replace(
    "max-width:500px;", "max-width:none;"
).replace(
    "max-width: 500px;", "max-width: none;"
)

# 4. Update Block 15 (User Accounts Cards)
blocks[15]['value'] = blocks[15]['value'].replace(
    "max-width:820px;", "max-width:100%;"
).replace(
    "max-width: 820px;", "max-width: 100%;"
)

# Save and Commit
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
db.session.commit()

print("All container widths expanded to 100% successfully!")
