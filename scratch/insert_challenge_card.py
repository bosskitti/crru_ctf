import json
import sys
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

challenge_card_html = """

<div style="background:#070a13;border:1px solid rgba(168,85,247,0.3);border-radius:12px;padding:24px;margin:2.5rem auto;max-width:1000px;box-shadow:0 10px 30px rgba(168,85,247,0.15);position:relative;overflow:hidden;">
  <!-- Neon decorative top bar -->
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg, #a855f7, #ec4899);"></div>
  
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
    <h4 style="margin:0;font-size:1.15rem;font-weight:800;color:#ffffff;display:flex;align-items:center;gap:8px;">
      <span style="font-size:1.3rem;">🎯</span> CTF Challenge: Web Parameter Tampering (การทดลองบิดเบือนพารามิเตอร์)
    </h4>
    <span style="font-size:0.68rem;font-family:monospace;font-weight:700;padding:3px 10px;border-radius:20px;background:rgba(168,85,247,0.1);color:#a855f7;border:1px solid rgba(168,85,247,0.25);">TUTORIAL CATEGORY</span>
  </div>
  
  <p style="margin:0 0 16px;font-size:0.83rem;color:#cbd5e1;line-height:1.6;">
    หลังจากได้เรียนรู้วิธีการทำงานของโปรโตคอล HTTP และโครงสร้างของพารามิเตอร์แล้ว ถึงเวลาทดสอบฝีมือจริงในระบบจำลองช่องโหว่ประเภท <strong>Broken Access Control</strong> ผ่านเทคนิค Parameter Tampering!
  </p>
  
  <div style="background:rgba(0,0,0,0.25);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:16px;margin-bottom:20px;">
    <h5 style="margin:0 0 8px;font-size:0.8rem;color:#fbbf24;font-weight:bold;text-transform:uppercase;letter-spacing:0.05em;">📌 ภารกิจการเจาะระบบ (Mission details)</h5>
    <ul style="margin:0;padding-left:20px;font-size:0.78rem;color:#94a3b8;line-height:1.6;">
      <li>สมัครสมาชิกใหม่ในหน้าเว็บไซต์เป้าหมาย แล้วศึกษารูปแบบ HTTP Request ที่ส่งออกไป</li>
      <li>สืบหาและดักจับ (Intercept) พารามิเตอร์ที่ควบคุมระดับสิทธิ์ (เช่น สิทธิ์ผู้ใช้งานทั่วไป/แอดมิน)</li>
      <li>ทำการดัดแปลงค่าพารามิเตอร์ดังกล่าว (Parameter Tampering) จากฝั่งไคลเอนต์ให้เป็นสิทธิ์ผู้ดูแลระบบ (Admin) เพื่อเข้าถึงความลับและช่วงชิง Flag</li>
    </ul>
  </div>
  
  <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:14px;background:rgba(168,85,247,0.03);border:1px solid rgba(168,85,247,0.1);border-radius:8px;padding:12px 18px;">
    <div style="display:flex;align-items:center;gap:10px;">
      <span style="font-size:1.1rem;">🚀</span>
      <span style="font-size:0.78rem;color:#cbd5e1;font-weight:600;">พร้อมเริ่มทำคำท้าทายนี้แล้วหรือยัง?</span>
    </div>
    <a href="/challenges" style="background:linear-gradient(135deg,#a855f7,#7c3aed);border:none;color:#ffffff;font-size:0.78rem;font-weight:bold;padding:8px 20px;border-radius:6px;text-decoration:none;box-shadow:0 4px 12px rgba(124,58,237,0.3);transition:all 0.2s;" onmouseover="this.style.transform='translateY(-1px)';this.style.boxShadow='0 6px 16px rgba(124,58,237,0.4)';" onmouseout="this.style.transform='none';this.style.boxShadow='0 4px 12px rgba(124,58,237,0.3)';">
      <i class="fas fa-flag mr-1"></i> ไปที่หน้า Challenges ของระบบ
    </a>
  </div>
</div>
"""

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        try:
            blocks = json.loads(l.content)
            val = blocks[0]["value"]
            
            # Target string to insert after
            target_str = "[🔗 คู่มือวิเคราะห์ HTTP Status Codes และการตรวจสอบสิทธิ์ความปลอดภัย](#http-status-codes-details)"
            
            # Check if card is already inserted to prevent double insertion
            if "CTF Challenge: Web Parameter Tampering" in val:
                print("Card is already inserted in Lesson 177 Block 0.")
                sys.exit(0)
                
            idx = val.find(target_str)
            if idx != -1:
                insert_pos = idx + len(target_str)
                new_val = val[:insert_pos] + challenge_card_html + val[insert_pos:]
                blocks[0]["value"] = new_val
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print("SUCCESS: Challenge card inserted into Lesson 177 Block 0!")
            else:
                print("ERROR: Target insertion marker string not found in Lesson 177 Block 0.")
                sys.exit(1)
        except Exception as e:
            print("ERROR:", e)
            sys.exit(1)
    else:
        print("ERROR: Lesson 177 not found in database.")
        sys.exit(1)
