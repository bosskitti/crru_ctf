import json
import sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
from CTFd.models import db, Challenges, Flags
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

card_html = """<div style="background:#070a13;border:1px solid rgba(251,191,36,0.3);border-radius:12px;padding:24px;margin:2.5rem auto 1.5rem;max-width:1000px;box-shadow:0 10px 30px rgba(251,191,36,0.15);position:relative;overflow:hidden;">
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg, #fbbf24, #f59e0b);"></div>
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
    <h4 style="margin:0;font-size:1.15rem;font-weight:800;color:#ffffff;display:flex;align-items:center;gap:8px;">
      <span style="font-size:1.3rem;">🎯</span> เป้าหมายการทำแล็บ (OBJECTIVE) - Cookie Hijacking & Hash Crack
    </h4>
    <span style="font-size:0.68rem;font-family:monospace;font-weight:700;padding:3px 10px;border-radius:20px;background:rgba(251,191,36,0.1);color:#fbbf24;border:1px solid rgba(251,191,36,0.25);">LAB: PRACTITIONER</span>
  </div>
  <p style="margin:0 0 16px;font-size:0.83rem;color:#cbd5e1;line-height:1.6;">
    เรียนรู้การขโมยเซสชันคุกกี้ของผู้ดูแลระบบ (Session Hijacking) และการถอดรหัสผ่านแบบแฮช MD5 (MD5 Hash Cracking) จากคอมเมนต์หรือข้อมูลที่หลุดรั่วในหน้าเว็บเพื่อล็อกอินเข้าสู่ระบบระดับแอดมิน
  </p>
  <div style="background:rgba(0,0,0,0.25);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:16px;margin:0;">
    <h5 style="margin:0 0 8px;font-size:0.8rem;color:#fbbf24;font-weight:bold;text-transform:uppercase;letter-spacing:0.05em;">📌 ภารกิจการเจาะระบบ (Mission details)</h5>
    <p style="margin:0 0 8px;font-size:0.78rem;color:#cbd5e1;">เลือกเคลียร์โจทย์ได้จาก 2 เส้นทาง (Path A หรือ Path B):</p>
    <ul style="margin:0;padding-left:20px;font-size:0.78rem;color:#94a3b8;line-height:1.6;">
      <li><strong>Path A (Session Hijack):</strong> ตรวจสอบหน้าพัฒนาเว็บบนเบราว์เซอร์ (F12) เพื่อค้นหาคอมเมนต์ของโปรแกรมเมอร์ที่ลืมทิ้งข้อมูลคุกกี้เซสชันของแอดมิน (<code>auth=adm_cookie_d3b5b11c</code>) นำคุกกี้นี้ไปตั้งค่าบนตัวแปรบราวเซอร์ <code>document.cookie</code> แล้วกด Refresh เพื่อเข้าสิทธิ์แอดมินทันที</li>
      <li><strong>Path B (MD5 Crack):</strong> นำ MD5 Hash (<code>962012d09b8170d912f0669f6d7d9d07</code>) ที่หลุดในสคริปต์ไปถอดรหัสผ่านด้วยบริการออนไลน์ (เช่น CrackStation) เพื่อหารหัสผ่านจริง แล้วทำการล็อกอินด้วยบัญชีแอดมิน</li>
    </ul>
  </div>
</div>"""

