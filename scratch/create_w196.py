import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

# ─── 1. Clean up Lesson 168 (Remove comparison blocks: index 18, 19, 20) ───
l168 = db.session.query(TutorialLesson).filter_by(id=168).first()
b168 = json.loads(l168.content)

# We remove indices 18, 19, and 20 (separator, comparison table, separator)
# Let us reconstruct new_b168 cleanly by excluding the comparison blocks
new_b168 = []
for idx, b in enumerate(b168):
    if idx in [18, 19, 20]:
        continue
    new_b168.append(b)

l168.content = json.dumps(new_b168, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=168).update({"content": l168.content})
db.session.commit()
print("Removed comparison blocks from Lesson 168 successfully.")

# ─── 2. Re-create or create Lesson 196 (07. Difference Between Linux & Windows) ───
existing = db.session.query(TutorialLesson).filter_by(id=196).first()
if existing:
    db.session.delete(existing)
    db.session.commit()
    print("Deleted old Lesson 196 to recreate cleanly.")

blocks_196 = []

# Block 0: Title Header
blocks_196.append({
    "type": "markdown",
    "value": "## ⚖️ การเปรียบเทียบความแตกต่างระหว่าง Linux และ Windows (Difference Between Linux & Windows)"
})

# Block 1: Intro Overview
blocks_196.append({
    "type": "markdown",
    "value": """### 📌 Overview of System Differences

การเข้าใจความแตกต่างเชิงสถาปัตยกรรม การบริหารจัดการสิทธิ์ และกลไกความปลอดภัยระหว่างระบบปฏิบัติการ **Linux** และ **Windows** เป็นทักษะพื้นฐานที่สำคัญยิ่งสำหรับนักวิเคราะห์ความปลอดภัยทางไซเบอร์ เพื่อช่วยในการวิเคราะห์พฤติกรรมมัลแวร์ การจัดการสิทธิ์เข้าถึง และการตรวจจับภัยคุกคามในระบบสารสนเทศ:

<style>
.w-intro-box{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:20px;margin:1.5rem auto;max-width:1050px;box-shadow:0 4px 20px rgba(0,0,0,0.2);}
.w-intro-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;}
@media(max-width:768px){.w-intro-grid{grid-template-columns:1fr;}}
.w-intro-card{background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:14px;box-sizing:border-box;}
.w-intro-title{font-size:0.88rem;font-weight:700;color:#00f0ff;margin-bottom:6px;display:flex;align-items:center;gap:8px;}
.w-intro-desc{font-size:0.8rem;color:#94a3b8;line-height:1.6;margin:0;}
</style>

<div class="w-intro-box">
<div class="w-intro-grid">
<div class="w-intro-card">
<div class="w-intro-title">🛡️ Security Philosophy</div>
<p class="w-intro-desc">เปรียบเทียบสิทธิ์และปรัชญาความมั่นคงปลอดภัยในการออกแบบของทั้งสองระบบปฏิบัติการ</p>
</div>
<div class="w-intro-card">
<div class="w-intro-title">⚙️ Core Architecture</div>
<p class="w-intro-desc">ทำความเข้าใจความต่างของระบบเคอร์เนล โครงสร้างไฟล์ และตำแหน่งการจัดเก็บไดเรกทอรีหลัก</p>
</div>
<div class="w-intro-card">
<div class="w-intro-title">🛠️ Cybersecurity Tools</div>
<p class="w-intro-desc">วิเคราะห์ความเหมาะสมและการรันเครื่องมือสำหรับงานเจาะระบบความปลอดภัยบนแต่ละแพลตฟอร์ม</p>
</div>
</div>
</div>"""
})

blocks_196.append({"type": "markdown", "value": "---"})

