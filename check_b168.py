from CTFd import create_app
from CTFd.models import db
from CTFd.plugins.tutorials import TutorialLesson
import json

app = create_app()
with app.app_context():
    l168 = db.session.query(TutorialLesson).filter_by(id=168).first()
    b168 = json.loads(l168.content)

    # If b168 contains b_layers and b_tree in old cells or we extract them:
    # Let's inspect if b168 currently has b_layers or if we need to load from a backup or recreate
    # Let's check:
    print("Total current cells in b168:", len(b168))
