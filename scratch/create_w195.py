import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

# ─── Check if lesson 195 already exists, if so delete it to recreate cleanly ───
existing = db.session.query(TutorialLesson).filter_by(id=195).first()
if existing:
    db.session.delete(existing)
    db.session.commit()
    print("Deleted old Lesson 195 to recreate cleanly.")

# ─── Create Lesson 195 Blocks ───
blocks_195 = []

# Block 0: Header
blocks_195.append({
    "type": "markdown",
    "value": "## 🖥️ คำสั่งควบคุมและตัวแปรสภาพแวดล้อมใน Windows (Windows DOS Commands & Environment)"
})

# Block 1: Intro Overview
blocks_195.append({
    "type": "markdown",
    "value": """### 📌 Overview of Windows Commands & Variables

บทเรียนนี้จะอธิบายสภาพแวดล้อมการควบคุมระบบปฏิบัติการ Windows ผ่านบรรทัดคำสั่ง **DOS/Command Prompt (cmd.exe)**, โครงสร้างคำสั่งควบคุมไฟล์ ตรวจสอบระบบ, และตัวแปรสภาพแวดล้อม (Environment Variables) ที่จำเป็นสำหรับผู้เชี่ยวชาญด้านความมั่นคงปลอดภัยไซเบอร์:

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
<div class="w-intro-title">🐚 DOS Terminal (CMD)</div>
<p class="w-intro-desc">เรียนรู้กลไกประวัติความเป็นมาและโครงสร้างการป้อนคำสั่งควบคุม cmd.exe ที่สืบทอดมาจาก MS-DOS</p>
</div>
<div class="w-intro-card">
<div class="w-intro-title">📂 File & System Commands</div>
<p class="w-intro-desc">รวบรวมคำสั่งจัดการระบบไฟล์ ค้นหา ตรวจสอบค่าคอนฟิก และแสดงผลโปรเซสของวินโดวส์อย่างละเอียด</p>
</div>
<div class="w-intro-card">
<div class="w-intro-title">⚙️ Environment Variables</div>
<p class="w-intro-desc">วิเคราะห์ตัวแปรสภาพแวดล้อมสำคัญ เช่น %PATH% และ %USERPROFILE% ที่มัลแวร์มักใช้ช่องโหว่โจมตี</p>
</div>
</div>
</div>"""
})

blocks_195.append({"type": "markdown", "value": "---"})

# Block 3: DOS in Windows System
blocks_195.append({
    "type": "markdown",
    "value": """### 🏛️ DOS in Windows System

**DOS (Disk Operating System)** คือแพลตฟอร์มระบบปฏิบัติการยุคแรกที่ควบคุมฮาร์ดแวร์ผ่านบรรทัดคำสั่งแบบข้อความ โดยมีรากฐานมาจาก **MS-DOS (Microsoft DOS)** และ **PC DOS (IBM)** ที่ปล่อยออกมาในปี 1981:

<style>
.w-dos-box{width:100%;max-width:1050px;margin:2rem auto;display:flex;gap:28px;align-items:center;}
@media(max-width:768px){.w-dos-box{flex-direction:column;}}
.w-dos-desc{flex:1.2;font-size:0.88rem;color:#94a3b8;line-height:1.75;}
.w-dos-desc strong{color:#ffffff;}
.w-dos-desc ul{margin:8px 0;padding-left:20px;}
.w-dos-desc li{margin-bottom:6px;}
.w-dos-vis{flex:0.8;background:rgba(15,17,26,0.6);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:24px;display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:180px;box-sizing:border-box;}
.w-dos-tag{font-family:'JetBrains Mono',monospace;font-size:1.4rem;font-weight:800;color:#fbbf24;text-shadow:0 0 10px rgba(251,191,36,0.4);margin-bottom:12px;}
.w-dos-arch{display:flex;align-items:center;gap:12px;width:100%;justify-content:center;}
.w-arch-box{padding:6px 12px;border:1px solid rgba(255,255,255,0.1);background:rgba(255,255,255,0.03);border-radius:6px;font-size:0.75rem;font-family:'JetBrains Mono',monospace;color:#e2e8f0;}
</style>

<div class="w-dos-box">
<div class="w-dos-desc">
<p>ระบบปฏิบัติการกลุ่ม MS-DOS ออกแบบมาสำหรับทำงานร่วมกับสถาปัตยกรรมหน่วยประมวลผลยุคประวัติศาสตร์ เช่น <strong>Intel 8080, Intel x86 (8086/80286/etc.) และ Zilog Z80</strong></p>
<p><strong>ความสัมพันธ์ของ DOS และ Windows ในปัจจุบัน:</strong></p>
<ul>
<li>ในอดีต (Windows 95/98/Me) ระบบ Windows เป็นเพียงหน้ากากกราฟิก (GUI) ที่ทำงานครอบอยู่บนฐานระบบปฏิบัติการ MS-DOS อีกทีหนึ่ง</li>
<li>ในปัจจุบัน (Windows NT/10/11) แม้ Windows จะเปลี่ยนไปใช้เคอร์เนลของตนเองแล้ว แต่ยังคงเก็บความสามารถและชุดคำสั่งของ DOS ไว้ภายในเพื่อรองรับแอปพลิเคชันเก่า ผ่านโปรแกรมจำลองหน้าต่างเทอร์มินัล <strong>cmd.exe (Command Prompt)</strong></li>
</ul>
</div>
<div class="w-dos-vis">
<div class="w-dos-tag">DOS in Windows</div>
<div class="w-dos-arch">
<div class="w-arch-box" style="border-color:#00f0ff;color:#00f0ff;">Windows GUI</div>
<div style="color:#64748b;font-size:0.8rem;">◀ runs ▶</div>
<div class="w-arch-box" style="border-color:#fbbf24;color:#fbbf24;">cmd.exe (DOS)</div>
</div>
</div>
</div>"""
})

