import sys
from CTFd import create_app
from CTFd.models import Challenges, Flags, db

app = create_app()

with app.app_context():
    chall = Challenges.query.filter_by(name="Web Parameter Tampering (Privilege Escalation)").first()
    if not chall:
        print("ERROR: Challenge not found in database.")
        sys.exit(1)
        
    print(f"Found Challenge ID: {chall.id}")
    
    # Check flags
    flags = Flags.query.filter_by(challenge_id=chall.id).all()
    static_flag_val = "flag{57423abe-e470-432b-85b3-10d360741b8b}"
    
    if len(flags) == 0:
        # Create a new static flag
        flag_obj = Flags(
            challenge_id=chall.id,
            type="static",
            content=static_flag_val,
            data=""
        )
        db.session.add(flag_obj)
        db.session.commit()
        print(f"SUCCESS: Created static flag: {static_flag_val}")
    else:
        # Update existing flags to be static and have the correct value
        for f in flags:
            f.type = "static"
            f.content = static_flag_val
            f.data = ""
        db.session.commit()
        print(f"SUCCESS: Updated existing flags to static: {static_flag_val}")
