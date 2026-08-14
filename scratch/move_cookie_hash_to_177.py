import json
import sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson
from CTFd.models import db

app = create_app()

with app.app_context():
    # 1. Update Lesson 178 (remove the cookie-hash challenge and card)
    l178 = TutorialLesson.query.get(178)
    if l178:
        blocks178 = json.loads(l178.content)
        print(f"Original Lesson 178 block count: {len(blocks178)}")
        
        # Look for the card value of cookie-hash
        target_indices = []
        for idx, b in enumerate(blocks178):
            if b['type'] == 'challenge' and b.get('challenge_id') == 35:
                target_indices.append(idx)
            elif b['type'] == 'markdown' and 'เป้าหมายการทำแล็บ (OBJECTIVE) - Cookie Hijacking' in b['value']:
                target_indices.append(idx)
                
        # Remove them from back to front to preserve indexing
        for idx in sorted(target_indices, reverse=True):
            print(f"  Removing block {idx} from Lesson 178")
            blocks178.pop(idx)
            
        l178.content = json.dumps(blocks178, ensure_ascii=False)
        print(f"New Lesson 178 block count: {len(blocks178)}")
    else:
        print("ERROR: Lesson 178 not found.")

    # 2. Update Lesson 177 (insert cookie-hash challenge and card after Block 3)
    l177 = TutorialLesson.query.get(177)
    if l177:
        blocks177 = json.loads(l177.content)
        print(f"Original Lesson 177 block count: {len(blocks177)}")
        
        # Define the card HTML
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
      <li><strong>Path A:</strong> นำคีย์ Admin Session (<code>adm_cookie_d3b5b11c</code>) ไปตั้งเป็นคุกกี้ชื่อ <code>auth</code> ในเบราว์เซอร์ แล้วรีเฟรชหน้าเว็บ</li>
      <li><strong>Path B:</strong> นำรหัสผ่านแฮช MD5 (<code>962012d09b8170d912f0669f6d7d9d07</code>) ไปถอดรหัส (เช่น ใช้เว็บ CrackStation) เพื่อหา Password จริง แล้วนำมาใช้ล็อกอินในแบบฟอร์มปกติ</li>
    </ul>
  </div>
</div>"""

        # Verify Block 3 is indeed Challenge ID 20
        assert blocks177[3]['type'] == 'challenge' and blocks177[3].get('challenge_id') == 20, "Block 3 is not Challenge ID 20!"
        
        # Insert after Block 3 (so at index 4 and index 5)
        blocks177.insert(4, {"type": "markdown", "value": card_html})
        blocks177.insert(5, {"type": "challenge", "value": "", "challenge_id": 35})
        
        l177.content = json.dumps(blocks177, ensure_ascii=False)
        print(f"New Lesson 177 block count: {len(blocks177)}")
    else:
        print("ERROR: Lesson 177 not found.")
        
    db.session.commit()
    print("Database committed successfully!")
