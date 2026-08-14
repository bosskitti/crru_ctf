import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l168 = db.session.query(TutorialLesson).filter_by(id=168).first()
blocks = json.loads(l168.content)

# ─── New Visuals for Block 5: Ring Diagram of Kernel & User Mode ───
blocks[5]['value'] = """### 🏛️ Windows System Architecture

<style>
.wsa-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;gap:32px;align-items:center;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:28px;box-shadow:0 4px 20px rgba(0,0,0,0.2);}
@media(max-width:768px){.wsa-wrap{flex-direction:column;}}
.wsa-diagram{flex-shrink:0;position:relative;width:240px;height:240px;display:flex;align-items:center;justify-content:center;}
.wsa-ring{border-radius:50%;position:absolute;display:flex;align-items:center;justify-content:center;transition:all 0.3s ease;}
.wsa-ring.user{width:240px;height:240px;background:rgba(0,240,255,0.05);border:2px dashed rgba(0,240,255,0.3);}
.wsa-ring.kernel{width:160px;height:160px;background:rgba(255,0,127,0.06);border:2px dashed rgba(255,0,127,0.3);}
.wsa-ring.hardware{width:80px;height:80px;background:rgba(251,191,36,0.1);border:2px solid rgba(251,191,36,0.5);}
.wsa-label{position:absolute;font-family:'JetBrains Mono',monospace;font-size:0.75rem;font-weight:700;letter-spacing:0.05em;}
.lbl-user{top:12px;color:#00f0ff;}
.lbl-kernel{top:52px;color:#ff007f;}
.lbl-hw{color:#fbbf24;}
.wsa-content{flex:1;display:flex;flex-direction:column;gap:18px;}
.wsa-mode-card{padding:16px;border-radius:8px;border:1px solid;background:rgba(255,255,255,0.02);}
.wsa-mode-card.kernel-card{border-color:rgba(255,0,127,0.15);background:rgba(255,0,127,0.01);}
.wsa-mode-card.user-card{border-color:rgba(0,240,255,0.15);background:rgba(0,240,255,0.01);}
.wsa-mode-title{font-size:0.95rem;font-weight:700;margin-bottom:6px;display:flex;align-items:center;gap:8px;}
.kernel-card .wsa-mode-title{color:#ff007f;}
.user-card .wsa-mode-title{color:#00f0ff;}
.wsa-mode-desc{font-size:0.85rem;color:#94a3b8;line-height:1.6;margin:0;}
</style>

<div class="wsa-wrap">
<div class="wsa-diagram">
<div class="wsa-ring user"></div>
<div class="wsa-ring kernel"></div>
<div class="wsa-ring hardware"></div>
<span class="wsa-label lbl-user">USER MODE</span>
<span class="wsa-label lbl-kernel">KERNEL MODE</span>
<span class="wsa-label lbl-hw">HARDWARE</span>
</div>
<div class="wsa-content">
<div class="wsa-mode-card kernel-card">
<div class="wsa-mode-title">🔴 Kernel Mode (โหมดเคอร์เนล)</div>
<p class="wsa-mode-desc">เป็นโปรแกรมที่มีสิทธิ์เข้าถึง <strong>ทรัพยากรฮาร์ดแวร์โดยตรงและไม่มีข้อจำกัด</strong> ทุกโค้ดที่รันใน Kernel Mode จะทำงานร่วมกันบนหน่วยความจำเสมือนเพียงพื้นที่เดียว (Single virtual address space) หากโค้ดส่วนใดทำงานผิดพลาดอาจทำให้ระบบล่มทั้งหมด (Blue Screen of Death)</p>
</div>
<div class="wsa-mode-card user-card">
<div class="wsa-mode-title">🔵 User Mode (โหมดผู้ใช้)</div>
<p class="wsa-mode-desc">เป็นโหมดสำหรับ <strong>แอปพลิเคชันทั่วไป</strong> ที่ผู้ใช้สั่งรัน Windows จะสร้างพื้นที่หน่วยความจำแยกเฉพาะสำหรับแต่ละโปรแกรม (Isolated process) แอปพลิเคชันในโหมดนี้ไม่มีสิทธิ์เข้าถึงฮาร์ดแวร์โดยตรง หากเกิดความเสียหายจะกระทบเฉพาะโปรแกรมนั้นๆ ไม่ทำให้ระบบหลักล่ม</p>
</div>
</div>
</div>"""

