import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l169 = db.session.query(TutorialLesson).filter_by(id=169).first()

# ─── Construct Premium Blocks for Lesson 169 ───
blocks_169 = []

# Block 0: Title & Header
blocks_169.append({
    "type": "markdown",
    "value": "## 🐍 การเปรียบเทียบภาษาและโครงสร้าง Hello World (Languages Comparison & HelloWorld)"
})

# Block 1: Overviews of Programming Languages (Interactive Selector)
blocks_169.append({
    "type": "markdown",
    "value": """### 📁 Overviews of Programming Languages

**ภาษาโปรแกรม (Programming Language)** คือภาษาประดิษฐ์ที่มีโครงสร้างไวยากรณ์ชัดเจน ใช้สำหรับเขียนคำสั่งให้คอมพิวเตอร์ทำงานตามที่มนุษย์ต้องการ ในวงการความมั่นคงปลอดภัยไซเบอร์และการเจาะระบบ (Ethical Hacking) ภาษาโปรแกรมยอดนิยมแต่ละภาษาจะมีบทบาทและหน้าที่จำเพาะดังนี้:

<style>
.lang-select-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;gap:24px;}
@media(max-width:820px){.lang-select-wrap{flex-direction:column;}}
.lang-cards-grid{flex-shrink:0;width:240px;display:flex;flex-direction:column;gap:10px;}
@media(max-width:820px){.lang-cards-grid{width:100%;flex-direction:row;flex-wrap:wrap;}}
.lang-select-card{background:rgba(15,17,26,0.5);border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:14px;cursor:pointer;transition:all 0.18s ease;display:flex;align-items:center;gap:12px;box-sizing:border-box;}
.lang-select-card:hover, .lang-select-card.active{border-color:#00f0ff;background:rgba(0,240,255,0.05);box-shadow:0 0 12px rgba(0,240,255,0.25);}
.lang-select-card .card-icon{font-size:1.6rem;}
.lang-select-card .card-title{font-family:'JetBrains Mono',monospace;font-size:0.95rem;font-weight:800;color:#e2e8f0;}
.lang-select-card.active .card-title{color:#ffffff;}

.lang-detail-panel{flex:1;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:24px;box-shadow:0 8px 32px rgba(0,0,0,0.4);display:flex;flex-direction:column;box-sizing:border-box;}
.lang-detail-hdr{display:flex;align-items:center;gap:12px;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:12px;margin-bottom:16px;}
.lang-detail-badge{font-size:0.68rem;font-weight:800;padding:2px 8px;border-radius:4px;text-transform:uppercase;letter-spacing:0.05em;background:rgba(0,240,255,0.08);border:1px solid rgba(0,240,255,0.25);color:#00f0ff;}
.lang-detail-title{font-size:1.15rem;font-weight:800;color:#ffffff;margin:0;}
.lang-detail-body{font-size:0.88rem;color:#94a3b8;line-height:1.75;}
.lang-detail-body p{margin:0 0 10px;}
.lang-detail-body strong{color:#fbbf24;}
</style>

<div class="lang-select-wrap">
<div class="lang-cards-grid">
<div class="lang-select-card active" onclick="showLangDetails('python', this)">
<span class="card-icon">🐍</span>
<span class="card-title">Python</span>
</div>
<div class="lang-select-card" onclick="showLangDetails('java', this)">
<span class="card-icon">☕</span>
<span class="card-title">Java</span>
</div>
<div class="lang-select-card" onclick="showLangDetails('cpp', this)">
<span class="card-icon">⚙️</span>
<span class="card-title">C / C++</span>
</div>
<div class="lang-select-card" onclick="showLangDetails('assembly', this)">
<span class="card-icon">📟</span>
<span class="card-title">Assembly</span>
</div>
</div>

<div class="lang-detail-panel">
<div class="lang-detail-hdr">
<span id="lang-badge" class="lang-detail-badge">Hacking Scripts</span>
<h4 id="lang-title" class="lang-detail-title">Python (ราชาแห่งการเจาะระบบ)</h4>
</div>
<div id="lang-desc" class="lang-detail-body">
<p>ภาษา Python เป็นภาษาที่ได้รับความนิยมสูงสุดในวงการ Cybersecurity และ Ethical Hacking</p>
<p><strong>บทบาทในความปลอดภัยไซเบอร์:</strong> นิยมใช้สำหรับเขียน <strong>Exploit Scripts (สคริปต์เจาะระบบ)</strong>, ระบบสแกนหาช่องโหว่อัตโนมัติ (Automation vulnerability scanning), และพัฒนาเครื่องมือแฮกเกอร์ขนาดเล็ก เนื่องจากมีโค้ดที่สั้น อ่านง่าย และมีคลังไลบรารีรองรับการรับส่งแพ็กเก็ตเครือข่ายที่หลากหลาย</p>
</div>
</div>
</div>

<script>
const langData = {
  'python': {
    title: 'Python (ราชาแห่งการเจาะระบบ)',
    badge: 'Hacking Scripts',
    desc: '<p>ภาษา Python เป็นภาษาที่ได้รับความนิยมสูงสุดในวงการ Cybersecurity และ Ethical Hacking</p><p><strong>บทบาทในความปลอดภัยไซเบอร์:</strong> นิยมใช้สำหรับเขียน <strong>Exploit Scripts (สคริปต์เจาะระบบ)</strong>, ระบบสแกนหาช่องโหว่อัตโนมัติ (Automation vulnerability scanning), และพัฒนาเครื่องมือแฮกเกอร์ขนาดเล็ก เนื่องจากมีโค้ดที่สั้น อ่านง่าย และมีคลังไลบรารีรองรับการรับส่งแพ็กเก็ตเครือข่ายที่หลากหลาย</p>'
  },
  'java': {
    title: 'Java (โครงสร้างหลักของแอปพลิเคชัน)',
    badge: 'App Security',
    desc: '<p>ภาษา Java เป็นภาษาหลักที่รันงานระบบหลังบ้านระดับองค์กรขนาดใหญ่ และเป็นแกนหลักในการพัฒนาแอปพลิเคชันบนระบบ Android</p><p><strong>บทบาทในความปลอดภัยไซเบอร์:</strong> มีบทบาทอย่างยิ่งในการตรวจสอบความปลอดภัยระดับ <strong>Android App Source Codes (การวิเคราะห์ซอร์สโค้ดและแกะแอปพลิเคชันแอนดรอยด์ย้อนกระบวนการ)</strong> รวมถึงการตรวจสอบสิทธิ์เพื่อหาช่องโหว่ OWASP ในระบบเซิร์ฟเวอร์องค์กร</p>'
  },
  'cpp': {
    title: 'C / C++ (สถาปัตยกรรมระดับล่างและระบบ)',
    badge: 'Low-Level & Malware',
    desc: '<p>ภาษา C และ C++ เป็นภาษาประสิทธิภาพสูงที่มีความสามารถในการเข้าถึงและสั่งงานหน่วยความจำ (RAM) และสิทธิ์ระดับฮาร์ดแวร์ได้เกือบไร้ข้อจำกัด</p><p><strong>บทบาทในความปลอดภัยไซเบอร์:</strong> ใช้สำหรับการพัฒนา <strong>System Services (บริการระดับล่างของระบบ)</strong> และในมุมมืดมักใช้สำหรับเขียน <strong>Malwares / Rootkits (มัลแวร์สิทธิ์สูง)</strong> ที่ต้องการหลบเลี่ยงแอนตี้ไวรัสและควบคุมเคอร์เนลของเครื่องคอมพิวเตอร์</p>'
  },
  'assembly': {
    title: 'Assembly (ภาษาเครื่องขั้นสุดยอด)',
    badge: 'Machine Code',
    desc: '<p>ภาษาแอสเซมบลี (Assembly) คือภาษาโปรแกรมระดับต่ำสุดถัดจากภาษาเครื่อง (Machine Code) โดยขึ้นตรงกับสถาปัตยกรรมชิปประมวลผล (เช่น Intel x86-64, ARM)</p><p><strong>บทบาทในความปลอดภัยไซเบอร์:</strong> เป็นกุญแจสำคัญสำหรับงาน <strong>Reverse Engineering (วิศวกรรมย้อนรอยเพื่อวิเคราะห์พฤติกรรมมัลแวร์)</strong> และการวิเคราะห์ช่องโหว่ความมั่นคงปลอดภัยแบบ Buffer Overflow ในไฟล์โปรแกรม binary ที่ไม่มีซอร์สโค้ดให้เปิดดู</p>'
  }
};

function showLangDetails(key, element) {
  const cards = document.querySelectorAll('.lang-select-card');
  cards.forEach(c => c.classList.remove('active'));
  element.classList.add('active');

  const data = langData[key];
  if (!data) return;

  document.getElementById('lang-title').textContent = data.title;
  document.getElementById('lang-badge').textContent = data.badge;
  document.getElementById('lang-desc').innerHTML = data.desc;
}
</script>"""
})

