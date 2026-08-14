import sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
import importlib

app = create_app()

with app.app_context():
    # Dynamic imports
    whale_models = importlib.import_module("CTFd.plugins.ctfd-whale.models")
    whale_control = importlib.import_module("CTFd.plugins.ctfd-whale.utils.control")
    
    WhaleContainer = whale_models.WhaleContainer
    ControlUtil = whale_control.ControlUtil

    containers = WhaleContainer.query.all()
    print(f"Found {len(containers)} active containers in the database.")
    
    for c in containers:
        user_id = c.user_id
        chall_id = c.challenge_id
        uuid = c.uuid
        print(f"Destroying container for User {user_id} (Chall {chall_id}, UUID {uuid})...")
        try:
            ok, msg = ControlUtil.try_remove_container(user_id)
            print(f"  Result: {ok} - {msg}")
        except Exception as e:
            print(f"  Error destroying container for user {user_id}: {e}")

    # Double check if there are any left in the DB
    leftovers = WhaleContainer.query.all()
    if leftovers:
        print(f"Warning: {len(leftovers)} containers still remain in the database. Cleaning them up manually from DB...")
        for c in leftovers:
            db.session.delete(c)
        db.session.commit()
        print("Database cleared of all leftover container records.")
    else:
        print("All containers successfully cleared.")
