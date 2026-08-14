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

current_blocks = json.loads(lesson.content)
print(f"Current blocks count: {len(current_blocks)}")

# Extract and preserve the last 2 interactive question blocks
question_blocks = [b for b in current_blocks if b.get('type') == 'question']
print(f"Preserved {len(question_blocks)} question blocks.")

# 1. Header block
header_md = """## 🗺️ โครงสร้างและสถาปัตยกรรมระบบ Linux (Linux Architecture & Directory)

**Chapter 02: Cybersecurity Operating Systems**

---"""

# 2. Slide 1: Linux
slide_1_md = """### 📌 Linux

**Operating Systems 2**"""

# 3. Slide 2: Overviews of Linux
slide_2_md = """### 📌 Overviews of Linux

- Linux is a family of open-source Unix-like operating systems based on the Linux kernel which first released on September 17, 1991, by **Linus Torvalds**
- Linux was written in C, assembly, and others
- **Tux the penguin** is the mascot of Linux
- Popular Linux distributions include Debian, Fedora, and Ubuntu, which itself consists of many different sub-distributions
- **Kali Linux** is a Debian-based Linux"""

# 4. Slide 3: Linux System Architecture (Side-by-side blueprint)
slide_3_md = """### 💻 Linux System Architecture

สถาปัตยกรรมระบบปฏิบัติการ Linux แบ่งการทำงานออกเป็นชั้นๆ อย่างเป็นระบบเพื่อแยกสิทธิ์หน้าที่และการเข้าถึงฮาร์ดแวร์อย่างปลอดภัย เลื่อนเมาส์ชี้ไปที่แต่ละชั้นสถาปัตยกรรมเพื่อเน้นข้อความเรืองแสงอธิบายความหมายกึ่งไทยอังกฤษและหน้าที่ด้านขวา:

<style>
.arch-grid-v3{margin:2.5rem 0;display:flex;flex-direction:column;align-items:center;width:100%;max-width:820px;background:rgba(15,17,26,0.4);border:1px solid rgba(255,255,255,0.05);border-radius:12px;padding:24px;box-shadow:inset 0 0 20px rgba(0,0,0,0.3);}
.arch-container-v3{display:flex;flex-direction:column;align-items:center;width:100%;}
.arch-row-v3{display:flex;align-items:center;width:100%;position:relative;transition:all 0.2s ease;cursor:pointer;}
.arch-card-wrapper-v3{min-width:200px;display:flex;justify-content:center;}
.arch-card-v3{width:180px;padding:12px 16px;border-radius:8px;text-align:center;font-weight:700;font-size:0.95rem;box-shadow:0 4px 15px rgba(0, 0, 0, 0.2);transition:all 0.25s ease;}
.arch-card-v3.layer-apps{border:1px solid #fbbf24;background:rgba(251, 191, 36, 0.05);color:#fbbf24;}
.arch-card-v3.layer-shells{border:1px solid #ab20fd;background:rgba(171, 32, 253, 0.05);color:#ab20fd;}
.arch-card-v3.layer-kernel{border:1px solid #ff007f;background:rgba(255, 0, 127, 0.05);color:#ff007f;}
.arch-card-v3.layer-hardware{border:1px solid #00f0ff;background:rgba(0, 240, 255, 0.05);color:#00f0ff;}

.arch-leader-v3{flex:1;height:1px;border-bottom:1px dashed rgba(255,255,255,0.12);margin:0 20px;min-width:20px;transition:border-color 0.2s ease;}
.arch-desc-v3{width:55%;font-size:0.88rem;color:#94a3b8;line-height:1.6;transition:all 0.2s ease;text-align:left;}
.arch-desc-v3 span.highlight{color:#a0aec0;font-weight:600;transition:all 0.2s ease;}

.arch-row-v3:hover .arch-card-v3{transform:scale(1.04);color:#ffffff;}
.arch-row-v3:hover .arch-card-v3.layer-apps{border-color:#fbbf24;box-shadow:0 0 15px rgba(251,191,36,0.35);background:rgba(251,191,36,0.1);}
.arch-row-v3:hover .arch-card-v3.layer-shells{border-color:#ab20fd;box-shadow:0 0 15px rgba(171,32,253,0.35);background:rgba(171,32,253,0.1);}
.arch-row-v3:hover .arch-card-v3.layer-kernel{border-color:#ff007f;box-shadow:0 0 15px rgba(255,0,127,0.35);background:rgba(255,0,127,0.1);}
.arch-row-v3:hover .arch-card-v3.layer-hardware{border-color:#00f0ff;box-shadow:0 0 15px rgba(0,240,255,0.35);background:rgba(0,240,255,0.1);}

.arch-row-v3:hover .arch-leader-v3{border-bottom-color:rgba(255,255,255,0.4);border-bottom-style:solid;}
.arch-row-v3:hover .arch-desc-v3{color:#ffffff;text-shadow:0 0 8px rgba(255,255,255,0.3);}
.arch-row-v3:hover .arch-desc-v3 span.highlight{color:#fbbf24;text-shadow:0 0 10px rgba(251,191,36,0.5);}

.arch-spine-v3{width:2px;height:12px;background:rgba(255,255,255,0.15);margin-right:auto;margin-left:99px;}
@media (max-width:768px){
.arch-desc-v3{width:45%;}
}
</style>

<div class="arch-grid-v3">
<div class="arch-container-v3">

<!-- Row 1: Apps -->
<div class="arch-row-v3">
<div class="arch-card-wrapper-v3"><div class="arch-card-v3 layer-apps">Applications / Utilities</div></div>
<div class="arch-leader-v3"></div>
<div class="arch-desc-v3"><span class="highlight">Applications & Utilities</span> (โปรแกรมประยุกต์และยูทิลิตี้) — Programs to do the user and specialized-level task โปรแกรมใช้งานเสริมระดับทั่วไปและระบบรักษาความปลอดภัย เช่น Web Browser, Text Editor, Compiler หรือ Security Tools</div>
</div>

<!-- Connector 1 -->
<div class="arch-spine-v3"></div>

<!-- Row 2: Shells -->
<div class="arch-row-v3">
<div class="arch-card-wrapper-v3"><div class="arch-card-v3 layer-shells">Shells</div></div>
<div class="arch-leader-v3"></div>
<div class="arch-desc-v3"><span class="highlight">Shells</span> (ตัวตีความคำสั่ง) — Interface which takes commands from user and executes kernel's functions อินเตอร์เฟซรับชุดคำสั่งผู้ใช้ไปสั่งระบบคอร์ มีทั้งแบบ Command-line shells (CLI) และ Graphical shells (GUI)</div>
</div>

<!-- Connector 2 -->
<div class="arch-spine-v3"></div>

<!-- Row 3: Kernel -->
<div class="arch-row-v3">
<div class="arch-card-wrapper-v3"><div class="arch-card-v3 layer-kernel">Kernel</div></div>
<div class="arch-leader-v3"></div>
<div class="arch-desc-v3"><span class="highlight">Kernel</span> (แกนกลางระบบปฏิบัติการ) — Core part of the OS, responsible for all the major activities of the Linux OS หัวใจหลักจัดการทรัพยากรส่วนกลาง ทั้งการเข้าถึงหน่วยความจำ CPU จัดการดิสก์ และควบคุมอุปกรณ์เชื่อมต่อ</div>
</div>

<!-- Connector 3 -->
<div class="arch-spine-v3"></div>

<!-- Row 4: Hardware -->
<div class="arch-row-v3">
<div class="arch-card-wrapper-v3"><div class="arch-card-v3 layer-hardware">Hardware</div></div>
<div class="arch-leader-v3"></div>
<div class="arch-desc-v3"><span class="highlight">Hardware</span> (ฮาร์ดแวร์อุปกรณ์) — Physical devices which execute calculations and instructions อุปกรณ์กายภาพทางอิเล็กทรอนิกส์ที่เป็นตัวขับเคลื่อนคำนวณประมวลผลคำสั่งจริง เช่น CPU, RAM, Hard Disk และการ์ดเน็ตเวิร์ก</div>
</div>

</div>
</div>"""

