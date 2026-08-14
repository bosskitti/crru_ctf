from CTFd import create_app
from CTFd.models import Challenges

app = create_app()

with app.app_context():
    for cid in [21, 22, 23]:
        c = Challenges.query.get(cid)
        print(f"--- ID: {cid} | Name: {c.name} ---")
        print(c.description)
        print("\n")
