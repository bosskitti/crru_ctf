import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson
from CTFd.models import Challenges

app = create_app()
with app.app_context():
    db = app.db
    l = TutorialLesson.query.get(166)
    blocks = json.loads(l.content) if l.content else []
    for i, b in enumerate(blocks):
        if b.get('type') == 'challenge':
            cid = b.get('value')
            ch = Challenges.query.get(cid) if cid else None
            print(f"Block {i}: Challenge ID={cid}, Name={ch.name if ch else 'Unknown'}, Category={ch.category if ch else ''}")
        else:
            print(f"\n--- Block {i} (len {len(b.get('value',''))}) ---")
            print(b.get('value','')[:200])
