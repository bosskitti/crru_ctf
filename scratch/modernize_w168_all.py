import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l168 = db.session.query(TutorialLesson).filter_by(id=168).first()
blocks = json.loads(l168.content)

INTRO_CSS = """<style>
.s-intro{display:flex;gap:14px;align-items:flex-start;padding:16px 18px;border-radius:10px;margin-bottom:20px;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);width:100%;max-width:1050px;margin-left:auto;margin-right:auto;box-sizing:border-box;}
.s-intro-icon{font-size:1.5rem;flex-shrink:0;margin-top:1px;}
.s-intro-body strong{display:block;font-size:0.9rem;color:#e2e8f0;margin-bottom:5px;}
.s-intro-body p{margin:0;font-size:0.85rem;color:#94a3b8;line-height:1.7;}
.s-intro-body code{font-family:'JetBrains Mono',monospace;font-size:0.82rem;color:#fbbf24;background:rgba(251,191,36,0.08);padding:1px 5px;border-radius:3px;}
.s-intro.cyan{border-color:rgba(0,240,255,0.15);background:rgba(0,240,255,0.03);}
.s-intro.amber{border-color:rgba(251,191,36,0.15);background:rgba(251,191,36,0.03);}
.s-intro.green{border-color:rgba(61,220,132,0.15);background:rgba(61,220,132,0.03);}
.s-intro.purple{border-color:rgba(171,32,253,0.15);background:rgba(171,32,253,0.03);}
.s-intro.pink{border-color:rgba(244,114,182,0.15);background:rgba(244,114,182,0.03);}
</style>"""

