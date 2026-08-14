import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

def save_lesson(lid, val0, val1, val2):
    l = db.session.query(TutorialLesson).filter_by(id=lid).first()
    blocks = [
        {"type": "markdown", "value": val0},
        {"type": "markdown", "value": val1},
        {"type": "markdown", "value": val2}
    ]
    l.content = json.dumps(blocks, ensure_ascii=False)
    db.session.query(TutorialLesson).filter_by(id=lid).update({"content": l.content})
    db.session.commit()
    print(f"Lesson {lid} successfully upgraded!")

# ─── Lesson 177 ───
val177_0 = """## 🌐 Web Application Security & OWASP (สถาปัตยกรรมเว็บแอปและความรู้เบื้องต้น)
---

ยินดีต้อนรับสู่บทเรียนสถาปัตยกรรมเว็บแอปและความเข้าใจเชิงความมั่นคงปลอดภัยตามมาตรฐาน OWASP

### 📄 SLIDE 1-3: ภาพรวมวิทยาการการโจมตีเว็บ (Web Exploitations)
- **Web Exploitation**: หมายถึงกระบวนการค้นหา วิเคราะห์ และการใช้ประโยชน์จากช่องโหว่ความมั่นคงปลอดภัยในแอปพลิเคชันเว็บ เพื่อเข้าถึงข้อมูลโดยไม่ได้รับอนุญาต (Unauthorized Access), ดึงสารสนเทศที่เป็นความลับ หรือครอบครองสิทธิ์การเข้าถึงระบบควบคุมเซิร์ฟเวอร์หลังบ้าน
- เป็นแกนหลักที่สำคัญมากในสายงานความปลอดภัยไซเบอร์ โดยเฉพาะอย่างยิ่งในการทำงานด้าน **การเจาะระบบแบบมีคุณธรรม (Ethical Hacking)** และ **การทดสอบเจาะระบบ (Penetration Testing)**

---

### 📄 SLIDE 4-8: มาตรฐานความเสี่ยง OWASP Top 10
- **OWASP Top 10**: เป็นเอกสารรายงานเชิงความมั่นคงสากลที่ชี้เป้า 10 อันดับความเสี่ยงสูงสุดที่เป็นอันตรายต่อแอปพลิเคชันเว็บ โดยจัดทำและเผยแพร่โดยองค์กรไม่แสวงหากำไร **Open Web Application Security Project (OWASP)** เพื่อให้นักพัฒนาและผู้ดูแลระบบนำไปตั้งรับและแก้ไข
- การปรับปรุงมาตรฐานเกิดขึ้นเป็นรอบปี โดยมีรุ่นแก้ไขสำคัญ ได้แก่ รุ่น 2003 (รุ่นแรก), 2004, 2007, 2010, 2013, 2017, 2021 และรุ่นล่าสุดในปัจจุบัน **(OWASP Top 10 Release 2025/2026)**

---

### 📄 SLIDE 9-28: รายละเอียดช่องโหว่ OWASP Top 10 (A01 - A10)

#### 🛡️ A01:2025 - Broken Access Control
- **คำจำกัดความ**: เกิดขึ้นเมื่อระบบไม่บังคับการควบคุมสิทธิ์อย่างถูกต้อง ทำให้ผู้ใช้ธรรมดาสามารถข้ามไปดึงข้อมูลหรือเข้าถึงฟังก์ชันระดับสูงที่ตนเองไม่มีสิทธิ์ใช้งาน
- **ผลกระทบ**: นำไปสู่การเข้าถึง แก้ไข หรือลบข้อมูลสำคัญโดยมิชอบ
- **ตัวอย่าง**:
  - การแอบเข้าถึงหน้าจัดการแอดมินหลังบ้านตรงๆ โดยไม่ผ่านการล็อกอิน (เช่น พิมพ์เข้าทาง `/admin` หรือ `/dashboard` ตรงๆ)
  - การเปลี่ยนตัวเลขพารามิเตอร์เพื่อเข้าดูข้อมูลผู้ใช้อื่น เช่น เปลี่ยน URL จาก `/profile/view/12345` เป็น `/profile/view/12346`
  - การปลอมแปลงค่า JSON Web Token (JWT) เพื่อยกระดับสิทธิ์ตัวเอง

#### 🛡️ A02:2025 - Security Misconfiguration
- **คำจำกัดความ**: เกิดขึ้นจากการกำหนดสิทธิ์และการตั้งค่าความปลอดภัยของแอปพลิเคชัน เซิร์ฟเวอร์ หรือฐานข้อมูลไม่รัดกุมเพียงพอ
- **ตัวอย่าง**:
  - การปล่อยบัญชีและรหัสผ่านเริ่มต้นของระบบไว้ เช่น `admin:admin` หรือ `root:root`
  - การเปิดสิทธิ์การเข้าถึงสารบัญโฟลเดอร์แบบดิบ (Directory Listing Enabled) เช่น พิมพ์เข้าเว็บแล้วเห็นรายการไฟล์ใน `/var/www/html/` ทั้งหมด
  - การปล่อยให้เปิดใช้งานระบบดีบั๊กในโหมด Production ทำให้หน้าเว็บแสดงรหัสผ่านหรือ stack trace ยาวเหยียดเมื่อระบบเอเรอร์

#### 🛡️ A03:2025 - Software Supply Chain Failures
- **คำจำกัดความ**: ความเสี่ยงจากการใช้ไลบรารี สัญญาภายนอก หรือซอร์สโค้ดเฟรมเวิร์กของผู้พัฒนาอื่นมาพัฒนาเว็บแอปพลิเคชัน ซึ่งผู้สืบทอดไม่ได้ตรวจสอบสิทธิ์และถูกโจมตีแฝงมัลแวร์
- **ตัวอย่าง**: การเรียกใช้งาน NPM, Pip หรือ Composer package ที่ถูกแฮกเกอร์แอบอัปเดตเวอร์ชันใหม่ประสงค์ร้ายเพื่อส่งขโมยตัวแปรระบบ (.env) ออกไป

#### 🛡️ A04:2025 - Cryptographic Failures
- **คำจำกัดความ**: ความเสี่ยงที่เกิดจากการใช้กลไกเข้ารหัสที่ไม่รัดกุม หรือความบกพร่องในการปกป้องข้อมูลที่เป็นความลับ
- **ตัวอย่าง**:
  - การเก็บรหัสผ่านผู้เรียนในฐานข้อมูลเป็นข้อความธรรมดา (Plaintext) แทนที่จะคำนวณแฮช
  - การประยุกต์ใช้อัลกอริทึมเข้ารหัสโบราณที่มีลูปชนกันง่าย เช่น MD5, SHA-1 หรือกุญแจเข้ารหัสลับขนาดเล็กเกินไป

#### 🛡️ A05:2025 - Injection (SQLi, XSS, Command Injection)
- **คำจำกัดความ**: การที่ระบบนำข้อมูลอินพุตจากผู้ใช้ไปรวมเข้าเป็นคำสั่งประมวลผลระบบหลังบ้านโดยไม่มีการคัดกรองอักขระพิเศษออกไปก่อน
- **ตัวอย่าง**:
  - **SQL Injection**: การแทรกคำสั่งคิวรีเพื่อดึงข้อมูลทั้งหมดจากฐานข้อมูล
  - **Cross-Site Scripting (XSS)**: การฝังแทรกสคริปต์ JavaScript ประสงค์ร้ายเข้ามาทำงานในบราวเซอร์ผู้ใช้
  - **Command Injection**: การแทรกคำสั่ง Command Line เพื่อควบคุมสั่งการเซิร์ฟเวอร์ตรงๆ

#### 🛡️ A06:2025 - Insecure Design
- **คำจำกัดความ**: ช่องโหว่จากการวางโครงสร้างสถาปัตยกรรมและตรรกะระบบตั้งแต่เริ่มออกแบบโดยไม่มีการจำลองภัยคุกคาม (Threat Modeling)
- **ตัวอย่าง**: ระบบยอมให้แก้ไขรหัสผ่านได้ทันทีโดยไม่ต้องกรอกรหัสผ่านเก่า เพื่อยืนยันตัวตน หรือการไม่มีฟังก์ชัน Rate Limiting ป้องกันการเดารหัสผ่านซ้ำๆ

#### 🛡️ A07:2025 - Authentication Failures
- **คำจำกัดความ**: ความบกพร่องของระบบตรวจรับและอนุญาตสิทธิ์การล็อกอินเข้าใช้งานระบบ
- **ตัวอย่าง**: ระบบยอมรับรหัสผ่านที่สั้นและคาดเดาง่าย เช่น `123456` หรือการไม่มีระบบ Account Lockout เพื่อสั่งล็อกผู้ใช้งานชั่วคราวเมื่อเดารหัสผิดเกินกำหนด

#### 🛡️ A08:2025 - Software and Data Integrity Failures
- **คำจำกัดความ**: ความบกพร่องในการทบทวนความถูกต้องของตัวติดตั้ง การอัปเดตระบบ หรือโครงสร้างข้อมูลแบบ serialize
- **ตัวอย่าง**: การปล่อยให้ผู้ใช้ส่งข้อมูล serialize object ที่ปรับเปลี่ยนสิทธิ์เข้าไปทำงานโดยไม่ตรวจสอบ signature ความปลอดภัยก่อน

#### 🛡️ A09:2025 - Security Logging and Monitoring Failures
- **คำจำกัดความ**: การไม่ได้ตั้งค่าจัดทำบันทึกประวัติการใช้สิทธิ์ (Log Files) หรือระบบแจ้งเตือนเมื่อเกิดกรณีการยิงแทรกคำสั่งผิดปกติ
- **ตัวอย่าง**: ระบบโดนทดสอบยิงรหัสผ่านล็อกอินเป็นหมื่นครั้ง แต่ไม่มีประวัติล็อกใดๆ บันทึกขึ้น ทำให้แฮกเกอร์โจมตีได้อย่างยาวนานโดยไม่ถูกตรวจพบ

#### 🛡️ A10:2025 - Mishandling of Exceptional Conditions
- **คำจำกัดความ**: ระบบจัดการกับสถานการณ์เอเรอร์ที่คาดเดาไม่ได้อย่างหละหลวม ส่งผลให้ข้ามขั้นตอนการยืนยันตัวตนหรืออนุญาตสิทธิ์เข้าถึงระบบไปอย่างง่ายดาย

---

### 📄 SLIDE 29-41: Web Page Source Inspections (F12 Developer Tools)
การแกะรหัสหน้าเว็บ (Inspect Elements) ช่วยให้นักทดสอบเจาะระบบและนักพัฒนาเข้าใจการทำงานของเว็บ:
- **ปุ่มลัดการเรียกใช้งาน**: กด `F12` หรือ `Ctrl + Shift + I` (Windows), `Cmd + Option + I` (Mac)
- **การดูซอร์สโค้ดดิบ (View Page Source)**: กด `Ctrl + U` (Windows) หรือคลิกขวาแล้วเลือก "ดูซอร์สโค้ดหน้าเว็บ"
- **การดัดแปลง HTML สด (Modifying HTML)**:
  - ช่วยให้นักโจมตีตรวจสอบ input ของแบบฟอร์มที่ถูกซ่อนอยู่ เช่น การเปลี่ยน `type="hidden"` เป็น `type="text"` เพื่อแสดงกล่องป้อนข้อมูลลับบนหน้าเว็บที่โปรแกรมเมอร์ซ่อนไว้
- **การดัดแปลง CSS (Modifying CSS)**:
  - การแอบดูและแก้ไขสไตล์หน้าเว็บสดเพื่อดึงข้อมูลที่ถูกปิดซ่อนผ่านสไตล์ความปลอดภัยหลวมๆ (เช่น ลบสไตล์ `display: none;` ของหน้าต่างล็อกสิทธิ์ทิ้ง)
- **การดีบั๊ก JavaScript (Debugging JS)**:
  - การวิเคราะห์สคริปต์ใน Sources tab และใส่ Breakpoint เพื่อหยุดพักตัวแปร ช่วยในการข้ามขั้นตอนยืนยันสิทธิ์ฝั่งผู้ใช้งาน (Client-Side Validation Bypass)

---

### 📄 SLIDE 42-45: Web Cookies Explorations
- **HTTP Cookies**: บล็อกข้อมูลขนาดเล็กที่เว็บเซิร์ฟเวอร์ส่งมาเก็บบันทึกบนบราวเซอร์ของผู้ใช้เพื่อใช้รักษาสถานะล็อกอิน (Session)
- **สเปกฟิลด์คุกกี้ที่สำคัญ (Cookie Attributes)**:
  - **HttpOnly**: มีความสำคัญสูงมากในการปิดกั้นไม่ให้โค้ด JavaScript (ผ่านคำสั่ง `document.cookie`) เข้าถึงตัวคุกกี้ได้ ช่วยลดทอนภัยคุกคามจากการขโมยเซสชันผ่านช่องโหว่ XSS
  - **Secure**: บังคับให้ส่งคุกกี้เฉพาะกรณีการรันผ่านช่องทางปลอดภัย HTTPS เท่านั้น
  - **SameSite**: ป้องกันการจู่โจมข้ามค่ายเชิงปลอมแปลงคำสั่ง (CSRF)

---

### 📄 SLIDE 46-50: Path and Directory Traversal
- **Directory Traversal**: ช่องโหว่ที่ช่วยให้แฮกเกอร์ใช้ประโยชน์จากช่องอินพุตประเภทอ้างอิงตำแหน่งไฟล์ ขยับขยับตำแหน่งออกจากรากเว็บบอร์ดขึ้นมาดึงไฟล์สำคัญของระบบ เช่น `../../../../etc/passwd`
- **Robots.txt**: เป็นเอกสารข้อกำหนดที่นักพัฒนาใส่ไว้ในเว็บเพื่อห้ามบอต (Search Engine) มาดึงข้อมูลหน้าเพจที่เป็นความลับ แต่แฮกเกอร์มักเปิดดูไฟล์นี้เพื่อค้นหาที่ตั้ง of แผงแอดมินหรือแบ็คอัปฐานข้อมูลได้ทันที"""

