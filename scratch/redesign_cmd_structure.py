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

# ── Block 1: Redesigned Command Line Structure ──
block_1 = """### 🖥️ Unix Command Line Structure

<style>
.cs-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.cs-terminal{background:#070910;border-radius:10px;overflow:hidden;border:1px solid rgba(255,255,255,0.08);box-shadow:0 8px 32px rgba(0,0,0,0.5);}
.cs-titlebar{background:rgba(30,32,48,0.95);padding:9px 16px;display:flex;align-items:center;gap:8px;border-bottom:1px solid rgba(255,255,255,0.06);}
.cs-dot{width:11px;height:11px;border-radius:50%;}
.cs-dot.r{background:#ff5f57;}.cs-dot.y{background:#ffbd2e;}.cs-dot.g{background:#28c840;}
.cs-titlebar-label{flex:1;text-align:center;font-size:0.75rem;color:#8a94a6;font-family:'JetBrains Mono',monospace;letter-spacing:0.06em;}
.cs-body{padding:24px 28px 8px 28px;font-family:'JetBrains Mono','Courier New',monospace;}
.cs-line{font-size:1.25rem;font-weight:600;display:flex;align-items:center;gap:0;flex-wrap:nowrap;letter-spacing:0.02em;}
.cs-line .t-prompt{color:#3ddc84;}.cs-line .t-space{color:transparent;user-select:none;width:10px;display:inline-block;}
.cs-line .t-cmd{color:#00f0ff;}.cs-line .t-opt{color:#fbbf24;}.cs-line .t-arg{color:#ab20fd;}
.cs-line .t-cursor{display:inline-block;width:10px;height:1.1em;background:#8a94a6;opacity:0.7;margin-left:4px;vertical-align:text-bottom;animation:blink 1.1s step-end infinite;}
@keyframes blink{50%{opacity:0;}}
.cs-annot{padding:0 28px 24px 28px;}
.cs-arrows{display:flex;flex-wrap:nowrap;gap:0;position:relative;padding-top:6px;}
.cs-ann{display:flex;flex-direction:column;align-items:center;gap:0;}
.cs-ann-line{width:1px;height:28px;background:rgba(255,255,255,0.15);}
.cs-ann-label{display:flex;flex-direction:column;align-items:center;padding:8px 14px;border-radius:8px;border:1px solid;margin-top:0;}
.cs-ann-label span:first-child{font-family:'JetBrains Mono',monospace;font-size:0.8rem;font-weight:700;letter-spacing:0.05em;}
.cs-ann-label span:last-child{font-size:0.75rem;color:#94a3b8;margin-top:2px;text-align:center;white-space:nowrap;}
.ann-prompt .cs-ann-label{border-color:rgba(61,220,132,0.25);background:rgba(61,220,132,0.05);color:#3ddc84;}
.ann-cmd .cs-ann-label{border-color:rgba(0,240,255,0.25);background:rgba(0,240,255,0.05);color:#00f0ff;}
.ann-opt .cs-ann-label{border-color:rgba(251,191,36,0.25);background:rgba(251,191,36,0.05);color:#fbbf24;}
.ann-arg .cs-ann-label{border-color:rgba(171,32,253,0.25);background:rgba(171,32,253,0.05);color:#ab20fd;}
.cs-spacer{flex:1;}
</style>

<div class="cs-wrap">
<div class="cs-terminal">
<div class="cs-titlebar">
<span class="cs-dot r"></span><span class="cs-dot y"></span><span class="cs-dot g"></span>
<span class="cs-titlebar-label">bash — kali@linux</span>
</div>
<div class="cs-body">
<div class="cs-line">
<span class="t-prompt">$</span><span class="t-space"> </span><span class="t-cmd">ls</span><span class="t-space"> </span><span class="t-opt">-la</span><span class="t-space"> </span><span class="t-arg">/home/kali</span><span class="t-cursor"></span>
</div>
</div>
<div class="cs-annot">
<div class="cs-arrows">
<div class="cs-ann ann-prompt">
<div class="cs-ann-line"></div>
<div class="cs-ann-label"><span>Prompt</span><span>บอกว่าระบบพร้อมรับคำสั่ง</span></div>
</div>
<div class="cs-spacer"></div>
<div class="cs-ann ann-cmd">
<div class="cs-ann-line"></div>
<div class="cs-ann-label"><span>Command</span><span>ชื่อคำสั่งหลัก</span></div>
</div>
<div class="cs-spacer"></div>
<div class="cs-ann ann-opt">
<div class="cs-ann-line"></div>
<div class="cs-ann-label"><span>Options</span><span>ตัวเลือกเพิ่มเติม (Flag)</span></div>
</div>
<div class="cs-spacer"></div>
<div class="cs-ann ann-arg">
<div class="cs-ann-line"></div>
<div class="cs-ann-label"><span>Arguments</span><span>เป้าหมายที่คำสั่งทำงานด้วย</span></div>
</div>
</div>
</div>
</div>
</div>"""

blocks[1]['value'] = block_1

lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=166).update({"content": lesson.content})
db.session.commit()
print("Block 1 (Command Line Structure) updated successfully!")
