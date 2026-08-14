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

# ─────────────────────────────────────────────────────────────────────────────
# BLOCK 6 — Separator + Heading
# ─────────────────────────────────────────────────────────────────────────────
b_sep2 = """---

### 🔐 File and Directory Permission Commands"""

# ─────────────────────────────────────────────────────────────────────────────
# BLOCK 7 — ls -l Output Annotation (Terminal + labeled columns)
# ─────────────────────────────────────────────────────────────────────────────
b_lsl = """#### 📋 ข้อมูลและรายละเอียดของไฟล์และ Directory (`ls -l`)

<style>
.lsl-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.lsl-terminal{background:#070910;border-radius:10px;overflow:hidden;border:1px solid rgba(255,255,255,0.08);box-shadow:0 8px 32px rgba(0,0,0,0.5);}
.lsl-titlebar{background:rgba(28,30,44,0.98);padding:9px 16px;display:flex;align-items:center;gap:8px;border-bottom:1px solid rgba(255,255,255,0.05);}
.lsl-dot{width:11px;height:11px;border-radius:50%;}
.lsl-dot.r{background:#ff5f57;}.lsl-dot.y{background:#ffbd2e;}.lsl-dot.g{background:#28c840;}
.lsl-title{flex:1;text-align:center;font-size:0.75rem;color:#8a94a6;font-family:'JetBrains Mono',monospace;letter-spacing:0.06em;}
.lsl-pre{background:transparent;margin:0;padding:20px 24px 8px;font-family:'JetBrains Mono','Courier New',monospace;font-size:0.88rem;line-height:1.9;white-space:pre;overflow-x:auto;border:none;}
.lsl-prompt{color:#3ddc84;}.lsl-cmd{color:#00f0ff;}
.lsl-perm{color:#fbbf24;}.lsl-link{color:#94a3b8;}.lsl-owner{color:#f472b6;}.lsl-group{color:#f472b6;}.lsl-size{color:#ab20fd;}.lsl-date{color:#3ddc84;}.lsl-name{color:#ffffff;}
.lsl-dir{color:#00f0ff;}.lsl-dim{color:#475569;}
.lsl-labels{display:flex;gap:0;padding:4px 24px 20px;overflow-x:auto;}
.lsl-col{display:flex;flex-direction:column;align-items:center;text-align:center;}
.lsl-vline{width:1px;background:rgba(255,255,255,0.1);flex-shrink:0;}
.lsl-chip{font-size:0.72rem;font-weight:700;padding:5px 9px;border-radius:6px;white-space:nowrap;border:1px solid;margin-top:4px;}
.lsl-chip-perm{color:#fbbf24;border-color:rgba(251,191,36,0.3);background:rgba(251,191,36,0.07);}
.lsl-chip-link{color:#94a3b8;border-color:rgba(148,163,184,0.3);background:rgba(148,163,184,0.05);}
.lsl-chip-own{color:#f472b6;border-color:rgba(244,114,182,0.3);background:rgba(244,114,182,0.07);}
.lsl-chip-size{color:#ab20fd;border-color:rgba(171,32,253,0.3);background:rgba(171,32,253,0.07);}
.lsl-chip-date{color:#3ddc84;border-color:rgba(61,220,132,0.3);background:rgba(61,220,132,0.07);}
.lsl-chip-name{color:#e2e8f0;border-color:rgba(226,232,240,0.2);background:rgba(226,232,240,0.04);}
.lsl-sub{font-size:0.68rem;color:#64748b;margin-top:3px;white-space:nowrap;}
.lsl-spacer{flex:1;min-width:4px;}
</style>

<div class="lsl-wrap">
<div class="lsl-terminal">
<div class="lsl-titlebar">
<span class="lsl-dot r"></span><span class="lsl-dot y"></span><span class="lsl-dot g"></span>
<span class="lsl-title">bash — root@wongyos:~/Desktop</span>
</div>
<pre class="lsl-pre"><span class="lsl-prompt">root@wongyos:~/Desktop#</span> <span class="lsl-cmd">ls -l</span>
<span class="lsl-dim">total 140516</span>
<span class="lsl-perm">-rwxrw-rw-</span> <span class="lsl-link">1</span> <span class="lsl-owner">root</span> <span class="lsl-group">root</span> <span class="lsl-size">  3942027</span> <span class="lsl-date">Mar 29  2018</span> <span class="lsl-name">20180329_130139.jpg</span>
<span class="lsl-perm">drwxr-xr-x</span> <span class="lsl-link">3</span> <span class="lsl-owner">root</span> <span class="lsl-group">root</span> <span class="lsl-size">      4096</span> <span class="lsl-date">Jul 27 10:27</span> <span class="lsl-dir">CTF-2018-07-03</span>
<span class="lsl-perm">drwxr-xr-x</span> <span class="lsl-link">2</span> <span class="lsl-owner">root</span> <span class="lsl-group">root</span> <span class="lsl-size">      4096</span> <span class="lsl-date">Sep 29 04:27</span> <span class="lsl-dir">CTF-2018-08-29</span>
<span class="lsl-perm">drwxr-xr-x</span> <span class="lsl-link">2</span> <span class="lsl-owner">root</span> <span class="lsl-group">root</span> <span class="lsl-size">      4096</span> <span class="lsl-date">Sep 29 04:23</span> <span class="lsl-dir">DE-2018-09-26</span>
<span class="lsl-perm">-rw-r--r--</span> <span class="lsl-link">1</span> <span class="lsl-owner">root</span> <span class="lsl-group">root</span> <span class="lsl-size">139921507</span> <span class="lsl-date">Jun 17 01:57</span> <span class="lsl-name">rockyou.txt</span>
<span class="lsl-perm">-rw-r--r--</span> <span class="lsl-link">1</span> <span class="lsl-owner">root</span> <span class="lsl-group">root</span> <span class="lsl-size">      4789</span> <span class="lsl-date">Oct 10 00:58</span> <span class="lsl-name">scan-2018-10-10.txt</span></pre>
<div class="lsl-labels">
<div class="lsl-col">
<div class="lsl-vline" style="height:24px;"></div>
<div class="lsl-chip lsl-chip-perm">type + permission</div>
<div class="lsl-sub">ประเภทและสิทธิ์</div>
</div>
<div class="lsl-spacer"></div>
<div class="lsl-col">
<div class="lsl-vline" style="height:24px;"></div>
<div class="lsl-chip lsl-chip-link">links</div>
<div class="lsl-sub">จำนวน Hard Link</div>
</div>
<div class="lsl-spacer"></div>
<div class="lsl-col">
<div class="lsl-vline" style="height:24px;"></div>
<div class="lsl-chip lsl-chip-own">owner</div>
<div class="lsl-sub">เจ้าของไฟล์</div>
</div>
<div class="lsl-spacer"></div>
<div class="lsl-col">
<div class="lsl-vline" style="height:24px;"></div>
<div class="lsl-chip lsl-chip-own">group</div>
<div class="lsl-sub">กลุ่มของไฟล์</div>
</div>
<div class="lsl-spacer"></div>
<div class="lsl-col">
<div class="lsl-vline" style="height:24px;"></div>
<div class="lsl-chip lsl-chip-size">size</div>
<div class="lsl-sub">ขนาดไฟล์ (bytes)</div>
</div>
<div class="lsl-spacer"></div>
<div class="lsl-col">
<div class="lsl-vline" style="height:24px;"></div>
<div class="lsl-chip lsl-chip-date">modified date</div>
<div class="lsl-sub">วันที่แก้ไขล่าสุด</div>
</div>
<div class="lsl-spacer"></div>
<div class="lsl-col">
<div class="lsl-vline" style="height:24px;"></div>
<div class="lsl-chip lsl-chip-name">file / directory name</div>
<div class="lsl-sub">ชื่อไฟล์หรือ Directory</div>
</div>
</div>
</div>
</div>"""

