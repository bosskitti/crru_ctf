import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

# Query lesson 165
lesson = db.session.query(TutorialLesson).filter_by(id=165).first()
if not lesson:
    print("Lesson not found!")
    exit(1)

blocks = json.loads(lesson.content)
block_7 = blocks[7]

# The HTML replacement code for the Linux Directory Tree (completely flat, 0-indentation)
html_tree = """<style>
.tree-layout-wrapper{margin:2.5rem 0;display:flex;flex-direction:column;align-items:center;width:100%;}
.tree-scroll-container{width:100%;overflow-x:auto;padding:24px 12px;background:rgba(15,17,26,0.4);border:1px solid rgba(255,255,255,0.05);border-radius:12px;box-shadow:inset 0 0 20px rgba(0,0,0,0.4);scrollbar-width:thin;scrollbar-color:rgba(0,240,255,0.3) rgba(15,17,26,0.5);}
.tree-scroll-container::-webkit-scrollbar{height:6px;}
.tree-scroll-container::-webkit-scrollbar-track{background:rgba(15,17,26,0.5);border-radius:3px;}
.tree-scroll-container::-webkit-scrollbar-thumb{background:rgba(0,240,255,0.3);border-radius:3px;}
.tree-scroll-container::-webkit-scrollbar-thumb:hover{background:rgba(0,240,255,0.6);}
.tree-chart{min-width:1250px;display:flex;flex-direction:column;align-items:center;padding:10px 0;position:relative;}
.tree-card{background:rgba(255,255,255,0.02);backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,0.08);border-radius:6px;padding:6px 10px;color:#cbd5e1;text-align:center;font-size:0.85rem;font-weight:600;box-shadow:0 4px 10px rgba(0,0,0,0.3);transition:all 0.3s ease;user-select:none;cursor:pointer;white-space:nowrap;}
.tree-card:hover{transform:translateY(-2px);color:#ffffff;}
.tree-card.root-node{border-color:#fbbf24;background:rgba(251,191,36,0.04);color:#fbbf24;font-size:1rem;padding:8px 16px;box-shadow:0 0 15px rgba(251,191,36,0.1);}
.tree-card.root-node:hover{border-color:#fbbf24;box-shadow:0 0 20px rgba(251, 191, 36, 0.3);}
.tree-card.lvl2-node{border-color:#00c0ff;background:rgba(0,192,255,0.03);color:#00c0ff;}
.tree-card.lvl2-node:hover{border-color:#00c0ff;box-shadow:0 0 12px rgba(0, 192, 255, 0.25);}
.tree-card.lvl3-node{border-color:#3ddc84;background:rgba(61, 220, 132, 0.03);color:#3ddc84;}
.tree-card.lvl3-node:hover{border-color:#3ddc84;box-shadow:0 0 12px rgba(61, 220, 132, 0.25);}
.line-v-connector{width:2px;height:20px;background:rgba(255, 255, 255, 0.15);}
.lvl2-row{display:flex;justify-content:space-between;width:100%;position:relative;padding-top:20px;}
.lvl2-row::before{content:'';position:absolute;top:0;left:3.333%;right:3.333%;height:2px;background:rgba(255, 255, 255, 0.15);}
.lvl2-col{display:flex;flex-direction:column;align-items:center;width:6.666%;position:relative;}
.lvl2-col::before{content:'';position:absolute;top:-20px;left:50%;width:2px;height:20px;background:rgba(255, 255, 255, 0.15);transform:translateX(-50%);}
.lvl3-tree-container{display:flex;flex-direction:column;align-items:center;position:absolute;top:30px;width:280px;z-index:10;}
.lvl3-row{display:flex;justify-content:space-between;width:100%;position:relative;padding-top:20px;}
.lvl3-row::before{content:'';position:absolute;top:0;left:12.5%;right:12.5%;height:2px;background:rgba(255, 255, 255, 0.15);}
.lvl3-col{display:flex;flex-direction:column;align-items:center;width:25%;position:relative;}
.lvl3-col::before{content:'';position:absolute;top:-20px;left:50%;width:2px;height:20px;background:rgba(255, 255, 255, 0.15);transform:translateX(-50%);}
.tree-side-text-card{background:linear-gradient(135deg, rgba(15, 17, 26, 0.6) 0%, rgba(30, 20, 45, 0.4) 100%);border:1px solid rgba(255, 255, 255, 0.08);border-radius:12px;padding:20px;width:100%;max-width:820px;margin-top:20px;display:flex;align-items:center;gap:16px;box-shadow:0 4px 15px rgba(0, 0, 0, 0.2);}
.tree-side-text-icon{font-size:2.2rem;color:#fbbf24;text-shadow:0 0 10px rgba(251, 191, 36, 0.4);}
.tree-side-text-content{font-size:1.15rem;font-weight:700;line-height:1.6;color:#ffffff;text-align:left;}
.tree-side-text-content span.highlight{color:#ff007f;text-shadow:0 0 8px rgba(255, 0, 127, 0.3);}
.tree-hover-info{margin-top:15px;background:rgba(15, 17, 26, 0.7);border:1px solid rgba(255, 255, 255, 0.05);border-radius:10px;padding:14px 20px;width:100%;max-width:820px;min-height:70px;display:flex;align-items:center;gap:16px;box-shadow:0 6px 20px rgba(0, 0, 0, 0.4);transition:all 0.3s ease;}
.tree-hover-badge{font-weight:800;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.12em;color:#8a94a6;border-right:2px solid rgba(255, 255, 255, 0.1);padding-right:16px;height:100%;display:flex;align-items:center;white-space:nowrap;transition:color 0.3s ease;}
.tree-hover-desc{font-size:0.95rem;color:#94a3b8;line-height:1.6;transition:color 0.3s ease;}
</style>
<div class="tree-layout-wrapper">
<div class="tree-side-text-card">
<div class="tree-side-text-icon"><i class="fas fa-sitemap"></i></div>
<div class="tree-side-text-content">Linux uses a <span class="highlight">tree structure (hierarchy)</span> to store and organize files</div>
</div>
<div class="tree-scroll-container">
<div class="tree-chart" style="height: 190px;">
<div class="tree-card root-node" onmouseover="updateTreeDesc('/', 'Root directory - จุดเริ่มต้นและรากของระบบไฟล์ทั้งหมดใน Linux', '#fbbf24')" onmouseout="resetTreeDesc()">/</div>
<div class="line-v-connector"></div>
<div class="lvl2-row">
<div class="lvl2-col"><div class="tree-card lvl2-node" onmouseover="updateTreeDesc('/bin/', 'Binary - ไดเรกทอรีเก็บคำสั่งโปรแกรมพื้นฐานที่จำเป็นต่อผู้ใช้งานทุกคน', '#00c0ff')" onmouseout="resetTreeDesc()">/bin/</div></div>
<div class="lvl2-col"><div class="tree-card lvl2-node" onmouseover="updateTreeDesc('/opt/', 'Optional - เก็บโปรแกรมซอฟต์แวร์เสริมและแอปพลิเคชันจากบุคคลที่สาม', '#00c0ff')" onmouseout="resetTreeDesc()">/opt/</div></div>
<div class="lvl2-col"><div class="tree-card lvl2-node" onmouseover="updateTreeDesc('/boot/', 'Boot - ไดเรกทอรีเก็บไฟล์ที่ใช้ในการบูตระบบปฏิบัติการ เช่น GRUB, Linux Kernel', '#00c0ff')" onmouseout="resetTreeDesc()">/boot/</div></div>
<div class="lvl2-col"><div class="tree-card lvl2-node" onmouseover="updateTreeDesc('/root/', 'Root user home - โโฟลเดอร์ส่วนตัวของสิทธิ์ผู้ดูแลระบบหลัก (root)', '#00c0ff')" onmouseout="resetTreeDesc()">/root/</div></div>
<div class="lvl2-col"><div class="tree-card lvl2-node" onmouseover="updateTreeDesc('/dev/', 'Devices - แหล่งรวมไฟล์ตำแหน่งอุปกรณ์ต่างๆ ของระบบ เช่น ฮาร์ดดิสก์ ไดรฟ์ต่างๆ', '#00c0ff')" onmouseout="resetTreeDesc()">/dev/</div></div>
<div class="lvl2-col"><div class="tree-card lvl2-node" onmouseover="updateTreeDesc('/sbin/', 'System Binaries - เก็บโปรแกรมรันระบบที่สำคัญเฉพาะของสิทธิ์ผู้ดูแลระบบ (Admin)', '#00c0ff')" onmouseout="resetTreeDesc()">/sbin/</div></div>
<div class="lvl2-col"><div class="tree-card lvl2-node" onmouseover="updateTreeDesc('/etc/', 'Etcetera - แหล่งรวมไฟล์การกำหนดค่า (Configuration Files) ของระบบทั้งหมด', '#00c0ff')" onmouseout="resetTreeDesc()">/etc/</div></div>
<div class="lvl2-col"><div class="tree-card lvl2-node" onmouseover="updateTreeDesc('/srv/', 'Services - เก็บข้อมูลสำหรับการให้บริการต่างๆ บนเซิร์ฟเวอร์ เช่น FTP, Web server data', '#00c0ff')" onmouseout="resetTreeDesc()">/srv/</div></div>
<div class="lvl2-col"><div class="tree-card lvl2-node" onmouseover="updateTreeDesc('/home/', 'Home directory - โฟลเดอร์บ้านของผู้ใช้ทั่วไป (Regular Users) ในระบบ', '#00c0ff')" onmouseout="resetTreeDesc()">/home/</div></div>
<div class="lvl2-col"><div class="tree-card lvl2-node" onmouseover="updateTreeDesc('/tmp/', 'Temporary - โฟลเดอร์เก็บไฟล์ชั่วคราวที่จะล้างออกโดยอัตโนมัติเมื่อรีสตาร์ทเครื่อง', '#00c0ff')" onmouseout="resetTreeDesc()">/tmp/</div></div>
<div class="lvl2-col"><div class="tree-card lvl2-node" onmouseover="updateTreeDesc('/lib/', 'Libraries - แฟ้มรวมไลบรารีระบบและโมดูลเคอร์เนลที่จำเป็นในการบูต', '#00c0ff')" onmouseout="resetTreeDesc()">/lib/</div></div>
<div class="lvl2-col" style="position: relative;">
<div class="tree-card lvl2-node" onmouseover="updateTreeDesc('/usr/', 'User - เก็บโปรแกรมและไฟล์ไลบรารีขนาดใหญ่ที่ผู้ใช้ทั่วไปใช้งาน (เป็นโหมด Read-Only)', '#00c0ff')" onmouseout="resetTreeDesc()">/usr/</div>
<div class="line-v-connector"></div>
<div class="lvl3-tree-container" style="left: -100px;">
<div class="lvl3-row">
<div class="lvl3-col"><div class="tree-card lvl3-node" onmouseover="updateTreeDesc('/usr/bin/', 'คำสั่งการทำงานส่วนใหญ่ของผู้ใช้ทั่วไป (User Executables)', '#3ddc84')" onmouseout="resetTreeDesc()">/bin/</div></div>
<div class="lvl3-col"><div class="tree-card lvl3-node" onmouseover="updateTreeDesc('/usr/include/', 'ไฟล์ Header (.h) มาตรฐานสำหรับเขียนโปรแกรมภาษา C/C++', '#3ddc84')" onmouseout="resetTreeDesc()">/include/</div></div>
<div class="lvl3-col"><div class="tree-card lvl3-node" onmouseover="updateTreeDesc('/usr/lib/', 'ไฟล์ออบเจ็กต์และไลบรารีมาตรฐานสำหรับโปรแกรมต่างๆ', '#3ddc84')" onmouseout="resetTreeDesc()">/lib/</div></div>
<div class="lvl3-col"><div class="tree-card lvl3-node" onmouseover="updateTreeDesc('/usr/sbin/', 'คำสั่งควบคุมระบบที่เรียกใช้โดยผู้ดูแลระบบและแอปพลิเคชันระบบ', '#3ddc84')" onmouseout="resetTreeDesc()">/sbin/</div></div>
</div>
</div>
</div>
<div class="lvl2-col"><div class="tree-card lvl2-node" onmouseover="updateTreeDesc('/media/', 'Media - แหล่งเชื่อมต่ออุปกรณ์จัดเก็บข้อมูลแบบถอดเสียบได้ เช่น แฟลชไดรฟ์, แผ่น CD-ROM', '#00c0ff')" onmouseout="resetTreeDesc()">/media/</div></div>
<div class="lvl2-col" style="position: relative;">
<div class="tree-card lvl2-node" onmouseover="updateTreeDesc('/var/', 'Variable - แหล่งรวมข้อมูลที่มีการเปลี่ยนแปลงบ่อย เช่น ล็อกไฟล์ (Log files) และสปูลอีเมล', '#00c0ff')" onmouseout="resetTreeDesc()">/var/</div>
<div class="line-v-connector"></div>
<div class="lvl3-tree-container" style="left: -100px;">
<div class="lvl3-row">
<div class="lvl3-col"><div class="tree-card lvl3-node" onmouseover="updateTreeDesc('/var/cache/', 'พื้นที่เก็บข้อมูลแคชสำหรับแอปพลิเคชันต่างๆ', '#3ddc84')" onmouseout="resetTreeDesc()">/cache/</div></div>
<div class="lvl3-col"><div class="tree-card lvl3-node" onmouseover="updateTreeDesc('/var/log/', 'ล็อกไฟล์ของระบบที่บันทึกเหตุการณ์ต่างๆ ที่เกิดขึ้น (เช่น การพยายามเข้าระบบ)', '#3ddc84')" onmouseout="resetTreeDesc()">/log/</div></div>
<div class="lvl3-col"><div class="tree-card lvl3-node" onmouseover="updateTreeDesc('/var/spool/', 'พื้นที่พักข้อมูลชั่วคราวเพื่อรอส่งต่อ เช่น สปูลงานพิมพ์ (Printers) หรือเมลสปูล', '#3ddc84')" onmouseout="resetTreeDesc()">/spool/</div></div>
<div class="lvl3-col"><div class="tree-card lvl3-node" onmouseover="updateTreeDesc('/var/tmp/', 'โฟลเดอร์เก็บไฟล์ข้อมูลชั่วคราวที่จะไม่ล้างออกโดยอัตโนมัติเมื่อรีบูตระบบ', '#3ddc84')" onmouseout="resetTreeDesc()">/tmp/</div></div>
</div>
</div>
</div>
<div class="lvl2-col"><div class="tree-card lvl2-node" onmouseover="updateTreeDesc('/mnt/', 'Mount - โฟลเดอร์สำหรับเมาท์และเข้าถึงระบบไฟล์ชั่วคราวอื่นๆ', '#00c0ff')" onmouseout="resetTreeDesc()">/mnt/</div></div>
</div>
</div>
</div>
<div class="tree-hover-info" id="tree-info-panel-el">
<div class="tree-hover-badge" id="tree-badge-el">System Path</div>
<div class="tree-hover-desc" id="tree-desc-el">เลื่อนเมาส์ไปชี้ที่แต่ละโฟลเดอร์ในแผนผัง เพื่ออ่านคำอธิบายหน้าที่ในระบบ Linux</div>
</div>
</div>
<script>
function updateTreeDesc(title, text, color) {
  const badge = document.getElementById('tree-badge-el');
  const desc = document.getElementById('tree-desc-el');
  const panel = document.getElementById('tree-info-panel-el');
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
function resetTreeDesc() {
  const badge = document.getElementById('tree-badge-el');
  const desc = document.getElementById('tree-desc-el');
  const panel = document.getElementById('tree-info-panel-el');
  if (badge && desc) {
    badge.textContent = 'System Path';
    badge.style.color = '#8a94a6';
    desc.textContent = 'เลื่อนเมาส์ไปชี้ที่แต่ละโฟลเดอร์ในแผนผัง เพื่ออ่านคำอธิบายหน้าที่ในระบบ Linux';
    desc.style.color = '#94a3b8';
    if (panel) {
      panel.style.borderColor = 'rgba(255, 255, 255, 0.08)';
      panel.style.boxShadow = '0 6px 20px rgba(0, 0, 0, 0.4)';
    }
  }
}
</script>"""

block_7['value'] = html_tree
blocks[7] = block_7

# Save and Commit database
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
db.session.commit()
print("Linux Directory Tree Diagram added successfully!")
