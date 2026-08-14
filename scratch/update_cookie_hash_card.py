import json
import sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson
from CTFd.models import db, Challenges

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
    เรียนรู้การขโมยเซสชันคุกกี้ของผู้ดูแลระบบ (Session Hijacking) และการถอดรหัสผ่านแบบแฮช MD5 (MD5 Hash Cracking) จากข้อมูลที่หลุดรั่วอยู่ใน Cookie ของบราวเซอร์ (remember_me)
  </p>
  <div style="background:rgba(0,0,0,0.25);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:16px;margin:0;">
    <h5 style="margin:0 0 8px;font-size:0.8rem;color:#fbbf24;font-weight:bold;text-transform:uppercase;letter-spacing:0.05em;">📌 ภารกิจการเจาะระบบ (Mission details)</h5>
    <ul style="margin:0;padding-left:20px;font-size:0.78rem;color:#94a3b8;line-height:1.6;">
      <li>กด F12 เพื่อเปิดเครื่องมือนักพัฒนา ไปที่แท็บ <strong>Application -> Cookies</strong> (หรือ Storage -> Cookies)</li>
      <li>ค้นหาคุกกี้ชื่อ <strong>remember_me</strong> และคัดลอกค่าที่เป็น Base64 String ออกมา</li>
      <li>นำไปแปลงรหัสกลับ (Base64 Decode) เพื่อกู้คืนรหัสผ่านแฮช MD5 และคีย์ Admin Session</li>
      <li><strong>Path A:</strong> นำคีย์ Admin Session (<code>adm_cookie_d3b5b11c_x</code>) ไปตั้งเป็นคุกกี้ชื่อ <code>auth</code> ในเบราว์เซอร์ แล้วรีเฟรชหน้าเว็บ</li>
      <li><strong>Path B:</strong> นำรหัสผ่านแฮช MD5 (<code>962012d09b8170d912f0669f6d7d9d07</code>) ไปถอดรหัส (เช่น ใช้เว็บ CrackStation) เพื่อหา Password จริง แล้วนำมาใช้ล็อกอินในแบบฟอร์มปกติ</li>
    </ul>
  </div>
</div>"""

chal_description = """<div class="p-4 mb-3" style="background: rgba(12, 15, 29, 0.85); border-left: 4px solid #fbbf24; border-radius: 4px; font-family: 'Outfit', sans-serif;">
    <h3 style="color: #fbbf24; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem;">
        🍪 Lab: Cookie Hijacking & MD5 Hash Crack
    </h3>
    <p style="color: #c8d1e0; font-size: 1rem; line-height: 1.6; margin-bottom: 1rem;">
        ระบบ Staff Portal ลักลอบเก็บข้อมูลความลับของระบบแอดมินไว้ในบราวเซอร์คุกกี้
    </p>
    <div class="mt-4 p-3" style="background: rgba(251,191,36,0.08); border: 1px dashed rgba(251,191,36,0.3); border-radius: 4px;">
        <h5 style="color: #fbbf24; font-weight: 700; margin-bottom: 0.5rem; text-transform: uppercase;">
            🎯 Objective:
        </h5>
        <p class="mb-0" style="color: #fff; font-size: 0.95rem; line-height: 1.5;">
            กู้คืนค่าจากคุกกี้ <code>remember_me</code> แล้วทำการเข้าสู่ระบบเพื่อกู้รหัส Flag
        </p>
    </div>
</div>"""

with app.app_context():
    # Update challenge description
    c = Challenges.query.filter_by(name="Web Cookie Hijacking & Hash Crack").first()
    if c:
        c.description = chal_description
        print("Updated Challenge Description")
        
    # Update Tutorial Lesson 177 content card block
    l = TutorialLesson.query.get(177)
    if l:
        blocks = json.loads(l.content)
        # Find block containing "เป้าหมายการทำแล็บ (OBJECTIVE) - Cookie Hijacking"
        for i, b in enumerate(blocks):
            if b['type'] == 'markdown' and 'เป้าหมายการทำแล็บ (OBJECTIVE) - Cookie Hijacking' in b['value']:
                blocks[i]['value'] = card_html
                print(f"Updated Lesson Card at Block {i}")
                break
        l.content = json.dumps(blocks, ensure_ascii=False)
        
    db.session.commit()
    print("Database committed successfully!")
