import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

# ─── Q&A Accordion Content templates for Lessons 164 to 167 ───
qa_164 = {
    "type": "markdown",
    "value": """---
### ❓ Practice Questions (คำถามทบทวนความรู้ท้ายบท)

คำถามทบทวนความรู้ที่สำคัญเกี่ยวกับความเข้าใจระบบปฏิบัติการขั้นพื้นฐาน:

<style>
.qa-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:12px;}
.qa-item{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:10px;overflow:hidden;transition:all 0.25s ease;}
.qa-item:hover{border-color:rgba(0,240,255,0.25);background:rgba(0,240,255,0.01);box-shadow:0 4px 15px rgba(0,0,0,0.3);}
.qa-q{padding:16px 20px;font-size:0.92rem;font-weight:700;color:#e2e8f0;cursor:pointer;display:flex;justify-content:between;align-items:center;user-select:none;}
.qa-q::after{content:"▼";font-size:0.65rem;color:#64748b;margin-left:auto;transition:transform 0.2s ease;}
.qa-item.active .qa-q::after{transform:rotate(180deg);color:#00f0ff;}
.qa-a{max-height:0;overflow:hidden;padding:0 20px;font-size:0.86rem;color:#94a3b8;line-height:1.7;transition:all 0.25s ease-out;background:rgba(0,0,0,0.15);}
.qa-item.active .qa-a{max-height:300px;padding:16px 20px;border-top:1px solid rgba(255,255,255,0.03);}
.qa-item.active .qa-q{color:#00f0ff;}
</style>

<div class="qa-wrap">
<div class="qa-item active">
<div class="qa-q" onclick="toggleQA(this)">1. เคอร์เนล (Kernel) ทำหน้าที่อะไรในระบบปฏิบัติการ และมีความสำคัญอย่างไร?</div>
<div class="qa-a">
เคอร์เนลเป็นแกนหลักส่วนที่สำคัญที่สุดของระบบปฏิบัติการ ทำหน้าที่เป็นสะพานเชื่อมระหว่างโปรแกรมประยุกต์ (Software) และตัวเครื่องทางกายภาพ (Hardware) คอยควบคุมการจัดสรรเวลาการใช้ซีพียู จัดสรรหน่วยความจำแรม และจัดการระบบการรับส่งข้อมูล (I/O Devices) เพื่อให้ซอฟต์แวร์สามารถสั่งงานเครื่องได้
</div>
</div>
<div class="qa-item">
<div class="qa-q" onclick="toggleQA(this)">2. ทำไมระบบปฏิบัติการต้องแยกการรันข้อมูลระหว่าง User Mode และ Kernel Mode?</div>
<div class="qa-a">
เพื่อป้องกันความเสถียรและความปลอดภัยสูงสุดของระบบปฏิบัติการ หากแอปพลิเคชันทั่วไปใน User Mode เกิดข้อผิดพลาดหรือแครช จะไม่มีสิทธิ์เข้าถึงและทำให้เคอร์เนลหลักของระบบปฏิบัติการเสียหายตามไปด้วย ช่วยจำกัดขอบเขตไม่ให้โปรแกรมประยุกต์ทำลายความปลอดภัยของระบบ
</div>
</div>
</div>

<script>
function toggleQA(element) {
    const item = element.parentElement;
    item.classList.toggle("active");
}
</script>"""
}

