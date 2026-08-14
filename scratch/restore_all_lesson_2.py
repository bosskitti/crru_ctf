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

# 1. Update Block 7 with the Bilingual Staggered Tree Diagram (flat HTML structure, 0-indentation)
html_tree_bilingual = """<style>
.tree-wrapper-v6{margin:2.5rem 0;display:flex;flex-direction:column;align-items:center;width:100%;}
.flex-tree-scroll{width:100%;overflow-x:auto;padding:24px 12px;background:rgba(15,17,26,0.4);border:1px solid rgba(255,255,255,0.05);border-radius:12px;box-shadow:inset 0 0 20px rgba(0,0,0,0.4);scrollbar-width:thin;scrollbar-color:rgba(0,240,255,0.3) rgba(15,17,26,0.5);}
.flex-tree-scroll::-webkit-scrollbar{height:6px;}
.flex-tree-scroll::-webkit-scrollbar-track{background:rgba(15,17,26,0.5);border-radius:3px;}
.flex-tree-scroll::-webkit-scrollbar-thumb{background:rgba(0,240,255,0.3);border-radius:3px;}
.flex-tree-scroll::-webkit-scrollbar-thumb:hover{background:rgba(0,240,255,0.6);}
.flex-tree-chart{min-width:1450px;display:flex;flex-direction:column;align-items:center;position:relative;padding:20px 0;}
.ft-root-box{display:flex;flex-direction:column;align-items:center;margin-bottom:24px;z-index:2;}
.ft-main-trunk{position:absolute;top:104px;left:3.333%;right:3.333%;height:2px;background:rgba(255,255,255,0.15);z-index:1;}
.ft-grid{display:flex;justify-content:space-between;width:100%;z-index:2;position:relative;}
.ft-col{display:flex;flex-direction:column;align-items:center;position:relative;flex:1 1 0;min-width:60px;}
.ft-col.has-subtree{flex:0 0 280px;min-width:280px;}
.ft-col.type-top{padding-bottom:50px;}
.ft-col.type-top::before{content:'';position:absolute;bottom:0;left:50%;width:2px;height:50px;background:rgba(255,255,255,0.15);transform:translateX(-50%);}
.ft-col.type-bottom{padding-top:50px;}
.ft-col.type-bottom::before{content:'';position:absolute;top:0;left:50%;width:2px;height:50px;background:rgba(255,255,255,0.15);transform:translateX(-50%);}
.ft-sub-wrapper{display:flex;flex-direction:column;align-items:center;width:100%;margin-top:16px;position:relative;}
.ft-sub-wrapper::before{content:'';position:absolute;top:-16px;left:50%;width:2px;height:16px;background:rgba(255,255,255,0.15);transform:translateX(-50%);}
.ft-sub-row{display:flex;justify-content:space-between;width:100%;position:relative;padding-top:16px;}
.ft-sub-row::before{content:'';position:absolute;top:0;left:12.5%;right:12.5%;height:2px;background:rgba(255,255,255,0.15);}
.ft-sub-col{width:23%;display:flex;flex-direction:column;align-items:center;position:relative;}
.ft-sub-col::before{content:'';position:absolute;top:-16px;left:50%;width:2px;height:16px;background:rgba(255,255,255,0.15);transform:translateX(-50%);}
.ft-card{font-size:0.8rem;padding:6px 10px;border-radius:6px;text-align:center;font-weight:700;width:auto;min-width:60px;cursor:pointer;transition:all 0.3s ease;white-space:nowrap;}
.ft-card:hover{transform:translateY(-2px);color:#ffffff;}
.ft-card.type-root{border:1px solid #fbbf24;background:rgba(251,191,36,0.05);color:#fbbf24;font-size:1.05rem;padding:8px 20px;box-shadow:0 0 15px rgba(251, 191, 36, 0.1);}
.ft-card.type-root:hover{box-shadow:0 0 20px rgba(251, 191, 36, 0.35);}
.ft-card.type-blue{border:1px solid #00c0ff;background:rgba(0,192,255,0.03);color:#00c0ff;}
.ft-card.type-blue:hover{border-color:#00c0ff;box-shadow:0 0 12px rgba(0,192,255,0.25);}
.ft-card.type-purple{border:1px solid #ab20fd;background:rgba(171,32,253,0.03);color:#ab20fd;}
.ft-card.type-purple:hover{border-color:#ab20fd;box-shadow:0 0 12px rgba(171, 32, 253, 0.25);}
.ft-card.type-green{border:1px solid #3ddc84;background:rgba(61,220,132,0.02);color:#3ddc84;font-size:0.75rem;padding:4px 8px;}
.ft-card.type-green:hover{border-color:#3ddc84;box-shadow:0 0 8px rgba(61,220,132,0.25);}
.line-v{width:2px;height:24px;background:rgba(255,255,255,0.15);}
.tree-side-text-card{background:linear-gradient(135deg,rgba(15,17,26,0.6) 0%,rgba(30,20,45,0.4) 100%);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:20px;width:100%;max-width:820px;margin-top:20px;display:flex;align-items:center;gap:16px;box-shadow:0 4px 15px rgba(0,0,0,0.2);}
.tree-side-text-icon{font-size:2.2rem;color:#fbbf24;text-shadow:0 0 10px rgba(251, 191, 36, 0.4);}
.tree-side-text-content{font-size:1.15rem;font-weight:700;line-height:1.6;color:#ffffff;text-align:left;}
.tree-side-text-content span.highlight{color:#ff007f;text-shadow:0 0 8px rgba(255, 0, 127, 0.3);}
.tree-hover-info{margin-top:20px;background:rgba(15, 17, 26, 0.7);border:1px solid rgba(255, 255, 255, 0.05);border-radius:10px;padding:14px 20px;width:100%;max-width:820px;min-height:75px;display:flex;align-items:center;gap:16px;box-shadow:0 6px 20px rgba(0, 0, 0, 0.4);transition:all 0.3s ease;}
.tree-hover-badge{font-weight:800;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.12em;color:#8a94a6;border-right:2px solid rgba(255, 255, 255, 0.1);padding-right:16px;height:100%;display:flex;align-items:center;white-space:nowrap;transition:color 0.3s ease;}
.tree-hover-desc{font-size:0.95rem;color:#94a3b8;line-height:1.6;transition:color 0.3s ease;}
.tl-scroll-hint{display:flex;font-size:0.75rem;color:#8a94a6;margin-bottom:12px;align-items:center;gap:6px;justify-content:center;}
</style>
<div class="tree-wrapper-v6">
<div class="tree-side-text-card">
<div class="tree-side-text-icon"><i class="fas fa-sitemap"></i></div>
<div class="tree-side-text-content">Linux uses a <span class="highlight">tree structure (โครงสร้างต้นไม้แบบลำดับขั้น)</span> to store and organize files</div>
</div>
<div class="tl-scroll-hint" style="margin-top: 15px;"><i class="fas fa-arrows-alt-h"></i> <span>เลื่อนในแนวนอนเพื่อดูโครงสร้างแผนผังทั้งหมด (Scroll horizontally to view full chart)</span></div>
<div class="flex-tree-scroll">
<div class="flex-tree-chart">
<div class="ft-root-box">
<div class="ft-card type-root" onmouseover="updateTreeDesc('/', 'Root directory (ไดเรกทอรีราก) - จุดเริ่มต้นและรากฐานของระบบไฟล์ทั้งหมดใน Linux', '#fbbf24')" onmouseout="resetTreeDesc()">/ (root)</div>
<div class="line-v"></div>
</div>
<div class="ft-main-trunk"></div>
<div class="ft-grid">
<div class="ft-col type-top">
<div class="ft-card type-blue" onmouseover="updateTreeDesc('/bin/', 'Binary (คำสั่งพื้นฐาน) - โฟลเดอร์เก็บไฟล์คำสั่งและโปรแกรมพื้นฐานที่จำเป็นสำหรับผู้ใช้ทุกคน', '#00c0ff')" onmouseout="resetTreeDesc()">/bin/</div>
</div>
<div class="ft-col type-bottom">
<div class="ft-card type-blue" onmouseover="updateTreeDesc('/opt/', 'Optional (ซอฟต์แวร์เสริม) - เก็บแอปพลิเคชันและโปรแกรมเสริมเพิ่มเติมที่ไม่ได้ติดตั้งมาพร้อมระบบ', '#00c0ff')" onmouseout="resetTreeDesc()">/opt/</div>
</div>
<div class="ft-col type-top">
<div class="ft-card type-blue" onmouseover="updateTreeDesc('/boot/', 'Boot (ไฟล์ระบบเปิดเครื่อง) - เก็บไฟล์สำคัญที่ใช้ในการเริ่มระบบปฏิบัติการ เช่น Kernel และ GRUB', '#00c0ff')" onmouseout="resetTreeDesc()">/boot/</div>
</div>
<div class="ft-col type-bottom">
<div class="ft-card type-blue" onmouseover="updateTreeDesc('/root/', 'Root User Home (โฮมของผู้ดูแลระบบ) - พื้นที่เก็บข้อมูลส่วนตัวของสิทธิ์ผู้ดูแลระบบหลัก (root)', '#00c0ff')" onmouseout="resetTreeDesc()">/root/</div>
</div>
<div class="ft-col type-top">
<div class="ft-card type-blue" onmouseover="updateTreeDesc('/dev/', 'Devices (ไฟล์ตำแหน่งอุปกรณ์) - แหล่งเก็บไฟล์เสมือนที่เชื่อมโยงกับฮาร์ดแวร์และอุปกรณ์เชื่อมต่อทั้งหมดในระบบ', '#00c0ff')" onmouseout="resetTreeDesc()">/dev/</div>
</div>
<div class="ft-col type-bottom">
<div class="ft-card type-blue" onmouseover="updateTreeDesc('/sbin/', 'System Binaries (คำสั่งเฉพาะผู้ดูแล) - เก็บไฟล์คำสั่งระบบที่จำเป็นเฉพาะของผู้ดูแลระบบสำหรับจัดการเครื่อง', '#00c0ff')" onmouseout="resetTreeDesc()">/sbin/</div>
</div>
<div class="ft-col type-top">
<div class="ft-card type-blue" onmouseover="updateTreeDesc('/etc/', 'Etcetera (ไฟล์ตั้งค่าระบบ) - แหล่งรวมไฟล์กำหนดค่าและคอนฟิกูเรชัน (Configuration) ของระบบทั้งหมด', '#00c0ff')" onmouseout="resetTreeDesc()">/etc/</div>
</div>
<div class="ft-col type-bottom">
<div class="ft-card type-blue" onmouseover="updateTreeDesc('/srv/', 'Services (ข้อมูลการให้บริการ) - เก็บไฟล์และข้อมูลที่ใช้ในการให้บริการเครือข่าย เช่น ข้อมูลของ Web Server', '#00c0ff')" onmouseout="resetTreeDesc()">/srv/</div>
</div>
<div class="ft-col type-top">
<div class="ft-card type-blue" onmouseover="updateTreeDesc('/home/', 'Home directory (โฮมผู้ใช้งานทั่วไป) - แหล่งเก็บข้อมูลและโฟลเดอร์ส่วนตัวของผู้ใช้งานทั่วไปในระบบ', '#00c0ff')" onmouseout="resetTreeDesc()">/home/</div>
</div>
<div class="ft-col type-bottom">
<div class="ft-card type-blue" onmouseover="updateTreeDesc('/tmp/', 'Temporary (ไฟล์ชั่วคราวระบบ) - โฟลเดอร์เก็บไฟล์ชั่วคราว ซึ่งจะถูกล้างข้อมูลออกโดยอัตโนมัติเมื่อรีสตาร์ทระบบ', '#00c0ff')" onmouseout="resetTreeDesc()">/tmp/</div>
</div>
<div class="ft-col type-top">
<div class="ft-card type-blue" onmouseover="updateTreeDesc('/lib/', 'Libraries (ไฟล์ไลบรารีระบบ) - แหล่งเก็บโมดูลระบบและไลบรารีแชร์ที่จำเป็นในการรันโปรแกรมหลัก', '#00c0ff')" onmouseout="resetTreeDesc()">/lib/</div>
</div>
<div class="ft-col type-bottom has-subtree">
<div class="ft-card type-purple" onmouseover="updateTreeDesc('/usr/', 'User (โปรแกรมผู้ใช้งานทั่วไป) - เก็บโปรแกรม คำสั่ง และไฟล์ขนาดใหญ่สำหรับผู้ใช้ทั่วไปใช้งาน (โหมดอ่านอย่างเดียว)', '#ab20fd')" onmouseout="resetTreeDesc()">/usr/</div>
<div class="ft-sub-wrapper">
<div class="ft-sub-row">
<div class="ft-sub-col"><div class="ft-card type-green" onmouseover="updateTreeDesc('/usr/bin/', 'User Executables (คำสั่งผู้ใช้ทั่วไป) - คำสั่งโปรแกรมทั่วไปสำหรับผู้ใช้งานในระบบ', '#3ddc84')" onmouseout="resetTreeDesc()">/bin/</div></div>
<div class="ft-sub-col"><div class="ft-card type-green" onmouseover="updateTreeDesc('/usr/include/', 'Header Files (ไฟล์ส่วนหัวภาษา C) - แฟ้มเก็บ Header (.h) มาตรฐานสำหรับเขียนและคอมไพล์โปรแกรม', '#3ddc84')" onmouseout="resetTreeDesc()">/include/</div></div>
<div class="ft-sub-col"><div class="ft-card type-green" onmouseover="updateTreeDesc('/usr/lib/', 'Libraries (ไลบรารีมาตรฐานทั่วไป) - ไฟล์ไลบรารีมาตรฐานสำหรับการรันโปรแกรมทั่วไป', '#3ddc84')" onmouseout="resetTreeDesc()">/lib/</div></div>
<div class="ft-sub-col"><div class="ft-card type-green" onmouseover="updateTreeDesc('/usr/sbin/', 'System Executables (คำสั่งควบคุมระบบ) - คำสั่งสำหรับผู้ดูแลระบบระดับสูงเพื่อจัดการระบบเพิ่มเติม', '#3ddc84')" onmouseout="resetTreeDesc()">/sbin/</div></div>
</div>
</div>
</div>
<div class="ft-col type-top">
<div class="ft-card type-blue" onmouseover="updateTreeDesc('/media/', 'Media (จุดเชื่อมอุปกรณ์พกพา) - โฟลเดอร์เมาท์สำหรับอุปกรณ์จัดเก็บข้อมูลแบบถอดเสียบภายนอก เช่น CD-ROM', '#00c0ff')" onmouseout="resetTreeDesc()">/media/</div>
</div>
<div class="ft-col type-bottom has-subtree">
<div class="ft-card type-purple" onmouseover="updateTreeDesc('/var/', 'Variable (ข้อมูลผันแปรระบบ) - แหล่งเก็บข้อมูลที่มีการเปลี่ยนแปลงบ่อย เช่น ล็อกไฟล์ (Log) หรือระบบคิวเมล', '#ab20fd')" onmouseout="resetTreeDesc()">/var/</div>
<div class="ft-sub-wrapper">
<div class="ft-sub-row">
<div class="ft-sub-col"><div class="ft-card type-green" onmouseover="updateTreeDesc('/var/cache/', 'Cache (พื้นที่เก็บแคช) - แหล่งเก็บข้อมูลแคชของแอปพลิเคชัน เพื่อให้เรียกใช้งานได้รวดเร็วยิ่งขึ้น', '#3ddc84')" onmouseout="resetTreeDesc()">/cache/</div></div>
<div class="ft-sub-col"><div class="ft-card type-green" onmouseover="updateTreeDesc('/var/log/', 'Log files (ไฟล์ประวัติการทำงาน) - ไฟล์บันทึกการทำงาน เหตุการณ์ และประวัติของกิจกรรมต่างๆ ในระบบ', '#3ddc84')" onmouseout="resetTreeDesc()">/log/</div></div>
<div class="ft-sub-col"><div class="ft-card type-green" onmouseover="updateTreeDesc('/var/spool/', 'Spool (คิวพักข้อมูล) - พื้นที่พักรอการประมวลผลของงาน เช่น คิวพิมพ์เอกสาร หรืออีเมลรอส่งออก', '#3ddc84')" onmouseout="resetTreeDesc()">/spool/</div></div>
<div class="ft-sub-col"><div class="ft-card type-green" onmouseover="updateTreeDesc('/var/tmp/', 'Temporary (ไฟล์ชั่วคราวข้ามการบูต) - แหล่งเก็บไฟล์ชั่วคราวของโปรแกรมที่จะไม่โดนลบไปเมื่อรีบูตเครื่องใหม่', '#3ddc84')" onmouseout="resetTreeDesc()">/tmp/</div></div>
</div>
</div>
</div>
<div class="ft-col type-top">
<div class="ft-card type-blue" onmouseover="updateTreeDesc('/mnt/', 'Mount (จุดเชื่อมระบบไฟล์ชั่วคราว) - ใช้สำหรับเมาท์และเข้าถึงระบบไฟล์ภายนอกอื่นชั่วคราวเพื่อคัดลอกหรือจัดการข้อมูล', '#00c0ff')" onmouseout="resetTreeDesc()">/mnt/</div>
</div>
</div>
</div>
</div>
</div>
<div class="tree-hover-info" id="tree-info-panel-el">
<div class="tree-hover-badge" id="tree-badge-el">System Path</div>
<div class="tree-hover-desc" id="tree-desc-el">เลื่อนเมาส์ไปชี้ที่แต่ละโฟลเดอร์ในแผนผัง เพื่ออ่านคำอธิบายหน้าที่ในระบบ Linux (Hover over directories to view descriptions)</div>
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
desc.textContent = 'เลื่อนเมาส์ไปชี้ที่แต่ละโฟลเดอร์ในแผนผัง เพื่ออ่านคำอธิบายหน้าที่ในระบบ Linux (Hover over directories to view descriptions)';
desc.style.color = '#94a3b8';
if (panel) {
panel.style.borderColor = 'rgba(255, 255, 255, 0.08)';
panel.style.boxShadow = '0 6px 20px rgba(0, 0, 0, 0.4)';
}
}
}
</script>"""

