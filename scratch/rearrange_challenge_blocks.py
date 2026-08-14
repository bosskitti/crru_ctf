import json
import sys
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

new_card_html = """

<div style="background:#070a13;border:1px solid rgba(168,85,247,0.3);border-radius:12px;padding:24px;margin:2.5rem auto 1.5rem;max-width:1000px;box-shadow:0 10px 30px rgba(168,85,247,0.15);position:relative;overflow:hidden;">
  <!-- Neon decorative top bar -->
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg, #a855f7, #ec4899);"></div>
  
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
    <h4 style="margin:0;font-size:1.15rem;font-weight:800;color:#ffffff;display:flex;align-items:center;gap:8px;">
      <span style="font-size:1.3rem;">🎯</span> เป้าหมายการทำแล็บ (OBJECTIVE) - Web Parameter Tampering
    </h4>
    <span style="font-size:0.68rem;font-family:monospace;font-weight:700;padding:3px 10px;border-radius:20px;background:rgba(168,85,247,0.1);color:#a855f7;border:1px solid rgba(168,85,247,0.25);">LAB MISSION</span>
  </div>
  
  <p style="margin:0 0 16px;font-size:0.83rem;color:#cbd5e1;line-height:1.6;">
    หลังจากได้เรียนรู้วิธีการทำงานของโปรโตคอล HTTP และโครงสร้างของพารามิเตอร์แล้ว ถึงเวลาทดสอบฝีมือจริงในระบบจำลองช่องโหว่ประเภท <strong>Broken Access Control</strong> ผ่านเทคนิค Parameter Tampering!
  </p>
  
  <div style="background:rgba(0,0,0,0.25);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:16px;margin:0;">
    <h5 style="margin:0 0 8px;font-size:0.8rem;color:#fbbf24;font-weight:bold;text-transform:uppercase;letter-spacing:0.05em;">📌 ภารกิจการเจาะระบบ (Mission details)</h5>
    <ul style="margin:0;padding-left:20px;font-size:0.78rem;color:#94a3b8;line-height:1.6;">
      <li>สมัครสมาชิกใหม่ในหน้าเว็บไซต์เป้าหมาย แล้วศึกษารูปแบบ HTTP Request ที่ส่งออกไป</li>
      <li>สืบหาและดักจับ (Intercept) พารามิเตอร์ที่ควบคุมระดับสิทธิ์ (เช่น สิทธิ์ผู้ใช้งานทั่วไป/แอดมิน)</li>
      <li>ทำการดัดแปลงค่าพารามิเตอร์ดังกล่าว (Parameter Tampering) จากฝั่งไคลเอนต์ให้เป็นสิทธิ์ผู้ดูแลระบบ (Admin) เพื่อเข้าถึงความลับและช่วงชิง Flag</li>
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
        if len(blocks) != 5:
            print(f"ERROR: Expected 5 blocks, found {len(blocks)}.")
            sys.exit(1)
            
        val_block_0 = blocks[0]["value"]
        val_block_2 = blocks[2]["value"]
        
        # Clean up Block 2 (remove the HTML card at the beginning)
        # Search for the start of the cURL section
        curl_marker = "### 🛠️ การใช้งานเครื่องมือ cURL"
        idx_curl = val_block_2.find(curl_marker)
        if idx_curl == -1:
            print("ERROR: cURL marker not found in Block 2.")
            sys.exit(1)
            
        # Find the preceding horizontal rule separator ---
        idx_sep = val_block_2.rfind("---", 0, idx_curl)
        if idx_sep == -1:
            # If not found, split at the start of cURL
            print("WARNING: --- separator not found, splitting at cURL header directly.")
            clean_val_block_2 = val_block_2[idx_curl:]
        else:
            clean_val_block_2 = val_block_2[idx_sep:]
            
        # Update Block 2
        blocks[2]["value"] = clean_val_block_2
        print("SUCCESS: Cleaned up Block 2 starting content.")
        
        # Update Block 0: Append the new objective card (without bottom button)
        # First ensure we don't have duplicate objective card text in Block 0
        if "เป้าหมายการทำแล็บ (OBJECTIVE) - Web Parameter Tampering" in val_block_0:
            print("Objective card already exists in Block 0.")
        else:
            blocks[0]["value"] = val_block_0.strip() + new_card_html
            print("SUCCESS: Appended clean objective card to the end of Block 0.")
            
        l.content = json.dumps(blocks, ensure_ascii=False)
        app.db.session.commit()
        print("SUCCESS: Database committed!")
    except Exception as e:
        print("ERROR:", e)
        sys.exit(1)
