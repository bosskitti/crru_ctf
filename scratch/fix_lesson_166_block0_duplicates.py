import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    lesson = db.session.query(TutorialLesson).filter_by(id=166).first()
    if lesson:
        blocks = json.loads(lesson.content)
        val = blocks[0]['value']
        
        # The duplicated block starts with this HTML pattern (the terminal card div)
        # Find where the second copy starts and cut everything from there
        MARKER = '<div style="background: #0b0f19; border: 1px solid rgba(0, 240, 255, 0.15);'
        
        first_idx = val.find(MARKER)
        if first_idx == -1:
            print("Marker not found!")
        else:
            # Find the second occurrence
            second_idx = val.find(MARKER, first_idx + 1)
            if second_idx == -1:
                print("No duplicate found — already clean!")
            else:
                # Keep only everything before the second occurrence
                clean_val = val[:second_idx].rstrip()
                blocks[0]['value'] = clean_val
                lesson.content = json.dumps(blocks, ensure_ascii=False)
                db.session.query(TutorialLesson).filter_by(id=166).update({"content": lesson.content})
                db.session.commit()
                print(f"Fixed! Removed duplicates. Original length: {len(val)}, Clean length: {len(clean_val)}")
    else:
        print("Lesson 166 not found!")