# 5. Slide 4: Linux File System
slide_4_md = """### 📌 Linux File System

Linux uses a **tree structure (hierarchy)** to store and organize files."""

# 6. Slide 5: Linux File System (Cont)
slide_5_md = """### 📌 Linux File System (Cont)

- Everything in Linux is considered as a file
- There are three types of files available in a Linux system:
  - **General files or ordinary files** are files that can be in ASCII or Binary format containing images, text, or programs.
  - **Directory files** are the depository for other files and directories can have a subdirectory within it.
  - **Device files** represent devices, such as the hard drive's partitions represented as `dev/sda1`, `dev/sda2`, etc."""

# 7. Slide 6: Linux Directory Structure (Staggered horizontal tree)
slide_6_md = """### 📂 Linux Directory Structure

สถาปัตยกรรมโครงสร้างระบบไฟล์และไดเรกทอรีของ Linux เริ่มต้นจากไดเรกทอรีราก (Root Directory `/`) และแตกกิ่งก้านสาขาตามลำดับขั้น เลื่อนเมาส์ชี้ที่แต่ละโฟลเดอร์เพื่อดูคำอธิบายหน้าที่กึ่งไทยอังกฤษและรายละเอียดระบบเส้นทางด้านล่าง:

<style>
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
.tree-side-text-card{background:linear-gradient(135deg,rgba(15,17,26,0.6) 0%,rgba(30,20,45,0.4) 100%);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:20px;width:100%;max-width:820px;margin-top:20px;display:flex;align-items:center;gap:16px;box-shadow:0 4px 15px rgba(0,0,0,0.2);}\n.tree-side-text-icon{font-size:2.2rem;color:#fbbf24;text-shadow:0 0 10px rgba(251, 191, 36, 0.4);}\n.tree-side-text-content{font-size:1.15rem;font-weight:700;line-height:1.6;color:#ffffff;text-align:left;}\n.tree-side-text-content span.highlight{color:#ff007f;text-shadow:0 0 8px rgba(255, 0, 127, 0.3);}\n.tree-hover-info{margin-top:24px;background:rgba(15, 17, 26, 0.75);border:1px solid rgba(255, 255, 255, 0.08);border-radius:12px;padding:20px 28px;width:100%;max-width:820px;min-height:100px;display:flex;align-items:center;gap:24px;box-shadow:0 8px 32px rgba(0, 0, 0, 0.4);transition:all 0.3s ease;}
.tree-hover-badge{font-weight:800;font-size:1.25rem;text-transform:none;letter-spacing:0.02em;color:#8a94a6;border-right:2px solid rgba(255, 255, 255, 0.15);padding-right:24px;display:flex;align-items:center;white-space:nowrap;transition:color 0.3s ease;font-family:'Fira Code', monospace;}
.tree-hover-desc{font-size:1.1rem;color:#cbd5e1;line-height:1.7;transition:color 0.3s ease;font-weight:600;}
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

# 8. Slide 7: Sub-trees map (our 5 flat-tree blueprints with CSS hover glow)
slide_7_md = """### 📂 Linux Important Files & Sub-Trees Map

