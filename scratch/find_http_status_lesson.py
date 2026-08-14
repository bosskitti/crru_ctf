from CTFd import create_app
from CTFd.models import Challenges

app = create_app()

with app.app_context():
    c = Challenges.query.filter_by(id=8).first()
    if c:
        print("Challenge 8 Description:")
        print(c.description)