blocks_195.append({"type": "markdown", "value": "---"})

# Block 5: DOS Command Line Structure
blocks_195.append({
    "type": "markdown",
    "value": """### 🖥️ DOS Command Line Structure

การป้อนคำสั่งและใช้งาน Command Prompt ใน Windows มีโครงสร้างไวยากรณ์หลักที่ประกอบด้วย 4 ส่วนสำคัญดังนี้:

<style>
.w-cmd-struct-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.w-terminal-mock{background:#070910;border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:24px;box-shadow:0 12px 32px rgba(0,0,0,0.5);font-family:'JetBrains Mono',monospace;box-sizing:border-box;}
.w-term-hdr{display:flex;gap:6px;margin-bottom:18px;}
.w-dot{width:10px;height:10px;border-radius:50%;}
.w-dot.red{background:#ff5f56;}.w-dot.yellow{background:#ffbd2e;}.w-dot.green{background:#27c93f;}
.w-term-line{font-size:1.15rem;color:#e2e8f0;display:flex;flex-wrap:wrap;gap:12px;align-items:center;}
.w-term-piece{position:relative;padding:4px 8px;border-radius:4px;cursor:pointer;transition:all 0.15s ease;}
.w-term-piece:hover{transform:translateY(-1px);}
.w-term-piece.prompt{border:1px solid rgba(0,240,255,0.3);background:rgba(0,240,255,0.04);color:#00f0ff;}
.w-term-piece.command{border:1px solid rgba(255,0,127,0.3);background:rgba(255,0,127,0.04);color:#ff007f;}
.w-term-piece.options{border:1px solid rgba(251,191,36,0.3);background:rgba(251,191,36,0.04);color:#fbbf24;}
.w-term-piece.args{border:1px solid rgba(171,32,253,0.3);background:rgba(171,32,253,0.04);color:#ab20fd;}

.w-term-exp-panel{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:20px;}
@media(max-width:768px){.w-term-exp-panel{grid-template-columns:1fr;}}
.w-term-exp-card{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:12px 14px;}
.w-term-exp-card.active{border-color:currentColor;}
.w-term-exp-title{font-size:0.83rem;font-weight:800;margin-bottom:4px;font-family:'JetBrains Mono',monospace;}
.w-term-exp-desc{font-size:0.78rem;color:#94a3b8;line-height:1.5;margin:0;}
</style>

<div class="w-cmd-struct-wrap">
<div class="w-terminal-mock">
<div class="w-term-hdr">
<div class="w-dot red"></div><div class="w-dot yellow"></div><div class="w-dot green"></div>
</div>
<div class="w-term-line">
<span class="w-term-piece prompt" onmouseover="focusPiece('prompt')" onclick="focusPiece('prompt')">C:\\Users\\User&gt;</span>
<span class="w-term-piece command" onmouseover="focusPiece('command')" onclick="focusPiece('command')">dir</span>
<span class="w-term-piece options" onmouseover="focusPiece('options')" onclick="focusPiece('options')">/a:h</span>
<span class="w-term-piece args" onmouseover="focusPiece('args')" onclick="focusPiece('args')">C:\\</span>
</div>
</div>

<div class="w-term-exp-panel">
<div id="exp-prompt" class="w-term-exp-card" style="color:#00f0ff;">
<div class="w-term-exp-title">1. Prompt (ตัวเตือนรับคำสั่ง)</div>
<p class="w-term-exp-desc">ระบุตำแหน่งไดเรกทอรีปัจจุบันที่ผู้ใช้กำลังทำงานอยู่ พร้อมสัญญลักษณ์ <code>&gt;</code> รอรับอินพุต</p>
</div>
<div id="exp-command" class="w-term-exp-card" style="color:#ff007f;">
<div class="w-term-exp-title">2. Command (คำสั่งหลัก)</div>
<p class="w-term-exp-desc">ชื่อไฟล์รันระบบของ DOS หรือคำสั่งในตัว (Built-in) เช่น <code>dir</code> สำหรับแสดงผลรายชื่อไฟล์</p>
</div>
<div id="exp-options" class="w-term-exp-card" style="color:#fbbf24;">
<div class="w-term-exp-title">3. Options / Switches</div>
<p class="w-term-exp-desc">ส่วนเสริมระบุคุณลักษณะการทำงาน ขึ้นต้นด้วยสัญลักษณ์ Forward Slash (เช่น <code>/a:h</code> แสดงเฉพาะไฟล์ซ่อน)</p>
</div>
<div id="exp-args" class="w-term-exp-card" style="color:#ab20fd;">
<div class="w-term-exp-title">4. Arguments (อาร์กิวเมนต์)</div>
<p class="w-term-exp-desc">เป้าหมายที่คำสั่งจะเข้าไปดำเนินการ เช่น ระบุโฟลเดอร์ปลายทาง ไฟล์อินพุต หรือพาธปลายทาง</p>
</div>
</div>
</div>

<script>
function focusPiece(type) {
const cards = document.querySelectorAll('.w-term-exp-card');
cards.forEach(c => {
c.classList.remove('active');
c.style.background = 'rgba(255,255,255,0.02)';
});
const target = document.getElementById('exp-' + type);
if (target) {
target.classList.add('active');
target.style.background = 'rgba(255,255,255,0.06)';
}
}
</script>"""
})

