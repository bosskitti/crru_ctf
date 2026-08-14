from CTFd import create_app
from CTFd.models import Challenges, Flags

app = create_app()

with app.app_context():
    challs = Challenges.query.all()
    print("CHALLENGES LIST:")
    for c in challs:
        print(f"ID: {c.id} | Name: {c.name} | Type: {c.type} | Category: {c.category} | State: {c.state}")
        # Get flags for this challenge
        flags = Flags.query.filter_by(challenge_id=c.id).all()
        for f in flags:
            print(f"  -> Flag ID: {f.id} | Type: {f.type} | Content: {f.content}")
        
        # If it's a whale challenge, show its image config if possible
        if c.type == "whale":
            try:
                from CTFd.plugins.ctfd_whale.models import WhaleContainer
                container = WhaleContainer.query.filter_by(challenge_id=c.id).first()
                if container:
                    print(f"  -> Whale Image: {container.image}")
            except Exception:
                # Alternatively, whale might use a different model
                pass
            try:
                from CTFd.plugins.ctfd_whale.models import WhaleChallenge
                wc = WhaleChallenge.query.filter_by(id=c.id).first()
                if wc:
                    print(f"  -> WhaleChallenge config: Image={wc.image} | Port={wc.inner_port}")
            except Exception as e:
                print(f"  -> WhaleChallenge query error: {e}")
