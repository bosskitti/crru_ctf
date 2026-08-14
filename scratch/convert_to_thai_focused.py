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

# 1. Update Block 5 (Architecture Blueprint)
blocks[5]['value'] = blocks[5]['value'].replace(
    '<span class="highlight">Applications & Utilities</span> (โปรแกรมประยุกต์และยูทิลิตี้) — Programs to do the user and specialized-level task',
    '<span class="highlight">Applications & Utilities</span> — Programs to do the user and specialized-level task'
).replace(
    '<span class="highlight">Shells</span> (ตัวตีความคำสั่ง) — Interface which takes commands from user and executes kernel\'s functions',
    '<span class="highlight">Shells</span> — Interface which takes commands from user and executes kernel\'s functions'
).replace(
    '<span class="highlight">Kernel</span> (แกนกลางระบบปฏิบัติการ) — Core part of the OS, responsible for all the major activities of the Linux OS',
    '<span class="highlight">Kernel</span> — Core part of the OS, responsible for all the major activities of the Linux OS'
).replace(
    '<span class="highlight">Hardware</span> (ฮาร์ดแวร์อุปกรณ์) — Physical devices which execute calculations and instructions',
    '<span class="highlight">Hardware</span> — Physical devices which execute calculations and instructions'
)

# 2. Update Block 11 (Directory Tree)
blocks[11]['value'] = blocks[11]['value'].replace(
    "Root directory (ไดเรกทอรีราก) - จุดเริ่มต้นและรากฐานของระบบไฟล์ทั้งหมดใน Linux",
    "Root directory — จุดเริ่มต้นและรากฐานของระบบไฟล์ทั้งหมดใน Linux"
).replace(
    "Binary (คำสั่งพื้นฐาน) - โฟลเดอร์เก็บไฟล์คำสั่งและโปรแกรมพื้นฐานที่จำเป็นสำหรับผู้ใช้ทุกคน",
    "Binary — โฟลเดอร์เก็บไฟล์คำสั่งและโปรแกรมพื้นฐานที่จำเป็นสำหรับผู้ใช้ทุกคน"
).replace(
    "Optional (ซอฟต์แวร์เสริม) - เก็บแอปพลิเคชันและโปรแกรมเสริมเพิ่มเติมที่ไม่ได้ติดตั้งมาพร้อมระบบ",
    "Optional — เก็บแอปพลิเคชันและโปรแกรมเสริมเพิ่มเติมที่ไม่ได้ติดตั้งมาพร้อมระบบ"
).replace(
    "Boot (ไฟล์ระบบเปิดเครื่อง) - เก็บไฟล์สำคัญที่ใช้ในการเริ่มระบบปฏิบัติการ เช่น Kernel และ GRUB",
    "Boot — เก็บไฟล์สำคัญที่ใช้ในการเริ่มระบบปฏิบัติการ เช่น Kernel และ GRUB"
).replace(
    "Root User Home (โฮมของผู้ดูแลระบบ) - พื้นที่เก็บข้อมูลส่วนตัวของสิทธิ์ผู้ดูแลระบบหลัก (root)",
    "Root User Home — พื้นที่เก็บข้อมูลส่วนตัวของสิทธิ์ผู้ดูแลระบบหลัก (root)"
).replace(
    "Devices (ไฟล์ตำแหน่งอุปกรณ์) - แหล่งเก็บไฟล์เสมือนที่เชื่อมโยงกับฮาร์ดแวร์และอุปกรณ์เชื่อมต่อทั้งหมดในระบบ",
    "Devices — แหล่งเก็บไฟล์เสมือนที่เชื่อมโยงกับฮาร์ดแวร์และอุปกรณ์เชื่อมต่อทั้งหมดในระบบ"
).replace(
    "System Binaries (คำสั่งเฉพาะผู้ดูแล) - เก็บไฟล์คำสั่งระบบที่จำเป็นเฉพาะของผู้ดูแลระบบสำหรับจัดการเครื่อง",
    "System Binaries — เก็บไฟล์คำสั่งระบบที่จำเป็นเฉพาะของผู้ดูแลระบบสำหรับจัดการเครื่อง"
).replace(
    "Etcetera (ไฟล์ตั้งค่าระบบ) - แหล่งรวมไฟล์กำหนดค่าและคอนฟิกูเรชัน (Configuration) ของระบบทั้งหมด",
    "Etcetera — แหล่งรวมไฟล์กำหนดค่าและคอนฟิกูเรชัน (Configuration) ของระบบทั้งหมด"
).replace(
    "Services (ข้อมูลการให้บริการ) - เก็บไฟล์และข้อมูลที่ใช้ในการให้บริการเครือข่าย เช่น ข้อมูลของ Web Server",
    "Services — เก็บไฟล์และข้อมูลที่ใช้ในการให้บริการเครือข่าย เช่น ข้อมูลของ Web Server"
).replace(
    "Home directory (โฮมผู้ใช้งานทั่วไป) - แหล่งเก็บข้อมูลและโฟลเดอร์ส่วนตัวของผู้ใช้งานทั่วไปในระบบ",
    "Home directory — แหล่งเก็บข้อมูลและโฟลเดอร์ส่วนตัวของผู้ใช้งานทั่วไปในระบบ"
).replace(
    "Temporary (ไฟล์ชั่วคราวระบบ) - โฟลเดอร์เก็บไฟล์ชั่วคราว ซึ่งจะถูกล้างข้อมูลออกโดยอัตโนมัติเมื่อรีสตาร์ทระบบ",
    "Temporary — โฟลเดอร์เก็บไฟล์ชั่วคราว ซึ่งจะถูกล้างข้อมูลออกโดยอัตโนมัติเมื่อรีสตาร์ทระบบ"
).replace(
    "Libraries (ไฟล์ไลบรารีระบบ) - แหล่งเก็บโมดูลระบบและไลบรารีแชร์ที่จำเป็นในการรันโปรแกรมหลัก",
    "Libraries — แหล่งเก็บโมดูลระบบและไลบรารีแชร์ที่จำเป็นในการรันโปรแกรมหลัก"
).replace(
    "User (โปรแกรมผู้ใช้งานทั่วไป) - เก็บโปรแกรม คำสั่ง และไฟล์ขนาดใหญ่สำหรับผู้ใช้ทั่วไปใช้งาน (โหมดอ่านอย่างเดียว)",
    "User — เก็บโปรแกรม คำสั่ง และไฟล์ขนาดใหญ่สำหรับผู้ใช้ทั่วไปใช้งาน (โหมดอ่านอย่างเดียว)"
).replace(
    "User Executables (คำสั่งผู้ใช้ทั่วไป) - คำสั่งโปรแกรมทั่วไปสำหรับผู้ใช้งานในระบบ",
    "User Executables — คำสั่งโปรแกรมทั่วไปสำหรับผู้ใช้งานในระบบ"
).replace(
    "Header Files (ไฟล์ส่วนหัวภาษา C) - แฟ้มเก็บ Header (.h) มาตรฐานสำหรับเขียนและคอมไพล์โปรแกรม",
    "Header Files — แฟ้มเก็บ Header (.h) มาตรฐานสำหรับเขียนและคอมไพล์โปรแกรม"
).replace(
    "Libraries (ไลบรารีมาตรฐานทั่วไป) - ไฟล์ไลบรารีมาตรฐานสำหรับการรันโปรแกรมทั่วไป",
    "Libraries — ไฟล์ไลบรารีมาตรฐานสำหรับการรันโปรแกรมทั่วไป"
).replace(
    "System Executables (คำสั่งควบคุมระบบ) - คำสั่งสำหรับผู้ดูแลระบบระดับสูงเพื่อจัดการระบบเพิ่มเติม",
    "System Executables — คำสั่งสำหรับผู้ดูแลระบบระดับสูงเพื่อจัดการระบบเพิ่มเติม"
).replace(
    "Media (จุดเชื่อมอุปกรณ์พกพา) - โฟลเดอร์เมาท์สำหรับอุปกรณ์จัดเก็บข้อมูลแบบถอดเสียบภายนอก เช่น CD-ROM",
    "Media — โฟลเดอร์เมาท์สำหรับอุปกรณ์จัดเก็บข้อมูลแบบถอดเสียบภายนอก เช่น CD-ROM"
).replace(
    "Variable (ข้อมูลผันแปรระบบ) - แหล่งเก็บข้อมูลที่มีการเปลี่ยนแปลงบ่อย เช่น ล็อกไฟล์ (Log) หรือระบบคิวเมล",
    "Variable — แหล่งเก็บข้อมูลที่มีการเปลี่ยนแปลงบ่อย เช่น ล็อกไฟล์ (Log) หรือระบบคิวเมล"
).replace(
    "Cache (พื้นที่เก็บแคช) - แหล่งเก็บข้อมูลแคชของแอปพลิเคชัน เพื่อให้เรียกใช้งานได้รวดเร็วยิ่งขึ้น",
    "Cache — แหล่งเก็บข้อมูลแคชของแอปพลิเคชัน เพื่อให้เรียกใช้งานได้รวดเร็วยิ่งขึ้น"
).replace(
    "Log files (ไฟล์ประวัติการทำงาน) - ไฟล์บันทึกการทำงาน เหตุการณ์ และประวัติของกิจกรรมต่างๆ ในระบบ",
    "Log files — ไฟล์บันทึกการทำงาน เหตุการณ์ และประวัติของกิจกรรมต่างๆ ในระบบ"
).replace(
    "Spool (คิวพักข้อมูล) - พื้นที่พักรอการประมวลผลของงาน เช่น คิวพิมพ์เอกสาร หรืออีเมลรอส่งออก",
    "Spool — พื้นที่พักรอการประมวลผลของงาน เช่น คิวพิมพ์เอกสาร หรืออีเมลรอส่งออก"
).replace(
    "Temporary (ไฟล์ชั่วคราวข้ามการบูต) - แหล่งเก็บไฟล์ชั่วคราวของโปรแกรมที่จะไม่โดนลบไปเมื่อรีบูตเครื่องใหม่",
    "Temporary — แหล่งเก็บไฟล์ชั่วคราวของโปรแกรมที่จะไม่โดนลบไปเมื่อรีบูตเครื่องใหม่"
).replace(
    "Mount (จุดเชื่อมระบบไฟล์ชั่วคราว) - ใช้สำหรับเมาท์และเข้าถึงระบบไฟล์ภายนอกอื่นชั่วคราวเพื่อคัดลอกหรือจัดการข้อมูล",
    "Mount — ใช้สำหรับเมาท์และเข้าถึงระบบไฟล์ภายนอกอื่นชั่วคราวเพื่อคัดลอกหรือจัดการข้อมูล"
)