blocks_195.append({"type": "markdown", "value": "---"})

# Block 7: File & Directory Manipulation Commands (dir, cd, mkdir, copy, move, del)
blocks_195.append({
    "type": "markdown",
    "value": """### 📂 File & Directory Manipulation Commands

กลุ่มคำสั่งสำหรับการสร้าง คัดลอก ย้าย และลบไฟล์หรือไดเรกทอรีในระบบ Windows:

<style>
.w-manip-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:16px;}
.w-manip-card{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:20px;box-sizing:border-box;}
.w-manip-hdr{display:flex;align-items:center;gap:12px;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:10px;margin-bottom:12px;}
.w-manip-cmd{font-family:'JetBrains Mono',monospace;font-size:1.15rem;font-weight:800;color:#00f0ff;}
.w-manip-alias{font-size:0.75rem;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);padding:2px 6px;border-radius:4px;color:#94a3b8;}
.w-manip-desc{font-size:0.86rem;color:#cbd5e1;margin:0 0 10px;line-height:1.6;}
.w-manip-tbl{width:100%;border-collapse:collapse;margin-top:8px;}
.w-manip-tbl th{padding:6px 12px;font-size:0.75rem;color:#8a94a6;text-align:left;border-bottom:1px solid rgba(255,255,255,0.06);text-transform:uppercase;letter-spacing:0.04em;}
.w-manip-tbl td{padding:8px 12px;font-size:0.82rem;border-bottom:1px solid rgba(255,255,255,0.04);vertical-align:top;}
.w-manip-tbl tr:last-child td{border-bottom:none;}
.w-manip-tbl td:first-child{font-family:'JetBrains Mono',monospace;color:#fbbf24;font-weight:700;width:160px;}
.w-manip-tbl td:last-child{color:#94a3b8;line-height:1.5;}
.w-manip-example{background:rgba(7,9,16,0.6);border:1px solid rgba(255,255,255,0.05);border-radius:6px;padding:8px 12px;font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#3ddc84;margin-top:10px;}
</style>

<div class="w-manip-wrap">
<!-- dir -->
<div class="w-manip-card">
<div class="w-manip-hdr">
<span class="w-manip-cmd">dir [path]</span>
<span class="w-manip-alias">Built-in Command</span>
</div>
<p class="w-manip-desc">แสดงรายชื่อไฟล์และโฟลเดอร์ย่อยในตำแหน่งโฟลเดอร์ปัจจุบันหรือตามพาธที่กำหนด</p>
<table class="w-manip-tbl">
<thead><tr><th>Option / Switch</th><th>Description (คุณลักษณะการแสดงผล)</th></tr></thead>
<tbody>
<tr><td>/a (all attributes)</td><td>แสดงไฟล์ทั้งหมด รวมถึงไฟล์ซ่อน (Hidden) และไฟล์ระบบ (System)</td></tr>
<tr><td>/a:d /a:h /a:r</td><td>คัดกรองตามแอตทริบิวต์: <code>d</code> = โฟลเดอร์, <code>h</code> = ไฟล์ซ่อน, <code>r</code> = อ่านอย่างเดียว (Read-only)</td></tr>
<tr><td>/o:d /o:e /o:n /o:s</td><td>เรียงลำดับผลลัพธ์: <code>d</code> = ตามเวลา, <code>e</code> = นามสกุลไฟล์, <code>n</code> = ตามชื่อ, <code>s</code> = ตามขนาด</td></tr>
<tr><td>/s "[string]"</td><td>ค้นหาและสแกนหาคำที่ระบุในโฟลเดอร์ปัจจุบันและโฟลเดอร์ย่อยทั้งหมด</td></tr>
<tr><td>/w /l</td><td><code>/w</code> แสดงผลแนวกว้าง (Wide), <code>/l</code> แสดงผลชื่อเป็นตัวพิมพ์เล็กทั้งหมด</td></tr>
<tr><td>/t:c /t:a /t:w</td><td>แสดงช่องเวลาและจัดเรียง: <code>c</code> = เวลาสร้าง, <code>a</code> = เข้าใช้ล่าสุด, <code>w</code> = เขียนทับล่าสุด</td></tr>
</tbody>
</table>
</div>

<!-- cd -->
<div class="w-manip-card">
<div class="w-manip-hdr">
<span class="w-manip-cmd">cd [path]</span>
<span class="w-manip-alias">Alias: chdir</span>
</div>
<p class="w-manip-desc">แสดงตำแหน่งไดเรกทอรีปัจจุบัน หรือสั่งเปลี่ยนเส้นทางการทำงานไปยังไดเรกทอรีใหม่ (เหมือนคำสั่ง <code>cd</code> ใน Linux)</p>
<div class="w-manip-example">C:\\Users&gt; cd Documents<br>C:\\Users\\Documents&gt;</div>
</div>

<!-- mkdir -->
<div class="w-manip-card">
<div class="w-manip-hdr">
<span class="w-manip-cmd">mkdir [dir_name]</span>
<span class="w-manip-alias">Alias: md</span>
</div>
<p class="w-manip-desc">สร้างไดเรกทอรี (โฟลเดอร์) ใหม่ขึ้นมาในระบบไฟล์</p>
<div class="w-manip-example">C:\\Users&gt; mkdir test_folder</div>
</div>

<!-- copy & move -->
<div class="w-manip-card">
<div class="w-manip-hdr">
<span class="w-manip-cmd">copy [src] [dst] / move [src] [dst]</span>
<span class="w-manip-alias">File Transfer</span>
</div>
<p class="w-manip-desc"><strong>copy</strong> ทำการคัดลอกไฟล์ปัจจุบันไปยังโฟลเดอร์หรือตั้งชื่อใหม่ / <strong>move</strong> สั่งย้ายตำแหน่งไฟล์ และเปลี่ยนชื่อไฟล์ปลายทางพร้อมลบไฟล์ต้นฉบับออก</p>
<div class="w-manip-example">C:\\Users&gt; move .\\data.txt C:\\temp\\info.txt</div>
</div>

<!-- del -->
<div class="w-manip-card">
<div class="w-manip-hdr">
<span class="w-manip-cmd">del [file_path]</span>
<span class="w-manip-alias">Alias: erase</span>
</div>
<p class="w-manip-desc">สั่งลบไฟล์ข้อมูลที่ระบุออกจากสารบบระบบย่อย</p>
<table class="w-manip-tbl">
<thead><tr><th>Option / Switch</th><th>Description</th></tr></thead>
<tbody>
<tr><td>/s [keyword]</td><td>ค้นหาและลบไฟล์เป้าหมายตามคีย์เวิร์ดในทุกโฟลเดอร์ย่อย (e.g. <code>del /s test*</code>)</td></tr>
<tr><td>/a:h /a:r</td><td>เลือกลบไฟล์ที่มีแอตทริบิวต์ซ่อนอยู่ (<code>h</code>) หรือไฟล์อ่านอย่างเดียว (<code>r</code>)</td></tr>
</tbody>
</table>
</div>
</div>"""
})

