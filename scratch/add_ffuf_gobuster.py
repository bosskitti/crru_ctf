import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

ffuf_gobuster_html = """

---

### ⚡ การใช้งานเครื่องมือ FFUF (Fast Web Fuzzer)

**FFUF** เป็นเครื่องมือประเภท Command-line Fuzzing ที่มีประสิทธิภาพความเร็วสูงพิเศษ (High performance) เขียนด้วยภาษา Go นิยมใช้สแกนค้นหาชื่อไฟล์ โฟลเดอร์ลับ และทำเว็บฟัซซิงพารามิเตอร์อื่นๆ โดยทำงานร่วมกับค่าตำแหน่งจุดเปลี่ยนที่เราป้อนคีย์เวิร์ดคำว่า <code style="color: #fbbf24; font-weight: bold;">FUZZ</code> ไว้

#### 💻 ตัวอย่างหน้าต่างสแกนและแสดงผลลัพธ์ของ FFUF (FFUF Execution Logs):

<div style="background:#0b0f19;border:1px solid rgba(0, 240, 255, 0.15);border-radius:12px;padding:24px;margin:2rem auto;max-width:850px;box-shadow:0 8px 32px rgba(0,0,0,0.45);font-family:'Inter',sans-serif;">
<div style="display:flex;align-items:center;justify-content:space-between;background:#161b26;border-radius:8px 8px 0 0;padding:10px 16px;border-bottom:1px solid rgba(255,255,255,0.05);">
<div style="display:flex;gap:6px;">
<span style="width:10px;height:10px;background:#ef4444;border-radius:50%;display:inline-block;"></span>
<span style="width:10px;height:10px;background:#f59e0b;border-radius:50%;display:inline-block;"></span>
<span style="width:10px;height:10px;background:#10b981;border-radius:50%;display:inline-block;"></span>
</div>
<span style="color:#94a3b8;font-family:monospace;font-size:0.75rem;font-weight:bold;">terminal — ffuf fuzzing</span>
<div style="width:36px;"></div>
</div>
<div style="background:#070913;border-radius:0 0 8px 8px;padding:20px;text-align:left;overflow-x:auto;font-family:'JetBrains Mono',monospace;font-size:0.8rem;line-height:1.5;color:#cbd5e1;">
<span style="color:#64748b;">(kali@kali)-[~] $ ffuf -u https://www.google.com/FUZZ -w /usr/share/wordlists/wfuzz/general/common.txt -t 1000</span><br><br>
<pre style="color:#fbbf24;font-family:monospace;font-size:0.72rem;line-height:1.25;border:none;background:transparent;padding:0;margin:10px 0;">
        /'___\  /'___\           /\_ \
       /\ \__/ /\ \__/  __  __   \//\ \
       \ \  _``\ \  _``/\ \/\ \    \ \ \
        \ \ \_/\ \ \_/\ \ \_\ \    \_\ \_
         \ \_\  \ \_\  \ \____/    /\____\
          \/_/   \/_/   \/___/     \/____/

       v2.1.0-dev
</pre>
:: Method           : GET<br>
:: URL              : https://www.google.com/FUZZ<br>
:: Wordlist         : FUZZ: /usr/share/wordlists/wfuzz/general/common.txt<br>
:: Follow redirects : false<br>
:: Calibration      : false<br>
:: Timeout          : 10<br>
:: Threads          : 1000<br>
:: Matcher          : Response status: 200-299,301,302,307,401,403,405,500<br>
____________________________________________________________________<br><br>
<span style="color:#fbbf24;">about         [Status: 302, Size: 218, Words: 9, Lines: 7, Duration: 66ms]</span><br>
<span style="color:#fbbf24;">2005          [Status: 301, Size: 239, Words: 9, Lines: 7, Duration: 62ms]</span><br>
<span style="color:#fbbf24;">design        [Status: 302, Size: 219, Words: 9, Lines: 7, Duration: 61ms]</span><br>
<span style="color:#10b981;">security      [Status: 301, Size: 227, Words: 9, Lines: 7, Duration: 64ms]</span><br>
<span style="color:#fbbf24;">contacts      [Status: 302, Size: 225, Words: 9, Lines: 7, Duration: 55ms]</span>
</div>
</div>

#### ตารางสรุปรูปแบบการใช้งานคำสั่ง FFUF (FFUF Command Cheat Sheet)

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
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;vertical-align:middle;">1. ค้นหาโฟลเดอร์ในไดเรกทอรีเฉพาะ</td>
<td style="padding:12px 16px;vertical-align:middle;">
<code style="color:#00f0ff;background:rgba(0,240,255,0.05);padding:4px 8px;border-radius:4px;border:1px solid rgba(0,240,255,0.1);font-family:monospace;display:block;font-size:0.78rem;">ffuf -u https://target.com/admin/FUZZ -w /usr/share/wordlists/rockyou.txt</code>
<span style="font-size:0.75rem;color:#94a3b8;display:block;margin-top:4px;">ยิงสแกนหาพาธภายใต้โฟลเดอร์ admin โดยสลับคำศัพท์ที่ตำแหน่ง <code style="color:#fbbf24;">FUZZ</code></span>
</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;vertical-align:middle;">2. การสแกนไฟล์และคัดกรองขนาดขนาดไฟล์ (Fuzz with Size Filter)</td>
<td style="padding:12px 16px;vertical-align:middle;">
<code style="color:#00f0ff;background:rgba(0,240,255,0.05);padding:4px 8px;border-radius:4px;border:1px solid rgba(0,240,255,0.1);font-family:monospace;display:block;font-size:0.78rem;">ffuf -u https://example.org/FUZZ -w wordlist.txt -mc all -fs 42 -c -v</code>
<span style="font-size:0.75rem;color:#94a3b8;display:block;margin-top:4px;">สแกนทุกรหัสตอบรับ (<code style="color:#ff007f;">-mc all</code>) แต่คัดกรองนำไฟล์ขนาด 42 bytes ออกจากรายงานสแกน (<code style="color:#ff007f;">-fs 42</code>)</span>
</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;vertical-align:middle;">3. ค้นหาชื่อโดเมนเสมือน (Fuzz Host-header / Subdomains)</td>
<td style="padding:12px 16px;vertical-align:middle;">
<code style="color:#00f0ff;background:rgba(0,240,255,0.05);padding:4px 8px;border-radius:4px;border:1px solid rgba(0,240,255,0.1);font-family:monospace;display:block;font-size:0.78rem;">ffuf -w hosts.txt -u https://example.org/ -H "Host: FUZZ" -mc 200</code>
<span style="font-size:0.75rem;color:#94a3b8;display:block;margin-top:4px;">ฟัซหาชื่อโดเมนภายใต้ส่วนหัว HTTP Host header และคัดเลือกเฉพาะรหัส HTTP 200</span>
</td>
</tr>
</tbody>
</table>
</div>

---

### 📦 การใช้งานเครื่องมือ Gobuster (Go Web Buster)

**Gobuster** คืออีกหนึ่งเครื่องมือความเร็วสูงเขียนขึ้นด้วยภาษา Go (ทำให้มีรอบความเร็วกว่าตัวสแกนทั่วไป) นิยมใช้ค้นหาไดเรกทอรี โฟลเดอร์ ค้นหาซับโดเมนระบบ (DNS subdomains) และเวอร์ชวลโฮสต์การแสดงผล

#### 💻 ตัวอย่างหน้าต่างสแกนและแสดงผลลัพธ์ของ Gobuster ในโหมด DNS (Gobuster DNS Logs):

<div style="background:#0b0f19;border:1px solid rgba(0, 240, 255, 0.15);border-radius:12px;padding:24px;margin:2rem auto;max-width:850px;box-shadow:0 8px 32px rgba(0,0,0,0.45);font-family:'Inter',sans-serif;">
<div style="display:flex;align-items:center;justify-content:space-between;background:#161b26;border-radius:8px 8px 0 0;padding:10px 16px;border-bottom:1px solid rgba(255,255,255,0.05);">
<div style="display:flex;gap:6px;">
<span style="width:10px;height:10px;background:#ef4444;border-radius:50%;display:inline-block;"></span>
<span style="width:10px;height:10px;background:#f59e0b;border-radius:50%;display:inline-block;"></span>
<span style="width:10px;height:10px;background:#10b981;border-radius:50%;display:inline-block;"></span>
</div>
<span style="color:#94a3b8;font-family:monospace;font-size:0.75rem;font-weight:bold;">terminal — gobuster dns scan</span>
<div style="width:36px;"></div>
</div>
<div style="background:#070913;border-radius:0 0 8px 8px;padding:20px;text-align:left;overflow-x:auto;font-family:'JetBrains Mono',monospace;font-size:0.8rem;line-height:1.5;color:#cbd5e1;">
<span style="color:#64748b;">(kali@kali)-[~] $ gobuster dns -d google.com -w /usr/share/wordlists/dirb/common.txt</span><br><br>
===============================================================<br>
Gobuster v3.6 - by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)<br>
===============================================================<br>
[+] Domain:     google.com<br>
[+] Threads:    10<br>
[+] Timeout:    1s<br>
[+] Wordlist:   /usr/share/wordlists/dirb/common.txt<br>
===============================================================<br><br>
Starting gobuster in DNS enumeration mode<br>
---------------------------------------------------------------<br>
<span style="color:#00f0ff;">Found: 1.google.com</span><br>
<span style="color:#00f0ff;">Found: aa.google.com</span><br>
<span style="color:#00f0ff;">Found: about.google.com</span><br>
<span style="color:#00f0ff;">Found: About.google.com</span>
</div>
</div>

#### ตารางสรุปรูปแบบการใช้งานคำสั่ง Gobuster (Gobuster Command Cheat Sheet)

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
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;vertical-align:middle;">1. สแกนหาโฟลเดอร์ปกติ (Directory Scan)</td>
<td style="padding:12px 16px;vertical-align:middle;">
<code style="color:#00f0ff;background:rgba(0,240,255,0.05);padding:4px 8px;border-radius:4px;border:1px solid rgba(0,240,255,0.1);font-family:monospace;display:block;font-size:0.78rem;">gobuster dir -u https://target.com -w /usr/share/wordlists/dirb/common.txt</code>
<span style="font-size:0.75rem;color:#94a3b8;display:block;margin-top:4px;">สแกนหาพาธโฟลเดอร์ปกติภายใต้โดเมนด้วยฐานคำศัพท์ทั่วไป</span>
</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;vertical-align:middle;">2. สแกนค้นหาไฟล์ชนิดเฉพาะนามสกุล (Find Hidden Files)</td>
<td style="padding:12px 16px;vertical-align:middle;">
<code style="color:#00f0ff;background:rgba(0,240,255,0.05);padding:4px 8px;border-radius:4px;border:1px solid rgba(0,240,255,0.1);font-family:monospace;display:block;font-size:0.78rem;">gobuster dir -u https://target.com -w /usr/share/wordlists/dirb/common.txt -x php</code>
<span style="font-size:0.75rem;color:#94a3b8;display:block;margin-top:4px;">ใช้พารามิเตอร์ <code style="color:#ff007f;">-x</code> เพื่อสั่งเจาะจงค้นหาไฟล์หน้าบ้านที่มีนามสกุลแบบ <code style="color:#ff007f;">.php</code></span>
</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;vertical-align:middle;">3. ค้นหารายการซับโดเมนของเซิร์ฟเวอร์ (DNS Subdomains Scan)</td>
<td style="padding:12px 16px;vertical-align:middle;">
<code style="color:#00f0ff;background:rgba(0,240,255,0.05);padding:4px 8px;border-radius:4px;border:1px solid rgba(0,240,255,0.1);font-family:monospace;display:block;font-size:0.78rem;">gobuster dns -d google.com -w ~/wordlists/subdomains.txt -i</code>
<span style="font-size:0.75rem;color:#94a3b8;display:block;margin-top:4px;">สแกนหาซับโดเมนย่อยด้วยโมดูล <code style="color:#fbbf24;">dns</code> และดักสืบค่าที่อยู่ไอพีแอดเดรสของซับโดเมน (<code style="color:#ff007f;">-i</code>)</span>
</td>
</tr>
</tbody>
</table>
</div>"""

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        try:
            blocks = json.loads(l.content)
            val = blocks[0]["value"]
            
            # Find the end of DirBuster section in Block 0 to append FFUF & Gobuster right there
            target_marker = "จากนั้นกดปุ่ม **Start** เพื่อเริ่มทำงาน"
            idx = val.find(target_marker)
            if idx != -1:
                end_idx = idx + len(target_marker)
                # Overwrite/append FFUF and Gobuster contents cleanly
                new_val = val[:end_idx] + ffuf_gobuster_html
                blocks[0]["value"] = new_val
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print("Successfully appended FFUF and Gobuster premium guides to Lesson 177 Block 0!")
            else:
                # If target_marker is not found, let's append to the end of Block 0
                new_val = val + ffuf_gobuster_html
                blocks[0]["value"] = new_val
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print("Appended FFUF and Gobuster to the end of Lesson 177 Block 0 successfully!")
        except Exception as e:
            print(f"Error: {e}")
