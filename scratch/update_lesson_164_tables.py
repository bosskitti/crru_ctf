import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    # Read the updated HTML for block 5
    with open("/opt/CTFd/scratch/block5_updated.html", "r") as f:
        block5_html = f.read()

    # Read the updated HTML for block 7
    with open("/opt/CTFd/scratch/block7_updated.html", "r") as f:
        block7_html = f.read()

    # Query lesson 164
    lesson = db.session.query(TutorialLesson).filter_by(id=164).first()
    if lesson:
        blocks = json.loads(lesson.content)
        # Update Block 5
        blocks[5]['value'] = block5_html
        # Update Block 7
        blocks[7]['value'] = block7_html
        
        lesson.content = json.dumps(blocks, ensure_ascii=False)
        db.session.query(TutorialLesson).filter_by(id=164).update({"content": lesson.content})
        db.session.commit()
        print("Lesson 164 Blocks 5 and 7 updated successfully with the beautiful graphical tables!")
    else:
        print("Error: Lesson 164 not found in database!")