qa_165 = {
    "type": "markdown",
    "value": """---
### ❓ Practice Questions (คำถามทบทวนความรู้ท้ายบท)

คำถามทบทวนโครงสร้างสถาปัตยกรรมและระบบไฟล์ของระบบปฏิบัติการ Linux:

<style>
.qa-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:12px;}
.qa-item{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:10px;overflow:hidden;transition:all 0.25s ease;}
.qa-item:hover{border-color:rgba(0,240,255,0.25);background:rgba(0,240,255,0.01);box-shadow:0 4px 15px rgba(0,0,0,0.3);}
.qa-q{padding:16px 20px;font-size:0.92rem;font-weight:700;color:#e2e8f0;cursor:pointer;display:flex;justify-content:between;align-items:center;user-select:none;}
.qa-q::after{content:"▼";font-size:0.65rem;color:#64748b;margin-left:auto;transition:transform 0.2s ease;}
.qa-item.active .qa-q::after{transform:rotate(180deg);color:#00f0ff;}
.qa-a{max-height:0;overflow:hidden;padding:0 20px;font-size:0.86rem;color:#94a3b8;line-height:1.7;transition:all 0.25s ease-out;background:rgba(0,0,0,0.15);}
.qa-item.active .qa-a{max-height:300px;padding:16px 20px;border-top:1px solid rgba(255,255,255,0.03);}
.qa-item.active .qa-q{color:#00f0ff;}
</style>

<div class="qa-wrap">
<div class="qa-item active">
<div class="qa-q" onclick="toggleQA(this)">1. ปรัชญาการออกแบบของระบบไฟล์ Linux ที่ว่า "Everything is a file" หมายถึงอะไร?</div>
<div class="qa-a">
หมายความว่า Linux มองและจัดการอุปกรณ์ฮาร์ดแวร์ภายนอกหรือบริการของระบบทุกอย่าง ไม่ว่าจะเป็น ฮาร์ดดิสก์ เครื่องพิมพ์ พอร์ตซีเรียล หรือโปรเซส ให้เป็น **ไฟล์ธรรมดา** ในตำแหน่งโฟลเดอร์ย่อย ทำให้เราใช้โปรแกรมและคำสั่งจัดการไฟล์มาตรฐานในการควบคุมการทำงานของฮาร์ดแวร์เหล่านั้นได้โดยตรง
</div>
</div>
<div class="qa-item">
<div class="qa-q" onclick="toggleQA(this)">2. โฟลเดอร์ /etc และ /var ในระบบปฏิบัติการ Linux ทำหน้าที่ต่างกันอย่างไร?</div>
<div class="qa-a">
โฟลเดอร์ <code>/etc</code> ใช้จัดเก็บไฟล์การตั้งค่า (Configuration Files) หลักของระบบปฏิบัติการและซอฟต์แวร์ ซึ่งมักจะเป็นไฟล์ข้อความนิ่ง ในขณะที่โฟลเดอร์ <code>/var</code> ใช้จัดเก็บข้อมูลที่มีการเปลี่ยนแปลงขนาดและบันทึกอยู่ตลอดเวลาขณะรันงาน เช่น ล็อกความปลอดภัย (Log Files) และคิวการส่งข้อมูล
</div>
</div>
</div>

<script>
function toggleQA(element) {
    const item = element.parentElement;
    item.classList.toggle("active");
}
</script>"""
}

