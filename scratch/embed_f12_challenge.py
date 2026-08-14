import json
import sys
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

f12_objective_card = """

<div style="background:#070a13;border:1px solid rgba(61,220,132,0.3);border-radius:12px;padding:24px;margin:2.5rem auto 1.5rem;max-width:1000px;box-shadow:0 10px 30px rgba(61,220,132,0.15);position:relative;overflow:hidden;">
  <!-- Neon decorative top bar -->
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg, #3ddc84, #00f0ff);"></div>
  
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
    <h4 style="margin:0;font-size:1.15rem;font-weight:800;color:#ffffff;display:flex;align-items:center;gap:8px;">
      <span style="font-size:1.3rem;">🎯</span> เป้าหมายการทำแล็บ (OBJECTIVE) - Web Source Code Inspection
    </h4>
    <span style="font-size:0.68rem;font-family:monospace;font-weight:700;padding:3px 10px;border-radius:20px;background:rgba(61,220,132,0.1);color:#3ddc84;border:1px solid rgba(61,220,132,0.25);">LAB MISSION</span>
  </div>
  
  <p style="margin:0 0 16px;font-size:0.83rem;color:#cbd5e1;line-height:1.6;">
    หลังจากได้เรียนรู้วิธีการทำงานของเครื่องมือนักพัฒนา (DevTools) และโครงสร้างซอร์สโค้ดของหน้าเว็บแล้ว ถึงเวลาค้นหาความลับที่อาจถูกมองข้าม!
  </p>
  
  <div style="background:rgba(0,0,0,0.25);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:16px;margin:0;">
    <h5 style="margin:0 0 8px;font-size:0.8rem;color:#fbbf24;font-weight:bold;text-transform:uppercase;letter-spacing:0.05em;">📌 ภารกิจการเจาะระบบ (Mission details)</h5>
    <ul style="margin:0;padding-left:20px;font-size:0.78rem;color:#94a3b8;line-height:1.6;">
      <li>ทำการคลิกขวาและเลือก <strong>View Page Source (ดูซอร์สโค้ดหน้าเว็บ)</strong> หรือเปิด <strong>F12 DevTools</strong> ของบราวเซอร์ในหน้านี้</li>
      <li>สืบค้นหาข้อความความลับหรือ Flag ที่ซ่อนอยู่ในคอมเมนต์ (HTML Comments) ใต้หัวข้อเครื่องมือแกะรหัสหน้าเว็บ</li>
      <li>ถอดรหัสข้อความ Base64 ที่ค้นพบเพื่อรับ Flag นำมาส่งในช่องส่งคำตอบด้านล่าง</li>
    </ul>
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
        
        # Verify if F12 challenge block is already inserted to prevent duplicate run
        if len(blocks) == 7 and blocks[3]["type"] == "challenge" and blocks[3].get("challenge_id") == 20:
            print("F12 Challenge block is already embedded.")
            sys.exit(0)
            
        if len(blocks) != 5:
            print("ERROR: Expected exactly 5 blocks before insert.")
            sys.exit(1)
            
        val_block_2 = blocks[2]["value"]
        
        # Find the start of the Path Traversal section
        path_traversal_marker = "### 📂 ช่องโหว่การไต่พาธระบบและข้ามไดเรกทอรี (Path and Directory Traversal)"
        idx = val_block_2.find(path_traversal_marker)
        if idx == -1:
            print("ERROR: Path Traversal marker not found in Block 2.")
            sys.exit(1)
            
        part2a = val_block_2[:idx].strip()
        part2b = val_block_2[idx:].strip()
        
        print(f"part2a length: {len(part2a)} chars")
        print(f"part2b length: {len(part2b)} chars")
        
        # Re-construct block 2 to end with the new objective card
        new_val_block_2 = part2a + f12_objective_card
        
        # Re-construct blocks list with the challenge embedded natively
        new_blocks = [
            blocks[0],  # Block 0 (HTTP Headers/Status Codes + Tampering card)
            blocks[1],  # Block 1 (Challenge ID 19 - Parameter Tampering console)
            {
                "type": "markdown",
                "value": new_val_block_2
            },
            {
                "type": "challenge",
                "challenge_id": 20
            },
            {
                "type": "markdown",
                "value": part2b
            },
            blocks[3],  # Sandbox (originally Block 3)
            blocks[4]   # Quiz (originally Block 4)
        ]
        
        l.content = json.dumps(new_blocks, ensure_ascii=False)
        app.db.session.commit()
        print("SUCCESS: Embedded standard challenge ID 20 into Lesson 177 successfully!")
    except Exception as e:
        print("ERROR:", e)
        sys.exit(1)
