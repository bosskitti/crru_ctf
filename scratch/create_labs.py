import json, sys, uuid
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
from CTFd.models import db, Challenges, Flags
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

# ============================================================
# Challenge definitions
# ============================================================
LABS = [
    # (name, value, docker_image, redirect_port, flag, lesson_id, description)
    {
        "name": "Web XSS (Reflected)",
        "value": 200,
        "docker_image": "web-xss-reflected:latest",
        "redirect_port": 80,
        "flag": "flag{reflected_xss_cookie_stolen_" + uuid.uuid4().hex[:12] + "}",
        "lesson_id": 178,
        "description": """<div class="p-4 mb-3" style="background: rgba(12, 15, 29, 0.85); border-left: 4px solid #fbbf24; border-radius: 4px; font-family: 'Outfit', sans-serif;">
    <h3 style="color: #fbbf24; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem;">
        🪞 Lab: Reflected XSS — Cookie Theft
    </h3>
    <p style="color: #c8d1e0; font-size: 1rem; line-height: 1.6; margin-bottom: 1rem;">
        เว็บแอปนี้มีช่องค้นหาที่นำ input ของผู้ใช้จาก URL parameter <code style="color:#fbbf24; background:rgba(251,191,36,0.1); padding:2px 6px; border-radius:3px;">?q=</code> ไปแสดงผลในหน้าเว็บ <strong style="color:#fff;">โดยไม่มีการ sanitize</strong>
    </p>
    <p style="color: #c8d1e0; font-size: 1rem; line-height: 1.6;">
        เว็บยังเก็บ secret token ไว้ใน browser cookie ชื่อ <code style="color:#fbbf24; background:rgba(251,191,36,0.1); padding:2px 6px; border-radius:3px;">flag</code>
    </p>
    <div class="mt-4 p-3" style="background: rgba(251,191,36,0.08); border: 1px dashed rgba(251,191,36,0.3); border-radius: 4px;">
        <h5 style="color: #fbbf24; font-weight: 700; margin-bottom: 0.5rem; text-transform: uppercase;">
            🎯 Objective:
        </h5>
        <p class="mb-0" style="color: #fff; font-size: 0.95rem; line-height: 1.5;">
            ใช้ Reflected XSS เพื่ออ่านค่า cookie ที่ซ่อน flag ไว้ แล้วนำ flag มา submit<br>
            <strong>Payload:</strong> <code style="color:#fbbf24; background:rgba(0,0,0,0.3); padding:2px 8px; border-radius:3px;">&lt;script&gt;alert(document.cookie)&lt;/script&gt;</code>
        </p>
    </div>
</div>""",
    },
    {
        "name": "Web XSS (Stored)",
        "value": 250,
        "docker_image": "web-xss-stored:latest",
        "redirect_port": 80,
        "flag": "flag{stored_xss_js_var_" + uuid.uuid4().hex[:12] + "}",
        "lesson_id": 178,
        "description": """<div class="p-4 mb-3" style="background: rgba(12, 15, 29, 0.85); border-left: 4px solid #fbbf24; border-radius: 4px; font-family: 'Outfit', sans-serif;">
    <h3 style="color: #fbbf24; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem;">
        💾 Lab: Stored XSS — Persistent Script Injection
    </h3>
    <p style="color: #c8d1e0; font-size: 1rem; line-height: 1.6; margin-bottom: 1rem;">
        เว็บ forum นี้เก็บ comment ลงในฐานข้อมูลและนำมาแสดงผล <strong style="color:#fff;">โดยไม่มีการ escape HTML</strong> ทำให้ script ที่ฝังไว้รันทุกครั้งที่มีคนเปิดหน้านี้
    </p>
    <p style="color: #c8d1e0; font-size: 1rem; line-height: 1.6;">
        Flag เก็บอยู่ใน JavaScript variable ชื่อ <code style="color:#fbbf24; background:rgba(251,191,36,0.1); padding:2px 6px; border-radius:3px;">secretFlag</code>
    </p>
    <div class="mt-4 p-3" style="background: rgba(251,191,36,0.08); border: 1px dashed rgba(251,191,36,0.3); border-radius: 4px;">
        <h5 style="color: #fbbf24; font-weight: 700; margin-bottom: 0.5rem; text-transform: uppercase;">
            🎯 Objective:
        </h5>
        <p class="mb-0" style="color: #fff; font-size: 0.95rem; line-height: 1.5;">
            โพสต์ comment ที่มี XSS payload เพื่ออ่านค่า secretFlag แล้วนำ flag มา submit<br>
            <strong>Payload:</strong> <code style="color:#fbbf24; background:rgba(0,0,0,0.3); padding:2px 8px; border-radius:3px;">&lt;script&gt;alert(secretFlag)&lt;/script&gt;</code>
        </p>
    </div>
</div>""",
    },
    {
        "name": "Web XSS (DOM-Based)",
        "value": 300,
        "docker_image": "web-xss-dom:latest",
        "redirect_port": 80,
        "flag": "flag{dom_xss_hash_fragment_" + uuid.uuid4().hex[:12] + "}",
        "lesson_id": 178,
        "description": """<div class="p-4 mb-3" style="background: rgba(12, 15, 29, 0.85); border-left: 4px solid #fbbf24; border-radius: 4px; font-family: 'Outfit', sans-serif;">
    <h3 style="color: #fbbf24; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem;">
        🌐 Lab: DOM-Based XSS — URL Hash Injection
    </h3>
    <p style="color: #c8d1e0; font-size: 1rem; line-height: 1.6; margin-bottom: 1rem;">
        หน้าเว็บนี้อ่านค่าจาก <code style="color:#fbbf24; background:rgba(251,191,36,0.1); padding:2px 6px; border-radius:3px;">location.hash</code> แล้วเขียนลง DOM ด้วย <code style="color:#fbbf24; background:rgba(251,191,36,0.1); padding:2px 6px; border-radius:3px;">innerHTML</code> โดยไม่ sanitize — เป็น DOM-Based XSS ที่ไม่ผ่าน server เลย
    </p>
    <p style="color: #c8d1e0; font-size: 1rem; line-height: 1.6;">
        Flag เก็บอยู่ใน JavaScript variable ชื่อ <code style="color:#fbbf24; background:rgba(251,191,36,0.1); padding:2px 6px; border-radius:3px;">FLAG</code>
    </p>
    <div class="mt-4 p-3" style="background: rgba(251,191,36,0.08); border: 1px dashed rgba(251,191,36,0.3); border-radius: 4px;">
        <h5 style="color: #fbbf24; font-weight: 700; margin-bottom: 0.5rem; text-transform: uppercase;">
            🎯 Objective:
        </h5>
        <p class="mb-0" style="color: #fff; font-size: 0.95rem; line-height: 1.5;">
            ฝัง payload ผ่าน URL hash fragment เพื่ออ่านค่า FLAG<br>
            <strong>Payload ใน URL:</strong> <code style="color:#fbbf24; background:rgba(0,0,0,0.3); padding:2px 8px; border-radius:3px;">#&lt;img src=x onerror=alert(FLAG)&gt;</code>
        </p>
    </div>
</div>""",
    },
    {
        "name": "Web Brute Force (PIN Lock)",
        "value": 200,
        "docker_image": "web-brute-pin:latest",
        "redirect_port": 80,
        "flag": "flag{brute_force_pin_cracked_" + uuid.uuid4().hex[:12] + "}",
        "lesson_id": 178,
        "description": """<div class="p-4 mb-3" style="background: rgba(12, 15, 29, 0.85); border-left: 4px solid var(--accent-cyan); border-radius: 4px; font-family: 'Outfit', sans-serif;">
    <h3 style="color: var(--accent-cyan); font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem;">
        🔐 Lab: Brute Force — PIN Lock (0000–9999)
    </h3>
    <p style="color: #c8d1e0; font-size: 1rem; line-height: 1.6; margin-bottom: 1rem;">
        ระบบ vault นี้ป้องกันด้วย PIN 4 หลัก แต่ <strong style="color:#fff;">ไม่มี rate limiting หรือ account lockout</strong> ทำให้สามารถ brute force ได้ทุก combination
    </p>
    <div class="mt-4 p-3" style="background: rgba(255, 0, 85, 0.08); border: 1px dashed rgba(255, 0, 85, 0.3); border-radius: 4px;">
        <h5 style="color: var(--accent-pink); font-weight: 700; margin-bottom: 0.5rem; text-transform: uppercase;">
            🎯 Objective:
        </h5>
        <p class="mb-0" style="color: #fff; font-size: 0.95rem; line-height: 1.5;">
            เขียน Python script ลอง PIN 0000–9999 จนกว่าจะได้ flag<br>
            ใช้ <code style="color:var(--accent-cyan); background:rgba(0,240,255,0.1); padding:2px 6px; border-radius:3px;">requests.post(url, data={{"pin": pin_str}})</code>
        </p>
    </div>
</div>""",
    },
    {
        "name": "Web Brute Force (Login)",
        "value": 250,
        "docker_image": "web-brute-login:latest",
        "redirect_port": 80,
        "flag": "flag{brute_force_login_wordlist_" + uuid.uuid4().hex[:12] + "}",
        "lesson_id": 178,
        "description": """<div class="p-4 mb-3" style="background: rgba(12, 15, 29, 0.85); border-left: 4px solid var(--accent-cyan); border-radius: 4px; font-family: 'Outfit', sans-serif;">
    <h3 style="color: var(--accent-cyan); font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem;">
        🔑 Lab: Brute Force — Dictionary Attack (Login Form)
    </h3>
    <p style="color: #c8d1e0; font-size: 1rem; line-height: 1.6; margin-bottom: 1rem;">
        Admin login form ที่ไม่มี rate limiting — username คือ <code style="color:var(--accent-cyan); background:rgba(0,240,255,0.1); padding:2px 6px; border-radius:3px;">admin</code> และ password เป็นคำในพจนานุกรมทั่วไป
    </p>
    <div class="mt-4 p-3" style="background: rgba(255, 0, 85, 0.08); border: 1px dashed rgba(255, 0, 85, 0.3); border-radius: 4px;">
        <h5 style="color: var(--accent-pink); font-weight: 700; margin-bottom: 0.5rem; text-transform: uppercase;">
            🎯 Objective:
        </h5>
        <p class="mb-0" style="color: #fff; font-size: 0.95rem; line-height: 1.5;">
            ใช้ Python + rockyou.txt หรือ Hydra โจมตี login form จนได้ flag<br>
            <code style="color:var(--accent-cyan); background:rgba(0,240,255,0.1); padding:2px 6px; border-radius:3px;">hydra -l admin -P rockyou.txt http-post-form "/:username=^USER^&amp;password=^PASS^:Invalid"</code>
        </p>
    </div>
</div>""",
    },
    {
        "name": "Web LFI (Simple Case)",
        "value": 200,
        "docker_image": "web-lfi-simple:latest",
        "redirect_port": 80,
        "flag": "flag{lfi_simple_file_read_" + uuid.uuid4().hex[:12] + "}",
        "lesson_id": 178,
        "description": """<div class="p-4 mb-3" style="background: rgba(12, 15, 29, 0.85); border-left: 4px solid #a855f7; border-radius: 4px; font-family: 'Outfit', sans-serif;">
    <h3 style="color: #a855f7; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem;">
        📁 Lab: Local File Inclusion — Simple Case
    </h3>
    <p style="color: #c8d1e0; font-size: 1rem; line-height: 1.6; margin-bottom: 1rem;">
        เว็บใช้ <code style="color:#a855f7; background:rgba(168,85,247,0.1); padding:2px 6px; border-radius:3px;">include($_GET['page'])</code> โดยตรง ไม่มีการ validate path ทำให้สามารถโหลดไฟล์ใดก็ได้บน server
    </p>
    <div class="mt-4 p-3" style="background: rgba(168, 85, 247, 0.08); border: 1px dashed rgba(168, 85, 247, 0.3); border-radius: 4px;">
        <h5 style="color: #a855f7; font-weight: 700; margin-bottom: 0.5rem; text-transform: uppercase;">
            🎯 Objective:
        </h5>
        <p class="mb-0" style="color: #fff; font-size: 0.95rem; line-height: 1.5;">
            อ่านไฟล์ <code style="color:#a855f7; background:rgba(168,85,247,0.1); padding:2px 6px; border-radius:3px;">/flag.txt</code> ผ่าน LFI แล้วนำ flag มา submit<br>
            <strong>Payload:</strong> <code style="color:#a855f7; background:rgba(0,0,0,0.3); padding:2px 8px; border-radius:3px;">?page=../../../../flag.txt</code>
        </p>
    </div>
</div>""",
    },
    {
        "name": "Web LFI (PHP Filter Bypass)",
        "value": 350,
        "docker_image": "web-lfi-filter:latest",
        "redirect_port": 80,
        "flag": "flag{lfi_php_filter_bypass_" + uuid.uuid4().hex[:12] + "}",
        "lesson_id": 178,
        "description": """<div class="p-4 mb-3" style="background: rgba(12, 15, 29, 0.85); border-left: 4px solid #a855f7; border-radius: 4px; font-family: 'Outfit', sans-serif;">
    <h3 style="color: #a855f7; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem;">
        🔓 Lab: LFI — PHP Filter Wrapper Bypass
    </h3>
    <p style="color: #c8d1e0; font-size: 1rem; line-height: 1.6; margin-bottom: 1rem;">
        เว็บพยายามบล็อก <code style="color:#a855f7; background:rgba(168,85,247,0.1); padding:2px 6px; border-radius:3px;">..</code> แต่ลืมบล็อก PHP stream wrappers เช่น <code style="color:#a855f7; background:rgba(168,85,247,0.1); padding:2px 6px; border-radius:3px;">php://filter</code>
    </p>
    <div class="mt-4 p-3" style="background: rgba(168, 85, 247, 0.08); border: 1px dashed rgba(168, 85, 247, 0.3); border-radius: 4px;">
        <h5 style="color: #a855f7; font-weight: 700; margin-bottom: 0.5rem; text-transform: uppercase;">
            🎯 Objective:
        </h5>
        <p class="mb-0" style="color: #fff; font-size: 0.95rem; line-height: 1.5;">
            ใช้ PHP filter wrapper อ่าน source code ของ secret_config.php แล้วหา flag<br>
            <strong>Payload:</strong> <code style="color:#a855f7; background:rgba(0,0,0,0.3); padding:2px 8px; border-radius:3px;">?page=php://filter/convert.base64-encode/resource=secret_config</code><br>
            จากนั้น base64 decode ผลลัพธ์ที่ได้
        </p>
    </div>
</div>""",
    },
    {
        "name": "Web Command Injection (Blind)",
        "value": 400,
        "docker_image": "web-cmd-blind:latest",
        "redirect_port": 80,
        "flag": "flag{blind_cmd_injection_exfil_" + uuid.uuid4().hex[:12] + "}",
        "lesson_id": 178,
        "description": """<div class="p-4 mb-3" style="background: rgba(12, 15, 29, 0.85); border-left: 4px solid var(--accent-cyan); border-radius: 4px; font-family: 'Outfit', sans-serif;">
    <h3 style="color: var(--accent-cyan); font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem;">
        👁️ Lab: Blind OS Command Injection
    </h3>
    <p style="color: #c8d1e0; font-size: 1rem; line-height: 1.6;">
        DNS lookup tool ที่รัน command แต่<strong style="color:#fff;">ไม่แสดงผลลัพธ์</strong> ต้องใช้ out-of-band technique เพื่อ exfiltrate flag
    </p>
    <pre style="background: rgba(0,0,0,0.4); border: 1px solid rgba(0,240,255,0.2); color: var(--accent-cyan); padding: 12px; font-family: 'JetBrains Mono', monospace; font-size: 0.9rem; border-radius: 4px; margin: 1rem 0;">nslookup [user-input] 2>/dev/null  # output suppressed!</pre>
    <div class="mt-4 p-3" style="background: rgba(255, 0, 85, 0.08); border: 1px dashed rgba(255, 0, 85, 0.3); border-radius: 4px;">
        <h5 style="color: var(--accent-pink); font-weight: 700; margin-bottom: 0.5rem; text-transform: uppercase;">
            🎯 Objective:
        </h5>
        <p class="mb-0" style="color: #fff; font-size: 0.95rem; line-height: 1.5;">
            ยืนยัน code execution ด้วย <code style="color:var(--accent-cyan); background:rgba(0,240,255,0.1); padding:2px 6px; border-radius:3px;">; sleep 5</code> แล้ว exfil flag:<br>
            <code style="color:var(--accent-cyan); background:rgba(0,240,255,0.1); padding:2px 6px; border-radius:3px;">; cp /flag.txt /var/www/html/flag_out.txt</code><br>
            จากนั้นเปิด <code style="color:var(--accent-cyan); background:rgba(0,240,255,0.1); padding:2px 6px; border-radius:3px;">/flag_out.txt</code> ใน browser
        </p>
    </div>
</div>""",
    },
    {
        "name": "Web CSRF (Token Bypass)",
        "value": 350,
        "docker_image": "web-csrf:latest",
        "redirect_port": 80,
        "flag": "flag{csrf_no_token_transfer_" + uuid.uuid4().hex[:12] + "}",
        "lesson_id": 179,
        "description": """<div class="p-4 mb-3" style="background: rgba(12, 15, 29, 0.85); border-left: 4px solid #10b981; border-radius: 4px; font-family: 'Outfit', sans-serif;">
    <h3 style="color: #10b981; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem;">
        🏦 Lab: CSRF — Cross-Site Request Forgery
    </h3>
    <p style="color: #c8d1e0; font-size: 1rem; line-height: 1.6; margin-bottom: 1rem;">
        ระบบ banking นี้มีฟอร์ม transfer เงิน <strong style="color:#fff;">ไม่มี CSRF token</strong> ทำให้ attacker สามารถสร้างหน้าเว็บที่ส่ง request แทนเหยื่อได้โดยอัตโนมัติ
    </p>
    <div class="mt-4 p-3" style="background: rgba(16, 185, 129, 0.08); border: 1px dashed rgba(16, 185, 129, 0.3); border-radius: 4px;">
        <h5 style="color: #10b981; font-weight: 700; margin-bottom: 0.5rem; text-transform: uppercase;">
            🎯 Objective:
        </h5>
        <p class="mb-0" style="color: #fff; font-size: 0.95rem; line-height: 1.5;">
            1. Login ด้วย <code style="color:#10b981; background:rgba(16,185,129,0.1); padding:2px 6px; border-radius:3px;">admin / password123</code><br>
            2. ขณะ login อยู่ ให้เปิดหน้า <code style="color:#10b981; background:rgba(16,185,129,0.1); padding:2px 6px; border-radius:3px;">/attacker.php</code><br>
            3. เงินจะถูกโอนออกโดยไม่ต้องยืนยัน → flag จะปรากฏ
        </p>
    </div>
</div>""",
    },
    {
        "name": "Web Clickjacking",
        "value": 200,
        "docker_image": "web-clickjacking:latest",
        "redirect_port": 80,
        "flag": "flag{clickjacking_iframe_overlay_" + uuid.uuid4().hex[:12] + "}",
        "lesson_id": 179,
        "description": """<div class="p-4 mb-3" style="background: rgba(12, 15, 29, 0.85); border-left: 4px solid #f59e0b; border-radius: 4px; font-family: 'Outfit', sans-serif;">
    <h3 style="color: #f59e0b; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem;">
        🖱️ Lab: Clickjacking — UI Redressing Attack
    </h3>
    <p style="color: #c8d1e0; font-size: 1rem; line-height: 1.6; margin-bottom: 1rem;">
        Admin panel ไม่มี <code style="color:#f59e0b; background:rgba(245,158,11,0.1); padding:2px 6px; border-radius:3px;">X-Frame-Options</code> header ทำให้ attacker สามารถฝัง iframe ที่มองไม่เห็น ซ้อนบนปุ่มปลอม หลอกให้เหยื่อกดโดยไม่รู้ตัว
    </p>
    <div class="mt-4 p-3" style="background: rgba(245, 158, 11, 0.08); border: 1px dashed rgba(245, 158, 11, 0.3); border-radius: 4px;">
        <h5 style="color: #f59e0b; font-weight: 700; margin-bottom: 0.5rem; text-transform: uppercase;">
            🎯 Objective:
        </h5>
        <p class="mb-0" style="color: #fff; font-size: 0.95rem; line-height: 1.5;">
            1. เปิดหน้า <code style="color:#f59e0b; background:rgba(245,158,11,0.1); padding:2px 6px; border-radius:3px;">/attacker.php</code><br>
            2. คลิกปุ่ม "CLAIM FREE PRIZE" (ที่จริงคือกดปุ่ม Delete Account ที่ซ่อนอยู่)<br>
            3. flag จะปรากฏใน <code style="color:#f59e0b; background:rgba(245,158,11,0.1); padding:2px 6px; border-radius:3px;">/victim.php</code>
        </p>
    </div>
</div>""",
    },
]

