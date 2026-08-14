import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    # Read the updated HTML for block 14
    with open("/opt/CTFd/scratch/block14_updated.html", "r") as f:
        block14_html = f.read()

    # Query lesson 164
    lesson = db.session.query(TutorialLesson).filter_by(id=164).first()
    if lesson:
        blocks = json.loads(lesson.content)
        # Update Block 14
        blocks[14]['value'] = block14_html
        
        lesson.content = json.dumps(blocks, ensure_ascii=False)
        db.session.query(TutorialLesson).filter_by(id=164).update({"content": lesson.content})
        db.session.commit()
        print("Lesson 164 Block 14 updated successfully with the 4-question high school quiz!")
    else:
        print("Error: Lesson 164 not found in database!")
