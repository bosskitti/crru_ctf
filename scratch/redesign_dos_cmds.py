import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l168 = db.session.query(TutorialLesson).filter_by(id=168).first()
blocks = json.loads(l168.content)

# ─── 1. DOS Command Line Structure (Block 31) ───
blocks[31]['value'] = """### 🖥️ DOS Command Line Structure

<style>
.dos-struct-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.dos-terminal{background:#070910;border-radius:10px;overflow:hidden;border:1px solid rgba(255,255,255,0.08);box-shadow:0 8px 32px rgba(0,0,0,0.5);margin-bottom:16px;}
.dos-titlebar{background:rgba(28,30,44,0.98);padding:9px 16px;display:flex;align-items:center;gap:8px;border-bottom:1px solid rgba(255,255,255,0.05);}
.dos-dot{width:11px;height:11px;border-radius:50%;}
.dos-dot.r{background:#ff5f57;}.dos-dot.y{background:#ffbd2e;}.dos-dot.g{background:#28c840;}
.dos-title{flex:1;text-align:center;font-size:0.75rem;color:#8a94a6;font-family:'JetBrains Mono',monospace;letter-spacing:0.06em;}
.dos-pre{background:transparent;margin:0;padding:24px 28px;font-family:'JetBrains Mono','Courier New',monospace;font-size:0.95rem;line-height:2.0;white-space:pre;overflow-x:auto;border:none;}
.d-prompt{color:#fbbf24;}.d-cmd{color:#00f0ff;}.d-opt{color:#ff007f;}.d-arg{color:#3ddc84;}
</style>

<div class="dos-struct-wrap">
<div class="dos-terminal">
<div class="dos-titlebar">
<span class="dos-dot r"></span><span class="dos-dot y"></span><span class="dos-dot g"></span>
<span class="dos-title">Command Prompt (cmd.exe)</span>
</div>
<pre class="dos-pre"><span class="d-prompt">C:\\Users&gt;</span> <span class="d-cmd">dir</span> <span class="d-opt">/a</span> <span class="d-arg">C:\\</span>█
│          │   │  │
│          │   │  └── Arguments & Path — เป้าหมายที่ต้องการค้นหา
│          │   └───── Options (Flags) — ตัวเลือกเพิ่มเติมเพื่อแสดงไฟล์ทั้งหมด (รวมไฟล์ซ่อน)
│          └───────── Command — ชื่อคำสั่งหลัก (แสดงรายชื่อไฟล์/โฟลเดอร์)
└──────────────────── Prompt with Path — ตำแหน่งโฟลเดอร์ปัจจุบันที่ระบบทำงานอยู่</pre>
</div>
</div>"""