blocks_169.append({"type": "markdown", "value": "---"})

# Block 2: Programming Language Rankings
blocks_169.append({
    "type": "markdown",
    "value": """### 📊 Programming Language Rankings & Popularity

ข้อมูลการจัดอันดับความนิยมและประสิทธิภาพของภาษาโปรแกรมจากดัชนีชั้นนำระดับสากล:

<style>
.w-rank-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;gap:20px;}
@media(max-width:768px){.w-rank-wrap{flex-direction:column;}}
.w-rank-card{flex:1;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:20px;box-shadow:0 4px 20px rgba(0,0,0,0.25);}
.w-rank-card h4{margin:0 0 12px;font-size:1rem;color:#00f0ff;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:8px;}
.w-rank-item{display:flex;justify-content:between;align-items:center;padding:10px 0;border-bottom:1px solid rgba(255,255,255,0.04);font-family:'JetBrains Mono',monospace;font-size:0.83rem;}
.w-rank-item:last-child{border-bottom:none;}
.w-rank-num{font-weight:800;color:#fbbf24;width:30px;}
.w-rank-name{color:#e2e8f0;flex:1;}
.w-rank-val{color:#94a3b8;font-weight:700;}
</style>

<div class="w-rank-wrap">
<!-- IEEE Spectrum -->
<div class="w-rank-card">
<h4>🏆 IEEE Spectrum Ranking (2025)</h4>
<div class="w-rank-item"><span class="w-rank-num">#1</span><span class="w-rank-name">Python</span><span class="w-rank-val">100.0</span></div>
<div class="w-rank-item"><span class="w-rank-num">#2</span><span class="w-rank-name">Java</span><span class="w-rank-val">58.7</span></div>
<div class="w-rank-item"><span class="w-rank-num">#3</span><span class="w-rank-name">JavaScript</span><span class="w-rank-val">52.3</span></div>
<div class="w-rank-item"><span class="w-rank-num">#4</span><span class="w-rank-name">C++</span><span class="w-rank-val">49.8</span></div>
<div class="w-rank-item"><span class="w-rank-num">#5</span><span class="w-rank-name">C</span><span class="w-rank-val">46.2</span></div>
</div>
<!-- TIOBE Index -->
<div class="w-rank-card">
<h4>📈 TIOBE Index Popularity</h4>
<div class="w-rank-item"><span class="w-rank-num">#1</span><span class="w-rank-name">Python</span><span class="w-rank-val">18.5%</span></div>
<div class="w-rank-item"><span class="w-rank-num">#2</span><span class="w-rank-name">C</span><span class="w-rank-val">12.1%</span></div>
<div class="w-rank-item"><span class="w-rank-num">#3</span><span class="w-rank-name">C++</span><span class="w-rank-val">10.8%</span></div>
<div class="w-rank-item"><span class="w-rank-num">#4</span><span class="w-rank-name">Java</span><span class="w-rank-val">8.4%</span></div>
<div class="w-rank-item"><span class="w-rank-num">#5</span><span class="w-rank-name">C#</span><span class="w-rank-val">6.2%</span></div>
</div>
</div>"""
})

