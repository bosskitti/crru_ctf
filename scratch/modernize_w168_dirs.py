import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l168 = db.session.query(TutorialLesson).filter_by(id=168).first()
blocks = json.loads(l168.content)

# ─── 1. Block 11: Windows Drive Letters & Components ───
blocks[11]['value'] = """### 💽 Windows Drive Letters & Components

ในระบบปฏิบัติการ Windows สื่อบันทึกข้อมูลหลักจะถูกแทนที่ด้วย **อักษรประจำไดรฟ์ (Drive Letters)** จาก A ถึง Z เพื่อชี้ตำแหน่งของพาร์ติชันทางกายภาพ:

<style>
.w-drive-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.w-drive-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;}
@media(max-width:768px){.w-drive-grid{grid-template-columns:repeat(2,1fr);}}
@media(max-width:480px){.w-drive-grid{grid-template-columns:1fr;}}
.w-drive-card{background:rgba(15,17,26,0.5);border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:16px;transition:all 0.2s ease;}
.w-drive-card:hover{border-color:rgba(0,240,255,0.2);transform:translateY(-2px);box-shadow:0 6px 20px rgba(0,0,0,0.3);}
.w-drive-hdr{display:flex;align-items:center;gap:10px;margin-bottom:8px;}
.w-drive-badge{font-family:'JetBrains Mono',monospace;font-size:1.1rem;font-weight:800;color:#00f0ff;text-shadow:0 0 8px rgba(0,240,255,0.4);}
.w-drive-icon{font-size:1.2rem;}
.w-drive-name{font-size:0.75rem;text-transform:uppercase;color:#8a94a6;font-weight:700;letter-spacing:0.04em;}
.w-drive-desc{font-size:0.83rem;color:#94a3b8;line-height:1.55;}
.w-comp-box{margin-top:20px;padding:16px;border-radius:10px;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);display:flex;gap:20px;}
@media(max-width:700px){.w-comp-box{flex-direction:column;gap:12px;}}
.w-comp-col{flex:1;display:flex;flex-direction:column;gap:4px;}
.w-comp-title{font-size:0.85rem;font-weight:700;color:#fbbf24;}
.w-comp-desc{font-size:0.8rem;color:#94a3b8;line-height:1.5;margin:0;}
</style>

<div class="w-drive-wrap">
<div class="w-drive-grid">
<!-- Drive A -->
<div class="w-drive-card">
<div class="w-drive-hdr">
<span class="w-drive-icon">💾</span>
<span class="w-drive-badge">Drive A:</span>
</div>
<div class="w-drive-name">Floppy Drive (3.5")</div>
<p class="wsa-mode-desc" style="font-size:0.8rem;color:#94a3b8;margin-top:4px;line-height:1.5;">ใช้แทนไดรฟ์แผ่นดิสก์เก็ตขนาด 3.5 นิ้ว (ปัจจุบันเลิกใช้ทั่วไปแล้ว)</p>
</div>
<!-- Drive B -->
<div class="w-drive-card">
<div class="w-drive-hdr">
<span class="w-drive-icon">💾</span>
<span class="w-drive-badge">Drive B:</span>
</div>
<div class="w-drive-name">Floppy Drive (5.25")</div>
<p class="wsa-mode-desc" style="font-size:0.8rem;color:#94a3b8;margin-top:4px;line-height:1.5;">ใช้แทนไดรฟ์แผ่นดิสก์เก็ตขนาด 5.25 นิ้ว (เทคโนโลยีโบราณยุค 80s)</p>
</div>
<!-- Drive C -->
<div class="w-drive-card" style="border-color:rgba(0,240,255,0.15);">
<div class="w-drive-hdr">
<span class="w-drive-icon">💽</span>
<span class="w-drive-badge" style="color:#00f0ff;">Drive C:</span>
</div>
<div class="w-drive-name" style="color:#ffffff;">Primary Boot Drive</div>
<p class="wsa-mode-desc" style="font-size:0.8rem;color:#cbd5e1;margin-top:4px;line-height:1.5;">พาร์ติชันหลักของฮาร์ดดิสก์ (HDD/SSD) ที่ใช้บูตและเก็บไฟล์ระบบ Windows</p>
</div>
<!-- Drive D -->
<div class="w-drive-card">
<div class="w-drive-hdr">
<span class="w-drive-icon">💿</span>
<span class="w-drive-badge">Drive D:</span>
</div>
<div class="w-drive-name">Secondary Partition</div>
<p class="wsa-mode-desc" style="font-size:0.8rem;color:#94a3b8;margin-top:4px;line-height:1.5;">มักใช้เป็นพาร์ติชันเก็บข้อมูลสำรอง หรือเครื่องอ่าน CD-ROM/DVD-ROM</p>
</div>
<!-- Drive E-Z -->
<div class="w-drive-card">
<div class="w-drive-hdr">
<span class="w-drive-icon">🔌</span>
<span class="w-drive-badge">Drive E:-Z:</span>
</div>
<div class="w-drive-name">Removable Storage</div>
<p class="wsa-mode-desc" style="font-size:0.8rem;color:#94a3b8;margin-top:4px;line-height:1.5;">ไดรฟ์เสริมสำหรับเก็บอุปกรณ์เชื่อมต่อถอดเสียบ เช่น Flash Drive หรือ External SSD</p>
</div>
</div>

<!-- Core Components of Windows File System -->
<div class="w-comp-box">
<div class="w-comp-col">
<div class="w-comp-title">📁 Drive / Volume (พาร์ติชัน)</div>
<p class="w-comp-desc">คือกลุ่มของไฟล์และโฟลเดอร์ทั้งหมดที่อยู่ภายในหน่วยเก็บข้อมูลนั้นๆ (เช่น ไดรฟ์ C:\ หรือ D:\)</p>
</div>
<div class="w-comp-col">
<div class="w-comp-title">🗂️ Directory / Folder (โฟลเดอร์)</div>
<p class="w-comp-desc">โครงสร้างลำดับชั้นสำหรับจัดกลุ่มและรวบรวมไฟล์ข้อมูลหรือโฟลเดอร์ย่อย เพื่อความสะดวกในการจัดเก็บ</p>
</div>
<div class="w-comp-col">
<div class="w-comp-title">📄 File (ไฟล์ข้อมูล)</div>
<p class="w-comp-desc">กลุ่มของข้อมูลดิจิทัลที่เกี่ยวข้องกันในเชิงตรรกะ จัดเก็บลงในไดรฟ์ปลายทางภายใต้ชื่อและนามสกุลไฟล์เฉพาะ</p>
</div>
</div>
</div>"""