# ─── 2. Combine Block 33 to 44: File and Directory Manipulation Commands (Block 33) ───
blocks[33]['value'] = """### 📁 File and Directory Manipulation Commands

<style>
.dos-tbl-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.dos-tbl-section{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;overflow:hidden;margin-bottom:24px;box-shadow:0 4px 20px rgba(0,0,0,0.2);}
.dos-tbl-header{padding:14px 20px;display:flex;align-items:center;gap:14px;border-bottom:1px solid rgba(255,255,255,0.06);}
.dos-tbl-mono{font-family:'JetBrains Mono',monospace;font-size:1.1rem;font-weight:800;flex-shrink:0;}
.dos-tbl-text{display:flex;flex-direction:column;gap:2px;}
.dos-tbl-en{font-size:0.78rem;text-transform:uppercase;letter-spacing:0.1em;opacity:0.55;font-family:'JetBrains Mono',monospace;}
.dos-tbl-th{font-size:0.83rem;font-weight:600;opacity:0.85;}
.sh-dir .dos-tbl-header{background:rgba(0,240,255,0.04);}.sh-dir .dos-tbl-mono,.sh-dir .dos-tbl-th{color:#00f0ff;}
.sh-cd .dos-tbl-header{background:rgba(61,220,132,0.04);}.sh-cd .dos-tbl-mono,.sh-cd .dos-tbl-th{color:#3ddc84;}
.sh-mkdir .dos-tbl-header{background:rgba(251,191,36,0.04);}.sh-mkdir .dos-tbl-mono,.sh-mkdir .dos-tbl-th{color:#fbbf24;}
.sh-copy .dos-tbl-header{background:rgba(171,32,253,0.04);}.sh-copy .dos-tbl-mono,.sh-copy .dos-tbl-th{color:#ab20fd;}
.sh-move .dos-tbl-header{background:rgba(244,114,182,0.04);}.sh-move .dos-tbl-mono,.sh-move .dos-tbl-th{color:#f472b6;}
.sh-del .dos-tbl-header{background:rgba(255,0,127,0.04);}.sh-del .dos-tbl-mono,.sh-del .dos-tbl-th{color:#ff007f;}
.dos-table{width:100%;border-collapse:collapse;}
.dos-table th{padding:10px 16px;text-align:left;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.08em;font-weight:700;color:#8a94a6;background:rgba(255,255,255,0.01);border-bottom:1px solid rgba(255,255,255,0.05);}
.dos-table td{padding:11px 16px;border-bottom:1px solid rgba(255,255,255,0.04);font-size:0.9rem;vertical-align:top;}
.dos-table tr:last-child td{border-bottom:none;}
.dos-table tr:hover td{background:rgba(255,255,255,0.02);}
.dos-table td:first-child{font-family:'JetBrains Mono',monospace;font-size:0.88rem;white-space:nowrap;}
.dos-table td:last-child{color:#94a3b8;line-height:1.6;}
.td-cyan{color:#00f0ff !important;}.td-green{color:#3ddc84 !important;}.td-amber{color:#fbbf24 !important;}.td-purple{color:#ab20fd !important;}.td-pink{color:#f472b6 !important;}.td-red{color:#ff007f !important;}
.dos-eg{display:block;margin-top:4px;font-size:0.82rem;color:#64748b;font-family:'JetBrains Mono',monospace;}
.dos-eg::before{content:"e.g. ";color:#475569;}
</style>

<div class="dos-tbl-wrap">

<!-- dir -->
<div class="dos-tbl-section sh-dir">
<div class="dos-tbl-header">
<span class="dos-tbl-mono">dir</span>
<div class="dos-tbl-text">
<span class="dos-tbl-en">directory — list files and folders</span>
<span class="dos-tbl-th">แสดงรายการไฟล์และโฟลเดอร์ในไดเรกทอรีปัจจุบันหรือระบุ (เหมือน ls ใน Linux)</span>
</div>
</div>
<table class="dos-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-cyan">dir [path]</td><td>แสดงรายชื่อไฟล์และโฟลเดอร์จากเส้นทางที่ระบุ</td></tr>
<tr><td class="td-cyan">dir /a</td><td>แสดงไฟล์และโฟลเดอร์ทั้งหมด รวมถึงไฟล์ที่ซ่อนอยู่ (Hidden files)</td></tr>
<tr><td class="td-cyan">dir /o:[d|e|n|s]</td><td>เรียงลำดับไฟล์ตามเงื่อนไข: d=วันที่, e=นามสกุล, n=ชื่อ, s=ขนาดไฟล์<span class="dos-eg">dir /o:d</span></td></tr>
<tr><td class="td-cyan">dir /l</td><td>แสดงรายชื่อไฟล์และโฟลเดอร์เป็นตัวพิมพ์เล็กทั้งหมด (Lower case)</td></tr>
<tr><td class="td-cyan">dir /t:[c|a|w]</td><td>เรียงเวลาตาม: c=เวลาสร้าง (Created), a=เข้าถึงล่าสุด (Accessed), w=แก้ไขล่าสุด (Written)</td></tr>
</table>
</div>

<!-- cd -->
<div class="dos-tbl-section sh-cd">
<div class="dos-tbl-header">
<span class="dos-tbl-mono">cd / chdir</span>
<div class="dos-tbl-text">
<span class="dos-tbl-en">change directory — change working folder</span>
<span class="dos-tbl-th">แสดงหรือเปลี่ยนตำแหน่งโฟลเดอร์ที่กำลังทำงานอยู่ในปัจจุบัน</span>
</div>
</div>
<table class="dos-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-green">cd</td><td>แสดงที่อยู่ของโฟลเดอร์ปัจจุบันที่กำลังทำงานอยู่ (เหมือน pwd)</td></tr>
<tr><td class="td-green">cd [path]</td><td>ย้ายไปยังไดเรกทอรีหรือโฟลเดอร์ตามที่ระบุ</td></tr>
<tr><td class="td-green">cd ..</td><td>ย้อนกลับไป 1 ระดับโฟลเดอร์ (Parent folder)</td></tr>
</table>
</div>

<!-- mkdir -->
<div class="dos-tbl-section sh-mkdir">
<div class="dos-tbl-header">
<span class="dos-tbl-mono">md / mkdir</span>
<div class="dos-tbl-text">
<span class="dos-tbl-en">make directory — create folder</span>
<span class="dos-tbl-th">สร้างโฟลเดอร์ใหม่ตามชื่อที่ต้องการ</span>
</div>
</div>
<table class="dos-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-amber">mkdir [dir]</td><td>สร้างโฟลเดอร์ใหม่ในตำแหน่งปัจจุบัน</td></tr>
</table>
</div>

<!-- copy -->
<div class="dos-tbl-section sh-copy">
<div class="dos-tbl-header">
<span class="dos-tbl-mono">copy</span>
<div class="dos-tbl-text">
<span class="dos-tbl-en">copy files — copy source to destination</span>
<span class="dos-tbl-th">คัดลอกไฟล์จากตำแหน่งต้นทางไปยังปลายทาง โดยไม่ลบไฟล์เดิม (เหมือน cp)</span>
</div>
</div>
<table class="dos-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-purple">copy [src] [dst]</td><td>คัดลอกไฟล์ไปยังปลายทางที่กำหนด<span class="dos-eg">copy C:\\data.txt D:\\backup\\data.txt</span></td></tr>
</table>
</div>

<!-- move -->
<div class="dos-tbl-section sh-move">
<div class="dos-tbl-header">
<span class="dos-tbl-mono">move</span>
<div class="dos-tbl-text">
<span class="dos-tbl-en">move or rename files/folders</span>
<span class="dos-tbl-th">ย้ายไฟล์หรือเปลี่ยนชื่อไฟล์/โฟลเดอร์ ไปยังปลายทาง (ลบต้นฉบับ เหมือน mv)</span>
</div>
</div>
<table class="dos-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-pink">move [src] [dst]</td><td>ย้ายไฟล์หรือโฟลเดอร์ไปยังที่อยู่ใหม่ หรือเปลี่ยนชื่อไฟล์<span class="dos-eg">move old.txt new.txt</span></td></tr>
</table>
</div>

<!-- del -->
<div class="dos-tbl-section sh-del">
<div class="dos-tbl-header">
<span class="dos-tbl-mono">del / erase</span>
<div class="dos-tbl-text">
<span class="dos-tbl-en">delete files — remove files from disk</span>
<span class="dos-tbl-th">ลบไฟล์หนึ่งไฟล์หรือหลายไฟล์ออกจากพื้นที่ดิสก์ (ไม่สามารถกู้คืนผ่านถังขยะปกติได้)</span>
</div>
</div>
<table class="dos-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-red">del [file]</td><td>ลบไฟล์ที่ระบุออกทันที</td></tr>
<tr><td class="td-red">del /s [keyword]</td><td>ลบไฟล์ที่มีคำระบุในทุกโฟลเดอร์ย่อยย้อนกลับเข้าไป (Recursive)</td></tr>
</table>
</div>

</div>"""

# Clear blocks 34-44 since we merged them into block 33
for i in range(34, 45):
    blocks[i]['value'] = ""

l168.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=168).update({"content": l168.content})
db.session.commit()
print("DOS Command Line Structure and merged File/Dir Commands updated successfully!")