blocks_169.append({"type": "markdown", "value": "---"})

# Block 3: Core structures & paradigms
blocks_169.append({
    "type": "markdown",
    "value": """### 💡 Core Functional Structures & paradigms

แม้ว่าแต่ละภาษาจะมีไวยากรณ์ (Syntax) ที่แตกต่างกันอย่างสิ้นเชิง แต่ทุกภาษาจะต้องประกอบไปด้วย **4 องค์ประกอบแกนหลักร่วม (Core Functional Structures)** และถูกแบ่งตามลักษณะแนวคิดการเขียนโค้ด (Programming Paradigms) ดังนี้:

<style>
.w-para-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:18px;}
.w-para-core-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;}
@media(max-width:768px){.w-para-core-grid{grid-template-columns:repeat(2,1fr);}}
.w-para-core-card{background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:14px;box-sizing:border-box;}
.w-para-core-title{font-size:0.83rem;font-weight:800;color:#00f0ff;margin-bottom:4px;}
.w-para-core-desc{font-size:0.78rem;color:#94a3b8;line-height:1.5;margin:0;}

.w-para-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;}
@media(max-width:768px){.w-para-grid{grid-template-columns:1fr;}}
.w-para-card{background:rgba(15,17,26,0.5);border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:16px;box-sizing:border-box;}
.w-para-title{font-size:0.88rem;font-weight:800;color:#fbbf24;margin-bottom:6px;}
.w-para-desc{font-size:0.8rem;color:#94a3b8;line-height:1.6;margin:0;}
</style>

<div class="w-para-wrap">
<!-- 4 Core Structures -->
<div class="w-para-core-grid">
<div class="w-para-core-card">
<div class="w-para-core-title">📥 Getting Input</div>
<p class="w-para-core-desc">รับข้อมูลเข้าจากคีย์บอร์ด เครือข่าย หรือไฟล์ภายนอกเข้าสู่โปรแกรม</p>
</div>
<div class="w-para-core-card">
<div class="w-para-core-title">📤 Displaying Output</div>
<p class="w-para-core-desc">นำเสนอผลลัพธ์ข้อมูลออกมาวาดบนหน้าจอ ส่งออกเครือข่าย หรือบันทึกไฟล์</p>
</div>
<div class="w-para-core-card">
<div class="w-para-core-title">⚖️ Deciding</div>
<p class="w-para-core-desc">ตรวจสอบเงื่อนไขและตัดสินใจเลือกทิศทางการรันโค้ด (e.g. if-else)</p>
</div>
<div class="w-para-core-card">
<div class="w-para-core-title">🔁 Iterating</div>
<p class="w-para-core-desc">ประมวลผลการทำงานชุดคำสั่งซ้ำๆ ตามเงื่อนไข (e.g. loops)</p>
</div>
</div>

<!-- Programming Paradigms -->
<div class="w-para-grid">
<div class="w-para-card">
<div class="w-para-title">Structured Paradigm</div>
<p class="w-para-desc">เน้นเขียนคำสั่งเป็นลำดับขั้นตอนการไหล ควบคุมด้วยโครงสร้างเงื่อนไขและฟังก์ชันย่อยที่ชัดเจน</p>
</div>
<div class="w-para-card">
<div class="w-para-title">Object-Oriented (OOP)</div>
<p class="w-para-desc">ผูกฟังก์ชันและข้อมูลเข้าด้วยกันเป็นอ็อบเจกต์ (Objects) โดยใช้ระบบคลาส (Classes) เพื่อความยืดหยุ่น</p>
</div>
<div class="w-para-card">
<div class="w-para-title">Scripting Paradigm</div>
<p class="w-para-desc">เน้นแปลรันคำสั่งโดยตรงแบบเรียลไทม์เพื่อประสานงานระบบปฏิบัติการ เหมาะกับระบบอัตโนมัติ</p>
</div>
</div>
</div>"""
})