qa_166 = {
    "type": "markdown",
    "value": """---
### ❓ Practice Questions (คำถามทบทวนความรู้ท้ายบท)

คำถามทบทวนการจัดการไฟล์และการวิเคราะห์สิทธิ์ความปลอดภัยในระบบ Linux:

<style>
.qa-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:12px;}
.qa-item{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:10px;overflow:hidden;transition:all 0.25s ease;}
.qa-item:hover{border-color:rgba(0,240,255,0.25);background:rgba(0,240,255,0.01);box-shadow:0 4px 15px rgba(0,0,0,0.3);}
.qa-q{padding:16px 20px;font-size:0.92rem;font-weight:700;color:#e2e8f0;cursor:pointer;display:flex;justify-content:between;align-items:center;user-select:none;}
.qa-q::after{content:"▼";font-size:0.65rem;color:#64748b;margin-left:auto;transition:transform 0.2s ease;}
.qa-item.active .qa-q::after{transform:rotate(180deg);color:#00f0ff;}
.qa-a{max-height:0;overflow:hidden;padding:0 20px;font-size:0.86rem;color:#94a3b8;line-height:1.7;transition:all 0.25s ease-out;background:rgba(0,0,0,0.15);}
.qa-item.active .qa-a{max-height:300px;padding:16px 20px;border-top:1px solid rgba(255,255,255,0.03);}
.qa-item.active .qa-q{color:#00f0ff;}
</style>

<div class="qa-wrap">
<div class="qa-item active">
<div class="qa-q" onclick="toggleQA(this)">1. คำสั่ง 'chmod 755 script.sh' มีผลลัพธ์ในการปรับสิทธิ์ความปลอดภัยอย่างไรบ้าง?</div>
<div class="qa-a">
คำสั่งนี้ทำการตั้งสิทธิ์ให้แก่ไฟล์ script.sh โดย:<br>
• **เจ้าของไฟล์ (User)** ได้รับสิทธิ์ระดับ 7 (Read+Write+Execute: <code>rwx</code>)<br>
• **กลุ่มเจ้าของไฟล์ (Group)** ได้รับสิทธิ์ระดับ 5 (Read+Execute: <code>r-x</code>)<br>
• **ผู้ใช้อื่นๆ (Others)** ได้รับสิทธิ์ระดับ 5 (Read+Execute: <code>r-x</code>) เพื่อให้เปิดดูเนื้อหาและสั่งรันสคริปต์ได้โดยไม่สามารถแก้ไขโค้ดข้างในได้
</div>
</div>
<div class="qa-item">
<div class="qa-q" onclick="toggleQA(this)">2. สิทธิ์ระดับ SUID (Set User ID) และ SGID ส่งผลต่อการเจาะระบบอย่างไรในมิติด้านความปลอดภัย?</div>
<div class="qa-a">
สิทธิ์ SUID ช่วยให้ผู้ใช้ปกติที่สั่งรันไฟล์โปรแกรมนั้นสามารถประมวลผลคำสั่งด้วยสิทธิ์ของ **เจ้าของไฟล์** (ซึ่งมักเป็น root) ชั่วคราว หากแฮกเกอร์พบจุดบกพร่องในไฟล์ที่ติดสิทธิ์ SUID แฮกเกอร์จะสามารถฉวยโอกาสยิง Payload เพื่อยกระดับสิทธิ์ตัวเองขึ้นเป็น root ทันที (Privilege Escalation)
</div>
</div>
</div>

<script>
function toggleQA(element) {
    const item = element.parentElement;
    item.classList.toggle("active");
}
</script>"""
}

