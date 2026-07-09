import sys
import importlib
from CTFd import create_app

app = create_app()
with app.app_context():
    try:
        control_module = importlib.import_module("CTFd.plugins.ctfd-whale.utils.control")
        ControlUtil = control_module.ControlUtil
    except Exception as e:
        print(f"Error importing ControlUtil: {e}")
        sys.exit(1)

    print("Attempting to spawn SQLi container for user 2, challenge 7...")
    success, message = ControlUtil.try_add_container(user_id=2, challenge_id=7)
    print(f"Success: {success}, Message: {message}")

    if success:
        whale_models = importlib.import_module("CTFd.plugins.ctfd-whale.models")
        WhaleContainer = whale_models.WhaleContainer
        container = WhaleContainer.query.filter_by(user_id=2, challenge_id=7).first()
        if container:
            print(f"Container created with port: {container.port}, flag: {container.flag}, uuid: {container.uuid}")
            print(f"User access: {container.user_access}")
