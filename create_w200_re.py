import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

# ─── 1. Shift Lesson 172 to Position 7 to make room for Lesson 200 ───
l172 = db.session.query(TutorialLesson).filter_by(id=172).first()
if l172:
    l172.position = 7
    l172.title = "07. การเขียนโค้ดที่ไม่มีความปลอดภัยและช่องโหว่ (Insecure Coding & Buffer Overflows)"
    db.session.commit()
    print("Lesson 172 shifted to Position 7.")

# ─── 2. Construct content blocks for Lesson 200 (06. Reverse Engineering) ───
blocks_200 = []

# Block 0: Title & Header
blocks_200.append({
    "type": "markdown",
    "value": "## 🔎 ทักษะโปรแกรมมิ่งสำหรับการวิเคราะห์ย้อนรอยซอฟต์แวร์ (Programming Skills for Reverse Engineering)"
})

# Block 1: Foundations Grid
blocks_200.append({
    "type": "markdown",
    "value": """### 🔬 Essential Reverse Engineering Foundations

วิศวกรรมย้อนรอย (Reverse Engineering) เป็นศาสตร์ในการคลี่แยกโครงสร้างไฟล์ไบนารี (Compiled Binaries) ที่ไม่มีซอร์สโค้ด เพื่อวิเคราะห์กลไกการทำงาน ตรวจจับมัลแวร์ หรือค้นหาจุดบกพร่องของซอฟต์แวร์ โดยมีทักษะและเครื่องมือแกนหลักที่เกี่ยวข้องดังนี้:

<style>
.rev-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:2rem auto;max-width:1050px;}
@media(max-width:820px){.rev-grid{grid-template-columns:1fr;}}
.rev-card{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:20px;box-sizing:border-box;transition:all 0.25s ease;display:flex;flex-direction:column;justify-content:between;}
.rev-card:hover{border-color:#00f0ff;background:rgba(0,240,255,0.02);transform:translateY(-2px);box-shadow:0 0 15px rgba(0,240,255,0.25);}
.rev-title{font-size:0.92rem;font-weight:800;color:#00f0ff;margin-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.05);padding-bottom:6px;}
.rev-desc{font-size:0.8rem;color:#94a3b8;line-height:1.65;margin:0 0 10px;}
.rev-badge{font-size:0.68rem;font-weight:700;color:#fbbf24;font-family:'JetBrains Mono',monospace;}
</style>

<div class="rev-grid">
<!-- Low-level languages -->
<div class="rev-card">
<div>
<div class="rev-title">📟 Assembly Languages</div>
<p class="rev-desc">ทำความเข้าใจโครงสร้างรีจิสเตอร์และการประมวลผลระดับต่ำของ CPU (x86/x64, ARM) เพื่ออ่านคำสั่ง Assembly</p>
</div>
<span class="rev-badge">Registers, CPU Instructions</span>
</div>

<!-- Stack/Heap -->
<div class="rev-card">
<div>
<div class="rev-title">🧠 Memory & Pointers</div>
<p class="rev-desc">ทำความเข้าใจการจัดสรรข้อมูลในหน่วยความจำ RAM โครงสร้างพิกัด Pointers และการทำงานของ Heap และ Stack</p>
</div>
<span class="rev-badge">Heap, Stack, Memory Address</span>
</div>

<!-- Debuggers -->
<div class="rev-card">
<div>
<div class="rev-title">🐞 Debuggers & Tracers</div>
<p class="rev-desc">การใช้ระบบดักสถานะการรัน เช่น การปักหมุดจุดหยุด (Breakpoints) และการก้าวคำสั่งทีละบรรทัด (Stepping) ผ่านโปรแกรม</p>
</div>
<span class="rev-badge">Tools: GDB, x64dbg, WinDbg</span>
</div>
</div>

<div class="rev-grid" style="margin-top:0;">
<!-- Disassemblers -->
<div class="rev-card" style="grid-column: span 2;">
<div>
<div class="rev-title">🛠️ Disassemblers & Decompilers</div>
<p class="rev-desc">การใช้ซอฟต์แวร์วิเคราะห์แยกแยะซอร์สโค้ด โดย <strong>Disassemblers</strong> ทำหน้าที่แปลงเลขฐานภาษาเครื่องดิบให้เป็นคำสั่งแอสเซมบลีที่มนุษย์พออ่านเข้าใจได้ และ <strong>Decompilers</strong> แปลงกลับขึ้นไปเป็นภาษาโปรแกรมระดับสูง (เช่น C Language)</p>
</div>
<span class="rev-badge">Tools: Ghidra, IDA Pro, Radare2, Binary Ninja</span>
</div>

<!-- Bytecode -->
<div class="rev-card">
<div>
<div class="rev-title">🌐 Python Bytecode</div>
<p class="rev-desc">ทำความเข้าใจรหัสระดับกลางของภาษาประเภท VM-based เพื่อแกะระบบ ถอดความ หรือเขียนโค้ดทับแบบเรียลไทม์</p>
</div>
<span class="rev-badge">Python dis module, bytecode</span>
</div>
</div>"""
})

