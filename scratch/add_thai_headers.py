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

blocks = json.loads(lesson.content)

# ─── Block 3: File & Directory Manipulation (with Thai in headers) ───
b_file_dir = """### 📁 File and Directory Manipulation Commands

<style>
.cmd-table-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.cmd-section{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;overflow:hidden;margin-bottom:24px;box-shadow:0 4px 20px rgba(0,0,0,0.2);}
.cmd-section-header{padding:14px 20px;display:flex;align-items:center;gap:14px;border-bottom:1px solid rgba(255,255,255,0.06);}
.cmd-section-header .cmd-mono{font-family:'JetBrains Mono',monospace;font-size:1.1rem;font-weight:800;flex-shrink:0;}
.cmd-header-text{display:flex;flex-direction:column;gap:2px;}
.cmd-header-en{font-size:0.78rem;text-transform:uppercase;letter-spacing:0.1em;opacity:0.55;font-family:'JetBrains Mono',monospace;}
.cmd-header-th{font-size:0.83rem;font-weight:600;opacity:0.85;}
.sh-ls .cmd-section-header{background:rgba(0,240,255,0.04);}
.sh-ls .cmd-mono,.sh-ls .cmd-header-th{color:#00f0ff;}
.sh-pwd .cmd-section-header{background:rgba(61,220,132,0.04);}
.sh-pwd .cmd-mono,.sh-pwd .cmd-header-th{color:#3ddc84;}
.sh-cd .cmd-section-header{background:rgba(251,191,36,0.04);}
.sh-cd .cmd-mono,.sh-cd .cmd-header-th{color:#fbbf24;}
.sh-mkdir .cmd-section-header{background:rgba(171,32,253,0.04);}
.sh-mkdir .cmd-mono,.sh-mkdir .cmd-header-th{color:#ab20fd;}
.sh-cp .cmd-section-header{background:rgba(244,114,182,0.04);}
.sh-cp .cmd-mono,.sh-cp .cmd-header-th{color:#f472b6;}
.sh-mv .cmd-section-header{background:rgba(251,146,60,0.04);}
.sh-mv .cmd-mono,.sh-mv .cmd-header-th{color:#fb923c;}
.sh-rm .cmd-section-header{background:rgba(255,0,127,0.04);}
.sh-rm .cmd-mono,.sh-rm .cmd-header-th{color:#ff007f;}
.cmd-table{width:100%;border-collapse:collapse;}
.cmd-table th{padding:10px 16px;text-align:left;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.08em;font-weight:700;color:#8a94a6;background:rgba(255,255,255,0.01);border-bottom:1px solid rgba(255,255,255,0.05);}
.cmd-table td{padding:11px 16px;border-bottom:1px solid rgba(255,255,255,0.04);font-size:0.9rem;vertical-align:top;}
.cmd-table tr:last-child td{border-bottom:none;}
.cmd-table tr:hover td{background:rgba(255,255,255,0.02);}
.cmd-table td:first-child{font-family:'JetBrains Mono',monospace;font-size:0.88rem;white-space:nowrap;}
.cmd-table td:last-child{color:#94a3b8;line-height:1.6;}
.td-cyan{color:#00f0ff !important;}.td-green{color:#3ddc84 !important;}.td-amber{color:#fbbf24 !important;}.td-purple{color:#ab20fd !important;}.td-pink{color:#f472b6 !important;}.td-orange{color:#fb923c !important;}.td-red{color:#ff007f !important;}
.cmd-eg{display:block;margin-top:4px;font-size:0.82rem;color:#64748b;font-family:'JetBrains Mono',monospace;}
.cmd-eg::before{content:"e.g. ";color:#475569;}
</style>

<div class="cmd-table-wrap">

<div class="cmd-section sh-ls">
<div class="cmd-section-header">
<span class="cmd-mono">ls</span>
<div class="cmd-header-text">
<span class="cmd-header-en">list files and directories</span>
<span class="cmd-header-th">แสดงรายการไฟล์และโฟลเดอร์ใน directory ที่ระบุ</span>
</div>
</div>
<table class="cmd-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-cyan">ls [path]</td><td>แสดงรายการไฟล์และโฟลเดอร์ใน directory ที่ระบุ</td></tr>
<tr><td class="td-cyan">ls -l [path]</td><td>แสดงรายการแบบ long format (แสดงรายละเอียดสิทธิ์ ขนาด วันที่)<span class="cmd-eg">ls -l /home/kali</span></td></tr>
<tr><td class="td-cyan">ls -a [path]</td><td>แสดงไฟล์และโฟลเดอร์ทั้งหมด รวมถึงไฟล์ที่ซ่อนอยู่ (ขึ้นต้นด้วย .)</td></tr>
<tr><td class="td-cyan">ls -d [path]</td><td>แสดงเฉพาะ directory ไม่รวมไฟล์ภายใน</td></tr>
<tr><td class="td-cyan">ls -R [path]</td><td>แสดงรายการไฟล์ทั้งหมดซ้ำลงไปในทุก subdirectory (Recursive)</td></tr>
</table>
</div>

<div class="cmd-section sh-pwd">
<div class="cmd-section-header">
<span class="cmd-mono">pwd</span>
<div class="cmd-header-text">
<span class="cmd-header-en">print working directory</span>
<span class="cmd-header-th">แสดงเส้นทางแบบ absolute path ของ directory ที่ทำงานอยู่ขณะนี้</span>
</div>
</div>
<table class="cmd-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-green">pwd</td><td>แสดงเส้นทางแบบ absolute path จาก root ไปยัง directory ปัจจุบัน</td></tr>
</table>
</div>

<div class="cmd-section sh-cd">
<div class="cmd-section-header">
<span class="cmd-mono">cd</span>
<div class="cmd-header-text">
<span class="cmd-header-en">change directory</span>
<span class="cmd-header-th">เปลี่ยน directory ที่กำลังทำงานอยู่ไปยัง directory ที่ต้องการ</span>
</div>
</div>
<table class="cmd-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-amber">cd</td><td>เปลี่ยนไปยัง home directory ของผู้ใช้ปัจจุบัน</td></tr>
<tr><td class="td-amber">cd [path]</td><td>เปลี่ยนไปยัง directory ที่ระบุ</td></tr>
<tr><td class="td-amber">cd .[dir]</td><td>เปลี่ยนไปยัง subdirectory ที่อยู่ภายใน directory ปัจจุบัน<span class="cmd-eg">cd ./secret/passdir</span></td></tr>
<tr><td class="td-amber">cd ..</td><td>ย้อนกลับขึ้นไปยัง parent directory (directory ลำดับบน)</td></tr>
</table>
</div>

<div class="cmd-section sh-mkdir">
<div class="cmd-section-header">
<span class="cmd-mono">mkdir</span>
<div class="cmd-header-text">
<span class="cmd-header-en">make directory</span>
<span class="cmd-header-th">สร้าง directory ใหม่ในตำแหน่งที่ระบุ</span>
</div>
</div>
<table class="cmd-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-purple">mkdir [dir]</td><td>สร้าง directory ใหม่ตามชื่อที่ระบุ</td></tr>
</table>
</div>

<div class="cmd-section sh-cp">
<div class="cmd-section-header">
<span class="cmd-mono">cp</span>
<div class="cmd-header-text">
<span class="cmd-header-en">copy files</span>
<span class="cmd-header-th">คัดลอกไฟล์จากตำแหน่งต้นทางไปยังปลายทาง โดยไฟล์ต้นทางยังคงอยู่</span>
</div>
</div>
<table class="cmd-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-pink">cp [old] [new]</td><td>คัดลอกไฟล์ต้นทาง (old) ไปยังปลายทาง (new) โดยไฟล์ต้นทางยังคงอยู่</td></tr>
</table>
</div>

<div class="cmd-section sh-mv">
<div class="cmd-section-header">
<span class="cmd-mono">mv</span>
<div class="cmd-header-text">
<span class="cmd-header-en">move or rename file</span>
<span class="cmd-header-th">ย้ายไฟล์ไปยัง directory ใหม่ หรือเปลี่ยนชื่อไฟล์ (ไฟล์ต้นทางจะถูกลบ)</span>
</div>
</div>
<table class="cmd-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-orange">mv [old] [new]</td><td>เปลี่ยนชื่อไฟล์ หรือย้ายไฟล์ไปยัง directory ใหม่พร้อมลบต้นฉบับ<span class="cmd-eg">mv /usr/data.x /var/info.d</span></td></tr>
</table>
</div>

<div class="cmd-section sh-rm">
<div class="cmd-section-header">
<span class="cmd-mono">rm</span>
<div class="cmd-header-text">
<span class="cmd-header-en">remove files and directories</span>
<span class="cmd-header-th">ลบไฟล์หรือ directory ออกจากระบบ (ไม่สามารถกู้คืนได้)</span>
</div>
</div>
<table class="cmd-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-red">rm [file]</td><td>ลบไฟล์ที่ระบุออกจากระบบ</td></tr>
<tr><td class="td-red">rm -R [dir]</td><td>ลบ directory และทุกไฟล์/โฟลเดอร์ภายในแบบ Recursive<span class="cmd-eg">rm -R /home/kali/temp</span></td></tr>
</table>
</div>

</div>"""

