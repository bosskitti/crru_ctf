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

# Assemble the combined table markdown
combined_markdown = """### 📂 Important Files and Directories in Linux

ระบบ Linux จะจัดเก็บไฟล์ตั้งค่า คอนฟิกูเรชัน ไฟล์ไบนารีระบบ ล็อกบันทึกเหตุการณ์ และประวัติต่างๆ ไว้ในไฟล์เฉพาะตัวที่สำคัญ ตารางด้านล่างนี้ได้รวบรวมไฟล์และไดเรกทอรีที่สำคัญที่สุดเพื่อใช้ในการอ้างอิงและตรวจสอบระบบ:

| Path (พาธไฟล์) | Category (หมวดหมู่) | Description (คำอธิบายแบบกึ่งไทยอังกฤษ) |
|---|---|---|
| `/boot/vmlinux` | Kernel (แกนหลัก) | the kernel file / ไฟล์แกนหลักและหัวใจควบคุมระบบปฏิบัติการ (Linux Kernel) |
| `/dev/hda` | Devices (อุปกรณ์) | first IDE HDD / ไฟล์เชื่อมต่อและตำแหน่งฮาร์ดดิสก์ IDE ตัวแรกของระบบ |
| `/dev/hdc` | Devices (อุปกรณ์) | CD-ROM or pseudo-device / อุปกรณ์จำลองสำหรับทิ้งข้อมูลขยะ หรือไฟล์ไดรฟ์ CD-ROM |
| `/etc/bashrc` | Configuration (ตั้งค่าระบบ) | system defaults and aliases / ไฟล์กำหนดค่าเริ่มต้นและชื่อย่อคำสั่งของ Bash Shell สำหรับผู้ใช้ทุกคน |
| `/etc/crontab` | Configuration (ตั้งค่าระบบ) | crontab script / ไฟล์สคริปต์หลักสำหรับตั้งเวลาเรียกใช้งานโปรแกรมอัตโนมัติตามกำหนด |
| `/etc/exports` | Configuration (ตั้งค่าระบบ) | network filesystem info / ข้อมูลระบบไฟล์แชร์และสิทธิ์การเข้าถึงอุปกรณ์ข้อมูลบนเครือข่าย |
| `/etc/group` | Configuration (ตั้งค่าระบบ) | security group definitions / ไฟล์นิยามกลุ่มความปลอดภัยและกลุ่มผู้ใช้งานภายในระบบ |
| `/etc/init.d` | Configuration (ตั้งค่าระบบ) | service startup script / โฟลเดอร์สคริปต์รันระบบเมื่อเริ่มเปิดเครื่อง (Services Startup) |
| `/etc/hosts` | Configuration (ตั้งค่าระบบ) | IP and hostnames mappings / ไฟล์เก็บแผนผังหมายเลข IP Address กับชื่อเครื่องคอมพิวเตอร์ |
| `/etc/hosts.allow` | Configuration (ตั้งค่าระบบ) | hosts allowed access / รายชื่อเครื่องโฮสต์ที่ได้รับอนุญาตให้เชื่อมต่อเข้าบริการระบบ |
| `/etc/host.deny` | Configuration (ตั้งค่าระบบ) | hosts denied access / รายชื่อเครื่องโฮสต์ที่ถูกบล็อกไม่ให้เชื่อมต่อเข้าใช้บริการระบบ |
| `/etc/issue` | Configuration (ตั้งค่าระบบ) | pre-login message / ข้อความแจ้งข่าวสารหรือต้อนรับที่แสดงผลก่อนเข้าสู่ระบบล็อกอิน |
| `/etc/motd` | Configuration (ตั้งค่าระบบ) | message of the day / ข้อความต้อนรับและประกาศสั้นหลังล็อกอินเข้าระบบสำเร็จ |
| `/etc/passwd` | Configuration (ตั้งค่าระบบ) | system user accounts / รายชื่อบัญชีผู้ใช้ ข้อมูลระบบ รหัสผ่าน และสิทธิ์พื้นฐานในระบบ |
| `/etc/printcap` | Configuration (ตั้งค่าระบบ) | printer configurations / ไฟล์เก็บรายละเอียดคอนฟิกและเครื่องพิมพ์ที่ต่อเชื่อมใช้งาน |
| `/etc/profile` | Configuration (ตั้งค่าระบบ) | bash shell defaults / ไฟล์ตั้งค่าสภาพแวดล้อมตั้งต้นสำหรับผู้ใช้ Bash Shell ทุกคนตอนล็อกอิน |
| `/etc/profile.d` | Configuration (ตั้งค่าระบบ) | post-login scripts / โฟลเดอร์เก็บสคริปต์ย่อยที่จะทำงานอัตโนมัติทันทีหลังผู้ใช้ล็อกอินสำเร็จ |
| `/etc/re.conf` | Configuration (ตั้งค่าระบบ) | interface/service configurations / ไฟล์กำหนดค่าการทำงานของอินเตอร์เฟซและบริการระบบ |
| `/etc/rc.d` | Configuration (ตั้งค่าระบบ) | startup/shutdown control / สคริปต์ควบคุมการรัน หยุด หรือเริ่มใหม่ของฟังก์ชันการทำงานระบบ |
| `/etc/rc.d/init.d` | Configuration (ตั้งค่าระบบ) | initialization scripts / โฟลเดอร์เก็บไฟล์ตั้งค่าเริ่มต้นโปรแกรมระบบขณะบูตเครื่อง |
| `/etc/security` | Configuration (ตั้งค่าระบบ) | security terminal settings / ข้อกำหนดความปลอดภัยที่ตั้งให้สิทธิ์ root สามารถล็อกอินเข้าใช้เครื่องได้ |
| `/etc/shadow` | Configuration (ตั้งค่าระบบ) | encrypted passwords / ไฟล์เก็บรหัสผ่านของผู้ใช้งานทั้งหมดในรูปแบบที่เข้ารหัสลับเพื่อความปลอดภัย |
| `/etc/skel` | Configuration (ตั้งค่าระบบ) | new user home template / โฟลเดอร์ต้นแบบสำหรับสร้างไฟล์ตั้งต้นให้โฟลเดอร์โฮมเมื่อมีผู้ใช้งานใหม่ |
| `/etc/X11` | Configuration (ตั้งค่าระบบ) | X-window configurations / แหล่งรวมไฟล์ตั้งค่าสำหรับการแสดงผลในระบบกราฟิก (GUI) ของ X11 |
| `/usr/bin` | User Files (ไฟล์ผู้ใช้งาน) | user executable files / แหล่งรวมไฟล์โปรแกรมคำสั่งใช้งานทั่วไปที่ผู้ใช้ทุกคนสามารถรันได้ |
| `/usr/include` | User Files (ไฟล์ผู้ใช้งาน) | C header files / ไฟล์ส่วนหัวมาตรฐาน (.h) สำหรับการแปลงและเขียนโปรแกรมภาษา C |
| `/usr/share` | User Files (ไฟล์ผู้ใช้งาน) | shareable text files / ไฟล์เอกสาร คู่มือช่วยเหลือการใช้คำสั่ง และไฟล์ที่ใช้แชร์ข้ามระบบ |
| `/usr/lib` | User Files (ไฟล์ผู้ใช้งาน) | object files and libraries / ไฟล์รันระบบของโปรแกรมและไลบรารีต่างๆ ที่โปรแกรมทั่วไปเรียกใช้ |
| `/usr/sbin` | User Files (ไฟล์ผู้ใช้งาน) | admin commands / ไฟล์คำสั่งควบคุมระบบขั้นสูงสำหรับผู้ใช้ระดับผู้ดูแลระบบหลัก |
| `/var/log/httpd-access.log` | System Logs (ล็อกไฟล์) | web access information / ล็อกประวัติการเข้าชมและสถิติการร้องขอไฟล์ในระบบเว็บเซิร์ฟเวอร์ |
| `/var/log/lastlog` | System Logs (ล็อกไฟล์) | user last login / รายละเอียดและประวัติการล็อกอินเข้าระบบครั้งล่าสุดของผู้ใช้งานแต่ละราย |
| `/var/log/maillog` | System Logs (ล็อกไฟล์) | email usage log / ไฟล์บันทึกประวัติการส่ง-รับข้อมูลในระบบบริการจดหมายอีเมล |
| `/var/log/messages` | System Logs (ล็อกไฟล์) | global system messages / ล็อกระบบทั่วไปที่เก็บบันทึกประวัติและข้อผิดพลาดสำคัญของระบบปฏิบัติการ |
| `/var/log/userlog` | System Logs (ล็อกไฟล์) | user history log / ไฟล์บันทึกประวัติความเคลื่อนไหวเกี่ยวกับการสร้างและลบบัญชีผู้ใช้ |
| `/var/log/wtmp` | System Logs (ล็อกไฟล์) | login/logout history / ประวัติการเข้างานและออกงานของระบบ พร้อมช่วงเวลาใช้งานแบบถาวร |
| `~/.bashrc` | Home Config (โฮมและโปรไฟล์) | user bash settings / ไฟล์กำหนดค่าเริ่มต้นและคีย์ลัดคำสั่งเฉพาะตัวสำหรับผู้ใช้ Bash Shell |
| `~/.cache` | Home Config (โฮมและโปรไฟล์) | user cache files / โฟลเดอร์เก็บข้อมูลแคชสำหรับแอปพลิเคชันส่วนตัวเพื่อความรวดเร็ว |
| `~/.dmrc` | Home Config (โฮมและโปรไฟล์) | session initialization / ไฟล์เก็บบันทึกประเภทเดสก์ท็อปและค่าเริ่มต้นที่เลือกใช้ตอนล็อกอิน |
| `~/.history` | Home Config (โฮมและโปรไฟล์) | command history list / ไฟล์บันทึกประวัติคำสั่งต่างๆ ที่เคยพิมพ์ในเทอร์มินัลย้อนหลัง |
| `~/.local/share/Trash` | Home Config (โฮมและโปรไฟล์) | trash directory / โฟลเดอร์ถังขยะส่วนตัวสำหรับเก็บไฟล์และข้อมูลที่กดลบชั่วคราว |
| `~/.profile` | Home Config (โฮมและโปรไฟล์) | user profile settings / ไฟล์ตั้งค่าสภาพแวดล้อมเฉพาะบัญชีผู้ใช้เมื่อล็อกอินเข้าสู่ระบบ |
| `~/.zshrc` | Home Config (โฮมและโปรไฟล์) | user zsh settings / ไฟล์ตั้งค่าการเริ่มต้นโปรแกรม คอนฟิก และคำสั่งย่อสำหรับ Zsh Shell |
| `~/Desktop` | Home Config (โฮมและโปรไฟล์) | desktop folder / โฟลเดอร์จัดเก็บสิ่งต่างๆ บนหน้าจอเดสก์ท็อปของผู้ใช้งาน |
| `~/Documents` | Home Config (โฮมและโปรไฟล์) | documents folder / โฟลเดอร์สำหรับจัดเก็บเอกสารและไฟล์ข้อมูลส่วนบุคคล |
| `~/Downloads` | Home Config (โฮมและโปรไฟล์) | downloads folder / โฟลเดอร์จัดเก็บไฟล์และแอปพลิเคชันที่ดาวน์โหลดจากอินเทอร์เน็ต |
| `~/Music` | Home Config (โฮมและโปรไฟล์) | music folder / โฟลเดอร์สำหรับจัดเก็บไฟล์เสียงและเพลงของผู้ใช้งาน |
| `~/Pictures` | Home Config (โฮมและโปรไฟล์) | pictures folder / โฟลเดอร์สำหรับจัดเก็บรูปภาพและสื่อทางภาพต่างๆ |
| `~/Public` | Home Config (โฮมและโปรไฟล์) | public sharing folder / โฟลเดอร์เปิดแชร์ไฟล์สำหรับเครือข่ายและเครื่องอื่นๆ ในระบบ |
| `~/Videos` | Home Config (โฮมและโปรไฟล์) | videos folder / โฟลเดอร์สำหรับจัดเก็บไฟล์วิดีโอและภาพยนตร์ |
"""

# Set the combined markdown table into block 23
blocks[23]['value'] = combined_markdown

# Clear blocks 24 to 37 (empty values)
for i in range(24, 38):
    blocks[i]['value'] = ""

# Save and Commit
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
db.session.commit()
print("All fragmented important file tables consolidated into a single comprehensive table successfully!")
