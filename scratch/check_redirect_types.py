import sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
from CTFd.models import db

app = create_app()

with app.app_context():
    result = db.session.execute("SELECT c.id, c.name, d.redirect_type, d.redirect_port FROM challenges c JOIN dynamic_docker_challenge d ON c.id = d.id").fetchall()
    print("=== Dynamic Docker Challenge Redirections ===")
    for row in result:
        print(f"ID: {row[0]} | Name: {row[1]} | Redirect Type: {row[2]} | Redirect Port: {row[3]}")
