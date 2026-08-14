import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

lesson = db.session.query(TutorialLesson).filter_by(id=166).first()
if not lesson:
    print("Lesson 166 not found!")
    exit(1)

# ─────────────────────────────────────────────────────────────────────────────
# BLOCK 0 — Header
# ─────────────────────────────────────────────────────────────────────────────
b_header = """## 🐧 คำสั่งควบคุมไฟล์และจัดการสิทธิ์ใน Linux (Linux File & Permission Commands)

**Chapter 02: Cybersecurity Operating Systems**

---"""

# ─────────────────────────────────────────────────────────────────────────────
# BLOCK 1 — Unix Command Line Structure (annotated diagram)
# ─────────────────────────────────────────────────────────────────────────────
b_cmd_structure = """### 🖥️ Unix Command Line Structure

<style>
.cmd-struct-wrap{width:100%;max-width:1050px;margin:2rem auto;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:32px;box-shadow:inset 0 0 20px rgba(0,0,0,0.3);}
.cmd-display{display:flex;align-items:center;justify-content:center;font-family:'JetBrains Mono',monospace;font-size:1.7rem;font-weight:700;gap:0;margin-bottom:40px;flex-wrap:wrap;gap:8px;}
.cmd-token{padding:10px 16px;border-radius:8px;transition:all 0.25s ease;cursor:default;position:relative;}
.cmd-token:hover{transform:translateY(-4px);}
.cmd-token.type-prompt{color:#3ddc84;border:2px solid rgba(61,220,132,0.4);background:rgba(61,220,132,0.06);box-shadow:0 0 12px rgba(61,220,132,0.1);}
.cmd-token.type-cmd{color:#00f0ff;border:2px solid rgba(0,240,255,0.4);background:rgba(0,240,255,0.06);box-shadow:0 0 12px rgba(0,240,255,0.1);}
.cmd-token.type-opt{color:#fbbf24;border:2px solid rgba(251,191,36,0.4);background:rgba(251,191,36,0.06);box-shadow:0 0 12px rgba(251,191,36,0.1);}
.cmd-token.type-arg{color:#ab20fd;border:2px solid rgba(171,32,253,0.4);background:rgba(171,32,253,0.06);box-shadow:0 0 12px rgba(171,32,253,0.1);}
.cmd-token:hover.type-prompt{box-shadow:0 0 20px rgba(61,220,132,0.35);background:rgba(61,220,132,0.1);}
.cmd-token:hover.type-cmd{box-shadow:0 0 20px rgba(0,240,255,0.35);background:rgba(0,240,255,0.1);}
.cmd-token:hover.type-opt{box-shadow:0 0 20px rgba(251,191,36,0.35);background:rgba(251,191,36,0.1);}
.cmd-token:hover.type-arg{box-shadow:0 0 20px rgba(171,32,253,0.35);background:rgba(171,32,253,0.1);}
.cmd-legend{display:flex;gap:20px;flex-wrap:wrap;justify-content:center;}
.cmd-legend-item{display:flex;align-items:flex-start;gap:14px;padding:16px 20px;border-radius:10px;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);flex:1;min-width:180px;transition:all 0.2s ease;}
.cmd-legend-item:hover{background:rgba(255,255,255,0.04);transform:translateY(-2px);}
.cmd-legend-chip{font-family:'JetBrains Mono',monospace;font-size:0.9rem;font-weight:800;padding:6px 12px;border-radius:6px;white-space:nowrap;flex-shrink:0;}
.cmd-legend-chip.type-prompt{color:#3ddc84;background:rgba(61,220,132,0.1);border:1px solid rgba(61,220,132,0.3);}
.cmd-legend-chip.type-cmd{color:#00f0ff;background:rgba(0,240,255,0.1);border:1px solid rgba(0,240,255,0.3);}
.cmd-legend-chip.type-opt{color:#fbbf24;background:rgba(251,191,36,0.1);border:1px solid rgba(251,191,36,0.3);}
.cmd-legend-chip.type-arg{color:#ab20fd;background:rgba(171,32,253,0.1);border:1px solid rgba(171,32,253,0.3);}
.cmd-legend-text{font-size:0.88rem;color:#94a3b8;line-height:1.6;}
.cmd-legend-text strong{color:#ffffff;display:block;margin-bottom:4px;font-size:0.95rem;}
</style>

<div class="cmd-struct-wrap">
<div class="cmd-display">
<span class="cmd-token type-prompt">$</span>
<span class="cmd-token type-cmd">ls</span>
<span class="cmd-token type-opt">-la</span>
<span class="cmd-token type-arg">/home/kali</span>
</div>
<div class="cmd-legend">
<div class="cmd-legend-item">
<span class="cmd-legend-chip type-prompt">$</span>
<div class="cmd-legend-text"><strong>Prompt</strong>สัญลักษณ์บอกว่าระบบพร้อมรับคำสั่ง <code>$</code> = ผู้ใช้ทั่วไป, <code>#</code> = root</div>
</div>
<div class="cmd-legend-item">
<span class="cmd-legend-chip type-cmd">ls</span>
<div class="cmd-legend-text"><strong>Command</strong>ชื่อคำสั่งหลักที่ต้องการสั่งให้ระบบปฏิบัติการดำเนินการ</div>
</div>
<div class="cmd-legend-item">
<span class="cmd-legend-chip type-opt">-la</span>
<div class="cmd-legend-text"><strong>Options / Flags</strong>ตัวเลือกเพิ่มเติมที่ปรับเปลี่ยนพฤติกรรมของคำสั่ง นำหน้าด้วย <code>-</code> หรือ <code>--</code></div>
</div>
<div class="cmd-legend-item">
<span class="cmd-legend-chip type-arg">/home/kali</span>
<div class="cmd-legend-text"><strong>Arguments</strong>เป้าหมายที่คำสั่งจะทำงานด้วย เช่น ชื่อไฟล์ เส้นทาง หรือข้อความ</div>
</div>
</div>
</div>"""