blocks_195.append({"type": "markdown", "value": "---"})

# Block 9: File Examining & Printing Commands (type, echo, findstr, more, comp, sort)
blocks_195.append({
    "type": "markdown",
    "value": """### 📄 File Examining & Printing Commands

กลุ่มคำสั่งสำหรับใช้อ่านข้อมูล ค้นหาข้อความ คัดกรอง และเปรียบเทียบเนื้อหาภายในไฟล์:

<div class="w-manip-wrap">
<!-- type -->
<div class="w-manip-card">
<div class="w-manip-hdr">
<span class="w-manip-cmd">type [file_path]</span>
<span class="w-manip-alias">Same as 'cat' in Linux</span>
</div>
<p class="w-manip-desc">แสดงเนื้อหาหรือพิมพ์ข้อมูลในไฟล์ข้อความ (Text File) ออกมาบนหน้าต่างคอนโซลโดยตรง</p>
<div class="w-manip-example">C:\\Users&gt; type .\\config.txt</div>
</div>

<!-- echo -->
<div class="w-manip-card">
<div class="w-manip-hdr">
<span class="w-manip-cmd">echo [message | ON | OFF]</span>
<span class="w-manip-alias">Echoing</span>
</div>
<p class="w-manip-desc">แสดงข้อความ ตัวแปรระบบ หรือสั่งเปิด/ปิดการแสดงผลบรรทัดรับคำสั่งบนหน้าจอ Command Prompt</p>
<div class="w-manip-example">C:\\Users&gt; echo %OS%<br>Windows_NT</div>
</div>

<!-- findstr -->
<div class="w-manip-card">
<div class="w-manip-hdr">
<span class="w-manip-cmd">findstr [pattern] [file]</span>
<span class="w-manip-alias">Same as 'grep' in Linux</span>
</div>
<p class="w-manip-desc">สแกนและค้นหาบรรทัดที่มีคำหรือข้อความที่ระบุอยู่ภายในไฟล์ข้อมูลหนึ่งหรือหลายไฟล์</p>
<table class="w-manip-tbl">
<thead><tr><th>Option / Switch</th><th>Description</th></tr></thead>
<tbody>
<tr><td>/r "[regex]"</td><td>ใช้ Regular Expressions ในการกำหนดรูปแบบคำค้นหา</td></tr>
<tr><td>/s</td><td>ค้นหาและประมวลผลคำดังกล่าวในโฟลเดอร์ปัจจุบันรวมถึงโฟลเดอร์ย่อยทั้งหมด</td></tr>
<tr><td>/i</td><td>กำหนดให้การค้นหาไม่สนใจตัวอักษรพิมพ์เล็กหรือพิมพ์ใหญ่ (Case-Insensitive)</td></tr>
<tr><td>/n</td><td>แสดงหมายเลขบรรทัดกำกับหน้าข้อความที่พบคำค้นหา</td></tr>
</tbody>
</table>
</div>

<!-- more -->
<div class="w-manip-card">
<div class="w-manip-hdr">
<span class="w-manip-cmd">more [file]</span>
<span class="w-manip-alias">Pagination</span>
</div>
<p class="w-manip-desc">แสดงผลเนื้อหาไฟล์ทีละหนึ่งหน้าจอคอมพิวเตอร์ เหมาะสำหรับอ่านล็อกที่มีขนาดบรรทัดยาวมาก</p>
<table class="w-manip-tbl">
<thead><tr><th>Option / Switch</th><th>Description</th></tr></thead>
<tbody>
<tr><td>/c</td><td>สั่งล้างหน้าจอคอนโซล (Clear Screen) ก่อนทำการวาดผลลัพธ์หน้าถัดไป</td></tr>
</tbody>
</table>
</div>

<!-- comp & sort -->
<div class="w-manip-card">
<div class="w-manip-hdr">
<span class="w-manip-cmd">comp [file1] [file2] / sort [file]</span>
<span class="w-manip-alias">Compare & Sort</span>
</div>
<p class="w-manip-desc"><strong>comp</strong> เปรียบเทียบเนื้อหาของสองไฟล์และชี้จุดต่างเป็นรายบรรทัด / <strong>sort</strong> แสดงผลลัพธ์โดยการเรียงลำดับอักษรในไฟล์จาก A-Z หรือสลับ Z-A</p>
<table class="w-manip-tbl">
<thead><tr><th>sort Option</th><th>Description</th></tr></thead>
<tbody>
<tr><td>/r</td><td>เรียงลำดับเนื้อหาจากหลังมาหน้าแบบย้อนกลับ (Reverse / Descending)</td></tr>
<tr><td>/t [path]</td><td>กำหนดพาธไดเรกทอรีสำหรับใช้เขียนไฟล์ชั่วคราวขณะประมวลผลการจัดเรียงขนาดใหญ่</td></tr>
</tbody>
</table>
</div>
</div>"""
})

