import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
with app.app_context():
    db = app.db
    l = TutorialLesson.query.get(166)
    if l:
        print(f"Lesson 166 Title: {l.title}")
        blocks = json.loads(l.content) if l.content else []
        print(f"Total blocks: {len(blocks)}")
        for i, b in enumerate(blocks):
            b_type = b.get('type')
            val = b.get('value', '')
            if b_type == 'challenge':
                print(f"Block {i}: [CHALLENGE] ID={val}")
            else:
                first_line = val.strip().split('\n')[0] if isinstance(val, str) else str(val)
                print(f"Block {i}: [MARKDOWN] Len={len(val)} | {first_line[:80]}")
