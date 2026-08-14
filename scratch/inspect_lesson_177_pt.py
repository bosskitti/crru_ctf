import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    l = TutorialLesson.query.get(177)
    blocks = json.loads(l.content) if l.content else []
    for idx in range(4, 11):
        if idx < len(blocks):
            print(f"=== BLOCK {idx} ({blocks[idx].get('type')}) ===")
            print(blocks[idx].get('value', ''))
            print("=" * 60)