# 3. Update Block 13 (5 Flat-Tree Sub-trees)
blocks[13]['value'] = blocks[13]['value'].replace(
    "First IDE HDD (ฮาร์ดดิสก์ IDE ตัวแรก)", "First IDE HDD"
).replace(
    "CD-ROM / Pseudo-device (ไดรฟ์ซีดี / อุปกรณ์จำลอง)", "CD-ROM / Pseudo-device"
).replace(
    "Linux Kernel (ไฟล์แกนหลักระบบ)", "Linux Kernel"
).replace(
    "Bash defaults (ตั้งค่า Bash ทั่วระบบ)", "Bash defaults"
).replace(
    "Crontab script (ตารางงานอัตโนมัติ)", "Crontab script"
).replace(
    "Network filesystem (แชร์ระบบไฟล์เครือข่าย)", "Network filesystem"
).replace(
    "User Groups (กลุ่มผู้ใช้งาน)", "User Groups"
).replace(
    "IP Mappings (แผนผังเครื่อง)", "IP Mappings"
).replace(
    "Hosts allowed (โฮสต์ที่อนุญาต)", "Hosts allowed"
).replace(
    "Hosts denied (โฮสต์ที่บล็อก)", "Hosts denied"
).replace(
    "Pre-login message (เตือนก่อนล็อกอิน)", "Pre-login message"
).replace(
    "Message of the day (ข่าวสารประจำวัน)", "Message of the day"
).replace(
    "User accounts (ข้อมูลผู้ใช้)", "User accounts"
).replace(
    "Encrypted passwords (รหัสผ่านที่เข้ารหัส)", "Encrypted passwords"
).replace(
    "Skel folder (ต้นแบบโฮม)", "Skel folder"
).replace(
    "Service scripts (สคริปต์เปิดบริการ)", "Service scripts"
).replace(
    "Startup scripts (คำสั่งรันระบบ)", "Startup scripts"
).replace(
    "Security configurations (ความปลอดภัย)", "Security configurations"
).replace(
    "GUI configs (หน้าต่างกราฟิก)", "GUI configs"
).replace(
    "User Executables (โปรแกรมใช้ทั่วไป)", "User Executables"
).replace(
    "C Header files (ไฟล์ส่วนหัวภาษา C)", "C Header files"
).replace(
    "User Libraries (ไลบรารีระบบทั่วไป)", "User Libraries"
).replace(
    "Admin Executables (คำสั่งควบคุมระบบ)", "Admin Executables"
).replace(
    "Shareable text (คู่มือเอกสารระบบ)", "Shareable text"
).replace(
    "Global System messages (ประวัติล็อกไฟล์รวม)", "Global System messages"
).replace(
    "User last login (ล็อกอินล่าสุด)", "User last login"
).replace(
    "Email log (ล็อกประวัติระบบอีเมล)", "Email log"
).replace(
    "Web Access Log (ล็อกประวัติเว็บเซิร์ฟเวอร์)", "Web Access Log"
).replace(
    "User accounts history (ประวัติบัญชี)", "User accounts history"
).replace(
    "Login/logout history (ประวัติเวลาเข้างาน)", "Login/logout history"
).replace(
    "Desktop folder (หน้าจอหลัก)", "Desktop folder"
).replace(
    "Documents folder (เอกสารส่วนตัว)", "Documents folder"
).replace(
    "Downloads folder (ไฟล์ดาวน์โหลด)", "Downloads folder"
).replace(
    "Music folder (ไฟล์เพลง)", "Music folder"
).replace(
    "Pictures folder (รูปภาพ)", "Pictures folder"
).replace(
    "Public sharing folder (แชร์ไฟล์สาธารณะ)", "Public sharing folder"
).replace(
    "Videos folder (วิดีโอ)", "Videos folder"
).replace(
    "Bash Config (ตั้งค่าสคริปต์ Bash)", "Bash Config"
).replace(
    "User cache (ไฟล์แคช)", "User cache"
).replace(
    "Terminal history (ประวัติรันคำสั่ง)", "Terminal history"
).replace(
    "User Profile (ตั้งสภาพแวดล้อมแรกเริ่ม)", "User Profile"
).replace(
    "Zsh shell config (คอนฟิก Zsh)", "Zsh shell config"
)

# Save and Commit
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
db.session.commit()

print("Lesson 165 updated successfully: English technical terms remain untranslated, followed by Thai explanations!")
