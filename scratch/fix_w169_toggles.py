import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l169 = db.session.query(TutorialLesson).filter_by(id=169).first()
blocks = json.loads(l169.content)

# ─── 1. Rewrite Block 4 (Processing flows) using stable DOM Toggle ───
blocks[4]['value'] = """### ⚙️ Language Processing Workflows (การประมวลผลรันซอร์สโค้ด)

คลิกสลับแท็บภาษาเพื่อดูภาพกราฟิกโฟลวด้านล่างแสดงขั้นตอนการประมวลผล (Processing Flow) ของแต่ละภาษา:

<style>
.w-proc-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:18px;}
.w-proc-tabs{display:flex;gap:10px;justify-content:center;}
.w-proc-tab-btn{padding:8px 14px;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);border-radius:6px;font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#94a3b8;cursor:pointer;transition:all 0.15s ease;}
.w-proc-tab-btn:hover, .w-proc-tab-btn.active{border-color:#00f0ff;color:#ffffff;background:rgba(0,240,255,0.05);box-shadow:0 0 10px rgba(0,240,255,0.2);}

/* High-Fidelity Flow Box */
.w-proc-flow-box{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:28px;min-height:300px;display:flex;flex-direction:column;align-items:center;box-sizing:border-box;}
.w-flow-title{font-size:1.05rem;font-weight:800;color:#ffffff;margin:0 0 20px;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:10px;width:100%;text-align:center;}

/* Visual Flow Canvas */
.w-flow-canvas{display:none;align-items:center;justify-content:center;gap:16px;width:100%;margin:20px 0;flex-wrap:wrap;min-height:120px;}
.w-flow-canvas.active{display:flex;}

/* Graphical Nodes */
.g-node{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:12px 18px;border-radius:10px;border:1px solid;font-family:'JetBrains Mono',monospace;font-size:0.75rem;font-weight:800;text-align:center;box-shadow:0 4px 15px rgba(0,0,0,0.3);position:relative;min-width:110px;box-sizing:border-box;transition:all 0.25s ease;}
.g-node .g-icon{font-size:1.8rem;margin-bottom:6px;}
.g-node .g-lbl{font-size:0.65rem;text-transform:uppercase;color:#8a94a6;margin-top:2px;font-weight:700;letter-spacing:0.04em;}

/* Theme Colors */
.g-node.theme-src{border-color:#fbbf24;background:rgba(251,191,36,0.04);color:#fbbf24;}
.g-node.theme-proc{border-color:#00f0ff;background:rgba(0,240,255,0.04);color:#00f0ff;}
.g-node.theme-interm{border-color:#ab20fd;background:rgba(171,32,253,0.04);color:#ab20fd;}
.g-node.theme-out{border-color:#3ddc84;background:rgba(61,220,132,0.04);color:#3ddc84;}

/* Pulse glow effect on hover */
.g-node:hover{transform:translateY(-2px);box-shadow:0 8px 25px rgba(255,255,255,0.1);}
.g-node.theme-src:hover{box-shadow:0 0 15px rgba(251,191,36,0.35);border-color:#fbbf24;}
.g-node.theme-proc:hover{box-shadow:0 0 15px rgba(0,240,255,0.35);border-color:#00f0ff;}
.g-node.theme-interm:hover{box-shadow:0 0 15px rgba(171,32,253,0.35);border-color:#ab20fd;}
.g-node.theme-out:hover{box-shadow:0 0 15px rgba(61,220,132,0.35);border-color:#3ddc84;}

/* Neon Connectors */
.g-arrow{display:flex;flex-direction:column;align-items:center;color:#64748b;}
.g-arrow-line{width:36px;height:2px;background:rgba(255,255,255,0.15);position:relative;}
.g-arrow-line::after{content:"";position:absolute;right:0;top:-3px;width:0;height:0;border-top:4px solid transparent;border-bottom:4px solid transparent;border-left:6px solid rgba(255,255,255,0.35);}
.g-arrow-lbl{font-size:0.6rem;margin-top:4px;font-family:'JetBrains Mono',monospace;}

.w-flow-desc-box{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:16px;width:100%;box-sizing:border-box;}
.lang-flow-desc{display:none;font-size:0.86rem;color:#94a3b8;line-height:1.7;margin:0;}
.lang-flow-desc.active{display:block;}
.lang-flow-desc strong{color:#fbbf24;}
</style>

<div class="w-proc-wrap">
<div class="w-proc-tabs">
<button class="w-proc-tab-btn active" onclick="showProcFlow('python', this)">Python</button>
<button class="w-proc-tab-btn" onclick="showProcFlow('java', this)">Java</button>
<button class="w-proc-tab-btn" onclick="showProcFlow('cpp', this)">C / C++</button>
<button class="w-proc-tab-btn" onclick="showProcFlow('assembly', this)">Assembly</button>
</div>

<div class="w-proc-flow-box">
<h4 id="proc-title" class="w-flow-title">Python Language Processing (ระบบแปลแบบเรียลไทม์)</h4>

<!-- Python Flow -->
<div id="canvas-python" class="w-flow-canvas lang-flow-canvas active">
<div class="g-node theme-src">
<span class="g-icon">📄</span>
<span>Source Code</span>
<span class="g-lbl">Test.py</span>
</div>
<div class="g-arrow"><div class="g-arrow-line"></div><span class="g-arrow-lbl">Read</span></div>
<div class="g-node theme-proc">
<span class="g-icon">⚙️</span>
<span>Interpreter</span>
<span class="g-lbl">Line-by-line</span>
</div>
<div class="g-arrow"><div class="g-arrow-line"></div><span class="g-arrow-lbl">Execute</span></div>
<div class="g-node theme-out">
<span class="g-icon">🖥️</span>
<span>Output</span>
<span class="g-lbl">Hello World</span>
</div>
</div>

<!-- Java Flow -->
<div id="canvas-java" class="w-flow-canvas lang-flow-canvas">
<div class="g-node theme-src">
<span class="g-icon">📄</span>
<span>Source Code</span>
<span class="g-lbl">Test.java</span>
</div>
<div class="g-arrow"><div class="g-arrow-line"></div><span class="g-arrow-lbl">javac</span></div>
<div class="g-node theme-proc">
<span class="g-icon">📦</span>
<span>Compiler</span>
<span class="g-lbl">Translate</span>
</div>
<div class="g-arrow"><div class="g-arrow-line"></div><span class="g-arrow-lbl">Write</span></div>
<div class="g-node theme-interm">
<span class="g-icon">🪙</span>
<span>Byte Code</span>
<span class="g-lbl">Test.class</span>
</div>
<div class="g-arrow"><div class="g-arrow-line"></div><span class="g-arrow-lbl">Load</span></div>
<div class="g-node theme-proc">
<span class="g-icon">🌐</span>
<span>JVM</span>
<span class="g-lbl">Virtual Machine</span>
</div>
<div class="g-arrow"><div class="g-arrow-line"></div><span class="g-arrow-lbl">Run</span></div>
<div class="g-node theme-out">
<span class="g-icon">🖥️</span>
<span>Output</span>
<span class="g-lbl">Hello World</span>
</div>
</div>

<!-- C++ Flow -->
<div id="canvas-cpp" class="w-flow-canvas lang-flow-canvas">
<div class="g-node theme-src">
<span class="g-icon">📄</span>
<span>Source Code</span>
<span class="g-lbl">Test.c / .cpp</span>
</div>
<div class="g-arrow"><div class="g-arrow-line"></div><span class="g-arrow-lbl">Compile</span></div>
<div class="g-node theme-proc">
<span class="g-icon">📦</span>
<span>Compiler</span>
<span class="g-lbl">gcc / g++</span>
</div>
<div class="g-arrow"><div class="g-arrow-line"></div><span class="g-arrow-lbl">Output</span></div>
<div class="g-node theme-interm">
<span class="g-icon">⚙️</span>
<span>Object Code</span>
<span class="g-lbl">Test.o / .obj</span>
</div>
<div class="g-arrow"><div class="g-arrow-line"></div><span class="g-arrow-lbl">Link</span></div>
<div class="g-node theme-proc">
<span class="g-icon">🔗</span>
<span>Linker</span>
<span class="g-lbl">Include Libs</span>
</div>
<div class="g-arrow"><div class="g-arrow-line"></div><span class="g-arrow-lbl">Generate</span></div>
<div class="g-node theme-out">
<span class="g-icon">🚀</span>
<span>Executable</span>
<span class="g-lbl">a.out / .exe</span>
</div>
</div>

<!-- Assembly Flow -->
<div id="canvas-assembly" class="w-flow-canvas lang-flow-canvas">
<div class="g-node theme-src">
<span class="g-icon">📄</span>
<span>Source Code</span>
<span class="g-lbl">Test.asm</span>
</div>
<div class="g-arrow"><div class="g-arrow-line"></div><span class="g-arrow-lbl">nasm</span></div>
<div class="g-node theme-proc">
<span class="g-icon">🛠️</span>
<span>Assembler</span>
<span class="g-lbl">Translate CPU</span>
</div>
<div class="g-arrow"><div class="g-arrow-line"></div><span class="g-arrow-lbl">Output</span></div>
<div class="g-node theme-interm">
<span class="g-icon">⚙️</span>
<span>Object Code</span>
<span class="g-lbl">Test.o</span>
</div>
<div class="g-arrow"><div class="g-arrow-line"></div><span class="g-arrow-lbl">Link (ld)</span></div>
<div class="g-node theme-proc">
<span class="g-icon">🔗</span>
<span>Linker</span>
<span class="g-lbl">ld tool</span>
</div>
<div class="g-arrow"><div class="g-arrow-line"></div><span class="g-arrow-lbl">Output</span></div>
<div class="g-node theme-out">
<span class="g-icon">🚀</span>
<span>Executable</span>
<span class="g-lbl">a.out</span>
</div>
</div>

<!-- Descriptions -->
<div class="w-flow-desc-box">
<p id="desc-python" class="lang-flow-desc active">ระบบการประมวลผลของ Python ใช้แนวคิด **Interpretation** โดยตัวโปรแกรมจะส่งซอร์สโค้ดเข้าสู่ <strong>Interpreter</strong> เพื่อแปลและทำงานทีละบรรทัดจากบนลงล่างทันทีโดยไม่ต้องทำการแปลงโค้ดทั้งหมดเป็นไฟล์อื่นล่วงหน้า ช่วยให้นักวิเคราะห์สคริปต์แก้ไขและทดสอบสคริปต์เจาะระบบได้ยืดหยุ่นและรวดเร็ว</p>
<p id="desc-java" class="lang-flow-desc">ระบบของ Java ใช้แนวคิด **Hybrid Compilation**: ขั้นแรกจะทำการคอมไพล์โค้ดดั้งเดิมด้วยคำสั่ง <code>javac</code> ให้กลายเป็นไฟล์ระดับกลางที่เรียกว่า <strong>Byte Code (.class)</strong> ซึ่งไม่ใช่ภาษาเครื่องของซีพียูโดยตรง แต่เป็นภาษาของ <strong>Java Virtual Machine (JVM)</strong> ทำให้เมื่อนำไฟล์ Byte Code นี้ไปเปิดรันบนเครื่องใดๆ ที่ติดตั้ง JVM (เช่น Android OS หรือเซิร์ฟเวอร์องค์กร) จะทำงานได้เหมือนกันทันที</p>
<p id="desc-cpp" class="lang-flow-desc">ระบบของ C/C++ ใช้การ **Compile สู่ภาษาเครื่องโดยตรง (Native Compilation)**: ซอร์สโค้ดทั้งหมดจะถูกส่งให้คอมไพเลอร์ (เช่น <code>gcc</code> หรือ <code>g++</code>) แปลงรวดเดียวให้กลายเป็นไฟล์ <strong>Object Code</strong> จากนั้นโปรแกรม <strong>Linker</strong> จะทำการนำไลบรารีระบบและ Object Code มาผูกรวมกันกลายเป็นไฟล์รันระบบที่สมบูรณ์ (เช่น <code>a.out</code> ใน Linux หรือ <code>.exe</code> ใน Windows) ส่งรันบนดิสก์และแรมได้อย่างรวดเร็วถึงขีดสุด</p>
<p id="desc-assembly" class="lang-flow-desc">ระบบของ Assembly ทำการแปลตัวย่อคำสั่งระดับต่ำ (เช่น <code>mov</code>, <code>push</code>) ขึ้นตรงกับชิปสถาปัตยกรรมซีพียู ผ่านโปรแกรมแปลภาษาเครื่องระดับต่ำที่เรียกว่า <strong>Assembler (เช่น nasm)</strong> จนได้ Object Code แล้วส่งให้ตัวเชื่อมโยงระบบ <strong>Linker (ld)</strong> ทำการชี้ตำแหน่งเซกเตอร์ความปลอดภัยและจุดเริ่มต้น <code>_start</code> ของโปรแกรม ออกมาเป็นไฟล์รันสิทธิ์ระบบตรงโดยไม่มีระบบครอบแทรกแซง</p>
</div>
</div>
</div>

<script>
window.showProcFlow = function(key, element) {
  const buttons = document.querySelectorAll('.w-proc-tab-btn');
  buttons.forEach(b => b.classList.remove('active'));
  element.classList.add('active');

  const canvases = document.querySelectorAll('.lang-flow-canvas');
  canvases.forEach(c => c.classList.remove('active'));
  const targetCanvas = document.getElementById('canvas-' + key);
  if (targetCanvas) targetCanvas.classList.add('active');

  const descs = document.querySelectorAll('.lang-flow-desc');
  descs.forEach(d => d.classList.remove('active'));
  const targetDesc = document.getElementById('desc-' + key);
  if (targetDesc) targetDesc.classList.add('active');

  const titles = {
    'python': 'Python Language Processing (ระบบแปลแบบเรียลไทม์)',
    'java': 'Java Language Processing (ระบบรันข้ามแพลตฟอร์มด้วย JVM)',
    'cpp': 'C / C++ Language Processing (ระบบแปลภาษาเครื่องตรงประสิทธิภาพสูง)',
    'assembly': 'Assembly Language Processing (ระบบแปลชุดคำสั่งซีพียูระดับล่าง)'
  };
  document.getElementById('proc-title').textContent = titles[key] || '';
}
</script>"""


