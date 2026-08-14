import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l168 = db.session.query(TutorialLesson).filter_by(id=168).first()
blocks = json.loads(l168.content)

# ─── Replace Block 9 with Premium Cyberpunk Hierarchical Tree Diagram (0-indentation) ───
blocks[9]['value'] = """### 📁 Windows File System & Directory Structure

ต่างจาก Linux ที่รวมทุกอย่างเข้ากับ Root Directory (/) เพียงอันเดียว ระบบปฏิบัติการ Windows ใช้สถาปัตยกรรมแบบ **หลายพาร์ติชัน (Multi-Partitions)** โดยแบ่งข้อมูลจัดเก็บออกเป็นไดรฟ์ต่างๆ เช่น **C:, D:, E:**

<style>
.wfs-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:24px;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:28px;box-shadow:0 8px 32px rgba(0,0,0,0.4);box-sizing:border-box;}
.wfs-info{font-size:0.9rem;color:#94a3b8;line-height:1.7;margin-bottom:12px;}
.wfs-info strong{color:#00f0ff;}

/* Hierarchical Tree Styles */
.tree-container{width:100%;display:flex;flex-direction:column;align-items:center;padding:20px 0;overflow-x:auto;scrollbar-width:thin;}
.tree-branch{display:flex;justify-content:center;gap:12px;position:relative;}

/* Nodes */
.tnode{display:flex;flex-direction:column;align-items:center;padding:8px 14px;background:rgba(7,9,16,0.8);border:1px solid rgba(255,255,255,0.08);border-radius:8px;font-family:'JetBrains Mono',monospace;font-size:0.78rem;font-weight:700;color:#e2e8f0;transition:all 0.2s ease;z-index:2;position:relative;}
.tnode:hover{border-color:#00f0ff;box-shadow:0 0 12px rgba(0,240,255,0.3);transform:translateY(-2px);color:#ffffff;}
.tnode-icon{font-size:1.4rem;margin-bottom:4px;}
.tnode.root{border-color:#00f0ff;background:rgba(0,240,255,0.04);color:#00f0ff;}
.tnode.sub{border-color:#fbbf24;background:rgba(251,191,36,0.04);color:#fbbf24;}
.tnode.file{border-color:rgba(255,255,255,0.15);background:rgba(255,255,255,0.02);color:#94a3b8;font-size:0.7rem;padding:6px 10px;}
.tnode.file .tnode-icon{font-size:1.1rem;color:#94a3b8;}

/* File group wrapper */
.file-grp{display:flex;gap:4px;margin-top:12px;}

/* Spine Connectors using CSS */
.t-spine-v{width:2px;height:24px;background:rgba(255,255,255,0.12);margin:0 auto;position:relative;}
.t-spine-h{height:2px;background:rgba(255,255,255,0.12);position:absolute;top:-12px;left:0;right:0;width:calc(100% - 150px);margin:0 auto;}
.t-connector-down{width:2px;height:12px;background:rgba(255,255,255,0.12);position:absolute;top:-12px;left:50%;transform:translateX(-50%);}

/* Column structures */
.t-col{display:flex;flex-direction:column;align-items:center;position:relative;}
</style>

<div class="wfs-wrap">
<div class="wfs-info">
ระบบไฟล์ Windows ใช้ <strong>ไดรฟ์ C:\เป็น Root Directory (โฟลเดอร์ราก)</strong> ของระบบปฏิบัติการ และแตกแขนงออกเป็นโฟลเดอร์ย่อย (Subdirectories) และไฟล์ต่างๆ ในลักษณะโครงสร้างต้นไม้ลำดับขั้น (Hierarchical Tree) ดังนี้:
</div>

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

<!-- Horizontal link for Level 2 -->
<div class="tree-branch" style="width:100%;max-width:850px;">
<div class="t-spine-h" style="width:66.6%;"></div>

<!-- Level 2 Subdirectories -->
<div class="w-row" style="justify-content:center;gap:36px;width:100%;">
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
<div class="t-col" style="flex:1.5;">
<div class="t-connector-down"></div>
<div class="tnode sub">
<span class="tnode-icon">📁</span>
<span>DOC</span>
</div>
<div class="t-spine-v"></div>
<div class="w-row" style="gap:12px;align-items:flex-start;">
<div class="file-grp" style="margin-top:0;">
<div class="tnode file"><span class="tnode-icon">📝</span><span>doc1.doc</span></div>
<div class="tnode file"><span class="tnode-icon">📝</span><span>doc2.doc</span></div>
<div class="tnode file"><span class="tnode-icon">📝</span><span>doc3.doc</span></div>
</div>
<!-- Deep branch from DOC -->
<div class="t-col" style="margin-top:-2px;">
<div class="t-spine-h" style="width:50%;top:-10px;"></div>
<div class="w-row" style="gap:12px;">
<!-- ENG -->
<div class="t-col">
<div class="t-connector-down" style="top:-10px;"></div>
<div class="tnode sub" style="font-size:0.72rem;padding:6px 10px;">
<span class="tnode-icon" style="font-size:1.1rem;">📁</span>
<span>ENG</span>
</div>
<div class="t-spine-v" style="height:14px;"></div>
<div class="file-grp" style="margin-top:0;gap:2px;">
<div class="tnode file" style="padding:4px 6px;font-size:0.65rem;"><span class="tnode-icon" style="font-size:0.9rem;">📄</span><span>eng.doc</span></div>
<div class="tnode file" style="padding:4px 6px;font-size:0.65rem;"><span class="tnode-icon" style="font-size:0.9rem;">📄</span><span>info.doc</span></div>
</div>
</div>
<!-- PHY -->
<div class="t-col">
<div class="t-connector-down" style="top:-10px;"></div>
<div class="tnode sub" style="font-size:0.72rem;padding:6px 10px;">
<span class="tnode-icon" style="font-size:1.1rem;">📁</span>
<span>PHY</span>
</div>
<div class="t-spine-v" style="height:14px;"></div>
<div class="file-grp" style="margin-top:0;gap:2px;">
<div class="tnode file" style="padding:4px 6px;font-size:0.65rem;"><span class="tnode-icon" style="font-size:0.9rem;">📄</span><span>phy.doc</span></div>
<div class="tnode file" style="padding:4px 6px;font-size:0.65rem;"><span class="tnode-icon" style="font-size:0.9rem;">📄</span><span>lab.doc</span></div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>

</div>
</div>"""

l168.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=168).update({"content": l168.content})
db.session.commit()
print("Windows File System hierarchical tree diagram redesigned in Block 9!")
