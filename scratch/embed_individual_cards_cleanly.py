import json
import sys
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

card_lab1 = """<div style="background:#070a13;border:1px solid rgba(0,240,255,0.3);border-radius:12px;padding:24px;margin:2.5rem auto 1.5rem;max-width:1000px;box-shadow:0 10px 30px rgba(0,240,255,0.15);position:relative;overflow:hidden;">
<div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg, #00f0ff, #3b82f6);"></div>
<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
<h4 style="margin:0;font-size:1.15rem;font-weight:800;color:#ffffff;display:flex;align-items:center;gap:8px;">
<span style="font-size:1.3rem;">🎯</span> เป้าหมายการทำแล็บ (OBJECTIVE) - Path Traversal (Simple Case)
</h4>
<span style="font-size:0.68rem;font-family:monospace;font-weight:700;padding:3px 10px;border-radius:20px;background:rgba(0,240,255,0.1);color:#00f0ff;border:1px solid rgba(0,240,255,0.25);">LAB 1: APPRENTICE</span>
</div>
<p style="margin:0 0 16px;font-size:0.83rem;color:#cbd5e1;line-height:1.6;">
เรียนรู้การย้อนพาธแบบพื้นฐานโดยไม่มีตัวคัดกรองพารามิเตอร์ใดๆ เพื่อเข้าถึงไฟล์สำคัญในระบบ Linux
</p>
<div style="background:rgba(0,0,0,0.25);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:16px;margin:0;">
<h5 style="margin:0 0 8px;font-size:0.8rem;color:#fbbf24;font-weight:bold;text-transform:uppercase;letter-spacing:0.05em;">📌 ภารกิจการเจาะระบบ (Mission details)</h5>
<ul style="margin:0;padding-left:20px;font-size:0.78rem;color:#94a3b8;line-height:1.6;">
<li>ทำการย้อนพาธออกไปอ่านไฟล์รายชื่อบัญชีของระบบ Linux <strong><code>/etc/passwd</code></strong> (อ้างอิงจาก Sub-Trees Map ในบทที่ 2)</li>
<li>ค้นหาบัญชีผู้ใช้ชื่อ <code>flag_user</code> และคัดลอกรหัส Flag ที่แฝงอยู่ในฟิลด์คำอธิบายผู้ใช้งานมาส่งเพื่อผ่านด่าน</li>
</ul>
</div>
</div>"""

card_lab2 = """<div style="background:#070a13;border:1px solid rgba(168,85,247,0.3);border-radius:12px;padding:24px;margin:2.5rem auto 1.5rem;max-width:1000px;box-shadow:0 10px 30px rgba(168,85,247,0.15);position:relative;overflow:hidden;">
<div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg, #a855f7, #9333ea);"></div>
<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
<h4 style="margin:0;font-size:1.15rem;font-weight:800;color:#ffffff;display:flex;align-items:center;gap:8px;">
<span style="font-size:1.3rem;">🎯</span> เป้าหมายการทำแล็บ (OBJECTIVE) - Path Traversal (Stripped Non-Recursively)
</h4>
<span style="font-size:0.68rem;font-family:monospace;font-weight:700;padding:3px 10px;border-radius:20px;background:rgba(168,85,247,0.1);color:#a855f7;border:1px solid rgba(168,85,247,0.25);">LAB 2: PRACTITIONER</span>
</div>
<p style="margin:0 0 16px;font-size:0.83rem;color:#cbd5e1;line-height:1.6;">
เรียนรู้การบายพาสตัวกรองความปลอดภัยที่จะลบตัวอักษร <code>../</code> ออกไป 1 รอบ โดยอาศัยเทคนิคการซ้อนชุดตัวอักษร (Nested Sequence)
</p>
<div style="background:rgba(0,0,0,0.25);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:16px;margin:0;">
<h5 style="margin:0 0 8px;font-size:0.8rem;color:#fbbf24;font-weight:bold;text-transform:uppercase;letter-spacing:0.05em;">📌 ภารกิจการเจาะระบบ (Mission details)</h5>
<ul style="margin:0;padding-left:20px;font-size:0.78rem;color:#94a3b8;line-height:1.6;">
<li>ทำการบายพาสตัวกรองย้อนพาธเพื่อเข้าไปเปิดอ่านไฟล์ประวัติการเข้าใช้งานเว็บเซิร์ฟเวอร์ <strong><code>/var/log/httpd-access.log</code></strong> (อ้างอิงจาก Sub-Trees Map ในบทที่ 2)</li>
<li>ค้นหาทราฟฟิกเว็บในล็อกและสืบหาคีย์ Flag ที่หลบซ่อนอยู่มาส่งในช่องตอบคำถาม</li>
</ul>
</div>
</div>"""

