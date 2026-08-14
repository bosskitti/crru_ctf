import json
import importlib
from CTFd import create_app
from CTFd.models import db

app = create_app()

description_html = """<div class="p-4 mb-3" style="background: rgba(12, 15, 29, 0.85); border-left: 4px solid var(--accent-cyan); border-radius: 4px; font-family: 'Outfit', sans-serif;">
    <h3 style="color: var(--accent-cyan); font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem; font-family: 'Outfit', sans-serif !important;">
        Lab: Web Parameter Tampering & Privilege Escalation
    </h3>
    <p style="color: #c8d1e0; font-size: 1.05rem; line-height: 1.6; font-family: 'Outfit', sans-serif !important;">
        This lab contains a registration function that is vulnerable to parameter tampering, allowing users to register with arbitrary privileges.
    </p>
    <div class="mt-4 p-3" style="background: rgba(255, 0, 85, 0.08); border: 1px dashed rgba(255, 0, 85, 0.3); border-radius: 4px;">
        <h5 style="color: var(--accent-pink); font-weight: 700; margin-bottom: 0.5rem; text-transform: uppercase; font-family: 'Outfit', sans-serif !important;">
            Objective:
        </h5>
        <p class="mb-0" style="color: #fff; font-family: 'Outfit', sans-serif !important; font-size: 0.95rem; line-height: 1.5;">
            To solve the lab, register a new account and tamper with the registration parameters to gain administrative privileges (<code>role=admin</code>). Then, log in to access the administrator dashboard and retrieve the flag.
        </p>
    </div>
</div>"""

with app.app_context():
    # Import inside app_context to prevent Flask RuntimeError
    ctfd_whale_models = importlib.import_module("CTFd.plugins.ctfd-whale.models")
    DynamicDockerChallenge = ctfd_whale_models.DynamicDockerChallenge

    chall = DynamicDockerChallenge.query.filter_by(name="Web Parameter Tampering (Privilege Escalation)").first()
    if not chall:
        chall = DynamicDockerChallenge(
            name="Web Parameter Tampering (Privilege Escalation)",
            description=description_html,
            category="Tutorial",
            type="dynamic_docker",
            state="visible",
            value=500,
            initial=500,
            decay=15,
            minimum=50,
            docker_image="web-parameter-tampering:latest",
            redirect_type="http",
            redirect_port=80,
            memory_limit="128m",
            cpu_limit=0.5,
            dynamic_score=1
        )
        db.session.add(chall)
        db.session.commit()
        print(f"SUCCESS: Challenge registered with ID {chall.id}")
    else:
        # Update challenge attributes in case they changed
        chall.description = description_html
        chall.category = "Tutorial"
        chall.docker_image = "web-parameter-tampering:latest"
        chall.redirect_port = 80
        chall.redirect_type = "http"
        db.session.commit()
        print(f"SUCCESS: Challenge updated with ID {chall.id}")
