import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    l = TutorialLesson.query.get(179)
    blocks = json.loads(l.content) if l.content else []
    print(f"Total blocks in Lesson 179: {len(blocks)}")
    val = blocks[0].get('value', '')
    keywords = ["XSStrike", "hydra -l", "File Inclusion Attacks", "LFI Common Payloads", "requests.post"]
    missing = [k for k in keywords if k not in val]
    if not missing:
        print("Verification SUCCESS: All Lesson 179 content verified successfully in database!")
    else:
        print(f"Verification FAILURE: Missing keywords in database: {missing}")
