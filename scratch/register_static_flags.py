import sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
from CTFd.models import db, Flags, Challenges

app = create_app()

STATIC_FLAGS = {
    "Web XSS (Reflected)": "flag{reflected_xss_cookie_stolen_a8b2}",
    "Web XSS (Stored)": "flag{stored_xss_js_var_c3d4}",
    "Web XSS (DOM-Based)": "flag{dom_xss_hash_fragment_e5f6}",
    "Web Brute Force (PIN Lock)": "flag{brute_force_pin_cracked_g7h8}",
    "Web Brute Force (Login)": "flag{brute_force_login_wordlist_i9j0}",
    "Web LFI (Simple Case)": "flag{lfi_simple_file_read_k1l2}",
    "Web LFI (PHP Filter Bypass)": "flag{lfi_php_filter_bypass_m3n4}",
    "Web Command Injection (Blind)": "flag{blind_cmd_injection_exfil_o5p6}",
    "Web CSRF (Token Bypass)": "flag{csrf_no_token_transfer_q7r8}",
    "Web Clickjacking": "flag{clickjacking_iframe_overlay_s9t0}",
}

with app.app_context():
    # Loop over our challenges
    for name, flag_content in STATIC_FLAGS.items():
        c = Challenges.query.filter_by(name=name).first()
        if not c:
            print(f"ERROR: Challenge not found: {name}")
            continue
        
        # Delete old flags if any
        Flags.query.filter_by(challenge_id=c.id).delete()
        
        # Create new static flag
        f = Flags(challenge_id=c.id, type="static", content=flag_content, data="")
        db.session.add(f)
        print(f"SUCCESS: Set flag for {name} (ID: {c.id}) -> {flag_content}")
        
    db.session.commit()
    print("Database committed successfully!")
