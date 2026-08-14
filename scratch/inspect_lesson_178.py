import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    l = TutorialLesson.query.get(178)
    blocks = json.loads(l.content) if l.content else []
    print(f"Total blocks in Lesson 178: {len(blocks)}")
    for i, b in enumerate(blocks):
        print(f"Block {i} type: {b.get('type')}")
        val = b.get('value', '')
        print(f"First 300 chars: {val[:300]}")
        print("-" * 30)