blocks_169.append({"type": "markdown", "value": "---"})

# Block 5: Language Processing Workflows
blocks_169.append({
    "type": "markdown",
    "value": """### ⚙️ Language Processing Workflows (การประมวลผลรันซอร์สโค้ด)

แต่ละภาษาโปรแกรมมีวิธีสั่งคอมพิวเตอร์ประมวลผลรันซอร์สโค้ด (Source Code) แตกต่างกัน โดยแบ่งเป็น 4 รูปแบบหลัก:

<style>
.w-proc-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:18px;}
.w-proc-tabs{display:flex;gap:10px;justify-content:center;}
.w-proc-tab-btn{padding:8px 14px;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);border-radius:6px;font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#94a3b8;cursor:pointer;transition:all 0.15s ease;}
.w-proc-tab-btn:hover, .w-proc-tab-btn.active{border-color:#00f0ff;color:#ffffff;background:rgba(0,240,255,0.05);box-shadow:0 0 10px rgba(0,240,255,0.2);}

.w-proc-flow-box{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:24px;min-height:160px;display:flex;flex-direction:column;justify-content:center;box-sizing:border-box;}
.w-flow-title{font-size:0.95rem;font-weight:700;color:#ffffff;margin:0 0 12px;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:8px;}
.w-flow-diagram{display:flex;align-items:center;gap:12px;justify-content:center;font-family:'JetBrains Mono',monospace;font-size:0.75rem;margin-bottom:14px;flex-wrap:wrap;}
.w-flow-node{padding:6px 12px;border-radius:6px;border:1px solid;font-weight:700;}
.w-flow-node.src{border-color:#fbbf24;background:rgba(251,191,36,0.04);color:#fbbf24;}
.w-flow-node.proc{border-color:#00f0ff;background:rgba(0,240,255,0.04);color:#00f0ff;}
.w-flow-node.out{border-color:#3ddc84;background:rgba(61,220,132,0.04);color:#3ddc84;}
.w-flow-arrow{color:#64748b;font-weight:bold;}
.w-flow-desc{font-size:0.83rem;color:#94a3b8;line-height:1.6;margin:0;}
</style>

<div class="w-proc-wrap">
<div class="w-proc-tabs">
<button class="w-proc-tab-btn active" onclick="showProcFlow('python', this)">Python</button>
<button class="w-proc-tab-btn" onclick="showProcFlow('java', this)">Java</button>
<button class="w-proc-tab-btn" onclick="showProcFlow('cpp', this)">C / C++</button>
<button class="w-proc-tab-btn" onclick="showProcFlow('assembly', this)">Assembly</button>
</div>

<div class="w-proc-flow-box">
<h4 id="proc-title" class="w-flow-title">Python processing (ระบบ Interpreter)</h4>
<div id="proc-diagram" class="w-flow-diagram">
<div class="w-flow-node src">Source Code (.py)</div>
<div class="w-flow-arrow">➡</div>
<div class="w-flow-node proc">Interpreter</div>
<div class="w-flow-arrow">➡</div>
<div class="w-flow-node out">Output</div>
</div>
<p id="proc-desc" class="w-flow-desc">ภาษา Python แปลและรันซอร์สโค้ดผ่านซอฟต์แวร์นำรัน (Interpreter) ทีละบรรทัดจากบนลงล่างโดยตรง ไม่ต้องแปลงเป็นไฟล์ binary ก่อน ทำให้สั่งรันและดีบั๊กเครื่องมือได้รวดเร็วมาก</p>
</div>
</div>

<script>
const procFlowData = {
  'python': {
    title: 'Python processing (ระบบ Interpreter)',
    flow: '<div class="w-flow-node src">Source Code (.py)</div><div class="w-flow-arrow">➡</div><div class="w-flow-node proc">Interpreter (Line-by-line)</div><div class="w-flow-arrow">➡</div><div class="w-flow-node out">Output</div>',
    desc: 'ภาษา Python แปลและรันซอร์สโค้ดผ่านซอฟต์แวร์นำรัน (Interpreter) ทีละบรรทัดจากบนลงล่างโดยตรง ไม่ต้องแปลงเป็นไฟล์ binary ก่อน ทำให้สั่งรันและดีบั๊กเครื่องมือได้รวดเร็วมาก'
  },
  'java': {
    title: 'Java processing (ระบบ Hybrid Compiler & JVM)',
    flow: '<div class="w-flow-node src">Source Code (.java)</div><div class="w-flow-arrow">➡</div><div class="w-flow-node proc">Compile (javac)</div><div class="w-flow-arrow">➡</div><div class="w-flow-node src">Byte Code (.class)</div><div class="w-flow-arrow">➡</div><div class="w-flow-node proc">JVM (Run java)</div><div class="w-flow-arrow">➡</div><div class="w-flow-node out">Output</div>',
    desc: 'ภาษา Java ใช้กระบวนการแบบผสม: ขั้นแรกซอร์สโค้ดจะถูกคอมไพล์ผ่าน <code>javac</code> ให้กลายเป็นไฟล์ระดับกลางเรียกว่า <strong>Byte Code (.class)</strong> จากนั้นจะนำไฟล์ไปแปลรันในระบบเครื่องจำลอง <strong>Java Virtual Machine (JVM)</strong> ทำให้โปรแกรมรันได้ทุกแพลตฟอร์ม'
  },
  'cpp': {
    title: 'C / C++ processing (ระบบ Native Compiler)',
    flow: '<div class="w-flow-node src">Source Code (.c/.cpp)</div><div class="w-flow-arrow">➡</div><div class="w-flow-node proc">Compile (gcc/g++)</div><div class="w-flow-arrow">➡</div><div class="w-flow-node src">Object Code (.o)</div><div class="w-flow-arrow">➡</div><div class="w-flow-node proc">Linker</div><div class="w-flow-arrow">➡</div><div class="w-flow-node out">Executable & Output</div>',
    desc: 'ภาษา C/C++ ทำการคอมไพล์โค้ดตรงให้เป็นภาษาเครื่อง <strong>Object Code</strong> จากนั้นผ่านขั้นตอน Linker เพื่อผูกไฟล์ไลบรารีระบบย่อยรวมกันออกมาเป็นไฟล์รันตัวระบบตรง (เช่น <code>a.out</code> หรือ <code>.exe</code>) ทำให้โปรแกรมมีประสิทธิภาพความเร็วการรันสูงสุด'
  },
  'assembly': {
    title: 'Assembly processing (ระบบ Assembler & Linker)',
    flow: '<div class="w-flow-node src">Source Code (.asm)</div><div class="w-flow-arrow">➡</div><div class="w-flow-node proc">Assemble (nasm)</div><div class="w-flow-arrow">➡</div><div class="w-flow-node src">Object Code (.o)</div><div class="w-flow-arrow">➡</div><div class="w-flow-node proc">Linker (ld)</div><div class="w-flow-arrow">➡</div><div class="w-flow-node out">Runnable & Output</div>',
    desc: 'ภาษาแอสเซมบลีเขียนชุดคำสั่งขึ้นตรงกับซีพียู ทำการแปลงคำสั่ง (Assemble) ผ่านเครื่องมือเช่น <code>nasm</code> เป็น Object Code แล้วจึงใช้ตัวเชื่อมโยงระบบ <code>ld (Linker)</code> ประกอบรวมเป็นไฟล์พร้อมรันระบบตรง'
  }
};

function showProcFlow(key, element) {
  const buttons = document.querySelectorAll('.w-proc-tab-btn');
  buttons.forEach(b => b.classList.remove('active'));
  element.classList.add('active');

  const data = procFlowData[key];
  if (!data) return;

  document.getElementById('proc-title').textContent = data.title;
  document.getElementById('proc-diagram').innerHTML = data.flow;
  document.getElementById('proc-desc').innerHTML = data.desc;
}
</script>"""
})

