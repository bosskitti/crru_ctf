import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l169 = db.session.query(TutorialLesson).filter_by(id=169).first()
blocks = json.loads(l169.content)

# ─── Replace Block 7 script with explicit JS style.display toggling ───
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

<pre id="code-python" class="w-code-body play-code-box" style="color:#00f0ff; display:block;">print('Hello World')</pre>
<pre id="code-java" class="w-code-body play-code-box" style="color:#fbbf24; display:none;">public class Test {
   public static void main(String[] args) {
      System.out.println("Hello World");
   }
}</pre>
<pre id="code-c" class="w-code-body play-code-box" style="color:#3ddc84; display:none;">#include &lt;stdio.h&gt;
int main() {
   printf("Hello World\\n");
   return 0;
}</pre>
<pre id="code-cpp" class="w-code-body play-code-box" style="color:#00f0ff; display:none;">#include &lt;iostream&gt;
using namespace std;
int main() {
   cout &lt;&lt; "Hello World" &lt;&lt; endl;
   return 0;
}</pre>
<pre id="code-asm64" class="w-code-body play-code-box" style="color:#ab20fd; display:none;">section .text
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
<pre id="code-asm32" class="w-code-body play-code-box" style="color:#ff007f; display:none;">extern printf
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

<pre id="term-python" class="w-code-body play-term-box" style="color:#94a3b8; display:block;">$ python3 Test.py
<span style="color:#3ddc84; font-weight:bold;">Hello World</span></pre>
<pre id="term-java" class="w-code-body play-term-box" style="color:#94a3b8; display:none;">$ javac Test.java
$ java Test
<span style="color:#3ddc84; font-weight:bold;">Hello World</span></pre>
<pre id="term-c" class="w-code-body play-term-box" style="color:#94a3b8; display:none;">$ gcc Test.c
$ ./a.out
<span style="color:#3ddc84; font-weight:bold;">Hello World</span></pre>
<pre id="term-cpp" class="w-code-body play-term-box" style="color:#94a3b8; display:none;">$ g++ Test.cpp
$ ./a.out
<span style="color:#3ddc84; font-weight:bold;">Hello World</span></pre>
<pre id="term-asm64" class="w-code-body play-term-box" style="color:#94a3b8; display:none;">$ nasm -f elf64 Test.asm
$ ld -o a.out Test.o
$ ./a.out
<span style="color:#3ddc84; font-weight:bold;">Hello World</span></pre>
<pre id="term-asm32" class="w-code-body play-term-box" style="color:#94a3b8; display:none;">$ nasm -f elf32 Test.asm
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

  // Explicitly set style.display to hide all code boxes
  const codes = document.querySelectorAll('.play-code-box');
  codes.forEach(c => {{
    c.style.setProperty('display', 'none', 'important');
  }});
  
  // Explicitly set style.display to show selected code box
  const targetCode = document.getElementById('code-' + key);
  if (targetCode) {{
    targetCode.style.setProperty('display', 'block', 'important');
  }}

  // Explicitly set style.display to hide all terminal boxes
  const terms = document.querySelectorAll('.play-term-box');
  terms.forEach(t => {{
    t.style.setProperty('display', 'none', 'important');
  }});
  
  // Explicitly set style.display to show selected terminal box
  const targetTerm = document.getElementById('term-' + key);
  if (targetTerm) {{
    targetTerm.style.setProperty('display', 'block', 'important');
  }}

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
print("Hello World playground fixed with explicit JS style.display style overrides!")
ctx.pop()