blocks_195.append({"type": "markdown", "value": "---"})

# Block 11: Frequently Used Commands (28 commands grid reference)
blocks_195.append({
    "type": "markdown",
    "value": """### 🛠️ Frequently Used Windows Commands Reference

ตารางสรุปชุดคำสั่งลัดและคำสั่งระบบที่ถูกเรียกใช้งานบ่อยที่สุดในการดูแลและสแกนระบบ Windows:

<style>
.w-freq-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.w-freq-card{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,0.2);}
.w-freq-tbl{width:100%;border-collapse:collapse;}
.w-freq-tbl th{padding:10px 14px;text-align:left;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.08em;font-weight:700;color:#8a94a6;background:rgba(255,255,255,0.01);border-bottom:1px solid rgba(255,255,255,0.06);}
.w-freq-tbl td{padding:10px 14px;border-bottom:1px solid rgba(255,255,255,0.04);font-size:0.83rem;vertical-align:top;line-height:1.5;}
.w-freq-tbl tr:last-child td{border-bottom:none;}
.w-freq-tbl tr:hover td{background:rgba(255,255,255,0.015);}
.w-freq-tbl td:first-child{font-family:'JetBrains Mono',monospace;color:#00f0ff;font-weight:700;white-space:nowrap;width:180px;}
.w-freq-tbl td:last-child{color:#94a3b8;}
</style>

<div class="w-freq-wrap">
<div class="w-freq-card">
<table class="w-freq-tbl">
<thead><tr><th>Command</th><th>Description (สรุปหน้าที่การทำงานหลัก)</th></tr></thead>
<tbody>
<tr><td>chkdsk</td><td>ตรวจสอบความสมบูรณ์และซ่อมแซมจุดเสียทางโครงสร้างบนฮาร์ดดิสก์ (Check Disk)</td></tr>
<tr><td>cls</td><td>เคลียร์และล้างข้อความทั้งหมดออกจากหน้าต่าง Command Prompt (Clear Screen)</td></tr>
<tr><td>date / time</td><td>ตรวจสอบหรือตั้งค่าวันที่ปัจจุบัน / เวลาปัจจุบันของระบบปฏิบัติการ</td></tr>
<tr><td>exit</td><td>สั่งยกเลิกและปิดหน้าต่างโปรแกรม Command Prompt (cmd.exe) ปัจจุบัน</td></tr>
<tr><td>fc</td><td>เปรียบเทียบความต่างระหว่างสองไฟล์และแสดงความแตกต่างแบบอักษรต่ออักษร (File Compare)</td></tr>
<tr><td>find</td><td>ค้นหาคำหรือชุดอักษรเป้าหมายที่ระบุภายในไฟล์ข้อมูลหนึ่งหรือหลายไฟล์</td></tr>
<tr><td>help</td><td>แสดงคู่มือการใช้งานและรายละเอียดสวิตช์ควบคุมของแต่ละคำสั่งหลักในวินโดวส์</td></tr>
<tr><td>ipconfig</td><td>แสดงค่ากำหนดโปรโตคอลเครือข่าย TCP/IP (IP Address, Gateway, Subnet) ของทุกการ์ดแลน</td></tr>
<tr><td>net</td><td>คำสั่งอเนกประสงค์สำหรับตั้งค่าและดูนโยบายเครื่อง เช่น บัญชีผู้ใช้ สิทธิ์ และรหัสผ่านเครื่อง</td></tr>
<tr><td>openfiles</td><td>แสดงรายการไฟล์ระบบย่อยที่ถูกเปิดค้างไว้โดยผู้ใช้งานระยะไกลผ่านระบบแชร์ไฟล์</td></tr>
<tr><td>path</td><td>แสดงหรือตั้งค่าไดเรกทอรีที่ระบบจะวิ่งไปหาไฟล์โปรแกรม (executable) เพื่อเปิดรันงาน</td></tr>
<tr><td>print</td><td>ส่งไฟล์ข้อความที่ระบุเข้าไปยังคิวเครื่องพิมพ์ของ Windows</td></tr>
<tr><td>prompt</td><td>เปลี่ยนรูปแบบข้อความตัวแจ้งรับคำสั่งใน Command Prompt</td></tr>
<tr><td>rd / rmdir</td><td>สั่งลบโฟลเดอร์หรือสารบบปลายทางออกจากฮาร์ดดิสก์</td></tr>
<tr><td>ren / rename</td><td>เปลี่ยนชื่อไฟล์หรือกลุ่มไฟล์ข้อมูลเป้าหมาย</td></tr>
<tr><td>replace</td><td>ค้นหาและเขียนไฟล์ทับลงไปแทนที่ไฟล์เดิมในระบบย่อย</td></tr>
<tr><td>set</td><td>แสดงผล ตั้งค่าชั่วคราว หรือลบตัวแปรสภาพแวดล้อมระบบ (Environment Variables)</td></tr>
<tr><td>shutdown</td><td>สั่งปิดการทำงาน รีสตาร์ทเครื่อง หรือตั้งเวลานับถอยหลังในการดับเครื่องคอมพิวเตอร์</td></tr>
<tr><td>systeminfo</td><td>ดึงค่าและแสดงรายงานสรุปสเปกเครื่อง รุ่นโอเอส เมนบอร์ด แรม และแพตช์อัปเดตระบบ</td></tr>
<tr><td>tasklist</td><td>ดึงรายงานโปรเซส (Processes) และแอปพลิเคชันทั้งหมดที่กำลังทำงานอยู่ ณ ปัจจุบัน</td></tr>
<tr><td>taskkill</td><td>สั่งปิดหรือหยุดการประมวลผลโปรเซสเป้าหมายผ่านไอดีโปรเซส (PID) หรือชื่อไฟล์</td></tr>
<tr><td>title</td><td>เปลี่ยนป้ายชื่อหัวข้อตรงแถบวินโดว์ของโปรแกรม Command Prompt ที่กำลังรันอยู่</td></tr>
<tr><td>tree</td><td>วาดแผนภูมิต้นไม้แสดงโครงสร้างลำดับชั้นโฟลเดอร์ของดิสก์หรือพาธที่ระบุในรูปแบบกราฟิกตัวอักษร</td></tr>
<tr><td>ver</td><td>แสดงข้อมูลเวอร์ชันและ Build Number ล่าสุดของระบบปฏิบัติการ Windows</td></tr>
<tr><td>vol</td><td>แสดงชื่อป้ายกำกับระดับความจุ (Volume Label) และซีเรียลนัมเบอร์ของดิสก์ไดรฟ์นั้นๆ</td></tr>
<tr><td>xcopy</td><td>คัดลอกไฟล์และโครงสร้างโฟลเดอร์ย่อยทั้งหมดไปยังเป้าหมายปลายทางอย่างรวดเร็ว</td></tr>
</tbody>
</table>
</div>
</div>"""
})

