import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

deep_expanded_html = """### 🛡️ ไฟล์เป้าหมายและสัญลักษณ์ความปลอดภัย (Target Files & System Exposure)

ในกระบวนการโจมตีประเภท **Path and Directory Traversal** ผู้โจมตีไม่ได้เพียงแค่ต้องการอ่านไฟล์สุ่มสี่สุ่มห้า แต่มีเป้าหมายหลักคือการสืบค้นหาไฟล์ระบบที่สำคัญเพื่อนำมาวิเคราะห์และขยายผลการโจมตี (Privilege Escalation) 

#### 📂 คลังไฟล์ยอดนิยมที่เป็นเป้าหมายสำคัญของแฮกเกอร์:

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin: 1.5rem auto;">
  <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(239, 68, 68, 0.25); border-radius: 12px; padding: 20px; box-shadow: 0 4px 20px rgba(239, 68, 68, 0.05);">
    <strong style="color: #ef4444; font-size: 1rem; display: block; margin-bottom: 10px;">🐧 Linux System Files</strong>
    <ul style="color: #cbd5e1; font-size: 0.82rem; line-height: 1.6; margin: 0; padding-left: 20px;">
      <li><code style="color: #ff007f;">/etc/passwd</code>: รายชื่อบัญชีผู้ใช้ในระบบ พาธโฮมไดเรกทอรี และ Shell เริ่มต้น (ทุกคนอ่านได้)</li>
      <li><code style="color: #ff007f;">/etc/shadow</code>: ไฟล์เก็บค่าแฮชรหัสผ่านของผู้ใช้ (เฉพาะสิทธิ์ Root เท่านั้นจึงเข้าถึงได้)</li>
      <li><code style="color: #ff007f;">/etc/hosts</code>: รายการแมปไอพีแอดเดรสภายในระบบเครือข่าย</li>
    </ul>
  </div>

  <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(59, 130, 246, 0.25); border-radius: 12px; padding: 20px; box-shadow: 0 4px 20px rgba(59, 130, 246, 0.05);">
    <strong style="color: #3b82f6; font-size: 1rem; display: block; margin-bottom: 10px;">💻 Windows System Files</strong>
    <ul style="color: #cbd5e1; font-size: 0.82rem; line-height: 1.6; margin: 0; padding-left: 20px;">
      <li><code style="color: #00f0ff;">C:\\Windows\\win.ini</code>: ไฟล์การตั้งค่าดั้งเดิมของ Windows (มักใช้ทดสอบยืนยันสิทธิ์ช่องโหว่ LFI)</li>
      <li><code style="color: #00f0ff;">C:\\Windows\\System32\\config\\SAM</code>: ฐานข้อมูลรหัสผ่านบัญชีผู้ใช้ระบบ (Security Accounts Manager)</li>
      <li><code style="color: #00f0ff;">C:\\Windows\\System32\\drivers\\etc\\hosts</code>: ตารางบันทึกชื่อไอพีภายในของฝั่ง Windows</li>
    </ul>
  </div>
</div>

<div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(168, 85, 247, 0.25); border-radius: 12px; padding: 20px; margin: 1.5rem auto; box-shadow: 0 4px 20px rgba(168, 85, 247, 0.05);">
  <strong style="color: #a855f7; font-size: 1rem; display: block; margin-bottom: 10px;">🔑 Web Source Code & Configuration Files</strong>
  <p style="color: #cbd5e1; font-size: 0.82rem; line-height: 1.6; margin: 0 0 10px 0;">
    แฮกเกอร์มักมุ่งเป้าไปที่ไฟล์ตั้งค่าหลักของแอปพลิเคชัน เนื่องจากไฟล์เหล่านี้มักเก็บ **รหัสผ่านฐานข้อมูล (Database Credentials), คีย์ลับ JWT (Secret Keys), และ API Token** ของระบบภายนอก:
  </p>
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px;">
    <div style="background: rgba(255,255,255,0.02); padding: 10px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.05);">
      <code style="color: #eab308; font-size: 0.8rem;">.env</code> หรือ <code style="color: #eab308; font-size: 0.8rem;">config.json</code><br>
      <span style="font-size: 0.72rem; color: #94a3b8;">ไฟล์เก็บค่าตัวแปรสภาพแวดล้อมหลักของเว็บสมัยใหม่</span>
    </div>
    <div style="background: rgba(255,255,255,0.02); padding: 10px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.05);">
      <code style="color: #eab308; font-size: 0.8rem;">wp-config.php</code> หรือ <code style="color: #eab308; font-size: 0.8rem;">config.php</code><br>
      <span style="font-size: 0.72rem; color: #94a3b8;">รหัสผ่านเชื่อมต่อฐานข้อมูล SQL และซอลท์ยืนยันเซสชัน</span>
    </div>
    <div style="background: rgba(255,255,255,0.02); padding: 10px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.05);">
      <code style="color: #eab308; font-size: 0.8rem;">settings.py</code> หรือ <code style="color: #eab308; font-size: 0.8rem;">application.properties</code><br>
      <span style="font-size: 0.72rem; color: #94a3b8;">การตั้งค่าเบื้องหลังของแอป Django (Python) หรือ Spring Boot (Java)</span>
    </div>
  </div>
</div>

---

### 🤖 ไฟล์ Robots.txt กับความมั่นคงปลอดภัย (Path and Directory Traversal: Robots.txt)

ไฟล์ **robots.txt** เป็นไฟล์ข้อความธรรมดาที่แอดมินสร้างไว้ตรงโฟลเดอร์ราก (Web Root) เพื่อใช้สื่อสารกับบอตสำรวจข้อมูลของเสิร์ชเอนจิน (เช่น Googlebot, Bingbot) เพื่อแจ้งว่า **"ส่วนใดของเว็บไซต์ที่ไม่ต้องการให้บอตนำไปแสดงผลบน Google"**

> [!WARNING]
> **ความเข้าใจผิดร้ายแรง (Security through Obscurity)**:
> นักพัฒนาจำนวนมากใช้คำสั่ง <code style="color: #ff007f;">Disallow:</code> ในไฟล์ `robots.txt` เพื่อหวังที่จะ **"ซ่อน"** หน้าแดชบอร์ดผู้ดูแลระบบหรือโฟลเดอร์สำรองข้อมูลจากผู้ใช้งานทั่วไป ซึ่งเป็นการกระทำที่ผิดหลักการความปลอดภัยอย่างยิ่ง เนื่องจากไฟล์ `robots.txt` เป็นไฟล์สาธารณะที่ใครก็เปิดอ่านได้ แฮกเกอร์จึงมักเลือกเปิดอ่านไฟล์นี้เป็นพิกัดแรกเพื่อเก็บรวบรวมข้อมูลพาธลับ (Directory Exposure)!

<div style="display: flex; flex-direction: column; md-flex-direction: row; gap: 20px; margin: 1.5rem auto; max-width: 850px;">
  <!-- Bad Practice Card -->
  <div style="flex: 1; background: rgba(239, 68, 68, 0.03); border: 1px solid rgba(239, 68, 68, 0.25); border-radius: 12px; padding: 20px;">
    <div style="color: #ef4444; font-weight: bold; font-size: 0.95rem; margin-bottom: 12px;">❌ ตัวอย่างการใช้งานที่เป็นภัย (Insecure Practice)</div>
    <div style="background: #090c15; font-family: monospace; font-size: 0.8rem; padding: 12px; border-radius: 6px; border: 1px solid rgba(239, 68, 68, 0.15); color: #cbd5e1; line-height: 1.5;">
      User-agent: *<br>
      Disallow: /admin-portal-v2/<br>
      Disallow: /secret-database-backup/<br>
      Disallow: /config.php<br>
      Disallow: /api/private/key
    </div>
    <span style="font-size: 0.75rem; color: #fca5a5; display: block; margin-top: 8px;">💡 ผลลัพธ์: แฮกเกอร์รู้ตำแหน่งที่ควรจะเข้ายึดระบบหรือไต่ข้ามไดเรกทอรีได้ทันที!</span>
  </div>

  <!-- Good Practice Card -->
  <div style="flex: 1; background: rgba(16, 185, 129, 0.03); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 12px; padding: 20px;">
    <div style="color: #10b981; font-weight: bold; font-size: 0.95rem; margin-bottom: 12px;">✔️ แนวทางแก้ไขที่ถูกต้อง (Secure Practice)</div>
    <ul style="color: #cbd5e1; font-size: 0.82rem; line-height: 1.6; margin: 0; padding-left: 20px;">
      <li>ห้ามใส่ชื่อพิกัดไดเรกทอรีลับหรือสำคัญไว้ใน `robots.txt`</li>
      <li>ตั้งค่าความมั่นคงปลอดภัยจริงที่ **เว็บเซิร์ฟเวอร์หลังบ้าน (Back-end Configuration)** เช่น ทำการสกัดกั้นไอพีที่แปลกปลอม หรือจำกัดสิทธิ์เข้าใช้งานระดับเครือข่าย</li>
      <li>ควบคุมสิทธิ์การยืนยันตัวตนและการล็อกอิน (Authorization & Authentication) ในทุกพิกัดอย่างเข้มงวด</li>
    </ul>
  </div>
</div>

---

### 🛠️ เครื่องมืออัตโนมัติสำหรับการสแกนพาธ (Automated Scanning Tools)

ในการประเมินความปลอดภัยหาช่องโหว่ประเภท Directory Traversal หรือการทำ Directory Brute-forcing เพื่อสแกนหาโฟลเดอร์ลับ แฮกเกอร์และนักทดสอบระบบมักเลือกใช้เครื่องมือที่แตกต่างกันตามเป้าหมายและสถาปัตยกรรม ดังนี้:

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 1.5rem auto;">
  <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; padding: 16px;">
    <strong style="color: #00f0ff; display: block; margin-bottom: 6px; font-size: 0.95rem;">🛠️ DIRB / DirBuster</strong>
    <span style="color: #cbd5e1; font-size: 0.8rem; line-height: 1.5; display: block;">เป็นเครื่องมือดั้งเดิมที่เน้นการค้นหาไดเรกทอรีและไฟล์ทีละพาธตามลำดับ เหมาะสำหรับการหาพิกัดทั่วไปผ่านไฟล์ Wordlist</span>
  </div>
  <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; padding: 16px;">
    <strong style="color: #3ddc84; display: block; margin-bottom: 6px; font-size: 0.95rem;">⚡ FFUF / Gobuster</strong>
    <span style="color: #cbd5e1; font-size: 0.8rem; line-height: 1.5; display: block;">เครื่องมือยุคใหม่ที่เขียนด้วยภาษา Go ทำงานได้อย่างรวดเร็วเป็นพิเศษ (High performance) และรองรับการทำ Fuzzing พารามิเตอร์ต่างๆ ได้ดีมาก</span>
  </div>
  <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; padding: 16px;">
    <strong style="color: #a855f7; display: block; margin-bottom: 6px; font-size: 0.95rem;">🛡️ Burp Suite Intruder</strong>
    <span style="color: #cbd5e1; font-size: 0.8rem; line-height: 1.5; display: block;">เหมาะสำหรับการทดสอบเจาะจงจุดอย่างละเอียด เช่นการทำ Traversal fuzzing หรือป้อนรหัสแฝงในตัวแปรพารามิเตอร์แบบปรับแต่งค่าได้อิสระ</span>
  </div>
</div>

---

### 📂 การใช้งานเครื่องมือ DIRB (Directory Buster)

**DIRB** คือเครื่องมือในกลุ่ม Command-line บนระบบ Linux (เช่น Kali Linux) เพื่อค้นหารายการพาธและไฟล์ของเว็บแอปพลิเคชันผ่านฐานพจนานุกรมคำศัพท์ (Wordlist)

#### 💻 ตัวอย่างหน้าต่างประมวลผลจริงและการอ่านค่า Log สแกน (DIRB Output Logs):

<div style="background: #0b0f19; border: 1px solid rgba(0, 240, 255, 0.15); border-radius: 12px; padding: 24px; margin: 2rem auto; max-width: 850px; box-shadow: 0 8px 32px rgba(0,0,0,0.45); font-family: 'Inter', sans-serif;">
  <!-- Terminal Window Header -->
  <div style="display: flex; align-items: center; justify-content: space-between; background: #161b26; border-radius: 8px 8px 0 0; padding: 10px 16px; border-bottom: 1px solid rgba(255,255,255,0.05);">
    <div style="display: flex; gap: 6px;">
      <span style="width: 10px; height: 10px; background: #ef4444; border-radius: 50%; display: inline-block;"></span>
      <span style="width: 10px; height: 10px; background: #f59e0b; border-radius: 50%; display: inline-block;"></span>
      <span style="width: 10px; height: 10px; background: #10b981; border-radius: 50%; display: inline-block;"></span>
    </div>
    <span style="color: #94a3b8; font-family: monospace; font-size: 0.75rem; font-weight: bold;">terminal — dirb scan</span>
    <div style="width: 36px;"></div>
  </div>

  <!-- Terminal Window Body -->
  <div style="background: #070913; border-radius: 0 0 8px 8px; padding: 20px; text-align: left; overflow-x: auto; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; line-height: 1.5; color: #34d399;">
    <span style="color: #64748b;">(kali@kali)-[~] $ dirb https://www.google.com/ /usr/share/wordlists/dirb/common.txt</span><br><br>
    -----------------<br>
    DIRB v2.22 - By The Dark Raver<br>
    START_TIME: Mon Mar 3 11:33:14 2025<br>
    URL_BASE: https://www.google.com/<br>
    WORDLIST_FILES: /usr/share/wordlists/dirb/common.txt<br>
    -----------------<br><br>
    GENERATED WORDS: 4612<br><br>
    + <span style="color: #fbbf24;">https://www.google.com/2007 (CODE:301|SIZE:239)</span><br>
    + <span style="color: #fbbf24;">https://www.google.com/about (CODE:302|SIZE:218)</span><br>
    + <span style="color: #10b981;">https://www.google.com/alerts (CODE:200|SIZE:154358)</span><br>
    ==> <span style="color: #00f0ff;">DIRECTORY: https://www.google.com/ads/</span><br>
    + <span style="color: #fbbf24;">https://www.google.com/advertise (CODE:301|SIZE:224)</span><br>
    + <span style="color: #ef4444;">https://www.google.com/admin (CODE:403|SIZE:250)</span>
  </div>
</div>

#### 💡 การทำความเข้าใจ HTTP Status Codes จากผลลัพธ์ของ DIRB:
1. **CODE 200 (Success)**: หมายถึงตรวจพบไฟล์นั้นจริงบนเซิร์ฟเวอร์ และเปิดสิทธิ์เข้าดูได้อย่างเสรี (เช่น หน้าเว็บสาธารณะ หรือไฟล์รูปภาพ)
2. **CODE 301 / 302 (Redirect)**: มีการโอนย้ายเส้นทางของ URL ซึ่งแฮกเกอร์มักสนใจเพราะอาจถูกรีไดเรกต์ไปหาหน้าล็อกอินลับได้
3. **CODE 403 (Forbidden)**: ไฟล์/โฟลเดอร์นี้ **มีอยู่จริง** แต่เซิร์ฟเวอร์ตั้งค่าปิดกั้นสิทธิ์ไม่ให้อ่านโดยตรง ซึ่งเป็นข้อมูลสืบราชการที่ยอดเยี่ยมเพราะยืนยันได้ว่าเป้าหมายมีตัวตน
4. **DIRECTORY**: ตัวโปรแกรมพบโฟลเดอร์หลัก และจะเริ่มต้นวิ่งสแกนย่อยลึกลงไป (Recursive scan) โดยอัตโนมัติ

#### ตารางสรุปรูปแบบการใช้งานคำสั่ง DIRB (DIRB Command Cheat Sheet)

<div style="overflow-x:auto;margin:1.5rem auto;max-width:1000px;border:1px solid rgba(6,182,212,0.25);border-radius:12px;background:#05070f;box-shadow:0 10px 30px rgba(0,0,0,0.6);">
<table style="width:100%;border-collapse:collapse;text-align:left;font-family:sans-serif;font-size:0.85rem;">
<thead>
<tr style="background:rgba(6,182,212,0.08);border-bottom:1px solid rgba(6,182,212,0.2);">
<th style="padding:12px 16px;font-weight:bold;color:#00f0ff;width:35%;">คำอธิบายการใช้งาน (Use Case)</th>
<th style="padding:12px 16px;font-weight:bold;color:#3ddc84;width:65%;">รูปแบบคำสั่งคีย์เวิร์ด (Command)</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;vertical-align:middle;">1. การสแกนไดเรกทอรีขั้นพื้นฐาน (Basic Scan)</td>
<td style="padding:12px 16px;vertical-align:middle;">
<code style="color:#00f0ff;background:rgba(0,240,255,0.05);padding:4px 8px;border-radius:4px;border:1px solid rgba(0,240,255,0.1);font-family:monospace;display:block;font-size:0.78rem;">dirb https://target.com /usr/share/wordlists/dirb/common.txt</code>
<span style="font-size:0.75rem;color:#94a3b8;display:block;margin-top:4px;">สั่งรันค้นหาโฟลเดอร์ปกติโดยใช้ฐานคำศัพท์พื้นฐาน (common.txt)</span>
</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;vertical-align:middle;">2. ค้นหาไฟล์เฉพาะนามสกุล / แบ็คอัป (Find Backup Files)</td>
<td style="padding:12px 16px;vertical-align:middle;">
<code style="color:#00f0ff;background:rgba(0,240,255,0.05);padding:4px 8px;border-radius:4px;border:1px solid rgba(0,240,255,0.1);font-family:monospace;display:block;font-size:0.78rem;">dirb https://target.com /usr/share/wordlists/dirb/common.txt -X .bak,.zip,.tar</code>
<span style="font-size:0.75rem;color:#94a3b8;display:block;margin-top:4px;">เพิ่มออปชัน <code style="color:#ff007f;">-X</code> ตามด้วยชนิดไฟล์ เพื่อดักจับไฟล์สำรองข้อมูลหรือบีบอัดที่หลงเหลือบนเว็บ</span>
</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;vertical-align:middle;">3. การสแกนแบบไม่แบ่งขนาดตัวพิมพ์ (Case Insensitive)</td>
<td style="padding:12px 16px;vertical-align:middle;">
<code style="color:#00f0ff;background:rgba(0,240,255,0.05);padding:4px 8px;border-radius:4px;border:1px solid rgba(0,240,255,0.1);font-family:monospace;display:block;font-size:0.78rem;">dirb https://target.com -i</code>
<span style="font-size:0.75rem;color:#94a3b8;display:block;margin-top:4px;">ใช้พารามิเตอร์ <code style="color:#ff007f;">-i</code> เพื่อทดสอบเรียกชื่อพาร์ติชันทั้งตัวใหญ่และตัวเล็กสลับกัน</span>
</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;vertical-align:middle;">4. บันทึกผลลัพธ์เป็นไฟล์เอกสาร (Save Output File)</td>
<td style="padding:12px 16px;vertical-align:middle;">
<code style="color:#00f0ff;background:rgba(0,240,255,0.05);padding:4px 8px;border-radius:4px;border:1px solid rgba(0,240,255,0.1);font-family:monospace;display:block;font-size:0.78rem;">dirb https://target.com -o result.txt</code>
<span style="font-size:0.75rem;color:#94a3b8;display:block;margin-top:4px;">ใช้พารามิเตอร์ <code style="color:#ff007f;">-o</code> ตามด้วยชื่อไฟล์ เพื่อเขียนประวัติผลการวิเคราะห์เก็บไว้ตรวจสิทธิ์ย้อนหลัง</span>
</td>
</tr>
</tbody>
</table>
</div>

---

### 🖥️ การใช้งานเครื่องมือ DirBuster (OWASP DirBuster GUI)

**DirBuster** เป็นซอฟต์แวร์แอปพลิเคชันประเภทยูสเซอร์อินเตอร์เฟสแบบกราฟิก (GUI-based Java application) ซึ่งจัดเป็นเวอร์ชันอัปเกรดเพื่อช่วยสแกน Brute-force ค้นหาไฟล์และโฟลเดอร์ที่ถูกปิดบังไว้ในระดับลึกโดยทำงานร่วมกับระบบ Threading เพื่อให้ได้ประสิทธิภาพความเร็วระดับสูง

#### ⚙️ การตั้งค่าพารามิเตอร์การทำงานหลักของ DirBuster:

<div style="background: rgba(15, 23, 42, 0.4); border: 1px solid rgba(0, 240, 255, 0.1); border-radius: 12px; padding: 20px; margin: 1.5rem auto;">
  <div style="display: flex; flex-direction: column; gap: 16px; font-size: 0.85rem; line-height: 1.6; color: #cbd5e1;">
    <div style="display: flex; align-items: flex-start; gap: 10px;">
      <span style="color: #00f0ff; font-weight: bold; font-size: 1.1rem; line-height: 1;">🌐</span>
      <div>
        <strong style="color: #ffffff;">Target URL</strong><br>
        ระบุโดเมนเป้าหมายเว็บไซต์ที่ต้องการสแกนวิเคราะห์ความปลอดภัย เช่น <code style="color: #00f0ff;">http://example.com:80/</code> หรือใช้เป็นไอพีโดยตรง
      </div>
    </div>
    
    <div style="display: flex; align-items: flex-start; gap: 10px;">
      <span style="color: #00f0ff; font-weight: bold; font-size: 1.1rem; line-height: 1;">⚙️</span>
      <div>
        <strong style="color: #ffffff;">Work Method</strong><br>
        วิธีการส่งคำขอเรียกเซิร์ฟเวอร์ โดยแนะนำให้เลือกเป็น <strong style="color: #eab308;">Auto Switch HEAD and GET</strong> (จะส่ง HEAD คำขอข้อมูลสั้นๆ ก่อนเพื่อประหยัดแบนด์วิดท์เซิร์ฟเวอร์ และจะสลับไปส่ง GET เมื่อเริ่มพบรหัสสถานะที่มีนัยสำคัญ)
      </div>
    </div>

    <div style="display: flex; align-items: flex-start; gap: 10px;">
      <span style="color: #00f0ff; font-weight: bold; font-size: 1.1rem; line-height: 1;">⚡</span>
      <div>
        <strong style="color: #ffffff;">Number of Threads</strong><br>
        สปีดการทำงานแบบพร้อมกันของตัวประมวลผล (ตั้งแต่ 10 ถึง 200 Threads) โดยแนะนำให้ปรับตามระดับการตอบรับของเซิร์ฟเวอร์เป้าหมาย เพื่อไม่ให้เซิร์ฟเวอร์ล่มจากการโดนรุมยิงทราฟฟิก (Avoid DoS) หรือโดนกลไก WAF ตรวจจับบล็อกไอพี
      </div>
    </div>

    <div style="display: flex; align-items: flex-start; gap: 10px;">
      <span style="color: #00f0ff; font-weight: bold; font-size: 1.1rem; line-height: 1;">📂</span>
      <div>
        <strong style="color: #ffffff;">Select scanning type</strong><br>
        เลือกวิธีการสแกน โดยแนะนำรูปแบบ <strong style="color: #3ddc84;">List based brute force</strong> เพื่อระบุเรียกใช้ไฟล์ฐานข้อมูลพจนานุกรมคำศัพท์ที่เตรียมไว้ในโปรแกรม
      </div>
    </div>

    <div style="display: flex; align-items: flex-start; gap: 10px;">
      <span style="color: #00f0ff; font-weight: bold; font-size: 1.1rem; line-height: 1;">📝</span>
      <div>
        <strong style="color: #ffffff;">File extension</strong><br>
        นามสกุลของชื่อไฟล์ที่เราคาดว่าระบบหลังบ้านนั้นใช้งานอยู่ เช่นระบุค่า <code style="color: #a855f7;">php</code>, <code style="color: #a855f7;">txt</code>, หรือ <code style="color: #a855f7;">html</code> เพื่อกรองผลลัพธ์เฉพาะสกุลที่ช่วยค้นหาไฟล์ข้อมูลสำคัญเจาะลึกได้สูงสุด
      </div>
    </div>
  </div>
</div>"""

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        try:
            blocks = json.loads(l.content)
            val = blocks[0]["value"]
            
            # Find the start of the targets/exposure header
            target_start = val.find("### 🛡️ ไฟล์สำคัญและไฟล์ระบบที่แฮกเกอร์มักมุ่งเป้าโจมตีขโมยข้อมูล")
            if target_start == -1:
                target_start = val.find("ไฟล์สำคัญและไฟล์ระบบที่แฮกเกอร์มักมุ่งเป้าโจมตีขโมยข้อมูล")
                
            if target_start != -1:
                # Replace everything from that section to the end with our deep expanded HTML
                new_val = val[:target_start] + deep_expanded_html
                blocks[0]["value"] = new_val
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print("Successfully updated Lesson 177 Block 0 with deep expanded content and premium CSS!")
            else:
                print("Error: Could not find target section header in Lesson 177 Block 0.")
        except Exception as e:
            print(f"Error: {e}")
