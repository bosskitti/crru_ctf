import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l196 = db.session.query(TutorialLesson).filter_by(id=196).first()
blocks = json.loads(l196.content)

# ─── Replace Block 3 with Colorful Master Comparison Table (Cyan vs Pink themes) ───
blocks[3]['value'] = """### ⚖️ Linux vs Windows: Master Comparison Dashboard

ตารางเปรียบเทียบสถาปัตยกรรม ความปลอดภัย และลักษณะโครงสร้างข้อแตกต่างระหว่างระบบปฏิบัติการ Linux และ Windows:

<style>
.w-comp-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.w-comp-card{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;overflow:hidden;box-shadow:0 8px 32px rgba(0,0,0,0.45);}
.w-comp-tbl{width:100%;border-collapse:collapse;font-size:0.86rem;}
.w-comp-tbl th{padding:14px 18px;text-align:left;font-size:0.8rem;text-transform:uppercase;letter-spacing:0.08em;font-weight:700;border-bottom:1px solid rgba(255,255,255,0.08);}
.w-comp-tbl th.col-feature{color:#8a94a6;background:rgba(255,255,255,0.015);width:180px;}

/* Colorful Header Backgrounds */
.w-comp-tbl th.col-linux{color:#00f0ff;background:rgba(0,240,255,0.04);width:430px;text-shadow:0 0 8px rgba(0,240,255,0.3);}
.w-comp-tbl th.col-windows{color:#ff007f;background:rgba(255,0,127,0.04);width:430px;text-shadow:0 0 8px rgba(255,0,127,0.3);}

.w-comp-tbl td{padding:12px 18px;border-bottom:1px solid rgba(255,255,255,0.04);vertical-align:top;line-height:1.65;}
.w-comp-tbl tr:last-child td{border-bottom:none;}
.w-comp-tbl tr.sec-hdr td{background:rgba(255,255,255,0.015);font-weight:800;font-size:0.82rem;color:#e2e8f0;border-bottom:1px solid rgba(255,255,255,0.06);padding:8px 18px;}
.w-comp-tbl tr:hover td{background:rgba(255,255,255,0.01);}
.w-comp-tbl td.feat-name{color:#8a94a6;font-weight:700;}

/* Distinct Colors for each column */
.w-comp-tbl td.linux-val{color:#cbd5e1;background:rgba(0,240,255,0.005);}
.w-comp-tbl td.win-val{color:#cbd5e1;background:rgba(255,0,127,0.005);}

/* Highlight Colors: Cyan for Linux, Pink for Windows */
.w-comp-tbl td.linux-val strong{color:#00f0ff;text-shadow:0 0 4px rgba(0,240,255,0.15);}
.w-comp-tbl td.win-val strong{color:#ff007f;text-shadow:0 0 4px rgba(255,0,127,0.15);}
.w-comp-tbl td.linux-val code{color:#00f0ff;background:rgba(0,240,255,0.06);border:1px solid rgba(0,240,255,0.12);padding:1px 4px;border-radius:3px;}
.w-comp-tbl td.win-val code{color:#ff007f;background:rgba(255,0,127,0.06);border:1px solid rgba(255,0,127,0.12);padding:1px 4px;border-radius:3px;}
</style>

<div class="w-comp-wrap">
<div class="w-comp-card">
<table class="w-comp-tbl">
<thead>
<tr>
<th class="col-feature">Dimension / Feature</th>
<th class="col-linux">🐧 LINUX OPERATING SYSTEM</th>
<th class="col-windows">🪟 WINDOWS OPERATING SYSTEM</th>
</tr>
</thead>
<tbody>

<!-- Section 1: General -->
<tr class="sec-hdr">
<td colspan="3">📊 General Characteristics (ลักษณะทั่วไป)</td>
</tr>
<tr>
<td class="feat-name">Source Model</td>
<td class="linux-val">เป็นแบบ <strong>Open-source</strong> (เปิดเผยโค้ดให้สาธารณะนำไปพัฒนาต่อยอดฟรี)</td>
<td class="win-val">เป็นแบบ <strong>Closed-source</strong> (ลิขสิทธิ์ทางการค้า ควบคุมซอร์สโค้ดโดย Microsoft)</td>
</tr>
<tr>
<td class="feat-name">Efficiency</td>
<td class="linux-val">มีประสิทธิภาพสูงกว่า จัดสรรและกินทรัพยากรเครื่องน้อยมาก</td>
<td class="win-val">มีประสิทธิภาพน้อยกว่า กินหน่วยความจำและซีพียูค่อนข้างสูง</td>
</tr>
<tr>
<td class="feat-name">Performance</td>
<td class="linux-val">ทำงานได้รวดเร็ว ลื่นไหล แม้รันกับฮาร์ดแวร์ตระกูลเก่า</td>
<td class="win-val">ทำงานช้ากว่าบนฮาร์ดแวร์เดียวกัน และช้าลงเมื่อฮาร์ดแวร์เก่า</td>
</tr>
<tr>
<td class="feat-name">System Cost</td>
<td class="linux-val">สามารถใช้งานได้ <strong>ฟรี</strong> ไม่มีค่าลิขสิทธิ์ (Free OS)</td>
<td class="win-val">มีค่าใช้จ่ายลิขสิทธิ์ไลเซนส์ (Commercial OS)</td>
</tr>

<!-- Section 2: System Architecture -->
<tr class="sec-hdr">
<td colspan="3">⚙️ System Architecture & File System (สถาปัตยกรรมและระบบไฟล์)</td>
</tr>
<tr>
<td class="feat-name">Kernel Architecture</td>
<td class="linux-val">สถาปัตยกรรมแบบ <strong>Monolithic Kernel</strong> (รวมแกนหลักในพื้นที่เดียว)</td>
<td class="win-val">สถาปัตยกรรมแบบ <strong>Microkernel / Hybrid Kernel</strong> (แยกเซอร์วิสย่อย)</td>
</tr>
<tr>
<td class="feat-name">File System Structure</td>
<td class="linux-val">ใช้ระบบไฟล์โครงสร้างต้นไม้เดี่ยว (Single Tree Structure: <code>/</code>)</td>
<td class="win-val">ใช้ระบบไฟล์แบบ <strong>หลายพาร์ติชัน (Multi-Partition)</strong> แยกตามตัวอักษรไดรฟ์ (เช่น <code>C:\\\\</code>, <code>D:\\\\</code>, <code>E:\\\\</code>)</td>
</tr>
<tr>
<td class="feat-name">File Locations</td>
<td class="linux-val">ไฟล์ระบบย่อยและโปรแกรมติดตั้งจะกระจายตัวอยู่ตามไดเรกทอรีต่างกัน (เช่น <code>/bin</code>, <code>/etc</code>, <code>/usr</code>)</td>
<td class="win-val">ไฟล์ระบบหลักและไฟล์โปรแกรมถูกเก็บรวมไว้ที่ไดรฟ์ระบบหลัก (ปกติรวบรวมอยู่ที่ไดรฟ์ <code>C:\\\\</code>)</td>
</tr>
<tr>
<td class="feat-name">Terminology</td>
<td class="linux-val">เรียกที่เก็บกลุ่มไฟล์ข้อมูลว่า <strong>"Directory"</strong></td>
<td class="win-val">เรียกที่เก็บกลุ่มไฟล์ข้อมูลว่า <strong>"Folder"</strong></td>
</tr>
<tr>
<td class="feat-name">Peripherals / Devices</td>
<td class="linux-val">มองอุปกรณ์เชื่อมต่อภายนอกเป็น <strong>ไฟล์ปกติ</strong> (Everything is a file)</td>
<td class="win-val">มองอุปกรณ์เชื่อมต่อภายนอกเป็น <strong>อุปกรณ์เชิงกายภาพ (Devices)</strong></td>
</tr>
<tr>
<td class="feat-name">Case Sensitivity</td>
<td class="linux-val">ชื่อไฟล์มีความอ่อนไหวต่ออักษรพิมพ์ใหญ่/เล็ก (<strong>Case-Sensitive</strong>)<br>เช่น <code>data.txt</code> และ <code>Data.txt</code> ถือเป็นคนละไฟล์กัน</td>
<td class="win-val">ชื่อไฟล์ไม่สนใจพิมพ์เล็กพิมพ์ใหญ่ (<strong>Case-Insensitive</strong>)<br>เช่น <code>data.txt</code> และ <code>DATA.TXT</code> ถือเป็นไฟล์เดียวกัน</td>
</tr>
<tr>
<td class="feat-name">Path Separator</td>
<td class="linux-val">ใช้เครื่องหมาย Forward Slash (<code>/</code>) ในการคั่นโฟลเดอร์</td>
<td class="win-val">ใช้เครื่องหมาย Backslash (<code>\\\\</code>) ในการคั่นโฟลเดอร์</td>
</tr>
<tr>
<td class="feat-name">Home Directory</td>
<td class="linux-val">โฟลเดอร์โฮมตั้งต้นอยู่ที่ <code>/home/username</code></td>
<td class="win-val">โฟลเดอร์โฮมตั้งต้นอยู่ที่ <code>\\\\Users\\\\Username</code> (หรืออ้างอิงเป็น My Documents)</td>
</tr>

<!-- Section 3: Accounts -->
<tr class="sec-hdr">
<td colspan="3">👥 User Accounts & Privileges (บัญชีผู้ใช้และระดับสิทธิ์)</td>
</tr>
<tr>
<td class="feat-name">User Account Types</td>
<td class="linux-val">แบ่งหลักๆ เป็น <strong>3 ประเภท</strong> (root, regular, service accounts)</td>
<td class="win-val">แบ่งย่อยเป็น <strong>5 ประเภท</strong> (administrator, standard, work/school, child, guest)</td>
</tr>
<tr>
<td class="feat-name">Superuser Identity</td>
<td class="linux-val">ผู้มีอำนาจสิทธิ์ระบบสูงสุดเรียกว่า <strong>root</strong></td>
<td class="win-val">ผู้มีอำนาจสิทธิ์ระบบสูงสุดเรียกว่า <strong>administrator</strong></td>
</tr>

<!-- Section 4: Security -->
<tr class="sec-hdr">
<td colspan="3">🛡️ Cybersecurity & Robustness (ความปลอดภัยและความคุ้มกันระบบ)</td>
</tr>
<tr>
<td class="feat-name">Security Robustness</td>
<td class="linux-val">มีความมั่นคงปลอดภัยตามโครงสร้างสิทธิ์ที่เข้มงวด มัลแวร์โจมตีได้ยากกว่า</td>
<td class="win-val">มีความเสี่ยงความมั่นคงปลอดภัยสูงกว่า ตกเป็นเป้าหมายหลักของการโจมตีด้วยไวรัสและมัลแวร์</td>
</tr>
<tr>
<td class="feat-name">Vulnerability Fix</td>
<td class="linux-val">ช่องโหว่และข้อผิดพลาดได้รับการตรวจสอบและแก้ไขได้รวดเร็วผ่านนักพัฒนาทั่วโลก</td>
<td class="win-val">การอุดช่องโหว่และปล่อยแพตช์ความปลอดภัยดำเนินงานผ่านทีมนักพัฒนาของ Microsoft เท่านั้น</td>
</tr>
<tr>
<td class="feat-name">Cybersecurity Uses</td>
<td class="linux-val">เป็นระบบปฏิบัติการหลักสำหรับการทำงานด้านการเจาะระบบ (Hacking / Penetration Testing)</td>
<td class="win-val">ไม่มีความเหมาะสมหรือยืดหยุ่นเพียงพอสำหรับการทำกิจกรรมเจาะระบบความปลอดภัย</td>
</tr>
<tr>
<td class="feat-name">Security Tools</td>
<td class="linux-val">มีเครื่องมือความปลอดภัยไซเบอร์รันแบบ Native จำนวนมาก (เช่น Kali Linux)</td>
<td class="win-val">มีเครื่องมือความปลอดภัยไซเบอร์แบบ Native ในปริมาณที่น้อยกว่าฝั่ง Linux</td>
</tr>

</tbody>
</table>
</div>
</div>"""

l196.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=196).update({"content": l196.content})
db.session.commit()
print("Linux vs Windows Master Comparison Table color themes (Cyan vs Pink) updated successfully!")
