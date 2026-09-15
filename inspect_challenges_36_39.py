import json
from CTFd import create_app
from CTFd.models import Challenges, Flags

app = create_app()
with app.app_context():
    db = app.db
    for cid in [36, 37, 38, 39]:
        ch = Challenges.query.get(cid)
        flags = Flags.query.filter_by(challenge_id=cid).all()
        flag_strs = [f.content for f in flags]
        print(f"\n=== Challenge {cid} ===")
        print(f"Name: {ch.name if ch else 'None'}")
        print(f"Category: {ch.category if ch else 'None'}")
        print(f"Value: {ch.value if ch else 'None'}")
        print(f"Flags: {flag_strs}")
        print(f"Description:\n{ch.description if ch else 'None'}")