# ─── 1. Block 34: File Examining and Printing Commands ───
blocks[34]['value'] = INTRO_CSS + """
<div class="s-intro amber">
<span class="s-intro-icon">🔍</span>
<div class="s-intro-body">
<strong>File Examining and Printing Commands (DOS)</strong>
<p>คำสั่งสำหรับ <strong>อ่าน ค้นหา และเรียงลำดับเนื้อหาในไฟล์</strong> บน Windows Command Line ทำงานเทียบเท่าคำสั่งใน Linux เช่น <code>type</code> ทำหน้าที่เหมือน <code>cat</code> และ <code>findstr</code> ทำหน้าที่ค้นหา pattern เหมือน <code>grep</code></p>
</div>
</div>

<style>
.dos-exam-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.dos-exam-sec{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;overflow:hidden;margin-bottom:24px;box-shadow:0 4px 20px rgba(0,0,0,0.2);}
.dos-exam-hdr{padding:14px 20px;display:flex;align-items:center;gap:14px;border-bottom:1px solid rgba(255,255,255,0.06);}
.dos-exam-mono{font-family:'JetBrains Mono',monospace;font-size:1.1rem;font-weight:800;flex-shrink:0;}
.dos-exam-txt{display:flex;flex-direction:column;gap:2px;}
.dos-exam-en{font-size:0.78rem;text-transform:uppercase;letter-spacing:0.1em;opacity:0.55;font-family:'JetBrains Mono',monospace;}
.dos-exam-th{font-size:0.83rem;font-weight:600;opacity:0.85;}
.sh-type .dos-exam-hdr{background:rgba(0,240,255,0.04);}.sh-type .dos-exam-mono,.sh-type .dos-exam-th{color:#00f0ff;}
.sh-findstr .dos-exam-hdr{background:rgba(251,191,36,0.04);}.sh-findstr .dos-exam-mono,.sh-findstr .dos-exam-th{color:#fbbf24;}
.sh-more .dos-exam-hdr{background:rgba(244,114,182,0.04);}.sh-more .dos-exam-mono,.sh-more .dos-exam-th{color:#f472b6;}
.sh-sort .dos-exam-hdr{background:rgba(255,0,127,0.04);}.sh-sort .dos-exam-mono,.sh-sort .dos-exam-th{color:#ff007f;}
.dos-exam-tbl{width:100%;border-collapse:collapse;}
.dos-exam-tbl th{padding:10px 16px;text-align:left;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.08em;font-weight:700;color:#8a94a6;background:rgba(255,255,255,0.01);border-bottom:1px solid rgba(255,255,255,0.05);}
.dos-exam-tbl td{padding:11px 16px;border-bottom:1px solid rgba(255,255,255,0.04);font-size:0.9rem;vertical-align:top;}
.dos-exam-tbl tr:last-child td{border-bottom:none;}
.dos-exam-tbl tr:hover td{background:rgba(255,255,255,0.02);}
.dos-exam-tbl td:first-child{font-family:'JetBrains Mono',monospace;font-size:0.88rem;white-space:nowrap;}
.dos-exam-tbl td:last-child{color:#94a3b8;line-height:1.6;}
.td-cyan{color:#00f0ff !important;}.td-amber{color:#fbbf24 !important;}.td-pink{color:#f472b6 !important;}.td-red{color:#ff007f !important;}
.dos-eg{display:block;margin-top:4px;font-size:0.82rem;color:#64748b;font-family:'JetBrains Mono',monospace;}
.dos-eg::before{content:"e.g. ";color:#475569;}
</style>

<div class="dos-exam-wrap">

<!-- type -->
<div class="dos-exam-sec sh-type">
<div class="dos-exam-hdr">
<span class="dos-exam-mono">type</span>
<div class="dos-exam-txt">
<span class="dos-exam-en">display file contents</span>
<span class="dos-exam-th">แสดงเนื้อหาทั้งหมดของไฟล์ข้อความบนหน้าจอ (เหมือน cat ใน Linux)</span>
</div>
</div>
<table class="dos-exam-tbl">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-cyan">type [file]</td><td>แสดงเนื้อหาภายในไฟล์ข้อความที่กำหนดออกทางหน้าจอ Command Prompt<span class="dos-eg">type flag.txt</span></td></tr>
</table>
</div>

<!-- findstr -->
<div class="dos-exam-sec sh-findstr">
<div class="dos-exam-hdr">
<span class="dos-exam-mono">findstr</span>
<div class="dos-exam-txt">
<span class="dos-exam-en">search for strings in files</span>
<span class="dos-exam-th">ค้นหาข้อความหรือคำในไฟล์โดยใช้คำสำคัญหรือ Regular Expression (เหมือน grep ใน Linux)</span>
</div>
</div>
<table class="dos-exam-tbl">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-amber">findstr "word" [file]</td><td>ค้นหาบรรทัดที่มีข้อความหรือคำค้นหาที่ระบุในไฟล์</td></tr>
<tr><td class="td-amber">findstr /i "word" [file]</td><td>ค้นหาโดยไม่สนใจตัวพิมพ์เล็กหรือตัวพิมพ์ใหญ่ (Case-insensitive)</td></tr>
<tr><td class="td-amber">findstr /r "[regex]" [file]</td><td>ค้นหาข้อความโดยใช้ Regular Expression (Regex)<span class="dos-eg">findstr /r "^[0-9]" data.txt</span></td></tr>
<tr><td class="td-amber">findstr /s "word" *.*</td><td>ค้นหาคำในทุกไฟล์ในโฟลเดอร์ปัจจุบันและโฟลเดอร์ย่อยทั้งหมด (Recursive)</td></tr>
</table>
</div>

<!-- more -->
<div class="dos-exam-sec sh-more">
<div class="dos-exam-hdr">
<span class="dos-exam-mono">more</span>
<div class="dos-exam-txt">
<span class="dos-exam-en">display output page by page</span>
<span class="dos-exam-th">แสดงผลลัพธ์ทีละหน้าจอ เหมาะสำหรับไฟล์ขนาดใหญ่หรือข้อมูลที่ยาวเกินหน้าจอ</span>
</div>
</div>
<table class="dos-exam-tbl">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-pink">more [file]</td><td>แสดงเนื้อหาไฟล์ทีละหน้า กด Space เพื่อดูหน้าถัดไป หรือกด Enter เพื่อเลื่อนทีละบรรทัด</td></tr>
<tr><td class="td-pink">more /c [file]</td><td>ล้างหน้าจอก่อนแสดงข้อมูลหน้าถัดไป (Clear screen display)</td></tr>
</table>
</div>

<!-- sort -->
<div class="dos-exam-sec sh-sort">
<div class="dos-exam-hdr">
<span class="dos-exam-mono">sort</span>
<div class="dos-exam-txt">
<span class="dos-exam-en">sort file lines</span>
<span class="dos-exam-th">เรียงลำดับข้อมูลบรรทัดในไฟล์ตามตัวอักษรหรือตัวเลข</span>
</div>
</div>
<table class="dos-exam-tbl">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-red">sort [file]</td><td>เรียงลำดับข้อมูลในไฟล์จากน้อยไปมากตามตัวอักษร</td></tr>
<tr><td class="td-red">sort /r [file]</td><td>เรียงลำดับย้อนกลับจากมากไปน้อย (Reverse order)</td></tr>
</table>
</div>

</div>"""