# ─────────────────────────────────────────────────────────────────────────────
# BLOCK 2 — File & Directory Manipulation Commands
# ─────────────────────────────────────────────────────────────────────────────
b_file_dir = """### 📁 File and Directory Manipulation Commands

<style>
.cmd-table-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.cmd-section{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;overflow:hidden;margin-bottom:24px;box-shadow:0 4px 20px rgba(0,0,0,0.2);}
.cmd-section-header{padding:14px 20px;display:flex;align-items:center;gap:10px;border-bottom:1px solid rgba(255,255,255,0.06);}
.cmd-section-header span{font-family:'JetBrains Mono',monospace;font-size:1rem;font-weight:800;}
.cmd-section-header .cmd-name{font-size:0.78rem;text-transform:uppercase;letter-spacing:0.12em;opacity:0.6;font-family:inherit;}
.sh-ls .cmd-section-header{background:rgba(0,240,255,0.04);}
.sh-ls .cmd-section-header span{color:#00f0ff;}
.sh-pwd .cmd-section-header{background:rgba(61,220,132,0.04);}
.sh-pwd .cmd-section-header span{color:#3ddc84;}
.sh-cd .cmd-section-header{background:rgba(251,191,36,0.04);}
.sh-cd .cmd-section-header span{color:#fbbf24;}
.sh-mkdir .cmd-section-header{background:rgba(171,32,253,0.04);}
.sh-mkdir .cmd-section-header span{color:#ab20fd;}
.sh-cp .cmd-section-header{background:rgba(244,114,182,0.04);}
.sh-cp .cmd-section-header span{color:#f472b6;}
.sh-mv .cmd-section-header{background:rgba(251,146,60,0.04);}
.sh-mv .cmd-section-header span{color:#fb923c;}
.sh-rm .cmd-section-header{background:rgba(255,0,127,0.04);}
.sh-rm .cmd-section-header span{color:#ff007f;}
.cmd-table{width:100%;border-collapse:collapse;}
.cmd-table th{padding:10px 16px;text-align:left;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.08em;font-weight:700;color:#8a94a6;background:rgba(255,255,255,0.01);border-bottom:1px solid rgba(255,255,255,0.05);}
.cmd-table td{padding:11px 16px;border-bottom:1px solid rgba(255,255,255,0.04);font-size:0.9rem;vertical-align:top;}
.cmd-table tr:last-child td{border-bottom:none;}
.cmd-table tr:hover td{background:rgba(255,255,255,0.02);}
.cmd-table td:first-child{font-family:'JetBrains Mono',monospace;font-size:0.88rem;white-space:nowrap;}
.cmd-table td:last-child{color:#94a3b8;line-height:1.6;}
.td-cyan{color:#00f0ff !important;}
.td-green{color:#3ddc84 !important;}
.td-amber{color:#fbbf24 !important;}
.td-purple{color:#ab20fd !important;}
.td-pink{color:#f472b6 !important;}
.td-orange{color:#fb923c !important;}
.td-red{color:#ff007f !important;}
.cmd-eg{display:block;margin-top:4px;font-size:0.82rem;color:#64748b;font-family:'JetBrains Mono',monospace;}
.cmd-eg::before{content:"e.g. ";color:#475569;}
</style>

<div class="cmd-table-wrap">

<!-- ls -->
<div class="cmd-section sh-ls">
<div class="cmd-section-header">
<span>ls</span><span class="cmd-name">— list files and directories</span>
</div>
<table class="cmd-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-cyan">ls [path]</td><td>แสดงรายการไฟล์และโฟลเดอร์ใน directory ที่ระบุ</td></tr>
<tr><td class="td-cyan">ls -l [path]</td><td>แสดงรายการแบบ long format (แสดงรายละเอียดสิทธิ์ ขนาด วันที่)<span class="cmd-eg">ls -l /home/kali</span></td></tr>
<tr><td class="td-cyan">ls -a [path]</td><td>แสดงไฟล์และโฟลเดอร์ทั้งหมด รวมถึงไฟล์ที่ซ่อนอยู่ (ขึ้นต้นด้วย .)</td></tr>
<tr><td class="td-cyan">ls -d [path]</td><td>แสดงเฉพาะ directory ไม่รวมไฟล์ภายใน</td></tr>
<tr><td class="td-cyan">ls -h [path]</td><td>แสดงขนาดไฟล์ให้อ่านง่ายขึ้น (Human-Readable เช่น KB, MB, GB)</td></tr>
<tr><td class="td-cyan">ls -R [path]</td><td>แสดงรายการไฟล์ทั้งหมดซ้ำลงไปในทุก subdirectory (Recursive)</td></tr>
<tr><td class="td-cyan">ls -la [path]</td><td><strong>[รวม Flag]</strong> แสดงไฟล์ทั้งหมดรวมไฟล์ซ่อน + แบบรายละเอียด (ตัวอย่างในรูปไดอะแกรม)<span class="cmd-eg">ls -la /home/kali</span></td></tr>
<tr><td class="td-cyan">ls -lh [path]</td><td><strong>[รวม Flag]</strong> แสดงรายละเอียดแบบ long format + ขนาดไฟล์อ่านง่าย (B/KB/MB)</td></tr>
<tr><td class="td-cyan">ls -lah [path]</td><td><strong>[รวม Flag]</strong> รวมไฟล์ซ่อน + แบบรายละเอียด + ขนาดไฟล์อ่านง่าย (นิยมใช้บ่อยที่สุด)</td></tr>
</table>

<div style="background: rgba(0, 240, 255, 0.05); border-top: 1px solid rgba(0, 240, 255, 0.15); padding: 16px 20px; font-size: 0.88rem; line-height: 1.65;">
<div style="color: #00f0ff; font-weight: 800; font-size: 0.95rem; margin-bottom: 6px; display: flex; align-items: center; gap: 8px;">
💡 <span>เกร็ดความรู้: ทำไมถึงใช้ ls -la ในไดอะแกรมด้านบน? (การรวม Flag)</span>
</div>
<div style="color: #cbd5e1;">
ในระบบ Linux หากคำสั่งมี Short Flags (ตัวเลือกอักษรเดียว) หลายตัว เราสามารถ <strong>นำมารวมเขียนต่อกันหลังขีด (-) เพียงขีดเดียวได้ทันที</strong> โดยไม่ต้องพิมพ์แยกกัน:
<ul style="margin: 6px 0 8px 20px; padding: 0;">
<li><code>ls -l -a</code> ➡️ รวมเป็น <code style="color:#00f0ff;font-weight:700;">ls -la</code> หรือ <code style="color:#00f0ff;font-weight:700;">ls -al</code> (แสดงไฟล์ทั้งหมดรวมไฟล์ซ่อน + แบบรายละเอียด)</li>
<li><code>ls -l -h</code> ➡️ รวมเป็น <code style="color:#00f0ff;font-weight:700;">ls -lh</code> (แสดงรายละเอียด + ขนาดไฟล์อ่านง่าย)</li>
<li><code>ls -l -a -h</code> ➡️ รวมเป็น <code style="color:#00f0ff;font-weight:700;">ls -lah</code> (แสดงไฟล์ซ่อน + รายละเอียด + ขนาดอ่านง่าย)</li>
</ul>
<span style="font-size:0.82rem; color:#94a3b8;">*(หมายเหตุ: ลำดับการเรียงอักษรหลังขีดไม่มีผลต่อการทำงาน เช่น <code>ls -la</code> และ <code>ls -al</code> ให้ผลลัพธ์เหมือนกันทุกประการ)*</span>
</div>
</div>
</div>

<!-- pwd -->
<div class="cmd-section sh-pwd">
<div class="cmd-section-header">
<span>pwd</span><span class="cmd-name">— print working directory</span>
</div>
<table class="cmd-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-green">pwd</td><td>แสดงเส้นทางแบบ absolute path จาก root ไปยัง directory ปัจจุบัน</td></tr>
</table>
</div>

<!-- cd -->
<div class="cmd-section sh-cd">
<div class="cmd-section-header">
<span>cd</span><span class="cmd-name">— change directory</span>
</div>
<table class="cmd-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-amber">cd</td><td>เปลี่ยนไปยัง home directory ของผู้ใช้ปัจจุบัน</td></tr>
<tr><td class="td-amber">cd [path]</td><td>เปลี่ยนไปยัง directory ที่ระบุ</td></tr>
<tr><td class="td-amber">cd .[dir]</td><td>เปลี่ยนไปยัง subdirectory ที่อยู่ภายใน directory ปัจจุบัน<span class="cmd-eg">cd ./secret/passdir</span></td></tr>
<tr><td class="td-amber">cd ..</td><td>ย้อนกลับขึ้นไปยัง parent directory (directory ลำดับบน)</td></tr>
</table>
</div>

<!-- mkdir -->
<div class="cmd-section sh-mkdir">
<div class="cmd-section-header">
<span>mkdir</span><span class="cmd-name">— make directory</span>
</div>
<table class="cmd-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-purple">mkdir [dir]</td><td>สร้าง directory ใหม่ตามชื่อที่ระบุ</td></tr>
</table>
</div>

<!-- cp -->
<div class="cmd-section sh-cp">
<div class="cmd-section-header">
<span>cp</span><span class="cmd-name">— copy files</span>
</div>
<table class="cmd-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-pink">cp [old] [new]</td><td>คัดลอกไฟล์ต้นทาง (old) ไปยังปลายทาง (new) โดยไฟล์ต้นทางยังคงอยู่</td></tr>
</table>
</div>

<!-- mv -->
<div class="cmd-section sh-mv">
<div class="cmd-section-header">
<span>mv</span><span class="cmd-name">— move or rename file</span>
</div>
<table class="cmd-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-orange">mv [old] [new]</td><td>เปลี่ยนชื่อไฟล์ หรือย้ายไฟล์ไปยัง directory ใหม่พร้อมลบต้นฉบับ<span class="cmd-eg">mv /usr/data.x /var/info.d</span></td></tr>
</table>
</div>

<!-- rm -->
<div class="cmd-section sh-rm">
<div class="cmd-section-header">
<span>rm</span><span class="cmd-name">— remove files and directories</span>
</div>
<table class="cmd-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-red">rm [file]</td><td>ลบไฟล์ที่ระบุออกจากระบบ</td></tr>
<tr><td class="td-red">rm -R [dir]</td><td>ลบ directory และทุกไฟล์/โฟลเดอร์ภายในแบบ Recursive<span class="cmd-eg">rm -R /home/kali/temp</span></td></tr>
</table>
</div>

</div>"""

