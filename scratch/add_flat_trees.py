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

# The HTML code for flat tree blueprints (completely flat, 0-indentation)
html_flat_trees = """<style>
.mini-tree-wrapper{margin:2.5rem 0;width:100%;max-width:820px;background:rgba(15,17,26,0.4);border:1px solid rgba(255,255,255,0.05);border-radius:12px;padding:24px;box-shadow:inset 0 0 20px rgba(0,0,0,0.3);}
.mini-tree-title{font-size:1.15rem;font-weight:700;color:#fbbf24;margin-bottom:20px;display:flex;align-items:center;gap:8px;text-shadow:0 0 10px rgba(251,191,36,0.15);}
.mt-flat-tree{display:flex;align-items:center;width:100%;position:relative;padding:10px 0;}
.mt-root-box{margin-right:40px;position:relative;z-index:2;display:flex;flex-direction:column;align-items:center;}
.mt-root-box::after{content:'';position:absolute;top:50%;right:-40px;width:40px;height:2px;background:rgba(255,255,255,0.15);z-index:1;transform:translateY(-50%);}
.mt-children-grid{display:flex;flex-direction:column;gap:12px;position:relative;padding-left:20px;border-left:2px solid rgba(255,255,255,0.15);z-index:2;width:100%;}
.mt-item-row{display:flex;align-items:center;width:100%;position:relative;}
.mt-item-row::before{content:'';position:absolute;top:50%;left:-20px;width:20px;height:2px;background:rgba(255,255,255,0.15);z-index:1;transform:translateY(-50%);}
.mt-card{font-size:0.8rem;padding:6px 12px;border-radius:6px;text-align:center;font-weight:700;white-space:nowrap;width:auto;min-width:90px;}
.mt-card.type-root{border:1px solid #fbbf24;background:rgba(251,191,36,0.05);color:#fbbf24;box-shadow:0 0 10px rgba(251,191,36,0.15);min-width:70px;}
.mt-card.type-blue{border:1px solid #00c0ff;background:rgba(0,192,255,0.03);color:#00c0ff;}
.mt-card.type-green{border:1px solid #3ddc84;background:rgba(61,220,132,0.02);color:#3ddc84;}
.mt-leader-line{flex:1;height:1px;border-bottom:1px dashed rgba(255,255,255,0.12);margin:0 16px;min-width:20px;}
.mt-desc-text{font-size:0.85rem;color:#94a3b8;line-height:1.5;max-width:500px;text-align:left;}
.mt-desc-text span.highlight{color:#ffffff;font-weight:600;}
@media (max-width:768px){
.mt-desc-text{max-width:300px;}
}
</style>

<div class="mini-tree-wrapper">
<div class="mini-tree-title"><i class="fas fa-microchip"></i> 1. /dev/ (Device Files & Kernel)</div>
<div class="mt-flat-tree">
<div class="mt-root-box">
<div class="mt-card type-root">/dev/</div>
</div>
<div class="mt-children-grid">
<div class="mt-item-row">
<div class="mt-card type-blue">hda</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">First IDE HDD</span> (ฮาร์ดดิสก์ IDE ตัวแรก) — ไฟล์เชื่อมโยงและพาร์ทิชันของฮาร์ดดิสก์หลักตัวแรกในระบบ</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">hdc</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">CD-ROM / Pseudo-device</span> (ไดรฟ์ซีดี / อุปกรณ์จำลอง) — ไฟล์เชื่อมต่อไดรฟ์ CD-ROM หรือช่องส่งทิ้งข้อมูลระบบ</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-green">/boot/vmlinux</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Linux Kernel</span> (ไฟล์แกนหลักระบบ) — ไฟล์แกนควบคุมการทำงานหลักทั้งหมดของระบบปฏิบัติการ Linux</div>
</div>
</div>
</div>
</div>

<div class="mini-tree-wrapper">
<div class="mini-tree-title"><i class="fas fa-cogs"></i> 2. /etc/ (System Configurations)</div>
<div class="mt-flat-tree">
<div class="mt-root-box">
<div class="mt-card type-root">/etc/</div>
</div>
<div class="mt-children-grid">
<div class="mt-item-row">
<div class="mt-card type-blue">bashrc</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Bash defaults</span> (ตั้งค่า Bash ทั่วระบบ) — ไฟล์กำหนดค่าเริ่มต้นและคีย์ลัดคำสั่งย่อสำหรับผู้ใช้ทุกคน</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">crontab</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Crontab script</span> (ตารางงานอัตโนมัติ) — ไฟล์สคริปต์ตั้งเวลารันงานและรันโปรแกรมระบบแบบอัตโนมัติ</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">exports</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Network filesystem</span> (แชร์ระบบไฟล์เครือข่าย) — ไฟล์เก็บสิทธิ์และเส้นทางของระบบไฟล์ที่เปิดให้เครื่องอื่นเข้าแชร์</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">group</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">User Groups</span> (กลุ่มผู้ใช้งาน) — ไฟล์ระบุกลุ่มความปลอดภัยหลักและกลุ่มสิทธิ์สมาชิกในระบบคอมพิวเตอร์</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">hosts</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">IP Mappings</span> (แผนผังเครื่อง) — ไฟล์แผนผังเชื่อมโยงหมายเลข IP Address กับชื่อเครื่องคอมพิวเตอร์ในระบบ</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">hosts.allow</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Hosts allowed</span> (โฮสต์ที่อนุญาต) — รายชื่อคอมพิวเตอร์ภายนอกที่ได้รับอนุญาตให้เชื่อมต่อเข้าใช้งานระบบ</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">host.deny</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Hosts denied</span> (โฮสต์ที่บล็อก) — รายชื่อคอมพิวเตอร์ภายนอกที่ถูกระงับสิทธิ์ไม่ให้เชื่อมต่อระบบ</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">issue</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Pre-login message</span> (เตือนก่อนล็อกอิน) — ข้อความแสดงข่าวสารหรือแจ้งสิทธิ์ที่แสดงก่อนหน้าล็อกอิน</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">motd</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Message of the day</span> (ข่าวสารประจำวัน) — ประกาศระบบที่จะแสดงผลขึ้นมาทันทีหลังล็อกอินสำเร็จ</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">passwd</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">User accounts</span> (ข้อมูลผู้ใช้) — รายชื่อบัญชีผู้ใช้งาน สิทธิ์การเข้าถึง และไดเรกทอรีบ้านของทุกคน</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">shadow</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Encrypted passwords</span> (รหัสผ่านที่เข้ารหัส) — ไฟล์เก็บรหัสผ่านจริงของผู้ใช้ในรูปแบบที่เข้ารหัสลับไว้</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">skel/</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Skel folder</span> (ต้นแบบโฮม) — โฟลเดอร์ต้นแบบที่จะคัดลอกไฟล์ตั้งต้นให้เมื่อสร้างผู้ใช้ใหม่</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">init.d/</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Service scripts</span> (สคริปต์เปิดบริการ) — สคริปต์ควบคุมการเปิดและปิดบริการระบบต่างๆ (Services)</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">rc.d/</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Startup scripts</span> (คำสั่งรันระบบ) — สคริปต์ควบคุมการเริ่มหรือหยุดฟังก์ชันการทำงานหลักของระบบปฏิบัติการ</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">security/</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Security configurations</span> (ความปลอดภัย) — ไฟล์ตั้งค่าจำกัดการล็อกอิน กฎและข้อจำกัดการเข้าใช้ระบบ</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">X11/</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">GUI configs</span> (หน้าต่างกราฟิก) — ไฟล์กำหนดค่าการแสดงผลแบบอินเตอร์เฟซกราฟิก (GUI/X11) ของหน้าจอ</div>
</div>
</div>
</div>
</div>

<div class="mini-tree-wrapper">
<div class="mini-tree-title"><i class="fas fa-folder-open"></i> 3. /usr/ (User Executables & Files)</div>
<div class="mt-flat-tree">
<div class="mt-root-box">
<div class="mt-card type-root">/usr/</div>
</div>
<div class="mt-children-grid">
<div class="mt-item-row">
<div class="mt-card type-blue">bin/</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">User Executables</span> (โปรแกรมใช้ทั่วไป) — ไฟล์คำสั่งโปรแกรมใช้งานทั่วไปเสริมที่ผู้ใช้ทุกคนรันได้</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">include/</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">C Header files</span> (ไฟล์ส่วนหัวภาษา C) — แฟ้มเก็บไฟล์ Header (.h) มาตรฐานสำหรับเขียนภาษา C/C++</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">lib/</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">User Libraries</span> (ไลบรารีระบบทั่วไป) — ไฟล์ไลบรารีระบบสนับสนุนแอปพลิเคชันต่างๆ ในโฟลเดอร์ /usr</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">sbin/</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Admin Executables</span> (คำสั่งควบคุมระบบ) — คำสั่งควบคุมระบบเพิ่มเติมพิเศษเฉพาะให้สิทธิ์ Admin เรียกใช้</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-green">share/</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Shareable text</span> (คู่มือเอกสารระบบ) — เอกสารช่วยเหลือระบบ คู่มือคำสั่งอ้างอิง และคู่มือการใช้งาน (man pages)</div>
</div>
</div>
</div>
</div>

<div class="mini-tree-wrapper">
<div class="mini-tree-title"><i class="fas fa-file-alt"></i> 4. /var/log/ (System Logs)</div>
<div class="mt-flat-tree">
<div class="mt-root-box">
<div class="mt-card type-root">/var/log/</div>
</div>
<div class="mt-children-grid">
<div class="mt-item-row">
<div class="mt-card type-blue">messages</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Global System messages</span> (ประวัติล็อกไฟล์รวม) — ล็อกกิจกรรมรวม ปัญหาระบบ และข้อผิดพลาดของระบบปฏิบัติการ</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">lastlog</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">User last login</span> (ล็อกอินล่าสุด) — ประวัติและสถิติล็อกอินเข้าระบบหลังสุดแยกเป็นรายบัญชีผู้ใช้</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">maillog</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Email log</span> (ล็อกประวัติระบบอีเมล) — บันทึกการส่ง-รับและความเคลื่อนไหวของจดหมายระบบเซิร์ฟเวอร์อีเมล</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-green">httpd-access.log</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Web Access Log</span> (ล็อกประวัติเว็บเซิร์ฟเวอร์) — ล็อกประวัติการเข้าชมและการร้องขอไฟล์ของเว็บเซิร์ฟเวอร์ (Apache/HTTPD)</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-green">userlog</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">User accounts history</span> (ประวัติบัญชี) — ไฟล์บันทึกประวัติเหตุการณ์เกี่ยวกับการสร้างหรือลบบัญชีผู้ใช้งานระบบ</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-green">wtmp</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Login/logout history</span> (ประวัติเวลาเข้างาน) — รายละเอียดเวลาและช่วงเข้า-ออกระบบของผู้ใช้เก็บแบบถาวร</div>
</div>
</div>
</div>
</div>

<div class="mini-tree-wrapper">
<div class="mini-tree-title"><i class="fas fa-home"></i> 5. ~ /home/ (User Home & Configurations)</div>
<div class="mt-flat-tree">
<div class="mt-root-box">
<div class="mt-card type-root">~/ (home)</div>
</div>
<div class="mt-children-grid">
<div class="mt-item-row">
<div class="mt-card type-blue">Desktop/</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Desktop folder</span> (หน้าจอหลัก) — โฟลเดอร์เก็บแอปพลิเคชัน คีย์ลัด และไฟล์บนหน้าจอหน้าเดสก์ท็อปผู้ใช้</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">Documents/</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Documents folder</span> (เอกสารส่วนตัว) — แหล่งจัดเก็บเอกสาร ข้อมูลบันทึกส่วนบุคคลของบัญชีผู้ใช้</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">Downloads/</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Downloads folder</span> (ไฟล์ดาวน์โหลด) — โฟลเดอร์เก็บไฟล์และตัวติดตั้งแอปที่รับเข้าผ่านระบบอินเทอร์เน็ต</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">Music/</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Music folder</span> (ไฟล์เพลง) — โฟลเดอร์เก็บไฟล์เสียงและเพลงส่วนตัวของผู้ใช้งาน</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">Pictures/</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Pictures folder</span> (รูปภาพ) — โฟลเดอร์เก็บรูปภาพ สื่อภาพนิ่ง และภาพถ่ายต่างๆ ของผู้ใช้งาน</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">Public/</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Public sharing folder</span> (แชร์ไฟล์สาธารณะ) — แฟ้มเป้าหมายสำหรับเปิดให้บัญชีเครื่องอื่นมาร่วมใช้ร่วมแชร์ในวงแลน</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-blue">Videos/</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Videos folder</span> (วิดีโอ) — โฟลเดอร์บันทึกไฟล์ภาพเคลื่อนไหว คลิปวิดีโอ และภาพยนตร์ส่วนตัว</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-green">.bashrc</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Bash Config</span> (ตั้งค่าสคริปต์ Bash) — สคริปต์ตั้งค่าสภาพแวดล้อม คีย์ลัดคำสั่งย่อ เฉพาะตัวผู้ใช้งานบน Bash Shell</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-green">.cache/</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">User cache</span> (ไฟล์แคช) — โฟลเดอร์จัดเก็บข้อมูลแคชสำหรับแอปส่วนตัวผู้ใช้เพื่อเพิ่มความเร็วประมวลผล</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-green">.history</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Terminal history</span> (ประวัติรันคำสั่ง) — บันทึกประวัติประมวลผลรันคำสั่งย้อนหลังทั้งหมดที่เคยคีย์ลงเชลล์</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-green">.profile</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">User Profile</span> (ตั้งสภาพแวดล้อมแรกเริ่ม) — ไฟล์รันสิ่งแวดล้อมส่วนตัวของบัญชีผู้ใช้เมื่อล็อกอินเชื่อมเข้าระบบ</div>
</div>
<div class="mt-item-row">
<div class="mt-card type-green">.zshrc</div>
<div class="mt-leader-line"></div>
<div class="mt-desc-text"><span class="highlight">Zsh shell config</span> (คอนฟิก Zsh) — กำหนดรูปแบบการทำงานและคำสั่งย่อเฉพาะตัวสำหรับผู้ใช้ Zsh shell</div>
</div>
</div>
</div>
</div>
"""

# Set the HTML flat trees into block 23
blocks[23]['value'] = "### 📂 Linux Important Files & Sub-Trees Map\n\nแผนภาพจำลองกิ่งก้านโครงสร้างระบบไฟล์และไฟล์การตั้งค่าสำคัญต่างๆ ของ Linux แยกตามโฟลเดอร์หลักอย่างเป็นระบบ แสดงคีย์เวิร์ดและคำอธิบายภาษาไทยกึ่งอังกฤษถัดจากกิ่งไฟล์ทันทีเพื่อให้อ่านเปรียบเทียบความสัมพันธ์ได้โดยสะดวก:\n\n" + html_flat_trees

# Save and Commit
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
db.session.commit()
print("All sub-trees updated to flat blueprint layout successfully!")
