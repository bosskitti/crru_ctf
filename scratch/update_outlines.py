import json
import re
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

# Query lesson 164
lesson = db.session.query(TutorialLesson).filter_by(id=164).first()
if not lesson:
    print("Lesson not found!")
    exit(1)

blocks = json.loads(lesson.content)

# 1. Update Block 1 (System Component Hierarchy)
block_1 = blocks[1]
val_1 = block_1['value']

html_replacement_1 = """<style>
.sys-tree-wrapper{margin:2.5rem 0;display:flex;flex-direction:column;align-items:center;width:100%;}
.sys-tree-scroll{width:100%;overflow-x:auto;padding:24px 12px;background:rgba(15,17,26,0.4);border:1px solid rgba(255,255,255,0.05);border-radius:12px;box-shadow:inset 0 0 20px rgba(0,0,0,0.4);scrollbar-width:thin;scrollbar-color:rgba(0,240,255,0.3) rgba(15,17,26,0.5);}
.sys-tree-scroll::-webkit-scrollbar{height:6px;}
.sys-tree-scroll::-webkit-scrollbar-track{background:rgba(15,17,26,0.5);border-radius:3px;}
.sys-tree-scroll::-webkit-scrollbar-thumb{background:rgba(0,240,255,0.3);border-radius:3px;}
.sys-tree-scroll::-webkit-scrollbar-thumb:hover{background:rgba(0,240,255,0.6);}
.sys-tree-container{min-width:820px;display:flex;flex-direction:column;align-items:center;}
.sys-tree-row{display:flex;justify-content:center;position:relative;width:100%;}
.sys-line-v{width:2px;height:24px;background:linear-gradient(180deg,rgba(255,255,255,0.1) 0%,rgba(255,255,255,0.25) 100%);}
.sys-branches-row{display:flex;justify-content:space-between;width:100%;position:relative;padding-top:24px;}
.sys-branches-row.level-2::before{content:'';position:absolute;top:0;left:16.666%;right:16.666%;height:2px;background:rgba(255,255,255,0.15);}
.sys-sub-branches.level-3-hw::before{content:'';position:absolute;top:0;left:16.666%;right:16.666%;height:2px;background:rgba(255,255,255,0.15);}
.sys-sub-branches.level-3-sw::before{content:'';position:absolute;top:0;left:25%;right:25%;height:2px;background:rgba(255,255,255,0.15);}
.sys-branch-col{display:flex;flex-direction:column;align-items:center;flex:1;position:relative;}
.sys-branch-col::before{content:'';position:absolute;top:-24px;left:50%;width:2px;height:24px;background:rgba(255,255,255,0.15);transform:translateX(-50%);}
.sys-sub-branches{display:flex;justify-content:center;gap:16px;width:100%;position:relative;padding-top:24px;}
.sys-sub-branch-col{display:flex;flex-direction:column;align-items:center;flex:1;position:relative;}
.sys-sub-branch-col::before{content:'';position:absolute;top:-24px;left:50%;width:2px;height:24px;background:rgba(255,255,255,0.15);transform:translateX(-50%);}
.sys-node{background:rgba(255,255,255,0.02);backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:12px 20px;color:#cbd5e1;text-align:center;transition:all 0.3s cubic-bezier(0.4,0,0.2,1);cursor:pointer;box-shadow:0 4px 15px rgba(0,0,0,0.3);display:flex;flex-direction:column;align-items:center;justify-content:center;user-select:none;}
.sys-node:hover{transform:translateY(-4px);color:#ffffff;}
.sys-node .node-icon{font-size:1.3rem;margin-bottom:6px;transition:all 0.3s ease;}
.sys-node .node-title{font-weight:600;font-size:0.95rem;letter-spacing:0.03em;}
.sys-node.type-computer{background:linear-gradient(135deg,rgba(0,240,255,0.1) 0%,rgba(171,32,253,0.1) 100%);border:1.5px solid rgba(0,240,255,0.3);box-shadow:0 0 20px rgba(0,240,255,0.08);width:160px;}
.sys-node.type-computer .node-icon{color:#00f0ff;text-shadow:0 0 10px rgba(0,240,255,0.5);}
.sys-node.type-computer:hover{border-color:#00f0ff;box-shadow:0 0 25px rgba(0,240,255,0.3),0 0 35px rgba(171, 32, 253, 0.2);}
.sys-node.type-hardware{border:1px solid rgba(0,240,255,0.25);background:rgba(0,240,255,0.03);width:140px;}
.sys-node.type-hardware .node-icon{color:#00f0ff;}
.sys-node.type-hardware:hover{border-color:#00f0ff;box-shadow:0 0 15px rgba(0,240,255,0.25);background:rgba(0,240,255,0.08);}
.sys-node.type-software{border:1px solid rgba(171,32,253,0.25);background:rgba(171,32,253,0.03);width:140px;}
.sys-node.type-software .node-icon{color:#ab20fd;}
.sys-node.type-software:hover{border-color:#ab20fd;box-shadow:0 0 15px rgba(171,32,253,0.25);background:rgba(171,32,253,0.08);}
.sys-node.type-peopleware{border:1px solid rgba(251,191,36,0.25);background:rgba(251,191,36,0.03);width:140px;}
.sys-node.type-peopleware .node-icon{color:#fbbf24;}
.sys-node.type-peopleware:hover{border-color:#fbbf24;box-shadow:0 0 15px rgba(251,191,36,0.25);background:rgba(251,191,36,0.08);}
.sys-node.type-sub{padding:8px 14px;min-width:90px;border-radius:8px;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);}
.sys-node.type-sub:hover{background:rgba(255,255,255,0.06);border-color:rgba(255,255,255,0.2);}
.sys-node.type-sub.sub-hw{border-color:rgba(0,240,255,0.15);}
.sys-node.type-sub.sub-hw:hover{border-color:rgba(0,240,255,0.6);box-shadow:0 0 10px rgba(0,240,255,0.15);}
.sys-node.type-sub.sub-sw-sys{border-color:rgba(171,32,253,0.25);}
.sys-node.type-sub.sub-sw-sys:hover{border-color:#ab20fd;box-shadow:0 0 10px rgba(171,32,253,0.2);}
.sys-node.type-sub.sub-sw-app{border-color:rgba(244,114,182,0.25);}
.sys-node.type-sub.sub-sw-app:hover{border-color:#f472b6;box-shadow:0 0 10px rgba(244,114,182,0.2);}
.sys-node.type-os{border:1px solid rgba(255,0,127,0.3);background:rgba(255,0,127,0.03);width:155px;}
.sys-node.type-os .node-icon{color:#ff007f;}
.sys-node.type-os:hover{border-color:#ff007f;box-shadow:0 0 18px rgba(255,0,127,0.3);background:rgba(255,0,127,0.08);}
.sys-desc-panel{margin-top:1.5rem;background:rgba(15,17,26,0.7);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:14px 20px;width:100%;max-width:820px;min-height:80px;display:flex;align-items:center;gap:16px;box-shadow:0 6px 20px rgba(0,0,0,0.4);transition:all 0.3s ease;}
.sys-desc-badge{font-weight:800;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.12em;color:#8a94a6;border-right:2px solid rgba(255,255,255,0.1);padding-right:16px;height:100%;display:flex;align-items:center;white-space:nowrap;transition:color 0.3s ease;}
.sys-desc-text{font-size:0.95rem;color:#94a3b8;line-height:1.6;transition:color 0.3s ease;}
.sys-scroll-hint{display:none;font-size:0.75rem;color:#8a94a6;margin-bottom:8px;align-items:center;gap:6px;}
@media (max-width:850px){.sys-scroll-hint{display:flex;}}
</style>
<div class="sys-tree-wrapper">
<div class="sys-scroll-hint"><i class="fas fa-arrows-alt-h"></i> <span>เลื่อนในแนวนอนเพื่อดูโครงสร้างระบบทั้งหมด</span></div>
<div class="sys-tree-scroll">
<div class="sys-tree-container">
<div class="sys-tree-row">
<div class="sys-node type-computer" onmouseover="updateSysDesc('Computer', 'ระบบคอมพิวเตอร์โดยรวม ประกอบไปด้วยส่วนสำคัญ 3 ส่วนคือ Hardware, Software และ Peopleware ทำงานร่วมกันเพื่อประมวลผลข้อมูล', '#00f0ff')" onmouseout="resetSysDesc()"><div class="node-icon"><i class="fas fa-desktop"></i></div><div class="node-title">Computer</div></div>
</div>
<div class="sys-line-v"></div>
<div class="sys-branches-row level-2">
<div class="sys-branch-col">
<div class="sys-node type-hardware" onmouseover="updateSysDesc('Hardware', 'อุปกรณ์ทางกายภาพหรือชิ้นส่วนคอมพิวเตอร์ที่สัมผัสได้ เช่น เมนบอร์ด อุปกรณ์ประมวลผล หน่วยความจำ และอุปกรณ์เชื่อมต่อภายนอก', '#00f0ff')" onmouseout="resetSysDesc()"><div class="node-icon"><i class="fas fa-microchip"></i></div><div class="node-title">Hardware</div></div>
<div class="sys-line-v"></div>
<div class="sys-sub-branches level-3-hw">
<div class="sys-sub-branch-col"><div class="sys-node type-sub sub-hw" onmouseover="updateSysDesc('CPU (Central Processing Unit)', 'หน่วยประมวลผลกลาง ทำหน้าที่เสมือนสมองของคอมพิวเตอร์ในการคำนวณและประมวลผลคำสั่งต่าง ๆ', '#00f0ff')" onmouseout="resetSysDesc()"><div class="node-title">CPU</div></div></div>
<div class="sys-sub-branch-col"><div class="sys-node type-sub sub-hw" onmouseover="updateSysDesc('Memory (หน่วยความจำ)', 'อุปกรณ์สำหรับเก็บข้อมูลและโปรแกรมคำสั่ง แบ่งเป็นหน่วยความจำหลักชั่วคราว (RAM) และหน่วยความจำถาวร (ROM)', '#00f0ff')" onmouseout="resetSysDesc()"><div class="node-title">Memory</div></div></div>
<div class="sys-sub-branch-col"><div class="sys-node type-sub sub-hw" onmouseover="updateSysDesc('I/O (Input/Output)', 'อุปกรณ์นำข้อมูลเข้าและแสดงผล เช่น คีย์บอร์ด เมาส์ หน้าจอ เพื่อให้คอมพิวเตอร์สื่อสารกับผู้ใช้งานได้', '#00f0ff')" onmouseout="resetSysDesc()"><div class="node-title">I/O</div></div></div>
</div>
</div>
<div class="sys-branch-col">
<div class="sys-node type-software" onmouseover="updateSysDesc('Software', 'ชุดคำสั่งหรือชุดคำสั่งโปรแกรมที่ควบคุมการทำงานของฮาร์ดแวร์ แบ่งเป็นระบบปฏิบัติการควบคุมระบบ และแอปพลิเคชันใช้งานเฉพาะด้าน', '#ab20fd')" onmouseout="resetSysDesc()"><div class="node-icon"><i class="fas fa-code"></i></div><div class="node-title">Software</div></div>
<div class="sys-line-v"></div>
<div class="sys-sub-branches level-3-sw">
<div class="sys-sub-branch-col">
<div class="sys-node type-sub sub-sw-sys" onmouseover="updateSysDesc('System Software', 'ซอฟต์แวร์ระบบที่ควบคุมการทำงานพื้นฐานของเครื่องและประสานงานอุปกรณ์ เช่น ระบบปฏิบัติการ (OS) ไดรเวอร์อุปกรณ์ และยูทิลิตี้ต่าง ๆ', '#ab20fd')" onmouseout="resetSysDesc()"><div class="node-title">System SW</div></div>
<div class="sys-line-v"></div>
<div class="sys-node type-os" onmouseover="updateSysDesc('Operating System (OS)', 'ระบบปฏิบัติการที่จัดการฮาร์ดแวร์ จัดสรรทรัพยากร และเป็นตัวกลางให้บริการแก่แอปพลิเคชัน เช่น Windows, Linux, macOS', '#ff007f')" onmouseout="resetSysDesc()"><div class="node-icon"><i class="fas fa-cogs"></i></div><div class="node-title">Operating System</div></div>
</div>
<div class="sys-sub-branch-col"><div class="sys-node type-sub sub-sw-app" onmouseover="updateSysDesc('Application Software', 'ซอฟต์แวร์ประยุกต์หรือโปรแกรมที่พัฒนาขึ้นมาเพื่อการใช้งานเฉพาะทาง เช่น เว็บเบราว์เซอร์ โปรแกรมพิมพ์งาน เกม เครื่องมือแฮกต่าง ๆ', '#f472b6')" onmouseout="resetSysDesc()"><div class="node-title">Application SW</div></div></div>
</div>
</div>
<div class="sys-branch-col">
<div class="sys-node type-peopleware" onmouseover="updateSysDesc('Peopleware', 'บุคลากรที่เกี่ยวข้องกับการทำงานของคอมพิวเตอร์ ตั้งแต่ผู้พัฒนาซอฟต์แวร์ นักวิเคราะห์ระบบ ผู้ดูแลความปลอดภัย ไปจนถึงผู้ใช้งานทั่วไป', '#fbbf24')" onmouseout="resetSysDesc()"><div class="node-icon"><i class="fas fa-users"></i></div><div class="node-title">Peopleware</div></div>
</div>
</div>
</div>
</div>
<div class="sys-desc-panel" id="sys-panel-el">
<div class="sys-desc-badge" id="sys-badge-el">System Info</div>
<div class="sys-desc-text" id="sys-desc-el">เลื่อนเมาส์ไปชี้ที่แต่ละส่วนประกอบของระบบคอมพิวเตอร์ เพื่ออ่านรายละเอียดเพิ่มเติม</div>
</div>
</div>
<script>
function updateSysDesc(title, text, color) {
  const badge = document.getElementById('sys-badge-el');
  const desc = document.getElementById('sys-desc-el');
  const panel = document.getElementById('sys-panel-el');
  if (badge && desc) {
    badge.textContent = title;
    badge.style.color = color;
    desc.textContent = text;
    desc.style.color = '#ffffff';
    if (panel) {
      panel.style.borderColor = color;
      panel.style.boxShadow = '0 0 20px ' + color + '40, 0 6px 20px rgba(0, 0, 0, 0.4)';
    }
  }
}
function resetSysDesc() {
  const badge = document.getElementById('sys-badge-el');
  const desc = document.getElementById('sys-desc-el');
  const panel = document.getElementById('sys-panel-el');
  if (badge && desc) {
    badge.textContent = 'System Info';
    badge.style.color = '#8a94a6';
    desc.textContent = 'เลื่อนเมาส์ไปชี้ที่แต่ละส่วนประกอบของระบบคอมพิวเตอร์ เพื่ออ่านรายละเอียดเพิ่มเติม';
    desc.style.color = '#94a3b8';
    if (panel) {
      panel.style.borderColor = 'rgba(255, 255, 255, 0.08)';
      panel.style.boxShadow = '0 6px 20px rgba(0, 0, 0, 0.4)';
    }
  }
}
</script>"""