# ─── 2. Block 13: Windows Directory Structure Basics ───
blocks[13]['value'] = """### 📂 Windows Directory Structure & Path Basics

ลักษณะที่อยู่โฟลเดอร์ สัญลักษณ์แบ่งประเภท และสัญญลักษณ์พิเศษในการอ้างอิงตำแหน่งโฟลเดอร์ใน Windows:

<style>
.w-dir-basics-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;gap:20px;}
@media(max-width:768px){.w-dir-basics-wrap{flex-direction:column;}}
.w-dir-basic-card{flex:1.2;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:22px;box-shadow:0 4px 20px rgba(0,0,0,0.2);display:flex;flex-direction:column;justify-content:center;}
.w-dir-basic-card h4{margin:0 0 12px;font-size:1rem;color:#00f0ff;}
.w-dir-basic-card p{margin:0 0 10px;font-size:0.86rem;color:#94a3b8;line-height:1.7;}
.w-dir-basic-card p:last-child{margin-bottom:0;}
.w-dir-basic-card strong{color:#fbbf24;}
.w-dir-spec-card{flex:1;background:rgba(15,17,26,0.5);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:22px;box-shadow:0 4px 20px rgba(0,0,0,0.2);}
.w-dir-spec-hdr{font-size:0.75rem;color:#8a94a6;margin-bottom:12px;text-transform:uppercase;letter-spacing:0.04em;font-weight:700;}
.w-dir-spec-tbl{width:100%;border-collapse:collapse;}
.w-dir-spec-tbl th{padding:8px 12px;text-align:left;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.06em;color:#8a94a6;border-bottom:1px solid rgba(255,255,255,0.06);}
.w-dir-spec-tbl td{padding:10px 12px;border-bottom:1px solid rgba(255,255,255,0.04);font-size:0.85rem;vertical-align:top;}
.w-dir-spec-tbl tr:last-child td{border-bottom:none;}
.w-dir-spec-tbl td:first-child{font-family:'JetBrains Mono',monospace;font-size:0.95rem;font-weight:800;color:#fbbf24;width:80px;text-align:center;}
.w-dir-spec-tbl td:last-child{color:#94a3b8;line-height:1.6;}
.w-dir-spec-note{font-size:0.75rem;color:#64748b;font-family:'JetBrains Mono',monospace;margin-top:10px;line-height:1.5;}
</style>

<div class="w-dir-basics-wrap">
<div class="w-dir-basic-card">
<h4>📁 Directory & Path Rule</h4>
<p>1. <strong>ไม่มี Formal Root Directory รวมกลาง</strong>: เนื่องจาก Windows จัดการไดรฟ์แยกจากกันอย่างเด็ดขาด ทำให้สัญลักษณ์ Root Directory ของไดรฟ์นั้นขึ้นต้นด้วยอักษรไดรฟ์ เช่น <strong>C:\\</strong> หรือ <strong>D:\\</strong></p>
<p>2. <strong>การแบ่งโฟลเดอร์ย่อย (Separator)</strong>: Windows ใช้สัญลักษณ์ <strong>Backslash (<code>\\</code>)</strong> ในการคั่นตำแหน่งย่อยของโฟลเดอร์ (ต่างจาก Linux ที่ใช้ Forward Slash <code>/</code>)</p>
</div>
<div class="w-dir-spec-card">
<div class="w-dir-spec-hdr">🔗 Special Folders (โฟลเดอร์อ้างอิงพิเศษ)</div>
<table class="w-dir-spec-tbl">
<thead><tr><th>Folder</th><th>Description</th></tr></thead>
<tbody>
<tr><td>.</td><td>ตัวแทนของ <strong>โฟลเดอร์ปัจจุบัน</strong> (Current Folder) ที่กำลังรันงานอยู่</td></tr>
<tr><td>..</td><td>ตัวแทนของ <strong>โฟลเดอร์ลำดับชั้นขึ้นไป 1 ระดับ</strong> (Parent Folder)</td></tr>
</tbody>
</table>
<div class="w-dir-spec-note">
e.g. เมื่อสั่งรัน <code>cd ..</code> ในพรอมต์ระบบ จะเป็นการถอยกลับไปที่โฟลเดอร์หลักชั้นก่อนหน้า 1 ขั้น
</div>
</div>
</div>"""