blocks_195.append({"type": "markdown", "value": "---"})

# Block 13: DOS Terminal Output Examples (Interactive Terminal Tabbed Console Mockup)
blocks_195.append({
    "type": "markdown",
    "value": """### 💻 Live Command Prompt Terminal Examples

คลิกปุ่มคำสั่งด้านข้างเพื่อจำลองการพิมพ์และแสดงผลลัพธ์ (Terminal Output) ของคำสั่งที่ใช้งานบ่อยบนระบบ Windows:

<style>
.w-term-console-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;gap:20px;}
@media(max-width:820px){.w-term-console-wrap{flex-direction:column;}}
.w-console-tabs{flex-shrink:0;width:200px;display:flex;flex-direction:column;gap:8px;}
@media(max-width:820px){.w-console-tabs{width:100%;flex-direction:row;flex-wrap:wrap;}}
.w-console-tab-btn{padding:10px 14px;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);border-radius:6px;font-family:'JetBrains Mono',monospace;font-size:0.78rem;color:#94a3b8;cursor:pointer;text-align:left;transition:all 0.15s ease;display:flex;align-items:center;justify-content:between;}
.w-console-tab-btn:hover, .w-console-tab-btn.active{border-color:#00f0ff;color:#ffffff;background:rgba(0,240,255,0.05);box-shadow:0 0 10px rgba(0,240,255,0.15);}
.w-console-tab-btn::after{content:"▶";font-size:0.6rem;color:#64748b;}
.w-console-tab-btn:hover::after, .w-console-tab-btn.active::after{color:#00f0ff;}
@media(max-width:820px){.w-console-tab-btn::after{content:"";}}

.w-console-screen{flex:1;background:#05070f;border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:20px;box-shadow:0 12px 32px rgba(0,0,0,0.55);min-height:300px;box-sizing:border-box;}
.w-screen-bar{display:flex;gap:6px;margin-bottom:14px;border-bottom:1px solid rgba(255,255,255,0.05);padding-bottom:10px;}
.w-screen-prompt{font-family:'JetBrains Mono',monospace;font-size:0.85rem;color:#94a3b8;margin-bottom:8px;}
.w-screen-output{font-family:'JetBrains Mono',monospace;font-size:0.82rem;color:#3ddc84;line-height:1.6;white-space:pre-wrap;}
</style>

<div class="w-term-console-wrap">
<div class="w-console-tabs">
<button class="w-console-tab-btn active" onclick="showTermConsole('date', this)">C:\\&gt; date</button>
<button class="w-console-tab-btn" onclick="showTermConsole('net', this)">C:\\&gt; net</button>
<button class="w-console-tab-btn" onclick="showTermConsole('time', this)">C:\\&gt; time</button>
<button class="w-console-tab-btn" onclick="showTermConsole('path', this)">C:\\&gt; path</button>
<button class="w-console-tab-btn" onclick="showTermConsole('systeminfo', this)">C:\\&gt; systeminfo</button>
<button class="w-console-tab-btn" onclick="showTermConsole('ver', this)">C:\\&gt; ver</button>
<button class="w-console-tab-btn" onclick="showTermConsole('vol', this)">C:\\&gt; vol</button>
<button class="w-console-tab-btn" onclick="showTermConsole('tasklist', this)">C:\\&gt; tasklist</button>
</div>
<div class="w-console-screen">
<div class="w-screen-bar">
<div class="w-dot red"></div><div class="w-dot yellow"></div><div class="w-dot green"></div>
</div>
<div id="w-console-cmd" class="w-screen-prompt">C:\\Users\\User&gt; date</div>
<pre id="w-console-out" class="w-screen-output">The current date is: Thu 07/08/2026
Enter the new date: (mm-dd-yy)</pre>
</div>
</div>

<script>
const wConsoleOutputs = {
  'date': {
    cmd: 'C:\\\\Users\\\\User&gt; date',
    out: 'The current date is: Thu 07/08/2026\\nEnter the new date: (mm-dd-yy)'
  },
  'net': {
    cmd: 'C:\\\\Users\\\\User&gt; net',
    out: 'The syntax of this command is:\\n\\nNET\\n    [ ACCOUNTS | COMPUTER | CONFIG | CONTINUE | FILE | GROUP | HELP |\\n      HELPMSG | LOCALGROUP | PAUSE | SESSION | SHARE | START |\\n      STATISTICS | STOP | TIME | USE | USER | VIEW ]'
  },
  'time': {
    cmd: 'C:\\\\Users\\\\User&gt; time',
    out: 'The current time is: 11:32:15.84\\nEnter the new time:'
  },
  'path': {
    cmd: 'C:\\\\Users\\\\User&gt; path',
    out: 'PATH=C:\\\\Windows\\\\system32;C:\\\\Windows;C:\\\\Windows\\\\System32\\\\Wbem;C:\\\\Windows\\\\System32\\\\WindowsPowerShell\\\\v1.0\\\\;C:\\\\Program Files\\\\Git\\\\cmd;C:\\\\Users\\\\User\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python39\\\\'
  },
  'systeminfo': {
    cmd: 'C:\\\\Users\\\\User&gt; systeminfo',
    out: 'Host Name:                 WONGYOS-DESKTOP\\nOS Name:                   Microsoft Windows 10 Home\\nOS Version:                10.0.19045 N/A Build 19045\\nOS Manufacturer:           Microsoft Corporation\\nOS Configuration:          Standalone Workstation\\nOS Build Type:             Multiprocessor Free\\nSystem Boot Time:          07/08/2026, 09:12:45\\nRegistered Owner:          Wongyos\\nProduct ID:                00327-70000-00001-AA007\\nOriginal Install Date:     10/28/2020, 18:43:37'
  },
  'ver': {
    cmd: 'C:\\\\Users\\\\User&gt; ver',
    out: 'Microsoft Windows [Version 10.0.19045.2486]'
  },
  'vol': {
    cmd: 'C:\\\\Users\\\\User&gt; vol',
    out: ' Volume in drive C is Windows\\n Volume Serial Number is 2CC4-F411'
  },
  'tasklist': {
    cmd: 'C:\\\\Users\\\\User&gt; tasklist',
    out: 'Image Name                     PID Session Name        Session#    Mem Usage\\n========================= ======== ================ =========== ============\\nSystem Idle Process              0 Services                   0          8 K\\nSystem                           4 Services                   0      5,768 K\\nRegistry                       172 Services                   0     25,504 K\\nsmss.exe                       636 Services                   0        412 K\\ncsrss.exe                     1000 Services                   0      2,472 K\\nwininit.exe                   1032 Services                   0        684 K\\nexplorer.exe                  3420 Console                    1     98,412 K'
  }
};

function showTermConsole(key, element) {
const buttons = document.querySelectorAll('.w-console-tab-btn');
buttons.forEach(b => b.classList.remove('active'));
element.classList.add('active');

const data = wConsoleOutputs[key];
if (!data) return;

document.getElementById('w-console-cmd').innerHTML = data.cmd;
document.getElementById('w-console-out').textContent = data.out.replace(/\\\\n/g, '\\n');
}
</script>"""
})