# ─────────────────────────────────────────────────────────────────────────────
# BLOCK 8 — Permission String Breakdown + Mode Table
# ─────────────────────────────────────────────────────────────────────────────
b_perm = """#### 🔑 โครงสร้าง Permission String และตาราง Permission Mode

<style>
.perm-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:24px;}
.perm-string-card{background:rgba(15,17,26,0.5);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:28px;box-shadow:0 4px 20px rgba(0,0,0,0.2);}
.perm-string-card h5{margin:0 0 20px;font-size:0.8rem;text-transform:uppercase;letter-spacing:0.1em;color:#64748b;}
.perm-boxes{display:flex;gap:6px;justify-content:center;flex-wrap:nowrap;margin-bottom:20px;}
.perm-box{display:flex;flex-direction:column;align-items:center;gap:0;}
.perm-char{font-family:'JetBrains Mono',monospace;font-size:1.6rem;font-weight:800;width:42px;height:42px;display:flex;align-items:center;justify-content:center;border-radius:8px;border:2px solid;transition:all 0.2s;}
.perm-pos{font-size:0.65rem;color:#475569;margin-top:4px;font-family:'JetBrains Mono',monospace;}
.perm-type .perm-char{color:#fbbf24;border-color:rgba(251,191,36,0.4);background:rgba(251,191,36,0.08);}
.perm-owner .perm-char{color:#f472b6;border-color:rgba(244,114,182,0.4);background:rgba(244,114,182,0.08);}
.perm-group .perm-char{color:#00f0ff;border-color:rgba(0,240,255,0.4);background:rgba(0,240,255,0.08);}
.perm-others .perm-char{color:#ab20fd;border-color:rgba(171,32,253,0.4);background:rgba(171,32,253,0.08);}
.perm-dash .perm-char{color:#334155;border-color:rgba(51,65,85,0.4);background:rgba(51,65,85,0.05);}
.perm-labels{display:flex;gap:6px;justify-content:center;}
.perm-label{display:flex;flex-direction:column;align-items:center;gap:4px;}
.perm-label-chip{font-size:0.75rem;font-weight:700;padding:4px 10px;border-radius:6px;border:1px solid;}
.perm-label-chip.type{color:#fbbf24;border-color:rgba(251,191,36,0.3);background:rgba(251,191,36,0.07);}
.perm-label-chip.owner{color:#f472b6;border-color:rgba(244,114,182,0.3);background:rgba(244,114,182,0.07);}
.perm-label-chip.group{color:#00f0ff;border-color:rgba(0,240,255,0.3);background:rgba(0,240,255,0.07);}
.perm-label-chip.others{color:#ab20fd;border-color:rgba(171,32,253,0.3);background:rgba(171,32,253,0.07);}
.perm-label-sub{font-size:0.7rem;color:#64748b;text-align:center;}
.perm-label-pos{font-size:0.68rem;color:#475569;font-family:'JetBrains Mono',monospace;}
.perm-legend{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin-top:20px;}
.perm-legend-item{display:flex;align-items:center;gap:10px;padding:10px 14px;border-radius:8px;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.04);}
.perm-legend-sym{font-family:'JetBrains Mono',monospace;font-size:1.1rem;font-weight:800;width:28px;text-align:center;flex-shrink:0;}
.perm-legend-desc{font-size:0.85rem;color:#94a3b8;line-height:1.4;}
.perm-legend-desc strong{color:#e2e8f0;display:block;}
.sym-d{color:#00f0ff;}.sym-r{color:#3ddc84;}.sym-w{color:#fbbf24;}.sym-x{color:#f472b6;}.sym-dash{color:#334155;}
.perm-mode-card{background:rgba(15,17,26,0.5);border:1px solid rgba(255,255,255,0.06);border-radius:12px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,0.2);}
.perm-mode-card h5{margin:0;padding:14px 20px;font-size:0.8rem;text-transform:uppercase;letter-spacing:0.1em;color:#64748b;border-bottom:1px solid rgba(255,255,255,0.05);}
.perm-mode-table{width:100%;border-collapse:collapse;}
.perm-mode-table th{padding:10px 16px;text-align:center;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.08em;font-weight:700;color:#8a94a6;background:rgba(255,255,255,0.01);border-bottom:1px solid rgba(255,255,255,0.05);}
.perm-mode-table td{padding:10px 16px;border-bottom:1px solid rgba(255,255,255,0.04);font-size:0.9rem;text-align:center;font-family:'JetBrains Mono',monospace;}
.perm-mode-table tr:last-child td{border-bottom:none;}
.perm-mode-table tr:hover td{background:rgba(255,255,255,0.02);}
.perm-dec{color:#fbbf24;font-weight:800;font-size:1rem;}.perm-bin{color:#94a3b8;}
.perm-mode-r{color:#3ddc84;}.perm-mode-w{color:#fbbf24;}.perm-mode-x{color:#f472b6;}.perm-mode-dash{color:#334155;}
.perm-full{color:#3ddc84;font-weight:700;}
</style>

<div class="perm-wrap">
<div class="perm-string-card">
<h5>โครงสร้าง Permission String (10 ตัวอักษร)</h5>
<div class="perm-boxes">
<div class="perm-box perm-type"><div class="perm-char">d</div><div class="perm-pos">#1</div></div>
<div class="perm-box perm-owner"><div class="perm-char">r</div><div class="perm-pos">#2</div></div>
<div class="perm-box perm-owner"><div class="perm-char">w</div><div class="perm-pos">#3</div></div>
<div class="perm-box perm-owner"><div class="perm-char">x</div><div class="perm-pos">#4</div></div>
<div class="perm-box perm-group"><div class="perm-char">r</div><div class="perm-pos">#5</div></div>
<div class="perm-box perm-dash"><div class="perm-char">-</div><div class="perm-pos">#6</div></div>
<div class="perm-box perm-group"><div class="perm-char">x</div><div class="perm-pos">#7</div></div>
<div class="perm-box perm-others"><div class="perm-char">r</div><div class="perm-pos">#8</div></div>
<div class="perm-box perm-dash"><div class="perm-char">-</div><div class="perm-pos">#9</div></div>
<div class="perm-box perm-others"><div class="perm-char">x</div><div class="perm-pos">#10</div></div>
</div>
<div class="perm-labels">
<div class="perm-label" style="width:42px;">
<div class="perm-label-chip type">type</div>
<div class="perm-label-sub">ประเภท</div>
<div class="perm-label-pos">#1</div>
</div>
<div style="width:6px;"></div>
<div class="perm-label" style="width:138px;">
<div class="perm-label-chip owner">owner</div>
<div class="perm-label-sub">สิทธิ์เจ้าของ</div>
<div class="perm-label-pos">#2 – #4</div>
</div>
<div style="width:6px;"></div>
<div class="perm-label" style="width:138px;">
<div class="perm-label-chip group">group</div>
<div class="perm-label-sub">สิทธิ์กลุ่ม</div>
<div class="perm-label-pos">#5 – #7</div>
</div>
<div style="width:6px;"></div>
<div class="perm-label" style="width:138px;">
<div class="perm-label-chip others">others</div>
<div class="perm-label-sub">สิทธิ์ผู้อื่น</div>
<div class="perm-label-pos">#8 – #10</div>
</div>
</div>
<div class="perm-legend">
<div class="perm-legend-item"><span class="perm-legend-sym sym-d">d</span><div class="perm-legend-desc"><strong>Directory</strong>ตำแหน่ง #1 คือ d = directory, - = file</div></div>
<div class="perm-legend-item"><span class="perm-legend-sym sym-r">r</span><div class="perm-legend-desc"><strong>Read</strong>สิทธิ์อ่านไฟล์หรือดู directory</div></div>
<div class="perm-legend-item"><span class="perm-legend-sym sym-w">w</span><div class="perm-legend-desc"><strong>Write</strong>สิทธิ์เขียน แก้ไข หรือลบไฟล์</div></div>
<div class="perm-legend-item"><span class="perm-legend-sym sym-x">x</span><div class="perm-legend-desc"><strong>Execute</strong>สิทธิ์รันไฟล์หรือเข้า directory</div></div>
<div class="perm-legend-item"><span class="perm-legend-sym sym-dash">-</span><div class="perm-legend-desc"><strong>No Permission</strong>ไม่มีสิทธิ์ในระดับนั้น</div></div>
<div class="perm-legend-item"><span class="perm-legend-sym sym-dash">-</span><div class="perm-legend-desc"><strong>Regular File</strong>ตำแหน่ง #1 คือ - = regular file</div></div>
</div>
</div>
<div class="perm-mode-card">
<h5>ตาราง Permission Mode (Octal)</h5>
<table class="perm-mode-table">
<tr><th>Decimal</th><th>Binary</th><th>Mode</th><th>ความหมาย</th></tr>
<tr><td class="perm-dec">7</td><td class="perm-bin">111</td><td><span class="perm-mode-r">r</span><span class="perm-mode-w">w</span><span class="perm-mode-x">x</span></td><td style="color:#3ddc84;font-family:inherit;font-weight:600;">read + write + execute</td></tr>
<tr><td class="perm-dec">6</td><td class="perm-bin">110</td><td><span class="perm-mode-r">r</span><span class="perm-mode-w">w</span><span class="perm-mode-dash">-</span></td><td style="color:#94a3b8;font-family:inherit;">read + write</td></tr>
<tr><td class="perm-dec">5</td><td class="perm-bin">101</td><td><span class="perm-mode-r">r</span><span class="perm-mode-dash">-</span><span class="perm-mode-x">x</span></td><td style="color:#94a3b8;font-family:inherit;">read + execute</td></tr>
<tr><td class="perm-dec">4</td><td class="perm-bin">100</td><td><span class="perm-mode-r">r</span><span class="perm-mode-dash">-</span><span class="perm-mode-dash">-</span></td><td style="color:#94a3b8;font-family:inherit;">read only</td></tr>
<tr><td class="perm-dec">3</td><td class="perm-bin">011</td><td><span class="perm-mode-dash">-</span><span class="perm-mode-w">w</span><span class="perm-mode-x">x</span></td><td style="color:#94a3b8;font-family:inherit;">write + execute</td></tr>
<tr><td class="perm-dec">2</td><td class="perm-bin">010</td><td><span class="perm-mode-dash">-</span><span class="perm-mode-w">w</span><span class="perm-mode-dash">-</span></td><td style="color:#94a3b8;font-family:inherit;">write only</td></tr>
<tr><td class="perm-dec">1</td><td class="perm-bin">001</td><td><span class="perm-mode-dash">-</span><span class="perm-mode-dash">-</span><span class="perm-mode-x">x</span></td><td style="color:#94a3b8;font-family:inherit;">execute only</td></tr>
<tr><td class="perm-dec">0</td><td class="perm-bin">000</td><td><span class="perm-mode-dash">-</span><span class="perm-mode-dash">-</span><span class="perm-mode-dash">-</span></td><td style="color:#475569;font-family:inherit;">no permission</td></tr>
</table>
</div>
</div>"""