# Replace the HTML block (since it is already HTML, we will match from '<style>' to '</script>' tag)
pattern_1 = r"<style>.*?</script>"
modified_val_1 = re.sub(pattern_1, html_replacement_1, val_1, flags=re.DOTALL)
block_1['value'] = modified_val_1
blocks[1] = block_1

# 2. Update Block 3 (OS Layers Vertical Flow)
block_3 = blocks[3]
val_3 = block_3['value']

html_replacement_3 = """<style>
.os-layers-wrapper{margin:2.5rem 0;display:flex;flex-direction:column;align-items:center;width:100%;}
.os-layers-container{width:100%;max-width:500px;background:rgba(15,17,26,0.4);border:1px solid rgba(255,255,255,0.05);border-radius:12px;padding:24px;box-shadow:inset 0 0 20px rgba(0,0,0,0.4);display:flex;flex-direction:column;align-items:center;gap:8px;}
.os-layer-card{width:100%;background:rgba(255,255,255,0.02);backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:14px 20px;color:#cbd5e1;display:flex;align-items:center;gap:16px;transition:all 0.3s cubic-bezier(0.4,0,0.2,1);cursor:pointer;box-shadow:0 4px 15px rgba(0,0,0,0.3);user-select:none;}
.os-layer-card:hover{transform:translateY(-2px) scale(1.02);color:#ffffff;}
.os-layer-icon{font-size:1.5rem;width:40px;height:40px;display:flex;align-items:center;justify-content:center;border-radius:8px;background:rgba(255,255,255,0.03);transition:all 0.3s ease;}
.os-layer-details{display:flex;flex-direction:column;text-align:left;}
.os-layer-title{font-weight:700;font-size:1.05rem;letter-spacing:0.02em;}
.os-layer-subtitle{font-size:0.75rem;color:#8a94a6;text-transform:uppercase;margin-top:2px;}
.os-layer-card.type-user{border-color:rgba(251,191,36,0.25);}
.os-layer-card.type-user .os-layer-icon{color:#fbbf24;background:rgba(251,191,36,0.05);}
.os-layer-card.type-user:hover{border-color:#fbbf24;box-shadow:0 0 15px rgba(251,191,36,0.25);}
.os-layer-card.type-app{border-color:rgba(171,32,253,0.25);}
.os-layer-card.type-app .os-layer-icon{color:#ab20fd;background:rgba(171,32,253,0.05);}
.os-layer-card.type-app:hover{border-color:#ab20fd;box-shadow:0 0 15px rgba(171,32,253,0.25);}
.os-layer-card.type-os{border-color:rgba(255,0,127,0.3);}
.os-layer-card.type-os .os-layer-icon{color:#ff007f;background:rgba(255,0,127,0.05);}
.os-layer-card.type-os:hover{border-color:#ff007f;box-shadow:0 0 18px rgba(255,0,127,0.3);}
.os-layer-card.type-hw{border-color:rgba(0,240,255,0.25);}
.os-layer-card.type-hw .os-layer-icon{color:#00f0ff;background:rgba(0,240,255,0.05);}
.os-layer-card.type-hw:hover{border-color:#00f0ff;box-shadow:0 0 15px rgba(0,240,255,0.25);}
.os-layer-connector{display:flex;justify-content:center;align-items:center;height:28px;color:#00f0ff;animation:pulse-glow-arrow 2s infinite ease-in-out;}
@keyframes pulse-glow-arrow{0%{opacity:0.3;transform:scale(0.9);}50%{opacity:1;transform:scale(1.1);filter:drop-shadow(0 0 5px #00f0ff);}100%{opacity:0.3;transform:scale(0.9);}}
.os-layer-connector i{font-size:1.1rem;}
.os-layers-desc-panel{margin-top:1.5rem;background:rgba(15,17,26,0.7);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:14px 20px;width:100%;max-width:500px;min-height:80px;display:flex;align-items:center;gap:16px;box-shadow:0 6px 20px rgba(0,0,0,0.4);transition:all 0.3s ease;}
.os-layers-desc-badge{font-weight:800;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.12em;color:#8a94a6;border-right:2px solid rgba(255,255,255,0.1);padding-right:16px;height:100%;display:flex;align-items:center;white-space:nowrap;transition:color 0.3s ease;}
.os-layers-desc-text{font-size:0.95rem;color:#94a3b8;line-height:1.6;transition:color 0.3s ease;}
</style>
<div class="os-layers-wrapper">
<div class="os-layers-container">
<div class="os-layer-card type-user" onmouseover="updateOSLayerDesc('User (ผู้ใช้งาน)', 'ผู้ป้อนคำสั่งและโต้ตอบกับแอปพลิเคชันผ่าน UI หรือ Command Line เพื่อสั่งประมวลผลข้อมูล', '#fbbf24')" onmouseout="resetOSLayerDesc()">
<div class="os-layer-icon"><i class="fas fa-user-shield"></i></div>
<div class="os-layer-details">
<div class="os-layer-title">User</div>
<div class="os-layer-subtitle">ผู้ใช้ / ผู้ควบคุมระบบ</div>
</div>
</div>
<div class="os-layer-connector"><i class="fas fa-chevron-down"></i></div>
<div class="os-layer-card type-app" onmouseover="updateOSLayerDesc('Application (แอปพลิเคชัน)', 'โปรแกรมที่ผู้ใช้งานรันเพื่อเป้าหมายเฉพาะด้าน เช่น Web Browser, Terminal, Software Development Kit และโปรแกรมแฮกข้อมูล', '#ab20fd')" onmouseout="resetOSLayerDesc()">
<div class="os-layer-icon"><i class="fas fa-laptop-code"></i></div>
<div class="os-layer-details">
<div class="os-layer-title">Application</div>
<div class="os-layer-subtitle">โปรแกรมประยุกต์ / ซอฟต์แวร์ใช้งาน</div>
</div>
</div>
<div class="os-layer-connector"><i class="fas fa-chevron-down"></i></div>
<div class="os-layer-card type-os" onmouseover="updateOSLayerDesc('Operating System (OS)', 'ระบบปฏิบัติการที่ทำหน้าที่ประสานงานระหว่างแอปพลิเคชันกับฮาร์ดแวร์ จัดการการประมวลผล หน่วยความจำ และความปลอดภัย', '#ff007f')" onmouseout="resetOSLayerDesc()">
<div class="os-layer-icon"><i class="fas fa-cogs"></i></div>
<div class="os-layer-details">
<div class="os-layer-title">Operating System</div>
<div class="os-layer-subtitle">ระบบปฏิบัติการ (ตัวกลางประสานงาน)</div>
</div>
</div>
<div class="os-layer-connector"><i class="fas fa-chevron-down"></i></div>
<div class="os-layer-card type-hw" onmouseover="updateOSLayerDesc('Hardware (ฮาร์ดแวร์)', 'ชิ้นส่วนกายภาพและแผงวงจรอิเล็กทรอนิกส์ เช่น CPU, RAM, Disk, เครือข่ายการรับส่งข้อมูล ที่ประมวลผลตามคำสั่งของ OS', '#00f0ff')" onmouseout="resetOSLayerDesc()">
<div class="os-layer-icon"><i class="fas fa-microchip"></i></div>
<div class="os-layer-details">
<div class="os-layer-title">Hardware</div>
<div class="os-layer-subtitle">อุปกรณ์เครื่อง / ชิ้นส่วนกายภาพ</div>
</div>
</div>
</div>
<div class="os-layers-desc-panel" id="os-panel-el">
<div class="os-layers-desc-badge" id="os-badge-el">Layer Info</div>
<div class="os-layers-desc-text" id="os-desc-el">เลื่อนเมาส์ไปชี้ที่แต่ละชั้นสถาปัตยกรรม เพื่ออ่านคำอธิบายหน้าที่</div>
</div>
</div>
<script>
function updateOSLayerDesc(title, text, color) {
  const badge = document.getElementById('os-badge-el');
  const desc = document.getElementById('os-desc-el');
  const panel = document.getElementById('os-panel-el');
  if (badge && desc) {
    badge.textContent = title;
    badge.style.color = color;
    desc.textContent = text;
    desc.style.color = '#ffffff';
    if (panel) {
      panel.style.borderColor = color;
      panel.style.boxShadow = '0 0 20px ' + color + '40, 0 6px 20px rgba(0, 0, 0, 0.4)';
    }
  }
}
function resetOSLayerDesc() {
  const badge = document.getElementById('os-badge-el');
  const desc = document.getElementById('os-desc-el');
  const panel = document.getElementById('os-panel-el');
  if (badge && desc) {
    badge.textContent = 'Layer Info';
    badge.style.color = '#8a94a6';
    desc.textContent = 'เลื่อนเมาส์ไปชี้ที่แต่ละชั้นสถาปัตยกรรม เพื่ออ่านคำอธิบายหน้าที่';
    desc.style.color = '#94a3b8';
    if (panel) {
      panel.style.borderColor = 'rgba(255, 255, 255, 0.08)';
      panel.style.boxShadow = '0 6px 20px rgba(0, 0, 0, 0.4)';
    }
  }
}
</script>"""

# Replace the HTML block (since it is already HTML, we will match from '<style>' to '</script>' tag)
pattern_3 = r"<style>.*?</script>"
modified_val_3 = re.sub(pattern_3, html_replacement_3, val_3, flags=re.DOTALL)
block_3['value'] = modified_val_3
blocks[3] = block_3

# Save and Commit database
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=164).update({"content": lesson.content})
db.session.commit()
print("Outlines updated dynamically for both diagrams!")
