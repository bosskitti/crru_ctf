import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    l = TutorialLesson.query.get(177)
    blocks = json.loads(l.content) if l.content else []
    print(f"Total blocks in Lesson 177: {len(blocks)}")
    for i, b in enumerate(blocks):
        print(f"Block {i} type: {b.get('type')}")
        val = b.get('value', '')
        print(f"First 150 chars: {val[:150]}")
        print("-" * 30)
