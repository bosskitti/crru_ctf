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

block_1 = """### 🖥️ Unix Command Line Structure

<style>
.cs2-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.cs2-terminal{background:#070910;border-radius:10px;overflow:hidden;border:1px solid rgba(255,255,255,0.08);box-shadow:0 8px 32px rgba(0,0,0,0.5);}
.cs2-titlebar{background:rgba(28,30,44,0.98);padding:9px 16px;display:flex;align-items:center;gap:8px;border-bottom:1px solid rgba(255,255,255,0.05);}
.cs2-dot{width:11px;height:11px;border-radius:50%;}
.cs2-dot.r{background:#ff5f57;}.cs2-dot.y{background:#ffbd2e;}.cs2-dot.g{background:#28c840;}
.cs2-titlebar-label{flex:1;text-align:center;font-size:0.75rem;color:#8a94a6;font-family:'JetBrains Mono',monospace;letter-spacing:0.06em;}
.cs2-body{padding:28px 32px 32px 32px;}
.cs2-ann-row{display:flex;align-items:flex-start;gap:0;}
.cs2-col{display:flex;flex-direction:column;align-items:center;flex:1;}
.cs2-token{font-family:'JetBrains Mono','Courier New',monospace;font-size:1.5rem;font-weight:700;padding:0 10px;white-space:nowrap;line-height:2;}
.cs2-col.ann-prompt .cs2-token{color:#3ddc84;}
.cs2-col.ann-cmd .cs2-token{color:#00f0ff;}
.cs2-col.ann-opt .cs2-token{color:#fbbf24;}
.cs2-col.ann-arg .cs2-token{color:#ab20fd;}
.cs2-vline{width:1px;height:32px;background:rgba(255,255,255,0.12);}
.cs2-label{display:flex;flex-direction:column;align-items:center;text-align:center;padding:8px 12px;border-radius:8px;border:1px solid;width:100%;max-width:160px;box-sizing:border-box;}
.cs2-label strong{font-family:'JetBrains Mono',monospace;font-size:0.82rem;font-weight:700;display:block;margin-bottom:3px;}
.cs2-label span{font-size:0.75rem;color:#94a3b8;line-height:1.4;}
.ann-prompt .cs2-label{border-color:rgba(61,220,132,0.3);background:rgba(61,220,132,0.05);}
.ann-prompt .cs2-label strong{color:#3ddc84;}
.ann-cmd .cs2-label{border-color:rgba(0,240,255,0.3);background:rgba(0,240,255,0.05);}
.ann-cmd .cs2-label strong{color:#00f0ff;}
.ann-opt .cs2-label{border-color:rgba(251,191,36,0.3);background:rgba(251,191,36,0.05);}
.ann-opt .cs2-label strong{color:#fbbf24;}
.ann-arg .cs2-label{border-color:rgba(171,32,253,0.3);background:rgba(171,32,253,0.05);}
.ann-arg .cs2-label strong{color:#ab20fd;}
.cs2-cursor{display:inline-block;width:9px;height:1.1em;background:#8a94a6;opacity:0.7;vertical-align:text-bottom;animation:blink2 1.1s step-end infinite;margin-left:2px;}
@keyframes blink2{50%{opacity:0;}}
</style>

<div class="cs2-wrap">
<div class="cs2-terminal">
<div class="cs2-titlebar">
<span class="cs2-dot r"></span><span class="cs2-dot y"></span><span class="cs2-dot g"></span>
<span class="cs2-titlebar-label">bash — kali@linux</span>
</div>
<div class="cs2-body">
<div class="cs2-ann-row">
<div class="cs2-col ann-prompt">
<span class="cs2-token">$</span>
<div class="cs2-vline"></div>
<div class="cs2-label"><strong>Prompt</strong><span>บอกว่าระบบพร้อมรับคำสั่ง</span></div>
</div>
<div class="cs2-col ann-cmd">
<span class="cs2-token">ls</span>
<div class="cs2-vline"></div>
<div class="cs2-label"><strong>Command</strong><span>ชื่อคำสั่งหลัก</span></div>
</div>
<div class="cs2-col ann-opt">
<span class="cs2-token">-la</span>
<div class="cs2-vline"></div>
<div class="cs2-label"><strong>Options</strong><span>ตัวเลือกเพิ่มเติม (Flag)</span></div>
</div>
<div class="cs2-col ann-arg">
<span class="cs2-token">/home/kali<span class="cs2-cursor"></span></span>
<div class="cs2-vline"></div>
<div class="cs2-label"><strong>Arguments</strong><span>เป้าหมายที่คำสั่งทำงานด้วย</span></div>
</div>
</div>
</div>
</div>
</div>"""

blocks[1]['value'] = block_1
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=166).update({"content": lesson.content})
db.session.commit()
print("Block 1 redesigned with aligned annotation columns!")