# ─── Block 5: File Examining & Printing (with Thai in headers) ───
b_file_examine = """### 🔍 File Examining and Printing Commands

<style>
.cmd2-table-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.cmd2-section{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;overflow:hidden;margin-bottom:24px;box-shadow:0 4px 20px rgba(0,0,0,0.2);}
.cmd2-section-header{padding:14px 20px;display:flex;align-items:center;gap:14px;border-bottom:1px solid rgba(255,255,255,0.06);}
.cmd2-section-header .cmd2-mono{font-family:'JetBrains Mono',monospace;font-size:1.1rem;font-weight:800;flex-shrink:0;}
.cmd2-header-text{display:flex;flex-direction:column;gap:2px;}
.cmd2-header-en{font-size:0.78rem;text-transform:uppercase;letter-spacing:0.1em;opacity:0.55;font-family:'JetBrains Mono',monospace;}
.cmd2-header-th{font-size:0.83rem;font-weight:600;opacity:0.85;}
.sh2-cat .cmd2-section-header{background:rgba(0,240,255,0.04);}
.sh2-cat .cmd2-mono,.sh2-cat .cmd2-header-th{color:#00f0ff;}
.sh2-echo .cmd2-section-header{background:rgba(61,220,132,0.04);}
.sh2-echo .cmd2-mono,.sh2-echo .cmd2-header-th{color:#3ddc84;}
.sh2-grep .cmd2-section-header{background:rgba(251,191,36,0.04);}
.sh2-grep .cmd2-mono,.sh2-grep .cmd2-header-th{color:#fbbf24;}
.sh2-find .cmd2-section-header{background:rgba(171,32,253,0.04);}
.sh2-find .cmd2-mono,.sh2-find .cmd2-header-th{color:#ab20fd;}
.sh2-more .cmd2-section-header{background:rgba(244,114,182,0.04);}
.sh2-more .cmd2-mono,.sh2-more .cmd2-header-th{color:#f472b6;}
.sh2-diff .cmd2-section-header{background:rgba(251,146,60,0.04);}
.sh2-diff .cmd2-mono,.sh2-diff .cmd2-header-th{color:#fb923c;}
.sh2-sort .cmd2-section-header{background:rgba(255,0,127,0.04);}
.sh2-sort .cmd2-mono,.sh2-sort .cmd2-header-th{color:#ff007f;}
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

<div class="cmd2-section sh2-cat">
<div class="cmd2-section-header">
<span class="cmd2-mono">cat</span>
<div class="cmd2-header-text">
<span class="cmd2-header-en">print file contents on screen</span>
<span class="cmd2-header-th">แสดงเนื้อหาทั้งหมดของไฟล์ออกมาบนหน้าจอ Terminal ทีเดียวทั้งหมด</span>
</div>
</div>
<table class="cmd2-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="c2-cyan">cat [file]</td><td>แสดงเนื้อหาทั้งหมดของไฟล์บนหน้าจอ</td></tr>
</table>
</div>

<div class="cmd2-section sh2-echo">
<div class="cmd2-section-header">
<span class="cmd2-mono">echo</span>
<div class="cmd2-header-text">
<span class="cmd2-header-en">display text or variable</span>
<span class="cmd2-header-th">แสดงข้อความหรือค่าตัวแปร Environment Variable บนหน้าจอ</span>
</div>
</div>
<table class="cmd2-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="c2-green">echo "[text]"</td><td>แสดงข้อความที่ระบุออกมาบนหน้าจอ</td></tr>
<tr><td class="c2-green">echo $[var]</td><td>แสดงค่าของ Environment Variable ที่ระบุ<span class="cmd2-eg">echo $HOME</span></td></tr>
</table>
</div>

<div class="cmd2-section sh2-grep">
<div class="cmd2-section-header">
<span class="cmd2-mono">grep</span>
<div class="cmd2-header-text">
<span class="cmd2-header-en">search pattern and print matching lines</span>
<span class="cmd2-header-th">ค้นหาบรรทัดที่ตรงกับ pattern ที่ระบุในไฟล์ แล้วแสดงบรรทัดนั้นออกมา</span>
</div>
</div>
<table class="cmd2-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="c2-amber">grep "word" [file]</td><td>ค้นหาทุกบรรทัดที่มีคำ/pattern ที่ระบุในไฟล์</td></tr>
<tr><td class="c2-amber">grep -R "word" [path]</td><td>ค้นหาคำในทุกไฟล์ภายใน directory และ subdirectory แบบ Recursive<span class="cmd2-eg">grep -R "Wongyos"</span></td></tr>
<tr><td class="c2-amber">grep -i "word" [file]</td><td>ค้นหาแบบไม่สนตัวพิมพ์เล็ก-ใหญ่ (Case-insensitive)<span class="cmd2-eg">grep -i "fLaG" /var/data.txt</span></td></tr>
<tr><td class="c2-amber">grep -G "regex" [file]</td><td>ค้นหาด้วย Regular Expression (Basic Regex)<span class="cmd2-eg">grep -G "^[r]" /etc/passwd</span></td></tr>
</table>
</div>

<div class="cmd2-section sh2-find">
<div class="cmd2-section-header">
<span class="cmd2-mono">find</span>
<div class="cmd2-header-text">
<span class="cmd2-header-en">find files matching type or pattern</span>
<span class="cmd2-header-th">ค้นหาไฟล์หรือ directory ในระบบตาม pattern ชื่อ ประเภท หรือขนาดที่ระบุ</span>
</div>
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

<div class="cmd2-section sh2-more">
<div class="cmd2-section-header">
<span class="cmd2-mono">more</span>
<div class="cmd2-header-text">
<span class="cmd2-header-en">print file contents page by page</span>
<span class="cmd2-header-th">แสดงเนื้อหาไฟล์ทีละหน้าจอ เหมาะสำหรับไฟล์ขนาดใหญ่ที่มีเนื้อหาจำนวนมาก</span>
</div>
</div>
<table class="cmd2-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="c2-pink">more [file]</td><td>แสดงเนื้อหาไฟล์ทีละหน้า กด Space เพื่อเลื่อนหน้า กด q เพื่อออก<span class="cmd2-eg">more rockyou.txt</span></td></tr>
</table>
</div>

<div class="cmd2-section sh2-diff">
<div class="cmd2-section-header">
<span class="cmd2-mono">diff</span>
<div class="cmd2-header-text">
<span class="cmd2-header-en">compare two files and print differences</span>
<span class="cmd2-header-th">เปรียบเทียบสองไฟล์และแสดงเฉพาะบรรทัดที่มีความแตกต่างกัน</span>
</div>
</div>
<table class="cmd2-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="c2-orange">diff [file1] [file2]</td><td>วิเคราะห์ไฟล์สองไฟล์และแสดงเฉพาะบรรทัดที่แตกต่างกัน</td></tr>
</table>
</div>

<div class="cmd2-section sh2-sort">
<div class="cmd2-section-header">
<span class="cmd2-mono">sort</span>
<div class="cmd2-header-text">
<span class="cmd2-header-en">sort file lines</span>
<span class="cmd2-header-th">เรียงลำดับบรรทัดในไฟล์ตาม option ที่ระบุ เช่น ตัวอักษร ตัวเลข หรือย้อนกลับ</span>
</div>
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

blocks[3]['value'] = b_file_dir
blocks[5]['value'] = b_file_examine

lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=166).update({"content": lesson.content})
db.session.commit()
print("Thai descriptions added to all command section headers in blocks 3 and 5!")
