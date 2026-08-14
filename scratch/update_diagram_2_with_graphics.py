import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    # Read the updated HTML content
    with open("/opt/CTFd/scratch/block3_updated.html", "r") as f:
        new_html = f.read()

    # Query lesson 164
    lesson = db.session.query(TutorialLesson).filter_by(id=164).first()
    if lesson:
        blocks = json.loads(lesson.content)
        # Update Block 3's value
        blocks[3]['value'] = new_html
        
        lesson.content = json.dumps(blocks, ensure_ascii=False)
        db.session.query(TutorialLesson).filter_by(id=164).update({"content": lesson.content})
        db.session.commit()
        print("Lesson 164 Block 3 updated successfully with the side-by-side graphical layout!")
    else:
        print("Error: Lesson 164 not found in database!")