qa_167 = {
    "type": "markdown",
    "value": """---
### ❓ Practice Questions (คำถามทบทวนความรู้ท้ายบท)

คำถามทบทวนการจัดการตัวแปรสภาพแวดล้อม คีย์ควบคุมดักจับ และ Regular Expression ใน Linux:

<style>
.qa-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:12px;}
.qa-item{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:10px;overflow:hidden;transition:all 0.25s ease;}
.qa-item:hover{border-color:rgba(0,240,255,0.25);background:rgba(0,240,255,0.01);box-shadow:0 4px 15px rgba(0,0,0,0.3);}
.qa-q{padding:16px 20px;font-size:0.92rem;font-weight:700;color:#e2e8f0;cursor:pointer;display:flex;justify-content:between;align-items:center;user-select:none;}
.qa-q::after{content:"▼";font-size:0.65rem;color:#64748b;margin-left:auto;transition:transform 0.2s ease;}
.qa-item.active .qa-q::after{transform:rotate(180deg);color:#00f0ff;}
.qa-a{max-height:0;overflow:hidden;padding:0 20px;font-size:0.86rem;color:#94a3b8;line-height:1.7;transition:all 0.25s ease-out;background:rgba(0,0,0,0.15);}
.qa-item.active .qa-a{max-height:300px;padding:16px 20px;border-top:1px solid rgba(255,255,255,0.03);}
.qa-item.active .qa-q{color:#00f0ff;}
</style>

<div class="qa-wrap">
<div class="qa-item active">
<div class="qa-q" onclick="toggleQA(this)">1. คีย์ลัดดักจับ 'ctrl-z' และ 'ctrl-c' ส่งสัญญาณควบคุมการทำงานต่างกันอย่างไร?</div>
<div class="qa-a">
ปุ่มลัด <code>ctrl-c</code> ทำหน้าที่ส่งสัญญาณ <strong>SIGINT (Interrupt)</strong> เพื่อบังคับให้โปรแกรมที่กำลังทำงานอยู่ปิดตัวลงและยุติการทำงานในทันที ส่วนปุ่มลัด <code>ctrl-z</code> จะส่งสัญญาณ <strong>SIGTSTP (Suspend)</strong> เพื่อทำการหยุดการทำงานของโปรแกรมไว้ชั่วคราวและพักโปรแกรมไปรันอยู่ด้านหลัง (Background Process)
</div>
</div>
<div class="qa-item">
<div class="qa-q" onclick="toggleQA(this)">2. การใช้เครื่องหมายท่อส่งน้ำ (| - Pipe) ทำหน้าที่อย่างไรในการรันคำสั่งความปลอดภัย?</div>
<div class="qa-a">
เครื่องหมายไพป์ทำหน้าที่ส่งต่อผลลัพธ์คำสั่ง (stdout) จากคำสั่งฝั่งซ้ายมือไปใช้เป็นข้อมูลอินพุต (stdin) ให้แก่คำสั่งฝั่งขวาตัวถัดไปโดยตรง ทำให้สามารถรันเรียงลำดับหลายคำสั่งเพื่อคัดกรองข้อมูลได้ เช่น ค้นหาล็อกผ่านคำสั่ง <code>cat log.txt | grep "Failed password"</code> เป็นต้น
</div>
</div>
</div>

<script>
function toggleQA(element) {
    const item = element.parentElement;
    item.classList.toggle("active");
}
</script>"""
}

# ─── 1. Update Lessons 164, 165, 166, 167 with bottom Q&A Accordion blocks ───
lesson_qa_map = {
    164: qa_164,
    165: qa_165,
    166: qa_166,
    167: qa_167
}

for lid, qa_block in lesson_qa_map.items():
    l = db.session.query(TutorialLesson).filter_by(id=lid).first()
    blocks = json.loads(l.content)
    # Check if last block is already a Q&A to avoid duplicates
    if "Practice Questions" not in blocks[-1].get("value", ""):
        blocks.append(qa_block)
        l.content = json.dumps(blocks, ensure_ascii=False)
        db.session.query(TutorialLesson).filter_by(id=lid).update({"content": l.content})
        db.session.commit()
        print(f"Added Q&A block to Lesson {lid}")

# ─── 2. Create/Recreate Lesson 197 (08. Final Module Exam) ───
existing = db.session.query(TutorialLesson).filter_by(id=197).first()
if existing:
    db.session.delete(existing)
    db.session.commit()
    print("Deleted old Lesson 197 to recreate cleanly.")

blocks_197 = []

# Header
blocks_197.append({
    "type": "markdown",
    "value": "## 📊 แบบทดสอบประเมินความรู้ท้ายบทเรียน (Final Module Exam: Linux & Windows)"
})