blocks_195.append({"type": "markdown", "value": "---"})

# Block 15: Environment Variables (%PATH%, %PROMPT%, %TEMP%, %OS%, %USERPROFILE%)
blocks_195.append({
    "type": "markdown",
    "value": """### ⚙️ Windows Environment Variables

ตัวแปรสภาพแวดล้อม (Environment Variables) เป็นตัวแปรระดับระบบที่ใช้เก็บค่ารันไทม์ที่โปรแกรมและระบบใช้ร่วมกัน:

<style>
.w-env-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.w-env-card{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,0.2);}
.w-env-tbl{width:100%;border-collapse:collapse;}
.w-env-tbl th{padding:12px 16px;text-align:left;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.08em;font-weight:700;color:#8a94a6;background:rgba(255,255,255,0.01);border-bottom:1px solid rgba(255,255,255,0.06);}
.w-env-tbl td{padding:12px 16px;border-bottom:1px solid rgba(255,255,255,0.04);font-size:0.86rem;vertical-align:top;line-height:1.6;}
.w-env-tbl tr:last-child td{border-bottom:none;}
.w-env-tbl tr:hover td{background:rgba(255,255,255,0.015);}
.w-env-tbl td:first-child{font-family:'JetBrains Mono',monospace;font-size:0.9rem;color:#fbbf24;font-weight:800;white-space:nowrap;width:200px;}
.w-env-tbl td:last-child{color:#94a3b8;}
</style>

<div class="w-env-wrap">
<div class="w-env-card">
<table class="w-env-tbl">
<thead><tr><th>Variable Name</th><th>Description (บทบาทและคุณลักษณะการทำงาน)</th></tr></thead>
<tbody>
<tr>
<td>%PATH%</td>
<td>รายการพาธไดเรกทอรีที่ระบบจะใช้วิ่งไปค้นหาไฟล์โปรแกรมรันอัตโนมัติเมื่อป้อนชื่อคำสั่ง (หากโฟลเดอร์โปรแกรมไม่อยู่ใน %PATH% จะไม่สามารถสั่งรันจากตู้ CMD โดยตรงได้)</td>
</tr>
<tr>
<td>%PROMPT%</td>
<td>ตัวแปรเก็บรหัส Tokenized String ที่ระบุว่าจะให้หน้าจอ Command Prompt วาดป้ายตัวนำรับคำสั่งในลักษณะใด</td>
</tr>
<tr>
<td>%TEMP% / %TMP%</td>
<td>พาธไดเรกทอรีชั่วคราว (Temporary Directory) ที่โปรแกรมต่างๆ ใช้เขียนและบันทึกไฟล์ชั่วขณะระหว่างประมวลผล</td>
</tr>
<tr>
<td>%OS%</td>
<td>เก็บบันทึกข้อมูลระบุชื่อระบบปฏิบัติการหลักของโฮสต์เครื่องคอมพิวเตอร์ (ปกติคือ <code>Windows_NT</code>)</td>
</tr>
<tr>
<td>%USERPROFILE%</td>
<td>พาธเก็บข้อมูลโฮมโฟลเดอร์ของบัญชีผู้ใช้งานปัจจุบัน (เช่น <code>C:\\Users\\User</code>) ซึ่งใช้รวบรวมไฟล์และข้อมูลการตั้งค่าเฉพาะของบัญชีนั้น</td>
</tr>
</tbody>
</table>
</div>
</div>"""
})

