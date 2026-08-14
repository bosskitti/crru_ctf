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

# Block 7: ls -l with TABLE-based column alignment (no more flex drift)
block_7 = """#### 📋 ข้อมูลและรายละเอียดของไฟล์และ Directory (`ls -l`)

<style>
.lsl2-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.lsl2-terminal{background:#070910;border-radius:10px;overflow:hidden;border:1px solid rgba(255,255,255,0.08);box-shadow:0 8px 32px rgba(0,0,0,0.5);}
.lsl2-titlebar{background:rgba(28,30,44,0.98);padding:9px 16px;display:flex;align-items:center;gap:8px;border-bottom:1px solid rgba(255,255,255,0.05);}
.lsl2-dot{width:11px;height:11px;border-radius:50%;}
.lsl2-dot.r{background:#ff5f57;}.lsl2-dot.y{background:#ffbd2e;}.lsl2-dot.g{background:#28c840;}
.lsl2-title{flex:1;text-align:center;font-size:0.75rem;color:#8a94a6;font-family:'JetBrains Mono',monospace;letter-spacing:0.06em;}
.lsl2-body{padding:20px 24px 0;}
.lsl2-prompt{font-family:'JetBrains Mono',monospace;font-size:0.88rem;margin:0 0 4px;color:#3ddc84;}
.lsl2-prompt span{color:#00f0ff;}
.lsl2-dim{font-family:'JetBrains Mono',monospace;font-size:0.88rem;color:#334155;margin-bottom:6px;}
.lsl2-tbl{width:100%;border-collapse:collapse;font-family:'JetBrains Mono',monospace;font-size:0.88rem;table-layout:auto;}
.lsl2-tbl td{padding:2px 8px 2px 0;white-space:nowrap;vertical-align:bottom;line-height:1.8;}
.lsl2-tbl td:first-child{padding-left:0;}
.lsl2-tbl .data-perm{color:#fbbf24;}
.lsl2-tbl .data-link{color:#64748b;text-align:right;padding-right:12px;}
.lsl2-tbl .data-own{color:#f472b6;}
.lsl2-tbl .data-grp{color:#f472b6;}
.lsl2-tbl .data-size{color:#ab20fd;text-align:right;padding-right:12px;}
.lsl2-tbl .data-date{color:#3ddc84;}
.lsl2-tbl .data-name{color:#ffffff;}
.lsl2-tbl .data-dir{color:#00f0ff;}
.lsl2-sep-row td{padding:12px 0 0;border-top:1px solid rgba(255,255,255,0.06);}
.lsl2-tbl .lbl-cell{padding:8px 8px 16px 0;vertical-align:top;text-align:center;}
.lsl2-tbl .lbl-cell:first-child{padding-left:0;}
.lsl2-chip{display:inline-block;font-size:0.7rem;font-weight:700;padding:4px 8px;border-radius:6px;border:1px solid;white-space:nowrap;font-family:inherit;}
.lsl2-sub{font-size:0.67rem;color:#64748b;margin-top:3px;white-space:nowrap;font-family:inherit;}
.chip-perm{color:#fbbf24;border-color:rgba(251,191,36,0.35);background:rgba(251,191,36,0.08);}
.chip-link{color:#94a3b8;border-color:rgba(148,163,184,0.3);background:rgba(148,163,184,0.05);}
.chip-own{color:#f472b6;border-color:rgba(244,114,182,0.35);background:rgba(244,114,182,0.08);}
.chip-size{color:#ab20fd;border-color:rgba(171,32,253,0.35);background:rgba(171,32,253,0.08);}
.chip-date{color:#3ddc84;border-color:rgba(61,220,132,0.35);background:rgba(61,220,132,0.08);}
.chip-name{color:#e2e8f0;border-color:rgba(226,232,240,0.2);background:rgba(226,232,240,0.04);}
</style>

<div class="lsl2-wrap">
<div class="lsl2-terminal">
<div class="lsl2-titlebar">
<span class="lsl2-dot r"></span><span class="lsl2-dot y"></span><span class="lsl2-dot g"></span>
<span class="lsl2-title">bash — root@kali:~</span>
</div>
<div class="lsl2-body">
<div class="lsl2-prompt"><span>root@kali:~#</span> ls -l</div>
<div class="lsl2-dim">total 140516</div>
<table class="lsl2-tbl">
<tbody>
<tr>
<td class="data-perm">-rwxrw-rw-</td>
<td class="data-link">1</td>
<td class="data-own">root</td>
<td class="data-grp">root</td>
<td class="data-size">3942027</td>
<td class="data-date">Mar 29&nbsp; 2018</td>
<td class="data-name">20180329_130139.jpg</td>
</tr>
<tr>
<td class="data-perm">drwxr-xr-x</td>
<td class="data-link">3</td>
<td class="data-own">root</td>
<td class="data-grp">root</td>
<td class="data-size">4096</td>
<td class="data-date">Jul 27 10:27</td>
<td class="data-dir">CTF-2018-07-03</td>
</tr>
<tr>
<td class="data-perm">drwxr-xr-x</td>
<td class="data-link">2</td>
<td class="data-own">root</td>
<td class="data-grp">root</td>
<td class="data-size">4096</td>
<td class="data-date">Sep 29 04:27</td>
<td class="data-dir">CTF-2018-08-29</td>
</tr>
<tr>
<td class="data-perm">drwxr-xr-x</td>
<td class="data-link">2</td>
<td class="data-own">root</td>
<td class="data-grp">root</td>
<td class="data-size">4096</td>
<td class="data-date">Sep 29 04:23</td>
<td class="data-dir">DE-2018-09-26</td>
</tr>
<tr>
<td class="data-perm">-rw-r--r--</td>
<td class="data-link">1</td>
<td class="data-own">root</td>
<td class="data-grp">root</td>
<td class="data-size">139921507</td>
<td class="data-date">Jun 17 01:57</td>
<td class="data-name">rockyou.txt</td>
</tr>
<tr>
<td class="data-perm">-rw-r--r--</td>
<td class="data-link">1</td>
<td class="data-own">root</td>
<td class="data-grp">root</td>
<td class="data-size">4789</td>
<td class="data-date">Oct 10 00:58</td>
<td class="data-name">scan-2018-10-10.txt</td>
</tr>
</tbody>
<tfoot>
<tr class="lsl2-sep-row"><td colspan="7"></td></tr>
<tr>
<td class="lbl-cell"><div class="lsl2-chip chip-perm">type + permission</div><div class="lsl2-sub">ประเภทและสิทธิ์</div></td>
<td class="lbl-cell"><div class="lsl2-chip chip-link">links</div><div class="lsl2-sub">จำนวน Hard Link</div></td>
<td class="lbl-cell"><div class="lsl2-chip chip-own">owner</div><div class="lsl2-sub">เจ้าของไฟล์</div></td>
<td class="lbl-cell"><div class="lsl2-chip chip-own">group</div><div class="lsl2-sub">กลุ่มของไฟล์</div></td>
<td class="lbl-cell"><div class="lsl2-chip chip-size">size</div><div class="lsl2-sub">ขนาดไฟล์ (bytes)</div></td>
<td class="lbl-cell"><div class="lsl2-chip chip-date">modified date</div><div class="lsl2-sub">วันที่แก้ไขล่าสุด</div></td>
<td class="lbl-cell"><div class="lsl2-chip chip-name">file / directory name</div><div class="lsl2-sub">ชื่อไฟล์หรือ Directory</div></td>
</tr>
</tfoot>
</table>
</div>
</div>
</div>"""

blocks[7]['value'] = block_7
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=166).update({"content": lesson.content})
db.session.commit()
print("Block 7 updated: table-based alignment + removed wongyos!")
