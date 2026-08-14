import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        blocks = json.loads(l.content)
        val = blocks[0]["value"]
        
        # Search for target header
        target = "รหัสสถานะตอบรับการสื่อสาร"
        idx = val.find(target)
        if idx != -1:
            print("FOUND! Around index:", idx)
            print("--- CONTEXT ---")
            print(val[max(0, idx-500):idx+1000])
        else:
            print("NOT FOUND!")
