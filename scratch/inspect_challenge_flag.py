import json
from CTFd import create_app
from CTFd.models import Challenges, Flags

app = create_app()

with app.app_context():
    # Find the challenge by name
    chall = Challenges.query.filter_by(name="Web Parameter Tampering (Privilege Escalation)").first()
    if chall:
        print(f"Challenge found: ID={chall.id}, Name={chall.name}")
        # Find flags for this challenge
        flags = Flags.query.filter_by(challenge_id=chall.id).all()
        print(f"Number of flags: {len(flags)}")
        for f in flags:
            print(f"  Flag: ID={f.id}, Content={f.content}, Type={f.type}")
    else:
        print("Challenge not found.")
