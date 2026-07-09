import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l200 = db.session.query(TutorialLesson).filter_by(id=200).first()
blocks = json.loads(l200.content)

# ─── Upgrade Block 2 of Lesson 200 to include Live Flow Terminal Simulation ───
blocks[2]['value'] = """### 💻 Reverse Engineering Coding Sandbox (วิเคราะห์เจาะลึก 5 ตัวอย่างโค้ดย้อนรอย)

คลิกหัวข้อด้านซ้ายมือเพื่อตรวจสอบตัวอย่างโค้ดวิเคราะห์โครงสร้างข้อมูล และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลลัพธ์ผ่านเทอร์มินัลระบบ:

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
.w-sand-panel.active{display:block !important;}

.w-sand-hdr{font-size:0.95rem;font-weight:800;color:#ffffff;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:10px;margin-bottom:14px;display:flex;justify-content:between;align-items:center;}
.w-sand-hdr span.tag{font-size:0.65rem;padding:2px 8px;border-radius:4px;background:rgba(0,240,255,0.08);border:1px solid rgba(0,240,255,0.2);color:#00f0ff;font-family:'JetBrains Mono',monospace;}
.w-sand-code{font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#00f0ff;white-space:pre-wrap;margin:0 0 12px;background:rgba(0,0,0,0.2);padding:14px;border-radius:8px;border:1px solid rgba(255,255,255,0.02);}

/* Terminal box */
.w-sand-term-container{position:relative;background:#02040a;border:1px solid rgba(255,255,255,0.06);border-radius:8px;margin-bottom:16px;box-shadow:inset 0 2px 8px rgba(0,0,0,0.9);overflow:hidden;}
.w-sand-term-bar{background:rgba(255,255,255,0.03);padding:6px 12px;border-bottom:1px solid rgba(255,255,255,0.05);display:flex;justify-content:space-between;align-items:center;}
.w-sand-term-title{font-size:0.65rem;color:#64748b;font-weight:800;letter-spacing:0.06em;font-family:'JetBrains Mono',monospace;}
.w-sand-term-btn{background:rgba(0,240,255,0.1);border:1px solid rgba(0,240,255,0.3);border-radius:4px;color:#00f0ff;font-size:0.68rem;padding:3px 8px;cursor:pointer;font-family:'JetBrains Mono',monospace;font-weight:700;transition:all 0.15s ease;display:flex;align-items:center;gap:4px;}
.w-sand-term-btn:hover{background:#00f0ff;color:#02040a;box-shadow:0 0 8px rgba(0,240,255,0.4);}
.w-sand-term{font-family:'JetBrains Mono',monospace;font-size:0.76rem;color:#a7f3d0;padding:12px 16px;white-space:pre-wrap;min-height:90px;}
.w-sand-term span.prompt{color:#3ddc84;}
.w-sand-term span.cmd{color:#ffffff;font-weight:bold;}

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
<button id="nav-item-pyewdis" class="w-nav-item active" onclick="showSandboxItem('pyewdis', this)">1. Disassembly via Pyew</button>
<button id="nav-item-radare2" class="w-nav-item" onclick="showSandboxItem('radare2', this)">2. Radare2 (r2pipe)</button>
<button id="nav-item-pybytecode" class="w-nav-item" onclick="showSandboxItem('pybytecode', this)">3. View Python Bytecode</button>
<button id="nav-item-compilebyte" class="w-nav-item" onclick="showSandboxItem('compilebyte', this)">4. Compile Code to Bytecode</button>
<button id="nav-item-modbytecode" class="w-nav-item" onclick="showSandboxItem('modbytecode', this)">5. Modifying Python Bytecode</button>
</div>

<!-- Panel details right side -->
<div class="w-sandbox-panels">

<!-- 1. Pyew -->
<div id="panel-pyewdis" class="w-sand-panel">
<div class="w-sand-hdr"><span>1. Disassembly via Pyew</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">from pyew import Pyew
pyew = Pyew("malware.exe")
pyew.analyze()
pyew.disassemble()</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startReSim('pyewdis')">▶ Run Simulation</button>
</div>
<div id="term-pyewdis" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation ด้านขวาบนเพื่อจำลองการเรียกใช้งาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>สคริปต์สแกนตรวจสอบพฤติกรรมและความอันตรายของมัลแวร์ PE ไบนารี:</p>
<ul>
<li><strong>pyew.analyze()</strong>: รวบรวมข้อมูลจำเพาะ เช่น ส่วน Import table, แฮช MD5, และสกัดหาจุดประสงค์เชิงลึก</li>
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
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startReSim('radare2')">▶ Run Simulation</button>
</div>
<div id="term-radare2" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation ด้านขวาบนเพื่อจำลองการเรียกใช้งาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>สคริปต์เชื่อมต่อควบคุม Radare2 เฟรมเวิร์กย้อนรอยระดับล่างประสิทธิภาพสูง:</p>
<ul>
<li><strong>pd 10</strong>: สั่งแกะและแสดงคำสั่งแอสเซมบลีแรกจำนวน 10 แถวเพื่อหาทางกระโดดทิศทางรัน</li>
</ul>
</div>
</div>

<!-- 3. View Python Bytecode -->
<div id="panel-pybytecode" class="w-sand-panel">
<div class="w-sand-hdr"><span>3. View Python Bytecode</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import dis
def example_function(a, b):
    return a + b
dis.dis(example_function)</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startReSim('pybytecode')">▶ Run Simulation</button>
</div>
<div id="term-pybytecode" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation ด้านขวาบนเพื่อจำลองการเรียกใช้งาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การวิเคราะห์โค้ดแปลรูปของภาษาโปรแกรม Python ในระดับ Bytecode:</p>
<ul>
<li><strong>dis.dis()</strong>: ถอดรหัสตรรกะให้กลายเป็น Opcodes บนเครื่องจำลองไพธอน (PVM)</li>
</ul>
</div>
</div>

<!-- 4. Compile Code to Bytecode -->
<div id="panel-compilebyte" class="w-sand-panel">
<div class="w-sand-hdr"><span>4. Compile Code to Bytecode</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">code = compile("a + b", "&lt;string&gt;", "eval")
print(code.co_code)  # Raw bytecode bytes</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startReSim('compilebyte')">▶ Run Simulation</button>
</div>
<div id="term-compilebyte" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation ด้านขวาบนเพื่อจำลองการเรียกใช้งาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>คำนวณและสกัดข้อมูลภาษาเครื่องไบนารีดิบของไพธอน:</p>
<ul>
<li><strong>co_code</strong>: ดึงข้อมูลเลขดิบแบบฐานสิบหกซึ่งมักถูกใช้สกัดหรือประมวลผลหลบซ่อนความปลอดภัย</li>
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
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startReSim('modbytecode')">▶ Run Simulation</button>
</div>
<div id="term-modbytecode" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation ด้านขวาบนเพื่อจำลองการเรียกใช้งาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การเขียนโปรแกรมเขียนทับ แก้ไข และรันโค้ดระดับล่างแบบ Dynamic:</p>
<ul>
<li><strong>Self-modifying code</strong>: แก้ไขพฤติกรรมการรันของตัวเองแบบเรียลไทม์เพื่อซ่อนตรรกะพฤติกรรมในคอมพิวเตอร์</li>
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

// Auto render
setTimeout(() => {
  const activeBtn = document.querySelector('.w-sandbox-nav .w-nav-item.active');
  if (activeBtn) { activeBtn.click(); }
}, 100);

// Re Terminal Simulation
window.startReSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;

  term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">Disassembling binary headers...</span>\\n[.] Loading structures\\n[.] Printing instructions...';

  setTimeout(() => {
    if (itemKey === 'pyewdis') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 pyew_analyze.py</span>\\n[+] Size: 104448 bytes\\n[+] MD5: 8c6976e5b5410415bde908bd4dee15df\\n[+] Entry Point: 0x4010a0\\nDisassembling PE target...\\n0x004010a0:  push ebp\\n0x004010a1:  mov ebp, esp';
    } else if (itemKey === 'radare2') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 r2_pipe_scan.py</span>\\n0x004011a0  55             push rbp\\n0x004011a1  4889e5         mov rbp, rsp\\n0x004011a4  4883ec10       sub rsp, 0x10\\n0x004011a8  897dfc         mov dword [rbp - 4], edi\\n0x004011ab  e810ffffff     call 0x4010c0';
    } else if (itemKey === 'pybytecode') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 view_bytecode.py</span>\\n  2           0 LOAD_FAST                0 (a)\\n              2 LOAD_FAST                1 (b)\\n              4 BINARY_ADD\\n              6 RETURN_VALUE';
    } else if (itemKey === 'compilebyte') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 get_raw_bytecode.py</span>\\nb\\'e\\\\x00e\\\\x01\\\\x17\\\\x00S\\\\x00\\'';
    } else if (itemKey === 'modbytecode') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 modify_bytecode.py</span>\\n42';
    }
  }, 1000);
}
</script>"""

l200.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=200).update({"content": l200.content})
db.session.commit()
print("Lesson 200 Live Terminal Simulation successfully integrated!")
ctx.pop()
