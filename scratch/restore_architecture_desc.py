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

# The HTML code for side-aligned architecture blueprints (completely flat, 0-indentation)
html_arch_blueprint = """### 💻 Linux System Architecture

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
</div>
"""

# Update block 2
blocks[2]['value'] = html_arch_blueprint

# Save and Commit
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
db.session.commit()
print("Architecture block 2 updated with side-by-side blueprint layout successfully!")
