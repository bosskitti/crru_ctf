import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    l = TutorialLesson.query.get(178)
    blocks = json.loads(l.content) if l.content else []
    print(f"Total blocks in Lesson 178: {len(blocks)}")
    val = blocks[0].get('value', '')
    if "sqlmap" in val.lower() and "Stealing Data" in val:
        print("Verification SUCCESS: New SQL Injection and SQLMap content found in database!")
    else:
        print("Verification FAILURE: Expected keywords not found in database.")
