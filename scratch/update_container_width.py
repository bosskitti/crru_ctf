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

# Replace max-width:820px inside .os-layers-container back to max-width:500px
# Let's target specifically the container's CSS rule:
# ".os-layers-container{width:100%;max-width:820px;"
target_str = ".os-layers-container{width:100%;max-width:820px;"
replacement_str = ".os-layers-container{width:100%;max-width:500px;"

if target_str in val_3:
    modified_val_3 = val_3.replace(target_str, replacement_str)
else:
    # If the spacing was slightly different, let's search more generally
    print("Warning: Direct container string match not found, performing search and replace...")
    # Find the first occurrences of max-width:820px which corresponds to container
    # Since there are two: .os-layers-container and .os-layers-desc-panel
    # We will replace only the one associated with .os-layers-container
    modified_val_3 = val_3.replace(".os-layers-container{width:100%;max-width:820px;", ".os-layers-container{width:100%;max-width:500px;")

block_3['value'] = modified_val_3
blocks[3] = block_3

# Save and Commit database
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=164).update({"content": lesson.content})
db.session.commit()
print("Successfully changed cards container width back to 500px while keeping description panel at 820px!")