val177_1 = """### 💻 HTTP Headers Diagnostic Sandbox (จำลองวิเคราะห์โครงสร้างข้อมูลเว็บ)

คลิกหัวข้อด้านซ้ายมือเพื่อจำลองวิเคราะห์โครงสร้าง และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อตรวจสอบทราฟฟิกข้อมูล:

<style type="text/css">
.w-sandbox-main { display: flex !important; gap: 20px !important; margin: 1.5rem auto !important; max-width: 1000px !important; }
.w-sandbox-nav { width: 220px !important; display: flex !important; flex-direction: column !important; gap: 8px !important; flex-shrink: 0 !important; }
.w-nav-item { background: rgba(255, 255, 255, 0.02) !important; border: 1px solid rgba(255, 255, 255, 0.06) !important; border-radius: 6px !important; padding: 10px 14px !important; color: #cbd5e1 !important; text-align: left !important; cursor: pointer !important; font-size: 0.78rem !important; transition: all 0.2s !important; }
.w-nav-item:hover, .w-nav-item.active { border-color: #00f0ff !important; color: #ffffff !important; background: rgba(0, 240, 255, 0.05) !important; }
.w-nav-item.active { font-weight: 700 !important; box-shadow: 0 0 8px rgba(0, 240, 255, 0.15) !important; }
.w-sandbox-panels { flex-grow: 1 !important; display: flex !important; flex-direction: column !important; gap: 14px !important; }
.w-sand-panel { display: none; background: #05070f !important; border: 1px solid rgba(255, 255, 255, 0.08) !important; border-radius: 10px !important; padding: 20px !important; box-shadow: 0 8px 24px rgba(0,0,0,0.45) !important; }
.w-sand-panel.active { display: block !important; }
</style>
<div class="w-sandbox-main" style="display: flex; gap: 20px; margin: 1.5rem auto; max-width: 1000px;">
<div class="w-sandbox-nav" style="width: 220px; display: flex; flex-direction: column; gap: 8px; flex-shrink: 0;">
<button id="nav-item-httpget" class="w-nav-item active" style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 6px; padding: 10px 14px; color: #cbd5e1; text-align: left; cursor: pointer; font-size: 0.78rem; transition: all 0.2s;" onclick="showSandboxItem('httpget', this)">1. Send HTTP GET</button>
<button id="nav-item-httppost" class="w-nav-item" style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 6px; padding: 10px 14px; color: #cbd5e1; text-align: left; cursor: pointer; font-size: 0.78rem; transition: all 0.2s;" onclick="showSandboxItem('httppost', this)">2. Send HTTP POST</button>
</div>
<div class="w-sandbox-panels" style="flex-grow: 1; display: flex; flex-direction: column; gap: 14px;">
<div id="panel-httpget" class="w-sand-panel active" style="background: #05070f; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 10px; padding: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.45);">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>1. HTTP GET Request Method</span>
<span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(0,240,255,0.08); border: 1px solid rgba(0,240,255,0.2); color: #00f0ff; font-family: monospace;">HTTP Client</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #00f0ff; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">GET /index.php HTTP/1.1
Host: ctf.rpca.ac.th
User-Agent: Mozilla/5.0
Accept: text/html
Cookie: session_id=abc123xyz</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button style="background: rgba(0,240,255,0.1); border: 1px solid rgba(0,240,255,0.3); border-radius: 4px; color: #00f0ff; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700; transition: all 0.15s;" onclick="startWebSim('httpget')">▶ Run Simulation</button>
</div>
<div id="term-httpget" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 90px;">
<span style="color: #3ddc84;">client$</span> [กดปุ่ม Run Simulation เพื่อส่ง Request]
</div>
</div>
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 16px; font-size: 0.83rem; color: #cbd5e1; line-height: 1.65;">
<h5 style="margin: 0 0 8px; font-size: 0.85rem; color: #fbbf24; font-weight: bold;">⚙️ Command Description</h5>
<p style="margin: 0;">เมธอด GET ใช้เพื่อดึงหน้าเพจขึ้นมาแสดงผล โดยบราวเซอร์ส่ง Cookie ยืนยันสิทธิ์เซสชันแอดมิน</p>
</div>
</div>
<div id="panel-httppost" class="w-sand-panel" style="background: #05070f; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 10px; padding: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.45); display: none;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>2. HTTP POST Request Method</span>
<span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(0,240,255,0.08); border: 1px solid rgba(0,240,255,0.2); color: #00f0ff; font-family: monospace;">HTTP Client</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #00f0ff; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">POST /login.php HTTP/1.1
Host: ctf.rpca.ac.th
Content-Type: application/x-www-form-urlencoded
Content-Length: 29

username=admin&password=secret</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button style="background: rgba(0,240,255,0.1); border: 1px solid rgba(0,240,255,0.3); border-radius: 4px; color: #00f0ff; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700; transition: all 0.15s;" onclick="startWebSim('httppost')">▶ Run Simulation</button>
</div>
<div id="term-httppost" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 90px;">
<span style="color: #3ddc84;">client$</span> [กดปุ่ม Run Simulation เพื่อส่ง Request]
</div>
</div>
<div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 8px; padding: 16px; font-size: 0.83rem; color: #cbd5e1; line-height: 1.65;">
<h5 style="margin: 0 0 8px; font-size: 0.85rem; color: #fbbf24; font-weight: bold;">⚙️ Command Description</h5>
<p style="margin: 0;">เมธอด POST ใช้เพื่อส่งข้อมูลชุดใหญ่ที่เป็นความลับ (เช่น รหัสผ่าน) ไปประมวลผลบนเซิร์ฟเวอร์โดยไม่โชว์บน URL</p>
</div>
</div>
</div>
</div>
<script>
window.showSandboxItem = function(itemKey, element) {
  const navButtons = document.querySelectorAll('.w-sandbox-nav button');
  navButtons.forEach(btn => {
    btn.style.borderColor = 'rgba(255, 255, 255, 0.06)';
    btn.style.color = '#cbd5e1';
    btn.style.background = 'rgba(255, 255, 255, 0.02)';
  });
  element.style.borderColor = '#00f0ff';
  element.style.color = '#ffffff';
  element.style.background = 'rgba(0, 240, 255, 0.05)';
  const panels = document.querySelectorAll('.w-sand-panel');
  panels.forEach(p => { p.style.display = 'none'; });
  const target = document.getElementById('panel-' + itemKey);
  if (target) { target.style.display = 'block'; }
}
window.startWebSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span style="color:#64748b;">client$</span> <span style="color:#ffffff; font-weight:bold;">Sending HTTP Request...</span>\\n[.] Accessing remote port 80/443\\n[.] Reading Response Headers...';
  setTimeout(() => {
    if (itemKey === 'httpget') {
      term.innerHTML = '<span style="color:#64748b;">client$</span> <span style="color:#3ddc84; font-weight:bold;">HTTP/1.1 200 OK</span>\\nServer: Apache/2.4.41 (Ubuntu)\\nContent-Type: text/html\\nContent-Length: 1042\\n\\n&lt;html&gt;&lt;body&gt;&lt;h1&gt;Welcome to RPCA Cyber Club&lt;/h1&gt;&lt;/body&gt;&lt;/html&gt;';
    } else if (itemKey === 'httppost') {
      term.innerHTML = '<span style="color:#64748b;">client$</span> <span style="color:#fbbf24; font-weight:bold;">HTTP/1.1 302 Found</span>\\nServer: Apache/2.4.41 (Ubuntu)\\nLocation: /dashboard.php\\nSet-Cookie: session_id=abc123xyz; Path=/; HttpOnly\\n\\n[+] Redirecting to dashboard...';
    }
  }, 1000);
}
</script>"""

