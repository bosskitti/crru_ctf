import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

# Load the clean baseline value from lesson_177_block_0.txt
with open("/opt/CTFd/lesson_177_block_0.txt", "r", encoding="utf-8") as f:
    baseline_value = f.read()

expanded_html_section = """### 🛠️ เครื่องมือแกะรหัสหน้าเว็บ (Web Page Source Inspections)

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
  - **ตรวจสอบกล่องข้อมูลฟอร์มที่ถูกซ่อนไว้ (Hidden Form Fields)** เช่น ค้นหาแท็ก `<input type="hidden" name="admin_role" value="false">` แล้วลองเปลี่ยนประเภทจาก `hidden` ให้กลายเป็น `text` เพื่อแสดงฟิลด์ลับ (Hidden field will be displayed) เพื่อทำการแก้ไขค่าพารามิเตอร์ส่งกลับไปให้เซิร์ฟเวอร์

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

<div style="background:#070a13;border:1px solid rgba(0,240,255,0.15);border-radius:12px;padding:24px;text-align:center;margin:2rem auto;max-width:850px;box-shadow:0 8px 32px rgba(0,0,0,0.4);">
<div style="font-size:0.85rem;color:#00f0ff;font-weight:bold;margin-bottom:16px;text-transform:uppercase;letter-spacing:0.08em;text-shadow:0 0 8px rgba(0,240,255,0.4);"><i class="fas fa-project-diagram mr-2"></i> แผนภาพจำลองกระบวนการโจมตี Path Traversal (3-Step Attack Flow)</div>
<svg viewBox="0 0 720 280" style="width:100%;height:auto;display:block;margin:0 auto;background:#03050a;border-radius:8px;">
<defs>
<linearGradient id="neon-blue" x1="0%" y1="0%" x2="100%" y2="0%">
<stop offset="0%" stop-color="#00f0ff" />
<stop offset="100%" stop-color="#3b82f6" />
</linearGradient>
<linearGradient id="neon-red" x1="0%" y1="0%" x2="100%" y2="0%">
<stop offset="0%" stop-color="#ff007f" />
<stop offset="100%" stop-color="#ef4444" />
</linearGradient>
<filter id="glow-blue" x="-20%" y="-20%" width="140%" height="140%">
<feGaussianBlur stdDeviation="3" result="blur" />
<feComposite in="SourceGraphic" in2="blur" operator="over" />
</filter>
<filter id="glow-red" x="-20%" y="-20%" width="140%" height="140%">
<feGaussianBlur stdDeviation="3" result="blur" />
<feComposite in="SourceGraphic" in2="blur" operator="over" />
</filter>
</defs>
<g transform="translate(20, 80)">
<rect x="0" y="0" width="110" height="110" rx="8" fill="#0f1322" stroke="#ff007f" stroke-width="1.5" filter="url(#glow-red)"/>
<circle cx="55" cy="40" r="18" fill="none" stroke="#ff007f" stroke-width="1.5"/>
<path d="M42,40 C42,32 68,32 68,40" fill="none" stroke="#ff007f" stroke-width="1.5"/>
<path d="M37,70 C37,55 73,55 73,70 L73,80 L37,80 Z" fill="#ff007f" opacity="0.2"/>
<path d="M37,70 C37,55 73,55 73,70 L73,80 L37,80 Z" fill="none" stroke="#ff007f" stroke-width="1.5"/>
<text x="55" y="100" fill="#ffffff" font-size="10" font-family="sans-serif" font-weight="bold" text-anchor="middle">Hacker</text>
</g>
<path d="M140,110 L220,110" fill="none" stroke="#ff007f" stroke-width="2" stroke-dasharray="4,2" filter="url(#glow-red)"/>
<polygon points="220,110 212,106 212,114" fill="#ff007f"/>
<text x="180" y="100" fill="#ff007f" font-size="8.5" font-family="monospace" text-anchor="middle" font-weight="bold">1. Send Path Request</text>
<text x="180" y="122" fill="#cbd5e1" font-size="7.5" font-family="monospace" text-anchor="middle">?page=../../etc/passwd</text>
<path d="M220,160 L140,160" fill="none" stroke="#3b82f6" stroke-width="2" filter="url(#glow-blue)"/>
<polygon points="140,160 148,156 148,164" fill="#3b82f6"/>
<text x="180" y="152" fill="#3b82f6" font-size="8.5" font-family="monospace" text-anchor="middle" font-weight="bold">3. Return Private File</text>
<text x="180" y="174" fill="#34d399" font-size="7.5" font-family="monospace" text-anchor="middle">Content of passwd file...</text>
<g transform="translate(240, 80)">
<rect x="0" y="0" width="100" height="110" rx="8" fill="#0f1322" stroke="#3b82f6" stroke-width="1.5" filter="url(#glow-blue)"/>
<rect x="10" y="15" width="80" height="18" rx="3" fill="#1e293b" stroke="#3b82f6" stroke-width="0.75"/>
<circle cx="20" cy="24" r="3" fill="#34d399" filter="url(#glow-blue)"/>
<text x="50" y="26" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Server OS</text>
<rect x="10" y="45" width="80" height="18" rx="3" fill="#1e293b" stroke="#3b82f6" stroke-width="0.75"/>
<circle cx="20" cy="54" r="3" fill="#3b82f6"/>
<text x="50" y="56" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Web Service</text>
<rect x="10" y="75" width="80" height="18" rx="3" fill="#1e293b" stroke="#3b82f6" stroke-width="0.75"/>
<circle cx="20" cy="84" r="3" fill="#ff007f" filter="url(#glow-red)"/>
<text x="50" y="86" fill="#ff007f" font-size="8" font-family="sans-serif" font-weight="bold" text-anchor="middle">Vulnerable API</text>
</g>
<path d="M350,115 L430,75" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,2"/>
<circle cx="390" cy="95" r="9" fill="#03050a" stroke="#ef4444" stroke-width="1.5"/>
<path d="M386,91 L394,99 M394,91 L386,99" fill="none" stroke="#ef4444" stroke-width="1.5"/>
<path d="M350,150 L430,195" fill="none" stroke="#ff007f" stroke-width="2" filter="url(#glow-red)"/>
<polygon points="430,195 422,190 424,199" fill="#ff007f"/>
<text x="395" y="215" fill="#ff007f" font-size="8" font-family="monospace" text-anchor="middle" font-weight="bold">2. Include Hacker Path</text>
<g transform="translate(450, 20)">
<rect x="0" y="0" width="130" height="210" rx="8" fill="#05070f" stroke="#3b82f6" stroke-width="1" stroke-dasharray="2,2"/>
<text x="65" y="16" fill="#3b82f6" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Website (Web Root)</text>
<g transform="translate(15, 30)">
<rect x="0" y="0" width="100" height="50" rx="5" fill="#0f1322" stroke="#3b82f6" stroke-width="1"/>
<path d="M15,15 L25,15 L25,35 L15,35 Z" fill="none" stroke="#3b82f6" stroke-width="1"/>
<text x="60" y="25" fill="#ffffff" font-size="8.5" font-family="sans-serif" text-anchor="middle">Normal File</text>
<text x="60" y="38" fill="#94a3b8" font-size="7" font-family="monospace" text-anchor="middle">index.html</text>
</g>
<g transform="translate(15, 140)">
<rect x="0" y="0" width="100" height="55" rx="5" fill="#0f1322" stroke="#ff007f" stroke-width="1" filter="url(#glow-red)"/>
<path d="M12,18 L12,42 L38,42 L38,24 L24,24 L20,18 Z" fill="rgba(255, 0, 127, 0.1)" stroke="#ff007f" stroke-width="1"/>
<text x="62" y="28" fill="#ffffff" font-size="8" font-family="sans-serif" font-weight="bold" text-anchor="middle">Private Dir</text>
<text x="62" y="42" fill="#ff007f" font-size="7" font-family="monospace" text-anchor="middle">/../../</text>
</g>
</g>
<path d="M570,170 L600,170" fill="none" stroke="#ff007f" stroke-width="2" filter="url(#glow-red)"/>
<polygon points="600,170 592,166 592,174" fill="#ff007f"/>
<g transform="translate(605, 95)">
<rect x="0" y="0" width="100" height="100" rx="8" fill="#05070f" stroke="#ef4444" stroke-width="1"/>
<text x="50" y="16" fill="#ef4444" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">System (OS)</text>
<g transform="translate(10, 30)">
<rect x="0" y="0" width="80" height="50" rx="4" fill="#0f1322" stroke="#ef4444" stroke-width="1" filter="url(#glow-red)"/>
<text x="40" y="24" fill="#ffffff" font-size="8" font-family="sans-serif" font-weight="bold" text-anchor="middle">Private File</text>
<text x="40" y="38" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">/etc/passwd</text>
</g>
</g>
</svg>
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
            
            # Load the baseline content from backup first to start clean!
            blocks[0]["value"] = baseline_value
            
            # Find the marker in the clean baseline
            target_marker = "### 🛠️ เครื่องมือแกะรหัสหน้าเว็บ (Web Page Source Inspections)"
            idx = blocks[0]["value"].find(target_marker)
            
            if idx != -1:
                # Replace cleanly to the end of the text
                blocks[0]["value"] = blocks[0]["value"][:idx] + expanded_html_section
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print("Successfully restored baseline and performed a clean targeted replacement!")
            else:
                print("Error: Target marker not found in baseline value.")
        except Exception as e:
            print(f"Error: {e}")
