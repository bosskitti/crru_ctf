import sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
from CTFd.models import db

app = create_app()

with app.app_context():
    # Use raw SQL to fetch from the dynamic_docker_challenge table which has memory_limit and cpu_limit
    result = db.session.execute("SELECT c.id, c.name, d.docker_image, d.memory_limit, d.cpu_limit FROM challenges c JOIN dynamic_docker_challenge d ON c.id = d.id").fetchall()
    print("=== Dynamic Docker Challenge Limits (Raw SQL) ===")
    for row in result:
        print(f"ID: {row[0]} | Name: {row[1]} | Image: {row[2]} | Mem Limit: {row[3]} | CPU Limit: {row[4]}")
