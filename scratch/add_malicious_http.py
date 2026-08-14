import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

malicious_http_html = """

---

### 🚨 การตรวจจับข้อความ HTTP ที่เป็นอันตราย (Malicious HTTP Message Detections)

นักโจมตีระบบมักจะทำการดัดแปลงแก้ไขข้อความ HTTP Request เพื่อส่งข้อมูลที่เป็นอันตราย ค้นหาข้อมูลหลังบ้าน หรือหลบเลี่ยงระบบป้องกันตรวจจับ (Web Application Firewall - WAF) การทำความเข้าใจพฤติกรรมผิดปกติเหล่านี้จึงมีความสำคัญอย่างมากต่อการรักษาความปลอดภัยของระบบเว็บ

#### 📊 ตารางสรุปสิ่งบ่งชี้ข้อความ HTTP ผิดปกติ (Key Malicious HTTP Indicators)

<div style="overflow-x:auto;margin:1.5rem auto;max-width:1000px;border:1px solid rgba(239,68,68,0.25);border-radius:12px;background:#05070f;box-shadow:0 10px 30px rgba(0,0,0,0.6);">
<table style="width:100%;border-collapse:collapse;text-align:left;font-family:sans-serif;font-size:0.83rem;color:#cbd5e1;">
<thead>
<tr style="background:rgba(239,68,68,0.08);border-bottom:1px solid rgba(239,68,68,0.2);">
<th style="padding:12px 16px;font-weight:bold;color:#ef4444;width:25%;">สิ่งบ่งชี้ (Indicator)</th>
<th style="padding:12px 16px;font-weight:bold;color:#ffffff;width:35%;">รายละเอียดการโจมตี (Description)</th>
<th style="padding:12px 16px;font-weight:bold;color:#fbbf24;width:40%;">ตัวอย่างข้อความ HTTP (Examples)</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;">1. Unusual HTTP Methods</td>
<td style="padding:12px 16px;">ใช้เมธอดแปลกประหลาดเพื่อดึงข้อมูลหรือดัดแปลงไฟล์บนระบบ</td>
<td style="padding:12px 16px;"><code style="color:#ef4444;">TRACE / HTTP/1.1</code> หรือใช้กลุ่ม WebDAV</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;">2. Unusual User-Agents</td>
<td style="padding:12px 16px;">ปลอมแปลงค่าหัวเบราว์เซอร์ หรือดึงค่าเปล่าเพื่อหลบเลี่ยงฟิลเตอร์</td>
<td style="padding:12px 16px;"><code style="color:#ef4444;">User-Agent: python-requests/2.26.0</code></td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;">3. Large or Encoded POST</td>
<td style="padding:12px 16px;">ส่งข้อมูลขนาดใหญ่มหึมา หรือเข้ารหัสคีย์ลับเพื่อซ่อนโค้ดเจาะระบบ</td>
<td style="padding:12px 16px;"><code style="color:#ef4444;">Content-Length: 50000</code> พร้อมข้อมูล Base64/Hex</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;">4. SQL Injection (SQLi)</td>
<td style="padding:12px 16px;">ป้อนชุดคำสั่งฐานข้อมูลเพื่อขโมยข้อมูลหลังบ้านผ่านช่องค้นหา</td>
<td style="padding:12px 16px;"><code style="color:#ef4444;">GET /login?user=admin' OR '1'='1</code></td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;">5. Command Injection</td>
<td style="padding:12px 16px;">แนบคำสั่งฝั่ง OS ไปรันที่ระบบปลายทางโดยตรง</td>
<td style="padding:12px 16px;"><code style="color:#ef4444;">GET /search?cmd=ls -la</code></td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;">6. Cross-Site Scripting (XSS)</td>
<td style="padding:12px 16px;">แทรกสคริปต์ JavaScript เพื่อโจมตีเบราว์เซอร์ผู้ใช้รายอื่น</td>
<td style="padding:12px 16px;"><code style="color:#ef4444;">GET /search?q=&lt;script&gt;alert(1)&lt;/script&gt;</code></td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;">7. File Inclusion (LFI/RFI)</td>
<td style="padding:12px 16px;">เรียกพาธในเครื่องระบบ หรือลิงก์ภายนอกผ่านพารามิเตอร์เว็บ</td>
<td style="padding:12px 16px;"><code style="color:#ef4444;">GET /index.php?page=../../../../etc/passwd</code></td>
</tr>
</tbody>
</table>
</div>

#### 💻 ตัวอย่างหน้าจอบันทึกประวัติการเข้าใช้งานเครื่องแม่ข่าย (Web Server Access Logs):

<div style="background:#0b0f19;border:1px solid rgba(239, 68, 68, 0.15);border-radius:12px;padding:24px;margin:2rem auto;max-width:900px;box-shadow:0 8px 32px rgba(0,0,0,0.45);font-family:'Inter',sans-serif;">
<div style="display:flex;align-items:center;justify-content:space-between;background:#1b1616;border-radius:8px 8px 0 0;padding:10px 16px;border-bottom:1px solid rgba(255,255,255,0.05);">
<div style="display:flex;gap:6px;">
<span style="width:10px;height:10px;background:#ef4444;border-radius:50%;display:inline-block;"></span>
<span style="width:10px;height:10px;background:#f59e0b;border-radius:50%;display:inline-block;"></span>
<span style="width:10px;height:10px;background:#10b981;border-radius:50%;display:inline-block;"></span>
</div>
<span style="color:#f87171;font-family:monospace;font-size:0.75rem;font-weight:bold;">access.log — malicious requests audit</span>
<div style="width:36px;"></div>
</div>
<div style="background:#070913;border-radius:0 0 8px 8px;padding:20px;text-align:left;overflow-x:auto;font-family:'JetBrains Mono',monospace;font-size:0.8rem;line-height:1.6;color:#cbd5e1;">
<span style="color:#64748b;"># 1. Directory Traversal Attempt (พยายามเจาะทะลุหาไฟล์ระบบ)</span><br>
192.168.1.10 - - [28/Feb/2025:12:34:56 +0000] "<span style="color:#ef4444;font-weight:bold;">GET /../../etc/passwd HTTP/1.1</span>" 200 1850<br><br>
<span style="color:#64748b;"># 2. SQL Injection Attack (พยายามแทรกคำสั่งฐานข้อมูล)</span><br>
192.168.1.20 - - [28/Feb/2025:12:35:10 +0000] "<span style="color:#f59e0b;font-weight:bold;">GET /login?username=admin' OR '1'='1 HTTP/1.1</span>" 403 245<br><br>
<span style="color:#64748b;"># 3. Brute Force Attack (พยายามสุ่มเดารหัสผ่านความถี่สูง)</span><br>
192.168.1.30 - - [28/Feb/2025:12:36:00 +0000] "POST /login HTTP/1.1" <span style="color:#ef4444;font-weight:bold;">401</span> 150<br>
192.168.1.30 - - [28/Feb/2025:12:36:01 +0000] "POST /login HTTP/1.1" <span style="color:#ef4444;font-weight:bold;">401</span> 150<br>
192.168.1.30 - - [28/Feb/2025:12:36:02 +0000] "POST /login HTTP/1.1" <span style="color:#ef4444;font-weight:bold;">401</span> 150
</div>
</div>

---

### 🔍 การใช้ HTTP Method ผิดปกติและช่องทาง WebDAV (Unusual HTTP Methods)

แม้แอปพลิเคชันเว็บทั่วไปจะใช้งานเพียง `GET`, `POST` และอาจมี `PUT`, `DELETE` ในระบบ REST API แต่ยังมีกลุ่มเมธอดผิดปกติหรือกลุ่มที่เป็นคุณลักษณะเก่าที่ระบบยังไม่ได้ปิดการทำงาน (เช่น **WebDAV**) ซึ่งนำมาซึ่งช่องโหว่ความเสถียรและความมั่นคงปลอดภัยได้:

#### รายละเอียดเมธอดเครือข่ายผิดปกติและการนำมาใช้โจมตี:

1. **OPTIONS**:
   - *วัตถุประสงค์*: ใช้แสดงรายการเมธอดทั้งหมดที่เว็บเซิร์ฟเวอร์ปลายทางเปิดใช้งานอยู่
   - *ช่องโหว่*: แฮกเกอร์ใช้เพื่อตรวจสอบความเหมาะสมเบื้องหลังว่าเป้าหมายเปิดให้รันสัญญลักษณ์ใดเพื่อโจมตีต่อ
2. **TRACE**:
   - *วัตถุประสงค์*: ส่งข้อความทวนสอบเพื่อให้เว็บเซิร์ฟเวอร์ส่งกลับมาเหมือนเดิมเพื่อการดีบั๊ก (Debugging)
   - *ช่องโหว่*: นำมาประยุกต์โจมตีประเภท **Cross-Site Tracing (XST)** เพื่อขโมยรหัสผ่านคุกกี้ของผู้เรียน
3. **CONNECT**:
   - *วัตถุประสงค์*: สร้างพาเนลทะลุผ่านความปลอดภัย (Tunneling) ไปยังโฮสต์ปลายทาง
   - *ช่องโหว่*: อาจถูกนำมาใช้เพื่อสแกนพอร์ต หรือทะลวงข้อมูลจราจรที่เป็นพิษผ่านตัวแทน (Proxy)
4. **WebDAV (PROPFIND, MKCOL, COPY, MOVE, LOCK, UNLOCK)**:
   - *คุณลักษณะ*: โพรโทคอลย่อยของ HTTP สำหรับการจัดระเบียบไฟล์เอกสารผ่านเว็บเซิร์ฟเวอร์
   - *ช่องโหว่*: หากไม่มีการตั้งสิทธิ์ความปลอดภัย แฮกเกอร์สามารถใช้คำสั่งสร้างโฟลเดอร์ คัดลอก ย้าย หรือล็อกไฟล์ระบบเป้าหมายได้โดยตรง

#### 💻 ตัวอย่างการส่งคำขอด้วย cURL เพื่อแอบเจาะใช้ช่องทางเมธอดพิเศษ:

<div style="background:#0b0f19;border:1px solid rgba(0, 240, 255, 0.15);border-radius:12px;padding:24px;margin:2rem auto;max-width:850px;box-shadow:0 8px 32px rgba(0,0,0,0.45);font-family:'Inter',sans-serif;">
<div style="display:flex;align-items:center;justify-content:space-between;background:#161b26;border-radius:8px 8px 0 0;padding:10px 16px;border-bottom:1px solid rgba(255,255,255,0.05);">
<div style="display:flex;gap:6px;">
<span style="width:10px;height:10px;background:#ef4444;border-radius:50%;display:inline-block;"></span>
<span style="width:10px;height:10px;background:#f59e0b;border-radius:50%;display:inline-block;"></span>
<span style="width:10px;height:10px;background:#10b981;border-radius:50%;display:inline-block;"></span>
</div>
<span style="color:#94a3b8;font-family:monospace;font-size:0.75rem;font-weight:bold;">terminal — exploiting unusual methods</span>
<div style="width:36px;"></div>
</div>
<div style="background:#070913;border-radius:0 0 8px 8px;padding:20px;text-align:left;overflow-x:auto;font-family:'JetBrains Mono',monospace;font-size:0.8rem;line-height:1.5;color:#cbd5e1;">
<span style="color:#64748b;"># 1. การยิงสแกนหาเมธอดเว็บที่เปิดสิทธิ์ไว้ (OPTIONS Audit)</span><br>
curl -X OPTIONS -i https://example.com<br><br>
<span style="color:#64748b;"># 2. การโจมตี Cross-Site Tracing (XST Attack)</span><br>
curl -X TRACE -H "XSS: &lt;script&gt;alert('XST')&lt;/script&gt;" https://example.com<br><br>
<span style="color:#64748b;"># 3. การส่งคำสั่งสร้างโฟลเดอร์ใหม่ (MKCOL WebDAV)</span><br>
curl -X MKCOL https://example.com/newdir<br><br>
<span style="color:#64748b;"># 4. การแอบคัดลอกไฟล์ระบบเป้าหมาย (COPY WebDAV)</span><br>
curl -X COPY -H "Destination: https://example.com/backup" https://example.com/secretfile.txt
</div>
</div>

---

### 🕵️ การตรวจวิเคราะห์ข้อมูลส่วนหัวบราวเซอร์ (Unusual User-Agents)

**User-Agent** คือข้อความส่วนหัว HTTP ที่เว็บเบราว์เซอร์ส่งไปให้เครื่องแม่ข่าย เพื่อรายงานรายละเอียดระบบปฏิบัติการ โปรเซสเซอร์ และรุ่นของโปรแกรมที่เปิดเชื่อมต่อเข้ามา ซึ่งเซิร์ฟเวอร์จะนำข้อมูลนี้ไปคัดสรรฟอร์แมตการแสดงผลให้เหมาะสม แต่แฮกเกอร์มักเปลี่ยนค่า User-Agent เพื่อวัตถุประสงค์เหล่านี้:
- หลบเลี่ยงระบบบล็อกแบนด์วิดท์ หรือกฎ WAF
- ปลอมตัวเป็นระบบตรวจเก็บข้อมูลปกติ (เช่น บอทค้นหา Googlebot)
- ปิดบังซอฟต์แวร์สแกนความปลอดภัยที่แฮกเกอร์ใช้งาน

#### ตารางแสดงรายการ User-Agents ผิดปกติที่นิยมใช้ตรวจจับการโจมตี (Unusual User-Agent Signatures)

<div style="overflow-x:auto;margin:1.5rem auto;max-width:1000px;border:1px solid rgba(6,182,212,0.25);border-radius:12px;background:#05070f;box-shadow:0 10px 30px rgba(0,0,0,0.6);">
<table style="width:100%;border-collapse:collapse;text-align:left;font-family:sans-serif;font-size:0.83rem;color:#cbd5e1;">
<thead>
<tr style="background:rgba(6,182,212,0.08);border-bottom:1px solid rgba(6,182,212,0.2);">
<th style="padding:12px 16px;font-weight:bold;color:#00f0ff;width:25%;">ซอฟต์แวร์ต้นกำเนิด</th>
<th style="padding:12px 16px;font-weight:bold;color:#ffffff;width:35%;">รูปแบบ/ความเสี่ยงความมั่นคงปลอดภัย</th>
<th style="padding:12px 16px;font-weight:bold;color:#3ddc84;width:40%;">ตัวอย่างข้อความหัวดิบ (User-Agent String)</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;">1. Empty (ช่องว่าง)</td>
<td style="padding:12px 16px;">สแกนเนอร์หรือบอทตัดส่วนหัว User-Agent ทิ้งเพื่อลบลายเซ็นแฝง</td>
<td style="padding:12px 16px;"><code style="color:#ef4444;">""</code> (ค่าว่างเปล่า)</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;">2. Custom Fake</td>
<td style="padding:12px 16px;">ตั้งค่าหลอกลวงเบื้องต้นเพื่ออำพรางตัวหลีกเลี่ยงการสกัดกั้น</td>
<td style="padding:12px 16px;"><code style="color:#ef4444;">HackerTool/1.0</code></td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;">3. cURL / Wget</td>
<td style="padding:12px 16px;">ยิงผ่านคำสั่งรันสคริปต์อัตโนมัติหรือสกัดกั้นดึงข้อมูลระบบ</td>
<td style="padding:12px 16px;"><code style="color:#ef4444;">curl/7.64.1</code> หรือ <code style="color:#ef4444;">Wget/1.20.3</code></td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;">4. Burp Suite Scanner</td>
<td style="padding:12px 16px;">ใช้เครื่องมือสำรวจสแกนหาช่องโหว่ความเสี่ยงสูงอัตโนมัติ</td>
<td style="padding:12px 16px;"><code style="color:#ef4444;">Mozilla/5.0 (...) BurpSuite</code></td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;">5. SQLMap</td>
<td style="padding:12px 16px;">เจาะระบบหาฐานข้อมูลเชิงลึกแบบอัตโนมัติผ่านช่องโหว่ SQLi</td>
<td style="padding:12px 16px;"><code style="color:#ef4444;">sqlmap/1.5.2#dev</code></td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;">6. Nmap / Nikto</td>
<td style="padding:12px 16px;">สแกนหาพอร์ตและช่องโหว่ของเซิร์ฟเวอร์ระบบทั้งหมด</td>
<td style="padding:12px 16px;"><code style="color:#ef4444;">Mozilla/5.0 (compatible; Nmap Scripting Engine;...)</code></td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;">7. Python Requests</td>
<td style="padding:12px 16px;">การรันยิงส่งโจมตีผ่านสคริปต์สคริปต์สแกนช่องโหว่</td>
<td style="padding:12px 16px;"><code style="color:#ef4444;">python-requests/2.25.1</code></td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;">8. Metasploit</td>
<td style="padding:12px 16px;">รันโค้ดเจาะทำลายขโมยข้อมูลหลังบ้านผ่านเมทาสปลอยต์</td>
<td style="padding:12px 16px;"><code style="color:#ef4444;">Mozilla/5.0 (...) Metasploit</code></td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;">9. Googlebot Spoofing</td>
<td style="padding:12px 16px;">ปลอมเป็นโปรแกรมกวาดเสิร์ชเอนจินของ Google เพื่อเปิดสิทธิ์ฟรี</td>
<td style="padding:12px 16px;"><code style="color:#ef4444;">Googlebot/2.1 (+http://www.google.com/bot.html)</code></td>
</tr>
</tbody>
</table>
</div>

#### 💻 ตัวอย่างการส่งคำขอด้วย cURL แบบปลอมแปลงส่วนหัว User-Agent เพื่อหลบเลี่ยง:

<div style="background:#0b0f19;border:1px solid rgba(0, 240, 255, 0.15);border-radius:12px;padding:24px;margin:2rem auto;max-width:850px;box-shadow:0 8px 32px rgba(0,0,0,0.45);font-family:'Inter',sans-serif;">
<div style="display:flex;align-items:center;justify-content:space-between;background:#161b26;border-radius:8px 8px 0 0;padding:10px 16px;border-bottom:1px solid rgba(255,255,255,0.05);">
<div style="display:flex;gap:6px;">
<span style="width:10px;height:10px;background:#ef4444;border-radius:50%;display:inline-block;"></span>
<span style="width:10px;height:10px;background:#f59e0b;border-radius:50%;display:inline-block;"></span>
<span style="width:10px;height:10px;background:#10b981;border-radius:50%;display:inline-block;"></span>
</div>
<span style="color:#94a3b8;font-family:monospace;font-size:0.75rem;font-weight:bold;">terminal — spoofed user-agent testing</span>
<div style="width:36px;"></div>
</div>
<div style="background:#070913;border-radius:0 0 8px 8px;padding:20px;text-align:left;overflow-x:auto;font-family:'JetBrains Mono',monospace;font-size:0.8rem;line-height:1.5;color:#cbd5e1;">
<span style="color:#64748b;"># การรันสั่งส่งคำขอปลอมค่า User-Agent เป็นอุปกรณ์ธนาคารหลอกลวง (BankWongyos)</span><br>
curl -X GET -H "User-Agent: BankWongyos/1.0" -i http://202.29.103.200/<br><br>
<span style="color:#64748b;"># ตัวนำส่ง HTTP Request จริงที่วิ่งออกระบบเครือข่าย</span><br>
GET / HTTP/1.1<br>
Host: 202.29.103.200<br>
Accept: */*<br>
<span style="color:#fbbf24;">User-Agent: BankWongyos/1.0</span><br><br>
<span style="color:#64748b;"># ผลตอบรับการประมวลผลสำเร็จกลับมา (HTTP Response)</span><br>
HTTP/1.1 200 OK<br>
Server: nginx/1.17.10<br>
Date: Tue, 04 Mar 2025 17:20:36 GMT
</div>
</div>

---

### 📦 การโจมตีผ่านคำขอขนาดใหญ่และการเข้ารหัสพฤติกรรมหลบเลี่ยง (Large & Encoded POST Requests)

โดยธรรมชาติแล้ว ข้อความ **GET Request** จะมีข้อจำกัดด้านความยาวพาธ (URL limit) อยู่ที่ประมาณ **2KB (2048 bytes)** เท่านั้น หากเกินกว่านี้เบราว์เซอร์หรือโปรแกรมตรวจรับจะไม่ส่งข้อมูลต่อ แต่ข้อความ **POST Request** ได้รับการออกแบบให้ส่งข้อมูลผ่านเนื้อหาหลัก (Body) ซึ่งแทบ **ไม่มีขีดจำกัดขนาดข้อมูล** ทำให้ผู้โจมตีมักเลือกใช้ช่องทาง POST เพื่อส่งไฟล์มุ่งร้าย แทรกโค้ดขนาดใหญ่ หรือเข้ารหัสไฟล์เพื่อหลีกเลี่ยงเครื่องมือรักษาความปลอดภัย (WAF)

#### ขีดจำกัดเริ่มต้นของขนาดรับส่งไฟล์ประเภท HTTP POST (POST body limits):
- **Nginx**: ขนาดจำกัดเริ่มต้น (Default) คือ **1MB** (สามารถแก้ไขคอนฟิกปรับเปลี่ยนได้ตามเหมาะสม)
- **Apache**: ขีดจำกัดการรับส่งไฟล์สูงสุดอยู่ที่ **2GB**
- **IIS (Windows)**: ขนาดเริ่มต้นอยู่ที่ **28.6MB** (และจำกัดพารามิเตอร์ URL ในคิวรีไม่เกิน 2048 bytes)

#### รูปแบบการโจมตีและการเข้ารหัสข้อมูลใน POST Request ที่พบบ่อย:

1. **ส่งสคริปต์อันตรายขนาดใหญ่เพื่อเจาะ SQL Injection (Large SQLi Payload)**:
   - นักโจมตีจะระบุข้อมูลอักขระขยะจำนวนหลายพันตัวแปรเพื่อปั่นป่วนระบบตรวจวิเคราะห์ และปิดท้ายด้วยคำสั่งแทรกฐานข้อมูล
   ```http
   POST /search HTTP/1.1
   Host: example.com
   Content-Type: application/x-www-form-urlencoded
   Content-Length: 5000
   
   search=aaaaaaaaaaaaaaaaaaaa...(5000 characters)...' OR 1=1 --
   ```
2. **การอัปโหลดไฟล์ไม่พึงประสงค์ (Web Shell Upload Exploitation)**:
   - การซ่อนโค้ดสั่งรันคำสั่ง OS (Web Shell เช่น `.php`) ผ่านคำขอประเภทอัปโหลดไฟล์ขนาดใหญ่แบบ `multipart/form-data`
   ```http
   POST /upload HTTP/1.1
   Host: example.com
   Content-Type: multipart/form-data; boundary=----XYZ
   Content-Length: 15000
   
   ------XYZ
   Content-Disposition: form-data; name="file"; filename="shell.php"
   Content-Type: application/x-php
   
   <?php system($_GET['cmd']); ?>
   ------XYZ-
   ```
3. **การเข้ารหัสอำพรางโค้ดสคริปต์ (Base64 Encoded Payloads)**:
   - แปลงโค้ดมุ่งร้ายหลักให้เป็นอักขระตาราง Base64 เพื่อให้เครื่องมือ WAF ที่ดักสืบคำดักจับไม่เข้าใจความหมาย
   ```http
   POST /api HTTP/1.1
   Host: example.com
   Content-Type: application/x-www-form-urlencoded
   Content-Length: 300
   
   data=PHNjcmlwdD5hbGVydCgnWHNTJyk8L3NjcmlwdD4=  <-- โค้ดที่ผ่านการเข้ารหัส <script>alert('XSS')</script>
   ```
4. **การเข้ารหัสพาธ URL และเลขฐานสิบหก (URL & Hex Encoding)**:
   - เข้ารหัสด้วยรูปแบบ `%` (เช่น `%3Cscript%3E` ➡️ `<script>`) หรือรูปแบบ Hex String (เช่น `3C73637269...`) เพื่อหลบเลี่ยงการตรวจสอบของฟิลเตอร์กรองอักขระพิเศษ
   ```http
   POST /api HTTP/1.1
   Host: example.com
   Content-Length: 100
   
   data=%3Cscript%3Ealert%281%29%3C%2Fscript%3E
   ```

"""

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        try:
            blocks = json.loads(l.content)
            val = blocks[0]["value"]
            
            # Find the Web Page Source Inspections header
            target_inspections = "### 🛠️ เครื่องมือแกะรหัสหน้าเว็บ (Web Page Source Inspections)"
            idx = val.find(target_inspections)
            
            if idx != -1:
                # Insert this malicious HTTP messages section right before the source inspections
                new_val = val[:idx] + malicious_http_html + "\n\n" + val[idx:]
                blocks[0]["value"] = new_val
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print("Successfully inserted malicious HTTP message detection section into database!")
            else:
                # If target is not found, prepend
                new_val = malicious_http_html + "\n\n" + val
                blocks[0]["value"] = new_val
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print("Prepended malicious HTTP message detection section successfully!")
        except Exception as e:
            print(f"Error: {e}")