# ============================================================
# Create challenges + flags + update lessons
# ============================================================
with app.app_context():
    created = []
    lesson_blocks = {}  # lesson_id -> list of challenge ids to add

    for lab in LABS:
        # 1. Create challenge record
        c = Challenges(
            name=lab["name"],
            description=lab["description"],
            category="Tutorial",
            value=lab["value"],
            type="dynamic_docker",
            state="visible",
        )
        db.session.add(c)
        db.session.flush()  # get c.id

        # 2. Insert dynamic_challenge row (required by FK chain)
        db.session.execute(db.text(
            "INSERT INTO dynamic_challenge (id, dynamic_initial, dynamic_minimum, dynamic_decay, dynamic_function) "
            "VALUES (:id, :init, :mini, :decay, :func)"
        ), {
            "id": c.id,
            "init": lab["value"],
            "mini": 50,
            "decay": 15,
            "func": "logarithmic",
        })

        # 3. Insert dynamic_docker_challenge row
        db.session.execute(db.text(
            "INSERT INTO dynamic_docker_challenge (id, memory_limit, cpu_limit, dynamic_score, docker_image, redirect_type, redirect_port) "
            "VALUES (:id, :mem, :cpu, :dyn, :img, :rtype, :rport)"
        ), {
            "id": c.id,
            "mem": "128m",
            "cpu": 0.5,
            "dyn": 0,
            "img": lab["docker_image"],
            "rtype": "http",
            "rport": lab["redirect_port"],
        })

        # 3. Create flag
        f = Flags(challenge_id=c.id, type="static", content=lab["flag"], data="")
        db.session.add(f)

        created.append((c.id, lab["name"], lab["flag"], lab["lesson_id"]))

        # Track by lesson
        lesson_blocks.setdefault(lab["lesson_id"], []).append(c.id)
        print(f"  Created challenge [{c.id}]: {lab['name']}")

    db.session.commit()
    print(f"\nTotal created: {len(created)} challenges")

    # 4. Add challenge blocks to lessons
    for lesson_id, chal_ids in lesson_blocks.items():
        lesson = TutorialLesson.query.get(lesson_id)
        if not lesson:
            print(f"Lesson {lesson_id} not found!")
            continue

        blocks = json.loads(lesson.content)
        # Insert challenge blocks before the last block (quiz)
        # Find position before quiz (last block)
        insert_pos = len(blocks) - 1  # before quiz
        new_blocks = []
        for cid in chal_ids:
            new_blocks.append({"type": "challenge", "value": "", "challenge_id": cid})

        for i, nb in enumerate(new_blocks):
            blocks.insert(insert_pos + i, nb)

        lesson.content = json.dumps(blocks, ensure_ascii=False)
        print(f"  Added {len(chal_ids)} challenge blocks to Lesson {lesson_id}")

    db.session.commit()
    print("\nAll done!")

    print("\n=== Summary ===")
    for cid, name, flag, lid in created:
        print(f"  [{cid}] {name} → Lesson {lid} | {flag}")
