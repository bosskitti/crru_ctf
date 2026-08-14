import sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
from CTFd.models import db, Configs
import importlib

app = create_app()

with app.app_context():
    # Dynamic import of Whale models due to hyphen in path inside app context
    whale_models = importlib.import_module("CTFd.plugins.ctfd-whale.models")
    DynamicDockerChallenge = whale_models.DynamicDockerChallenge

    # 1. Update all DynamicDockerChallenge CPU limits to 0.2
    # This prevents students' brute force or scanner scripts from hogging the host CPU
    db.session.execute("UPDATE dynamic_docker_challenge SET cpu_limit = 0.2")
    print("Updated all challenge CPU limits to 0.2")
    
    # 2. Optimize container lifetimes in Whale Configs
    # Reduce timeout from 1 hour (3600s) to 30 minutes (1800s) to clean up unused containers faster
    timeout_cfg = Configs.query.filter_by(key="whale:docker_timeout").first()
    if timeout_cfg:
        timeout_cfg.value = "1800"
        print("Updated whale:docker_timeout to 1800 seconds")
    else:
        # Insert if it doesn't exist
        db.session.add(Configs(key="whale:docker_timeout", value="1800"))
        print("Created and set whale:docker_timeout to 1800 seconds")

    db.session.commit()
    print("Database committed successfully!")