blocks_169.append({"type": "markdown", "value": "---"})

# Block 7: The Hello World Showdown (Interactive Playground)
blocks_169.append({
    "type": "markdown",
    "value": """### 💻 The Hello World Showdown

เลือกสลับแถบภาษาด้านข้างเพื่อเปรียบเทียบความแตกต่างของ **โครงสร้างชุดคำสั่ง (Source Code)** และ **ขั้นตอนคำสั่งรันงาน (Terminal Commands)** สำหรับแสดงคำว่า 'Hello World' ของแต่ละภาษา:

<style>
.w-play-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;gap:20px;}
@media(max-width:820px){.w-play-wrap{flex-direction:column;}}
.w-play-tabs{flex-shrink:0;width:180px;display:flex;flex-direction:column;gap:8px;}
@media(max-width:820px){.w-play-tabs{width:100%;flex-direction:row;flex-wrap:wrap;}}
.w-play-tab-btn{padding:10px 14px;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);border-radius:6px;font-family:'JetBrains Mono',monospace;font-size:0.75rem;color:#94a3b8;cursor:pointer;text-align:left;transition:all 0.15s ease;display:flex;align-items:center;justify-content:between;}
.w-play-tab-btn:hover, .w-play-tab-btn.active{border-color:#00f0ff;color:#ffffff;background:rgba(0,240,255,0.05);box-shadow:0 0 10px rgba(0,240,255,0.15);}
.w-play-tab-btn::after{content:"▶";font-size:0.6rem;color:#64748b;}
.w-play-tab-btn:hover::after, .w-play-tab-btn.active::after{color:#00f0ff;}
@media(max-width:820px){.w-play-tab-btn::after{content:"";}}

.w-play-content{flex:1;display:flex;flex-direction:column;gap:14px;}
.w-code-console{background:#05070f;border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:20px;box-shadow:0 8px 24px rgba(0,0,0,0.45);box-sizing:border-box;}
.w-code-title{font-size:0.8rem;color:#8a94a6;margin-bottom:8px;font-family:'JetBrains Mono',monospace;display:flex;justify-content:between;}
.w-code-title span.filename{color:#fbbf24;}
.w-code-body{font-family:'JetBrains Mono',monospace;font-size:0.82rem;color:#e2e8f0;white-space:pre-wrap;margin:0;}
</style>

<div class="w-play-wrap">
<div class="w-play-tabs">
<button class="w-play-tab-btn active" onclick="showPlayground('python', this)">Python</button>
<button class="w-play-tab-btn" onclick="showPlayground('java', this)">Java</button>
<button class="w-play-tab-btn" onclick="showPlayground('c', this)">C Language</button>
<button class="w-play-tab-btn" onclick="showPlayground('cpp', this)">C++ Language</button>
<button class="w-play-tab-btn" onclick="showPlayground('asm64', this)">Assembly 64-bit</button>
<button class="w-play-tab-btn" onclick="showPlayground('asm32', this)">Assembly 32-bit</button>
</div>

<div class="w-play-content">
<!-- Code Block -->
<div class="w-code-console" style="border-color:rgba(0,240,255,0.15);">
<div class="w-code-title">📄 Source Code: <span id="w-play-file" class="filename">Test.py</span></div>
<pre id="w-play-code" class="w-code-body" style="color:#00f0ff;">print('Hello World')</pre>
</div>
<!-- Run terminal -->
<div class="w-code-console" style="background:#070910;">
<div class="w-code-title">🐚 Terminal Compiler & Run Commands</div>
<pre id="w-play-term" class="w-code-body" style="color:#94a3b8;">$ python3 Test.py
<span style="color:#3ddc84; font-weight:bold;">Hello World</span></pre>
</div>
</div>
</div>

<script>
const playData = {
  'python': {
    file: 'Test.py',
    code: "print('Hello World')",
    term: "$ python3 Test.py\\n<span style=\\"color:#3ddc84; font-weight:bold;\\">Hello World</span>",
    color: '#00f0ff'
  },
  'java': {
    file: 'Test.java',
    code: "public class Test {\\n   public static void main(String[] args) {\\n      System.out.println(\\"Hello World\\");\\n   }\\n}",
    term: "$ javac Test.java\\n$ java Test\\n<span style=\\"color:#3ddc84; font-weight:bold;\\">Hello World</span>",
    color: '#fbbf24'
  },
  'c': {
    file: 'Test.c',
    code: "#include &lt;stdio.h&gt;\\nint main() {\\n   printf(\\"Hello World\\\\n\\");\\n   return 0;\\n}",
    term: "$ gcc Test.c\\n$ ./a.out\\n<span style=\\"color:#3ddc84; font-weight:bold;\\">Hello World</span>",
    color: '#3ddc84'
  },
  'cpp': {
    file: 'Test.cpp',
    code: "#include &lt;iostream&gt;\\nusing namespace std;\\nint main() {\\n   cout &lt;&lt; \\"Hello World\\" &lt;&lt; endl;\\n   return 0;\\n}",
    term: "$ g++ Test.cpp\\n$ ./a.out\\n<span style=\\"color:#3ddc84; font-weight:bold;\\">Hello World</span>",
    color: '#00f0ff'
  },
  'asm64': {
    file: 'Test.asm (64-bit Linux)',
    code: "section .text\\n    global _start\\n_start:\\n    mov rax, 1          ; syscall: write\\n    mov rdi, 1          ; fd: stdout\\n    mov rsi, message    ; buffer address\\n    mov rdx, length     ; length\\n    syscall\\n    mov rax, 60         ; syscall: exit\\n    xor rdi, rdi        ; code 0\\n    syscall\\nsection .data\\nmessage: db 'Hello World', 10\\nlength: equ $ - message",
    term: "$ nasm -f elf64 Test.asm\\n$ ld -o a.out Test.o\\n$ ./a.out\\n<span style=\\"color:#3ddc84; font-weight:bold;\\">Hello World</span>",
    color: '#ab20fd'
  },
  'asm32': {
    file: 'Test.asm (32-bit Linux)',
    code: "extern printf\\nsection .text\\n    global main\\nmain:\\n    push ebp\\n    mov ebp, esp\\n    push message\\n    call printf\\n    add esp, 4\\n    leave\\n    ret\\nsection .data\\nmessage: db 'Hello World', 10",
    term: "$ nasm -f elf32 Test.asm\\n$ gcc -m32 -no-pie -o a.out Test.o\\n$ ./a.out\\n<span style=\\"color:#3ddc84; font-weight:bold;\\">Hello World</span>",
    color: '#ff007f'
  }
};

function showPlayground(key, element) {
  const buttons = document.querySelectorAll('.w-play-tab-btn');
  buttons.forEach(b => b.classList.remove('active'));
  element.classList.add('active');

  const data = playData[key];
  if (!data) return;

  document.getElementById('w-play-file').textContent = data.file;
  
  const codeNode = document.getElementById('w-play-code');
  codeNode.innerHTML = data.code.replace(/\\\\n/g, '\\n');
  codeNode.style.color = data.color;

  document.getElementById('w-play-term').innerHTML = data.term.replace(/\\\\n/g, '\\n');
}
</script>"""
})