blocks_200.append({"type": "markdown", "value": "---"})

# Block 2: Interactive Code Console with Detailed Line-by-Line analysis
blocks_200.append({
    "type": "markdown",
    "value": """### 💻 Reverse Engineering Coding Sandbox (วิเคราะห์เจาะลึก 5 ตัวอย่างโค้ดย้อนรอย)

คลิกหัวข้อด้านซ้ายมือเพื่อตรวจสอบตัวอย่างโค้ดวิเคราะห์โครงสร้างข้อมูล (Code) และ **การวิเคราะห์การทำงานอย่างละเอียดในเชิงความปลอดภัยไซเบอร์ (Detailed Security Analysis)**:

<style>
.w-sandbox-main{display:flex;gap:20px;margin:2rem auto;max-width:1050px;}
@media(max-width:820px){.w-sandbox-main{flex-direction:column;}}

.w-sandbox-nav{width:220px;display:flex;flex-direction:column;gap:6px;flex-shrink:0;}
@media(max-width:820px){.w-sandbox-nav{width:100%;flex-direction:row;flex-wrap:wrap;}}
.w-nav-item{padding:8px 12px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.04);border-radius:6px;font-size:0.75rem;color:#cbd5e1;cursor:pointer;text-align:left;transition:all 0.15s ease;}
.w-nav-item:hover, .w-nav-item.active{border-color:#00f0ff;color:#ffffff;background:rgba(0,240,255,0.04);}
.w-nav-item.active{font-weight:bold;box-shadow:0 0 8px rgba(0,240,255,0.1);}

.w-sandbox-panels{flex:1;display:flex;flex-direction:column;gap:14px;}
.w-sand-panel{display:none;background:#05070f;border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:20px;box-shadow:0 8px 24px rgba(0,0,0,0.45);box-sizing:border-box;}
.w-sand-panel.active{display:block;}

.w-sand-hdr{font-size:0.95rem;font-weight:800;color:#ffffff;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:10px;margin-bottom:14px;display:flex;justify-content:between;align-items:center;}
.w-sand-hdr span.tag{font-size:0.65rem;padding:2px 8px;border-radius:4px;background:rgba(0,240,255,0.08);border:1px solid rgba(0,240,255,0.2);color:#00f0ff;font-family:'JetBrains Mono',monospace;}
.w-sand-code{font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#00f0ff;white-space:pre-wrap;margin:0 0 16px;background:rgba(0,0,0,0.2);padding:14px;border-radius:8px;border:1px solid rgba(255,255,255,0.02);}

.w-sand-expl{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:16px;font-size:0.83rem;color:#cbd5e1;line-height:1.65;}
.w-sand-expl h5{margin:0 0 8px;font-size:0.85rem;color:#fbbf24;font-weight:bold;}
.w-sand-expl p{margin:0 0 10px;}
.w-sand-expl p:last-child{margin-bottom:0;}
.w-sand-expl ul{margin:0;padding-left:20px;}
.w-sand-expl li{margin-bottom:6px;}
.w-sand-expl strong{color:#ffffff;}
</style>

<div class="w-sandbox-main">
<!-- Navigation Left Side -->
<div class="w-sandbox-nav">
<button class="w-nav-item active" onclick="showSandboxItem('pyewdis', this)">1. Disassembly via Pyew</button>
<button class="w-nav-item" onclick="showSandboxItem('radare2', this)">2. Radare2 (r2pipe)</button>
<button class="w-nav-item" onclick="showSandboxItem('pybytecode', this)">3. View Python Bytecode</button>
<button class="w-nav-item" onclick="showSandboxItem('compilebyte', this)">4. Compile Code to Bytecode</button>
<button class="w-nav-item" onclick="showSandboxItem('modbytecode', this)">5. Modifying Python Bytecode</button>
</div>

<!-- Panel details right side -->
<div class="w-sandbox-panels">

<!-- 1. Pyew -->
<div id="panel-pyewdis" class="w-sand-panel active">
<div class="w-sand-hdr"><span>1. Disassembly via Pyew</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">from pyew import Pyew
pyew = Pyew("malware.exe")
pyew.analyze()
pyew.disassemble()</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>สคริปต์สแกนตรวจสอบพฤติกรรมและความอันตรายของมัลแวร์ไบนารี:</p>
<ul>
<li><strong>Pyew</strong>: เป็นเครื่องมือแบบ Python Command Line สำหรับวิเคราะห์โค้ดช่องโหว่ความมั่นคงปลอดภัยของไฟล์ PE (Portable Executable)</li>
<li><strong>pyew.analyze()</strong>: สั่งรันวิเคราะห์หาลักษณะข้อมูลผิดปกติภายนอก เช่น การแกะโครงสร้างหัวตาราง (Import Table) และตรวจสอบการใช้ฟังก์ชันระดับล่างที่น่าสงสัย</li>
<li><strong>pyew.disassemble()</strong>: ถอดรหัสชุดคำสั่งไบนารีดิบให้กลายเป็นคำสั่งภาษาแอสเซมบลี เพื่อประเมินความปลอดภัยและสืบสวนหาเจตนารมณ์ความประพฤติมัลแวร์</li>
</ul>
</div>
</div>

<!-- 2. Radare2 (r2pipe) -->
<div id="panel-radare2" class="w-sand-panel">
<div class="w-sand-hdr"><span>2. Radare2 (r2pipe) Example</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import r2pipe
r = r2pipe.open("binary.exe")
disassembly = r.cmd("pd 10")  # Disassemble first 10 instructions
print(disassembly)</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>สคริปต์เชื่อมต่อควบคุม Radare2 เฟรมเวิร์กย้อนรอยระดับล่างประสิทธิภาพสูง:</p>
<ul>
<li><strong>r2pipe.open("binary.exe")</strong>: เปิดช่องท่อสื่อสาร (Pipe) และอิมพอร์ตดึงไฟล์ไบนารีเป้าหมายเข้าสู่เครื่องมือสแกน</li>
<li><strong>r.cmd("pd 10")</strong>: สั่งงานส่งคำสั่งภายในของ Radare2 โดยใช้คำสั่ง <code>pd 10</code> (Print Disassembly of 10 instructions) เพื่อสั่งถอดความและพิมพ์เอาท์พุตคำสั่งภาษาแอสเซมบลี 10 บรรทัดแรก</li>
</ul>
</div>
</div>

<!-- 3. View Python Bytecode -->
<div id="panel-pybytecode" class="w-sand-panel">
<div class="w-sand-hdr"><span>3. View Python Bytecode</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import dis
def example_function(a, b):
    return a + b
dis.dis(example_function)

# Output:
# 2           0 LOAD_FAST                0 (a)
#             2 LOAD_FAST                1 (b)
#             4 BINARY_ADD
#             6 RETURN_VALUE</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การวิเคราะห์โค้ดแปลรูปของภาษาโปรแกรม Python ในระดับ Bytecode:</p>
<ul>
<li><strong>import dis</strong>: เรียกใช้โมดูลวิเคราะห์และถอดความสถาปัตยกรรม Python (Disassembler for Python Bytecode)</li>
<li><strong>dis.dis(example_function)</strong>: แปลงตรรกะระดับสูงของฟังก์ชันให้เป็นคำสั่ง Assembly ของตัวแปลภาษาจำลอง (Python Virtual Machine - PVM)</li>
<li><strong>LOAD_FAST / BINARY_ADD</strong>: รหัสคำสั่งประมวลผล (Opcode) โดยดึงค่าตัวแปรเข้ามาใส่และประมวลผลบวกเลข</li>
</ul>
</div>
</div>

<!-- 4. Compile Code to Bytecode -->
<div id="panel-compilebyte" class="w-sand-panel">
<div class="w-sand-hdr"><span>4. Compile Code to Bytecode</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">code = compile("a + b", "&lt;string&gt;", "eval")
print(code.co_code)  # Raw bytecode bytes
# Output: b'e\x00e\x01\x17\x00S\x00'</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>คำนวณและสกัดข้อมูลภาษาเครื่องไบนารีดิบของไพธอน:</p>
<ul>
<li><strong>compile("a + b", ...)</strong>: สั่งทำการคอมไพล์โค้ดข้อความธรรมดาให้กลายเป็นวัตถุโค้ดพร้อมรัน (Code Object)</li>
<li><strong>code.co_code</strong>: แสดงผลและกู้ค่าในส่วน **ไบต์โค้ดดิบ (Raw Bytecode Bytes)** ซึ่งเก็บไว้ในอาร์เรย์ฐานสิบหก โดยเป็นรูปแบบเดียวกับที่มัลแวร์ประเภท Python-based (e.g. PyInstaller malware) มักใช้หลบเลี่ยงการตรวจสอบ</li>
</ul>
</div>
</div>

<!-- 5. Modifying Python Bytecode -->
<div id="panel-modbytecode" class="w-sand-panel">
<div class="w-sand-hdr"><span>5. Modifying Python Bytecode</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">from bytecode import Bytecode, Instr
bytecode = Bytecode([
    Instr("LOAD_CONST", 42),
    Instr("STORE_NAME", "x"),
    Instr("LOAD_NAME", "print"),
    Instr("LOAD_NAME", "x"),
    Instr("CALL_FUNCTION", 1),
    Instr("RETURN_VALUE")
])
code = bytecode.to_code()
exec(code)</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การเขียนโปรแกรมเขียนทับ แก้ไข และรันโค้ดระดับล่างแบบ Dynamic:</p>
<ul>
<li><strong>Bytecode([...])</strong>: โครงสร้างอาร์เรย์เก็บชุดคำสั่งควบคุมหน่วยความจำโดยตรงแบบมีระบบระเบียบ</li>
<li><strong>LOAD_CONST 42 / STORE_NAME "x"</strong>: สั่งโหลดเลข 42 เข้าหน่วยความจำและเก็บไว้ในตัวแปรชื่อ x</li>
<li><strong>exec(code)</strong>: สั่งประมวลผลวัตถุโค้ดจำลองระดับล่างแบบทันที ซึ่งในมิติความมั่นคงปลอดภัย ไซเบอร์มัลแวร์มักใช้แก้ไขโค้ดตัวเองในหน่วยความจำเพื่อหลบการตรวจจับ (Obfuscation / Self-modifying code)</li>
</ul>
</div>
</div>

</div>
</div>

<script>
window.showSandboxItem = function(itemKey, element) {
  const items = document.querySelectorAll('.w-sandbox-nav .w-nav-item');
  items.forEach(i => i.classList.remove('active'));
  element.classList.add('active');

  const panels = document.querySelectorAll('.w-sand-panel');
  panels.forEach(p => {
    p.style.setProperty('display', 'none', 'important');
  });

  const targetPanel = document.getElementById('panel-' + itemKey);
  if (targetPanel) {
    targetPanel.style.setProperty('display', 'block', 'important');
  }
}
</script>"""
})

