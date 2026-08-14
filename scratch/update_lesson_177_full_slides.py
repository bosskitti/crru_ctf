import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

new_content_block_0 = """<div style="text-align: center; margin-bottom: 2rem; padding: 24px; background: linear-gradient(135deg, rgba(6,182,212,0.15) 0%, rgba(59,130,246,0.15) 100%); border: 1px solid rgba(6,182,212,0.3); border-radius: 16px; box-shadow: 0 0 20px rgba(6,182,212,0.15);">
<h2 style="margin: 0; font-size: 1.9rem; font-weight: 800; color: #ffffff; text-shadow: 0 0 12px rgba(6,182,212,0.6); letter-spacing: 0.03em;">🌐 Web Application Security & OWASP</h2>
<p style="margin: 8px 0 0 0; font-size: 0.92rem; color: #cbd5e1;">เรียนรู้สถาปัตยกรรมเว็บแอปพลิเคชัน โครงสร้างของข้อมูล และความสำคัญของการตรวจสอบคุณลักษณะความมั่นคงปลอดภัยบนเว็บเบราว์เซอร์</p>
</div>

### 🌐 ความเข้าใจพื้นฐานสถาปัตยกรรมเว็บแอปพลิเคชัน (Web Architecture Overview)

ในการติดต่อสื่อสารทางเว็บ จะทำงานผ่านโครงสร้างแบบ **Client-Server Architecture** โดยมีองค์ประกอบหลักดังนี้:
1. **Client (บราวเซอร์)**: ผู้ใช้งานเปิดใช้เว็บเบราว์เซอร์เพื่อป้อนที่อยู่เว็บปลายทาง (URL) บราวเซอร์จะทำการส่งคำขอข้อมูลในรูปแบบ **HTTP Request** ขึ้นไปยังหลังบ้าน
2. **Server (เซิร์ฟเวอร์และฐานข้อมูล)**: เซิร์ฟเวอร์จะรับคำขอ ประมวลผลตรรกะระบบ (Backend Logic) สื่อสารกับระบบฐานข้อมูลเพื่อเก็บหรือดึงข้อมูล จากนั้นส่งข้อมูลกลับมาในรูป **HTTP Response** (มักเป็นโค้ด HTML, CSS, JavaScript) เพื่อให้บราวเซอร์นำไปวาดแสดงผลหน้าจอ

---

### 🛠️ เครื่องมือแกะรหัสหน้าเว็บ (Web Page Source Inspections)

การตรวจสอบซอร์สโค้ดหน้าเว็บ (Inspecting a web page) ช่วยให้คุณวิเคราะห์โครงสร้าง (Structure), ค้นหาช่องโหว่ความมั่นคงปลอดภัย (Identify Vulnerabilities) และทำความเข้าใจกลไกการทำงานของเว็บแอปพลิเคชัน ซึ่งเป็นทักษะพื้นฐานและกุญแจสำคัญสำหรับ **Web Exploitation, Debugging และ Web Development**

Most modern web browsers have built-in **Developer Tools (DevTools)** to inspect and analyze web pages:
- **Google Chrome / Microsoft Edge**: กดปุ่ม <kbd style="background: #202430; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); font-family: monospace; font-size: 0.75rem;">F12</kbd> หรือกดคีย์บอร์ดลัด <kbd style="background: #202430; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); font-family: monospace; font-size: 0.75rem;">Ctrl + Shift + I</kbd> เพื่อเรียกใช้ DevTools
- **Mozilla Firefox**: กดปุ่ม <kbd style="background: #202430; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); font-family: monospace; font-size: 0.75rem;">F12</kbd> หรือกดคีย์บอร์ดลัด <kbd style="background: #202430; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); font-family: monospace; font-size: 0.75rem;">Ctrl + Shift + I</kbd>
- **Apple Safari**: เปิดใช้งาน "Show Developer Menu" ใน Settings จากนั้นกดคีย์บอร์ดลัด <kbd style="background: #202430; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); font-family: monospace; font-size: 0.75rem;">Cmd + Option + I</kbd>

#### 1. การดูซอร์สโค้ดหน้าเว็บโดยตรง (View Page Source)
คุณสามารถเรียกดูซอร์สโค้ด (Source Code) ดิบของไฟล์ HTML ได้โดยการคลิกขวาบนพื้นที่ว่างของหน้าเว็บแล้วเลือก **"View page source" (ดูซอร์สโค้ดหน้าเพจ)** หรือใช้คีย์ลัด:
- 💻 สำหรับ Windows: <kbd style="background: #202430; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); font-family: monospace; font-size: 0.75rem;">Ctrl + U</kbd>
- 🍎 สำหรับ Mac: <kbd style="background: #202430; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); font-family: monospace; font-size: 0.75rem;">Command + Option + U</kbd>

#### 2. การดัดแปลงและตรวจสอบ HTML (Modifying HTML)
- **วิธีการใช้งาน**: เปิด DevTools ไปยังแท็บ **Elements** จากนั้นเลื่อนเมาส์ไปชี้ที่โครงสร้างโค้ดหน้าจอในส่วน DOM (Document Object Model) ระบบจะทำการไฮไลต์พื้นที่บนหน้าเว็บจริงให้คุณเห็น หรือคลิกขวาที่จุดใดๆ บนหน้าเพจแล้วเลือก **"Inspect" (ตรวจสอบ)** เพื่อดู HTML ของส่วนนั้นทันที
- **กรณีตัวอย่าง (Use Case)**:
  - ดัดแปลงข้อความหรือรูปภาพสดบนบราวเซอร์ของตนเอง (Client-side)
  - **ตรวจสอบกล่องข้อมูลฟอร์มที่ถูกซ่อนไว้ (Hidden Form Fields)** เช่น ค้นหาแท็ก `<input type="hidden" name="admin_role" value="false">` แล้วลองเปลี่ยนประเภทจาก `hidden` ให้กลายเป็น `text` เพื่อแก้ไขค่าพารามิเตอร์ส่งกลับไปให้เซิร์ฟเวอร์

#### 3. การดัดแปลงและตรวจสอบ CSS (Modifying CSS)
- **วิธีการใช้งาน**: ในแท็บ Elements แผงด้านล่าง/ขวามือจะมีส่วน **Styles** ซึ่งแสดงสไตล์ชีตทั้งหมดของคลาสที่เลือก คุณสามารถเพิ่ม แก้ไข หรือปิดใช้งานกฎ CSS เพื่อดูการเปลี่ยนแปลงแบบสดเรียลไทม์ได้ทันที
- **กรณีตัวอย่าง (Use Case)**:
  - ทดลองปรับสี ปุ่ม หรือฟอนต์เพื่อตรวจสอบการแสดงผล
  - **ค้นหาความบกพร่องของ CSS (Weak CSS Rules)** เช่น การซ่อนส่วนอินเทอร์เฟซลับที่เกี่ยวข้องกับสิทธิ์แอดมินด้วยคลาส CSS ง่ายๆ (เช่น สั่งแค่ `display: none;` หรือ `visibility: hidden;` ในหน้าเว็บสำหรับบุคคลทั่วไปแทนที่จะบล็อกจากหลังบ้าน) ซึ่งแฮกเกอร์สามารถปิดใช้คุณสมบัตินี้ในสไตล์ชีตเพื่อกดเข้าใช้งานได้ทันที

#### 4. การดีบักสคริปต์ JavaScript (Debugging JavaScript)
- **วิธีการใช้งาน**: 
  - ไปยังแท็บ **Sources** เพื่อตรวจสอบไฟล์ JavaScript ทั้งหมดที่ถูกโหลดเข้ามาในหน้านั้น
  - สามารถทำการคลิกที่ตัวเลขบรรทัดเพื่อเพิ่ม **Breakpoint (จุดหยุดชะงัก)** เพื่อให้โค้ดหยุดประมวลผลชั่วคราวขณะรันงาน ทำให้นักพัฒนา/แฮกเกอร์สามารถตรวจสอบค่าตัวแปรภายในหน่วยความจำขณะนั้นได้
  - สามารถประมวลผลสคริปต์สดเพิ่มเติมในแท็บ **Console** เพื่อทดสอบฟังก์ชันในเบราว์เซอร์
- **กรณีตัวอย่าง (Use Case)**:
  - **การข้ามการตรวจสอบข้อมูลฝั่ง Client (Bypass Client-side Validation)** เช่น แก้ไขค่าตัวแปรใน Console หรือสั่งหยุดการตรวจสอบความยาว/รูปแบบอีเมลก่อนกดส่งฟอร์ม
  - ปรับเปลี่ยนกลไกการรับสิทธิ์เข้าใช้งานฝั่งเบราว์เซอร์ (JS-based Auth mechanisms)

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin: 1.5rem auto;">
  <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.25);">
    <strong style="color: #00f0ff; display: block; margin-bottom: 6px; font-size: 0.95rem;">📄 Elements Tab</strong>
    <span style="color: #cbd5e1; font-size: 0.8rem; line-height: 1.5;">วิเคราะห์ DOM แก้ไข HTML และตรวจสอบ Hidden input fields</span>
  </div>
  <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.25);">
    <strong style="color: #00f0ff; display: block; margin-bottom: 6px; font-size: 0.95rem;">💻 Console Tab</strong>
    <span style="color: #cbd5e1; font-size: 0.8rem; line-height: 1.5;">รันคำสั่งสคริปต์สด ดึงค่าคุกกี้ หรือดักจับค่าตัวแปร JavaScript</span>
  </div>
  <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.25);">
    <strong style="color: #00f0ff; display: block; margin-bottom: 6px; font-size: 0.95rem;">💾 Application Tab</strong>
    <span style="color: #cbd5e1; font-size: 0.8rem; line-height: 1.5;">ตรวจสอบ Local Storage, Session Storage และวิเคราะห์/แก้ไข Cookies</span>
  </div>
</div>

---

### 🍪 การสำรวจระบบจัดเก็บคุกกี้เว็บ (Web Cookies Explorations)

**คุกกี้ (HTTP Cookies / Web Cookies)** คือข้อมูลชิ้นเล็กๆ ที่เว็บเซิร์ฟเวอร์สร้างขึ้นและจัดส่งมาเก็บบันทึกไว้ในเครื่องผู้ใช้งาน (Client-side) ผ่านเว็บบราวเซอร์ คุกกี้จะถูกแนบส่งกลับไปหาเซิร์ฟเวอร์ในทุกการเข้าถึงหน้าเว็บของโดเมนนั้นเพื่อยืนยันตัวตนเซสชัน (Session Tracking) และจดจำการตั้งค่าผู้ใช้

สำหรับนักทดสอบเจาะระบบและนักพัฒนา การสืบสวนค่าคุกกี้มีความสำคัญมากเพื่อตรวจสอบความเสี่ยงต่อการโดนขโมยเซสชัน (**Session Hijacking**) หรือช่องโหว่ **Cross-Site Scripting (XSS)**

#### การตรวจสอบและแก้ไขคุกกี้ใน DevTools:
- **วิธีเข้าดู**: เปิด DevTools ➡️ เลือกแท็บ **Application** ➡️ หัวข้อ **Storage** ทางซ้ายมือ ➡️ เลือกคลิกที่ **Cookies** ➡️ เลือกชื่อเว็บปัจจุบัน
- **การปรับเปลี่ยน**: คุณสามารถดับเบิลคลิกเพื่อทำการ **แก้ไขค่า (Edit), เพิ่มค่า (Create) หรือลบค่าคุกกี้ (Delete)** ได้ทันทีผ่านอินเทอร์เฟซนี้

#### คุณลักษณะสำคัญของคุกกี้ (Key Cookie Attributes) ที่ต้องใส่ใจความปลอดภัย:
1. **Name & Value**: ข้อมูลชื่อและค่าคีย์ของคุกกี้ (เช่น `session=abc123xyz`)
2. **Domain & Path**: ขอบเขตขอบข่ายเว็บไซต์ที่มีผลเรียกใช้งานคุกกี้ชิ้นนี้
3. **Expires**: กำหนดวันเวลาหมดอายุการใช้งานของคุกกี้
4. **HttpOnly**: คุณสมบัติความปลอดภัยที่ **ป้องกันไม่ให้ JavaScript (เช่นคำสั่ง XSS) เข้าถึงข้อมูลคุกกี้ชิ้นนี้ได้** ซึ่งจะช่วยบล็อกการขโมยคุกกี้ไปใช้งานต่อ
5. **Secure**: คุณสมบัติที่บังคับให้เบราว์เซอร์ส่งคุกกี้นี้เฉพาะเมื่อเชื่อมต่อผ่านช่องทางเข้ารหัสความปลอดภัย **HTTPS** เท่านั้น
6. **SameSite**: การตั้งค่าสกัดกั้นการโจมตีประเภท **CSRF (Cross-Site Request Forgery)** โดยการจำกัดสิทธิ์การส่งคุกกี้ข้ามโดเมนอื่น

---

### 📂 ช่องโหว่การไต่พาธระบบและข้ามไดเรกทอรี (Path and Directory Traversal)

**ช่องโหว่การไต่ไดเรกทอรี (Path and Directory Traversal)** คือจุดอ่อนความมั่นคงปลอดภัยบนเว็บแอปพลิเคชันที่ยินยอมให้ผู้โจมตีทำการส่งคีย์เวิร์ดรหัสอักขระพิเศษเพื่อควบคุมพาธการเข้าถึงไฟล์ระบบ (File Parameter Manipulation) นอกขอบเขตโฟลเดอร์ราก (Web Root) ไปยังไดเรกทอรีอื่นๆ บนระบบปฏิบัติการของเซิร์ฟเวอร์หลังบ้านได้

<div style="text-align: center; margin: 2rem auto; padding: 15px; background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 12px; max-width: 900px;">
  <img src="/tutorials/static/uploads/media__1783909984729.png" alt="Path Traversal Diagram" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);" />
  <span style="color: #cbd5e1; display: block; mt-3; font-size: 0.8rem; line-height: 1.5; text-align: center; margin-top: 10px;">
    <strong>แผนภาพกระบวนการโจมตี Directory Traversal (อ้างอิงจาก Wallarm):</strong><br>
    1. แฮกเกอร์ส่งเส้นทางไฟล์ที่ตนต้องการข้ามสิทธิ์ขึ้นไปยังเซิร์ฟเวอร์ผ่านพารามิเตอร์อินพุต (เช่น LFI parameter)<br>
    2. เซิร์ฟเวอร์ที่ไม่มีระบบตรวจสอบที่ดี (X) จะยินยอมดึงข้อมูลในระบบไฟล์เครื่องเซิร์ฟเวอร์ตามที่แฮกเกอร์ร้องขอแทนที่จะเรียกเฉพาะไฟล์ของเว็บไซต์ปกติ<br>
    3. เซิร์ฟเวอร์ดึงข้อมูลจากพาร์ติชันส่วนบุคคล (Private Directory/File) ส่งกลับไปแสดงผลหน้าเว็บให้แฮกเกอร์อ่านได้สำเร็จ
  </span>
</div>

#### ไฟล์สำคัญและไฟล์ระบบที่แฮกเกอร์มักมุ่งเป้าโจมตีขโมยข้อมูล:
- **ไฟล์ระบบ (System Files)**:
  - 🐧 สำหรับ Linux: `/etc/passwd` (รายชื่อบัญชีผู้ใช้ระบบ)
  - 💻 สำหรับ Windows: `C:\\Windows\\System32\\config\\SAM` หรือไฟล์ในโฟลเดอร์ระบบอื่นๆ
- **ซอร์สโค้ดของแอปพลิเคชัน (Application Source Code)**: ไฟล์เขียนระบบหลักที่อาจมีอัลกอริทึมที่เป็นความลับ
- **ไฟล์การตั้งค่าระบบ (Configuration Files)**: เช่น ไฟล์เก็บกู้อินเทอร์เฟซคีย์ส่วนตัว `.env` หรือ `config.php`
- **ไฟล์แนะนำบอตเสิร์ชเอนจิน**: เช่น `robots.txt`

---

### 🤖 ไฟล์ Robots.txt กับความมั่นคงปลอดภัย (Path and Directory Traversal: Robots.txt)

ไฟล์ **robots.txt** เป็นไฟล์มาตรฐานสำหรับจัดเก็บบันทึกบนเว็บเซิร์ฟเวอร์ที่ระบุข้อมูลแนะนำตัวสแกนเก็บข้อมูล (Search Engine Crawlers เช่น Googlebot) ว่าไดเรกทอรีหรือหน้าเพจใดของเว็บไซต์ที่ไม่ควรนำไปทำดัชนีผลการค้นหา (Index) ในสาธารณะ

**ข้อควรระวังสำคัญสำหรับความปลอดภัย**:
นักพัฒนาและผู้ดูแลระบบเว็บไซต์จำนวนมากมักเข้าใจผิด โดยการนำไดเรกทอรีหรือโฟลเดอร์เก็บข้อมูลส่วนตัวมาพิมพ์ระบุไว้ใน robots.txt เพื่อป้องกันไม่ให้คนอื่นสืบค้นเจอ ซึ่งการทำเช่นนี้จะเท่ากับเป็นการ **"ชี้เป้า" (Directory exposure)** ให้ผู้โจมตีทราบทันทีว่าควรเดินทางไปเจาะระบบหรือแอบดูไฟล์ในพาธลับพิกัดใดของเว็บไซต์!"""

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        try:
            blocks = json.loads(l.content)
            blocks[0]['value'] = new_content_block_0
            l.content = json.dumps(blocks, ensure_ascii=False)
            app.db.session.commit()
            print("Successfully updated Lesson 177 Block 0 with comprehensive slide contents and diagram!")
        except Exception as e:
            print(f"Error: {e}")
