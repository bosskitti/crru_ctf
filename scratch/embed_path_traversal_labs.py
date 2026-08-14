import json
import sys
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

path_traversal_objective_card = """

<div style="background:#070a13;border:1px solid rgba(168,85,247,0.3);border-radius:12px;padding:24px;margin:2.5rem auto 1.5rem;max-width:1000px;box-shadow:0 10px 30px rgba(168,85,247,0.15);position:relative;overflow:hidden;">
  <!-- Neon decorative top bar -->
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg, #a855f7, #ff007f);"></div>
  
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
    <h4 style="margin:0;font-size:1.15rem;font-weight:800;color:#ffffff;display:flex;align-items:center;gap:8px;">
      <span style="font-size:1.3rem;">🎯</span> เป้าหมายการทำแล็บ (OBJECTIVES) - Path Traversal Suite
    </h4>
    <span style="font-size:0.68rem;font-family:monospace;font-weight:700;padding:3px 10px;border-radius:20px;background:rgba(168,85,247,0.1);color:#a855f7;border:1px solid rgba(168,85,247,0.25);">3 PRACTICAL LABS</span>
  </div>
  
  <p style="margin:0 0 16px;font-size:0.83rem;color:#cbd5e1;line-height:1.6;">
    ทดสอบความเข้าใจเกี่ยวกับการโจมตีช่องโหว่ Directory Traversal โดยนำความรู้เรื่องโครงสร้างของระบบ Linux (<strong>Linux Important Files & Sub-Trees Map</strong>) จากบทเรียนมาประยุกต์ใช้เพื่ออ่านไฟล์เป้าหมายที่อยู่ภายนอกเว็บเซิร์ฟเวอร์รูท:
  </p>
  
  <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(240px, 1fr));gap:15px;margin:0;">
    <!-- Card 1 -->
    <div style="background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:15px;">
      <span style="font-size:0.65rem;font-family:monospace;font-weight:700;padding:2px 6px;border-radius:10px;background:rgba(0, 240, 255, 0.1);color:#00f0ff;border:1px solid rgba(0, 240, 255, 0.2);display:inline-block;margin-bottom:8px;">LAB 1: APPRENTICE</span>
      <h5 style="margin:0 0 6px;font-size:0.85rem;color:#ffffff;font-weight:bold;">Simple Case</h5>
      <p style="margin:0;font-size:0.75rem;color:#94a3b8;line-height:1.4;">
        ย้อนพาธโดยไม่มีฟิลเตอร์คัดกรองเพื่ออ่านไฟล์รายชื่อบัญชีระบบ <code>/etc/passwd</code> นำข้อความ Flag ในคำอธิบายของ user <code>flag_user</code> มาส่งด้านล่าง
      </p>
    </div>

    <!-- Card 2 -->
    <div style="background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:15px;">
      <span style="font-size:0.65rem;font-family:monospace;font-weight:700;padding:2px 6px;border-radius:10px;background:rgba(168, 85, 247, 0.1);color:#a855f7;border:1px solid rgba(168, 85, 247, 0.2);display:inline-block;margin-bottom:8px;">LAB 2: PRACTITIONER</span>
      <h5 style="margin:0 0 6px;font-size:0.85rem;color:#ffffff;font-weight:bold;">Stripped Non-Recursively</h5>
      <p style="margin:0;font-size:0.75rem;color:#94a3b8;line-height:1.4;">
        ระบบกรองและลบคำว่า <code>../</code> ออกไป ให้เขียนบายพาสโดยใช้หลักการซ้อนพาธเพื่ออ่านไฟล์ล็อกระบบ <code>/var/log/httpd-access.log</code> และนำ Flag มาส่ง
      </p>
    </div>

    <!-- Card 3 -->
    <div style="background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:15px;">
      <span style="font-size:0.65rem;font-family:monospace;font-weight:700;padding:2px 6px;border-radius:10px;background:rgba(255, 0, 127, 0.1);color:#ff007f;border:1px solid rgba(255, 0, 127, 0.2);display:inline-block;margin-bottom:8px;">LAB 3: PRACTITIONER</span>
      <h5 style="margin:0 0 6px;font-size:0.85rem;color:#ffffff;font-weight:bold;">Prefix Validation</h5>
      <p style="margin:0;font-size:0.75rem;color:#94a3b8;line-height:1.4;">
        ระบบบังคับตรวจสอบให้พารามิเตอร์ขึ้นต้นด้วยโฟลเดอร์ภาพก่อนเสมอ เขียนบายพาสเพื่อไปเปิดอ่านประวัติและสภาพแวดล้อมสคริปต์ของรูท <code>/root/.bashrc</code>
      </p>
    </div>
  </div>
</div>
"""

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if not l:
        print("ERROR: Lesson 177 not found.")
        sys.exit(1)
        
    try:
        blocks = json.loads(l.content)
        print(f"Current blocks count: {len(blocks)}")
        
        # Check if already embedded to prevent double insertion
        if len(blocks) == 11 and blocks[5]["type"] == "challenge" and blocks[5].get("challenge_id") == 21:
            print("Path Traversal Lab blocks are already embedded.")
            sys.exit(0)
            
        if len(blocks) != 7:
            print("ERROR: Expected exactly 7 blocks before insert (after F12 split).")
            sys.exit(1)
            
        val_block_4 = blocks[4]["value"]
        
        # Find the start of the Automated Scanning Tools section
        tools_marker = "### 🛠️ เครื่องมืออัตโนมัติสำหรับการสแกนพาธ (Automated Scanning Tools)"
        idx = val_block_4.find(tools_marker)
        if idx == -1:
            print("ERROR: Tools marker not found in Block 4.")
            sys.exit(1)
            
        part4a = val_block_4[:idx].strip()
        part4b = val_block_4[idx:].strip()
        
        print(f"part4a length: {len(part4a)} chars")
        print(f"part4b length: {len(part4b)} chars")
        
        # Re-construct Block 4 to end with the path traversal objective card
        new_val_block_4 = part4a + path_traversal_objective_card
        
        # Re-construct blocks list with the 3 path traversal challenges natively embedded
        new_blocks = [
            blocks[0],  # Block 0 (HTTP Headers/Status Codes + Tampering card)
            blocks[1],  # Block 1 (Challenge ID 19 - Parameter Tampering console)
            blocks[2],  # Block 2 (cURL/F12 slides + F12 objective card)
            blocks[3],  # Block 3 (Challenge ID 20 - F12 view source console)
            {
                "type": "markdown",
                "value": new_val_block_4
            },
            {
                "type": "challenge",
                "challenge_id": 21
            },
            {
                "type": "challenge",
                "challenge_id": 22
            },
            {
                "type": "challenge",
                "challenge_id": 23
            },
            {
                "type": "markdown",
                "value": part4b
            },
            blocks[5],  # Sandbox (originally Block 5)
            blocks[6]   # Quiz (originally Block 6)
        ]
        
        l.content = json.dumps(new_blocks, ensure_ascii=False)
        app.db.session.commit()
        print("SUCCESS: Embedded 3 path traversal labs (ID 21, 22, 23) into Lesson 177 successfully!")
    except Exception as e:
        print("ERROR:", e)
        sys.exit(1)
