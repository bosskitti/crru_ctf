import json
import sys
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

old_card_signature = '<div style="background:#070a13;border:1px solid rgba(168,85,247,0.3);border-radius:12px;padding:24px;margin:2.5rem auto;max-width:1000px;box-shadow:0 10px 30px rgba(168,85,247,0.15);position:relative;overflow:hidden;">'

new_card_html = """<div style="background:#070a13;border:1px solid rgba(168,85,247,0.3);border-radius:12px;padding:24px;margin:2.5rem auto 1.5rem;max-width:1000px;box-shadow:0 10px 30px rgba(168,85,247,0.15);position:relative;overflow:hidden;">
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
</div>"""

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if not l:
        print("ERROR: Lesson 177 not found.")
        sys.exit(1)
        
    try:
        blocks = json.loads(l.content)
        val = blocks[2]["value"]
        
        # Locate the old card
        start_idx = val.find(old_card_signature)
        if start_idx == -1:
            print("ERROR: Old card signature not found in Block 2.")
            sys.exit(1)
            
        # Find the closing </div> of that card
        # Since the card has multiple nested divs, we search for </div> from the end of the button link
        end_marker = "</div>\n</div>"
        end_idx = val.find(end_marker, start_idx)
        if end_idx == -1:
            print("ERROR: Card end marker not found.")
            sys.exit(1)
            
        full_end_idx = end_idx + len(end_marker)
        
        # Perform replacement
        new_val = val[:start_idx] + new_card_html + val[full_end_idx:]
        blocks[2]["value"] = new_val
        l.content = json.dumps(blocks, ensure_ascii=False)
        app.db.session.commit()
        print("SUCCESS: Updated challenge card to a clean objective card inside Lesson 177!")
    except Exception as e:
        print("ERROR:", e)
        sys.exit(1)
