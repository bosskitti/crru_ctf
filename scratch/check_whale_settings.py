import sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
from CTFd.models import db, Configs

app = create_app()

with app.app_context():
    configs = Configs.query.filter(Configs.key.like('%whale%')).all()
    print("=== CTFd-Whale Configs ===")
    for c in configs:
        print(f"{c.key}: {c.value}")
