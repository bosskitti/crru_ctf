import sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
from CTFd.models import db
import importlib

app = create_app()

with app.app_context():
    # Dynamic import
    whale_models = importlib.import_module("CTFd.plugins.ctfd-whale.models")
    WhaleContainer = whale_models.WhaleContainer

    containers = WhaleContainer.query.all()
    print("=== Registered Whale Containers in DB ===")
    for c in containers:
        print(f"ID: {c.id} | User: {c.user_id} | Chall: {c.challenge_id} | UUID: {c.uuid} | Start: {c.start_time}")
