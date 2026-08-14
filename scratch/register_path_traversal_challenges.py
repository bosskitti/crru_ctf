import sys
import importlib
from CTFd import create_app
from CTFd.models import db, Challenges, Flags

app = create_app()

desc_lab1 = """<div class="p-4 mb-3" style="background: rgba(12, 15, 29, 0.85); border-left: 4px solid var(--accent-cyan); border-radius: 4px; font-family: 'Outfit', sans-serif;">
    <h3 style="color: var(--accent-cyan); font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem; font-family: 'Outfit', sans-serif !important;">
        Lab 1: File Path Traversal (Simple Case)
    </h3>
    <p style="color: #c8d1e0; font-size: 1.05rem; line-height: 1.6; font-family: 'Outfit', sans-serif !important;">
        This lab contains a simple file path traversal vulnerability in the display of image files.
    </p>
    <div class="mt-4 p-3" style="background: rgba(255, 0, 85, 0.08); border: 1px dashed rgba(255, 0, 85, 0.3); border-radius: 4px;">
        <h5 style="color: var(--accent-pink); font-weight: 700; margin-bottom: 0.5rem; text-transform: uppercase; font-family: 'Outfit', sans-serif !important;">
            Objective:
        </h5>
        <p class="mb-0" style="color: #fff; font-family: 'Outfit', sans-serif !important; font-size: 0.95rem; line-height: 1.5;">
            To solve the lab, retrieve the content of the <code>/etc/passwd</code> file, locate the user <code>flag_user</code>, and submit the flag found in their user description field.
        </p>
    </div>
</div>"""

desc_lab2 = """<div class="p-4 mb-3" style="background: rgba(12, 15, 29, 0.85); border-left: 4px solid var(--accent-cyan); border-radius: 4px; font-family: 'Outfit', sans-serif;">
    <h3 style="color: var(--accent-cyan); font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem; font-family: 'Outfit', sans-serif !important;">
        Lab 2: File Path Traversal (Stripped Non-Recursively)
    </h3>
    <p style="color: #c8d1e0; font-size: 1.05rem; line-height: 1.6; font-family: 'Outfit', sans-serif !important;">
        This lab blocks traversal sequences by stripping <code>../</code> non-recursively before loading files.
    </p>
    <div class="mt-4 p-3" style="background: rgba(255, 0, 85, 0.08); border: 1px dashed rgba(255, 0, 85, 0.3); border-radius: 4px;">
        <h5 style="color: var(--accent-pink); font-weight: 700; margin-bottom: 0.5rem; text-transform: uppercase; font-family: 'Outfit', sans-serif !important;">
            Objective:
        </h5>
        <p class="mb-0" style="color: #fff; font-family: 'Outfit', sans-serif !important; font-size: 0.95rem; line-height: 1.5;">
            To solve the lab, bypass the non-recursive path traversal filter, read the web server access log file <code>/var/log/httpd-access.log</code>, and extract the flag hidden inside.
        </p>
    </div>
</div>"""

desc_lab3 = """<div class="p-4 mb-3" style="background: rgba(12, 15, 29, 0.85); border-left: 4px solid var(--accent-cyan); border-radius: 4px; font-family: 'Outfit', sans-serif;">
    <h3 style="color: var(--accent-cyan); font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem; font-family: 'Outfit', sans-serif !important;">
        Lab 3: File Path Traversal (Start of Path Validation)
    </h3>
    <p style="color: #c8d1e0; font-size: 1.05rem; line-height: 1.6; font-family: 'Outfit', sans-serif !important;">
        This lab validates that the input path starts with a specific prefix folder, but fails to check relative directory traversal.
    </p>
    <div class="mt-4 p-3" style="background: rgba(255, 0, 85, 0.08); border: 1px dashed rgba(255, 0, 85, 0.3); border-radius: 4px;">
        <h5 style="color: var(--accent-pink); font-weight: 700; margin-bottom: 0.5rem; text-transform: uppercase; font-family: 'Outfit', sans-serif !important;">
            Objective:
        </h5>
        <p class="mb-0" style="color: #fff; font-family: 'Outfit', sans-serif !important; font-size: 0.95rem; line-height: 1.5;">
            To solve the lab, bypass the start-of-path validation filter, read the root user shell configuration file <code>/root/.bashrc</code>, and extract the flag hidden inside.
        </p>
    </div>
</div>"""

challenges_data = [
    {
        "name": "File Path Traversal (Simple Case)",
        "description": desc_lab1,
        "flag": "flag{path_traversal_passwd_success_a3b2}"
    },
    {
        "name": "File Path Traversal (Stripped Non-Recursively)",
        "description": desc_lab2,
        "flag": "flag{path_traversal_access_log_success_c8e9}"
    },
    {
        "name": "File Path Traversal (Start of Path Validation)",
        "description": desc_lab3,
        "flag": "flag{path_traversal_bashrc_success_d7d2}"
    }
]

with app.app_context():
    from CTFd.models import Challenges
    ctfd_whale_models = importlib.import_module("CTFd.plugins.ctfd-whale.models")
    DynamicDockerChallenge = ctfd_whale_models.DynamicDockerChallenge

    for idx, c_data in enumerate(challenges_data):
        # Resolve type mismatch if any
        base_chall = Challenges.query.filter_by(name=c_data["name"]).first()
        if base_chall and base_chall.type != "dynamic_docker":
            db.session.query(Challenges).filter_by(id=base_chall.id).update({"type": "dynamic_docker"})
            db.session.commit()

        chall = DynamicDockerChallenge.query.filter_by(name=c_data["name"]).first()
        if not chall:
            chall = DynamicDockerChallenge(
                name=c_data["name"],
                description=c_data["description"],
                category="Tutorial",
                type="dynamic_docker",
                state="visible",
                value=200 + idx * 50,
                initial=200 + idx * 50,
                decay=15,
                minimum=50,
                docker_image="web-path-traversal:latest",
                redirect_type="http",
                redirect_port=80,
                memory_limit="128m",
                cpu_limit=0.5,
                dynamic_score=1
            )
            db.session.add(chall)
            db.session.commit()
            print(f"SUCCESS: Challenge '{c_data['name']}' registered with ID {chall.id}")
            
            # Add static flag
            flag_obj = Flags(
                challenge_id=chall.id,
                type="static",
                content=c_data["flag"],
                data=""
            )
            db.session.add(flag_obj)
            db.session.commit()
            print(f"SUCCESS: Created flag for '{c_data['name']}': {c_data['flag']}")
        else:
            # Update challenge attributes
            chall.description = c_data["description"]
            chall.category = "Tutorial"
            chall.docker_image = "web-path-traversal:latest"
            chall.redirect_port = 80
            chall.redirect_type = "http"
            db.session.commit()
            print(f"SUCCESS: Challenge '{c_data['name']}' updated with ID {chall.id}")
            
            # Update existing flag
            flag_obj = Flags.query.filter_by(challenge_id=chall.id).first()
            if flag_obj:
                flag_obj.content = c_data["flag"]
                db.session.commit()
                print(f"SUCCESS: Updated flag for '{c_data['name']}': {c_data['flag']}")