val177_2 = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการบันทึกความสำเร็จและปลดล็อกปุ่มบทเรียนถัดไป:

<div class="row align-items-center" style="margin:1.5rem auto; max-width:980px;"><div class="col-md-8"><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. พอร์ตบริการเครือข่ายมาตรฐานสำหรับการเข้าถึงหน้าเว็บเพจแบบเข้ารหัสปลอดภัย (HTTPS) คือพอร์ตใด?</p><div class="options-container" data-q="q1"><label class="w-quiz-option"><input type="radio" name="web_port" value="80" data-hash="false">Port 80</label><label class="w-quiz-option"><input type="radio" name="web_port" value="443" data-hash="868846c4f8d48e0259b38466e3fb0c4b26090cfa4b6f1f457788be4fbf0fa8fb">Port 443 (HTTPS)</label><label class="w-quiz-option"><input type="radio" name="web_port" value="22" data-hash="false">Port 22</label><label class="w-quiz-option"><input type="radio" name="web_port" value="8080" data-hash="false">Port 8080</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. โครงการมาตรฐานสากลด้านความปลอดภัยเว็บที่จัดอันดับ 10 ความเสี่ยงสูงสุดของเว็บแอปพลิเคชันคือองค์กรใด?</p><div class="options-container" data-q="q2"><label class="w-quiz-option"><input type="radio" name="owasp_q" value="W3C" data-hash="false">W3C</label><label class="w-quiz-option"><input type="radio" name="owasp_q" value="OWASP" data-hash="3367b846e49226cb100416972049d5bf59892cfa76e4a2cdbbf24c56e2978000">OWASP</label><label class="w-quiz-option"><input type="radio" name="owasp_q" value="SANS" data-hash="false">SANS Institute</label><label class="w-quiz-option"><input type="radio" name="owasp_q" value="MITRE" data-hash="false">MITRE Corporation</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div></div><div class="col-md-4 text-center"><div class="p-4" style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); border-radius:12px; min-height:220px; display:flex; flex-direction:column; justify-content:center; align-items:center;"><span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;">Lesson Progress</span><div class="neon-gauge-container"><svg class="neon-gauge" viewBox="0 0 36 36"><path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><path class="neon-gauge-fill" id="lesson-gauge-fill" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text">0%</text></svg></div><span id="lesson-status-txt" class="mt-3 d-block text-muted" style="font-size:0.78rem;">โปรดตอบคำถามให้ครบ 2 ข้อ</span></div></div></div>
<style>
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:#00f0ff; stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease, stroke 0.5s ease; filter:drop-shadow(0 0 5px rgba(0,240,255,0.5));}
.neon-gauge-text {fill:#ffffff; font-family:\'JetBrains Mono\',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}
</style>
<script>
const lessonKey = 'solved_lesson_177';
function getSavedSolves() { try { return JSON.parse(localStorage.getItem(lessonKey) || '[]'); } catch(e) { return []; } }
function updateLocalProgress() {
  const solved = getSavedSolves();
  const total = 2;
  const percent = Math.round((solved.length / total) * 100);
  const fill = document.getElementById('lesson-gauge-fill');
  const text = document.getElementById('lesson-gauge-text');
  const status = document.getElementById('lesson-status-txt');
  if (fill) fill.setAttribute('stroke-dasharray', `${percent}, 100`);
  if (text) text.textContent = `${percent}%`;
  if (solved.length === total) {
    if (fill) fill.style.stroke = '#3ddc84';
    if (status) status.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
  } else {
    if (fill) fill.style.stroke = '#00f0ff';
    if (status) status.textContent = `ทำเสร็จแล้ว ${solved.length}/${total} ข้อ`;
  }
}
document.addEventListener('click', function(e) {
  const label = e.target.closest('.w-quiz-option');
  if (label) {
    const container = label.closest('.options-container');
    if (container) {
      container.querySelectorAll('.w-quiz-option').forEach(opt => opt.classList.remove('selected'));
      label.classList.add('selected');
      const radio = label.querySelector('input[type="radio"]');
      if (radio) radio.checked = true;
    }
  }
});
window.verifyMultipleChoice = function(button) {
  const cell = button.closest('.question-cell');
  const selectedRadio = cell.querySelector('input[type="radio"]:checked');
  const feedback = cell.querySelector('.feedback-msg');
  if (!selectedRadio) {
    feedback.className = "feedback-msg mt-2 alert-warning py-1.5 px-3 text-dark";
    feedback.innerHTML = '<i class="fas fa-exclamation-triangle mr-1"></i> กรุณาเลือกคำตอบ';
    feedback.style.setProperty('display', 'block', 'important');
    return;
  }
  const hashVal = selectedRadio.getAttribute('data-hash');
  if (hashVal !== 'false') {
    feedback.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
    feedback.innerHTML = '<i class="fas fa-check-circle mr-1"></i> คำตอบถูกต้อง!';
    feedback.style.setProperty('display', 'block', 'important');
    cell.querySelectorAll('input[type="radio"]').forEach(r => r.disabled = true);
    cell.querySelectorAll('.w-quiz-option').forEach(opt => opt.style.pointerEvents = 'none');
    button.disabled = true;
    const solved = getSavedSolves();
    if (!solved.includes(hashVal)) {
      solved.push(hashVal);
      localStorage.setItem(lessonKey, JSON.stringify(solved));
    }
    updateLocalProgress();
  } else {
    feedback.className = "feedback-msg mt-2 alert-danger py-1.5 px-3 text-white bg-danger border-0";
    feedback.innerHTML = '<i class="fas fa-times-circle mr-1"></i> คำตอบไม่ถูกต้อง ลองใหม่!';
    feedback.style.setProperty('display', 'block', 'important');
  }
}
setTimeout(() => {
  const solved = getSavedSolves();
  document.querySelectorAll('.options-container').forEach(container => {
    container.querySelectorAll('input[type="radio"]').forEach(radio => {
      const hash = radio.getAttribute('data-hash');
      if (solved.includes(hash)) {
        radio.checked = true;
        const label = radio.closest('.w-quiz-option');
        if (label) label.classList.add('selected');
        container.querySelectorAll('input[type="radio"]').forEach(r => r.disabled = true);
        container.querySelectorAll('.w-quiz-option').forEach(opt => opt.style.pointerEvents = 'none');
        const cell = container.closest('.question-cell');
        if (cell) {
          const btn = cell.querySelector('button');
          if (btn) btn.disabled = true;
          const fb = cell.querySelector('.feedback-msg');
          if (fb) {
            fb.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
            fb.innerHTML = '<i class="fas fa-check-circle mr-1"></i> เรียบร้อยแล้ว';
            fb.style.setProperty('display', 'block', 'important');
          }
        }
      }
    });
  });
  updateLocalProgress();
}, 200);
</script>"""

# ─── Lesson 178 ───
val178_0 = """## 💉 Path Traversal, HTTP Messages & SQLi Intro (ช่องโหว่ประเภท Injection)
---

ยินดีต้อนรับสู่บทเรียนการสืบค้นข้อมูลเชิงลึกผ่านเส้นทางโฟลเดอร์เครือข่าย, โครงสร้าง HTTP Message และปูพื้นฐานการโจมตี SQL Injection

### 📄 SLIDE 51-58: เครื่องมือสแกนหาความสัมพันธ์ไฟล์ระบบ (Path Traversal Tools)
การค้นหาไดเรกทอรีลับหรือหน้าล็อกอินระบบหลังบ้านโดยใช้โปรแกรมแสกนความปลอดภัยอัตโนมัติ:

#### 📁 Dirb (Directory brute-forcing)
- **คุณลักษณะ**: สั่งรันผ่าน Command Line เพื่อสุ่มเดาชื่อไฟล์และโฟลเดอร์ โดยส่งอิงจาก Wordlist มาตรฐาน
- **ตัวอย่างการสแกนปกติ**:
  ```bash
  dirb https://target.com /usr/share/wordlists/dirb/common.txt
  ```
- **ตัวอย่างการสแกนหาไฟล์แบ็คอัปตามประเภทนามสกุล**:
  ```bash
  dirb https://target.com /usr/share/wordlists/dirb/common.txt -X .bak,.zip,.tar
  ```

#### 📁 Dirbuster (GUI-based fuzzer)
- **คุณลักษณะ**: เวอร์ชัน Graphic User Interface (มีหน้าต่างให้กดปรับแต่ง) เหมาะสำหรับการรันหาพาเนลแอดมินหรือทรัพยากรเว็บแบบเห็นภาพ

#### 📁 FFUF (Fast Web Fuzzer)
- **คุณลักษณะ**: fuzzer ความเร็วสูงในสายงานเจาะระบบ มีลูกเล่น recursive ค้นหาเส้นทางเชิงลึกแบบซับซ้อน
- **ตัวอย่างการสแกน**:
  ```bash
  ffuf -u https://target.com/admin/FUZZ -w /usr/share/wordlists/rockyou.txt
  ```

#### 📁 Gobuster (Go-written scanner)
- **คุณลักษณะ**: พัฒนาขึ้นมาด้วยภาษา Go ทำให้ข้ามขีดจำกัดความเร็วของเครื่องมืออื่นๆ มาก
- **ตัวอย่างการค้นหาไฟล์ .php**:
  ```bash
  gobuster dir -u https://target.com -w /usr/share/wordlists/dirb/common.txt -x php
  ```

---

### 📄 SLIDE 59-75: HTTP Message Anatomy (โครงสร้างทราฟฟิกเว็บ)
- **HTTP Request**: ทราฟฟิกข้อมูลที่ฝั่ง Client ส่งหาเซิร์ฟเวอร์ ประกอบด้วย:
  - **Method**: คำสั่งการทำงาน เช่น GET (ดึงข้อมูล), POST (ส่งประมวลผล), PUT (ปรับปรุงไฟล์), DELETE (ลบไฟล์)
  - **Path**: พิกัดเป้าหมาย เช่น `/api/user?id=123`
  - **Protocol**: ระบุรุ่นการส่ง เช่น `HTTP/1.1` หรือ `HTTP/2`
  - **Headers**: เมทาดาตาเสริม เช่น User-Agent (ระบุประเภทบราวเซอร์), Cookie (ระบุสิทธิ์)
  - **Body**: ข้อมูลชุดใหญ่ที่ฝั่งเซิร์ฟเวอร์นำไปประมวลผล (มีผลเฉพาะ POST/PUT)
- **HTTP Response**: ทราฟฟิกตอบกลับจากเซิร์ฟเวอร์ ประกอบด้วย:
  - **Status Line**: แจ้งรหัสผลลัพธ์ เช่น `200 OK` (สำเร็จ), `301 Moved` (ย้ายหน้า), `401 Unauthorized` (ไม่ผ่านสิทธิ์), `403 Forbidden` (ห้ามเข้า), `404 Not Found` (ไม่พบไฟล์), `500 Server Error` (เซิร์ฟเวอร์พัง)
  - **Server**: แจ้งโปรแกรมที่รันบนเครื่อง เช่น Apache, Nginx
  - **Headers**: เช่น Content-Type (ประเภทผลลัพธ์)
  - **Body**: ซอร์สโค้ด HTML หรือข้อมูล JSON ที่บราวเซอร์นำมาวาดแสดงผล
- **cURL Command**: โปรแกรมรัน Command Line ยอดนิยมในการยิงขอเรียกข้อมูลดิบจากเซิร์ฟเวอร์
  - **ตัวอย่าง**: สั่งดึงเฉพาะ Header ของเป้าหมายเพื่อตรวจความปลอดภัย:
    ```bash
    curl -I https://www.example.com
    ```

---

### 📄 SLIDE 76-90: Malicious HTTP Message Detections (การตรวจสอบภัยคุกคาม)
- **Unusual HTTP Methods**: นักโจมตีใช้ประโยชน์จากเมธอดพิเศษ เช่น OPTIONS, TRACE หรือ WebDAV (MKCOL, COPY) เพื่อตรวจและควบคุมไฟล์เซิร์ฟเวอร์
- **Unusual User-Agents**: แฮกเกอร์ใช้โปรแกรมโจมตี ซึ่งตัวโปรแกรมจะแนบ User-Agent แปลกปลอมมา (เช่น `sqlmap/1.5.2`, `HackerTool/1.0`, `python-requests`, `Nmap compatible`) แอดมินจึงควรเฝ้าระวังหรือปิดกั้นทราฟฟิกเหล่านี้
- **Large/Encoded POST**: การลอบส่ง Web Shell หรือคำสั่งยิงเจาะโดยเข้ารหัส Base64 หรือ Hex เพื่อให้ผ่านพ้นระบบ WAF (Web Application Firewall)

---

### 📄 SLIDE 91-100: SQL Injection (SQLi) Introduction
- **คำจำกัดความ**: ช่องโหว่ที่เกิดจากการเชื่อมต่อซอร์สโค้ดแอปพลิเคชันกับฐานข้อมูล SQL ผิดพลาด ปล่อยให้นำค่าอินพุตที่ผู้ใช้พิมพ์เข้ามาไปรวมเข้ากับประโยคคิวรีตรงๆ ส่งผลให้แฮกเกอร์สามารถควบคุมการประมวลผลฐานข้อมูลหลังบ้านได้
- **สไลด์ความต่างระหว่าง Query**:
  - คิวรีปกติ: `SELECT * FROM users WHERE username = 'admin' AND password = 'p@ssW0rd';`
  - คิวรีเมื่อโดนยิง bypass: `SELECT * FROM users WHERE username = 'admin' --' AND password = 'xxx';` (สัญลักษณ์ `--` ปิดประโยคตรวจรหัสผ่านด้านหลัง)"""

val178_1 = """### 💻 Directory & HTTP Diagnostic Sandbox (จำลองค้นหาไฟล์และยิงคำสั่ง)

คลิกหัวข้อด้านซ้ายมือเพื่อศึกษาตัวอย่างการทำแล็บจำลองความปลอดภัย และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลลัพธ์:

<style type="text/css">
.w-sandbox-main { display: flex !important; gap: 20px !important; margin: 1.5rem auto !important; max-width: 1000px !important; }
.w-sandbox-nav { width: 220px !important; display: flex !important; flex-direction: column !important; gap: 8px !important; flex-shrink: 0 !important; }
.w-nav-item { background: rgba(255, 255, 255, 0.02) !important; border: 1px solid rgba(255, 255, 255, 0.06) !important; border-radius: 6px !important; padding: 10px 14px !important; color: #cbd5e1 !important; text-align: left !important; cursor: pointer !important; font-size: 0.78rem !important; transition: all 0.2s !important; }
.w-nav-item:hover, .w-nav-item.active { border-color: #a855f7 !important; color: #ffffff !important; background: rgba(168, 85, 247, 0.05) !important; }
.w-nav-item.active { font-weight: 700 !important; box-shadow: 0 0 8px rgba(168, 85, 247, 0.15) !important; }
.w-sandbox-panels { flex-grow: 1 !important; display: flex !important; flex-direction: column !important; gap: 14px !important; }
.w-sand-panel { display: none; background: #05070f !important; border: 1px solid rgba(255, 255, 255, 0.08) !important; border-radius: 10px !important; padding: 20px !important; box-shadow: 0 8px 24px rgba(0,0,0,0.45) !important; }
.w-sand-panel.active { display: block !important; }
</style>
<div class="w-sandbox-main" style="display: flex; gap: 20px; margin: 1.5rem auto; max-width: 1000px;">
<div class="w-sandbox-nav" style="width: 220px; display: flex; flex-direction: column; gap: 8px; flex-shrink: 0;">
<button id="nav-item-dirb" class="w-nav-item active" style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 6px; padding: 10px 14px; color: #cbd5e1; text-align: left; cursor: pointer; font-size: 0.78rem; transition: all 0.2s;" onclick="showSandboxItem('dirb', this)">1. Dirb Backup Scan</button>
<button id="nav-item-curl" class="w-nav-item" style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 6px; padding: 10px 14px; color: #cbd5e1; text-align: left; cursor: pointer; font-size: 0.78rem; transition: all 0.2s;" onclick="showSandboxItem('curl', this)">2. cURL HTTP Audit</button>
</div>
<div class="w-sandbox-panels" style="flex-grow: 1; display: flex; flex-direction: column; gap: 14px;">
<div id="panel-dirb" class="w-sand-panel active" style="background: #05070f; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 10px; padding: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.45);">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>1. Brute-forcing Web Backups with Dirb</span>
<span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(168,85,247,0.08); border: 1px solid rgba(168,85,247,0.2); color: #a855f7; font-family: monospace;">Dirb Scanner</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #a855f7; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">dirb http://ctf.rpca.ac.th/ /usr/share/wordlists/dirb/common.txt -X .zip,.bak</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button style="background: rgba(168,85,247,0.1); border: 1px solid rgba(168,85,247,0.3); border-radius: 4px; color: #a855f7; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700; transition: all 0.15s;" onclick="startWebSim('dirb')">▶ Run Simulation</button>
</div>
<div id="term-dirb" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 90px;">
<span style="color: #3ddc84;">kali$</span> [กดปุ่ม Run Simulation เพื่อยิงคำสั่ง Dirb]
</div>
</div>
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 16px; font-size: 0.83rem; color: #cbd5e1; line-height: 1.65;">
<h5 style="margin: 0 0 8px; font-size: 0.85rem; color: #fbbf24; font-weight: bold;">⚙️ Command Description</h5>
<p style="margin: 0;">คำสั่งค้นหาไฟล์สำรอง (เช่น .zip หรือ .bak) ในรากโฮสต์เป้าหมาย เพื่อตรวจจับความเสื่อมสภาพของข้อมูลสำคัญ</p>
</div>
</div>
<div id="panel-curl" class="w-sand-panel" style="background: #05070f; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 10px; padding: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.45); display: none;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>2. cURL HTTP OPTIONS Audit</span>
<span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(168,85,247,0.08); border: 1px solid rgba(168,85,247,0.2); color: #a855f7; font-family: monospace;">cURL Tool</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #a855f7; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">curl -X OPTIONS -i http://ctf.rpca.ac.th/</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button style="background: rgba(168,85,247,0.1); border: 1px solid rgba(168,85,247,0.3); border-radius: 4px; color: #a855f7; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700; transition: all 0.15s;" onclick="startWebSim('curl')">▶ Run Simulation</button>
</div>
<div id="term-curl" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 90px;">
<span style="color: #3ddc84;">kali$</span> [กดปุ่ม Run Simulation เพื่อรันคำสั่ง cURL]
</div>
</div>
<div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 8px; padding: 16px; font-size: 0.83rem; color: #cbd5e1; line-height: 1.65;">
<h5 style="margin: 0 0 8px; font-size: 0.85rem; color: #fbbf24; font-weight: bold;">⚙️ Command Description</h5>
<p style="margin: 0;">เมธอด OPTIONS ใช้ทดสอบเพื่อขอข้อมูลรายการ HTTP methods ทั้งหมดที่เว็บเซิร์ฟเวอร์เปิดไว้ทำงาน</p>
</div>
</div>
</div>
</div>
<script>
window.showSandboxItem = function(itemKey, element) {
  const navButtons = document.querySelectorAll('.w-sandbox-nav button');
  navButtons.forEach(btn => {
    btn.style.borderColor = 'rgba(255, 255, 255, 0.06)';
    btn.style.color = '#cbd5e1';
    btn.style.background = 'rgba(255, 255, 255, 0.02)';
  });
  element.style.borderColor = '#a855f7';
  element.style.color = '#ffffff';
  element.style.background = 'rgba(168, 85, 247, 0.05)';
  const panels = document.querySelectorAll('.w-sand-panel');
  panels.forEach(p => { p.style.display = 'none'; });
  const target = document.getElementById('panel-' + itemKey);
  if (target) { target.style.display = 'block'; }
}
window.startWebSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#ffffff; font-weight:bold;">Running audit checks...</span>\\n[.] Connecting target server...';
  setTimeout(() => {
    if (itemKey === 'dirb') {
      term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#3ddc84; font-weight:bold;">DIRB scan results:</span>\\nFOUND: http://ctf.rpca.ac.th/backup.zip (CODE: 200)\\nFOUND: http://ctf.rpca.ac.th/old_site.bak (CODE: 200)\\n\\n[+] Dirb completed successfully!';
    } else if (itemKey === 'curl') {
      term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#a855f7; font-weight:bold;">HTTP/1.1 200 OK</span>\\nAllow: GET, POST, OPTIONS, TRACE, WebDAV\\nServer: Apache/2.4.41 (Ubuntu)\\nContent-Length: 0\\n\\n[+] OPTIONS check finished.';
    }
  }, 1000);
}
</script>"""

val178_2 = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการบันทึกความสำเร็จและปลดล็อกปุ่มบทเรียนถัดไป:

<div class="row align-items-center" style="margin:1.5rem auto; max-width:980px;"><div class="col-md-8"><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. ช่องโหว่ประเภทใดเกิดขึ้นจากการที่เซิร์ฟเวอร์นำอินพุตของผู้ใช้ไปเรียกประมวลผลเป็นคำสั่งระบบปฏิบัติการโดยตรง?</p><div class="options-container" data-q="q1"><label class="w-quiz-option"><input type="radio" name="inj_type" value="SQLi" data-hash="false">SQL Injection</label><label class="w-quiz-option"><input type="radio" name="inj_type" value="Command Injection" data-hash="23c7f5c90b6b80d90bd93d8435d648b26e03fb21884be5e38f6b864a66e4a2cd">Command Injection</label><label class="w-quiz-option"><input type="radio" name="inj_type" value="XSS" data-hash="false">Cross-Site Scripting (XSS)</label><label class="w-quiz-option"><input type="radio" name="inj_type" value="LFI" data-hash="false">Local File Inclusion (LFI)</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. คิวรีเป้าหมายพิเศษระดับมาตรฐาน \' OR 1=1 -- นิยมใช้ส่งเข้าไปในฐานข้อมูลเพื่อทำลายเงื่อนไขข้อใด?</p><div class="options-container" data-q="q2"><label class="w-quiz-option"><input type="radio" name="sqli_opt" value="Data Exfiltration" data-hash="false">ขโมยดูข้อมูลทั้งหมด (Data Exfiltration)</label><label class="w-quiz-option"><input type="radio" name="sqli_opt" value="Bypass Auth" data-hash="a95aa975765796245d8b8ff716d0046522bb33f749eb721867c4e515d18d451">ข้ามขั้นตอนตรวจสอบยืนยันตน (Bypass Authentication)</label><label class="w-quiz-option"><input type="radio" name="sqli_opt" value="DoS" data-hash="false">ทำลายเซิร์ฟเวอร์ระบบล่ม (Denial of Service)</label><label class="w-quiz-option"><input type="radio" name="sqli_opt" value="Password cracking" data-hash="false">ค้นหารหัสผ่านระบบ (Password Cracking)</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div></div><div class="col-md-4 text-center"><div class="p-4" style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); border-radius:12px; min-height:220px; display:flex; flex-direction:column; justify-content:center; align-items:center;"><span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;">Lesson Progress</span><div class="neon-gauge-container"><svg class="neon-gauge" viewBox="0 0 36 36"><path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><path class="neon-gauge-fill" id="lesson-gauge-fill" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text">0%</text></svg></div><span id="lesson-status-txt" class="mt-3 d-block text-muted" style="font-size:0.78rem;">โปรดตอบคำถามให้ครบ 2 ข้อ</span></div></div></div>
<style>
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:#a855f7; stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease, stroke 0.5s ease; filter:drop-shadow(0 0 5px rgba(168,85,247,0.5));}
.neon-gauge-text {fill:#ffffff; font-family:\'JetBrains Mono\',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}
</style>
<script>
const lessonKey = 'solved_lesson_178';
function getSavedSolves() { try { return JSON.parse(localStorage.getItem(lessonKey) || '[]'); } catch(e) { return []; } }
function updateLocalProgress() {
  const solved = getSavedSolves();
  const total = 2;
  const percent = Math.round((solved.length / total) * 100);
  const fill = document.getElementById('lesson-gauge-fill');
  const text = document.getElementById('lesson-gauge-text');
  const status = document.getElementById('lesson-status-txt');
  if (fill) fill.setAttribute('stroke-dasharray', `${percent}, 100`);
  if (text) text.textContent = `${percent}%`;
  if (solved.length === total) {
    if (fill) fill.style.stroke = '#3ddc84';
    if (status) status.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
  } else {
    if (fill) fill.style.stroke = '#a855f7';
    if (status) status.textContent = `ทำเสร็จแล้ว ${solved.length}/${total} ข้อ`;
  }
}
document.addEventListener('click', function(e) {
  const label = e.target.closest('.w-quiz-option');
  if (label) {
    const container = label.closest('.options-container');
    if (container) {
      container.querySelectorAll('.w-quiz-option').forEach(opt => opt.classList.remove('selected'));
      label.classList.add('selected');
      const radio = label.querySelector('input[type="radio"]');
      if (radio) radio.checked = true;
    }
  }
});
window.verifyMultipleChoice = function(button) {
  const cell = button.closest('.question-cell');
  const selectedRadio = cell.querySelector('input[type="radio"]:checked');
  const feedback = cell.querySelector('.feedback-msg');
  if (!selectedRadio) {
    feedback.className = "feedback-msg mt-2 alert-warning py-1.5 px-3 text-dark";
    feedback.innerHTML = '<i class="fas fa-exclamation-triangle mr-1"></i> กรุณาเลือกคำตอบ';
    feedback.style.setProperty('display', 'block', 'important');
    return;
  }
  const hashVal = selectedRadio.getAttribute('data-hash');
  if (hashVal !== 'false') {
    feedback.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
    feedback.innerHTML = '<i class="fas fa-check-circle mr-1"></i> คำตอบถูกต้อง!';
    feedback.style.setProperty('display', 'block', 'important');
    cell.querySelectorAll('input[type="radio"]').forEach(r => r.disabled = true);
    cell.querySelectorAll('.w-quiz-option').forEach(opt => opt.style.pointerEvents = 'none');
    button.disabled = true;
    const solved = getSavedSolves();
    if (!solved.includes(hashVal)) {
      solved.push(hashVal);
      localStorage.setItem(lessonKey, JSON.stringify(solved));
    }
    updateLocalProgress();
  } else {
    feedback.className = "feedback-msg mt-2 alert-danger py-1.5 px-3 text-white bg-danger border-0";
    feedback.innerHTML = '<i class="fas fa-times-circle mr-1"></i> คำตอบไม่ถูกต้อง ลองใหม่!';
    feedback.style.setProperty('display', 'block', 'important');
  }
}
setTimeout(() => {
  const solved = getSavedSolves();
  document.querySelectorAll('.options-container').forEach(container => {
    container.querySelectorAll('input[type="radio"]').forEach(radio => {
      const hash = radio.getAttribute('data-hash');
      if (solved.includes(hash)) {
        radio.checked = true;
        const label = radio.closest('.w-quiz-option');
        if (label) label.classList.add('selected');
        container.querySelectorAll('input[type="radio"]').forEach(r => r.disabled = true);
        container.querySelectorAll('.w-quiz-option').forEach(opt => opt.style.pointerEvents = 'none');
        const cell = container.closest('.question-cell');
        if (cell) {
          const btn = cell.querySelector('button');
          if (btn) btn.disabled = true;
          const fb = cell.querySelector('.feedback-msg');
          if (fb) {
            fb.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
            fb.innerHTML = '<i class="fas fa-check-circle mr-1"></i> เรียบร้อยแล้ว';
            fb.style.setProperty('display', 'block', 'important');
          }
        }
      }
    });
  });
  updateLocalProgress();
}, 200);
</script>"""

# ─── Lesson 179 ───
val179_2 = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการบันทึกความสำเร็จและปลดล็อกปุ่มบทเรียนถัดไป:

<div class="row align-items-center" style="margin:1.5rem auto; max-width:980px;"><div class="col-md-8"><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. ช่องโหว่ Cross-Site Scripting (XSS) เกิดจากการลอบฝังแทรกสคริปต์โค้ดประเภทใดเข้ามาทำงานฝั่ง Client Browser?</p><div class="options-container" data-q="q1"><label class="w-quiz-option"><input type="radio" name="xss_lang" value="SQL" data-hash="false">SQL Query code</label><label class="w-quiz-option"><input type="radio" name="xss_lang" value="JavaScript" data-hash="78ec09be8733f52e505820464fdbb19d45388047970d47d457cb146ef279ec3d">JavaScript</label><label class="w-quiz-option"><input type="radio" name="xss_lang" value="Bash" data-hash="false">Bash Shell command</label><label class="w-quiz-option"><input type="radio" name="xss_lang" value="PHP" data-hash="false">PHP Server Script</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. คีย์เวิร์ดมาตรฐาน HTML tag ใดที่นักโจมตีใช้ส่ง XSS Payload เพื่อเปิดจำลองกล่องป๊อปอัพ?</p><div class="options-container" data-q="q2"><label class="w-quiz-option"><input type="radio" name="xss_tag" value="script" data-hash="3a95aa975765796245d8b8ff716d0046522bb33f749eb721867c4e515d18d451"><span>&lt;script&gt;</span></label><label class="w-quiz-option"><input type="radio" name="xss_tag" value="iframe" data-hash="false"><span>&lt;iframe&gt;</span></label><label class="w-quiz-option"><input type="radio" name="xss_tag" value="div" data-hash="false"><span>&lt;div&gt;</span></label><label class="w-quiz-option"><input type="radio" name="xss_tag" value="img" data-hash="false"><span>&lt;img&gt;</span></label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div></div><div class="col-md-4 text-center"><div class="p-4" style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); border-radius:12px; min-height:220px; display:flex; flex-direction:column; justify-content:center; align-items:center;"><span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;">Lesson Progress</span><div class="neon-gauge-container"><svg class="neon-gauge" viewBox="0 0 36 36"><path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><path class="neon-gauge-fill" id="lesson-gauge-fill" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text">0%</text></svg></div><span id="lesson-status-txt" class="mt-3 d-block text-muted" style="font-size:0.78rem;">โปรดตอบคำถามให้ครบ 2 ข้อ</span></div></div></div>
<style>
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:#3b82f6; stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease, stroke 0.5s ease; filter:drop-shadow(0 0 5px rgba(59,130,246,0.5));}
.neon-gauge-text {fill:#ffffff; font-family:\'JetBrains Mono\',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}
</style>
<script>
const lessonKey = 'solved_lesson_179';
function getSavedSolves() { try { return JSON.parse(localStorage.getItem(lessonKey) || '[]'); } catch(e) { return []; } }
function updateLocalProgress() {
  const solved = getSavedSolves();
  const total = 2;
  const percent = Math.round((solved.length / total) * 100);
  const fill = document.getElementById('lesson-gauge-fill');
  const text = document.getElementById('lesson-gauge-text');
  const status = document.getElementById('lesson-status-txt');
  if (fill) fill.setAttribute('stroke-dasharray', `${percent}, 100`);
  if (text) text.textContent = `${percent}%`;
  if (solved.length === total) {
    if (fill) fill.style.stroke = '#3ddc84';
    if (status) status.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
  } else {
    if (fill) fill.style.stroke = '#3b82f6';
    if (status) status.textContent = `ทำเสร็จแล้ว ${solved.length}/${total} ข้อ`;
  }
}
document.addEventListener('click', function(e) {
  const label = e.target.closest('.w-quiz-option');
  if (label) {
    const container = label.closest('.options-container');
    if (container) {
      container.querySelectorAll('.w-quiz-option').forEach(opt => opt.classList.remove('selected'));
      label.classList.add('selected');
      const radio = label.querySelector('input[type="radio"]');
      if (radio) radio.checked = true;
    }
  }
});
window.verifyMultipleChoice = function(button) {
  const cell = button.closest('.question-cell');
  const selectedRadio = cell.querySelector('input[type="radio"]:checked');
  const feedback = cell.querySelector('.feedback-msg');
  if (!selectedRadio) {
    feedback.className = "feedback-msg mt-2 alert-warning py-1.5 px-3 text-dark";
    feedback.innerHTML = '<i class="fas fa-exclamation-triangle mr-1"></i> กรุณาเลือกคำตอบ';
    feedback.style.setProperty('display', 'block', 'important');
    return;
  }
  const hashVal = selectedRadio.getAttribute('data-hash');
  if (hashVal !== 'false') {
    feedback.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
    feedback.innerHTML = '<i class="fas fa-check-circle mr-1"></i> คำตอบถูกต้อง!';
    feedback.style.setProperty('display', 'block', 'important');
    cell.querySelectorAll('input[type="radio"]').forEach(r => r.disabled = true);
    cell.querySelectorAll('.w-quiz-option').forEach(opt => opt.style.pointerEvents = 'none');
    button.disabled = true;
    const solved = getSavedSolves();
    if (!solved.includes(hashVal)) {
      solved.push(hashVal);
      localStorage.setItem(lessonKey, JSON.stringify(solved));
    }
    updateLocalProgress();
  } else {
    feedback.className = "feedback-msg mt-2 alert-danger py-1.5 px-3 text-white bg-danger border-0";
    feedback.innerHTML = '<i class="fas fa-times-circle mr-1"></i> คำตอบไม่ถูกต้อง ลองใหม่!';
    feedback.style.setProperty('display', 'block', 'important');
  }
}
setTimeout(() => {
  const solved = getSavedSolves();
  document.querySelectorAll('.options-container').forEach(container => {
    container.querySelectorAll('input[type="radio"]').forEach(radio => {
      const hash = radio.getAttribute('data-hash');
      if (solved.includes(hash)) {
        radio.checked = true;
        const label = radio.closest('.w-quiz-option');
        if (label) label.classList.add('selected');
        container.querySelectorAll('input[type="radio"]').forEach(r => r.disabled = true);
        container.querySelectorAll('.w-quiz-option').forEach(opt => opt.style.pointerEvents = 'none');
        const cell = container.closest('.question-cell');
        if (cell) {
          const btn = cell.querySelector('button');
          if (btn) btn.disabled = true;
          const fb = cell.querySelector('.feedback-msg');
          if (fb) {
            fb.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
            fb.innerHTML = '<i class="fas fa-check-circle mr-1"></i> เรียบร้อยแล้ว';
            fb.style.setProperty('display', 'block', 'important');
          }
        }
      }
    });
  });
  updateLocalProgress();
}, 200);
</script>"""

# ─── Lesson 180 ───
val180_2 = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการบันทึกความสำเร็จและปลดล็อกปุ่มบทเรียนถัดไป:

<div class="row align-items-center" style="margin:1.5rem auto; max-width:980px;"><div class="col-md-8"><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. ส่วนหัว (Header) ความปลอดภัยใดใน HTTP Response ที่ใช้ป้องกันหน้าเว็บไม่ให้ถูกนำไปฝังใน Iframe เพื่อเลี่ยงช่องโหว่ Clickjacking?</p><div class="options-container" data-q="q1"><label class="w-quiz-option"><input type="radio" name="xframe_h" value="X-Frame-Options" data-hash="c9b7f5256e2978000bd93d8435d648b26e03fb21884be5e38f6b864a66e4a2cd">X-Frame-Options</label><label class="w-quiz-option"><input type="radio" name="xframe_h" value="CSP" data-hash="false">Content-Security-Policy</label><label class="w-quiz-option"><input type="radio" name="xframe_h" value="HSTS" data-hash="false">Strict-Transport-Security</label><label class="w-quiz-option"><input type="radio" name="xframe_h" value="XXSS" data-hash="false">X-XSS-Protection</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. หลักปฏิบัติเพื่อความปลอดภัยในการป้องกันการแทรกโค้ดทำลายระบบเครือข่ายฐานข้อมูล (Injection) ทุกประเภทคือข้อใด?</p><div class="options-container" data-q="q2"><label class="w-quiz-option"><input type="radio" name="sec_coding" value="Input Validation" data-hash="277bc1b69ad3178c775080e7221f75355694a08ba1c38fa8b79f38ebcb5c8a41">การกรองตรวจสอบความถูกต้องข้อมูลนำเข้า (Input Validation)</label><label class="w-quiz-option"><input type="radio" name="sec_coding" value="Encryption" data-hash="false">การเข้ารหัสฐานข้อมูล (Database Encryption)</label><label class="w-quiz-option"><input type="radio" name="sec_coding" value="Backup" data-hash="false">การสำรองไฟล์ข้อมูลประจำวัน (Daily Backup)</label><label class="w-quiz-option"><input type="radio" name="sec_coding" value="IDS" data-hash="false">การติดตั้งระบบแจ้งเตือนแฮกเกอร์ (Intrusion Detection)</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div></div><div class="col-md-4 text-center"><div class="p-4" style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); border-radius:12px; min-height:220px; display:flex; flex-direction:column; justify-content:center; align-items:center;"><span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;">Lesson Progress</span><div class="neon-gauge-container"><svg class="neon-gauge" viewBox="0 0 36 36"><path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><path class="neon-gauge-fill" id="lesson-gauge-fill" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text">0%</text></svg></div><span id="lesson-status-txt" class="mt-3 d-block text-muted" style="font-size:0.78rem;">โปรดตอบคำถามให้ครบ 2 ข้อ</span></div></div></div>
<style>
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:#10b981; stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease, stroke 0.5s ease; filter:drop-shadow(0 0 5px rgba(16,185,129,0.5));}
.neon-gauge-text {fill:#ffffff; font-family:\'JetBrains Mono\',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}
</style>
<script>
const lessonKey = 'solved_lesson_180';
function getSavedSolves() { try { return JSON.parse(localStorage.getItem(lessonKey) || '[]'); } catch(e) { return []; } }
function updateLocalProgress() {
  const solved = getSavedSolves();
  const total = 2;
  const percent = Math.round((solved.length / total) * 100);
  const fill = document.getElementById('lesson-gauge-fill');
  const text = document.getElementById('lesson-gauge-text');
  const status = document.getElementById('lesson-status-txt');
  if (fill) fill.setAttribute('stroke-dasharray', `${percent}, 100`);
  if (text) text.textContent = `${percent}%`;
  if (solved.length === total) {
    if (fill) fill.style.stroke = '#3ddc84';
    if (status) status.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
  } else {
    if (fill) fill.style.stroke = '#10b981';
    if (status) status.textContent = `ทำเสร็จแล้ว ${solved.length}/${total} ข้อ`;
  }
}
document.addEventListener('click', function(e) {
  const label = e.target.closest('.w-quiz-option');
  if (label) {
    const container = label.closest('.options-container');
    if (container) {
      container.querySelectorAll('.w-quiz-option').forEach(opt => opt.classList.remove('selected'));
      label.classList.add('selected');
      const radio = label.querySelector('input[type="radio"]');
      if (radio) radio.checked = true;
    }
  }
});
window.verifyMultipleChoice = function(button) {
  const cell = button.closest('.question-cell');
  const selectedRadio = cell.querySelector('input[type="radio"]:checked');
  const feedback = cell.querySelector('.feedback-msg');
  if (!selectedRadio) {
    feedback.className = "feedback-msg mt-2 alert-warning py-1.5 px-3 text-dark";
    feedback.innerHTML = '<i class="fas fa-exclamation-triangle mr-1"></i> กรุณาเลือกคำตอบ';
    feedback.style.setProperty('display', 'block', 'important');
    return;
  }
  const hashVal = selectedRadio.getAttribute('data-hash');
  if (hashVal !== 'false') {
    feedback.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
    feedback.innerHTML = '<i class="fas fa-check-circle mr-1"></i> คำตอบถูกต้อง!';
    feedback.style.setProperty('display', 'block', 'important');
    cell.querySelectorAll('input[type="radio"]').forEach(r => r.disabled = true);
    cell.querySelectorAll('.w-quiz-option').forEach(opt => opt.style.pointerEvents = 'none');
    button.disabled = true;
    const solved = getSavedSolves();
    if (!solved.includes(hashVal)) {
      solved.push(hashVal);
      localStorage.setItem(lessonKey, JSON.stringify(solved));
    }
    updateLocalProgress();
  } else {
    feedback.className = "feedback-msg mt-2 alert-danger py-1.5 px-3 text-white bg-danger border-0";
    feedback.innerHTML = '<i class="fas fa-times-circle mr-1"></i> คำตอบไม่ถูกต้อง ลองใหม่!';
    feedback.style.setProperty('display', 'block', 'important');
  }
}
setTimeout(() => {
  const solved = getSavedSolves();
  document.querySelectorAll('.options-container').forEach(container => {
    container.querySelectorAll('input[type="radio"]').forEach(radio => {
      const hash = radio.getAttribute('data-hash');
      if (solved.includes(hash)) {
        radio.checked = true;
        const label = radio.closest('.w-quiz-option');
        if (label) label.classList.add('selected');
        container.querySelectorAll('input[type="radio"]').forEach(r => r.disabled = true);
        container.querySelectorAll('.w-quiz-option').forEach(opt => opt.style.pointerEvents = 'none');
        const cell = container.closest('.question-cell');
        if (cell) {
          const btn = cell.querySelector('button');
          if (btn) btn.disabled = true;
          const fb = cell.querySelector('.feedback-msg');
          if (fb) {
            fb.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
            fb.innerHTML = '<i class="fas fa-check-circle mr-1"></i> เรียบร้อยแล้ว';
            fb.style.setProperty('display', 'block', 'important');
          }
        }
      }
    });
  });
  updateLocalProgress();
}, 200);
</script>"""

# ─── Execute updates ───
save_lesson(177, val177_0, val177_1, val177_2)
save_lesson(178, val178_0, val178_1, val178_2)
save_lesson(179, val179_0, val179_1, val179_2)
save_lesson(180, val180_0, val180_1, val180_2)
ctx.pop()