blocks_195.append({"type": "markdown", "value": "---"})

# Block 17: FAQ / Q&A Accordion
blocks_195.append({
    "type": "markdown",
    "value": """### ❓ Questions & Answers (Q&A)

ไขข้อสงสัยเกี่ยวกับการใช้งานคำสั่ง DOS และการจัดการสภาพแวดล้อมระบบ Windows:

<div class="qa-wrap">

<div class="qa-item active">
<div class="qa-q" onclick="toggleQA(this)">1. คำสั่ง 'findstr' ใน Windows มีระดับการเทียบเคียงกับคำสั่งใดในฝั่ง Linux?</div>
<div class="qa-a">
คำสั่ง <code>findstr</code> ใน Windows มีคุณสมบัติเทียบเท่าและทำหน้าที่คล้ายกับคำสั่ง <code>grep</code> ในระบบปฏิบัติการ Linux โดยใช้สแกนค้นหาข้อความหรือประมวลผลด้วย <strong>Regular Expressions (/r)</strong> เพื่อคัดกรองข้อมูลล็อกหรือรายงานความปลอดภัยที่มีปริมาณบรรทัดขนาดใหญ่ได้ในเสี้ยววินาที
</div>
</div>

<div class="qa-item">
<div class="qa-q" onclick="toggleQA(this)">2. ทำไมตัวแปร %PATH% ถึงเป็นเป้าหมายสำคัญของการวิเคราะห์ภัยคุกคามทางไซเบอร์?</div>
<div class="qa-a">
เนื่องจากเมื่อพิมพ์คำสั่งใดๆ ลงใน CMD ระบบจะสแกนหาไฟล์โปรแกรมนั้นตามตำแหน่งโฟลเดอร์ใน %PATH% ทีละโฟลเดอร์ตามลำดับ แฮกเกอร์มักใช้ช่องโหว่โจมตีที่เรียกว่า <strong>DLL Hijacking</strong> หรือ <strong>Path Hijacking</strong> โดยการนำไฟล์โปรแกรมมัลแวร์ไปตั้งชื่อเดียวกับคำสั่งระบบแล้ววางไว้ในโฟลเดอร์ลำดับแรกๆ เพื่อหลอกให้ Windows เรียกเปิดรันมัลแวร์นั้นแทนคำสั่งระบบจริง
</div>
</div>

<div class="qa-item">
<div class="qa-q" onclick="toggleQA(this)">3. คำสั่ง 'tasklist' และ 'taskkill' ทำประโยชน์อย่างไรในการรับมือมัลแวร์เบื้องต้น?</div>
<div class="qa-a">
เมื่อเครื่องคอมพิวเตอร์ต้องสงสัยว่าติดมัลแวร์ นักวิเคราะห์ความปลอดภัยสามารถสั่งรัน <code>tasklist</code> เพื่อตรวจสอบรายชื่อกระบวนการทำงานที่ผิดปกติ (รวมถึง Services ที่แฝงตัวอยู่) และเมื่อตรวจพบโปรเซสเป้าหมายที่ต้องสงสัย สามารถใช้คำสั่ง <code>taskkill /f /im [process_name]</code> เพื่อบังคับปิด (Force Close) การทำงานของมัลแวร์นั้นได้ทันทีจาก Command Line
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

# ─── Write Lesson 195 to Database ───
new_lesson = TutorialLesson(
    id=195,
    module_id=33,
    title="06. คำสั่งควบคุมและตัวแปรสภาพแวดล้อมใน Windows (Windows DOS Commands & Environment)",
    content=json.dumps(blocks_195, ensure_ascii=False),
    position=6,
    challenge_id=None
)

db.session.add(new_lesson)
db.session.commit()
print("New Lesson 195 created and committed to the database!")
