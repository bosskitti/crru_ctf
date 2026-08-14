import sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
app = create_app()

with app.app_context():
    from CTFd.models import db, Challenges

    # Convert Challenges 37, 38, 39 to standard challenges
    for cid in [37, 38, 39]:
        c = Challenges.query.get(cid)
        if c:
            c.type = 'standard'
            db.session.add(c)
    
    db.session.commit()
    print("Successfully converted Challenges 37, 38, 39 to standard challenges!")