# ─────────────────────────────────────────────────────────────────────────────
# BLOCK 3 — File Examining & Printing Commands
# ─────────────────────────────────────────────────────────────────────────────
b_file_examine = """### 🔍 File Examining and Printing Commands

<style>
.cmd2-table-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.cmd2-section{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;overflow:hidden;margin-bottom:24px;box-shadow:0 4px 20px rgba(0,0,0,0.2);}
.cmd2-section-header{padding:14px 20px;display:flex;align-items:center;gap:10px;border-bottom:1px solid rgba(255,255,255,0.06);}
.cmd2-section-header span{font-family:'JetBrains Mono',monospace;font-size:1rem;font-weight:800;}
.cmd2-section-header .cmd2-name{font-size:0.78rem;text-transform:uppercase;letter-spacing:0.12em;opacity:0.6;font-family:inherit;}
.sh2-cat .cmd2-section-header{background:rgba(0,240,255,0.04);}
.sh2-cat .cmd2-section-header span{color:#00f0ff;}
.sh2-echo .cmd2-section-header{background:rgba(61,220,132,0.04);}
.sh2-echo .cmd2-section-header span{color:#3ddc84;}
.sh2-grep .cmd2-section-header{background:rgba(251,191,36,0.04);}
.sh2-grep .cmd2-section-header span{color:#fbbf24;}
.sh2-find .cmd2-section-header{background:rgba(171,32,253,0.04);}
.sh2-find .cmd2-section-header span{color:#ab20fd;}
.sh2-more .cmd2-section-header{background:rgba(244,114,182,0.04);}
.sh2-more .cmd2-section-header span{color:#f472b6;}
.sh2-diff .cmd2-section-header{background:rgba(251,146,60,0.04);}
.sh2-diff .cmd2-section-header span{color:#fb923c;}
.sh2-sort .cmd2-section-header{background:rgba(255,0,127,0.04);}
.sh2-sort .cmd2-section-header span{color:#ff007f;}
.cmd2-table{width:100%;border-collapse:collapse;}
.cmd2-table th{padding:10px 16px;text-align:left;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.08em;font-weight:700;color:#8a94a6;background:rgba(255,255,255,0.01);border-bottom:1px solid rgba(255,255,255,0.05);}
.cmd2-table td{padding:11px 16px;border-bottom:1px solid rgba(255,255,255,0.04);font-size:0.9rem;vertical-align:top;}
.cmd2-table tr:last-child td{border-bottom:none;}
.cmd2-table tr:hover td{background:rgba(255,255,255,0.02);}
.cmd2-table td:first-child{font-family:'JetBrains Mono',monospace;font-size:0.88rem;white-space:nowrap;}
.cmd2-table td:last-child{color:#94a3b8;line-height:1.6;}
.c2-cyan{color:#00f0ff !important;}.c2-green{color:#3ddc84 !important;}.c2-amber{color:#fbbf24 !important;}.c2-purple{color:#ab20fd !important;}.c2-pink{color:#f472b6 !important;}.c2-orange{color:#fb923c !important;}.c2-red{color:#ff007f !important;}
.cmd2-eg{display:block;margin-top:4px;font-size:0.82rem;color:#64748b;font-family:'JetBrains Mono',monospace;}
.cmd2-eg::before{content:"e.g. ";color:#475569;}
</style>

<div class="cmd2-table-wrap">

<!-- cat -->
<div class="cmd2-section sh2-cat">
<div class="cmd2-section-header">
<span>cat</span><span class="cmd2-name">— print file contents on screen</span>
</div>
<table class="cmd2-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="c2-cyan">cat [file]</td><td>แสดงเนื้อหาทั้งหมดของไฟล์บนหน้าจอ</td></tr>
</table>
</div>

<!-- echo -->
<div class="cmd2-section sh2-echo">
<div class="cmd2-section-header">
<span>echo</span><span class="cmd2-name">— display text or variable</span>
</div>
<table class="cmd2-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="c2-green">echo "[text]"</td><td>แสดงข้อความที่ระบุออกมาบนหน้าจอ</td></tr>
<tr><td class="c2-green">echo $[var]</td><td>แสดงค่าของ Environment Variable ที่ระบุ<span class="cmd2-eg">echo $HOME</span></td></tr>
</table>
</div>

<!-- grep -->
<div class="cmd2-section sh2-grep">
<div class="cmd2-section-header">
<span>grep</span><span class="cmd2-name">— search pattern and print matching lines</span>
</div>
<table class="cmd2-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="c2-amber">grep "word" [file]</td><td>ค้นหาทุกบรรทัดที่มีคำ/pattern ที่ระบุในไฟล์</td></tr>
<tr><td class="c2-amber">grep -R "word" [path]</td><td>ค้นหาคำในทุกไฟล์ภายใน directory และ subdirectory แบบ Recursive<span class="cmd2-eg">grep -R "Wongyos"</span></td></tr>
<tr><td class="c2-amber">grep -i "word" [file]</td><td>ค้นหาแบบไม่สนตัวพิมพ์เล็ก-ใหญ่ (Case-insensitive)<span class="cmd2-eg">grep -i "fLaG" /var/data.txt</span></td></tr>
<tr><td class="c2-amber">grep -G "regex" [file]</td><td>ค้นหาด้วย Regular Expression (Basic Regex)<span class="cmd2-eg">grep -G "^[r]" /etc/passwd</span></td></tr>
</table>
</div>

<!-- find -->
<div class="cmd2-section sh2-find">
<div class="cmd2-section-header">
<span>find</span><span class="cmd2-name">— find files matching type or pattern</span>
</div>
<table class="cmd2-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="c2-purple">find [path] -name "word"</td><td>ค้นหาไฟล์ที่ชื่อตรงกับคำที่ระบุ (Case-sensitive)<span class="cmd2-eg">find /home -name "*flag*"</span></td></tr>
<tr><td class="c2-purple">find [path] -iname "word"</td><td>ค้นหาไฟล์ที่ชื่อตรงกัน แบบไม่สนตัวพิมพ์เล็ก-ใหญ่<span class="cmd2-eg">find / -iname "flag"</span></td></tr>
<tr><td class="c2-purple">find [path] -type f</td><td>ค้นหาเฉพาะไฟล์ปกติ (Regular file)<span class="cmd2-eg">find / -type f -name "flag*.*"</span></td></tr>
<tr><td class="c2-purple">find [path] -type d</td><td>ค้นหาเฉพาะ Directory</td></tr>
<tr><td class="c2-purple">find [path] -regex "regex"</td><td>ค้นหาไฟล์หรือ directory ด้วย Regular Expression<span class="cmd2-eg">find / -regex "\.\/f[0-9]"</span></td></tr>
<tr><td class="c2-purple">find [path] -size [n]c/k/M/G</td><td>ค้นหาไฟล์ตามขนาด (c=bytes, k=KB, M=MB, G=GB)<span class="cmd2-eg">find / -size 1024c</span></td></tr>
</table>
</div>

<!-- more -->
<div class="cmd2-section sh2-more">
<div class="cmd2-section-header">
<span>more</span><span class="cmd2-name">— print file contents page by page</span>
</div>
<table class="cmd2-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="c2-pink">more [file]</td><td>แสดงเนื้อหาไฟล์ทีละหน้า กด Space เพื่อเลื่อนหน้า กด q เพื่อออก<span class="cmd2-eg">more rockyou.txt</span></td></tr>
</table>
</div>

<!-- diff -->
<div class="cmd2-section sh2-diff">
<div class="cmd2-section-header">
<span>diff</span><span class="cmd2-name">— compare two files and print differences</span>
</div>
<table class="cmd2-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="c2-orange">diff [file1] [file2]</td><td>วิเคราะห์ไฟล์สองไฟล์และแสดงเฉพาะบรรทัดที่แตกต่างกัน</td></tr>
</table>
</div>

<!-- sort -->
<div class="cmd2-section sh2-sort">
<div class="cmd2-section-header">
<span>sort</span><span class="cmd2-name">— sort file lines</span>
</div>
<table class="cmd2-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="c2-red">sort [file]</td><td>เรียงบรรทัดในไฟล์จากน้อยไปมาก (Ascending order)</td></tr>
<tr><td class="c2-red">sort -d [file]</td><td>เรียงตามลำดับพจนานุกรม (Dictionary order)</td></tr>
<tr><td class="c2-red">sort -f [file]</td><td>เรียงโดยไม่สนตัวพิมพ์เล็ก-ใหญ่ (Case-insensitive)</td></tr>
<tr><td class="c2-red">sort -r [file]</td><td>เรียงจากมากไปน้อย (Descending / Reverse order)</td></tr>
</table>
</div>

</div>"""

# ─────────────────────────────────────────────────────────────────────────────
# BUILD & SAVE
# ─────────────────────────────────────────────────────────────────────────────
blocks = [
    {"type": "markdown", "value": b_header},
    {"type": "markdown", "value": b_cmd_structure},
    {"type": "markdown", "value": "---"},
    {"type": "markdown", "value": b_file_dir},
    {"type": "markdown", "value": "---"},
    {"type": "markdown", "value": b_file_examine},
]

lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=166).update({"content": lesson.content})
db.session.commit()

print(f"Lesson 166 rebuilt successfully! Total blocks: {len(blocks)}")
for i, b in enumerate(blocks):
    print(f"  Block {i}: {len(b['value'])} chars — {b['value'][:60].replace(chr(10),' ')}")