# ─── New Visuals for Block 7: Detailed Architecture Layers ───
blocks[7]['value'] = """### ⚙️ Windows System Architecture Layers

<style>
.arch-layers-wrap{width:100%;max-width:1050px;margin:2rem auto;background:#0d0e15;border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:24px;box-shadow:0 8px 32px rgba(0,0,0,0.4);}
.arch-mode-section{border:1px solid;border-radius:8px;padding:16px;margin-bottom:16px;position:relative;}
.arch-mode-section.um{border-color:rgba(0,240,255,0.15);background:rgba(0,240,255,0.02);}
.arch-mode-section.km{border-color:rgba(255,0,127,0.15);background:rgba(255,0,127,0.02);margin-bottom:0;}
.arch-mode-tag{position:absolute;top:-10px;left:16px;font-size:0.7rem;font-weight:800;padding:2px 8px;border-radius:4px;border:1px solid;text-transform:uppercase;letter-spacing:0.05em;}
.um .arch-mode-tag{color:#00f0ff;border-color:rgba(0,240,255,0.3);background:#070910;}
.km .arch-mode-tag{color:#ff007f;border-color:rgba(255,0,127,0.3);background:#070910;}
.arch-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:8px;}
.arch-box{padding:10px 8px;border-radius:6px;border:1px solid rgba(255,255,255,0.06);background:rgba(255,255,255,0.03);text-align:center;font-size:0.78rem;font-weight:700;font-family:'JetBrains Mono',monospace;color:#cbd5e1;}
.arch-box.app{grid-column:span 4;background:rgba(61,220,132,0.08);border-color:rgba(61,220,132,0.25);color:#3ddc84;}
.arch-box.dll{grid-column:span 2;background:rgba(0,240,255,0.08);border-color:rgba(0,240,255,0.25);color:#00f0ff;}
.arch-box.sys{grid-column:span 2;background:rgba(171,32,253,0.08);border-color:rgba(171,32,253,0.25);color:#ab20fd;}
.arch-box.ntdll{grid-column:span 4;background:rgba(251,191,36,0.08);border-color:rgba(251,191,36,0.25);color:#fbbf24;}
.arch-box.trap{grid-column:span 4;background:rgba(244,114,182,0.08);border-color:rgba(244,114,182,0.25);color:#f472b6;}
.arch-box.mgr{background:rgba(255,255,255,0.05);border-color:rgba(255,255,255,0.1);color:#e2e8f0;}
.arch-box.hal{grid-column:span 4;background:rgba(255,0,127,0.08);border-color:rgba(255,0,127,0.25);color:#ff007f;}
</style>

<div class="arch-layers-wrap">
<!-- User Mode -->
<div class="arch-mode-section um">
<span class="arch-mode-tag">User Mode (Ring 3)</span>
<div class="arch-grid">
<div class="arch-box app">Applications (โปรแกรมใช้งานของผู้ใช้)</div>
<div class="arch-box dll">Subsystem DLLs (Kernel32.dll, User32.dll)</div>
<div class="arch-box sys">System Services & Critical Services</div>
<div class="arch-box ntdll">ntdll.dll / Run-time Library (ตัวกลางเรียกเข้าสู่ Kernel)</div>
</div>
</div>

<!-- Kernel Mode -->
<div class="arch-mode-section km">
<span class="arch-mode-tag">Kernel Mode (Ring 0)</span>
<div class="arch-grid">
<div class="arch-box trap">System Service Dispatcher (Trap Interface / LPC)</div>
<div class="arch-box mgr">I/O Manager</div>
<div class="arch-box mgr">Memory Manager</div>
<div class="arch-box mgr">Process Manager</div>
<div class="arch-box mgr">Security Ref Monitor</div>
<div class="arch-box hal">Hardware Abstraction Layer (HAL) & Kernel Run-time</div>
</div>
</div>
</div>"""