# Clear blocks 35 to 41 since we merged them into block 34
for i in range(35, 42):
    blocks[i]['value'] = ""


# ─── 2. Block 42: File and Directory Permission Commands ───
blocks[42]['value'] = INTRO_CSS + """
<div class="s-intro cyan">
<span class="s-intro-icon">🛡️</span>
<div class="s-intro-body">
<strong>Windows NTFS Permission System & Attributes</strong>
<p>Windows ใช้ระบบความปลอดภัยสิทธิ์เข้าถึงไฟล์แบบ <strong>NTFS permissions (Access Control Lists - ACLs)</strong> และระบบแอตทริบิวต์คุณสมบัติไฟล์ (File Attributes เช่น Hidden, Read-only) สามารถควบคุมได้ผ่านคำสั่ง <code>icacls</code> และ <code>attrib</code></p>
</div>
</div>

<style>
.w-perm-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:24px;}
.w-perm-card{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,0.2);}
.w-perm-hdr{padding:14px 20px;border-bottom:1px solid rgba(255,255,255,0.05);background:rgba(0,240,255,0.02);}
.w-perm-hdr h4{margin:0 0 4px;font-size:0.98rem;font-weight:700;color:#00f0ff;}
.w-perm-hdr p{margin:0;font-size:0.82rem;color:#64748b;line-height:1.5;}
.w-perm-tbl{width:100%;border-collapse:collapse;}
.w-perm-tbl th{padding:10px 16px;text-align:left;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.08em;font-weight:700;color:#8a94a6;background:rgba(255,255,255,0.01);border-bottom:1px solid rgba(255,255,255,0.05);}
.w-perm-tbl td{padding:12px 16px;border-bottom:1px solid rgba(255,255,255,0.04);font-size:0.88rem;vertical-align:top;line-height:1.6;}
.w-perm-tbl tr:last-child td{border-bottom:none;}
.w-perm-tbl tr:hover td{background:rgba(255,255,255,0.02);}
.w-perm-tbl td:first-child{font-family:'JetBrains Mono',monospace;font-size:0.92rem;font-weight:700;color:#00f0ff;}
.w-perm-tbl td:last-child{color:#94a3b8;}
.flag-g{color:#3ddc84;font-weight:700;font-family:'JetBrains Mono',monospace;}
.flag-r{color:#ff007f;font-weight:700;font-family:'JetBrains Mono',monospace;}
.w-perm-note{display:flex;align-items:flex-start;gap:10px;margin:12px 16px;padding:12px 14px;border-radius:8px;background:rgba(0,240,255,0.04);border:1px solid rgba(0,240,255,0.12);}
.w-perm-note-icon{font-size:1rem;flex-shrink:0;}
.w-perm-note-text{font-size:0.83rem;color:#94a3b8;line-height:1.6;font-family:'JetBrains Mono',monospace;}
.w-perm-note-text span{color:#fbbf24;font-weight:700;}
</style>

<div class="w-perm-wrap">

<!-- Standard permissions -->
<div class="w-perm-card">
<div class="w-perm-hdr">
<h4>🛡️ Standard Windows NTFS Permissions</h4>
<p>ประเภทสิทธิ์มาตรฐานที่ระบุแก่ผู้ใช้งานในระบบไฟล์ NTFS</p>
</div>
<table class="w-perm-tbl">
<tr><th>Permission</th><th>Description (คำอธิบายสิทธิ์การใช้งาน)</th></tr>
<tr><td>Full Control (F)</td><td>มีสิทธิ์สูงสุดเหนือไฟล์และโฟลเดอร์ รวมถึงการเปลี่ยนแปลงสิทธิ์ของผู้อื่นด้วย</td></tr>
<tr><td>Modify (M)</td><td>อนุญาตให้อ่าน เขียน แก้ไข และลบไฟล์หรือโฟลเดอร์ย่อยได้</td></tr>
<tr><td>Read & Execute (RX)</td><td>อนุญาตให้อ่านข้อมูลและสามารถรันไฟล์โปรแกรม (.exe, .bat) ได้</td></tr>
<tr><td>List Folder Contents</td><td>อนุญาตเฉพาะการดูรายชื่อไฟล์และโฟลเดอร์ย่อยข้างใน (สำหรับโฟลเดอร์เท่านั้น)</td></tr>
<tr><td>Read (R)</td><td>อนุญาตให้เปิดอ่านเนื้อหาไฟล์หรือดูคุณสมบัติทั่วไปได้เท่านั้น</td></tr>
<tr><td>Write (W)</td><td>อนุญาตให้สร้างไฟล์ใหม่ เขียนทับ หรือเขียนต่อท้ายเนื้อหาในไฟล์</td></tr>
</table>
</div>

<!-- icacls -->
<div class="w-perm-card">
<div class="w-perm-hdr">
<h4>⚙️ icacls — จัดการ Access Control Lists (ACLs)</h4>
<p>แสดง แก้ไข หรือสำรองข้อมูลการอนุญาตสิทธิ์เข้าถึงไฟล์ของแต่ละ User/Group</p>
</div>
<table class="w-perm-tbl">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td>icacls [file]</td><td>แสดงรายชื่อสิทธิ์การเข้าถึง (ACL) ทั้งหมดของไฟล์หรือโฟลเดอร์</td></tr>
<tr><td>icacls [file] /grant [user]:[perm]</td><td>มอบสิทธิ์การเข้าถึงประเภทที่กำหนดให้กับผู้ใช้<span class="dos-eg">icacls "data.txt" /grant User1:F</span></td></tr>
<tr><td>icacls [file] /deny [user]:[perm]</td><td>ปฏิเสธสิทธิ์การเข้าถึงอย่างชัดแจ้ง (มีผลสำคัญกว่า /grant)<span class="dos-eg">icacls "data.txt" /deny Guest:W</span></td></tr>
</table>
<div class="w-perm-note">
<span class="w-perm-note-icon">💡</span>
<div class="w-perm-note-text">ตัวย่อสิทธิ์ของ icacls: <span>n</span> = no access, <span>f</span> = full, <span>m</span> = modify, <span>rx</span> = read/execute, <span>r</span> = read, <span>w</span> = write, <span>d</span> = delete</div>
</div>
</div>

<!-- attrib -->
<div class="w-perm-card" style="border-color:rgba(251,191,36,0.15);">
<div class="w-perm-hdr" style="background:rgba(251,191,36,0.02);">
<h4 style="color:#fbbf24;">🏷️ attrib — จัดการแอตทริบิวต์ไฟล์ (File Attributes)</h4>
<p>แสดงผลหรือสลับแอตทริบิวต์ของคุณสมบัติความปลอดภัยทางกายภาพของไฟล์</p>
</div>
<table class="w-perm-tbl">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td>attrib [file]</td><td>แสดงแอตทริบิวต์ปัจจุบันของไฟล์</td></tr>
<tr><td>attrib +r [file] / attrib -r [file]</td><td><span class="flag-g">+r</span> กำหนดไฟล์เป็น Read-only (อ่านอย่างเดียว) / <span class="flag-r">-r</span> ยกเลิกคุณสมบัติอ่านอย่างเดียว</td></tr>
<tr><td>attrib +h [file] / attrib -h [file]</td><td><span class="flag-g">+h</span> กำหนดไฟล์เป็น Hidden (ซ่อนไฟล์) / <span class="flag-r">-h</span> ยกเลิกการซ่อนไฟล์</td></tr>
<tr><td>attrib +s [file] / attrib -s [file]</td><td><span class="flag-g">+s</span> กำหนดเป็นไฟล์ของระบบ (System file) / <span class="flag-r">-s</span> ยกเลิกคุณสมบัติไฟล์ระบบ</td></tr>
<tr><td>attrib /s /d [path]</td><td>กำหนดให้ attrib มีผลครอบคลุมเข้าไปในโฟลเดอร์ย่อยและโฟลเดอร์หลักทั้งหมด (Recursive)<span class="dos-eg">attrib +r +h /s /d C:\\data\\*.*</span></td></tr>
</table>
</div>

</div>"""

