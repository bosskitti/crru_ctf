import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        blocks = json.loads(l.content)
        val = blocks[0]["value"]
        
        target = "รหัสสถานะตอบรับการสื่อสาร"
        idx = val.find(target)
        if idx != -1:
            # Let's find the closing </table> or </div> after idx
            # Actually let's search for "---" or "###" after target
            next_separator = val.find("---", idx + len(target))
            next_header = val.find("###", idx + len(target))
            print("Next separator index:", next_separator)
            print("Next header index:", next_header)
            
            # Print content between target and next separator/header
            end_idx = min(next_separator if next_separator != -1 else len(val), next_header if next_header != -1 else len(val))
            print("--- SECTION CONTENT ---")
            print(val[idx:end_idx + 100])
        else:
            print("NOT FOUND!")