blocks_169.append({"type": "markdown", "value": "---"})

# Block 9: Interactive Mini-Quiz 2 questions with Neon Gauge Bar
blocks_169.append({
    "type": "markdown",
    "value": """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการผ่านบทเรียนย่อยนี้ (Lesson Clear):

<style>
.mini-quiz-box{width:100%;max-width:1050px;margin:2rem auto;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:24px;box-shadow:0 8px 32px rgba(0,0,0,0.3);box-sizing:border-box;}
.mq-q{margin-bottom:20px;}
.mq-title{font-size:0.9rem;font-weight:800;color:#e2e8f0;margin-bottom:10px;}
.mq-title span{color:#00f0ff;font-family:'JetBrains Mono',monospace;margin-right:6px;}
.mini-opts{display:flex;flex-direction:column;gap:6px;}
.mini-opt{display:flex;align-items:center;gap:10px;padding:10px 14px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.05);border-radius:8px;cursor:pointer;transition:all 0.15s ease;user-select:none;font-size:0.83rem;color:#cbd5e1;}
.mini-opt:hover{border-color:rgba(0,240,255,0.2);background:rgba(0,240,255,0.02);}
.mini-opt.selected{border-color:#00f0ff;background:rgba(0,240,255,0.08);color:#ffffff;}
.mini-opt.correct{border-color:#3ddc84;background:rgba(61,220,132,0.08);color:#ffffff;}
.mini-opt.incorrect{border-color:#ff007f;background:rgba(255,0,127,0.08);color:#ffffff;}
.mini-bullet{width:15px;height:15px;border:1px solid rgba(255,255,255,0.3);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.58rem;font-weight:bold;}
.mini-opt.selected .mini-bullet{border-color:#00f0ff;background:#00f0ff;color:#070910;}

/* Neon Gauge Progress Bar styling */
.mq-progress-container{width:100%;background:rgba(7,9,16,0.8);border:1px solid rgba(255,255,255,0.08);height:26px;border-radius:13px;position:relative;overflow:hidden;margin:20px 0;display:flex;align-items:center;box-shadow:inset 0 2px 8px rgba(0,0,0,0.6);}
.mq-progress-bar{width:0%;height:100%;background:linear-gradient(90deg, #ff007f 0%, #fbbf24 50%, #00f0ff 100%);transition:all 0.35s cubic-bezier(0.4, 0, 0.2, 1);box-shadow:0 0 12px rgba(0,240,255,0.2);}
.mq-progress-text{position:absolute;width:100%;text-align:center;font-family:'JetBrains Mono',monospace;font-size:0.75rem;font-weight:800;color:#ffffff;text-shadow:0 1px 3px rgba(0,0,0,0.9);z-index:2;letter-spacing:0.05em;}

.mq-btn-check{padding:10px 20px;background:#00f0ff;border:none;border-radius:6px;font-family:'JetBrains Mono',monospace;font-size:0.82rem;font-weight:800;color:#070910;cursor:pointer;box-shadow:0 0 10px rgba(0,240,255,0.25);transition:all 0.15s ease;}
.mq-btn-check:hover{background:#ffffff;box-shadow:0 0 15px rgba(255,255,255,0.4);transform:translateY(-1px);}
.mq-status-bar{display:none;padding:12px 16px;border-radius:8px;font-size:0.85rem;margin-top:16px;font-weight:700;line-height:1.5;}
</style>

<div id="mq-box-341" class="mini-quiz-box">
<!-- Question 1 -->
<div class="mq-q" data-correct="B">
<div class="mq-title"><span>Q1.</span> ภาษาโปรแกรมยอดนิยมข้อใดในวงการความปลอดภัยไซเบอร์ ที่นิยมใช้สำหรับพัฒนา Exploit Scripts (สคริปต์เจาะระบบ)?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A" onclick="updateMiniProgress(341)"><span class="mini-bullet">A</span> Java Language</div>
<div class="mini-opt" data-val="B" onclick="updateMiniProgress(341)"><span class="mini-bullet">B</span> Python Language</div>
<div class="mini-opt" data-val="C" onclick="updateMiniProgress(341)"><span class="mini-bullet">C</span> HTML / CSS</div>
</div>
</div>

<!-- Question 2 -->
<div class="mq-q" data-correct="A">
<div class="mq-title"><span>Q2.</span> กระบวนการประมวลผลและการรันไฟล์ของภาษา C/C++ มีลักษณะข้อใดที่ต่างจากภาษา Python?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A" onclick="updateMiniProgress(341)"><span class="mini-bullet">A</span> C/C++ ต้องคอมไพล์โค้ดให้เป็น Object code/ภาษาเครื่องก่อนรันจริง ขณะที่ Python รันผ่าน Interpreter ทีละบรรทัด</div>
<div class="mini-opt" data-val="B" onclick="updateMiniProgress(341)"><span class="mini-bullet">B</span> C/C++ ประมวลผลบนเครื่องจำลอง JVM ขณะที่ Python รันตรงบนแรมโดยไม่มีระบบ Interpreter แปลงคำสั่ง</div>
<div class="mini-opt" data-val="C" onclick="updateMiniProgress(341)"><span class="mini-bullet">C</span> ทั้งสองภาษามีกระบวนการแปลผลทีละบรรทัดจากบนลงล่างพร้อมกันเหมือนกันทุกประการ</div>
</div>
</div>

<!-- Neon Gauge Bar Progress -->
<div class="mq-progress-container">
<div id="mq-progress-bar-341" class="mq-progress-bar"></div>
<span id="mq-progress-text-341" class="mq-progress-text">Lesson Progress: 0% (ยังไม่ผ่าน)</span>
</div>

<button class="mq-btn-check" onclick="checkMiniQuiz(341)">Check Answers / ตรวจคำตอบ</button>
<div id="mq-status-341" class="mq-status-bar"></div>
</div>

<script>
// Attach click listeners to manage selection state
document.querySelectorAll('#mq-box-341 .mini-opt').forEach(opt => {
  opt.addEventListener('click', function() {
    const parent = this.closest('.mq-q');
    parent.querySelectorAll('.mini-opt').forEach(o => o.classList.remove('selected'));
    this.classList.add('selected');
  });
});

function updateMiniProgress(lnum) {
  const box = document.getElementById('mq-box-' + lnum);
  const qGroups = box.querySelectorAll('.mq-q');
  let answeredCount = 0;
  
  qGroups.forEach(g => {
    if (g.querySelector('.mini-opt.selected')) {
      answeredCount++;
    }
  });

  const pct = Math.round((answeredCount / qGroups.length) * 100);
  const pbar = document.getElementById('mq-progress-bar-' + lnum);
  const ptext = document.getElementById('mq-progress-text-' + lnum);

  if (pct > 0) {
    pbar.style.width = pct + '%';
    pbar.style.background = 'linear-gradient(90deg, #ff007f 0%, #fbbf24 100%)';
    ptext.textContent = 'Lesson Progress: ' + pct + '% (ตอบคำถามค้างอยู่)';
  }
}

function checkMiniQuiz(lnum) {
  const box = document.getElementById('mq-box-' + lnum);
  const groups = box.querySelectorAll('.mq-q');
  let score = 0;
  let allAnswered = true;

  groups.forEach(g => {
    const selected = g.querySelector('.mini-opt.selected');
    if (!selected) allAnswered = false;
  });

  if (!allAnswered) {
    alert("กรุณาตอบคำถามท้ายบทให้ครบถ้วนทั้ง 2 ข้อก่อนส่งตรวจคำตอบครับ!");
    return;
  }

  groups.forEach(g => {
    const correctVal = g.getAttribute('data-correct');
    const selected = g.querySelector('.mini-opt.selected');
    const selectedVal = selected.getAttribute('data-val');

    g.querySelectorAll('.mini-opt').forEach(o => {
      o.classList.remove('correct', 'incorrect');
      const val = o.getAttribute('data-val');
      if (val === correctVal) {
        o.classList.add('correct');
      } else if (o.classList.contains('selected')) {
        o.classList.add('incorrect');
      }
    });

    if (selectedVal === correctVal) score++;
  });

  const pbar = document.getElementById('mq-progress-bar-' + lnum);
  const ptext = document.getElementById('mq-progress-text-' + lnum);
  const status = document.getElementById('mq-status-' + lnum);
  status.style.display = 'block';

  if (score === 2) {
    pbar.style.width = '100%';
    pbar.style.background = '#3ddc84';
    pbar.style.boxShadow = '0 0 15px rgba(61,220,132,0.6)';
    ptext.textContent = 'Lesson Progress: 100% (ผ่านเรียบร้อย)';
    
    status.style.background = 'rgba(61,220,132,0.08)';
    status.style.border = '1px solid rgba(61,220,132,0.25)';
    status.style.color = '#3ddc84';
    status.innerHTML = '🏆 <strong>LESSON CLEARED!</strong> คุณผ่านการประเมินความรู้ท้ายบทเรียนย่อยนี้เรียบร้อย (คะแนน 2/2) สามารถเดินทางไปศึกษาบทเรียนถัดไปได้ครับ!';
  } else {
    const errorPct = Math.round((score / groups.length) * 100);
    pbar.style.width = errorPct + '%';
    pbar.style.background = '#ff007f';
    pbar.style.boxShadow = '0 0 15px rgba(255,0,127,0.6)';
    ptext.textContent = 'Lesson Progress: ' + errorPct + '% (ไม่ผ่าน - ทำไม่จบ)';

    status.style.background = 'rgba(255,0,127,0.08)';
    status.style.border = '1px solid rgba(255,0,127,0.25)';
    status.style.color = '#ff007f';
    status.innerHTML = '❌ <strong>ยังไม่ผ่าน!</strong> คุณได้คะแนน ' + score + '/2 (ทำข้อสอบไม่จบตาม Gauge Bar Progress) กรุณาทบทวนบทเรียนและตรวจเลือกคำตอบใหม่อีกครั้ง';
  }
}
</script>"""
})

# ─── Save the new restructured content of Lesson 169 to Database ───
l169.content = json.dumps(blocks_169, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=169).update({"content": l169.content})
db.session.commit()
print("Lesson 169 content completely redesigned into high-fidelity premium blocks!")
ctx.pop()
