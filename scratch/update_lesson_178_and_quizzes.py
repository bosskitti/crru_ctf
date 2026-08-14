import re

# Read term_w36_web_app_complete_v5.py
with open("/home/kali/crru_ctf/CTFd/term_w36_web_app_complete_v5.py", "r", encoding="utf-8") as f:
    code = f.read()

# Define updated val178_0
val178_0_new = r'''val178_0 = """## 💉 HTTP Anatomy, SQL Injection & OS Command Injections (โครงสร้างเว็บแอปพลิเคชันและการฝังคำสั่งโจมตี)
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
'''

# Define updated val178_1
val178_1_new = r'''val178_1 = """### 💻 SQL Injection & SQLMap Simulation Sandbox (บอร์ดเรียนรู้จำลองการเจาะฐานข้อมูล)

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
    preview.innerHTML = 'SELECT * FROM users\\nWHERE username = \\'<span style="color:#ff007f;">' + u + '</span>\\'\\nAND password = \\'<span style="color:#00f0ff;">' + p + '</span>\\';';
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
  term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#ffffff; font-weight:bold;">sqlmap -u "http://ctf.rpca.ac.th/view_profile.php?id=1" --dbs</span>\\n[.] testing connection to the target URL...';
  setTimeout(() => {
    term.innerHTML += '\\n[!] heuristic test shows that GET parameter \\'id\\' might be injectable';
  }, 600);
  setTimeout(() => {
    term.innerHTML += '\\n[+] UNION query (SQLi) injection technique detected on parameter \\'id\\'';
  }, 1200);
  setTimeout(() => {
    term.innerHTML += '\\n[.] retrieving database names...\\n\\n[+] available databases [3]:\\n<span style="color:#00f0ff;">[*] ctf_vulnerabilities</span>\\n<span style="color:#00f0ff;">[*] information_schema</span>\\n<span style="color:#00f0ff;">[*] users_database</span>\\n\\n<span style="color:#3ddc84; font-weight:bold;">[+] SQLMap execution completed successfully.</span>';
  }, 2000);
}

setTimeout(() => {
  if (typeof updateSQLPreview === 'function') updateSQLPreview();
}, 200);
</script>
"""
'''

# Define updated val177_2
val177_2_new = r'''val177_2 = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

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
'''

# Define updated val178_2
val178_2_new = r'''val178_2 = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

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
'''

# Define updated val179_2
val179_2_new = r'''val179_2 = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

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
'''

# Define updated val180_2
val180_2_new = r'''val180_2 = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

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
'''

# Regex replace val177_2
pattern_177_2 = r'val177_2\s*=\s*\"\"\"### ✏️ Lesson Quick Quiz.*?</script>\"\"\"'
code = re.sub(pattern_177_2, val177_2_new.strip(), code, flags=re.DOTALL)

# Regex replace val178_0
pattern_178_0_regex = r'val178_0\s*=\s*\"\"\"## 💉 Path Traversal.*?(ทำให้เครื่องแม่ข่ายของเซิร์ฟเวอร์ยอมรับการทำงานรันคำสั่งดึงไฟล์รายชื่อผู้ใช้ออกมาแสดงทันที|shell_exec\("ping -c 4 " \. \$ip\);.*?)\s*\"\"\"'
code = re.sub(pattern_178_0_regex, val178_0_new.strip(), code, flags=re.DOTALL)

# Regex replace val178_1
pattern_178_1 = r'val178_1\s*=\s*\"\"\"### 💻 Directory & HTTP Diagnostic Sandbox.*?</script>\"\"\"'
code = re.sub(pattern_178_1, val178_1_new.strip(), code, flags=re.DOTALL)

# Regex replace val178_2
pattern_178_2 = r'val178_2\s*=\s*\"\"\"### ✏️ Lesson Quick Quiz.*?</script>\"\"\"'
code = re.sub(pattern_178_2, val178_2_new.strip(), code, flags=re.DOTALL)

# Regex replace val179_2
pattern_179_2 = r'val179_2\s*=\s*\"\"\"### ✏️ Lesson Quick Quiz.*?</script>\"\"\"'
code = re.sub(pattern_179_2, val179_2_new.strip(), code, flags=re.DOTALL)

# Regex replace val180_2
pattern_180_2 = r'val180_2\s*=\s*\"\"\"### ✏️ Lesson Quick Quiz.*?</script>\"\"\"'
code = re.sub(pattern_180_2, val180_2_new.strip(), code, flags=re.DOTALL)

# Save to term_w36_web_app_complete_v6.py
output_path = "/home/kali/crru_ctf/CTFd/term_w36_web_app_complete_v6.py"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(code)

print("term_w36_web_app_complete_v6.py successfully generated!")
