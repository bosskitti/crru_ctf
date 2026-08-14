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

# The HTML replacement code for the static CSS tree (completely flat, 0-indentation)
html_static_tree = """<style>
.simple-tree-container{width:100%;max-width:820px;margin:2rem 0;background:rgba(15,17,26,0.4);border:1px solid rgba(255,255,255,0.05);border-radius:12px;padding:24px;box-shadow:inset 0 0 20px rgba(0,0,0,0.4);font-family:'Fira Code',monospace,Courier;font-size:0.9rem;color:#cbd5e1;line-height:1.8;overflow-x:auto;}
.simple-tree-container::-webkit-scrollbar{height:6px;}
.simple-tree-container::-webkit-scrollbar-track{background:rgba(0,0,0,0.2);border-radius:3px;}
.simple-tree-container::-webkit-scrollbar-thumb{background:rgba(255,255,255,0.1);border-radius:3px;}
.st-root{font-weight:700;color:#fbbf24;text-shadow:0 0 8px rgba(251,191,36,0.15);}
.st-folder{margin-left:20px;border-left:1px dashed rgba(255,255,255,0.12);padding-left:15px;}
.st-item{display:flex;align-items:flex-start;gap:8px;margin:6px 0;}
.st-name{color:#00c0ff;font-weight:600;white-space:nowrap;}
.st-name.file{color:#3ddc84;}
.st-desc{color:#94a3b8;font-size:0.85rem;}
</style>
<div class="simple-tree-container">
<div class="st-item"><i class="fas fa-folder-open text-warning"></i> <span class="st-name st-root">/ (root)</span> <span class="st-desc">— Root Directory (ไดเรกทอรีราก) - จุดเริ่มต้นและรากฐานของระบบไฟล์ทั้งหมดใน Linux ซึ่งทุกไฟล์จะแตกสาขาออกไปจากจุดนี้</span></div>
<div class="st-folder">
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">bin/</span> <span class="st-desc">— Binary (คำสั่งพื้นฐาน) - โฟลเดอร์เก็บไฟล์คำสั่งและโปรแกรมพื้นฐานที่จำเป็นสำหรับผู้ใช้ทุกคน (เช่น ls, cd, cp, mkdir)</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">boot/</span> <span class="st-desc">— Boot (ไฟล์ระบบเปิดเครื่อง) - เก็บไฟล์และข้อมูลระบบทั้งหมดที่ใช้ในการเริ่มต้นเปิดเครื่องระบบปฏิบัติการ</span></div>
<div class="st-folder">
<div class="st-item"><i class="fas fa-file-alt text-success"></i> <span class="st-name file">vmlinux</span> <span class="st-desc">— Kernel File (ไฟล์แกนหลักระบบ) - แกนกลางควบคุมการทำงานหลักทั้งหมดของระบบปฏิบัติการ Linux</span></div>
</div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">dev/</span> <span class="st-desc">— Devices (ไฟล์ตำแหน่งอุปกรณ์) - แหล่งรวมไฟล์ตำแหน่งอุปกรณ์ต่างๆ ของฮาร์ดแวร์จริงในระบบ เช่น ฮาร์ดดิสก์ และการ์ดเชื่อมต่อ</span></div>
<div class="st-folder">
<div class="st-item"><i class="fas fa-file-alt text-success"></i> <span class="st-name file">hda</span> <span class="st-desc">— First IDE HDD (ฮาร์ดดิสก์ IDE ตัวแรก) - ไฟล์เชื่อมโยงและควบคุมตำแหน่งของฮาร์ดดิสก์แบบ IDE ตัวแรกในระบบ</span></div>
<div class="st-item"><i class="fas fa-file-alt text-success"></i> <span class="st-name file">hdc</span> <span class="st-desc">— CD-ROM / Pseudo-device (ไดรฟ์ซีดี / อุปกรณ์จำลอง) - ไฟล์เชื่อมโยงเครื่องเล่น CD-ROM หรือช่องอุปกรณ์ทดสอบขยะข้อมูล</span></div>
</div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">etc/</span> <span class="st-desc">— Etcetera (ไฟล์ตั้งค่าระบบ) - แหล่งรวบรวมไฟล์สำหรับใช้กำหนดค่าระบบและการตั้งค่าหลัก (Configuration Files) ทั้งหมด</span></div>
<div class="st-folder">
<div class="st-item"><i class="fas fa-file-alt text-success"></i> <span class="st-name file">bashrc</span> <span class="st-desc">— System defaults and aliases (ตั้งค่า Bash ทั่วระบบ) - ไฟล์กำหนดค่าเริ่มต้นและคีย์ลัดคำสั่งย่อของ Bash Shell สำหรับผู้ใช้ทุกคน</span></div>
<div class="st-item"><i class="fas fa-file-alt text-success"></i> <span class="st-name file">crontab</span> <span class="st-desc">— Crontab script (ตารางงานอัตโนมัติ) - ไฟล์สคริปต์หลักสำหรับตั้งเวลาเรียกใช้งานคำสั่งตามตารางเวลาที่กำหนดอัตโนมัติ</span></div>
<div class="st-item"><i class="fas fa-file-alt text-success"></i> <span class="st-name file">exports</span> <span class="st-desc">— Network filesystem info (แชร์ไฟล์เครือข่าย) - ข้อมูลสิทธิ์และเส้นทางของระบบไฟล์ที่เปิดให้เครื่องอื่นในเครือข่ายเข้าถึงได้</span></div>
<div class="st-item"><i class="fas fa-file-alt text-success"></i> <span class="st-name file">group</span> <span class="st-desc">— Security group definitions (กลุ่มผู้ใช้งาน) - ไฟล์ระบุรายชื่อกลุ่มความปลอดภัยหลักและกลุ่มสิทธิ์สมาชิกในระบบ</span></div>
<div class="st-item"><i class="fas fa-file-alt text-success"></i> <span class="st-name file">hosts</span> <span class="st-desc">— IP and hostnames mappings (แผนผังเครื่อง) - ไฟล์แผนผังเชื่อมโยงหมายเลข IP Address กับชื่อเครื่องคอมพิวเตอร์</span></div>
<div class="st-item"><i class="fas fa-file-alt text-success"></i> <span class="st-name file">hosts.allow</span> <span class="st-desc">— Hosts allowed access (โฮสต์ที่อนุญาต) - รายชื่อหมายเลขไอพีเครื่องภายนอกที่ได้รับอนุญาตให้เชื่อมต่อเข้าใช้งานระบบ</span></div>
<div class="st-item"><i class="fas fa-file-alt text-success"></i> <span class="st-name file">hosts.deny</span> <span class="st-desc">— Hosts denied access (โฮสต์ที่บล็อก) - รายชื่อหมายเลขไอพีเครื่องภายนอกที่ถูกจำกัดหรือปฏิเสธสิทธิ์เข้าใช้งาน</span></div>
<div class="st-item"><i class="fas fa-file-alt text-success"></i> <span class="st-name file">issue</span> <span class="st-desc">— Pre-login message (ข้อความเตือนก่อนเข้าระบบ) - ข้อความแสดงข่าวสารแจ้งสิทธิ์หรือเตือนสิทธิ์แสดงก่อนหน้าล็อกอิน</span></div>
<div class="st-item"><i class="fas fa-file-alt text-success"></i> <span class="st-name file">motd</span> <span class="st-desc">— Message of the day (ข่าวสารประจำวัน) - ข้อความแสดงประกาศผู้ดูแลระบบหลังล็อกอินเข้าระบบสำเร็จ</span></div>
<div class="st-item"><i class="fas fa-file-alt text-success"></i> <span class="st-name file">passwd</span> <span class="st-desc">— System user accounts (ข้อมูลบัญชีผู้ใช้งาน) - ข้อมูลรายชื่อผู้ใช้อย่างเป็นทางการ รายละเอียดสิทธิ์ โฮมไดเรกทอรี และประเภทเชลล์</span></div>
<div class="st-item"><i class="fas fa-file-alt text-success"></i> <span class="st-name file">shadow</span> <span class="st-desc">— Encrypted passwords (รหัสผ่านที่เข้ารหัสลับ) - ไฟล์เก็บรหัสผ่านผู้ใช้งานในรูปแบบเข้ารหัสลับเพื่อความปลอดภัย</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">skel/</span> <span class="st-desc">— New user home template (ต้นแบบโฮม) - โฟลเดอร์ต้นแบบที่จะคัดลอกไฟล์ตั้งต้นให้เมื่อสร้างผู้ใช้ใหม่ในระบบ</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">init.d/</span> <span class="st-desc">— Service startup scripts (สคริปต์เปิดบริการ) - โฟลเดอร์เก็บสคริปต์ย่อยสำหรับควบคุมการเปิด-ปิดโปรแกรมบริการต่างๆ</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">rc.d/</span> <span class="st-desc">— Startup/shutdown control (คำสั่งรันระบบปฏิบัติการ) - สคริปต์เริ่มต้นและหยุดการทำงานหลักตามระดับสิทธิ์รันระบบ</span></div>
<div class="st-folder">
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">init.d/</span> <span class="st-desc">— Initialization scripts (สคริปต์เริ่มต้นรันระบบ) - โฟลเดอร์เก็บไฟล์ตั้งค่าเริ่มต้นโปรแกรมระบบขณะบูตเครื่อง</span></div>
</div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">security/</span> <span class="st-desc">— Security configurations (ความปลอดภัยระบบ) - ไฟล์ตั้งค่าจำกัดการล็อกอินและจำกัดสิทธิ์ความปลอดภัยต่างๆ</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">X11/</span> <span class="st-desc">— X-window configurations (หน้าต่างกราฟิก) - ไฟล์เก็บรายละเอียดตั้งค่าระบบหน้าจอแสดงผลแบบกราฟิก GUI</span></div>
</div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">home/</span> <span class="st-desc">— Home directory (โฮมผู้ใช้งานทั่วไป) - แหล่งจัดเก็บโฟลเดอร์ส่วนตัวและข้อมูลทั้งหมดของผู้ใช้งานทั่วไปในระบบ</span></div>
<div class="st-folder">
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">wongyos/</span> <span class="st-desc">— User Wongyos Home (โฮมของผู้ใช้ wongyos) - โฟลเดอร์และโฟลเดอร์ส่วนตัวของบัญชี wongyos</span></div>
<div class="st-folder">
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">Desktop/</span> <span class="st-desc">— Desktop folder (หน้าจอเดสก์ท็อป) - โฟลเดอร์จัดเก็บไฟล์ไอคอนและสิ่งต่างๆ บนหน้าจอหลัก</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">Documents/</span> <span class="st-desc">— Documents folder (เอกสารส่วนตัว) - แหล่งบันทึกและจัดเก็บเอกสาร ข้อมูล หรือรายงานต่างๆ ของผู้ใช้งาน</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">Downloads/</span> <span class="st-desc">— Downloads folder (ไฟล์ดาวน์โหลด) - โฟลเดอร์เก็บข้อมูลไฟล์ทุกชนิดที่ดาวน์โหลดมาจากอินเทอร์เน็ต</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">Music/</span> <span class="st-desc">— Music folder (ไฟล์เพลง) - โฟลเดอร์เก็บรวบรวมไฟล์เสียงและไฟล์เพลงส่วนตัว</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">Pictures/</span> <span class="st-desc">— Pictures folder (ไฟล์รูปภาพ) - โฟลเดอร์จัดเก็บข้อมูลรูปภาพ สื่อภาพนิ่ง และภาพถ่ายต่างๆ</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">Public/</span> <span class="st-desc">— Public sharing folder (แชร์ไฟล์สาธารณะ) - พื้นที่เปิดให้แชร์ไฟล์ร่วมกันกับบัญชีคอมพิวเตอร์เครื่องอื่น</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">Videos/</span> <span class="st-desc">— Videos folder (ไฟล์วิดีโอ) - โฟลเดอร์เก็บบันทึกไฟล์ภาพเคลื่อนไหว และวิดีโอส่วนตัว</span></div>
<div class="st-item"><i class="fas fa-file-alt text-success"></i> <span class="st-name file">.bashrc</span> <span class="st-desc">— User bash settings (ตั้งค่าคำสั่งย่อ Bash) - สคริปต์ตั้งค่าสภาพแวดล้อม คีย์ลัดคำสั่งย่อสำหรับ Bash Shell ของผู้ใช้</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">.cache/</span> <span class="st-desc">— User cache files (ไฟล์แคชผู้ใช้) - โฟลเดอร์เก็บไฟล์แคชการทำงาน เพื่อประหยัดเวลาการประมวลผล</span></div>
<div class="st-item"><i class="fas fa-file-alt text-success"></i> <span class="st-name file">.history</span> <span class="st-desc">— Command history list (ประวัติคำสั่งรัน) - ไฟล์ประวัติบันทึกประวัติการใช้คำสั่งที่พิมพ์ผ่านเทอร์มินัลทั้งหมด</span></div>
<div class="st-item"><i class="fas fa-file-alt text-success"></i> <span class="st-name file">.profile</span> <span class="st-desc">— User profile settings (ตั้งค่าเริ่มต้นผู้ใช้) - สคริปต์รันสิ่งแวดล้อมตั้งต้นของบัญชีผู้ใช้เมื่อล็อกอินเข้าสู่เครื่อง</span></div>
<div class="st-item"><i class="fas fa-file-alt text-success"></i> <span class="st-name file">.zshrc</span> <span class="st-desc">— User zsh settings (ตั้งค่าเชลล์ Zsh) - ไฟล์คอนฟิกและคำสั่งย่อเฉพาะตัวสำหรับผู้ใช้ Zsh shell</span></div>
</div>
</div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">lib/</span> <span class="st-desc">— Libraries (ไฟล์ไลบรารีระบบ) - โฟลเดอร์แชร์โมดูลไลบรารีสนับสนุนการทำงานระบบคอมพิวเตอร์ยามบูตเครื่อง</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">media/</span> <span class="st-desc">— Media (จุดเชื่อมต่ออุปกรณ์พกพา) - แหล่งเชื่อมต่อสำหรับอุปกรณ์จัดเก็บข้อมูลแบบถอดเสียบพกพา เช่น แฟลชไดรฟ์</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">mnt/</span> <span class="st-desc">— Mount (จุดเมาท์อุปกรณ์ชั่วคราว) - จุดเชื่อมต่อระบบไฟล์ภายนอกอื่นๆ เป็นการชั่วคราวเพื่อคัดลอกหรือจัดการข้อมูล</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">opt/</span> <span class="st-desc">— Optional (ซอฟต์แวร์เสริม) - โฟลเดอร์สำหรับติดตั้งซอฟต์แวร์ประยุกต์เสริมเพิ่มเติมที่ไม่ได้ติดตั้งมาพร้อมระบบดั้งเดิม</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">root/</span> <span class="st-desc">— Root home directory - พื้นที่และโฟลเดอร์โฮมส่วนตัวทั้งหมดของผู้ดูแลระบบหลักสูงสุด (root/superuser)</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">run/</span> <span class="st-desc">— Runtime directory - เก็บข้อมูลสถานะระบบชั่วคราว (Volatile Data) ระหว่างกระบวนการทำงาน</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">sbin/</span> <span class="st-desc">— System binaries (คำสั่งเฉพาะผู้ดูแล) - แหล่งรวมคำสั่งรันระบบพิเศษสำหรับให้ผู้ดูแลระบบใช้งานซ่อมบำรุง</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">srv/</span> <span class="st-desc">— Services (ข้อมูลการให้บริการ) - เก็บไฟล์ข้อมูลที่ให้บริการเครือข่าย เช่น ข้อมูลหน้าเว็บ หรือ FTP</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">sys/</span> <span class="st-desc">— System directory (โครงสร้างอุปกรณ์เคอร์เนล) - จุดเชื่อมไฟล์จำลองของโมดูลไดรเวอร์และอุปกรณ์จริงสำหรับเคอร์เนล</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">tmp/</span> <span class="st-desc">— Temporary (ไฟล์ชั่วคราวระบบ) - โฟลเดอร์เก็บไฟล์ชั่วคราวแอปพลิเคชันระบบ ซึ่งจะถูกล้างเมื่อเปิดเครื่องใหม่</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">usr/</span> <span class="st-desc">— User directory (โปรแกรมผู้ใช้งานทั่วไป) - เก็บโปรแกรม คำสั่ง และไฟล์ไลบรารีระบบสำหรับผู้ใช้ทั่วไปรันใช้งาน</span></div>
<div class="st-folder">
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">bin/</span> <span class="st-desc">— User executable files (โปรแกรมใช้ทั่วไป) - แหล่งรวมไฟล์โปรแกรมคำสั่งประยุกต์เสริมที่ผู้ใช้ทั่วไปรันได้</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">include/</span> <span class="st-desc">— C header files (ไฟล์ส่วนหัวภาษา C) - แฟ้มเก็บไฟล์ Header (.h) มาตรฐานสำหรับรันและเขียนภาษา C/C++</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">lib/</span> <span class="st-desc">— Libraries (ไลบรารีระบบทั่วไป) - ไฟล์ไลบรารีระบบแชร์ภายนอกคอยสนับสนุนโปรแกรมในโฟลเดอร์ /usr</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">sbin/</span> <span class="st-desc">— System executables (คำสั่งควบคุมระบบ) - คำสั่งพิเศษสำหรับผู้ดูแลเครื่องระดับสูงควบคุมการดูแลรักษาเครื่อง</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">share/</span> <span class="st-desc">— Shareable text files (คู่มือเอกสารระบบ) - ไฟล์คำอธิบาย คู่มือช่วยเหลืออ้างอิง และคู่มือการใช้คำสั่ง (man pages)</span></div>
</div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">var/</span> <span class="st-desc">— Variable directory (ข้อมูลผันแปรระบบ) - แหล่งเก็บบันทึกข้อมูลระบบที่มีการเคลื่อนไหว อัปเดต และบันทึกประวัติอย่างต่อเนื่อง</span></div>
<div class="st-folder">
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">cache/</span> <span class="st-desc">— Cache (แคชแอป) - แหล่งเก็บข้อมูลแคชสำหรับช่วยเร่งการประมวลผลการทำงานโปรแกรมให้เร็วขึ้น</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">spool/</span> <span class="st-desc">— Spool (คิวพักข้อมูล) - พื้นที่สำหรับจัดคิวข้อมูลรอประมวลผล เช่น คิวเมลรอจัดส่ง คิวสั่งพิมพ์เอกสาร</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">tmp/</span> <span class="st-desc">— Temporary (ไฟล์ชั่วคราวข้ามบูต) - โฟลเดอร์เก็บไฟล์ชั่วคราวของแอปพลิเคชันระบบที่จะไม่ถูกล้างเมื่อเครื่องเริ่มทำงานใหม่</span></div>
<div class="st-item"><i class="fas fa-folder text-info"></i> <span class="st-name">log/</span> <span class="st-desc">— Log files (โฟลเดอร์เก็บประวัติบันทึก) - แหล่งรวมประวัติการเข้าใช้งาน ระบบ ล็อกระบบ และความปลอดภัยทั้งหมด</span></div>
<div class="st-folder">
<div class="st-item"><i class="fas fa-file-alt text-success"></i> <span class="st-name file">messages</span> <span class="st-desc">— Global system messages (บันทึกล็อกไฟล์รวม) - ล็อกกิจกรรมรวม ปัญหาระบบ และเหตุการณ์สำคัญทั้งหมดของ OS</span></div>
<div class="st-item"><i class="fas fa-file-alt text-success"></i> <span class="st-name file">lastlog</span> <span class="st-desc">— User last login (ล็อกอินล่าสุดผู้ใช้) - รายละเอียดสถิติประวัติการล็อกอินเข้าระบบหลังสุดของผู้ใช้งานทุกคนแยกรายบัญชี</span></div>
<div class="st-item"><i class="fas fa-file-alt text-success"></i> <span class="st-name file">maillog</span> <span class="st-desc">— Email usage log (ล็อกประวัติระบบอีเมล) - บันทึกเหตุการณ์การรับส่งจดหมายอิเล็กทรอนิกส์ของระบบเซิร์ฟเวอร์อีเมล</span></div>
</div>
</div>
</div>
</div>
"""

# Replace block 11 with the static tree, which has all details nested
block_11 = blocks[11]
block_11['value'] = "### 📂 โครงสร้างไดเรกทอรีและไฟล์สำคัญใน Linux (Linux Directory & File Structure Tree)\n\n- แผนผังจำลองโครงสร้างระบบไฟล์ของ Linux ในรูปแบบแผนภูมิลำดับขั้น (Bilingual) แสดงความหมายและไฟล์สำคัญที่เกี่ยวข้อง\n\n" + html_static_tree
blocks[11] = block_11

# Empty out all subsequent table blocks (indices 12 to 38)
for i in range(12, 39):
    blocks[i]['value'] = ""

# Save and Commit
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
db.session.commit()
print("Bilingual File structure upgraded to Static CSS tree view successfully!")