# Clear blocks 43 to 55 since we merged them into block 42
for i in range(43, 56):
    blocks[i]['value'] = ""


# ─── 3. Block 56: Frequently Used Commands ───
blocks[56]['value'] = INTRO_CSS + """
<div class="s-intro green">
<span class="s-intro-icon">⚡</span>
<div class="s-intro-body">
<strong>Frequently Used Commands (Windows / DOS)</strong>
<p>คำสั่งทั่วไปสำหรับการบริหารจัดการเครื่อง ตรวจสอบสถานะหน่วยบันทึกข้อมูล (<code>chkdsk</code>), การตรวจสอบกระบวนการทำงานและหยุดการทำงาน (<code>tasklist</code>, <code>taskkill</code>), และการตั้งค่านโยบายเครือข่ายและผู้ใช้ (<code>net</code>)</p>
</div>
</div>

<style>
.w-freq-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.w-freq-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;}
@media(max-width:700px){.w-freq-grid{grid-template-columns:repeat(2,1fr);}}
@media(max-width:460px){.w-freq-grid{grid-template-columns:1fr;}}
.w-freq-card{background:rgba(15,17,26,0.5);border:1px solid rgba(255,255,255,0.05);border-radius:10px;padding:14px 16px;transition:all 0.2s ease;cursor:default;}
.w-freq-card:hover{background:rgba(255,255,255,0.03);border-color:rgba(61,220,132,0.15);transform:translateY(-2px);box-shadow:0 6px 20px rgba(0,0,0,0.3);}
.w-freq-card:hover .w-freq-cmd{color:#3ddc84;text-shadow:0 0 8px rgba(61,220,132,0.4);}
.w-freq-cmd{font-family:'JetBrains Mono',monospace;font-size:0.95rem;font-weight:800;color:#e2e8f0;margin-bottom:4px;transition:all 0.2s;}
.w-freq-en{font-size:0.74rem;color:#64748b;line-height:1.4;margin-bottom:4px;font-style:italic;}
.w-freq-th{font-size:0.8rem;color:#94a3b8;line-height:1.45;}
</style>

<div class="w-freq-wrap">
<div class="w-freq-grid">
<div class="w-freq-card"><div class="w-freq-cmd">chkdsk</div><div class="w-freq-en">check disk and report status</div><div class="w-freq-th">ตรวจสอบระบบไฟล์และดิสก์พร้อมสร้างรายงานข้อผิดพลาด</div></div>
<div class="w-freq-card"><div class="w-freq-cmd">cls</div><div class="w-freq-en">clear screen</div><div class="w-freq-th">ล้างข้อความผลลัพธ์ทั้งหมดออกจากหน้าจอ Command Prompt</div></div>
<div class="w-freq-card"><div class="w-freq-cmd">date</div><div class="w-freq-en">display or set date</div><div class="w-freq-th">แสดงวันที่หรือกำหนดวันที่ใหม่ให้ระบบปฏิบัติการ</div></div>
<div class="w-freq-card"><div class="w-freq-cmd">exit</div><div class="w-freq-en">exit cmd interpreter</div><div class="w-freq-th">ออกจากโปรแกรม Command Prompt (cmd.exe)</div></div>
<div class="w-freq-card"><div class="w-freq-cmd">fc</div><div class="w-freq-en">file compare and print diffs</div><div class="w-freq-th">เปรียบเทียบไฟล์สองไฟล์และแสดงความแตกต่างที่ตรวจพบ</div></div>
<div class="w-freq-card"><div class="w-freq-cmd">find</div><div class="w-freq-en">search text string in files</div><div class="w-freq-th">ค้นหาคำหรือข้อความที่ตรงกันในไฟล์ (แบบพื้นฐาน)</div></div>
<div class="w-freq-card"><div class="w-freq-cmd">help</div><div class="w-freq-en">provide command help details</div><div class="w-freq-th">แสดงคู่มือข้อมูลอธิบายการใช้งานเบื้องต้นของคำสั่งที่ระบุ</div></div>
<div class="w-freq-card"><div class="w-freq-cmd">ipconfig</div><div class="w-freq-en">display TCP/IP configurations</div><div class="w-freq-th">แสดงการตั้งค่าและที่อยู่ IP ของการ์ดเครือข่ายทั้งหมดในเครื่อง</div></div>
<div class="w-freq-card"><div class="w-freq-cmd">net</div><div class="w-freq-en">manage network and users</div><div class="w-freq-th">ตั้งค่าและแสดงนโยบายเครือข่าย บัญชีผู้ใช้ หรือการแชร์ไฟล์</div></div>
<div class="w-freq-card"><div class="w-freq-cmd">openfiles</div><div class="w-freq-en">show files opened by remote users</div><div class="w-freq-th">แสดงรายชื่อไฟล์ของเครื่องปัจจุบันที่ถูกเปิดรันโดยผู้ใช้อื่นบนเครือข่าย</div></div>
<div class="w-freq-card"><div class="w-freq-cmd">path</div><div class="w-freq-en">display or set search path</div><div class="w-freq-th">แสดงผลหรือกำหนดที่อยู่โฟลเดอร์สำหรับค้นหาโปรแกรมรันอัตโนมัติ</div></div>
<div class="w-freq-card"><div class="w-freq-cmd">print</div><div class="w-freq-en">print text file</div><div class="w-freq-th">ส่งไฟล์เอกสารข้อความไปยังเครื่องพิมพ์</div></div>
<div class="w-freq-card"><div class="w-freq-cmd">prompt</div><div class="w-freq-en">change command prompt layout</div><div class="w-freq-th">กำหนดรูปแบบสัญลักษณ์การแสดงผลและที่อยู่ของพรอมต์ใหม่</div></div>
<div class="w-freq-card"><div class="w-freq-cmd">rd / rmdir</div><div class="w-freq-en">remove directory</div><div class="w-freq-th">ลบโฟลเดอร์เปล่าออกจากเครื่อง</div></div>
<div class="w-freq-card"><div class="w-freq-cmd">ren / rename</div><div class="w-freq-en">rename file or folder</div><div class="w-freq-th">เปลี่ยนชื่อไฟล์หรือโฟลเดอร์ที่ระบุ</div></div>
<div class="w-freq-card"><div class="w-freq-cmd">tasklist</div><div class="w-freq-en">display active processes</div><div class="w-freq-th">แสดงรายชื่อกระบวนการ (Processes) และแอปพลิเคชันทั้งหมดที่รันอยู่</div></div>
<div class="w-freq-card"><div class="w-freq-cmd">taskkill</div><div class="w-freq-en">kill process by pid or name</div><div class="w-freq-th">สั่งปิดหรือหยุดการทำงานของ Process ตามชื่อหรือ PID ที่กำหนด</div></div>
<div class="w-freq-card"><div class="w-freq-cmd">time</div><div class="w-freq-en">display or set system time</div><div class="w-freq-th">แสดงผลหรือกำหนดเวลาปัจจุบันให้แก่ระบบปฏิบัติการ</div></div>
<div class="w-freq-card"><div class="w-freq-cmd">title</div><div class="w-freq-en">set window title for cmd</div><div class="w-freq-th">ตั้งชื่อหัวข้อหน้าต่าง (Window Title) ของ Command Prompt ปัจจุบัน</div></div>
<div class="w-freq-card"><div class="w-freq-cmd">tree</div><div class="w-freq-en">display graphical directory tree</div><div class="w-freq-th">แสดงผลแผนผังโฟลเดอร์และโฟลเดอร์ย่อยในรูปกราฟิกต้นไม้</div></div>
<div class="w-freq-card"><div class="w-freq-cmd">ver</div><div class="w-freq-en">display Windows OS version</div><div class="w-freq-th">แสดงชื่อและหมายเลขเวอร์ชันการอัปเดตของ Windows ปัจจุบัน</div></div>
<div class="w-freq-card"><div class="w-freq-cmd">vol</div><div class="w-freq-en">display volume label and serial</div><div class="w-freq-th">แสดงชื่อป้ายกำกับของไดรฟ์ดิสก์และหมายเลขซีเรียล</div></div>
<div class="w-freq-card"><div class="w-freq-cmd">xcopy</div><div class="w-freq-en">copy files and directory trees</div><div class="w-freq-th">คัดลอกไฟล์และโครงสร้างโฟลเดอร์ทั้งหมดไปยังตำแหน่งใหม่อย่างครอบคลุม</div></div>
</div>
</div>"""

