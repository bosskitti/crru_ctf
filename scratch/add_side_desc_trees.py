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

# The HTML code for side-by-side description trees (completely flat, 0-indentation)
html_side_desc_trees = """<style>
.mini-tree-wrapper{margin:2.5rem 0;width:100%;max-width:820px;background:rgba(15,17,26,0.4);border:1px solid rgba(255,255,255,0.05);border-radius:12px;padding:24px;box-shadow:inset 0 0 20px rgba(0,0,0,0.3);}
.mini-tree-title{font-size:1.15rem;font-weight:700;color:#fbbf24;margin-bottom:20px;display:flex;align-items:center;gap:8px;text-shadow:0 0 10px rgba(251,191,36,0.15);}
.mt-flex-container{display:flex;gap:24px;align-items:stretch;width:100%;}
.mt-tree-side{flex:1.2;display:flex;align-items:center;position:relative;padding:10px 0;min-width:260px;}
.mt-root-box{margin-right:40px;position:relative;z-index:2;display:flex;flex-direction:column;align-items:center;}
.mt-root-box::after{content:'';position:absolute;top:50%;right:-40px;width:40px;height:2px;background:rgba(255,255,255,0.15);z-index:1;transform:translateY(-50%);}
.mt-children-grid{display:flex;flex-direction:column;gap:10px;position:relative;padding-left:20px;border-left:2px solid rgba(255,255,255,0.15);z-index:2;}
.mt-child-item{position:relative;display:flex;align-items:center;width:100%;}
.mt-child-item::before{content:'';position:absolute;top:50%;left:-20px;width:20px;height:2px;background:rgba(255,255,255,0.15);z-index:1;transform:translateY(-50%);}
.mt-card{font-size:0.8rem;padding:6px 12px;border-radius:6px;text-align:center;font-weight:700;cursor:pointer;transition:all 0.3s ease;white-space:nowrap;width:auto;min-width:80px;}
.mt-card:hover{transform:translateX(3px);color:#ffffff;}
.mt-card.type-root{border:1px solid #fbbf24;background:rgba(251,191,36,0.05);color:#fbbf24;box-shadow:0 0 10px rgba(251,191,36,0.15);min-width:70px;}
.mt-card.type-root:hover{box-shadow:0 0 15px rgba(251,191,36,0.3);transform:none;}
.mt-card.type-blue{border:1px solid #00c0ff;background:rgba(0,192,255,0.03);color:#00c0ff;}
.mt-card.type-blue:hover{border-color:#00c0ff;box-shadow:0 0 10px rgba(0,192,255,0.25);}
.mt-card.type-green{border:1px solid #3ddc84;background:rgba(61,220,132,0.02);color:#3ddc84;}
.mt-card.type-green:hover{border-color:#3ddc84;box-shadow:0 0 10px rgba(61,220,132,0.25);}
.mt-desc-side{flex:1.3;background:rgba(15,17,26,0.6);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:20px;display:flex;flex-direction:column;justify-content:center;transition:all 0.3s ease;min-height:150px;box-shadow:0 4px 15px rgba(0,0,0,0.2);}
.mt-hover-badge{font-weight:800;font-size:0.75rem;color:#8a94a6;margin-bottom:10px;text-transform:uppercase;letter-spacing:0.1em;transition:color 0.3s ease;}
.mt-hover-desc{font-size:0.9rem;color:#94a3b8;line-height:1.6;transition:color 0.3s ease;}
@media (max-width:768px){
.mt-flex-container{flex-direction:column;gap:16px;}
.mt-tree-side{justify-content:center;}
}
</style>
<script>
function updateMiniDesc(treeId, title, text, color) {
var badge = document.getElementById(treeId + '-badge');
var desc = document.getElementById(treeId + '-desc');
var panel = document.getElementById(treeId + '-panel');
if (badge && desc) {
badge.textContent = title;
badge.style.color = color;
desc.textContent = text;
desc.style.color = '#ffffff';
if (panel) {
panel.style.borderColor = color;
panel.style.boxShadow = '0 0 15px ' + color + '15, 0 4px 15px rgba(0,0,0,0.2)';
}
}
}
function resetMiniDesc(treeId, defaultText) {
var badge = document.getElementById(treeId + '-badge');
var desc = document.getElementById(treeId + '-desc');
var panel = document.getElementById(treeId + '-panel');
if (badge && desc) {
badge.textContent = 'Path';
badge.style.color = '#8a94a6';
desc.textContent = defaultText;
desc.style.color = '#94a3b8';
if (panel) {
panel.style.borderColor = 'rgba(255, 255, 255, 0.05)';
panel.style.boxShadow = '0 4px 15px rgba(0,0,0,0.2)';
}
}
}
</script>

<div class="mini-tree-wrapper">
<div class="mini-tree-title"><i class="fas fa-microchip"></i> 1. /dev/ (Device Files & Kernel)</div>
<div class="mt-flex-container">
<div class="mt-tree-side">
<div class="mt-root-box">
<div class="mt-card type-root" onmouseover="updateMiniDesc('dev', '/dev/', 'Device Directory - โฟลเดอร์ศูนย์รวมไฟล์เชื่อมต่ออุปกรณ์ฮาร์ดแวร์ทั้งหมด', '#fbbf24')" onmouseout="resetMiniDesc('dev', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /dev/ เพื่อดูรายละเอียดหน้าที่')">/dev/</div>
</div>
<div class="mt-children-grid">
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('dev', '/dev/hda', 'First IDE HDD - ไฟล์เชื่อมโยงและพาร์ทิชันของฮาร์ดดิสก์หลักตัวแรกในระบบ', '#00c0ff')" onmouseout="resetMiniDesc('dev', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /dev/ เพื่อดูรายละเอียดหน้าที่')">hda</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('dev', '/dev/hdc', 'CD-ROM / Pseudo-device - ไฟล์เชื่อมต่อไดรฟ์ CD-ROM หรือช่องส่งทิ้งข้อมูลระบบ', '#00c0ff')" onmouseout="resetMiniDesc('dev', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /dev/ เพื่อดูรายละเอียดหน้าที่')">hdc</div></div>
<div class="mt-child-item"><div class="mt-card type-green" onmouseover="updateMiniDesc('dev', '/boot/vmlinux', 'Linux Kernel - ไฟล์แกนหลักและหัวใจควบคุมการทำงานของระบบปฏิบัติการ Linux', '#3ddc84')" onmouseout="resetMiniDesc('dev', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /dev/ เพื่อดูรายละเอียดหน้าที่')">/boot/vmlinux</div></div>
</div>
</div>
<div class="mt-desc-side" id="dev-panel">
<div class="mt-hover-badge" id="dev-badge">Path</div>
<div class="mt-hover-desc" id="dev-desc">ชี้ที่กิ่งไฟล์ในโครงสร้าง /dev/ เพื่อดูรายละเอียดหน้าที่</div>
</div>
</div>
</div>

<div class="mini-tree-wrapper">
<div class="mini-tree-title"><i class="fas fa-cogs"></i> 2. /etc/ (System Configurations)</div>
<div class="mt-flex-container">
<div class="mt-tree-side" style="flex: 1;">
<div class="mt-root-box">
<div class="mt-card type-root" onmouseover="updateMiniDesc('etc', '/etc/', 'Configuration Directory - แหล่งรวมไฟล์ตั้งค่าการทำงานและกำหนดค่าระบบปฏิบัติการทั้งหมด', '#fbbf24')" onmouseout="resetMiniDesc('etc', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /etc/ เพื่อดูรายละเอียดหน้าที่')">/etc/</div>
</div>
<div class="mt-children-grid">
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('etc', '/etc/bashrc', 'Bash defaults - ไฟล์ตั้งค่าคีย์ลัดและคอนฟิกเริ่มต้นสำหรับผู้ใช้ Bash Shell ทุกคน', '#00c0ff')" onmouseout="resetMiniDesc('etc', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /etc/ เพื่อดูรายละเอียดหน้าที่')">bashrc</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('etc', '/etc/crontab', 'Crontab script - ตั้งเวลารันสคริปต์และรันโปรแกรมระบบแบบอัตโนมัติ', '#00c0ff')" onmouseout="resetMiniDesc('etc', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /etc/ เพื่อดูรายละเอียดหน้าที่')">crontab</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('etc', '/etc/exports', 'Network filesystem - ข้อมูลแชร์ระบบไฟล์และควบคุมสิทธิ์ใช้งานผ่านเครือข่าย', '#00c0ff')" onmouseout="resetMiniDesc('etc', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /etc/ เพื่อดูรายละเอียดหน้าที่')">exports</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('etc', '/etc/group', 'User Groups - ไฟล์ระบุกลุ่มความปลอดภัยและสิทธิ์กลุ่มบัญชีผู้ใช้งาน', '#00c0ff')" onmouseout="resetMiniDesc('etc', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /etc/ เพื่อดูรายละเอียดหน้าที่')">group</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('etc', '/etc/hosts', 'IP Mappings - แผนผังไอพีแอดเดรสเชื่อมโยงกับชื่อเครื่องคอมพิวเตอร์', '#00c0ff')" onmouseout="resetMiniDesc('etc', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /etc/ เพื่อดูรายละเอียดหน้าที่')">hosts</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('etc', '/etc/hosts.allow', 'Hosts allowed - รายชื่อคอมพิวเตอร์ภายนอกที่อนุญาตให้ล็อกอินใช้บริการเครื่อง', '#00c0ff')" onmouseout="resetMiniDesc('etc', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /etc/ เพื่อดูรายละเอียดหน้าที่')">hosts.allow</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('etc', '/etc/host.deny', 'Hosts denied - รายชื่อคอมพิวเตอร์ภายนอกที่ถูกระงับสิทธิ์เข้าใช้งานระบบ', '#00c0ff')" onmouseout="resetMiniDesc('etc', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /etc/ เพื่อดูรายละเอียดหน้าที่')">host.deny</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('etc', '/etc/issue', 'Pre-login message - ข้อความแจ้งเตือนหรือข้อความต้อนรับแสดงก่อนหน้าล็อกอิน', '#00c0ff')" onmouseout="resetMiniDesc('etc', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /etc/ เพื่อดูรายละเอียดหน้าที่')">issue</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('etc', '/etc/motd', 'Message of the day - ประกาศข้อความระบบแสดงให้เห็นทันทีหลังผู้ใช้ล็อกอินสำเร็จ', '#00c0ff')" onmouseout="resetMiniDesc('etc', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /etc/ เพื่อดูรายละเอียดหน้าที่')">motd</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('etc', '/etc/passwd', 'User accounts - รายชื่อบัญชีผู้ใช้งาน สิทธิ์การเข้าถึง และไดเรกทอรีบ้านของทุกคน', '#00c0ff')" onmouseout="resetMiniDesc('etc', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /etc/ เพื่อดูรายละเอียดหน้าที่')">passwd</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('etc', '/etc/shadow', 'Encrypted passwords - รหัสผ่านจริงของผู้ใช้ที่ถูกเข้ารหัสลับไว้เพื่อความปลอดภัย', '#00c0ff')" onmouseout="resetMiniDesc('etc', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /etc/ เพื่อดูรายละเอียดหน้าที่')">shadow</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('etc', '/etc/skel', 'Skel folder - โฟลเดอร์ต้นแบบสำหรับป้อนไฟล์ตั้งต้นให้โฮมผู้ใช้ที่สร้างใหม่', '#00c0ff')" onmouseout="resetMiniDesc('etc', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /etc/ เพื่อดูรายละเอียดหน้าที่')">skel/</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('etc', '/etc/init.d', 'Service scripts - สคริปต์ควบคุมระบบการเปิดและปิดโปรแกรมบริการระบบ (Services)', '#00c0ff')" onmouseout="resetMiniDesc('etc', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /etc/ เพื่อดูรายละเอียดหน้าที่')">init.d/</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('etc', '/etc/rc.d', 'Startup scripts - สคริปต์เริ่มต้นหรือหยุดกระบวนการรันระบบคอมพิวเตอร์หลัก', '#00c0ff')" onmouseout="resetMiniDesc('etc', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /etc/ เพื่อดูรายละเอียดหน้าที่')">rc.d/</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('etc', '/etc/security', 'Security limits - กฎการจำกัดความปลอดภัยและจำกัดสิทธิ์การเชื่อมต่อระบบ', '#00c0ff')" onmouseout="resetMiniDesc('etc', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /etc/ เพื่อดูรายละเอียดหน้าที่')">security/</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('etc', '/etc/X11', 'GUI configs - ไฟล์ตั้งค่าการแสดงผลแบบกราฟิกอินเตอร์เฟซ (GUI) ของระบบ', '#00c0ff')" onmouseout="resetMiniDesc('etc', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /etc/ เพื่อดูรายละเอียดหน้าที่')">X11/</div></div>
</div>
</div>
<div class="mt-desc-side" id="etc-panel" style="flex: 1.2;">
<div class="mt-hover-badge" id="etc-badge">Path</div>
<div class="mt-hover-desc" id="etc-desc">ชี้ที่กิ่งไฟล์ในโครงสร้าง /etc/ เพื่อดูรายละเอียดหน้าที่</div>
</div>
</div>
</div>

<div class="mini-tree-wrapper">
<div class="mini-tree-title"><i class="fas fa-folder-open"></i> 3. /usr/ (User Executables & Files)</div>
<div class="mt-flex-container">
<div class="mt-tree-side">
<div class="mt-root-box">
<div class="mt-card type-root" onmouseover="updateMiniDesc('usr', '/usr/', 'User Directory - เก็บโปรแกรม คำสั่ง และไฟล์ขนาดใหญ่สำหรับสิทธิ์ผู้ใช้ทั่วไป', '#fbbf24')" onmouseout="resetMiniDesc('usr', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /usr/ เพื่อดูรายละเอียดหน้าที่')">/usr/</div>
</div>
<div class="mt-children-grid">
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('usr', '/usr/bin', 'User Executables - ไฟล์คำสั่งโปรแกรมใช้งานทั่วไปเสริมที่ผู้ใช้ทุกคนสามารถรันได้', '#00c0ff')" onmouseout="resetMiniDesc('usr', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /usr/ เพื่อดูรายละเอียดหน้าที่')">bin/</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('usr', '/usr/include', 'C Header files - ไฟล์ส่วนหัวมาตรฐาน (.h) สำหรับใช้เขียนและคอมไพล์ภาษา C/C++', '#00c0ff')" onmouseout="resetMiniDesc('usr', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /usr/ เพื่อดูรายละเอียดหน้าที่')">include/</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('usr', '/usr/lib', 'User Libraries - ไลบรารีการแชร์แอปพลิเคชันคอยสนับสนุนโปรแกรมใน /usr', '#00c0ff')" onmouseout="resetMiniDesc('usr', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /usr/ เพื่อดูรายละเอียดหน้าที่')">lib/</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('usr', '/usr/sbin', 'Admin Executables - ไฟล์คำสั่งควบคุมระบบเสริมสำหรับให้ Admin เรียกใช้งาน', '#00c0ff')" onmouseout="resetMiniDesc('usr', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /usr/ เพื่อดูรายละเอียดหน้าที่')">sbin/</div></div>
<div class="mt-child-item"><div class="mt-card type-green" onmouseover="updateMiniDesc('usr', '/usr/share', 'Shareable text - เอกสารอ้างอิง ระบบคู่มือช่วยเหลือ และไฟล์แชร์ส่วนกลาง', '#3ddc84')" onmouseout="resetMiniDesc('usr', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /usr/ เพื่อดูรายละเอียดหน้าที่')">share/</div></div>
</div>
</div>
<div class="mt-desc-side" id="usr-panel">
<div class="mt-hover-badge" id="usr-badge">Path</div>
<div class="mt-hover-desc" id="usr-desc">ชี้ที่กิ่งไฟล์ในโครงสร้าง /usr/ เพื่อดูรายละเอียดหน้าที่</div>
</div>
</div>
</div>

<div class="mini-tree-wrapper">
<div class="mini-tree-title"><i class="fas fa-file-alt"></i> 4. /var/log/ (System Logs)</div>
<div class="mt-flex-container">
<div class="mt-tree-side">
<div class="mt-root-box">
<div class="mt-card type-root" onmouseover="updateMiniDesc('var', '/var/log/', 'Log Directory - โฟลเดอร์ศูนย์รวมประวัติการล็อกอินและการประมวลผลระบบทั้งหมด', '#fbbf24')" onmouseout="resetMiniDesc('var', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /var/log/ เพื่อดูรายละเอียดหน้าที่')">/var/log/</div>
</div>
<div class="mt-children-grid">
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('var', '/var/log/messages', 'Global System messages - บันทึกกิจกรรมระบบโดยรวมและประวัติล็อกไฟล์เหตุการณ์ระบบปฏิบัติการ', '#00c0ff')" onmouseout="resetMiniDesc('var', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /var/log/ เพื่อดูรายละเอียดหน้าที่')">messages</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('var', '/var/log/lastlog', 'User last login - รายละเอียดประวัติล็อกอินเข้าระบบครั้งล่าสุดของผู้ใช้ทุกคนแยกรายบัญชี', '#00c0ff')" onmouseout="resetMiniDesc('var', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /var/log/ เพื่อดูรายละเอียดหน้าที่')">lastlog</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('var', '/var/log/maillog', 'Email log - บันทึกการส่ง-รับและความเคลื่อนไหวของระบบจดหมายอิเล็กทรอนิกส์เซิร์ฟเวอร์', '#00c0ff')" onmouseout="resetMiniDesc('var', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /var/log/ เพื่อดูรายละเอียดหน้าที่')">maillog</div></div>
<div class="mt-child-item"><div class="mt-card type-green" onmouseover="updateMiniDesc('var', '/var/log/httpd-access.log', 'Web Access Log - ล็อกประวัติการเข้าเยี่ยมชมเว็บไซต์บน Apache/HTTPD Web Server', '#3ddc84')" onmouseout="resetMiniDesc('var', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /var/log/ เพื่อดูรายละเอียดหน้าที่')">httpd-access.log</div></div>
<div class="mt-child-item"><div class="mt-card type-green" onmouseover="updateMiniDesc('var', '/var/log/userlog', 'User accounts history - ไฟล์ประวัติควบคุมเหตุการณ์เกี่ยวกับการสร้างหรือลบบัญชีผู้ใช้', '#3ddc84')" onmouseout="resetMiniDesc('var', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /var/log/ เพื่อดูรายละเอียดหน้าที่')">userlog</div></div>
<div class="mt-child-item"><div class="mt-card type-green" onmouseover="updateMiniDesc('var', '/var/log/wtmp', 'Login/logout history - ประวัติการล็อกอินและล็อกเอาท์พร้อมช่วงเวลาใช้งานระบบอย่างละเอียด', '#3ddc84')" onmouseout="resetMiniDesc('var', 'ชี้ที่กิ่งไฟล์ในโครงสร้าง /var/log/ เพื่อดูรายละเอียดหน้าที่')">wtmp</div></div>
</div>
</div>
<div class="mt-desc-side" id="var-panel">
<div class="mt-hover-badge" id="var-badge">Path</div>
<div class="mt-hover-desc" id="var-desc">ชี้ที่กิ่งไฟล์ในโครงสร้าง /var/log/ เพื่อดูรายละเอียดหน้าที่</div>
</div>
</div>
</div>

<div class="mini-tree-wrapper">
<div class="mini-tree-title"><i class="fas fa-home"></i> 5. ~ /home/ (User Home & Configurations)</div>
<div class="mt-flex-container">
<div class="mt-tree-side" style="flex: 1.1;">
<div class="mt-root-box">
<div class="mt-card type-root" onmouseover="updateMiniDesc('home', '/home/$USER/', 'Home Directory - โฟลเดอร์บ้านและศูนย์รวมไฟล์ของบัญชีผู้ใช้งานปัจจุบัน', '#fbbf24')" onmouseout="resetMiniDesc('home', 'ชี้ที่กิ่งไฟล์ในโครงสร้างโฮมผู้ใช้ เพื่อดูรายละเอียดหน้าที่')">~/ (home)</div>
</div>
<div class="mt-children-grid">
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('home', '~/Desktop', 'Desktop folder - โฟลเดอร์เก็บันทึกไอคอนและแอปบนหน้าจอหลักผู้ใช้', '#00c0ff')" onmouseout="resetMiniDesc('home', 'ชี้ที่กิ่งไฟล์ในโครงสร้างโฮมผู้ใช้ เพื่อดูรายละเอียดหน้าที่')">Desktop/</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('home', '~/Documents', 'Documents folder - แหล่งบันทึกและจัดเก็บเอกสาร ข้อมูลส่วนตัวของผู้ใช้งาน', '#00c0ff')" onmouseout="resetMiniDesc('home', 'ชี้ที่กิ่งไฟล์ในโครงสร้างโฮมผู้ใช้ เพื่อดูรายละเอียดหน้าที่')">Documents/</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('home', '~/Downloads', 'Downloads folder - โฟลเดอร์เก็บไฟล์ทุกชนิดที่ดาวน์โหลดมาจากอินเทอร์เน็ต', '#00c0ff')" onmouseout="resetMiniDesc('home', 'ชี้ที่กิ่งไฟล์ในโครงสร้างโฮมผู้ใช้ เพื่อดูรายละเอียดหน้าที่')">Downloads/</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('home', '~/Music', 'Music folder - โฟลเดอร์เก็บรวบรวมไฟล์เสียงและไฟล์เพลงส่วนตัว', '#00c0ff')" onmouseout="resetMiniDesc('home', 'ชี้ที่กิ่งไฟล์ในโครงสร้างโฮมผู้ใช้ เพื่อดูรายละเอียดหน้าที่')">Music/</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('home', '~/Pictures', 'Pictures folder - โฟลเดอร์จัดเก็บรูปภาพและสื่อทางภาพต่างๆ ของผู้ใช้งาน', '#00c0ff')" onmouseout="resetMiniDesc('home', 'ชี้ที่กิ่งไฟล์ในโครงสร้างโฮมผู้ใช้ เพื่อดูรายละเอียดหน้าที่')">Pictures/</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('home', '~/Public', 'Public sharing folder - พื้นที่เปิดให้แชร์ไฟล์ร่วมกับคอมพิวเตอร์บัญชีอื่นๆ ในเครือข่าย', '#00c0ff')" onmouseout="resetMiniDesc('home', 'ชี้ที่กิ่งไฟล์ในโครงสร้างโฮมผู้ใช้ เพื่อดูรายละเอียดหน้าที่')">Public/</div></div>
<div class="mt-child-item"><div class="mt-card type-blue" onmouseover="updateMiniDesc('home', '~/Videos', 'Videos folder - โฟลเดอร์เก็บบันทึกไฟล์ภาพเคลื่อนไหวและไฟล์วิดีโอส่วนตัว', '#00c0ff')" onmouseout="resetMiniDesc('home', 'ชี้ที่กิ่งไฟล์ในโครงสร้างโฮมผู้ใช้ เพื่อดูรายละเอียดหน้าที่')">Videos/</div></div>
<div class="mt-child-item"><div class="mt-card type-green" onmouseover="updateMiniDesc('home', '~/.bashrc', 'Bash Config - สคริปต์กำหนดค่า คีย์ลัดคำสั่งย่อ เฉพาะตัวผู้ใช้งานบน Bash Shell', '#3ddc84')" onmouseout="resetMiniDesc('home', 'ชี้ที่กิ่งไฟล์ในโครงสร้างโฮมผู้ใช้ เพื่อดูรายละเอียดหน้าที่')">.bashrc</div></div>
<div class="mt-child-item"><div class="mt-card type-green" onmouseover="updateMiniDesc('home', '~/.cache', 'User cache - แฟ้มสำหรับเก็บไฟล์ข้อมูลแคชของแอปพลิเคชันส่วนตัวผู้ใช้', '#3ddc84')" onmouseout="resetMiniDesc('home', 'ชี้ที่กิ่งไฟล์ในโครงสร้างโฮมผู้ใช้ เพื่อดูรายละเอียดหน้าที่')">.cache/</div></div>
<div class="mt-child-item"><div class="mt-card type-green" onmouseover="updateMiniDesc('home', '~/.history', 'Terminal history - ไฟล์บันทึกประวัติการเรียกรันคำสั่งผ่าน Terminal ทั้งหมด', '#3ddc84')" onmouseout="resetMiniDesc('home', 'ชี้ที่กิ่งไฟล์ในโครงสร้างโฮมผู้ใช้ เพื่อดูรายละเอียดหน้าที่')">.history</div></div>
<div class="mt-child-item"><div class="mt-card type-green" onmouseover="updateMiniDesc('home', '~/.profile', 'User Profile - สคริปต์เริ่มต้นสภาพแวดล้อมเฉพาะตัวของบัญชีเมื่อล็อกอินเข้าเครื่อง', '#3ddc84')" onmouseout="resetMiniDesc('home', 'ชี้ที่กิ่งไฟล์ในโครงสร้างโฮมผู้ใช้ เพื่อดูรายละเอียดหน้าที่')">.profile</div></div>
<div class="mt-child-item"><div class="mt-card type-green" onmouseover="updateMiniDesc('home', '~/.zshrc', 'Zsh shell config - คอนฟิกูเรชันกำหนดค่าและคำสั่งย่อสำหรับผู้ใช้งาน Zsh Shell', '#3ddc84')" onmouseout="resetMiniDesc('home', 'ชี้ที่กิ่งไฟล์ในโครงสร้างโฮมผู้ใช้ เพื่อดูรายละเอียดหน้าที่')">.zshrc</div></div>
</div>
</div>
<div class="mt-desc-side" id="home-panel" style="flex: 1.2;">
<div class="mt-hover-badge" id="home-badge">Path</div>
<div class="mt-hover-desc" id="home-desc">ชี้ที่กิ่งไฟล์ในโครงสร้างโฮมผู้ใช้ เพื่อดูรายละเอียดหน้าที่</div>
</div>
</div>
</div>
"""

# Set the HTML side description trees into block 23
blocks[23]['value'] = "### 📂 Linux Important Files & Sub-Trees Map\n\nแผนภาพจำลองกิ่งก้านโครงสร้างระบบไฟล์และไฟล์การตั้งค่าสำคัญต่างๆ ของ Linux แยกตามโฟลเดอร์หลักอย่างเป็นระบบ ชี้ที่ชื่อไฟล์ในกิ่งเพื่อดูคำแปลกึ่งไทยอังกฤษและคำอธิบายหน้าที่ปฏิบัติงานด้านขวา:\n\n" + html_side_desc_trees

# Save and Commit
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
db.session.commit()
print("All sub-trees updated to side-by-side description layout successfully!")
