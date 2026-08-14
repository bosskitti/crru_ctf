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
original_count = len(blocks)

# Filter out empty blocks
filtered_blocks = [b for b in blocks if b.get('value', '').strip() != '']
new_count = len(filtered_blocks)

# Save and Commit
lesson.content = json.dumps(filtered_blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
db.session.commit()

print(f"Database upgraded: Removed {original_count - new_count} empty blocks. Remaining blocks: {new_count}.")