# Clear blocks 57 to 65 since we merged them into block 56
for i in range(57, 66):
    blocks[i]['value'] = ""


# ─── 4. Block 66: DOS Terminal Output Examples ───
blocks[66]['value'] = """#### 💻 ตัวอย่าง Output ของคำสั่งที่ใช้บ่อยใน Command Prompt

<style>
.dos-ex-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.dos-ex-term{background:#070910;border-radius:10px;overflow:hidden;border:1px solid rgba(255,255,255,0.08);box-shadow:0 8px 32px rgba(0,0,0,0.5);}
.dos-ex-bar{background:rgba(28,30,44,0.98);padding:9px 16px;display:flex;align-items:center;gap:8px;border-bottom:1px solid rgba(255,255,255,0.05);}
.dos-ex-dot{width:11px;height:11px;border-radius:50%;}
.dos-ex-dot.r{background:#ff5f57;}.dos-ex-dot.y{background:#ffbd2e;}.dos-ex-dot.g{background:#28c840;}
.dos-ex-title{flex:1;text-align:center;font-size:0.75rem;color:#8a94a6;font-family:'JetBrains Mono',monospace;letter-spacing:0.06em;}
.dos-ex-body{padding:20px 24px 24px;font-family:'JetBrains Mono','Courier New',monospace;font-size:0.83rem;line-height:1.75;}
.dos-ex-prompt{color:#fbbf24;}.dos-ex-cmd{color:#ffffff;font-weight:600;}
.dos-ex-out{color:#94a3b8;white-space:pre;}
.dos-ex-out-g{color:#3ddc84;white-space:pre;}
.dos-ex-out-y{color:#fbbf24;white-space:pre;}
.dos-ex-out-c{color:#00f0ff;white-space:pre;}
.dos-ex-divider{border:none;border-top:1px solid rgba(255,255,255,0.05);margin:12px 0;}
</style>

<div class="dos-ex-wrap">
<div class="dos-ex-term">
<div class="dos-ex-bar">
<span class="dos-ex-dot r"></span><span class="dos-ex-dot y"></span><span class="dos-ex-dot g"></span>
<span class="dos-ex-title">Command Prompt (cmd.exe)</span>
</div>
<div class="dos-ex-body">
<div><span class="dos-ex-prompt">C:\\Users\\HP&gt;</span> <span class="dos-ex-cmd">date</span></div>
<div class="dos-ex-out-y">The current date is: Thu 02/09/2023
Enter the new date: (mm-dd-yy)</div>
<hr class="dos-ex-divider"/>
<div><span class="dos-ex-prompt">C:\\Users\\HP&gt;</span> <span class="dos-ex-cmd">ver</span></div>
<div class="dos-ex-out-c">Microsoft Windows [Version 10.0.19045.2486]</div>
<hr class="dos-ex-divider"/>
<div><span class="dos-ex-prompt">C:\\Users\\HP&gt;</span> <span class="dos-ex-cmd">vol</span></div>
<div class="dos-ex-out">Volume in drive C is Windows
Volume Serial Number is 2CC4-F411</div>
<hr class="dos-ex-divider"/>
<div><span class="dos-ex-prompt">C:\\Users\\HP&gt;</span> <span class="dos-ex-cmd">tasklist</span></div>
<div class="dos-ex-out">Image Name                     PID Session Name        Session#    Mem Usage
========================= ======== ================ =========== ============
System Idle Process              0 Services                   0          8 K
System                           4 Services                   0      5,768 K
Registry                       172 Services                   0     25,504 K
smss.exe                       636 Services                   0        412 K
csrss.exe                     1000 Services                   0      2,472 K
wininit.exe                   1032 Services                   0      1,912 K
services.exe                  1092 Services                   0     15,224 K
lsass.exe                     1112 Services                   0     18,740 K</div>
</div>
</div>
</div>"""