card_lab3 = """<div style="background:#070a13;border:1px solid rgba(255,0,127,0.3);border-radius:12px;padding:24px;margin:2.5rem auto 1.5rem;max-width:1000px;box-shadow:0 10px 30px rgba(255,0,127,0.15);position:relative;overflow:hidden;">
<div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg, #ff007f, #db2777);"></div>
<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
<h4 style="margin:0;font-size:1.15rem;font-weight:800;color:#ffffff;display:flex;align-items:center;gap:8px;">
<span style="font-size:1.3rem;">🎯</span> เป้าหมายการทำแล็บ (OBJECTIVE) - Path Traversal (Prefix Validation)
</h4>
<span style="font-size:0.68rem;font-family:monospace;font-weight:700;padding:3px 10px;border-radius:20px;background:rgba(255,0,127,0.1);color:#ff007f;border:1px solid rgba(255,0,127,0.25);">LAB 3: PRACTITIONER</span>
</div>
<p style="margin:0 0 16px;font-size:0.83rem;color:#cbd5e1;line-height:1.6;">
เรียนรู้การบายพาสการตรวจสอบพาธส่วนหน้า (Prefix Validation) ที่กำหนดให้การเรียกเปิดไฟล์ต้องขึ้นต้นด้วยไดเรกทอรีที่บังคับไว้เท่านั้น
</p>
<div style="background:rgba(0,0,0,0.25);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:16px;margin:0;">
<h5 style="margin:0 0 8px;font-size:0.8rem;color:#fbbf24;font-weight:bold;text-transform:uppercase;letter-spacing:0.05em;">📌 ภารกิจการเจาะระบบ (Mission details)</h5>
<ul style="margin:0;padding-left:20px;font-size:0.78rem;color:#94a3b8;line-height:1.6;">
<li>ป้อนข้อมูลพารามิเตอร์ให้ตรงเงื่อนไขของระบบ (ต้องขึ้นต้นด้วย <code>/var/www/html/images/</code>) แต่ทำการย้อนพาธเพื่อไปเปิดอ่านสคริปต์คอนฟิกระบบของรูท <strong><code>/root/.bashrc</code></strong></li>
<li>สืบหาคีย์ Flag ที่คอมเมนต์ซ่อนอยู่ในไฟล์มาส่งเพื่อปลดล็อกแล็บ</li>
</ul>
</div>
</div>"""

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if not l:
        print("ERROR: Lesson 177 not found.")
        sys.exit(1)
        
    try:
        blocks = json.loads(l.content)
        print(f"Current blocks count: {len(blocks)}")
        
        # Verify block structure
        if len(blocks) != 11:
            print("ERROR: Expected exactly 11 blocks before redistributing.")
            sys.exit(1)
            
        val_block_4 = blocks[4]["value"]
        
        # Strip the old 3-column card from Block 4
        # The card starts with <div style="background:#070a13;border:1px solid rgba(168,85,247,0.3)
        marker = '<div style="background:#070a13;border:1px solid rgba(168,85,247,0.3);'
        idx = val_block_4.find(marker)
        if idx != -1:
            val_block_4 = val_block_4[:idx].strip()
            print("Successfully stripped the big card from Block 4.")
        else:
            print("WARNING: Could not find the old big card in Block 4.")
            
        # Rebuild blocks list to have individual cards right before the respective challenges
        new_blocks = [
            blocks[0],  # Block 0 (Parameter Tampering slides)
            blocks[1],  # Block 1 (Challenge ID 19)
            blocks[2],  # Block 2 (cURL/F12 slides)
            blocks[3],  # Block 3 (Challenge ID 20)
            {
                "type": "markdown",
                "value": val_block_4
            },
            {
                "type": "markdown",
                "value": card_lab1
            },
            blocks[5],  # Challenge ID 21 (Lab 1)
            {
                "type": "markdown",
                "value": card_lab2
            },
            blocks[6],  # Challenge ID 22 (Lab 2)
            {
                "type": "markdown",
                "value": card_lab3
            },
            blocks[7],  # Challenge ID 23 (Lab 3)
            blocks[8],  # Block 8 (Automated Scanning Tools)
            blocks[9],  # Block 9 (Sandbox)
            blocks[10]  # Block 10 (Quiz)
        ]
        
        l.content = json.dumps(new_blocks, ensure_ascii=False)
        app.db.session.commit()
        print("SUCCESS: Redistributed Path Traversal cards into individual markdown blocks successfully!")
    except Exception as e:
        print("ERROR:", e)
        sys.exit(1)