# Exam Console
blocks_197.append({
    "type": "markdown",
    "value": """### 🖥️ Linux & Windows OS Security Final Exam

ประเมินความรู้ทางด้านระบบปฏิบัติการขั้นพื้นฐานและการจัดการสิทธิ์ความปลอดภัยในระบบไซเบอร์ด้วยแบบทดสอบประเมินความรู้จำลองแบบโต้ตอบได้ด้านล่างนี้ (มีทั้งหมด 5 ข้อ):

<style>
.w-exam-box{width:100%;max-width:1050px;margin:2rem auto;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:32px;box-shadow:0 8px 32px rgba(0,0,0,0.4);box-sizing:border-box;}
.q-title{font-size:0.95rem;font-weight:800;color:#e2e8f0;margin-bottom:12px;}
.q-title span{color:#00f0ff;font-family:'JetBrains Mono',monospace;margin-right:8px;}
.q-group{margin-bottom:28px;}
.q-group:last-of-type{margin-bottom:20px;}
.ans-options{display:flex;flex-direction:column;gap:8px;}
.ans-opt{display:flex;align-items:center;gap:10px;padding:12px 16px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.05);border-radius:8px;cursor:pointer;transition:all 0.15s ease;user-select:none;font-size:0.86rem;color:#cbd5e1;}
.ans-opt:hover{border-color:rgba(0,240,255,0.25);background:rgba(0,240,255,0.03);}
.ans-opt.selected{border-color:#00f0ff;background:rgba(0,240,255,0.08);color:#ffffff;box-shadow:0 0 10px rgba(0,240,255,0.15);}
.ans-opt.correct{border-color:#3ddc84;background:rgba(61,220,132,0.08);color:#ffffff;}
.ans-opt.incorrect{border-color:#ff007f;background:rgba(255,0,127,0.08);color:#ffffff;}
.ans-bullet{width:16px;height:16px;border:1px solid rgba(255,255,255,0.3);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.6rem;font-weight:bold;transition:all 0.15s ease;}
.ans-opt.selected .ans-bullet{border-color:#00f0ff;background:#00f0ff;color:#070910;}

.w-exam-btn{padding:12px 24px;background:#00f0ff;border:none;border-radius:6px;font-family:'JetBrains Mono',monospace;font-size:0.9rem;font-weight:800;color:#070910;cursor:pointer;box-shadow:0 0 12px rgba(0,240,255,0.3);transition:all 0.18s ease;}
.w-exam-btn:hover{background:#ffffff;box-shadow:0 0 20px rgba(255,255,255,0.5);transform:translateY(-1px);}

.w-result-panel{display:none;background:rgba(7,9,16,0.9);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:24px;margin-top:24px;box-shadow:inset 0 0 20px rgba(255,255,255,0.02);box-sizing:border-box;}
.w-result-score{font-size:1.4rem;font-weight:800;color:#ffffff;margin-bottom:8px;}
.w-result-score span{color:#00f0ff;}
.w-result-comment{font-size:0.88rem;color:#94a3b8;line-height:1.6;margin-bottom:18px;}
.w-expl-box{background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:16px;margin-top:14px;box-sizing:border-box;}
.w-expl-q{font-size:0.83rem;font-weight:700;color:#fbbf24;margin-bottom:4px;}
.w-expl-a{font-size:0.8rem;color:#94a3b8;line-height:1.55;margin:0;}
</style>

<div class="w-exam-box">
<!-- Question 1 -->
<div class="q-group" data-correct="A">
<div class="q-title"><span>Q1.</span> ข้อใดอธิบายประเภทและสถาปัตยกรรมของ Kernel ในระบบปฏิบัติการ Linux และ Windows ได้ถูกต้อง?</div>
<div class="ans-options">
<div class="ans-opt" data-val="A"><span class="ans-bullet">A</span> Linux เป็น Monolithic Kernel / Windows เป็น Hybrid Kernel</div>
<div class="ans-opt" data-val="B"><span class="ans-bullet">B</span> Linux เป็น Hybrid Kernel / Windows เป็น Monolithic Kernel</div>
<div class="ans-opt" data-val="C"><span class="ans-bullet">C</span> ทั้งคู่เป็น Monolithic Kernel ที่มีแกนหลักขนาดใหญ่เหมือนกัน</div>
<div class="ans-opt" data-val="D"><span class="ans-bullet">D</span> ทั้งคู่ทำงานในรูปแบบ Microkernel ที่ปลอดภัยและเสถียรสูงสุด</div>
</div>
</div>

<!-- Question 2 -->
<div class="q-group" data-correct="C">
<div class="q-title"><span>Q2.</span> หากต้องการเปลี่ยนสิทธิ์ของสคริปต์ความปลอดภัยใน Linux ให้เฉพาะผู้เป็น "เจ้าของไฟล์" เท่านั้นที่มีสิทธิ์อ่าน เขียน และรัน ส่วนคนอื่นไม่มีสิทธิ์ใดๆ ต้องใช้คำสั่งใด?</div>
<div class="ans-options">
<div class="ans-opt" data-val="A"><span class="ans-bullet">A</span> chmod 755 script.sh</div>
<div class="ans-opt" data-val="B"><span class="ans-bullet">B</span> chmod 777 script.sh</div>
<div class="ans-opt" data-val="C"><span class="ans-bullet">C</span> chmod 700 script.sh</div>
<div class="ans-opt" data-val="D"><span class="ans-bullet">D</span> chmod 644 script.sh</div>
</div>
</div>

<!-- Question 3 -->
<div class="q-group" data-correct="D">
<div class="q-title"><span>Q3.</span> ในสิทธิ์ความปลอดภัยระบบไฟล์ NTFS Permissions ของ Windows หากกลุ่ม User มีสิทธิ์อนุญาตเข้าถึงโฟลเดอร์ แต่ตัวบัญชีเดี่ยวโดนตั้งค่าปฏิเสธการเข้าใช้ (Explicit Deny) ผลจะเป็นอย่างไร?</div>
<div class="ans-options">
<div class="ans-opt" data-val="A"><span class="ans-bullet">A</span> สิทธิ์เฉลี่ยกัน สามารถเข้าไปอ่านข้อมูลได้แต่ไม่สามารถแก้ไขเขียนทับได้</div>
<div class="ans-opt" data-val="B"><span class="ans-bullet">B</span> สิทธิ์อนุญาตทำงาน เพราะมีสิทธิ์ที่กว้างกว่าของกลุ่มผู้ใช้นำทางสิทธิ์นำหน้า</div>
<div class="ans-opt" data-val="C"><span class="ans-bullet">C</span> ระบบจะข้ามสิทธิ์และยื่นขอสิทธิ์ยืนยันความต้องการผ่านหน้าต่าง UAC</div>
<div class="ans-opt" data-val="D"><span class="ans-bullet">D</span> ระบบจะห้ามเข้าถึงโฟลเดอร์นั้นทันที เพราะสิทธิ์ปฏิเสธ (Deny) มีผลสูงสุดเหนือกฎข้ออื่น</div>
</div>
</div>

<!-- Question 4 -->
<div class="q-group" data-correct="B">
<div class="q-title"><span>Q4.</span> ในระบบ Windows ตัวแปรสภาพแวดล้อมระดับระบบข้อใดที่เก็บค่ารายการของพาธโฟลเดอร์ซึ่งระบบจะวิ่งเข้าไปเพื่อค้นหาไฟล์โปรแกรมรันงานอัตโนมัติ?</div>
<div class="ans-options">
<div class="ans-opt" data-val="A"><span class="ans-bullet">A</span> %USERPROFILE%</div>
<div class="ans-opt" data-val="B"><span class="ans-bullet">B</span> %PATH%</div>
<div class="ans-opt" data-val="C"><span class="ans-bullet">C</span> %TEMP%</div>
<div class="ans-opt" data-val="D"><span class="ans-bullet">D</span> %OS%</div>
</div>
</div>

<!-- Question 5 -->
<div class="q-group" data-correct="B">
<div class="q-title"><span>Q5.</span> ข้อใดอธิบายความแตกต่างของมุมมองและวิธีการจัดการอุปกรณ์ต่อพ่วง (Peripherals) ใน Linux และ Windows ได้ตรงหลักการ?</div>
<div class="ans-options">
<div class="ans-opt" data-val="A"><span class="ans-bullet">A</span> Linux มองเป็นพาร์ติชันตัวอักษรดิสก์ (A:, B:) / Windows มองเป็นโหนดการเชื่อมต่อพอร์ต</div>
<div class="ans-opt" data-val="B"><span class="ans-bullet">B</span> Linux มองอุปกรณ์ภายนอกเป็น "ไฟล์ข้อมูลปกติ" / Windows มองอุปกรณ์เหล่านั้นแยกต่างหากเป็น "Devices"</div>
<div class="ans-opt" data-val="C"><span class="ans-bullet">C</span> Linux มองเป็นหน่วยฮาร์ดแวร์ / Windows มองเป็นไลบรารีระบบเชื่อมร่วม</div>
<div class="ans-opt" data-val="D"><span class="ans-bullet">D</span> ไม่มีข้อใดถูก ทั้งคู่จัดการผ่านไดรฟ์ C:\ และสิทธิ์แอดมินเหมือนกันทุกประการ</div>
</div>
</div>

<button class="w-exam-btn" onclick="submitFinalExam()">Submit Exam / ส่งคำตอบ</button>

<div id="exam-res" class="w-result-panel">
<div class="w-result-score">ผลการสอบประเมิน: <span id="score-val">0</span> / 5 คะแนน</div>
<p id="comment-val" class="w-result-comment">พยายามใหม่อีกครั้งเพื่ออุดช่องโหว่ความรู้!</p>

<div class="w-expl-box">
<div class="w-expl-q">🔑 เฉลยข้อที่ 1 (Kernel Architecture)</div>
<p class="w-expl-a">คำตอบคือ **A** เพราะ Linux เคอร์เนลเป็น Monolithic Kernel (รวบรวมฟังก์ชันระบบทั้งหมดเข้าในเคอร์เนลตัวเดี่ยวเพื่อประสิทธิภาพที่เร็ว) ขณะที่ Windows NT ใช้แนวคิด Microkernel แบบลูกผสม (Hybrid Kernel)</p>
</div>

<div class="w-expl-box">
<div class="w-expl-q">🔑 เฉลยข้อที่ 2 (Linux chmod)</div>
<p class="w-expl-a">คำตอบคือ **C** เพราะสิทธิ์ 700 ถอดรหัสฐานแปดได้เป็น `rwx------` หมายถึง เจ้าของไฟล์ได้สิทธิ์ครบถ้วน (7) ขณะที่กลุ่มเจ้าของไฟล์ (0) และผู้ใช้อื่นๆ (0) จะไม่มีสิทธิ์ใดๆ ในการเข้าถึงสคริปต์นี้</p>
</div>

<div class="w-expl-box">
<div class="w-expl-q">🔑 เฉลยข้อที่ 3 (Windows NTFS permissions)</div>
<p class="w-expl-a">คำตอบคือ **D** เพราะในระบบความปลอดภัยของ NTFS Permissions กฎการสั่งปฏิเสธสิทธิ์แบบระบุชัดเจน (Explicit Deny) จะมีน้ำหนักและความสำคัญสูงสุดเสมอ ซึ่งจะเอาชนะ (Override) ทุกสิทธิ์การอนุญาต (Grant) เสมอ</p>
</div>

<div class="w-expl-box">
<div class="w-expl-q">🔑 เฉลยข้อที่ 4 (Environment Variables)</div>
<p class="w-expl-a">คำตอบคือ **B** เพราะตัวแปรระบบ <code>%PATH%</code> เก็บบันทึกรายการพาธระบบที่ระบบปฏิบัติการใช้สแกนและสืบค้นหาไฟล์รันโปรแกรมเมื่อผู้ใช้ป้อนคำสั่งเข้ามาใน CMD</p>
</div>

<div class="w-expl-box">
<div class="w-expl-q">🔑 เฉลยข้อที่ 5 (Peripherals)</div>
<p class="w-expl-a">คำตอบคือ **B** เพราะตามปรัชญาของ Unix/Linux "Everything is a file" ทุกอุปกรณ์จะถูกเข้าถึงในฐานะไฟล์ย่อยบนพาร์ติชัน <code>/dev</code> ขณะที่ Windows มองแยกขาดออกเป็นวัตถุอุปกรณ์ (Devices)</p>
</div>
</div>
</div>

<script>
// Attach click listeners to exam options
document.querySelectorAll('.ans-opt').forEach(opt => {
  opt.addEventListener('click', function() {
    const parent = this.closest('.q-group');
    // Remove selected state from sibling options
    parent.querySelectorAll('.ans-opt').forEach(o => o.classList.remove('selected'));
    this.classList.add('selected');
  });
});

function submitFinalExam() {
  const groups = document.querySelectorAll('.q-group');
  let score = 0;
  let allAnswered = true;

  groups.forEach(g => {
    const selected = g.querySelector('.ans-opt.selected');
    if (!selected) {
      allAnswered = false;
    }
  });

  if (!allAnswered) {
    alert("กรุณาตอบคำถามให้ครบถ้วนทั้ง 5 ข้อก่อนส่งคำตอบครับ!");
    return;
  }

  groups.forEach(g => {
    const correctVal = g.getAttribute('data-correct');
    const selected = g.querySelector('.ans-opt.selected');
    const selectedVal = selected.getAttribute('data-val');

    g.querySelectorAll('.ans-opt').forEach(o => {
      o.classList.remove('correct', 'incorrect');
      const val = o.getAttribute('data-val');
      if (val === correctVal) {
        o.classList.add('correct');
      } else if (o.classList.contains('selected')) {
        o.classList.add('incorrect');
      }
    });

    if (selectedVal === correctVal) {
      score++;
    }
  });

  // Update result panel
  const scoreVal = document.getElementById('score-val');
  const commentVal = document.getElementById('comment-val');
  const resPanel = document.getElementById('exam-res');

  scoreVal.textContent = score;
  resPanel.style.display = 'block';

  if (score === 5) {
    commentVal.innerHTML = '🥇 <strong>ยอดเยี่ยมที่สุด!</strong> คุณทำคะแนนได้เต็ม 5/5 เข้าใจความมั่นคงปลอดภัยสถาปัตยกรรม Linux & Windows อย่างแจ่มแจ้ง!';
    commentVal.style.color = '#3ddc84';
  } else if (score >= 3) {
    commentVal.innerHTML = '👍 <strong>ผ่านการทดสอบ!</strong> คุณได้คะแนน ' + score + '/5 มีความเข้าใจในโครงสร้างหลักเป็นอย่างดี ลองดูข้อที่พลาดเพื่อพัฒนาตนเองต่อครับ';
    commentVal.style.color = '#fbbf24';
  } else {
    commentVal.innerHTML = '❌ <strong>พยายามอีกครั้ง!</strong> คุณได้คะแนน ' + score + '/5 ลองทบทวนเนื้อหาระบบสิทธิ์และสถาปัตยกรรมและกลับมาทำแบบทดสอบใหม่อีกครั้งนะครับ';
    commentVal.style.color = '#ff007f';
  }

  // Scroll to results cleanly
  resPanel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}
</script>"""
})

# ─── Add Lesson 197 to Database ───
new_exam = TutorialLesson(
    id=197,
    module_id=33,
    title="08. แบบทดสอบประเมินความรู้ท้ายบทเรียน (Final Module Exam: Linux & Windows OS)",
    content=json.dumps(blocks_197, ensure_ascii=False),
    position=8,
    challenge_id=None
)

db.session.add(new_exam)
db.session.commit()
print("New Lesson 197 (08. Final Module Exam) created and committed to the database!")
