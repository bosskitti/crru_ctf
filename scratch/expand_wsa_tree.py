import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l168 = db.session.query(TutorialLesson).filter_by(id=168).first()
blocks = json.loads(l168.content)

# ─── Replace Block 9 with Wider Graphical Tree Diagram + Bottom Knowledge Explanation Callout ───
blocks[9]['value'] = """### 📁 Windows File System & Directory Structure

ต่างจาก Linux ที่รวมทุกอย่างเข้ากับ Root Directory (/) เพียงอันเดียว ระบบปฏิบัติการ Windows ใช้สถาปัตยกรรมแบบ **หลายพาร์ติชัน (Multi-Partitions)** โดยแบ่งข้อมูลจัดเก็บออกเป็นไดรฟ์ต่างๆ เช่น **C:, D:, E:**

<style>
.wfs-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:24px;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:28px;box-shadow:0 8px 32px rgba(0,0,0,0.4);box-sizing:border-box;}

/* Hierarchical Tree Styles (Wider and Responsive) */
.tree-container{width:100%;display:flex;flex-direction:column;align-items:center;padding:20px 0;overflow-x:auto;scrollbar-width:thin;}
.tree-branch{display:flex;justify-content:center;gap:12px;position:relative;}

/* Nodes with slightly optimized sizes for wider fit */
.tnode{display:flex;flex-direction:column;align-items:center;padding:8px 12px;background:rgba(7,9,16,0.88);border:1px solid rgba(255,255,255,0.08);border-radius:8px;font-family:'JetBrains Mono',monospace;font-size:0.75rem;font-weight:700;color:#e2e8f0;transition:all 0.2s ease;z-index:2;position:relative;min-width:70px;text-align:center;}
.tnode:hover{border-color:#00f0ff;box-shadow:0 0 12px rgba(0,240,255,0.3);transform:translateY(-2px);color:#ffffff;}
.tnode-icon{font-size:1.3rem;margin-bottom:3px;}
.tnode.root{border-color:#00f0ff;background:rgba(0,240,255,0.04);color:#00f0ff;min-width:110px;}
.tnode.sub{border-color:#fbbf24;background:rgba(251,191,36,0.04);color:#fbbf24;min-width:90px;}
.tnode.file{border-color:rgba(255,255,255,0.12);background:rgba(255,255,255,0.02);color:#94a3b8;font-size:0.68rem;padding:5px 8px;min-width:65px;}
.tnode.file .tnode-icon{font-size:1rem;color:#94a3b8;}

/* File group wrappers */
.file-grp{display:flex;gap:4px;margin-top:10px;}

/* Connector Lines */
.t-spine-v{width:2px;height:24px;background:rgba(255,255,255,0.12);margin:0 auto;position:relative;}
.t-spine-h{height:2px;background:rgba(255,255,255,0.12);position:absolute;top:-12px;left:0;right:0;width:calc(100% - 140px);margin:0 auto;}
.t-connector-down{width:2px;height:12px;background:rgba(255,255,255,0.12);position:absolute;top:-12px;left:50%;transform:translateX(-50%);}
.t-col{display:flex;flex-direction:column;align-items:center;position:relative;}

/* Bottom Explanation Panel */
.wfs-exp-panel{background:rgba(15,17,26,0.6);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:20px;margin-top:12px;}
.wfs-exp-hdr{font-size:0.95rem;font-weight:700;color:#ffffff;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:8px;margin-bottom:12px;display:flex;align-items:center;gap:8px;}
.wfs-exp-hdr span{color:#00f0ff;}
.wfs-exp-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;}
@media(max-width:768px){.wfs-exp-grid{grid-template-columns:1fr;}}
.wfs-exp-card{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:12px 14px;}
.wfs-exp-title{font-size:0.83rem;font-weight:700;margin-bottom:6px;}
.wfs-exp-title.t-root{color:#00f0ff;}
.wfs-exp-title.t-sub{color:#fbbf24;}
.wfs-exp-title.t-file{color:#94a3b8;}
.wfs-exp-desc{font-size:0.8rem;color:#94a3b8;line-height:1.6;margin:0;}
</style>

<div class="wfs-wrap">
<div class="tree-container">
<!-- Level 1: Root C:\ -->
<div class="tree-branch">
<div class="tnode root">
<span class="tnode-icon">💽</span>
<span>C:\\ (Root)</span>
</div>
</div>

<!-- Connector 1 -->
<div class="t-spine-v"></div>

<!-- Horizontal link for Level 2 (Expanded width to 90%) -->
<div class="tree-branch" style="width:100%;max-width:980px;">
<div class="t-spine-h" style="width:75%;"></div>

<div class="w-row" style="justify-content:center;gap:40px;width:100%;">
<!-- DOS -->
<div class="t-col" style="flex:1;">
<div class="t-connector-down"></div>
<div class="tnode sub">
<span class="tnode-icon">📁</span>
<span>DOS</span>
</div>
<div class="t-spine-v"></div>
<div class="file-grp">
<div class="tnode file"><span class="tnode-icon">📄</span><span>file1.txt</span></div>
<div class="tnode file"><span class="tnode-icon">📄</span><span>file2.txt</span></div>
<div class="tnode file"><span class="tnode-icon">📄</span><span>file3.txt</span></div>
</div>
</div>

<!-- XLS -->
<div class="t-col" style="flex:1;">
<div class="t-connector-down"></div>
<div class="tnode sub">
<span class="tnode-icon">📁</span>
<span>XLS</span>
</div>
<div class="t-spine-v"></div>
<div class="file-grp">
<div class="tnode file"><span class="tnode-icon">📊</span><span>budget.xls</span></div>
<div class="tnode file"><span class="tnode-icon">📊</span><span>sales.xls</span></div>
<div class="tnode file"><span class="tnode-icon">📊</span><span>chart.xls</span></div>
</div>
</div>

<!-- DOC -->
<div class="t-col" style="flex:1.6;">
<div class="t-connector-down"></div>
<div class="tnode sub">
<span class="tnode-icon">📁</span>
<span>DOC</span>
</div>
<div class="t-spine-v"></div>
<div class="w-row" style="gap:16px;align-items:flex-start;">
<div class="file-grp" style="margin-top:0;">
<div class="tnode file"><span class="tnode-icon">📝</span><span>doc1.doc</span></div>
<div class="tnode file"><span class="tnode-icon">📝</span><span>doc2.doc</span></div>
<div class="tnode file"><span class="tnode-icon">📝</span><span>doc3.doc</span></div>
</div>

<!-- Deep branch from DOC -->
<div class="t-col" style="margin-top:-2px;">
<div class="t-spine-h" style="width:60%;top:-10px;"></div>
<div class="w-row" style="gap:14px;">
<!-- ENG -->
<div class="t-col">
<div class="t-connector-down" style="top:-10px;"></div>
<div class="tnode sub" style="font-size:0.72rem;padding:6px 10px;min-width:75px;">
<span class="tnode-icon" style="font-size:1.1rem;">📁</span>
<span>ENG</span>
</div>
<div class="t-spine-v" style="height:14px;"></div>
<div class="file-grp" style="margin-top:0;gap:3px;">
<div class="tnode file" style="padding:4px 6px;font-size:0.63rem;min-width:55px;"><span class="tnode-icon" style="font-size:0.85rem;">📄</span><span>eng.doc</span></div>
<div class="tnode file" style="padding:4px 6px;font-size:0.63rem;min-width:55px;"><span class="tnode-icon" style="font-size:0.85rem;">📄</span><span>info.doc</span></div>
</div>
</div>

<!-- PHY -->
<div class="t-col">
<div class="t-connector-down" style="top:-10px;"></div>
<div class="tnode sub" style="font-size:0.72rem;padding:6px 10px;min-width:75px;">
<span class="tnode-icon" style="font-size:1.1rem;">📁</span>
<span>PHY</span>
</div>
<div class="t-spine-v" style="height:14px;"></div>
<div class="file-grp" style="margin-top:0;gap:3px;">
<div class="tnode file" style="padding:4px 6px;font-size:0.63rem;min-width:55px;"><span class="tnode-icon" style="font-size:0.85rem;">📄</span><span>phy.doc</span></div>
<div class="tnode file" style="padding:4px 6px;font-size:0.63rem;min-width:55px;"><span class="tnode-icon" style="font-size:0.85rem;">📄</span><span>lab.doc</span></div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>

<!-- Explanation Section -->
<div class="wfs-exp-panel">
<div class="wfs-exp-hdr"><span>📂</span> โครงสร้างและการทำงานของระบบไฟล์ Windows (Hierarchical System)</div>
<div class="wfs-exp-grid">
<div class="wfs-exp-card">
<div class="wfs-exp-title t-root">💽 Root Directory (โฟลเดอร์ราก)</div>
<p class="wfs-exp-desc">ตำแหน่งบนสุดของพาร์ติชันนั้นๆ (เช่น <code>C:\\</code>) ทำหน้าที่เป็นจุดเริ่มต้นหรือรากของต้นไม้ระบบไฟล์ ทุกๆ โฟลเดอร์และไฟล์อื่นจะสืบทอดที่อยู่ลงมาจากตำแหน่ง Root นี้</p>
</div>
<div class="wfs-exp-card">
<div class="wfs-exp-title t-sub">📁 Subdirectory (โฟลเดอร์ย่อย)</div>
<p class="wfs-exp-desc">โฟลเดอร์ที่อยู่ภายใน Root อีกทีหนึ่ง (เช่น <code>DOS</code>, <code>XLS</code>, <code>DOC</code>) มีคุณสมบัติในการสร้างโฟลเดอร์ย่อยซ้อนลงไปได้อีกหลายเลเวล (เช่น <code>DOC\\ENG</code>, <code>DOC\\PHY</code>) ช่วยจัดระเบียบโครงสร้างข้อมูล</p>
</div>
<div class="wfs-exp-card">
<div class="wfs-exp-title t-file">📄 Files (ไฟล์ข้อมูล)</div>
<p class="wfs-exp-desc">ใบไม้หรือกิ่งปลายสุดของโครงสร้าง เป็นที่จัดเก็บเนื้อหาข้อมูลจริงในรูปแบบดิจิทัล (เช่น <code>.txt</code>, <code>.xls</code>, <code>.doc</code>) โดยไฟล์จะอาศัยอยู่ในโฟลเดอร์หรือรูทเพื่อความเป็นระเบียบ</p>
</div>
</div>
</div>

</div>"""

l168.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=168).update({"content": l168.content})
db.session.commit()
print("Windows File System tree expanded to 980px max-width, gaps optimized, and explain panel added!")
