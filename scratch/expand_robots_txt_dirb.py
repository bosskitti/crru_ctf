import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

expanded_robots_dirb_html = """### 🤖 ไฟล์ Robots.txt กับความมั่นคงปลอดภัย (Path and Directory Traversal: Robots.txt)

ไฟล์ **robots.txt** เป็นไฟล์มาตรฐานสำหรับจัดเก็บบันทึกบนเว็บเซิร์ฟเวอร์ที่ระบุข้อมูลแนะนำตัวสแกนเก็บข้อมูล (Search Engine Crawlers เช่น Googlebot) ว่าไดเรกทอรีหรือหน้าเพจใดของเว็บไซต์ที่ไม่ควรนำไปทำดัชนีผลการค้นหา (Index) ในสาธารณะ

**ข้อควรระวังสำคัญสำหรับความปลอดภัย**:
นักพัฒนาและผู้ดูแลระบบเว็บไซต์จำนวนมากมักเข้าใจผิด โดยการนำไดเรกทอรีหรือโฟลเดอร์เก็บข้อมูลส่วนตัวมาพิมพ์ระบุไว้ใน robots.txt เพื่อป้องกันไม่ให้คนอื่นสืบค้นเจอ ซึ่งการทำเช่นนี้จะเท่ากับเป็นการ **"ชี้เป้า" (Directory exposure)** ให้ผู้โจมตีทราบทันทีว่าควรเดินทางไปเจาะระบบหรือแอบดูไฟล์ในพาธลับพิกัดใดของเว็บไซต์!

<div style="background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:16px;margin:15px auto;font-family:monospace;font-size:0.82rem;color:#a855f7;text-align:left;max-width:420px;box-shadow:0 4px 15px rgba(0,0,0,0.35);">
<span style="color:#64748b;"># ตัวอย่างไฟล์ robots.txt ที่มักชี้เป้าความลับให้แฮกเกอร์</span><br>
User-agent: *<br>
Disallow: /admin/<br>
Disallow: /backup/<br>
Disallow: /private/<br>
Disallow: /database/<br>
Disallow: /login/<br>
Disallow: /api/<br>
Disallow: /config.php<br>
Disallow: /old-site-backup/
</div>

---

### 🛠️ เครื่องมืออัตโนมัติสำหรับการสแกนพาธ (Automated Scanning Tools)

ในการทดสอบหาช่องโหว่ประเภท Directory Traversal หรือค้นหาโฟลเดอร์ที่ซ่อนอยู่ (Hidden directories) นักทดสอบระบบนิยมเลือกใช้เครื่องมือทำงานอัตโนมัติ (Automated Tools) ดังนี้:
- **Dirb / Dirbuster**: เครื่องมือประเภท Directory brute-forcing เพื่อค้นหาไฟล์และโฟลเดอร์ที่ซ่อนอยู่
- **FFUF / Gobuster**: เครื่องมือยอดนิยมประสิทธิภาพสูงในการทำ Directory & File enumeration (ค้นหารวดเร็วและรองรับการปรับแต่งค่าระดับสูง)
- **Burp Suite Intruder**: ระบบยิงส่ง Payload แบบกึ่งอัตโนมัติสำหรับการทำ Traversal fuzzing หรือป้อนรหัสข้ามไดเรกทอรี

---

### 📂 การใช้งานเครื่องมือ DIRB (Directory Buster)

**DIRB** คือเครื่องมือในกลุ่ม Command-line เพื่อทำการ Brute-force ค้นหารายการพาธและไฟล์ข้อมูลบนเซิร์ฟเวอร์ โดยจะทดสอบเรียกข้อมูลผ่านรายการคำ (Wordlist) และประมวลผลหา URL ที่มีอยู่จริง (ไม่ว่าหน้าเว็บจะตั้งค่าสกัดกั้น หรือเขียนโปรแกรมป้องกันการส่งรหัส 404 บกพร่องก็ตาม)

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
</div>"""

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        try:
            blocks = json.loads(l.content)
            val = blocks[0]["value"]
            
            # Find where "### 🤖 ไฟล์ Robots.txt กับความมั่นคงปลอดภัย" starts
            target_start = val.find("### 🤖 ไฟล์ Robots.txt กับความมั่นคงปลอดภัย")
            
            if target_start != -1:
                # Replace cleanly from that header to the end of Block 0
                new_val = val[:target_start] + expanded_robots_dirb_html
                blocks[0]["value"] = new_val
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print("Successfully expanded Robots.txt, Tools, and DIRB commands table cleanly!")
            else:
                print("Error: Could not find target Robots.txt header in Lesson 177 Block 0.")
        except Exception as e:
            print(f"Error: {e}")
