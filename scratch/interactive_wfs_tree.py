import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l168 = db.session.query(TutorialLesson).filter_by(id=168).first()
blocks = json.loads(l168.content)

# ─── Replace Block 9 with wider nodes, Hover details updater, and cleaner CSS tree ───
blocks[9]['value'] = """### 📁 Windows File System & Directory Structure

ต่างจาก Linux ที่รวมทุกอย่างเข้ากับ Root Directory (/) เพียงอันเดียว ระบบปฏิบัติการ Windows ใช้สถาปัตยกรรมแบบ **หลายพาร์ติชัน (Multi-Partitions)** โดยแบ่งข้อมูลจัดเก็บออกเป็นไดรฟ์ต่างๆ เช่น **C:, D:, E:**

<style>
.wfs-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:24px;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:28px;box-shadow:0 8px 32px rgba(0,0,0,0.4);box-sizing:border-box;}

/* Tree Structure with Expanded nodes */
.tree-container{width:100%;display:flex;flex-direction:column;align-items:center;padding:20px 0;overflow-x:auto;}
.tree-branch{display:flex;justify-content:center;gap:12px;position:relative;}

/* Expanded Nodes width */
.tnode{display:flex;flex-direction:column;align-items:center;padding:10px 18px;background:rgba(7,9,16,0.85);border:1px solid rgba(255,255,255,0.08);border-radius:8px;font-family:'JetBrains Mono',monospace;font-size:0.8rem;font-weight:700;color:#e2e8f0;transition:all 0.2s ease;z-index:2;position:relative;min-width:115px;text-align:center;cursor:pointer;box-sizing:border-box;}
.tnode:hover, .tnode.active{border-color:#00f0ff;box-shadow:0 0 12px rgba(0,240,255,0.3);transform:translateY(-2px);color:#ffffff;background:rgba(255,255,255,0.05);}
.tnode-icon{font-size:1.4rem;margin-bottom:4px;}

.tnode.root{border-color:#00f0ff;background:rgba(0,240,255,0.04);color:#00f0ff;min-width:140px;}
.tnode.root:hover, .tnode.root.active{background:rgba(0,240,255,0.12);box-shadow:0 0 15px rgba(0,240,255,0.4);}

.tnode.sub{border-color:#fbbf24;background:rgba(251,191,36,0.04);color:#fbbf24;min-width:110px;}
.tnode.sub:hover, .tnode.sub.active{background:rgba(251,191,36,0.12);box-shadow:0 0 15px rgba(251,191,36,0.4);}

.tnode.file{border-color:rgba(255,255,255,0.15);background:rgba(255,255,255,0.02);color:#94a3b8;font-size:0.72rem;padding:6px 12px;min-width:98px;}
.tnode.file:hover, .tnode.file.active{border-color:#3ddc84;color:#ffffff;box-shadow:0 0 12px rgba(61,220,132,0.3);background:rgba(61,220,132,0.06);}
.tnode.file .tnode-icon{font-size:1.1rem;color:#94a3b8;}
.tnode.file:hover .tnode-icon, .tnode.file.active .tnode-icon{color:#3ddc84;}

/* File Group (Vertical Alignment or Tight grid for spacing) */
.file-grp{display:flex;flex-direction:column;gap:5px;margin-top:12px;align-items:center;}

/* Connector Lines */
.t-spine-v{width:2px;height:24px;background:rgba(255,255,255,0.12);margin:0 auto;position:relative;}
.t-spine-h{height:2px;background:rgba(255,255,255,0.12);position:absolute;top:-12px;left:0;right:0;width:calc(100% - 180px);margin:0 auto;}
.t-connector-down{width:2px;height:12px;background:rgba(255,255,255,0.12);position:absolute;top:-12px;left:50%;transform:translateX(-50%);}
.t-col{display:flex;flex-direction:column;align-items:center;position:relative;}

/* Dynamic Info Panel below tree */
.wfs-exp-panel{background:rgba(15,17,26,0.6);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:20px;margin-top:12px;}
.wfs-exp-hdr{font-size:0.95rem;font-weight:700;color:#ffffff;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:10px;margin-bottom:12px;display:flex;align-items:center;gap:10px;}
.wfs-exp-hdr span{color:#00f0ff;}
.wfs-info-badge{font-size:0.68rem;font-weight:800;padding:2px 8px;border-radius:4px;text-transform:uppercase;letter-spacing:0.05em;}
.wfs-info-badge.root{background:rgba(0,240,255,0.08);border:1px solid rgba(0,240,255,0.25);color:#00f0ff;}
.wfs-info-badge.sub{background:rgba(251,191,36,0.08);border:1px solid rgba(251,191,36,0.25);color:#fbbf24;}
.wfs-info-badge.file{background:rgba(61,220,132,0.08);border:1px solid rgba(61,220,132,0.25);color:#3ddc84;}
.wfs-exp-title{font-size:1.05rem;font-weight:700;color:#ffffff;margin:0;}
.wfs-exp-desc{font-size:0.88rem;color:#94a3b8;line-height:1.7;margin:0;}
.wfs-exp-desc strong{color:#fbbf24;}
</style>

<div class="wfs-wrap">
<div class="tree-container">
<!-- Level 1: Root C:\ -->
<div class="tree-branch">
<div id="tn-root" class="tnode root active" onclick="updateTreeInfo('root', this)" onmouseover="updateTreeInfo('root', this)">
<span class="tnode-icon">💽</span>
<span>C:\\ (Root)</span>
</div>
</div>

<!-- Connector 1 -->
<div class="t-spine-v"></div>

<!-- Horizontal link for Level 2 -->
<div class="tree-branch" style="width:100%;max-width:1000px;">
<div class="t-spine-h" style="width:78%;"></div>

<div class="w-row" style="justify-content:center;gap:45px;width:100%;">
<!-- DOS -->
<div class="t-col" style="flex:1;">
<div class="t-connector-down"></div>
<div id="tn-dos" class="tnode sub" onclick="updateTreeInfo('dos', this)" onmouseover="updateTreeInfo('dos', this)">
<span class="tnode-icon">📁</span>
<span>DOS</span>
</div>
<div class="t-spine-v"></div>
<div class="file-grp">
<div class="tnode file" onclick="updateTreeInfo('dos-files', this)" onmouseover="updateTreeInfo('dos-files', this)"><span class="tnode-icon">📄</span><span>file1.txt</span></div>
<div class="tnode file" onclick="updateTreeInfo('dos-files', this)" onmouseover="updateTreeInfo('dos-files', this)"><span class="tnode-icon">📄</span><span>file2.txt</span></div>
<div class="tnode file" onclick="updateTreeInfo('dos-files', this)" onmouseover="updateTreeInfo('dos-files', this)"><span class="tnode-icon">📄</span><span>file3.txt</span></div>
</div>
</div>

<!-- XLS -->
<div class="t-col" style="flex:1;">
<div class="t-connector-down"></div>
<div id="tn-xls" class="tnode sub" onclick="updateTreeInfo('xls', this)" onmouseover="updateTreeInfo('xls', this)">
<span class="tnode-icon">📁</span>
<span>XLS</span>
</div>
<div class="t-spine-v"></div>
<div class="file-grp">
<div class="tnode file" onclick="updateTreeInfo('xls-files', this)" onmouseover="updateTreeInfo('xls-files', this)"><span class="tnode-icon">📊</span><span>budget.xls</span></div>
<div class="tnode file" onclick="updateTreeInfo('xls-files', this)" onmouseover="updateTreeInfo('xls-files', this)"><span class="tnode-icon">📊</span><span>sales.xls</span></div>
<div class="tnode file" onclick="updateTreeInfo('xls-files', this)" onmouseover="updateTreeInfo('xls-files', this)"><span class="tnode-icon">📊</span><span>chart.xls</span></div>
</div>
</div>

<!-- DOC -->
<div class="t-col" style="flex:1.7;">
<div class="t-connector-down"></div>
<div id="tn-doc" class="tnode sub" onclick="updateTreeInfo('doc', this)" onmouseover="updateTreeInfo('doc', this)">
<span class="tnode-icon">📁</span>
<span>DOC</span>
</div>
<div class="t-spine-v"></div>
<div class="w-row" style="gap:18px;align-items:flex-start;">
<div class="file-grp" style="margin-top:0;">
<div class="tnode file" onclick="updateTreeInfo('doc-files', this)" onmouseover="updateTreeInfo('doc-files', this)"><span class="tnode-icon">📝</span><span>doc1.doc</span></div>
<div class="tnode file" onclick="updateTreeInfo('doc-files', this)" onmouseover="updateTreeInfo('doc-files', this)"><span class="tnode-icon">📝</span><span>doc2.doc</span></div>
<div class="tnode file" onclick="updateTreeInfo('doc-files', this)" onmouseover="updateTreeInfo('doc-files', this)"><span class="tnode-icon">📝</span><span>doc3.doc</span></div>
</div>

<!-- Deep branch from DOC -->
<div class="t-col" style="margin-top:-2px;">
<div class="t-spine-h" style="width:65%;top:-10px;"></div>
<div class="w-row" style="gap:16px;">
<!-- ENG -->
<div class="t-col">
<div class="t-connector-down" style="top:-10px;"></div>
<div id="tn-eng" class="tnode sub" style="font-size:0.75rem;padding:6px 12px;min-width:85px;" onclick="updateTreeInfo('eng', this)" onmouseover="updateTreeInfo('eng', this)">
<span class="tnode-icon" style="font-size:1.15rem;">📁</span>
<span>ENG</span>
</div>
<div class="t-spine-v" style="height:14px;"></div>
<div class="file-grp" style="margin-top:0;gap:4px;">
<div class="tnode file" style="padding:4px 6px;font-size:0.65rem;min-width:68px;" onclick="updateTreeInfo('eng-files', this)" onmouseover="updateTreeInfo('eng-files', this)"><span class="tnode-icon" style="font-size:0.85rem;">📄</span><span>eng.doc</span></div>
<div class="tnode file" style="padding:4px 6px;font-size:0.65rem;min-width:68px;" onclick="updateTreeInfo('eng-files', this)" onmouseover="updateTreeInfo('eng-files', this)"><span class="tnode-icon" style="font-size:0.85rem;">📄</span><span>info.doc</span></div>
</div>
</div>

<!-- PHY -->
<div class="t-col">
<div class="t-connector-down" style="top:-10px;"></div>
<div id="tn-phy" class="tnode sub" style="font-size:0.75rem;padding:6px 12px;min-width:85px;" onclick="updateTreeInfo('phy', this)" onmouseover="updateTreeInfo('phy', this)">
<span class="tnode-icon" style="font-size:1.15rem;">📁</span>
<span>PHY</span>
</div>
<div class="t-spine-v" style="height:14px;"></div>
<div class="file-grp" style="margin-top:0;gap:4px;">
<div class="tnode file" style="padding:4px 6px;font-size:0.65rem;min-width:68px;" onclick="updateTreeInfo('phy-files', this)" onmouseover="updateTreeInfo('phy-files', this)"><span class="tnode-icon" style="font-size:0.85rem;">📄</span><span>phy.doc</span></div>
<div class="tnode file" style="padding:4px 6px;font-size:0.65rem;min-width:68px;" onclick="updateTreeInfo('phy-files', this)" onmouseover="updateTreeInfo('phy-files', this)"><span class="tnode-icon" style="font-size:0.85rem;">📄</span><span>lab.doc</span></div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>

<!-- Dynamic Explanation Panel -->
<div class="wfs-exp-panel">
<div class="wfs-exp-hdr">
<span id="wfs-badge" class="wfs-info-badge root">Root Folder</span>
<h4 id="wfs-title" class="wfs-exp-title">C:\\ (Root Directory)</h4>
</div>
<div id="wfs-desc" class="wfs-exp-desc">
<p>ตำแหน่งบนสุดของพาร์ติชันนั้นๆ (เช่น <code>C:\\</code>) ทำหน้าที่เป็นจุดเริ่มต้นหรือรากของต้นไม้ระบบไฟล์ ทุกๆ โฟลเดอร์และไฟล์อื่นจะสืบทอดที่อยู่ลงมาจากตำแหน่ง Root นี้</p>
</div>
</div>

</div>

<script>
const wfsTreeData = {
  'root': {
    title: 'C:\\\\ (Root Directory)',
    badge: 'Root Folder',
    badgeClass: 'root',
    desc: '<p>โฟลเดอร์ระดับบนสุด (Root) ของไดรฟ์ C: ซึ่งเปรียบเหมือนรากหลักของต้นไม้ระบบไฟล์ เป็นจุดเริ่มต้นของการอ้างอิงตำแหน่ง (Pathing) ไฟล์และไดเรกทอรีทั้งหมดในพาร์ติชันนี้</p>'
  },
  'dos': {
    title: 'DOS Folder (โฟลเดอร์เก็บโปรแกรมระบบ)',
    badge: 'Subdirectory',
    badgeClass: 'sub',
    desc: '<p>โฟลเดอร์ย่อย (Subdirectory) ระดับที่ 1 ใช้สำหรับจัดเก็บไฟล์ชุดคำสั่งและโปรแกรมยูทิลิตี้ของระบบปฏิบัติการ <strong>DOS (Disk Operating System)</strong> เพื่อใช้สั่งงานเครื่องคอมพิวเตอร์ผ่านทาง Text-mode Command Line</p>'
  },
  'dos-files': {
    title: 'DOS Files (ไฟล์ข้อมูลของระบบ DOS)',
    badge: 'Data Files',
    badgeClass: 'file',
    desc: '<p>ไฟล์ข้อมูลระบบทั่วไป (เช่น <code>file1.txt</code>, <code>file2.txt</code>) ภายในโฟลเดอร์ <code>DOS</code> <strong>ใช้จัดเก็บการตั้งค่า ข้อความ หรือชุดคำสั่งย่อย</strong> สำหรับการเรียกใช้บริการระบบงานฝั่ง DOS</p>'
  },
  'xls': {
    title: 'XLS Folder (โฟลเดอร์เก็บสเปรดชีต)',
    badge: 'Subdirectory',
    badgeClass: 'sub',
    desc: '<p>โฟลเดอร์ย่อยระดับที่ 1 ที่สร้างขึ้นมาเพื่อรวบรวมไฟล์ประเภท <strong>ตารางคำนวณและสเปรดชีต (Spreadsheets)</strong> ของโปรแกรม Microsoft Excel</p>'
  },
  'xls-files': {
    title: 'Excel Spreadsheets (ไฟล์ตารางคำนวณ)',
    badge: 'Data Files',
    badgeClass: 'file',
    desc: '<p>ไฟล์เอกสารตารางคำนวณ (เช่น <code>budget.xls</code> สรุปงบประมาณ, <code>sales.xls</code> ยอดขาย) <strong>ใช้จัดเก็บข้อมูลสถิติตัวเลข สูตรคำนวณทางบัญชี และแผนภูมิสรุปยอด</strong> ของบริษัท</p>'
  },
  'doc': {
    title: 'DOC Folder (โฟลเดอร์เก็บเอกสารหลัก)',
    badge: 'Subdirectory',
    badgeClass: 'sub',
    desc: '<p>โฟลเดอร์ย่อยระดับที่ 1 ที่สร้างขึ้นเพื่อรวบรวมและจัดหมวดหมู่ <strong>ไฟล์เอกสารข้อความและพิมพ์รายงานทั่วไป (Word Documents)</strong></p>'
  },
  'doc-files': {
    title: 'Word Documents (ไฟล์รายงานเอกสารพิมพ์)',
    badge: 'Data Files',
    badgeClass: 'file',
    desc: '<p>ไฟล์เอกสารบันทึกข้อความ (เช่น <code>doc1.doc</code>, <code>doc2.doc</code>) <strong>ใช้จัดเก็บรายงานพิมพ์งานพิมพ์ดีด จดหมายบันทึก หรือข้อมูลข้อความทั่วไป</strong> ของโปรแกรม Microsoft Word</p>'
  },
  'eng': {
    title: 'ENG Folder (วิศวกรรมย่อย)',
    badge: 'Subdirectory',
    badgeClass: 'sub',
    desc: '<p>โฟลเดอร์ย่อยระดับที่ 2 ภายใต้ DOC (ตำแหน่งเต็ม: <code>C:\\DOC\\ENG</code>) <strong>ใช้สำหรับเก็บและแยกหมวดหมู่เฉพาะเอกสารงานวิชาการและข้อมูลทางด้านวิศวกรรมศาสตร์ (Engineering)</strong></p>'
  },
  'eng-files': {
    title: 'Engineering Documents (เอกสารวิศวกรรม)',
    badge: 'Data Files',
    badgeClass: 'file',
    desc: '<p>ไฟล์ข้อมูลวิศวกรรม (เช่น <code>eng.doc</code>, <code>info.doc</code>) <strong>ใช้จัดเก็บพิมพ์เขียว บันทึกการคำนวณทางวิศวกรรม โครงสร้างระบบ หรือคู่มือการก่อสร้าง</strong></p>'
  },
  'phy': {
    title: 'PHY Folder (ฟิสิกส์ย่อย)',
    badge: 'Subdirectory',
    badgeClass: 'sub',
    desc: '<p>โฟลเดอร์ย่อยระดับที่ 2 ภายใต้ DOC (ตำแหน่งเต็ม: <code>C:\\DOC\\PHY</code>) <strong>ใช้สำหรับเก็บและแยกหมวดหมู่เฉพาะเอกสารงานสอนและบทความข้อมูลวิชาฟิสิกส์ (Physics)</strong></p>'
  },
  'phy-files': {
    title: 'Physics Reports (เอกสารฟิสิกส์)',
    badge: 'Data Files',
    badgeClass: 'file',
    desc: '<p>ไฟล์ข้อมูลฟิสิกส์ (เช่น <code>phy.doc</code>, <code>lab.doc</code>) <strong>ใช้จัดเก็บรายงานผลการทดลองแลปฟิสิกส์ สูตรคำนวณกลศาสตร์คลื่น หรือข้อมูลทฤษฎีแรงโน้มถ่วง</strong></p>'
  }
};

function updateTreeInfo(key, element) {
  const nodes = document.querySelectorAll('.tree-container .tnode');
  nodes.forEach(n => n.classList.remove('active'));
  element.classList.add('active');

  const data = wfsTreeData[key];
  if (!data) return;

  const badge = document.getElementById('wfs-badge');
  const title = document.getElementById('wfs-title');
  const desc = document.getElementById('wfs-desc');

  badge.textContent = data.badge;
  badge.className = 'wfs-info-badge ' + data.badgeClass;
  title.textContent = data.title;
  desc.innerHTML = data.desc;
}
</script>"""

l168.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=168).update({"content": l168.content})
db.session.commit()
print("Wider node boxes and dynamic explanation hover updating implemented successfully in Block 9!")