# Clear blocks 67 to 78 since we merged them into block 66
for i in range(67, 79):
    blocks[i]['value'] = ""


# ─── 5. Block 79: Environment Variables ───
blocks[79]['value'] = INTRO_CSS + """
<div class="s-intro purple">
<span class="s-intro-icon">🌐</span>
<div class="s-intro-body">
<strong>Windows Environment Variables</strong>
<p>ตัวแปรสภาพแวดล้อมที่จัดเก็บค่าระบบปฏิบัติการ Windows สำหรับเก็บข้อมูลและเรียกใช้การกำหนดค่าจากโปรแกรมต่างๆ สามารถแสดงค่าของตัวแปรระบบได้ด้วยคำสั่ง <code>echo %VARIABLE%</code></p>
</div>
</div>

<style>
.w-env-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.w-env-card{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,0.2);}
.w-env-tbl{width:100%;border-collapse:collapse;}
.w-env-tbl th{padding:10px 16px;text-align:left;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.08em;font-weight:700;color:#8a94a6;background:rgba(255,255,255,0.01);border-bottom:1px solid rgba(255,255,255,0.05);}
.w-env-tbl td{padding:12px 16px;border-bottom:1px solid rgba(255,255,255,0.04);font-size:0.9rem;vertical-align:top;line-height:1.6;}
.w-env-tbl tr:last-child td{border-bottom:none;}
.w-env-tbl tr:hover td{background:rgba(255,255,255,0.02);}
.w-env-var{font-family:'JetBrains Mono',monospace;font-size:0.92rem;color:#3ddc84;font-weight:700;}
.w-env-tbl td:last-child{color:#94a3b8;}
.w-env-val{font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#64748b;margin-top:4px;}
</style>

<div class="w-env-wrap">
<div class="w-env-card">
<table class="w-env-tbl">
<tr><th>Variable</th><th>Description & Example</th></tr>
<tr><td class="w-env-var">%PATH%</td><td>รายชื่อโฟลเดอร์สำหรับค้นหาโปรแกรมเมื่อมีการรันคำสั่ง คั่นด้วยเครื่องหมาย semicolon (<code>;</code>)<div class="w-env-val">e.g. C:\\Windows\\system32;C:\\Windows</div></td></tr>
<tr><td class="w-env-var">%PROMPT%</td><td>การกำหนดรูปแบบสัญลักษณ์และข้อมูลนำหน้าระบบ Command Prompt</td></tr>
<tr><td class="w-env-var">%TEMP% / %TMP%</td><td>ตำแหน่งที่เก็บไฟล์ชั่วคราว (Temporary Files) ของผู้ใช้ปัจจุบัน<div class="w-env-val">e.g. C:\\Users\\User\\AppData\\Local\\Temp</div></td></tr>
<tr><td class="w-env-var">%OS%</td><td>ระบุประเภทและชื่อระบบปฏิบัติการหลัก<div class="w-env-val">e.g. Windows_NT</div></td></tr>
<tr><td class="w-env-var">%USERPROFILE%</td><td>เส้นทางโฟลเดอร์โฮมและข้อมูลโปรไฟล์ของผู้ใช้งานปัจจุบัน (เหมือน $HOME)<div class="w-env-val">e.g. C:\\Users\\Administrator</div></td></tr>
<tr><td class="w-env-var">%WINDIR% / %SYSTEMROOT%</td><td>เส้นทางตำแหน่งโฟลเดอร์การติดตั้งหลักของตัว Windows OS<div class="w-env-val">e.g. C:\\Windows</div></td></tr>
</table>
</div>
</div>"""

# Remove empty blocks to clean up UI spaces
non_empty_blocks = [b for b in blocks if len(b.get("value", "").strip()) > 0]
l168.content = json.dumps(non_empty_blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=168).update({"content": l168.content})
db.session.commit()

print(f"Windows command tables modernized! Final blocks count: {len(non_empty_blocks)}")
