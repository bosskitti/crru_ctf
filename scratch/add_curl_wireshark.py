import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

curl_wireshark_html = """

---

### 🛠️ การใช้งานเครื่องมือ cURL สำหรับส่งข้อความเว็บ (HTTP Client Utility)

**cURL (Client URL)** คือเครื่องมือประเภทบรรทัดคำสั่ง (Command-line tool) ที่มีประสิทธิภาพสูง ขับเคลื่อนด้วยไลบรารีเบื้องหลังคือ **libcurl** ใช้สำหรับรับส่งถ่ายข้อมูลผ่านโพรโทคอลเครือข่ายที่หลากหลาย เช่น HTTP, HTTPS, FTP, SFTP โดยนักทดสอบระบบมักเลือกใช้เพื่อสแกนทดสอบการทำงานของเว็บแอปพลิเคชัน (API testing), ดาวน์โหลดไฟล์ และตรวจสอบปัญหาความปลอดภัยเครือข่าย

#### 💻 หน้าจอตัวเลือกคำสั่งเพิ่มเติมของ cURL (cURL Option Help Menu):

<div style="background:#0b0f19;border:1px solid rgba(0, 240, 255, 0.15);border-radius:12px;padding:24px;margin:2rem auto;max-width:850px;box-shadow:0 8px 32px rgba(0,0,0,0.45);font-family:'Inter',sans-serif;">
<div style="display:flex;align-items:center;justify-content:space-between;background:#161b26;border-radius:8px 8px 0 0;padding:10px 16px;border-bottom:1px solid rgba(255,255,255,0.05);">
<div style="display:flex;gap:6px;">
<span style="width:10px;height:10px;background:#ef4444;border-radius:50%;display:inline-block;"></span>
<span style="width:10px;height:10px;background:#f59e0b;border-radius:50%;display:inline-block;"></span>
<span style="width:10px;height:10px;background:#10b981;border-radius:50%;display:inline-block;"></span>
</div>
<span style="color:#94a3b8;font-family:monospace;font-size:0.75rem;font-weight:bold;">terminal — curl help options</span>
<div style="width:36px;"></div>
</div>
<div style="background:#070913;border-radius:0 0 8px 8px;padding:20px;text-align:left;overflow-x:auto;font-family:'JetBrains Mono',monospace;font-size:0.8rem;line-height:1.5;color:#cbd5e1;">
<span style="color:#64748b;">(kali@kali)-[~] $ curl --help</span><br>
Usage: curl [options...] &lt;url&gt;<br>
  -d, --data &lt;data&gt;          HTTP POST data (ส่งข้อมูลแบบ POST payload)<br>
  -f, --fail                 Fail fast with no output on HTTP errors (ข้ามผลลัพธ์กรณี HTTP Error)<br>
  -h, --help &lt;category&gt;      Get help for commands (ดูคู่มือหมวดหมู่ของคำสั่ง)<br>
  -i, --include              Include response headers in output (แสดง Headers ตอบกลับในผลลัพธ์)<br>
  -o, --output &lt;file&gt;        Write to file instead of stdout (บันทึกข้อมูลผลลัพธ์เป็นไฟล์ที่ตั้งชื่อเอง)<br>
  -O, --remote-name          Write output to file named as remote file (บันทึกไฟล์เป็นชื่อเดียวกับปลายทาง)<br>
  -s, --silent               Silent mode (โหมดเงียบ ไม่แสดงแถบดาวน์โหลดและการทำงานขัดข้อง)<br>
  -T, --upload-file &lt;file&gt;   Transfer local FILE to destination (อัปโหลดไฟล์ในเครื่องไปยังเซิร์ฟเวอร์)<br>
  -u, --user &lt;user:pwd&gt;      Server user and password (ป้อนชื่อและรหัสผ่านยืนยันสิทธิ์)<br>
  -A, --user-agent &lt;name&gt;    Send User-Agent &lt;name&gt; to server (ปลอมแปลงชื่อ Browser Client)<br>
  -v, --verbose              Make the operation more talkative (โหมดรายงานการเชื่อมต่อเชิงลึก)<br>
  -V, --version              Show version number and quit (ตรวจสอบรุ่นเวอร์ชันของโปรแกรม)<br>
</div>
</div>

#### ตารางสรุปคีย์คำสั่ง cURL ยอดนิยม (Common cURL Command Examples)

<div style="overflow-x:auto;margin:1.5rem auto;max-width:1000px;border:1px solid rgba(168,85,247,0.25);border-radius:12px;background:#05070f;box-shadow:0 10px 30px rgba(0,0,0,0.6);">
<table style="width:100%;border-collapse:collapse;text-align:left;font-family:sans-serif;font-size:0.85rem;color:#cbd5e1;">
<thead>
<tr style="background:rgba(168,85,247,0.08);border-bottom:1px solid rgba(168,85,247,0.2);">
<th style="padding:12px 16px;font-weight:bold;color:#a855f7;width:30%;">จุดประสงค์ (Purpose)</th>
<th style="padding:12px 16px;font-weight:bold;color:#3ddc84;width:70%;">รูปแบบการเขียนคำสั่ง (Command Example)</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;vertical-align:middle;">1. ส่งคำขอแบบดึงข้อมูล (GET Request)</td>
<td style="padding:12px 16px;vertical-align:middle;">
<code style="color:#00f0ff;background:rgba(0,240,255,0.05);padding:4px 8px;border-radius:4px;border:1px solid rgba(0,240,255,0.1);font-family:monospace;display:block;font-size:0.78rem;">curl -X GET https://api.example.com/data</code>
</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;vertical-align:middle;">2. ส่งคำขอแบบป้อนพารามิเตอร์ (POST Request)</td>
<td style="padding:12px 16px;vertical-align:middle;">
<code style="color:#00f0ff;background:rgba(0,240,255,0.05);padding:4px 8px;border-radius:4px;border:1px solid rgba(0,240,255,0.1);font-family:monospace;display:block;font-size:0.78rem;">curl -X POST -d "username=admin&password=1234" https://api.example.com/login</code>
</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;vertical-align:middle;">3. แนบข้อมูลส่วนหัวคีย์ลับ (Custom Headers)</td>
<td style="padding:12px 16px;vertical-align:middle;">
<code style="color:#00f0ff;background:rgba(0,240,255,0.05);padding:4px 8px;border-radius:4px;border:1px solid rgba(0,240,255,0.1);font-family:monospace;display:block;font-size:0.78rem;">curl -H "Authorization: Bearer token123" https://api.example.com/data</code>
</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;vertical-align:middle;">4. ดาวน์โหลดไฟล์จากลิงก์ปลายทาง (Download)</td>
<td style="padding:12px 16px;vertical-align:middle;">
<code style="color:#00f0ff;background:rgba(0,240,255,0.05);padding:4px 8px;border-radius:4px;border:1px solid rgba(0,240,255,0.1);font-family:monospace;display:block;font-size:0.78rem;">curl -O https://example.com/file.zip</code>
</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;vertical-align:middle;">5. ขอตรวจดูเฉพาะข้อมูลส่วนหัว (Response Headers)</td>
<td style="padding:12px 16px;vertical-align:middle;">
<code style="color:#00f0ff;background:rgba(0,240,255,0.05);padding:4px 8px;border-radius:4px;border:1px solid rgba(0,240,255,0.1);font-family:monospace;display:block;font-size:0.78rem;">curl -I https://www.google.com/</code>
</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;vertical-align:middle;">6. สั่งให้วิ่งตามลิงก์เปลี่ยนปลายทาง (Follow Redirects)</td>
<td style="padding:12px 16px;vertical-align:middle;">
<code style="color:#00f0ff;background:rgba(0,240,255,0.05);padding:4px 8px;border-radius:4px;border:1px solid rgba(0,240,255,0.1);font-family:monospace;display:block;font-size:0.78rem;">curl -L https://bit.ly/example</code>
</td>
</tr>
</tbody>
</table>
</div>

#### 💻 ตัวอย่างหน้าจอการตรวจสอบ Response Headers ด้วยคำสั่ง curl -I:

<div style="background:#0b0f19;border:1px solid rgba(0, 240, 255, 0.15);border-radius:12px;padding:24px;margin:2rem auto;max-width:850px;box-shadow:0 8px 32px rgba(0,0,0,0.45);font-family:'Inter',sans-serif;">
<div style="display:flex;align-items:center;justify-content:space-between;background:#161b26;border-radius:8px 8px 0 0;padding:10px 16px;border-bottom:1px solid rgba(255,255,255,0.05);">
<div style="display:flex;gap:6px;">
<span style="width:10px;height:10px;background:#ef4444;border-radius:50%;display:inline-block;"></span>
<span style="width:10px;height:10px;background:#f59e0b;border-radius:50%;display:inline-block;"></span>
<span style="width:10px;height:10px;background:#10b981;border-radius:50%;display:inline-block;"></span>
</div>
<span style="color:#94a3b8;font-family:monospace;font-size:0.75rem;font-weight:bold;">terminal — curl response headers</span>
<div style="width:36px;"></div>
</div>
<div style="background:#070913;border-radius:0 0 8px 8px;padding:20px;text-align:left;overflow-x:auto;font-family:'JetBrains Mono',monospace;font-size:0.8rem;line-height:1.5;color:#cbd5e1;">
<span style="color:#64748b;">(kali@kali)-[~] $ curl -I https://www.google.com/</span><br>
HTTP/2 200<br>
content-type: text/html; charset=ISO-8859-1<br>
<span style="color:#3ddc84;">content-security-policy-report-only: object-src 'none'; base-uri 'self'; script-src 'nonce-...';</span><br>
accept-ch: Sec-CH-Prefers-Color-Scheme<br>
p3p: CP="This is not a P3P policy! See g.co/p3phelp for more info."<br>
date: Mon, 03 Mar 2025 17:24:06 GMT<br>
server: gws<br>
<span style="color:#ef4444;">x-xss-protection: 0</span><br>
<span style="color:#3ddc84;">x-frame-options: SAMEORIGIN</span><br>
expires: Mon, 03 Mar 2025 17:24:06 GMT<br>
cache-control: private<br>
<span style="color:#fbbf24;">set-cookie: AEC=AVcja2c2...; expires=Sat, 30-Aug-2025 17:24:06 GMT; Secure; HttpOnly; SameSite=lax</span><br>
alt-svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
</div>
</div>

---

### 🕵️ การเปรียบเทียบข้อมูลจราจรระหว่างคำสั่ง cURL และตัวดักจับแพ็กเก็ต Wireshark

เพื่อทำความเข้าใจการเคลื่อนที่ของข้อมูลเว็บอย่างลึกซึ้ง นักทดสอบระบบมักจะเปิดคำสั่ง **cURL** ควบคู่ไปกับ **Wireshark (Packet Analyzer)** เพื่อดักสืบสวนหาแพ็กเก็ตนำส่งจริงบนระบบเน็ตเวิร์ก:

<div style="display:flex;gap:20px;flex-wrap:wrap;justify-content:center;margin:2rem auto;max-width:1000px;font-family:'Inter',sans-serif;">
<div style="flex:1;min-width:320px;background:#0b0f19;border:1px solid rgba(0, 240, 255, 0.15);border-radius:12px;padding:20px;box-shadow:0 6px 20px rgba(0,0,0,0.35);">
<div style="color:#00f0ff;font-weight:bold;font-size:0.88rem;margin-bottom:12px;border-bottom:1px solid rgba(0,240,255,0.1);padding-bottom:6px;"><i class="fas fa-terminal mr-1"></i> 1. ส่ง HTTP Request ผ่าน cURL</div>
<div style="background:#070913;border-radius:6px;padding:12px;font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:#cbd5e1;text-align:left;height:220px;overflow-y:auto;line-height:1.4;">
<span style="color:#64748b;">$ curl -X GET http://202.29.103.200/</span><br>
&lt;!DOCTYPE html&gt;<br>
&lt;html&gt;<br>
&lt;head&gt;<br>
&nbsp;&nbsp;&lt;title&gt;Wongyos CTF&lt;/title&gt;<br>
&nbsp;&nbsp;&lt;meta charset="utf-8"&gt;<br>
&nbsp;&nbsp;&lt;link rel="stylesheet" href="/style.css"&gt;<br>
&lt;/head&gt;<br>
&lt;body&gt;...&lt;/body&gt;<br>
&lt;/html&gt;
</div>
</div>
<div style="flex:1;min-width:320px;background:#0b0f19;border:1px solid rgba(16, 185, 129, 0.15);border-radius:12px;padding:20px;box-shadow:0 6px 20px rgba(0,0,0,0.35);">
<div style="color:#10b981;font-weight:bold;font-size:0.88rem;margin-bottom:12px;border-bottom:1px solid rgba(16,185,129,0.1);padding-bottom:6px;"><i class="fas fa-search-plus mr-1"></i> 2. ตรวจสอบข้อมูลแพ็กเก็ตใน Wireshark</div>
<div style="background:#070913;border-radius:6px;padding:12px;font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:#cbd5e1;text-align:left;height:220px;overflow-y:auto;line-height:1.4;">
<span style="color:#ef4444;font-weight:bold;"># [HTTP Request Packet]</span><br>
<span style="color:#ef4444;">GET / HTTP/1.1<br>
Host: 202.29.103.200<br>
User-Agent: curl/8.7.1<br>
Accept: */*</span><br><br>
<span style="color:#60a5fa;font-weight:bold;"># [HTTP Response Packet]</span><br>
<span style="color:#60a5fa;">HTTP/1.1 200 OK<br>
Server: nginx/1.17.10<br>
Date: Tue, 04 Mar 2025 17:36:20 GMT<br>
Content-Type: text/html; charset=utf-8<br>
Content-Length: 5750<br>
Set-Cookie: session=df930ce1-8fec...</span>
</div>
</div>
</div>

> [!TIP]
> **การดักจับข้อความ HTTP ด้วย Wireshark**:
> การรันคำสั่ง `curl` จะทำงานในระดับแอพพลิเคชัน แต่เมื่อผ่านลงไปที่การส่งข้อมูลจริงในเน็ตเวิร์ก โปรแกรมดักจับ **Wireshark** จะประกอบกลุ่มแพ็กเก็ต TCP/IP กลับคืนมาเป็นตัวอักษรดิบ ทำให้แฮกเกอร์และผู้ตรวจสอบระบบสามารถแกะดูรหัสผ่านพารามิเตอร์ หรือค่าคุกกี้เซสชันที่ส่งไปได้ทั้งหมดโดยตรง (หากเป็นการเชื่อมต่อแบบปกติที่ไม่ได้เข้ารหัสความปลอดภัย HTTPS)

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
                # Insert the cURL & Wireshark section right before the source inspections
                new_val = val[:idx] + curl_wireshark_html + "\n\n" + val[idx:]
                blocks[0]["value"] = new_val
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print("Successfully inserted cURL and Wireshark details into the database!")
            else:
                # If target is not found, prepend
                new_val = curl_wireshark_html + "\n\n" + val
                blocks[0]["value"] = new_val
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print("Prepended cURL and Wireshark details successfully!")
        except Exception as e:
            print(f"Error: {e}")