# ─── 3. Block 15: Windows System Directory Reference (15 Folders Table) ───
blocks[15]['value'] = """### 🛡️ Windows System Directories Reference

รายการโฟลเดอร์ระบบที่ติดตั้งมาแต่กำเนิดของ Windows ในไดรฟ์หลัก (Boot Partition):

<style>
.w-dir-ref-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.w-dir-ref-card{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,0.2);}
.w-dir-ref-tbl{width:100%;border-collapse:collapse;}
.w-dir-ref-tbl th{padding:12px 16px;text-align:left;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.08em;font-weight:700;color:#8a94a6;background:rgba(255,255,255,0.01);border-bottom:1px solid rgba(255,255,255,0.06);}
.w-dir-ref-tbl td{padding:12px 16px;border-bottom:1px solid rgba(255,255,255,0.04);font-size:0.86rem;vertical-align:top;line-height:1.6;}
.w-dir-ref-tbl tr:last-child td{border-bottom:none;}
.w-dir-ref-tbl tr:hover td{background:rgba(255,255,255,0.015);}
.w-dir-ref-tbl td:first-child{font-family:'JetBrains Mono',monospace;font-size:0.88rem;color:#00f0ff;font-weight:700;white-space:nowrap;width:240px;}
.w-dir-ref-tbl td:last-child{color:#94a3b8;}
.w-dir-tag{display:inline-block;padding:1px 5px;border-radius:3px;font-size:0.65rem;font-weight:800;text-transform:uppercase;letter-spacing:0.05em;margin-left:6px;vertical-align:middle;}
.w-dir-tag.hidden{background:rgba(251,191,36,0.08);border:1px solid rgba(251,191,36,0.25);color:#fbbf24;}
.w-dir-tag.sys64{background:rgba(171,32,253,0.08);border:1px solid rgba(171,32,253,0.25);color:#ab20fd;}
.w-dir-tag.sys32{background:rgba(61,220,132,0.08);border:1px solid rgba(61,220,132,0.25);color:#3ddc84;}
</style>

<div class="w-dir-ref-wrap">
<div class="w-dir-ref-card">
<table class="w-dir-ref-tbl">
<thead>
<tr>
<th>Folder Path</th>
<th>Description (คำอธิบายหน้าที่และการทำงาน)</th>
</tr>
</thead>
<tbody>
<tr>
<td>\\PerfLogs</td>
<td>ใช้สำหรับเก็บข้อมูลล็อกแสดงประสิทธิภาพของเครื่อง Windows (Performance Logs) ปกติจะไม่มีไฟล์ข้างใน (โฟลเดอร์เปล่า)</td>
</tr>
<tr>
<td>\\Program&nbsp;Files</td>
<td>โฟลเดอร์สำหรับติดตั้งโปรแกรมทั่วไป<br>
• <strong>ระบบ 32-bit</strong>: จะใช้เก็บไฟล์โปรแกรม 16-bit และ 32-bit ทั้งหมด<br>
• <strong>ระบบ 64-bit</strong>: จะใช้เก็บเฉพาะไฟล์โปรแกรม 64-bit เท่านั้น
</td>
</tr>
<tr>
<td>\\Program&nbsp;Files&nbsp;(x86)</td>
<td><span class="w-dir-tag sys64">64-bit OS Only</span><br>
ปรากฏเฉพาะบนระบบปฏิบัติการแบบ 64-bit เท่านั้น ใช้เก็บไฟล์ติดตั้งโปรแกรมประเภท 32-bit และ 16-bit ย้อนหลังเพื่อเสถียรภาพการทำงาน
</td>
</tr>
<tr>
<td>\\ProgramData</td>
<td><span class="w-dir-tag hidden">Hidden</span><br>
โฟลเดอร์ซ่อนสำหรับเก็บข้อมูลโปรแกรมคอมพิวเตอร์ที่แชร์ใช้ร่วมกันโดยไม่มีข้อจำกัดเรื่องระดับสิทธิ์ (เช่น Windows Defender จะเก็บฐานข้อมูลไวรัสไว้ที่ <code>\\ProgramData\\Microsoft\\Windows Defender</code>)
</td>
</tr>
<tr>
<td>\\Users</td>
<td>โฟลเดอร์โปรไฟล์ผู้ใช้ เก็บโฟลเดอร์ส่วนตัวของทุกบัญชีผู้ใช้งานที่เคยล็อกอินเข้าเครื่องอย่างน้อย 1 ครั้ง (ทำหน้าที่เหมือน <code>/home</code> ใน Linux)
</td>
</tr>
<tr>
<td>\\Users\\Public</td>
<td>โฟลเดอร์กลางสำหรับผู้ใช้งานทุกคนในเครื่อง เพื่อใช้แชร์ไฟล์ข้อมูล รูปภาพ หรือเอกสารส่งหากันอย่างเสรี
</td>
</tr>
<tr>
<td>\\Users\\User\\AppData</td>
<td><span class="w-dir-tag hidden">Hidden</span><br>
โฟลเดอร์ซ่อนสำหรับเก็บข้อมูลและคอนฟิกการตั้งค่าจำเพาะของแอปพลิเคชันรายบุคคล แบ่งย่อยเป็น 3 ส่วนหลัก: <strong>Roaming</strong>, <strong>Local</strong>, และ <strong>LocalLow</strong>
</td>
</tr>
<tr>
<td>\\Users\\User\\</td>
<td>โฟลเดอร์โฮม (Home) ของผู้ใช้แต่ละคน ประกอบด้วยโฟลเดอร์จัดเก็บข้อมูลเริ่มต้น เช่น <code>Desktop</code> (หน้าจอหลัก), <code>Downloads</code>, <code>Documents</code>, <code>Pictures</code>, <code>Music</code>, <code>Videos</code>
</td>
</tr>
<tr>
<td>\\Windows</td>
<td>โฟลเดอร์หลักสำหรับจัดเก็บไฟล์โปรแกรมระบบและไฟล์รันคำสั่งพื้นฐานทั้งหมดของระบบปฏิบัติการ Windows
</td>
</tr>
<tr>
<td>\\Windows\\System<br>\\Windows\\System32<br>\\Windows\\SysWOW64</td>
<td>โฟลเดอร์ที่เก็บรักษาไฟล์ไลบรารีระบบและ API หลักในรูปของ <strong>Dynamic-Link Library (DLL)</strong><br>
• <code>System32</code>: เก็บไฟล์ DLL แบบ 64-bit บนระบบปฏิบัติการ 64-bit<br>
• <code>SysWOW64</code>: เก็บไฟล์ DLL แบบ 32-bit เพื่อรันแอปพลิเคชัน 32-bit บนระบบ 64-bit
</td>
</tr>
<tr>
<td>\\WinSxS</td>
<td>โฟลเดอร์ <strong>Windows Component Store</strong> เป็นที่จัดเก็บและสำรองไฟล์ระบบเกือบทั้งหมด เพื่อใช้ซ่อมแซมและแก้ไขปัญหาไฟล์ระบบเสียหาย
</td>
</tr>
<tr>
<td>\\$Recycle.Bin</td>
<td><span class="w-dir-tag hidden">Hidden</span><br>
โฟลเดอร์ถังขยะ (Recycle Bin) บน Windows 7 หรือเวอร์ชันใหม่กว่า ใช้พักไฟล์ชั่วคราวที่ผู้ใช้สั่งลบออกแต่ยังไม่ได้สั่งลบถาวร
</td>
</tr>
<tr>
<td>\\Recycler</td>
<td><span class="w-dir-tag hidden">Hidden</span><br>
โฟลเดอร์ถังขยะของระบบปฏิบัติการ Windows รุ่นเก่า (ก่อน Windows 7) ทำหน้าที่เดียวกันกับ \$Recycle.Bin
</td>
</tr>
</tbody>
</table>
</div>
</div>"""

l168.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=168).update({"content": l168.content})
db.session.commit()
print("Windows System directory reference blocks updated and consolidated!")