blocks[7]['value'] = html_tree_bilingual

# 2. Clear redundant top-level directory tables (blocks 11 to 21)
for i in range(11, 22):
    blocks[i]['value'] = ""

# 3. Update Important Files tables (blocks 23 to 37) to bilingual format
bilingual_tables = {
    23: """### 📂 Important Files and Directories in Linux

Linux system stores some well-defined configuration files, binaries, man pages information files such as kernel files, device files, log files, etc.

**Kernel file:**

| Path | Description |
|---|---|
| `/boot/vmlinux` | the kernel file / ไฟล์แกนหลักและหัวใจควบคุมระบบปฏิบัติการ (Linux Kernel) |

**Device files:**

| Path | Description |
|---|---|
| `/dev/hda` | first IDE HDD / ไฟล์เชื่อมต่อและตำแหน่งฮาร์ดดิสก์ IDE ตัวแรกของระบบ |
| `/dev/hdc` | pseudo-device or CD-ROM / อุปกรณ์จำลองสำหรับทิ้งข้อมูลขยะ หรือไฟล์ไดรฟ์ CD-ROM |""",

    25: """### 📂 Important Files and Directories in Linux (Cont)

**System configuration files:**

| Path | Description |
|---|---|
| `/etc/bashrc` | system defaults and aliases / ไฟล์กำหนดค่าเริ่มต้นและชื่อย่อคำสั่งของ Bash Shell สำหรับผู้ใช้ทุกคน |
| `/etc/crontab` | crontab script / ไฟล์สคริปต์หลักสำหรับตั้งเวลาเรียกใช้งานโปรแกรมอัตโนมัติตามกำหนด |
| `/etc/exports` | network filesystem info / ข้อมูลระบบไฟล์แชร์และสิทธิ์การเข้าถึงอุปกรณ์ข้อมูลบนเครือข่าย |
| `/etc/group` | security group definitions / ไฟล์นิยามกลุ่มความปลอดภัยและกลุ่มผู้ใช้งานภายในระบบ |
| `/etc/init.d` | service startup script / โฟลเดอร์สคริปต์รันระบบเมื่อเริ่มเปิดเครื่อง (Services Startup) |
| `/etc/hosts` | IP and hostnames mappings / ไฟล์เก็บแผนผังหมายเลข IP Address กับชื่อเครื่องคอมพิวเตอร์ |
| `/etc/hosts.allow` | hosts allowed access / รายชื่อเครื่องโฮสต์ที่ได้รับอนุญาตให้เชื่อมต่อเข้าบริการระบบ |""",

    27: """### 📂 Important Files and Directories in Linux (Cont)

| Path | Description |
|---|---|
| `/etc/host.deny` | hosts denied access / รายชื่อเครื่องโฮสต์ที่ถูกบล็อกไม่ให้เชื่อมต่อเข้าใช้บริการระบบ |
| `/etc/issue` | pre-login message / ข้อความแจ้งข่าวสารหรือต้อนรับที่แสดงผลก่อนเข้าสู่ระบบล็อกอิน |
| `/etc/motd` | message of the day / ข้อความต้อนรับและประกาศสั้นหลังล็อกอินเข้าระบบสำเร็จ |
| `/etc/passwd` | system user accounts / รายชื่อบัญชีผู้ใช้ ข้อมูลระบบ รหัสผ่าน และสิทธิ์พื้นฐานในระบบ |
| `/etc/printcap` | printer configurations / ไฟล์เก็บรายละเอียดคอนฟิกและเครื่องพิมพ์ที่ต่อเชื่อมใช้งาน |
| `/etc/profile` | bash shell defaults / ไฟล์ตั้งค่าสภาพแวดล้อมตั้งต้นสำหรับผู้ใช้ Bash Shell ทุกคนตอนล็อกอิน |
| `/etc/profile.d` | post-login scripts / โฟลเดอร์เก็บสคริปต์ย่อยที่จะทำงานอัตโนมัติทันทีหลังผู้ใช้ล็อกอินสำเร็จ |
| `/etc/re.conf` | interface/service configurations / ไฟล์กำหนดค่าการทำงานของอินเตอร์เฟซและบริการระบบ |
| `/etc/rc.d` | startup/shutdown control / สคริปต์ควบคุมการรัน หยุด หรือเริ่มใหม่ของฟังก์ชันการทำงานระบบ |""",

    29: """### 📂 Important Files and Directories in Linux (Cont)

| Path | Description |
|---|---|
| `/etc/rc.d/init.d` | initialization scripts / โฟลเดอร์เก็บไฟล์ตั้งค่าเริ่มต้นโปรแกรมระบบขณะบูตเครื่อง |
| `/etc/security` | security terminal settings / ข้อกำหนดความปลอดภัยที่ตั้งให้สิทธิ์ root สามารถล็อกอินเข้าใช้เครื่องได้ |
| `/etc/shadow` | encrypted passwords / ไฟล์เก็บรหัสผ่านของผู้ใช้งานทั้งหมดในรูปแบบที่เข้ารหัสลับเพื่อความปลอดภัย |
| `/etc/skel` | new user home template / โฟลเดอร์ต้นแบบสำหรับสร้างไฟล์ตั้งต้นให้โฟลเดอร์โฮมเมื่อมีผู้ใช้งานใหม่ |
| `/etc/X11` | X-window configurations / แหล่งรวมไฟล์ตั้งค่าสำหรับการแสดงผลในระบบกราฟิก (GUI) ของ X11 |""",

    31: """### 📂 Important Files and Directories in Linux (Cont)

**User related files:**

| Path | Description |
|---|---|
| `/usr/bin` | user executable files / แหล่งรวมไฟล์โปรแกรมคำสั่งใช้งานทั่วไปที่ผู้ใช้ทุกคนสามารถรันได้ |
| `/usr/include` | C header files / ไฟล์ส่วนหัวมาตรฐาน (.h) สำหรับการแปลงและเขียนโปรแกรมภาษา C |
| `/usr/share` | shareable text files / ไฟล์เอกสาร คู่มือช่วยเหลือการใช้คำสั่ง และไฟล์ที่ใช้แชร์ข้ามระบบ |
| `/usr/lib` | object files and libraries / ไฟล์รันระบบของโปรแกรมและไลบรารีต่างๆ ที่โปรแกรมทั่วไปเรียกใช้ |
| `/usr/sbin` | admin commands / ไฟล์คำสั่งควบคุมระบบขั้นสูงสำหรับผู้ใช้ระดับผู้ดูแลระบบหลัก |""",

    33: """### 📂 Important Files and Directories in Linux (Cont)

**Log files:**

| Path | Description |
|---|---|
| `/var/log/httpd-access.log` | web access information / ล็อกประวัติการเข้าชมและสถิติการร้องขอไฟล์ในระบบเว็บเซิร์ฟเวอร์ |
| `/var/log/lastlog` | user last login / รายละเอียดและประวัติการล็อกอินเข้าระบบครั้งล่าสุดของผู้ใช้งานแต่ละราย |
| `/var/log/maillog` | email usage log / ไฟล์บันทึกประวัติการส่ง-รับข้อมูลในระบบบริการจดหมายอีเมล |
| `/var/log/messages` | global system messages / ล็อกระบบทั่วไปที่เก็บบันทึกประวัติและข้อผิดพลาดสำคัญของระบบปฏิบัติการ |
| `/var/log/userlog` | user history log / ไฟล์บันทึกประวัติความเคลื่อนไหวเกี่ยวกับการสร้างและลบบัญชีผู้ใช้ |
| `/var/log/wtmp` | login/logout history / ประวัติการเข้างานและออกงานของระบบ พร้อมช่วงเวลาใช้งานแบบถาวร |""",

    35: """### 📂 Important Files and Directories in Linux (Cont)

**Home files and directories under `/home/$USER`:**

| Path | Description |
|---|---|
| `~/.bashrc` | user bash settings / ไฟล์กำหนดค่าเริ่มต้นและคีย์ลัดคำสั่งเฉพาะตัวสำหรับผู้ใช้ Bash Shell |
| `~/.cache` | user cache files / โฟลเดอร์เก็บข้อมูลแคชสำหรับแอปพลิเคชันส่วนตัวเพื่อความรวดเร็ว |
| `~/.dmrc` | session initialization / ไฟล์เก็บบันทึกประเภทเดสก์ท็อปและค่าเริ่มต้นที่เลือกใช้ตอนล็อกอิน |
| `~/.history` | command history list / ไฟล์บันทึกประวัติคำสั่งต่างๆ ที่เคยพิมพ์ในเทอร์มินัลย้อนหลัง |
| `~/.local/share/Trash` | trash directory / โฟลเดอร์ถังขยะส่วนตัวสำหรับเก็บไฟล์และข้อมูลที่กดลบชั่วคราว |
| `~/.profile` | user profile settings / ไฟล์ตั้งค่าสภาพแวดล้อมเฉพาะบัญชีผู้ใช้เมื่อล็อกอินเข้าสู่ระบบ |
| `~/.zshrc` | user zsh settings / ไฟล์ตั้งค่าการเริ่มต้นโปรแกรม คอนฟิก และคำสั่งย่อสำหรับ Zsh Shell |""",

    37: """### 📂 Important Files and Directories in Linux (Cont)

| Path | Description |
|---|---|
| `~/Desktop` | desktop folder / โฟลเดอร์จัดเก็บสิ่งต่างๆ บนหน้าจอเดสก์ท็อปของผู้ใช้งาน |
| `~/Documents` | documents folder / โฟลเดอร์สำหรับจัดเก็บเอกสารและไฟล์ข้อมูลส่วนบุคคล |
| `~/Downloads` | downloads folder / โฟลเดอร์จัดเก็บไฟล์และแอปพลิเคชันที่ดาวน์โหลดจากอินเทอร์เน็ต |
| `~/Music` | music folder / โฟลเดอร์สำหรับจัดเก็บไฟล์เสียงและเพลงของผู้ใช้งาน |
| `~/Pictures` | pictures folder / โฟลเดอร์สำหรับจัดเก็บรูปภาพและสื่อทางภาพต่างๆ |
| `~/Public` | public sharing folder / โฟลเดอร์เปิดแชร์ไฟล์สำหรับเครือข่ายและเครื่องอื่นๆ ในระบบ |
| `~/Videos` | videos folder / โฟลเดอร์สำหรับจัดเก็บไฟล์วิดีโอและภาพยนตร์ |"""
}

# Update database blocks
for idx, new_val in bilingual_tables.items():
    blocks[idx]['value'] = new_val

# Save and Commit
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
db.session.commit()
print("Staggered tree and bilingual tables completely redeployed!")