# ─── 2. Rewrite Block 7 (Hello World Playground) using stable DOM Toggle ───
blocks[7]['value'] = """### 💻 The Hello World Showdown

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
.w-code-body{font-family:'JetBrains Mono',monospace;font-size:0.82rem;white-space:pre-wrap;margin:0;}

/* Dynamic playground elements style */
.play-code-box, .play-term-box{display:none;}
.play-code-box.active, .play-term-box.active{display:block;}
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
<!-- Code Box -->
<div class="w-code-console" style="border-color:rgba(0,240,255,0.15);">
<div class="w-code-title">📄 Source Code: <span id="w-play-file" class="filename">Test.py</span></div>

<pre id="code-python" class="w-code-body play-code-box active" style="color:#00f0ff;">print('Hello World')</pre>
<pre id="code-java" class="w-code-body play-code-box" style="color:#fbbf24;">public class Test {
   public static void main(String[] args) {
      System.out.println("Hello World");
   }
}</pre>
<pre id="code-c" class="w-code-body play-code-box" style="color:#3ddc84;">#include &lt;stdio.h&gt;
int main() {
   printf("Hello World\\n");
   return 0;
}</pre>
<pre id="code-cpp" class="w-code-body play-code-box" style="color:#00f0ff;">#include &lt;iostream&gt;
using namespace std;
int main() {
   cout &lt;&lt; "Hello World" &lt;&lt; endl;
   return 0;
}</pre>
<pre id="code-asm64" class="w-code-body play-code-box" style="color:#ab20fd;">section .text
    global _start
_start:
    mov rax, 1          ; syscall: write
    mov rdi, 1          ; fd: stdout
    mov rsi, message    ; buffer address
    mov rdx, length     ; length
    syscall
    mov rax, 60         ; syscall: exit
    xor rdi, rdi        ; code 0
    syscall
section .data
message: db 'Hello World', 10
length: equ $ - message</pre>
<pre id="code-asm32" class="w-code-body play-code-box" style="color:#ff007f;">extern printf
section .text
    global main
main:
    push ebp
    mov ebp, esp
    push message
    call printf
    add esp, 4
    leave
    ret
section .data
message: db 'Hello World', 10</pre>
</div>

<!-- Run terminal -->
<div class="w-code-console" style="background:#070910;">
<div class="w-code-title">🐚 Terminal Compiler & Run Commands</div>

<pre id="term-python" class="w-code-body play-term-box active" style="color:#94a3b8;">$ python3 Test.py
<span style="color:#3ddc84; font-weight:bold;">Hello World</span></pre>
<pre id="term-java" class="w-code-body play-term-box" style="color:#94a3b8;">$ javac Test.java
$ java Test
<span style="color:#3ddc84; font-weight:bold;">Hello World</span></pre>
<pre id="term-c" class="w-code-body play-term-box" style="color:#94a3b8;">$ gcc Test.c
$ ./a.out
<span style="color:#3ddc84; font-weight:bold;">Hello World</span></pre>
<pre id="term-cpp" class="w-code-body play-term-box" style="color:#94a3b8;">$ g++ Test.cpp
$ ./a.out
<span style="color:#3ddc84; font-weight:bold;">Hello World</span></pre>
<pre id="term-asm64" class="w-code-body play-term-box" style="color:#94a3b8;">$ nasm -f elf64 Test.asm
$ ld -o a.out Test.o
$ ./a.out
<span style="color:#3ddc84; font-weight:bold;">Hello World</span></pre>
<pre id="term-asm32" class="w-code-body play-term-box" style="color:#94a3b8;">$ nasm -f elf32 Test.asm
$ gcc -m32 -no-pie -o a.out Test.o
$ ./a.out
<span style="color:#3ddc84; font-weight:bold;">Hello World</span></pre>
</div>
</div>
</div>

<script>
window.showPlayground = function(key, element) {
  const buttons = document.querySelectorAll('.w-play-tab-btn');
  buttons.forEach(b => b.classList.remove('active'));
  element.classList.add('active');

  // Show corresponding Code Block
  const codes = document.querySelectorAll('.play-code-box');
  codes.forEach(c => c.classList.remove('active'));
  const targetCode = document.getElementById('code-' + key);
  if (targetCode) targetCode.classList.add('active');

  // Show corresponding Terminal Block
  const terms = document.querySelectorAll('.play-term-box');
  terms.forEach(t => t.classList.remove('active'));
  const targetTerm = document.getElementById('term-' + key);
  if (targetTerm) targetTerm.classList.add('active');

  // Update File Name label
  const filenames = {
    'python': 'Test.py',
    'java': 'Test.java',
    'c': 'Test.c',
    'cpp': 'Test.cpp',
    'asm64': 'Test.asm (64-bit Linux)',
    'asm32': 'Test.asm (32-bit Linux)'
  };
  document.getElementById('w-play-file').textContent = filenames[key] || '';
}
</script>"""

l169.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=169).update({"content": l169.content})
db.session.commit()
print("DOM toggle system successfully implemented for both Block 4 and Block 7 in Lesson 169!")
ctx.pop()
