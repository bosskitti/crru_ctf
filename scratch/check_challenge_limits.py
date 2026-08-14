import sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
import importlib

app = create_app()

with app.app_context():
    # Dynamically import inside app context
    whale_models = importlib.import_module("CTFd.plugins.ctfd-whale.models")
    DynamicDockerChallenge = whale_models.DynamicDockerChallenge

    chals = DynamicDockerChallenge.query.all()
    print("=== Dynamic Docker Challenge Limits ===")
    for c in chals:
        print(f"ID: {c.id} | Name: {c.name} | Image: {c.docker_image} | Mem Limit: {c.memory_limit} | CPU Limit: {c.cpu_limit}")