chal_description = """<div class="p-4 mb-3" style="background: rgba(12, 15, 29, 0.85); border-left: 4px solid #fbbf24; border-radius: 4px; font-family: 'Outfit', sans-serif;">
    <h3 style="color: #fbbf24; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem;">
        🍪 Lab: Cookie Hijacking & MD5 Hash Crack
    </h3>
    <p style="color: #c8d1e0; font-size: 1rem; line-height: 1.6; margin-bottom: 1rem;">
        ระบบพอร์ทัลเป้าหมายเปิดใช้งานหน้าเชื่อมต่อของนักพัฒนาที่หลงลืมคอมเมนต์รหัสผ่านแฮช MD5 และคุกกี้เซสชันของระบบแอดมินหลักค้างไว้
    </p>
    <div class="mt-4 p-3" style="background: rgba(251,191,36,0.08); border: 1px dashed rgba(251,191,36,0.3); border-radius: 4px;">
        <h5 style="color: #fbbf24; font-weight: 700; margin-bottom: 0.5rem; text-transform: uppercase;">
            🎯 Objective:
        </h5>
        <p class="mb-0" style="color: #fff; font-size: 0.95rem; line-height: 1.5;">
            เจาะระบบสิทธิ์แอดมินโดยใช้วิธีเปลี่ยนค่าคุกกี้ในบราวเซอร์ หรือถอดรหัสแฮช MD5 เพื่อล็อกอินตามปกติเพื่อกู้รหัส Flag
        </p>
    </div>
</div>"""

with app.app_context():
    # 1. Check if challenge already exists, delete if so
    old_c = Challenges.query.filter_by(name="Web Cookie Hijacking & Hash Crack").first()
    if old_c:
        Flags.query.filter_by(challenge_id=old_c.id).delete()
        # Delete from dynamic_challenge & dynamic_docker_challenge tables directly
        db.session.execute(db.text("DELETE FROM dynamic_docker_challenge WHERE id = :id"), {"id": old_c.id})
        db.session.execute(db.text("DELETE FROM dynamic_challenge WHERE id = :id"), {"id": old_c.id})
        Challenges.query.filter_by(id=old_c.id).delete()
        db.session.commit()
        print("Removed old Cookie Hijacking challenge.")

    # 2. Create new challenge
    c = Challenges(
        name="Web Cookie Hijacking & Hash Crack",
        description=chal_description,
        category="Tutorial",
        value=300,
        type="dynamic_docker",
        state="visible"
    )
    db.session.add(c)
    db.session.flush() # get c.id

    # 3. Insert dynamic_challenge and dynamic_docker_challenge rows
    db.session.execute(db.text(
        "INSERT INTO dynamic_challenge (id, dynamic_initial, dynamic_minimum, dynamic_decay, dynamic_function) "
        "VALUES (:id, :init, :mini, :decay, :func)"
    ), {
        "id": c.id,
        "init": 300,
        "mini": 50,
        "decay": 15,
        "func": "logarithmic",
    })

    db.session.execute(db.text(
        "INSERT INTO dynamic_docker_challenge (id, memory_limit, cpu_limit, dynamic_score, docker_image, redirect_type, redirect_port) "
        "VALUES (:id, :mem, :cpu, :dyn, :img, :rtype, :rport)"
    ), {
        "id": c.id,
        "mem": "128m",
        "cpu": 0.5,
        "dyn": 0,
        "img": "web-cookie-hash:latest",
        "rtype": "http",
        "rport": 80,
    })

    # 4. Create static flag in database
    f = Flags(challenge_id=c.id, type="static", content="flag{cookie_hijack_md5_crack_x9y2}", data="")
    db.session.add(f)
    print(f"Registered challenge [{c.id}]: Web Cookie Hijacking & Hash Crack")
    db.session.commit()

    # 5. Add to Lesson 178 content blocks list
    l178 = TutorialLesson.query.get(178)
    if l178:
        blocks = json.loads(l178.content)
        # Find where Block 18 (Quiz) is to insert before it
        quiz_pos = len(blocks) - 1
        
        # Insert markdown card and challenge console block
        blocks.insert(quiz_pos, {"type": "markdown", "value": card_html})
        blocks.insert(quiz_pos + 1, {"type": "challenge", "value": "", "challenge_id": c.id})
        
        l178.content = json.dumps(blocks, ensure_ascii=False)
        print("Embedded new challenge blocks into Lesson 178 structure successfully!")
        db.session.commit()
    else:
        print("ERROR: Lesson 178 not found.")