# Block 3: Interactive Mini-Quiz 2 questions with Neon Gauge Bar
blocks_200.append({
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

<div id="mq-box-346" class="mini-quiz-box">
<!-- Question 1 -->
<div class="mq-q" data-correct="B">
<div class="mq-title"><span>Q1.</span> เครื่องมือทางความปลอดภัยประเภทใดที่ทำหน้าที่ในการแปลงข้อมูลภาษาเครื่อง (Machine Code) ย้อนกลับเป็นภาษาโปรแกรมระดับสูง (เช่น C) เพื่อให้อ่านเข้าใจง่ายขึ้น?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A" onclick="updateMiniProgress(346)"><span class="mini-bullet">A</span> Disassembler</div>
<div class="mini-opt" data-val="B" onclick="updateMiniProgress(346)"><span class="mini-bullet">B</span> Decompiler</div>
<div class="mini-opt" data-val="C" onclick="updateMiniProgress(346)"><span class="mini-bullet">C</span> Debugger</div>
</div>
</div>

<!-- Question 2 -->
<div class="mq-q" data-correct="A">
<div class="mq-title"><span>Q2.</span> การดักถอดโค้ดในโมดูล `dis` ของไพธอนแล้วแสดงค่า Opcodes (เช่น `LOAD_FAST`, `BINARY_ADD`) แสดงว่าเรากำลังถอดความซอร์สโค้ดให้อยู่ในรูปแบบใด?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A" onclick="updateMiniProgress(346)"><span class="mini-bullet">A</span> Python Bytecode</div>
<div class="mini-opt" data-val="B" onclick="updateMiniProgress(346)"><span class="mini-bullet">B</span> Native Machine Code</div>
<div class="mini-opt" data-val="C" onclick="updateMiniProgress(346)"><span class="mini-bullet">C</span> C++ Source Header</div>
</div>
</div>

<!-- Neon Gauge Bar Progress -->
<div class="mq-progress-container">
<div id="mq-progress-bar-346" class="mq-progress-bar"></div>
<span id="mq-progress-text-346" class="mq-progress-text">Lesson Progress: 0% (ยังไม่ผ่าน)</span>
</div>

<button class="mq-btn-check" onclick="checkMiniQuiz(346)">Check Answers / ตรวจคำตอบ</button>
<div id="mq-status-346" class="mq-status-bar"></div>
</div>

<script>
// Attach click listeners to manage selection state
document.querySelectorAll('#mq-box-346 .mini-opt').forEach(opt => {
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

# ─── 3. Save and Commit the New Lesson 200 into Database ───
new_lesson = TutorialLesson(
    id=200,
    module_id=34,
    title="06. ทักษะโปรแกรมมิ่งสำหรับการวิเคราะห์ย้อนรอยซอฟต์แวร์ (Programming Skills for Reverse Engineering)",
    content=json.dumps(blocks_200, ensure_ascii=False),
    position=6,
    challenge_id=None
)

db.session.add(new_lesson)
db.session.commit()
print("New Lesson 200 (06. Reverse Engineering) successfully created and committed!")
ctx.pop()
