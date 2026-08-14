from CTFd import create_app
from CTFd.models import db
from CTFd.plugins.tutorials import TutorialLesson
import json

app = create_app()
with app.app_context():
    l168 = TutorialLesson.query.get(168)
    cells = json.loads(l168.content)

    b4_accounts_rich = """### 👥 WINDOWS USER ACCOUNTS (ประเภทบัญชีผู้ใช้ในระบบ WINDOWS)

ระบบปฏิบัติการ Windows สนับสนุนการจัดการบัญชีผู้ใช้งานหลักทั้งหมด 5 ประเภท เพื่อจัดสรรสิทธิ์และควบคุมระดับความปลอดภัยในลักษณะที่แตกต่างกัน:

<style>
.w-acc-cyber-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 22px; margin: 2rem 0; width: 100%; box-sizing: border-box; }

.w-acc-cyber-card { background: rgba(12, 15, 29, 0.85); border-radius: 14px; padding: 26px 22px; display: flex; flex-direction: column; align-items: center; text-align: center; transition: all 0.25s ease; box-sizing: border-box; overflow: hidden; width: 100%; position: relative; }
.w-acc-cyber-card:hover { transform: translateY(-4px); }
.w-acc-cyber-icon { width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.65rem; margin-bottom: 14px; flex-shrink: 0; }
.w-acc-cyber-title { font-size: 1.15rem; font-weight: 800; color: #ffffff; margin-bottom: 6px; }
.w-acc-cyber-badge { padding: 4px 14px; border-radius: 20px; font-size: 0.72rem; font-family: 'JetBrains Mono', monospace; font-weight: 700; margin-bottom: 18px; text-transform: uppercase; letter-spacing: 0.05em; }
.w-acc-cyber-list { text-align: left; padding-left: 0; list-style: none; margin: 0; font-size: 0.86rem; color: #cbd5e1; line-height: 1.7; width: 100%; word-break: break-word; overflow-wrap: break-word; }
.w-acc-cyber-item { margin-bottom: 10px; display: flex; align-items: flex-start; gap: 10px; }
.w-acc-cyber-item:last-child { margin-bottom: 0; }
.w-acc-cyber-bullet { flex-shrink: 0; font-weight: bold; font-size: 0.95rem; margin-top: 1px; }
.w-acc-cyber-list code { font-family: "JetBrains Mono", monospace; font-size: 0.78rem; word-break: break-all; overflow-wrap: anywhere; white-space: normal; background: rgba(0, 240, 255, 0.1); color: #38bdf8; border: 1px solid rgba(0, 240, 255, 0.25); padding: 1px 6px; border-radius: 4px; display: inline-block; box-sizing: border-box; }
</style>

<div class="w-acc-cyber-grid">
  <!-- 1. Administrator (Pink/Magenta) -->
  <div class="w-acc-cyber-card" style="border: 1px solid rgba(255, 0, 127, 0.35); box-shadow: 0 0 22px rgba(255, 0, 127, 0.1);">
    <div class="w-acc-cyber-icon" style="background: rgba(255, 0, 127, 0.15); border: 1px solid rgba(255, 0, 127, 0.4);">👑</div>
    <div class="w-acc-cyber-title">Administrator</div>
    <span class="w-acc-cyber-badge" style="background: rgba(255, 0, 127, 0.15); color: #ff007f; border: 1px solid #ff007f;">SUPER ADMIN</span>
    <ul class="w-acc-cyber-list">
      <li class="w-acc-cyber-item"><span class="w-acc-cyber-bullet" style="color: #ff007f;">⚡</span><div><strong>สิทธิ์สูงสุดไร้ข้อจำกัด:</strong> มีอำนาจในการสร้าง ลบ และจัดการบัญชีผู้ใช้งานอื่นทั้งหมดในเครื่อง</div></li>
      <li class="w-acc-cyber-item"><span class="w-acc-cyber-bullet" style="color: #ff007f;">⚡</span><div><strong>ผู้ดูแลระบบหลัก (Admin):</strong> เปิด อ่าน แก้ไข และลบไฟล์โครงสร้างระบบ รวมถึงปรับเปลี่ยนคอนฟิกความปลอดภัยและติดตั้งซอฟต์แวร์ได้ทุกชนิด</div></li>
    </ul>
  </div>

  <!-- 2. SYSTEM Account (Green/Emerald) -->
  <div class="w-acc-cyber-card" style="border: 1px solid rgba(16, 185, 129, 0.35); box-shadow: 0 0 22px rgba(16, 185, 129, 0.1);">
    <div class="w-acc-cyber-icon" style="background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(16, 185, 129, 0.4);">⚙️</div>
    <div class="w-acc-cyber-title">SYSTEM User</div>
    <span class="w-acc-cyber-badge" style="background: rgba(16, 185, 129, 0.15); color: #10b981; border: 1px solid #10b981;">CORE KERNEL</span>
    <ul class="w-acc-cyber-list">
      <li class="w-acc-cyber-item"><span class="w-acc-cyber-bullet" style="color: #10b981;">⚡</span><div><strong>สิทธิ์ระดับเคอร์เนล (Local System):</strong> บัญชีบริการระบบระดับสูงสุดที่มีสิทธิ์เหนือกว่า Administrator ในการเข้าถึงและควบคุมทรัพยากรระบบป้องกัน</div></li>
      <li class="w-acc-cyber-item"><span class="w-acc-cyber-bullet" style="color: #10b981;">⚡</span><div><strong>ไร้หน้าต่างล็อกอิน:</strong> ทำหน้าที่รัน Background Services และกระบวนการแกนกลางของ Windows (เช่น <code>lsass.exe</code>, <code>services.exe</code>) โดยอัตโนมัติ</div></li>
    </ul>
  </div>

  <!-- 3. Standard User (Cyan) -->
  <div class="w-acc-cyber-card" style="border: 1px solid rgba(0, 240, 255, 0.35); box-shadow: 0 0 22px rgba(0, 240, 255, 0.1);">
    <div class="w-acc-cyber-icon" style="background: rgba(0, 240, 255, 0.15); border: 1px solid rgba(0, 240, 255, 0.4);">👤</div>
    <div class="w-acc-cyber-title">Standard User</div>
    <span class="w-acc-cyber-badge" style="background: rgba(0, 240, 255, 0.15); color: #00f0ff; border: 1px solid #00f0ff;">STANDARD USER</span>
    <ul class="w-acc-cyber-list">
      <li class="w-acc-cyber-item"><span class="w-acc-cyber-bullet" style="color: #00f0ff;">⚡</span><div><strong>ผู้ใช้ทั่วไปประจำวัน:</strong> สำหรับการทำงานเอกสาร ท่องเว็บ หรือใช้งานโปรแกรมประยุกต์ทั่วไป โดยไม่สามารถเปลี่ยนค่าระบบหลักหรือลบไฟล์สำคัญของเครื่องได้</div></li>
      <li class="w-acc-cyber-item"><span class="w-acc-cyber-bullet" style="color: #00f0ff;">⚡</span><div><strong>สิทธิ์จำกัด (Least Privilege):</strong> มีขอบเขตพื้นที่ทำงานส่วนตัวเฉพาะภายในโฟลเดอร์ <code>C:\\Users\\Username</code> เพื่อป้องกันไม่ให้กระทบต่อผู้อื่น</div></li>
    </ul>
  </div>

  <!-- 4. Child Account (Yellow/Amber) -->
  <div class="w-acc-cyber-card" style="border: 1px solid rgba(251, 191, 36, 0.35); box-shadow: 0 0 22px rgba(251, 191, 36, 0.1);">
    <div class="w-acc-cyber-icon" style="background: rgba(251, 191, 36, 0.15); border: 1px solid rgba(251, 191, 36, 0.4);">🧸</div>
    <div class="w-acc-cyber-title">Child Account</div>
    <span class="w-acc-cyber-badge" style="background: rgba(251, 191, 36, 0.15); color: #fbbf24; border: 1px solid #fbbf24;">RESTRICTED</span>
    <ul class="w-acc-cyber-list">
      <li class="w-acc-cyber-item"><span class="w-acc-cyber-bullet" style="color: #fbbf24;">⚡</span><div><strong>บัญชีบุตรหลาน:</strong> บัญชี Standard User พิเศษที่ได้รับการดูแลและเปิดใช้งานระบบ Parental Controls ควบคุมโดยผู้ปกครอง</div></li>
      <li class="w-acc-cyber-item"><span class="w-acc-cyber-bullet" style="color: #fbbf24;">⚡</span><div><strong>การคัดกรองความปลอดภัย:</strong> ดักกรองเว็บไซต์ไม่เหมาะสม จำกัดช่วงเวลาใช้งานคอมพิวเตอร์ และส่งรายงานประวัติกิจกรรมแก่ผู้ปกครอง</div></li>
    </ul>
  </div>

  <!-- 5. Guest Account (Purple/Violet) -->
  <div class="w-acc-cyber-card" style="border: 1px solid rgba(168, 85, 247, 0.35); box-shadow: 0 0 22px rgba(168, 85, 247, 0.1);">
    <div class="w-acc-cyber-icon" style="background: rgba(168, 85, 247, 0.15); border: 1px solid rgba(168, 85, 247, 0.4);">👥</div>
    <div class="w-acc-cyber-title">Guest Account</div>
    <span class="w-acc-cyber-badge" style="background: rgba(168, 85, 247, 0.15); color: #c084fc; border: 1px solid #a855f7;">TEMPORARY</span>
    <ul class="w-acc-cyber-list">
      <li class="w-acc-cyber-item"><span class="w-acc-cyber-bullet" style="color: #c084fc;">⚡</span><div><strong>ผู้ใช้ชั่วคราว:</strong> บัญชีสิทธิ์ต่ำสุดสำหรับเปิดให้บุคคลภายนอกเข้าใช้งานเครื่องชั่วคราวโดยไม่ต้องใช้รหัสผ่าน</div></li>
      <li class="w-acc-cyber-item"><span class="w-acc-cyber-bullet" style="color: #c084fc;">⚡</span><div><strong>ไม่บันทึกค่าถาวร:</strong> ไม่สามารถตั้งค่าระบบ ไม่สามารถติดตั้งซอฟต์แวร์ และไฟล์ทั้งหมดจะถูกลบทิ้งเมื่อออกจากระบบ</div></li>
    </ul>
  </div>
</div>"""

    for idx, c in enumerate(cells):
        if "WINDOWS USER ACCOUNTS" in c.get("value", ""):
            cells[idx]["value"] = b4_accounts_rich
            print("Updated cell", idx, "with b4_accounts_rich!")

    l168.content = json.dumps(cells, ensure_ascii=False)
    db.session.commit()
    print("SUCCESSFULLY RESTORED FULL DETAILED RICH TEXT CONTENT FOR ALL 5 WINDOWS USER ACCOUNTS!")