# ─── New Visuals for Block 9: Windows File System (Multi-Partitions) ───
blocks[9]['value'] = """### 📁 Windows File System & Directory Tree

<style>
.wfs-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;gap:24px;}
@media(max-width:768px){.wfs-wrap{flex-direction:column;}}
.wfs-info-card{flex:1;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:24px;box-shadow:0 4px 20px rgba(0,0,0,0.2);display:flex;flex-direction:column;justify-content:center;}
.wfs-info-card h4{margin:0 0 10px;font-size:1.1rem;color:#00f0ff;}
.wfs-info-card p{margin:0;font-size:0.88rem;color:#94a3b8;line-height:1.7;}
.wfs-info-card strong{color:#fbbf24;}
.wfs-tree-card{flex:1;background:rgba(15,17,26,0.5);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:24px;box-shadow:0 4px 20px rgba(0,0,0,0.2);font-family:'JetBrains Mono',monospace;font-size:0.85rem;}
.wfs-tree-node{display:flex;align-items:center;gap:6px;margin:3px 0;}
.wfs-tree-node .icon{font-size:1rem;color:#fbbf24;}
.wfs-tree-node .drive{color:#00f0ff;font-weight:700;}
.wfs-tree-node .dir{color:#e2e8f0;font-weight:600;}
.wfs-tree-node .file{color:#94a3b8;}
.wfs-tree-indent{display:inline-block;width:20px;border-left:1px dashed rgba(255,255,255,0.15);margin-left:8px;height:18px;vertical-align:bottom;}
</style>

<div class="wfs-wrap">
<div class="wfs-info-card">
<h4>💾 Multi-Partition File System</h4>
<p>ต่างจาก Linux ที่รวมทุกอย่างเข้ากับ Root Directory (/) เพียงอันเดียว ระบบปฏิบัติการ Windows ใช้สถาปัตยกรรมแบบ <strong>หลายพาร์ติชัน (Multi-Partitions)</strong> โดยแบ่งข้อมูลจัดเก็บออกเป็นไดรฟ์ต่างๆ เช่น <strong>C:, D:, E:</strong> <br><br>
ซึ่งมีข้อดีในการจัดสรรข้อมูลและกู้คืนระบบได้สะดวก โดยปกติไดรฟ์ <strong>C:\</strong> จะเป็นไดรฟ์หลักที่ใช้สำหรับติดตั้งตัวระบบปฏิบัติการ Windows (Root Drive)</p>
</div>
<div class="wfs-tree-card">
<div style="font-size:0.75rem;color:#64748b;margin-bottom:12px;text-transform:uppercase;letter-spacing:0.05em;">📂 Windows Directory Tree Example</div>
<div class="wfs-tree-node"><span class="icon">💽</span><span class="drive">C:\ (Root Drive)</span></div>
<div class="wfs-tree-node"><span class="wfs-tree-indent"></span><span class="icon">📁</span><span class="dir">DOS</span></div>
<div class="wfs-tree-node"><span class="wfs-tree-indent"></span><span class="wfs-tree-indent"></span><span class="icon">📄</span><span class="file">Files (data.txt, config.sys)</span></div>
<div class="wfs-tree-node"><span class="wfs-tree-indent"></span><span class="icon">📁</span><span class="dir">XLS</span></div>
<div class="wfs-tree-node"><span class="wfs-tree-indent"></span><span class="wfs-tree-indent"></span><span class="icon">📄</span><span class="file">Files (budget.xls, sales.xls)</span></div>
<div class="wfs-tree-node"><span class="wfs-tree-indent"></span><span class="icon">📁</span><span class="dir">DOC</span></div>
<div class="wfs-tree-node"><span class="wfs-tree-indent"></span><span class="wfs-tree-indent"></span><span class="icon">📁</span><span class="dir">ENG</span></div>
<div class="wfs-tree-node"><span class="wfs-tree-indent"></span><span class="wfs-tree-indent"></span><span class="wfs-tree-indent"></span><span class="icon">📄</span><span class="file">Files (report.doc)</span></div>
<div class="wfs-tree-node"><span class="wfs-tree-indent"></span><span class="wfs-tree-indent"></span><span class="icon">📁</span><span class="dir">PHY</span></div>
<div class="wfs-tree-node"><span class="wfs-tree-indent"></span><span class="wfs-tree-indent"></span><span class="wfs-tree-indent"></span><span class="icon">📄</span><span class="file">Files (exam.doc)</span></div>
</div>
</div>"""

l168.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=168).update({"content": l168.content})
db.session.commit()
print("Windows system architecture and file system visuals updated in Lesson 168!")
