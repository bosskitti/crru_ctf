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

# Define bilingual table replacements
bilingual_tables = {
    11: """### 📂 Linux Directory Structure

- The base of the Linux file system hierarchy begins at the root and everything starts with the root directory

- The path is the route that starts from the root to the destination files or directories such as `/home/wongyos/rpca/data.txt`

- These are the special directories in Linux system:

| Directory | Description |
|---|---|
| `/` | root directory / ไดเรกทอรีราก (จุดเริ่มต้นและรากฐานของระบบไฟล์ทั้งหมด) |
| `.` | current directory / ไดเรกทอรีปัจจุบันที่กำลังทำงานอยู่ |
| `..` | parent directory / ไดเรกทอรีแม่ (ลำดับชั้นที่เหนือกว่า) ของไดเรกทอรีปัจจุบัน |""",

    13: """### 📂 Linux Directory Structure (Cont)

- These are the common top-level directories associated with the root directory:

| Directory | Description |
|---|---|
| `/bin` | binary directory / ไดเรกทอรีเก็บไฟล์คำสั่งและโปรแกรมพื้นฐานสำหรับผู้ใช้ทุกคน |
| `/etc` | etcetera directory / ไดเรกทอรีเก็บไฟล์คอนฟิกและการตั้งค่าของระบบทั้งหมด |
| `/home` | home directory / ไดเรกทอรีบ้านสำหรับเก็บข้อมูลส่วนตัวของผู้ใช้งานทั่วไป |
| `/opt` | optional directory / ไดเรกทอรีสำหรับติดตั้งซอฟต์แวร์เสริมภายนอกและโปรแกรมบุคคลที่สาม |""",

    15: """### 📂 Linux Directory Structure (Cont)

| Directory | Description |
|---|---|
| `/tmp` | temporary directory / ไดเรกทอรีเก็บไฟล์ชั่วคราว (จะถูกล้างข้อมูลอัตโนมัติเมื่อเริ่มระบบใหม่) |
| `/usr` | user directory / เก็บโปรแกรมและไฟล์ขนาดใหญ่สำหรับผู้ใช้ทั่วไป (อ่านได้เฉพาะตัวและแชร์กันได้) |
| `/var` | variable directory / เก็บไฟล์ที่มีการเปลี่ยนแปลงบ่อย เช่น ล็อกไฟล์ (Log) คิวเมล หรือไฟล์พักข้อมูล |""",

    17: """### 📂 Linux Directory Structure (Cont)

- These are some other top-level directories in the Linux system:

| Directory | Description |
|---|---|
| `/boot` | boot loader directory / เก็บไฟล์และสารสนเทศระบบทั้งหมดสำหรับการเริ่มระบบ เช่น GRUB, Kernel |
| `/dev` | device directory / เก็บไฟล์ตำแหน่งอุปกรณ์เชื่อมต่อฮาร์ดแวร์ต่างๆ ในระบบ เช่น ฮาร์ดดิสก์ |
| `/lib` | library directory / เก็บไฟล์ไลบรารีระบบและเคอร์เนลโมดูลที่จำเป็นในการเริ่มเปิดระบบเครื่อง |""",

    19: """### 📂 Linux Directory Structure (Cont)

| Directory | Description |
|---|---|
| `/media` | media directory / จุดเชื่อมต่อสำหรับอุปกรณ์พกพาภายนอกแบบถอดเสียบ เช่น Flash Drive หรือ CD-ROM |
| `/mnt` | mount directory / จุดเชื่อมต่อหรือเมาท์ระบบไฟล์ภายนอกและอุปกรณ์ข้อมูลชั่วคราว |
| `/proc` | process directory / ไดเรกทอรีจำลองข้อมูลสถานะโปรเซสที่กำลังรันอยู่ (สร้างอัตโนมัติโดยระบบ) |""",

    21: """### 📂 Linux Directory Structure (Cont)

| Directory | Description |
|---|---|
| `/root` | root home directory / โฟลเดอร์บ้านและข้อมูลส่วนตัวของผู้ดูแลระบบหลัก (root) |
| `/run` | runtime directory / เก็บข้อมูลชั่วคราวระหว่างการทำงานของระบบ (Runtime Data) |
| `/sbin` | system binary directory / เก็บคำสั่งและโปรแกรมระบบที่จำเป็นเฉพาะของผู้ดูแลระบบคอมพิวเตอร์ |
| `/srv` | server directory / เก็บข้อมูลบริการบนระบบเซิร์ฟเวอร์ เช่น ไฟล์ข้อมูลเว็บไซต์ หรือข้อมูล FTP |
| `/sys` | system directory / เก็บข้อมูลอุปกรณ์จำลองและไดรเวอร์ของเคอร์เนลเพื่อการตั้งค่าระบบปฏิบัติการ |""",

    23: """### 📂 Important Files and Directories in Linux

- Linux system stores some well-defined configuration files, binaries, man pages information files such as kernel files, device files, log files, etc.

- **Kernel file:**

| Path | Description |
|---|---|
| `/boot/vmlinux` | the kernel file / ไฟล์แกนหลักและหัวใจควบคุมระบบปฏิบัติการ (Linux Kernel) |

- **Device files:**

| Path | Description |
|---|---|
| `/dev/hda` | first IDE HDD / ไฟล์เชื่อมต่อและตำแหน่งฮาร์ดดิสก์ IDE ตัวแรกของระบบ |
| `/dev/hdc` | pseudo-device or CD-ROM / อุปกรณ์จำลองสำหรับทิ้งข้อมูลขยะ หรือไฟล์ไดรฟ์ CD-ROM |""",

    25: """### 📂 Important Files and Directories in Linux (Cont)

- **System configuration files:**

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
| `/etc/motd` | message of the day / ข้อความต้อนรับประจำวันที่จะแสดงผลหลังผู้ใช้งานล็อกอินเข้าเครื่องสำเร็จ |
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

- **User related files:**

| Path | Description |
|---|---|
| `/usr/bin` | user executable files / แหล่งรวมไฟล์โปรแกรมคำสั่งประยุกต์ทั่วไปที่ผู้ใช้ทุกคนสามารถรันได้ |
| `/usr/include` | C header files / ไฟล์ส่วนหัวมาตรฐาน (.h) สำหรับการแปลงและเขียนโปรแกรมภาษา C |
| `/usr/share` | shareable text files / ไฟล์เอกสาร คู่มือช่วยเหลือการใช้คำสั่ง และไฟล์ที่ใช้แชร์ข้ามระบบ |
| `/usr/lib` | object files and libraries / ไฟล์รันระบบของโปรแกรมและไลบรารีต่างๆ ที่โปรแกรมทั่วไปเรียกใช้ |
| `/usr/sbin` | admin commands / ไฟล์คำสั่งควบคุมระบบขั้นสูงสำหรับผู้ใช้ระดับผู้ดูแลระบบหลัก |""",

    33: """### 📂 Important Files and Directories in Linux (Cont)

- **Log files:**

| Path | Description |
|---|---|
| `/var/log/httpd-access.log` | web access information / ล็อกประวัติการเข้าชมและสถิติการร้องขอไฟล์ในระบบเว็บเซิร์ฟเวอร์ |
| `/var/log/lastlog` | user last login / รายละเอียดและประวัติการล็อกอินเข้าระบบครั้งล่าสุดของผู้ใช้งานแต่ละราย |
| `/var/log/maillog` | email usage log / ไฟล์บันทึกประวัติการส่ง-รับข้อมูลในระบบบริการจดหมายอิเล็กทรอนิกส์ |
| `/var/log/messages` | global system messages / ล็อกระบบทั่วไปที่เก็บบันทึกประวัติและข้อผิดพลาดสำคัญของระบบปฏิบัติการ |
| `/var/log/userlog` | user history log / ไฟล์บันทึกประวัติความเคลื่อนไหวเกี่ยวกับการสร้างและลบบัญชีผู้ใช้ |
| `/var/log/wtmp` | login/logout history / ประวัติการเข้างานและออกงานของระบบ พร้อมช่วงเวลาใช้งานแบบถาวร |""",

    35: """### 📂 Important Files and Directories in Linux (Cont)

- **Home files and directories under `/home/$USER`:**

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
print("All tables in Lesson 2 upgraded to bilingual Thai/English format successfully!")