แผนภาพจำลองกิ่งก้านโครงสร้างระบบไฟล์และไฟล์การตั้งค่าสำคัญต่างๆ ของ Linux แยกตามโฟลเดอร์หลักอย่างเป็นระบบ แสดงคีย์เวิร์ดและคำอธิบายภาษาไทยกึ่งอังกฤษถัดจากกิ่งไฟล์ทันทีเพื่อให้อ่านเปรียบเทียบความสัมพันธ์ได้โดยสะดวก (เลื่อนเมาส์ชี้เพื่อเน้นข้อความเรืองแสง):

<style>
.mini-tree-wrapper{margin:2.5rem 0;width:100%;max-width:820px;background:rgba(15,17,26,0.4);border:1px solid rgba(255,255,255,0.05);border-radius:12px;padding:24px;box-shadow:inset 0 0 20px rgba(0,0,0,0.3);}
.mini-tree-title{font-size:1.15rem;font-weight:700;color:#fbbf24;margin-bottom:20px;display:flex;align-items:center;gap:8px;text-shadow:0 0 10px rgba(251,191,36,0.15);}
.mt-flat-tree{display:flex;align-items:center;width:100%;position:relative;padding:10px 0;}
.mt-root-box{margin-right:40px;position:relative;z-index:2;display:flex;flex-direction:column;align-items:center;}
.mt-root-box::after{content:'';position:absolute;top:50%;right:-40px;width:40px;height:2px;background:rgba(255,255,255,0.15);z-index:1;transform:translateY(-50%);}
.mt-children-grid{display:flex;flex-direction:column;gap:12px;position:relative;padding-left:20px;border-left:2px solid rgba(255,255,255,0.15);z-index:2;width:100%;}
.mt-item-row{display:flex;align-items:center;width:100%;position:relative;transition:all 0.2s ease;cursor:pointer;}
.mt-item-row::before{content:'';position:absolute;top:50%;left:-20px;width:20px;height:2px;background:rgba(255,255,255,0.15);z-index:1;transform:translateY(-50%);transition:background 0.2s ease;}
.mt-card{font-size:0.8rem;padding:6px 12px;border-radius:6px;text-align:center;font-weight:700;white-space:nowrap;width:auto;min-width:90px;transition:all 0.25s ease;}
.mt-card.type-root{border:1px solid #fbbf24;background:rgba(251,191,36,0.05);color:#fbbf24;box-shadow:0 0 10px rgba(251,191,36,0.15);min-width:70px;}
.mt-card.type-blue{border:1px solid #00c0ff;background:rgba(0,192,255,0.03);color:#00c0ff;}
.mt-card.type-green{border:1px solid #3ddc84;background:rgba(61,220,132,0.02);color:#3ddc84;}
.mt-leader-line{flex:1;height:1px;border-bottom:1px dashed rgba(255,255,255,0.12);margin:0 16px;min-width:20px;transition:border-color 0.2s ease;}
.mt-desc-text{font-size:0.85rem;color:#94a3b8;line-height:1.5;max-width:500px;text-align:left;transition:all 0.2s ease;}
.mt-desc-text span.highlight{color:#a0aec0;font-weight:600;transition:all 0.2s ease;}
@media (max-width:768px){
.mt-desc-text{max-width:300px;}
}
.mt-item-row:hover .mt-card{transform:scale(1.04);color:#ffffff;}
.mt-item-row:hover .mt-card.type-blue{border-color:#00c0ff;box-shadow:0 0 12px rgba(0,192,255,0.35);background:rgba(0,192,255,0.08);}
.mt-item-row:hover .mt-card.type-green{border-color:#3ddc84;box-shadow:0 0 12px rgba(61,220,132,0.35);background:rgba(61,220,132,0.08);}
.mt-item-row:hover .mt-leader-line{border-bottom-color:rgba(255,255,255,0.4);border-bottom-style:solid;}
.mt-item-row:hover::before{background:rgba(255,255,255,0.4);}
.mt-item-row:hover .mt-desc-text{color:#ffffff;text-shadow:0 0 8px rgba(255,255,255,0.3);}
.mt-item-row:hover .mt-desc-text span.highlight{color:#fbbf24;text-shadow:0 0 10px rgba(251,191,36,0.5);}
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
</div>"""

# 9. Slide 8: Linux User Accounts
slide_8_md = """### 📌 Linux User Accounts

- Linux supports 3 types of users: **root**, **regular**, and **service**
- **Root user**:
  - Created during installation. Also called a **superuser** as it can access restricted files, install software and other utilities, and has full administrative rights.
  - Required for administrative tasks such as installing software or editing system files. We don't need root access for general tasks like creating files or browsing the internet.
- **Regular user**:
  - Created when installing Linux on the system. All files for each regular user are saved in their home directory. A regular user cannot access other users' directories.
- **Service user**:
  - Allows or denies access to various resources depending on the service type. Leading service providers such as Apache, Squid, email, and more have their own service accounts to increase security."""

# 10. Slide 9: Unix in Linux System
slide_9_md = """### 📌 Unix in Linux System

- **Unix** is an operating system first developed in the 1960s by Ken Thompson, Dennis Ritchie, etc., at Bell Laboratories.
- Bell Laboratories and MIT developed the operating system named Multics and renamed it to Unix (written in C).
- It is a stable, multi-user, multi-tasking system for servers, desktops, and laptops.
- **Linux** is a Unix-like operating system based on Unix principles."""

# 11. Slide 10: Unix in Linux System (Cont)
slide_10_md = """### 📌 Unix in Linux System (Cont)

- **UNIX Terminal**:
  - The terminal is a program that provides a command line interface (CLI) to interact with the shell and execute commands."""

# Build the complete list of blocks
blocks = []
blocks.append({"type": "markdown", "value": header_md})
blocks.append({"type": "markdown", "value": slide_1_md})
blocks.append({"type": "markdown", "value": "---"})
blocks.append({"type": "markdown", "value": slide_2_md})
blocks.append({"type": "markdown", "value": "---"})
blocks.append({"type": "markdown", "value": slide_3_md})
blocks.append({"type": "markdown", "value": "---"})
blocks.append({"type": "markdown", "value": slide_4_md})
blocks.append({"type": "markdown", "value": "---"})
blocks.append({"type": "markdown", "value": slide_5_md})
blocks.append({"type": "markdown", "value": "---"})
blocks.append({"type": "markdown", "value": slide_6_md})
blocks.append({"type": "markdown", "value": "---"})
blocks.append({"type": "markdown", "value": slide_7_md})
blocks.append({"type": "markdown", "value": "---"})
blocks.append({"type": "markdown", "value": slide_8_md})
blocks.append({"type": "markdown", "value": "---"})
blocks.append({"type": "markdown", "value": slide_9_md})
blocks.append({"type": "markdown", "value": "---"})
blocks.append({"type": "markdown", "value": slide_10_md})

# Append the preserved interactive question blocks
for qb in question_blocks:
    blocks.append({"type": "markdown", "value": "---"})
    blocks.append(qb)

# Save and Commit
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
db.session.commit()

print(f"Lesson 165 successfully rebuilt! Total blocks: {len(blocks)}")
for i, b in enumerate(blocks):
    print(f"Block {i}: type={b['type']} length={len(b['value'] or '')} snippet={b['value'][:80].replace(chr(10), ' ')}")