# ─────────────────────────────────────────────────────────────────────────────
# BLOCK 9 — chmod / chown / chgrp Commands
# ─────────────────────────────────────────────────────────────────────────────
b_chmod = """#### ⚙️ คำสั่งเปลี่ยนสิทธิ์และเจ้าของไฟล์

<style>
.perm-cmd-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.perm-cmd-section{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;overflow:hidden;margin-bottom:24px;box-shadow:0 4px 20px rgba(0,0,0,0.2);}
.perm-cmd-header{padding:14px 20px;display:flex;align-items:center;gap:14px;border-bottom:1px solid rgba(255,255,255,0.06);}
.perm-cmd-mono{font-family:'JetBrains Mono',monospace;font-size:1.1rem;font-weight:800;flex-shrink:0;}
.perm-cmd-text{display:flex;flex-direction:column;gap:2px;}
.perm-cmd-en{font-size:0.78rem;text-transform:uppercase;letter-spacing:0.1em;opacity:0.55;font-family:'JetBrains Mono',monospace;}
.perm-cmd-th{font-size:0.83rem;font-weight:600;opacity:0.85;}
.sh-chmod .perm-cmd-header{background:rgba(0,240,255,0.04);}
.sh-chmod .perm-cmd-mono,.sh-chmod .perm-cmd-th{color:#00f0ff;}
.sh-chown .perm-cmd-header{background:rgba(251,191,36,0.04);}
.sh-chown .perm-cmd-mono,.sh-chown .perm-cmd-th{color:#fbbf24;}
.sh-chgrp .perm-cmd-header{background:rgba(244,114,182,0.04);}
.sh-chgrp .perm-cmd-mono,.sh-chgrp .perm-cmd-th{color:#f472b6;}
.perm-cmd-table{width:100%;border-collapse:collapse;}
.perm-cmd-table th{padding:10px 16px;text-align:left;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.08em;font-weight:700;color:#8a94a6;background:rgba(255,255,255,0.01);border-bottom:1px solid rgba(255,255,255,0.05);}
.perm-cmd-table td{padding:11px 16px;border-bottom:1px solid rgba(255,255,255,0.04);font-size:0.9rem;vertical-align:top;}
.perm-cmd-table tr:last-child td{border-bottom:none;}
.perm-cmd-table tr:hover td{background:rgba(255,255,255,0.02);}
.perm-cmd-table td:first-child{font-family:'JetBrains Mono',monospace;font-size:0.88rem;white-space:nowrap;color:#00f0ff;}
.perm-cmd-table td:last-child{color:#94a3b8;line-height:1.6;}
.td-amber2{color:#fbbf24 !important;}.td-pink2{color:#f472b6 !important;}
.perm-eg{display:block;margin-top:4px;font-size:0.82rem;color:#64748b;font-family:'JetBrains Mono',monospace;}
.perm-eg::before{content:"e.g. ";color:#475569;}
.perm-note{display:flex;align-items:flex-start;gap:10px;margin:12px 16px;padding:12px 14px;border-radius:8px;background:rgba(0,240,255,0.04);border:1px solid rgba(0,240,255,0.12);}
.perm-note-icon{font-size:1rem;flex-shrink:0;margin-top:1px;}
.perm-note-text{font-size:0.83rem;color:#94a3b8;line-height:1.6;font-family:'JetBrains Mono',monospace;}
.perm-note-text span{color:#fbbf24;font-weight:700;}
</style>

<div class="perm-cmd-wrap">

<div class="perm-cmd-section sh-chmod">
<div class="perm-cmd-header">
<span class="perm-cmd-mono">chmod</span>
<div class="perm-cmd-text">
<span class="perm-cmd-en">change mode — change file/directory permissions</span>
<span class="perm-cmd-th">เปลี่ยนสิทธิ์การเข้าถึงไฟล์หรือ directory ด้วยรหัส Octal หรือ Symbolic</span>
</div>
</div>
<table class="perm-cmd-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td>chmod [mode] [file]</td><td>เปลี่ยนสิทธิ์ไฟล์ด้วย Octal mode ที่ระบุ<span class="perm-eg">chmod 755 data.txt</span></td></tr>
<tr><td>chmod -R [mode] [dir]</td><td>เปลี่ยนสิทธิ์ทุกไฟล์และ directory ภายในแบบ Recursive<span class="perm-eg">chmod -R 644 /home/kali</span></td></tr>
</table>
<div class="perm-note">
<span class="perm-note-icon">💡</span>
<div class="perm-note-text">ตัวอย่าง: <span>chmod 755 data.txt</span> → owner=<span>rwx(7)</span>, group=<span>r-x(5)</span>, others=<span>r-x(5)</span><br>-rwxrw-rw- 1 root root ... data.txt → เปลี่ยนเป็น → -rwxr-xr-x</div>
</div>
</div>

<div class="perm-cmd-section sh-chown">
<div class="perm-cmd-header">
<span class="perm-cmd-mono">chown</span>
<div class="perm-cmd-text">
<span class="perm-cmd-en">change owner — change ownership of files or directories</span>
<span class="perm-cmd-th">เปลี่ยนเจ้าของ (user) และกลุ่ม (group) ของไฟล์หรือ directory</span>
</div>
</div>
<table class="perm-cmd-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-amber2">chown [user:group] [file]</td><td>เปลี่ยนเจ้าของและกลุ่มของไฟล์หรือ directory ที่ระบุ<span class="perm-eg">chown root:kali data.txt</span></td></tr>
</table>
</div>

<div class="perm-cmd-section sh-chgrp">
<div class="perm-cmd-header">
<span class="perm-cmd-mono">chgrp</span>
<div class="perm-cmd-text">
<span class="perm-cmd-en">change group — change the group of files or directories</span>
<span class="perm-cmd-th">เปลี่ยนเฉพาะกลุ่ม (group) ของไฟล์หรือ directory โดยไม่เปลี่ยน owner</span>
</div>
</div>
<table class="perm-cmd-table">
<tr><th>Command Line</th><th>Description</th></tr>
<tr><td class="td-pink2">chgrp [group] [file]</td><td>เปลี่ยนกลุ่มของไฟล์หรือ directory ที่ระบุ<span class="perm-eg">chgrp root data.txt</span></td></tr>
</table>
</div>

</div>"""

# ─── Append new blocks ───
new_blocks = [
    {"type": "markdown", "value": b_sep2},
    {"type": "markdown", "value": b_lsl},
    {"type": "markdown", "value": b_perm},
    {"type": "markdown", "value": b_chmod},
]

blocks.extend(new_blocks)
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=166).update({"content": lesson.content})
db.session.commit()

print(f"Permission blocks appended! Total blocks now: {len(blocks)}")
for i, b in enumerate(blocks):
    print(f"  Block {i}: {len(b['value'])} chars")
