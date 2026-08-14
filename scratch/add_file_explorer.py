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

# The HTML replacement code for the Bilingual File Explorer (completely flat, 0-indentation)
html_explorer = """<style>
.fe-wrapper{display:flex;gap:24px;width:100%;max-width:820px;margin:2.5rem 0;height:550px;}
.fe-tree-panel{flex:1.2;background:rgba(15,17,26,0.4);border:1px solid rgba(255,255,255,0.05);border-radius:12px;padding:20px;overflow-y:auto;font-family:'Fira Code',monospace,Courier;font-size:0.85rem;scrollbar-width:thin;scrollbar-color:rgba(255,255,255,0.1) rgba(0,0,0,0.2);box-shadow:inset 0 0 20px rgba(0,0,0,0.4);}
.fe-tree-panel::-webkit-scrollbar{width:6px;}
.fe-tree-panel::-webkit-scrollbar-track{background:rgba(0,0,0,0.2);border-radius:3px;}
.fe-tree-panel::-webkit-scrollbar-thumb{background:rgba(255,255,255,0.1);border-radius:3px;}
.fe-tree-panel::-webkit-scrollbar-thumb:hover{background:rgba(255,255,255,0.25);}
.fe-details-panel{flex:1;background:rgba(15,17,26,0.6);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:24px;display:flex;flex-direction:column;justify-content:center;align-items:center;box-shadow:0 8px 32px rgba(0,0,0,0.3);text-align:center;transition:all 0.3s ease;overflow-y:auto;}
.fe-details-panel.selected{align-items:flex-start;text-align:left;justify-content:flex-start;}
.fe-node{margin:4px 0;display:flex;flex-direction:column;}
.fe-node-label{display:flex;align-items:center;gap:8px;padding:6px 8px;border-radius:6px;cursor:pointer;color:#a0aec0;transition:all 0.2s ease;user-select:none;}
.fe-node-label:hover{background:rgba(255,255,255,0.04);color:#ffffff;}
.fe-node-label.active{background:rgba(0,240,255,0.08);color:#00f0ff;border-left:3px solid #00f0ff;padding-left:5px;}
.fe-node-children{margin-left:16px;border-left:1px dashed rgba(255,255,255,0.1);padding-left:12px;display:none;}
.fe-node-children.expanded{display:block;}
.fe-toggle-arrow{font-size:0.65rem;width:12px;display:inline-block;text-align:center;color:#64748b;transition:transform 0.2s ease;}
.fe-details-header{font-size:0.75rem;text-transform:uppercase;letter-spacing:0.12em;color:#8a94a6;margin-bottom:8px;}
.fe-details-path{font-size:1.2rem;font-weight:700;color:#00f0ff;font-family:'Fira Code',monospace;margin-bottom:12px;text-shadow:0 0 10px rgba(0,240,255,0.2);word-break:break-all;}
.fe-details-title{font-size:1.05rem;font-weight:700;color:#fbbf24;margin-bottom:16px;line-height:1.4;}
.fe-details-desc{font-size:0.95rem;color:#cbd5e1;line-height:1.6;}
.fe-details-placeholder{color:#64748b;font-size:0.95rem;display:flex;flex-direction:column;align-items:center;gap:16px;}
.fe-details-placeholder i{font-size:3rem;color:rgba(255,255,255,0.05);text-shadow:none;}
@media (max-width:700px){
.fe-wrapper{flex-direction:column;height:auto;}
.fe-tree-panel{height:350px;}
.fe-details-panel{height:200px;}
}
</style>
<div class="fe-wrapper">
<div class="fe-tree-panel" id="fe-tree-root"></div>
<div class="fe-details-panel" id="fe-details-panel-el">
<div class="fe-details-placeholder">
<i class="fas fa-folder-open"></i>
<span>คลิกเลือกไฟล์หรือไดเรกทอรีในระบบจำลองเพื่อดูรายละเอียดหน้าที่และความหมาย (Click folder/file to view details)</span>
</div>
</div>
</div>
<script>
const treeData = {
name: "/",
type: "folder",
path: "/",
desc: "Root Directory (ไดเรกทอรีราก) - จุดเริ่มต้นและรากฐานของระบบไฟล์ทั้งหมดใน Linux ซึ่งทุกไฟล์และไดเรกทอรีจะแตกสาขาออกไปจากจุดนี้",
children: [
{
name: "bin",
type: "folder",
path: "/bin",
desc: "Binary (คำสั่งพื้นฐาน) - โฟลเดอร์เก็บไฟล์คำสั่งและโปรแกรมพื้นฐานที่จำเป็นสำหรับการใช้งานของระบบและผู้ใช้ทุกคน เช่น ls, cd, cp, mkdir",
},
{
name: "boot",
type: "folder",
path: "/boot",
desc: "Boot loader directory (ไฟล์ระบบเปิดเครื่อง) - เก็บไฟล์และสารสนเทศระบบทั้งหมดที่ใช้ในการเริ่มต้นเปิดเครื่องระบบปฏิบัติการ เช่น GRUB, Kernel (vmlinuz)",
children: [
{
name: "vmlinux",
type: "file",
path: "/boot/vmlinux",
desc: "Kernel File (ไฟล์แกนหลักระบบ) - แกนกลางควบคุมการทำงานหลักทั้งหมดของระบบปฏิบัติการ Linux"
}
]
},
{
name: "dev",
type: "folder",
path: "/dev",
desc: "Devices (ไฟล์ตำแหน่งอุปกรณ์) - แหล่งรวมไฟล์ตำแหน่งอุปกรณ์ต่างๆ ของฮาร์ดแวร์จริงในระบบ เช่น พอร์ต ฮาร์ดดิสก์ และพาร์ทิชันระบบ",
children: [
{
name: "hda",
type: "file",
path: "/dev/hda",
desc: "First IDE HDD (ฮาร์ดดิสก์ IDE ตัวแรก) - ไฟล์เชื่อมโยงและควบคุมตำแหน่งของฮาร์ดดิสก์แบบ IDE ตัวแรกในระบบ"
},
{
name: "hdc",
type: "file",
path: "/dev/hdc",
desc: "CD-ROM / Pseudo-device (ไดรฟ์ซีดี / อุปกรณ์จำลอง) - ไฟล์เชื่อมโยงเครื่องเล่น CD-ROM หรือช่องอุปกรณ์ทดสอบขยะข้อมูลในระบบ"
}
]
},
{
name: "etc",
type: "folder",
path: "/etc",
desc: "Etcetera (ไฟล์ตั้งค่าระบบ) - แหล่งรวบรวมไฟล์สำหรับใช้กำหนดค่าระบบและการตั้งค่าหลัก (Configuration Files) ทั้งหมดของระบบปฏิบัติการ",
children: [
{ name: "bashrc", type: "file", path: "/etc/bashrc", desc: "System defaults and aliases (ตั้งค่า Bash ทั่วทั้งระบบ) - ไฟล์กำหนดค่าเริ่มต้นและคีย์ลัดคำสั่งย่อของ Bash Shell สำหรับผู้ใช้ทุกคน" },
{ name: "crontab", type: "file", path: "/etc/crontab", desc: "Crontab script (ตารางงานอัตโนมัติ) - ไฟล์สคริปต์หลักสำหรับตั้งเวลาเรียกใช้งานคำสั่งตามตารางเวลาที่กำหนดอัตโนมัติ" },
{ name: "exports", type: "file", path: "/etc/exports", desc: "Network filesystem info (แชร์ระบบไฟล์เครือข่าย) - ข้อมูลสิทธิ์และเส้นทางของระบบไฟล์ที่เปิดให้เครื่องอื่นในเครือข่ายเข้าถึงได้" },
{ name: "group", type: "file", path: "/etc/group", desc: "Security group definitions (กลุ่มผู้ใช้งาน) - ไฟล์ระบุรายชื่อกลุ่มความปลอดภัยหลักและกลุ่มสิทธิ์สมาชิกในระบบคอมพิวเตอร์" },
{ name: "hosts", type: "file", path: "/etc/hosts", desc: "IP and hostnames mappings (แผนผังเครื่อง) - ไฟล์แผนผังเชื่อมโยงหมายเลข IP Address กับชื่อเครื่องคอมพิวเตอร์สำหรับการค้นหาแบบ Local" },
{ name: "hosts.allow", type: "file", path: "/etc/hosts.allow", desc: "Hosts allowed access (โฮสต์ที่อนุญาต) - รายชื่อหมายเลขไอพีเครื่องภายนอกที่ได้รับอนุญาตให้ใช้บริการเชื่อมต่อระบบ" },
{ name: "hosts.deny", type: "file", path: "/etc/hosts.deny", desc: "Hosts denied access (โฮสต์ที่บล็อก) - รายชื่อหมายเลขไอพีเครื่องภายนอกที่ถูกจำกัดหรือปฏิเสธสิทธิ์ไม่ให้เชื่อมต่อระบบ" },
{ name: "issue", type: "file", path: "/etc/issue", desc: "Pre-login message (แบนเนอร์ก่อนเข้าสู่ระบบ) - ข้อความแสดงข่าวสารแจ้งสิทธิ์หรือเตือนสติผู้ใช้ซึ่งแสดงผลขึ้นมาก่อนหน้าจอพิมพ์ล็อกอิน" },
{ name: "motd", type: "file", path: "/etc/motd", desc: "Message of the day (ข่าวสารประจำวัน) - ข้อความสั้นแจ้งประกาศผู้ดูแลระบบซึ่งจะแสดงผลขึ้นมาทันทีหลังล็อกอินระบบสำเร็จ" },
{ name: "passwd", type: "file", path: "/etc/passwd", desc: "System user accounts (ข้อมูลบัญชีผู้ใช้งาน) - ข้อมูลรายชื่อผู้ใช้อย่างเป็นทางการ รายละเอียดสิทธิ์ โฮมไดเรกทอรี และประเภทเชลล์" },
{ name: "shadow", type: "file", path: "/etc/shadow", desc: "Encrypted passwords (รหัสผ่านที่เข้ารหัสลับ) - ไฟล์เก็บรหัสผ่านจริงของผู้ใช้ในรูปแบบที่ผ่านการเข้ารหัสลับ เพื่อความปลอดภัยสูงสุด" },
{ name: "skel", type: "folder", path: "/etc/skel", desc: "New user home template (ต้นแบบโฟลเดอร์โฮม) - โฟลเดอร์ต้นแบบที่จะคัดลอกไฟล์ตั้งต้นต่างๆ ไปใส่ให้เมื่อสร้างผู้ใช้ใหม่ในระบบ" },
{ name: "init.d", type: "folder", path: "/etc/init.d", desc: "Service startup scripts (สคริปต์เปิดบริการ) - โฟลเดอร์เก็บสคริปต์ย่อยสำหรับควบคุมระบบในการเปิด-ปิดโปรแกรมบริการต่างๆ (Services)" },
{ name: "rc.d", type: "folder", path: "/etc/rc.d", desc: "Startup/shutdown control (คำสั่งรันระบบปฏิบัติการ) - สคริปต์เริ่มต้นและหยุดการทำงานหลักตามระดับสิทธิ์รันของระบบปฏิบัติการ" },
{ name: "security", type: "folder", path: "/etc/security", desc: "Security configurations (ความปลอดภัยระบบ) - โฟลเดอร์เก็บไฟล์ตั้งค่าจำกัดการล็อกอิน กฎและข้อจำกัดการใช้งานด้านความปลอดภัย" },
{ name: "X11", type: "folder", path: "/etc/X11", desc: "X-window configurations (กราฟิกอินเตอร์เฟซ) - โฟลเดอร์เก็บรายละเอียดคอนฟิกูเรชันสำหรับการแสดงผลหน้าจอแบบ GUI (X11)" }
]
},
{
name: "home",
type: "folder",
path: "/home",
desc: "Home directory (โฮมผู้ใช้งานทั่วไป) - แหล่งจัดเก็บโฟลเดอร์ส่วนตัวและข้อมูลทั้งหมดของผู้ใช้งานทั่วไปในระบบปฏิบัติการ Linux",
children: [
{
name: "wongyos",
type: "folder",
path: "/home/wongyos",
desc: "User Wongyos Home (โฮมของผู้ใช้ wongyos) - โฟลเดอร์ส่วนตัวของบัญชี wongyos สำหรับเก็บไฟล์การทำงาน เอกสาร และตั้งค่าคำสั่งย่อเฉพาะตัว",
children: [
{ name: "Desktop", type: "folder", path: "/home/wongyos/Desktop", desc: "Desktop folder (หน้าจอเดสก์ท็อป) - โฟลเดอร์สำหรับจัดเก็บไฟล์ไอคอนและสิ่งต่างๆ บนหน้าจอหลัก" },
{ name: "Documents", type: "folder", path: "/home/wongyos/Documents", desc: "Documents folder (เอกสารส่วนตัว) - แหล่งบันทึกและจัดเก็บเอกสาร ข้อมูล หรือรายงานต่างๆ ของผู้ใช้งาน" },
{ name: "Downloads", type: "folder", path: "/home/wongyos/Downloads", desc: "Downloads folder (ไฟล์ดาวน์โหลด) - โฟลเดอร์เก็บข้อมูลไฟล์ทุกชนิดที่ดาวน์โหลดมาจากเครือข่ายอินเทอร์เน็ต" },
{ name: "Music", type: "folder", path: "/home/wongyos/Music", desc: "Music folder (ไฟล์เพลง) - โฟลเดอร์เก็บรวบรวมไฟล์เสียงและไฟล์เพลงเฉพาะตัว" },
{ name: "Pictures", type: "folder", path: "/home/wongyos/Pictures", desc: "Pictures folder (ไฟล์รูปภาพ) - โฟลเดอร์จัดเก็บข้อมูลรูปภาพ สื่อภาพนิ่ง และภาพถ่ายต่างๆ" },
{ name: "Public", type: "folder", path: "/home/wongyos/Public", desc: "Public sharing folder (แชร์ไฟล์สาธารณะ) - พื้นที่เปิดให้แชร์ไฟล์ร่วมกันกับบัญชีเครื่องคอมพิวเตอร์อื่นๆ" },
{ name: "Videos", type: "folder", path: "/home/wongyos/Videos", desc: "Videos folder (ไฟล์วิดีโอ) - โฟลเดอร์เก็บบันทึกไฟล์ภาพเคลื่อนไหว ไฟล์ภาพยนตร์ และวิดีโอส่วนตัว" },
{ name: ".bashrc", type: "file", path: "/home/wongyos/.bashrc", desc: "User bash settings (ตั้งค่าคำสั่งย่อ Bash) - สคริปต์ตั้งค่าสภาพแวดล้อม คีย์ลัด และคำสั่งย่อ (aliases) ส่วนตัวผู้ใช้บน Bash Shell" },
{ name: ".cache", type: "folder", path: "/home/wongyos/.cache", desc: "User cache files (ไฟล์แคชผู้ใช้) - โฟลเดอร์เก็บไฟล์แคชการทำงานของแอปพลิเคชันส่วนตัว เพื่อช่วยประหยัดเวลาโหลดข้อมูลซ้ำ" },
{ name: ".history", type: "file", path: "/home/wongyos/.history", desc: "Command history list (ประวัติคำสั่งคำรัน) - ไฟล์ประวัติที่คอยบันทึกคำสั่งทั้งหมดที่ผู้ใช้เคยรันพิมพ์ผ่านเทอร์มินัลย้อนหลัง" },
{ name: ".profile", type: "file", path: "/home/wongyos/.profile", desc: "User profile settings (ตั้งค่าสิ่งแวดล้อมเริ่มต้น) - สคริปต์ตั้งค่าระบบสิ่งแวดล้อมส่วนตัวของบัญชีผู้ใช้เมื่อล็อกอินเข้าสู่เครื่อง" },
{ name: ".zshrc", type: "file", path: "/home/wongyos/.zshrc", desc: "User zsh settings (ตั้งค่าเชลล์ Zsh) - ไฟล์คอนฟิกและคำสั่งย่อเฉพาะตัวสำหรับบัญชีผู้ใช้งานที่เปิด Zsh shell" }
]
}
]
},
{ name: "lib", type: "folder", path: "/lib", desc: "Libraries (ไฟล์ไลบรารีระบบ) - โฟลเดอร์แชร์โมดูลไลบรารีและโมดูลเคอร์เนลหลักที่ช่วยสนับสนุนการรันโปรแกรมระบบคอมพิวเตอร์ในยามเริ่มบูตเครื่อง" },
{ name: "media", type: "folder", path: "/media", desc: "Media (จุดเชื่อมต่ออุปกรณ์พกพา) - แหล่งเชื่อมต่อสำหรับอุปกรณ์จัดเก็บข้อมูลแบบถอดเสียบพกพา เช่น แฟลชไดรฟ์ หรือแผ่นดิสก์ข้อมูล" },
{ name: "mnt", type: "folder", path: "/mnt", desc: "Mount (จุดเมาท์อุปกรณ์ข้อมูลชั่วคราว) - จุดที่ผู้ดูแลระบบใช้สำหรับเชื่อมต่อเพื่อเข้าใช้งานระบบไฟล์ภายนอกอื่นๆ เป็นการชั่วคราว" },
{ name: "opt", type: "folder", path: "/opt", desc: "Optional (ซอฟต์แวร์เสริม) - โฟลเดอร์สำหรับติดตั้งซอฟต์แวร์ประยุกต์และโปรแกรมเสริมเพิ่มเติมที่ไม่ได้ติดตั้งมาพร้อมระบบปฏิบัติการต้นฉบับ" },
{ name: "root", type: "folder", path: "/root", desc: "Root home directory (โฮมของผู้ดูแลระบบ) - พื้นที่สำหรับเก็บบันทึกข้อมูลส่วนตัวทั้งหมดของสิทธิ์ผู้ดูแลระบบหลักสูงสุด (root)" },
{ name: "run", type: "folder", path: "/run", desc: "Runtime directory (ข้อมูลการรันระบบชั่วคราว) - ไดเรกทอรีจัดเก็บข้อมูลสถานะชั่วคราว (Volatile Data) ระหว่างกระบวนการให้บริการของระบบ" },
{ name: "sbin", type: "folder", path: "/sbin", desc: "System binaries (คำสั่งระบบสำหรับผู้ดูแล) - แหล่งรวมคำสั่งและแอปพลิเคชันระบบพิเศษ สำหรับให้สิทธิ์ Admin/Root เรียกรันในการดูแลรักษาระบบ" },
{ name: "srv", type: "folder", path: "/srv", desc: "Services (ข้อมูลการให้บริการ) - เก็บข้อมูล บริการ และไฟล์ผลลัพธ์ของเซิร์ฟเวอร์ เช่น ข้อมูล Web Server ข้อมูล FTP หรือสถิติแชร์ระบบ" },
{ name: "sys", type: "folder", path: "/sys", desc: "System directory (โครงสร้างอุปกรณ์) - จุดเชื่อมต่อไฟล์จำลองของโมดูลไดรเวอร์ อุปกรณ์เชื่อมต่อ และเคอร์เนลจริงสำหรับตั้งค่าระบบปฏิบัติการ" },
{ name: "tmp", type: "folder", path: "/tmp", desc: "Temporary (ไฟล์ชั่วคราวระบบ) - โฟลเดอร์เก็บไฟล์ชั่วคราวของแอปพลิเคชันระบบ ซึ่งจะถูกลบหรือเคลียร์ข้อมูลออกเมื่อเครื่องทำการรีสตาร์ทระบบ" },
{
name: "usr",
type: "folder",
path: "/usr",
desc: "User directory (โปรแกรมผู้ใช้งานทั่วไป) - เก็บโปรแกรม คำสั่ง เอกสารคู่มือ และไฟล์ไลบรารีระบบสำหรับผู้ใช้ทั่วไปใช้งาน (เป็นโหมด Read-Only)",
children: [
{ name: "bin", type: "folder", path: "/usr/bin", desc: "User executable files (โปรแกรมใช้ทั่วไป) - แหล่งรวมโปรแกรมคำสั่งใช้งานเสริมภายนอกเพิ่มเติมที่ผู้ใช้งานทั่วไปสามารถเรียกใช้งานได้" },
{ name: "include", type: "folder", path: "/usr/include", desc: "C header files (ไฟล์ส่วนหัวภาษา C) - แฟ้มเก็บไฟล์ไลบรารี Header (.h) มาตรฐานสำหรับเขียนหรือคอมไพล์โปรแกรมด้วยภาษา C/C++" },
{ name: "lib", type: "folder", path: "/usr/lib", desc: "Libraries (ไลบรารีระบบทั่วไป) - ไฟล์ไลบรารีระบบภายนอกเสริมที่คอยสนับสนุนการทำงานของโปรแกรมในไดเรกทอรี /usr" },
{ name: "sbin", type: "folder", path: "/usr/sbin", desc: "System executables (คำสั่งสำหรับผู้ดูแลเครื่อง) - คำสั่งและแอปพลิเคชันระดับผู้ดูแลเครื่องพิเศษที่เกี่ยวข้องกับการจัดการและการซ่อมบำรุงเครือข่ายคอมพิวเตอร์" },
{ name: "share", type: "folder", path: "/usr/share", desc: "Shareable text files (คู่มือเอกสารระบบ) - ไฟล์เอกสารคำอธิบาย คู่มืออ้างอิงคำสั่งระบบ (man pages) และสคริปต์สากลที่แชร์สิทธิ์กันได้" }
]
},
{
name: "var",
type: "folder",
path: "/var",
desc: "Variable directory (ข้อมูลผันแปรระบบ) - แหล่งเก็บบันทึกข้อมูลระบบที่มีการเคลื่อนไหว เปลี่ยนแปลง และอัปเดตอย่างต่อเนื่อง เช่น ล็อกบันทึกกิจกรรม คิวส่งของระบบ",
children: [
{ name: "cache", type: "folder", path: "/var/cache", desc: "Cache (พื้นที่เก็บแคชแอป) - เก็บไฟล์แคชและข้อมูลประมวลผลชั่วคราวของซอฟต์แวร์ ช่วยเร่งความเร็วในการเรียกใช้งานซ้ำ" },
{ name: "spool", type: "folder", path: "/var/spool", desc: "Spool (พื้นที่คิวพักข้อมูล) - พื้นที่สำหรับจัดคิวพักข้อมูลก่อนส่งต่อไปทำงาน เช่น คิวพิมพ์เอกสาร และคิวพักส่งเมล" },
{ name: "tmp", type: "folder", path: "/var/tmp", desc: "Temporary (ไฟล์ชั่วคราวข้ามบูต) - โฟลเดอร์เก็บไฟล์ชั่วคราวที่จะไม่มีการลบข้อมูลไปแม้จะรีสตาร์ทระบบเปิดระบบเครื่องขึ้นใหม่ก็ตาม" },
{
name: "log",
type: "folder",
path: "/var/log",
desc: "Log files (โฟลเดอร์เก็บประวัติบันทึก) - แหล่งรวบรวมไฟล์บันทึกกิจกรรม ประวัติการเปิด และข้อผิดพลาดต่างๆ ของคอมพิวเตอร์",
children: [
{ name: "messages", type: "file", path: "/var/log/messages", desc: "Global system messages (ประวัติล็อกไฟล์รวม) - รายละเอียดบันทึกกิจกรรมโดยรวม ปัญหาระบบ และประวัติความปลอดภัยของตัวระบบปฏิบัติการ" },
{ name: "lastlog", type: "file", path: "/var/log/lastlog", desc: "User last login (ล็อกอินล่าสุดผู้ใช้) - รายละเอียดประวัติล็อกอินเข้าระบบครั้งหลังสุดของผู้ใช้งานทุกคน แยกรายบัญชี" },
{ name: "maillog", type: "file", path: "/var/log/maillog", desc: "Email usage log (ล็อกประวัติระบบอีเมล) - บันทึกเหตุการณ์การจัดส่ง รับอีเมล และล็อกการตั้งค่าต่างๆ ของระบบอีเมล" }
]
}
]
}
]
};

function buildTreeHTML(node) {
const isFolder = node.type === 'folder';
const hasChildren = node.children && node.children.length > 0;
let childrenHTML = '';
if (hasChildren) {
childrenHTML = `<div class="fe-node-children" id="children-${node.path.replace(/[^a-zA-Z0-9]/g, '-')}">
${node.children.map(child => buildTreeHTML(child)).join('')}
</div>`;
}
const icon = isFolder 
? `<i class="fas fa-folder text-warning"></i>` 
: `<i class="fas fa-file-alt text-info"></i>`;
const toggleIcon = hasChildren 
? `<span class="fe-toggle-arrow"><i class="fas fa-chevron-right"></i></span>` 
: `<span style="width: 12px; display: inline-block;"></span>`;
return `<div class="fe-node">
<div class="fe-node-label" onclick="selectNode(this, '${node.path}')">
${toggleIcon}
${icon}
<span>${node.name}${isFolder ? '/' : ''}</span>
</div>
${childrenHTML}
</div>`;
}

function selectNode(el, path) {
document.querySelectorAll('.fe-node-label').forEach(n => n.classList.remove('active'));
el.classList.add('active');
const node = findNodeByPath(treeData, path);
if (node) {
updateDetailsPanel(node);
const childrenContainer = el.nextElementSibling;
if (childrenContainer && childrenContainer.classList.contains('fe-node-children')) {
const arrow = el.querySelector('.fe-toggle-arrow i');
if (childrenContainer.classList.contains('expanded')) {
childrenContainer.classList.remove('expanded');
if (arrow) arrow.className = 'fas fa-chevron-right';
} else {
childrenContainer.classList.add('expanded');
if (arrow) arrow.className = 'fas fa-chevron-down';
}
}
}
}

function findNodeByPath(node, path) {
if (node.path === path) return node;
if (node.children) {
for (let child of node.children) {
const found = findNodeByPath(child, path);
if (found) return found;
}
}
return null;
}

function updateDetailsPanel(node) {
const panel = document.getElementById('fe-details-panel-el');
if (panel) {
panel.className = 'fe-details-panel selected';
let title = node.name;
let desc = node.desc;
const parts = node.desc.split(' - ');
if (parts.length >= 2) {
title = parts[0];
desc = parts.slice(1).join(' - ');
}
panel.innerHTML = `
<div class="fe-details-header">Selected ${node.type === 'folder' ? 'Directory' : 'File'}</div>
<div class="fe-details-path">${node.path}</div>
<div class="fe-details-title">${title}</div>
<div class="fe-details-desc">${desc}</div>
`;
}
}

const treeRoot = document.getElementById('fe-tree-root');
if (treeRoot) {
treeRoot.innerHTML = buildTreeHTML(treeData);
const firstChildren = treeRoot.querySelector('.fe-node-children');
if (firstChildren) {
firstChildren.classList.add('expanded');
const firstArrow = treeRoot.querySelector('.fe-toggle-arrow i');
if (firstArrow) firstArrow.className = 'fas fa-chevron-down';
}
}
</script>"""

# Replace Block 11 with the Bilingual File Explorer Component
block_11 = blocks[11]
block_11['value'] = "### 📂 Linux Directory & File Structure Explorer\n\n- สำรวจระบบไฟล์คอมพิวเตอร์ของ Linux ผ่านโปรแกรมจำลองโฟลเดอร์แบบโต้ตอบได้ด้านล่าง คลิกที่ชื่อไดเรกทอรีหรือไฟล์เพื่อสืบค้นหน้าที่การทำงานและคำแปล (Bilingual)\n\n" + html_explorer

blocks[11] = block_11

# Empty out all subsequent table blocks (indices 12 to 38)
for i in range(12, 39):
    blocks[i]['value'] = ""

# Save and Commit
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
db.session.commit()
print("Bilingual File Tree Explorer component deployed and intermediate tables cleared successfully!")