# Block 3: Master Comparison Table
blocks_196.append({
    "type": "markdown",
    "value": """### ⚖️ Linux vs Windows: Master Comparison Dashboard

ตารางเปรียบเทียบสถาปัตยกรรม ความปลอดภัย และลักษณะโครงสร้างข้อแตกต่างระหว่างระบบปฏิบัติการ Linux และ Windows:

<style>
.w-comp-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.w-comp-card{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;overflow:hidden;box-shadow:0 8px 32px rgba(0,0,0,0.45);}
.w-comp-tbl{width:100%;border-collapse:collapse;font-size:0.86rem;}
.w-comp-tbl th{padding:14px 18px;text-align:left;font-size:0.8rem;text-transform:uppercase;letter-spacing:0.08em;font-weight:700;border-bottom:1px solid rgba(255,255,255,0.08);}
.w-comp-tbl th.col-feature{color:#8a94a6;background:rgba(255,255,255,0.015);width:180px;}
.w-comp-tbl th.col-linux{color:#00f0ff;background:rgba(0,240,255,0.02);width:430px;}
.w-comp-tbl th.col-windows{color:#ff007f;background:rgba(255,0,127,0.02);width:430px;}
.w-comp-tbl td{padding:12px 18px;border-bottom:1px solid rgba(255,255,255,0.04);vertical-align:top;line-height:1.65;}
.w-comp-tbl tr:last-child td{border-bottom:none;}
.w-comp-tbl tr.sec-hdr td{background:rgba(255,255,255,0.015);font-weight:800;font-size:0.82rem;color:#e2e8f0;border-bottom:1px solid rgba(255,255,255,0.06);padding:8px 18px;}
.w-comp-tbl tr:hover td{background:rgba(255,255,255,0.01);}
.w-comp-tbl td.feat-name{color:#8a94a6;font-weight:700;}
.w-comp-tbl td.linux-val{color:#cbd5e1;}
.w-comp-tbl td.win-val{color:#cbd5e1;}
.w-comp-tbl td strong{color:#fbbf24;}
</style>

<div class="w-comp-wrap">
<div class="w-comp-card">
<table class="w-comp-tbl">
<thead>
<tr>
<th class="col-feature">Dimension / Feature</th>
<th class="col-linux">🐧 Linux Operating System</th>
<th class="col-windows">🪟 Windows Operating System</th>
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
})

blocks_196.append({"type": "markdown", "value": "---"})

# Block 5: FAQ / Q&A Accordion of Lesson 196
blocks_196.append({
    "type": "markdown",
    "value": """### ❓ Questions & Answers (Q&A)

ไขข้อสงสัยประเด็นสำคัญเกี่ยวกับความแตกต่างระหว่างระบบปฏิบัติการ Linux และ Windows:

<style>
.qa-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:12px;}
.qa-item{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:10px;overflow:hidden;transition:all 0.25s ease;}
.qa-item:hover{border-color:rgba(0,240,255,0.25);background:rgba(0,240,255,0.01);box-shadow:0 4px 15px rgba(0,0,0,0.3);}
.qa-q{padding:16px 20px;font-size:0.92rem;font-weight:700;color:#e2e8f0;cursor:pointer;display:flex;justify-content:between;align-items:center;user-select:none;}
.qa-q::after{content:"▼";font-size:0.65rem;color:#64748b;margin-left:auto;transition:transform 0.2s ease;}
.qa-item.active .qa-q::after{transform:rotate(180deg);color:#00f0ff;}
.qa-a{max-height:0;overflow:hidden;padding:0 20px;font-size:0.86rem;color:#94a3b8;line-height:1.7;transition:all 0.25s ease-out;background:rgba(0,0,0,0.15);}
.qa-item.active .qa-a{max-height:300px;padding:16px 20px;border-top:1px solid rgba(255,255,255,0.03);}
.qa-item.active .qa-q{color:#00f0ff;}
</style>

<div class="qa-wrap">

<div class="qa-item active">
<div class="qa-q" onclick="toggleQA(this)">1. ทำไมระบบ Case-Sensitivity ของชื่อไฟล์ใน Linux ถึงช่วยส่งเสริมความปลอดภัยมากกว่า Windows?</div>
<div class="qa-a">
การแยกความต่างระหว่างพิมพ์ใหญ่/พิมพ์เล็ก (เช่น <code>passwd</code> และ <code>PASSWD</code>) ใน Linux ช่วยป้องกันสับสนของระบบไฟล์แบบเข้มงวด ในขณะที่ระบบที่ไม่สนใจตัวพิมพ์ใหญ่เล็กของ Windows (Case-insensitive) ทำให้บางครั้งมัลแวร์สามารถเข้ามารันเขียนทับไฟล์คอนฟิกเดิมที่ผู้ใช้อาจเขียนผิดตัวพิมพ์ใหญ่เล็กได้โดยง่าย
</div>
</div>

<div class="qa-item">
<div class="qa-q" onclick="toggleQA(this)">2. ในมุมมองความมั่นคงปลอดภัย เหตุใด Monolithic Kernel ของ Linux ถึงแก้ช่องโหว่ได้เร็วกว่า Microkernel/Hybrid Kernel ของ Windows?</div>
<div class="qa-a">
เนื่องจาก Linux เป็น Open-source ทำให้นักพัฒนาทั่วโลกรวมถึงชุมชนความปลอดภัยขนาดใหญ่สามารถเข้ามาสแกนโค้ดและออกแพตช์แก้ไขช่องโหว่ความมั่นคงปลอดภัยในตัวเคอร์เนลหลักได้ทันที ขณะที่ Windows อาศัยเพียงทีมนักพัฒนาหลักของ Microsoft เท่านั้นในการปล่อยอัปเดตระบบความปลอดภัย
</div>
</div>

<div class="qa-item">
<div class="qa-q" onclick="toggleQA(this)">3. การจัดการที่เก็บอุปกรณ์ภายนอก (Peripherals) แบบ "Everything is a file" ใน Linux มีข้อดีเหนือกว่า Windows อย่างไร?</div>
<div class="qa-a">
การมองอุปกรณ์ทุกชนิด (เช่น ฮาร์ดดิสก์ เครื่องพิมพ์ พอร์ตเชื่อมต่อ) เป็นไฟล์ปกติในไดเรกทอรี <code>/dev</code> ทำให้การเขียนโปรแกรมควบคุม การสแกนข้อมูล และการบังคับใช้นโยบายความมั่นคงปลอดภัยสามารถทำได้ผ่านคำสั่งจัดการไฟล์มาตรฐาน (เช่น <code>chmod</code>, <code>chown</code>) ได้ทันที โดยไม่ต้องใช้ API เฉพาะทางที่ซับซ้อนเหมือนฝั่ง Windows
</div>
</div>

</div>

<script>
function toggleQA(element) {
    const item = element.parentElement;
    item.classList.toggle("active");
}
</script>"""
})

# ─── Write Lesson 196 to Database ───
new_lesson = TutorialLesson(
    id=196,
    module_id=33,
    title="07. การเปรียบเทียบความแตกต่างระหว่าง Linux และ Windows (Difference Between Linux & Windows)",
    content=json.dumps(blocks_196, ensure_ascii=False),
    position=7,
    challenge_id=None
)

db.session.add(new_lesson)
db.session.commit()
print("New Lesson 196 (07. Difference Between Linux & Windows) created and committed to the database!")
