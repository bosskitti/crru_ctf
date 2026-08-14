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

# Precise character alignment (monospace):
# $ ls -la /home/kali
# 0123456789...
# $ at 0, ls at 2, -la at 5, /home/kali at 9
# All "—" aligned at column 23

block_1 = """### 🖥️ Unix Command Line Structure

<style>
.cs3-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.cs3-terminal{background:#070910;border-radius:10px;overflow:hidden;border:1px solid rgba(255,255,255,0.08);box-shadow:0 8px 32px rgba(0,0,0,0.5);}
.cs3-titlebar{background:rgba(28,30,44,0.98);padding:9px 16px;display:flex;align-items:center;gap:8px;border-bottom:1px solid rgba(255,255,255,0.05);}
.cs3-dot{width:11px;height:11px;border-radius:50%;}
.cs3-dot.r{background:#ff5f57;}.cs3-dot.y{background:#ffbd2e;}.cs3-dot.g{background:#28c840;}
.cs3-titlebar-label{flex:1;text-align:center;font-size:0.75rem;color:#8a94a6;font-family:'JetBrains Mono',monospace;letter-spacing:0.06em;}
.cs3-pre{background:transparent;margin:0;padding:28px 32px;font-family:'JetBrains Mono','Courier New',monospace;font-size:1.05rem;line-height:1.85;white-space:pre;overflow-x:auto;border:none;}
.t3-prompt{color:#3ddc84;}.t3-cmd{color:#00f0ff;}.t3-opt{color:#fbbf24;}.t3-arg{color:#ab20fd;}
.t3-tree{color:#334155;}
.t3-sep{color:#475569;}
.t3-desc{color:#64748b;}
.t3-cursor{display:inline-block;width:0.6em;height:0.95em;background:#8a94a6;opacity:0.7;vertical-align:text-bottom;animation:blink3 1.1s step-end infinite;}
@keyframes blink3{50%{opacity:0;}}
</style>

<div class="cs3-wrap">
<div class="cs3-terminal">
<div class="cs3-titlebar">
<span class="cs3-dot r"></span><span class="cs3-dot y"></span><span class="cs3-dot g"></span>
<span class="cs3-titlebar-label">bash — kali@linux</span>
</div>
<pre class="cs3-pre"><span class="t3-prompt">$</span> <span class="t3-cmd">ls</span> <span class="t3-opt">-la</span> <span class="t3-arg">/home/kali</span><span class="t3-cursor"> </span>
<span class="t3-tree">│ │  │   │</span>
<span class="t3-tree">│ │  │   └── </span><span class="t3-arg">Arguments </span><span class="t3-sep">— </span><span class="t3-desc">เป้าหมายที่คำสั่งทำงานด้วย</span>
<span class="t3-tree">│ │  └─────── </span><span class="t3-opt">Options   </span><span class="t3-sep">— </span><span class="t3-desc">ตัวเลือกเพิ่มเติม (Flag)</span>
<span class="t3-tree">│ └────────── </span><span class="t3-cmd">Command   </span><span class="t3-sep">— </span><span class="t3-desc">ชื่อคำสั่งหลัก</span>
<span class="t3-tree">└──────────── </span><span class="t3-prompt">Prompt    </span><span class="t3-sep">— </span><span class="t3-desc">บอกว่าระบบพร้อมรับคำสั่ง</span></pre>
</div>
</div>"""

blocks[1]['value'] = block_1
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=166).update({"content": lesson.content})
db.session.commit()
print("Block 1 redesigned as tree annotation inside terminal!")
