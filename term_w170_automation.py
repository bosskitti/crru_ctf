import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l170 = db.session.query(TutorialLesson).filter_by(id=170).first()
blocks = json.loads(l170.content)

# ─── Upgrade Block 3 (Code Sandbox of Lesson 170) to include Live Flow Terminal Simulation ───
blocks[3]['value'] = """### 💻 Automation Code Console (วิเคราะห์ 15 ตัวอย่างการรันอัตโนมัติ)

คลิกหัวข้อด้านซ้ายมือเพื่อตรวจสอบตัวอย่างโค้ดพื้นฐานการเขียนสคริปต์อัตโนมัติ และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลลัพธ์ผ่านเทอร์มินัลระบบ:

<style>
.w-sandbox-main{display:flex;gap:20px;margin:2rem auto;max-width:1050px;}
@media(max-width:820px){.w-sandbox-main{flex-direction:column;}}

.w-sandbox-nav{width:220px;display:flex;flex-direction:column;gap:6px;flex-shrink:0;max-height:500px;overflow-y:auto;padding-right:4px;}
@media(max-width:820px){.w-sandbox-nav{width:100%;flex-direction:row;flex-wrap:wrap;max-height:none;overflow-y:visible;}}
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
<button id="nav-item-iter_list" class="w-nav-item active" onclick="showSandboxItem('iter_list', this)">1. Iterating Lists</button>
<button id="nav-item-iter_dict" class="w-nav-item" onclick="showSandboxItem('iter_dict', this)">2. Iterating Dictionaries</button>
<button id="nav-item-iter_range" class="w-nav-item" onclick="showSandboxItem('iter_range', this)">3. Iterating Ranges</button>
<button id="nav-item-iter_nested" class="w-nav-item" onclick="showSandboxItem('iter_nested', this)">4. Nested Iteration</button>
<button id="nav-item-recur_fact" class="w-nav-item" onclick="showSandboxItem('recur_fact', this)">5. Recursion (Factorial)</button>
<button id="nav-item-recur_fibo" class="w-nav-item" onclick="showSandboxItem('recur_fibo', this)">6. Recursion (Fibonacci)</button>
<button id="nav-item-file_read" class="w-nav-item" onclick="showSandboxItem('file_read', this)">7. Reading Files</button>
<button id="nav-item-file_write" class="w-nav-item" onclick="showSandboxItem('file_write', this)">8. Writing Files</button>
<button id="nav-item-file_append" class="w-nav-item" onclick="showSandboxItem('file_append', this)">9. Appending Files</button>
<button id="nav-item-sys_args" class="w-nav-item" onclick="showSandboxItem('sys_args', this)">10. Command Line Arguments</button>
<button id="nav-item-json_parse" class="w-nav-item" onclick="showSandboxItem('json_parse', this)">11. Parsing JSON</button>
<button id="nav-item-try_except" class="w-nav-item" onclick="showSandboxItem('try_except', this)">12. Exception Handling</button>
<button id="nav-item-custom_func" class="w-nav-item" onclick="showSandboxItem('custom_func', this)">13. Declaring Functions</button>
<button id="nav-item-math_mod" class="w-nav-item" onclick="showSandboxItem('math_mod', this)">14. Math Module</button>
<button id="nav-item-os_system" class="w-nav-item" onclick="showSandboxItem('os_system', this)">15. OS command run</button>
</div>

<!-- Panel details right side -->
<div class="w-sandbox-panels">

<!-- 1. Iterating Lists -->
<div id="panel-iter_list" class="w-sand-panel">
<div class="w-sand-hdr"><span>1. Iterating Lists</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startAutoSim('iter_list')">▶ Run Simulation</button>
</div>
<div id="term-iter_list" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation เพื่อจำลองการทำงาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การวนลูปอ่านอาเรย์พื้นฐานเพื่อใช้ดึงข้อมูลรายการเป้าหมาย:</p>
<ul>
<li><strong>for fruit in fruits</strong>: วนซ้ำดักจับทีละสมาชิก เหมาะสำหรับวิเคราะห์รายการที่ได้จาก wordlist</li>
</ul>
</div>
</div>

<!-- 2. Iterating Dictionaries -->
<div id="panel-iter_dict" class="w-sand-panel">
<div class="w-sand-hdr"><span>2. Iterating Dictionaries</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">user_roles = {"admin": "root", "user1": "guest"}
for user, role in user_roles.items():
    print(f"User: {user} | Role: {role}")</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startAutoSim('iter_dict')">▶ Run Simulation</button>
</div>
<div id="term-iter_dict" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation เพื่อจำลองการทำงาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การวนลูปสแกนดิกชันนารีเก็บประวัติบัญชีผู้ใช้:</p>
<ul>
<li><strong>.items()</strong>: สกัดดึงทั้งกุญแจ (Key) และค่าเป้าหมาย (Value) พร้อมกัน</li>
</ul>
</div>
</div>

<!-- 3. Iterating Ranges -->
<div id="panel-iter_range" class="w-sand-panel">
<div class="w-sand-hdr"><span>3. Iterating Ranges</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">for i in range(1, 4):
    print(f"Attempt: {i}")</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startAutoSim('iter_range')">▶ Run Simulation</button>
</div>
<div id="term-iter_range" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation เพื่อจำลองการทำงาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การสร้างตัวสแกนจำนวนครั้งการทำงานแบบกำหนดช่วงคงตัว:</p>
<ul>
<li><strong>range(1, 4)</strong>: วนทำงานรอบที่ 1, 2, 3 (จำกัดสูงสุด 3 ครั้ง)</li>
</ul>
</div>
</div>

<!-- 4. Nested Iteration -->
<div id="panel-iter_nested" class="w-sand-panel">
<div class="w-sand-hdr"><span>4. Nested Iteration</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">users = ["admin", "user"]
passwords = ["123", "abc"]
for u in users:
    for p in passwords:
         print(f"Bypassing: {u} : {p}")</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startAutoSim('iter_nested')">▶ Run Simulation</button>
</div>
<div id="term-iter_nested" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation เพื่อจำลองการทำงาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การไขรหัสสลับคู่บัญชีและรหัสผ่าน (Brute-force matrix):</p>
<ul>
<li><strong>Nested loops</strong>: วนซ้อนลูปเพื่อลองจับคู่ข้อมูลทั้งหมดที่เป็นไปได้</li>
</ul>
</div>
</div>

<!-- 5. Recursion Factorial -->
<div id="panel-recur_fact" class="w-sand-panel">
<div class="w-sand-hdr"><span>5. Recursion (Factorial)</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startAutoSim('recur_fact')">▶ Run Simulation</button>
</div>
<div id="term-recur_fact" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation เพื่อจำลองการทำงาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การใช้ฟังก์ชันวนซ้ำแบบเรียกตัวเองประมวลผล (Recursive Function):</p>
<ul>
<li><strong>n == 1</strong>: เงื่อนไข Base Case ป้องกันไม่ให้โปรแกรมวนซ้ำจนเกิดช่องโหว่ Stack Overflow</li>
</ul>
</div>
</div>

<!-- 6. Recursion Fibonacci -->
<div id="panel-recur_fibo" class="w-sand-panel">
<div class="w-sand-hdr"><span>6. Recursion (Fibonacci)</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">def fibonacci(n):
    if n &lt;= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startAutoSim('recur_fibo')">▶ Run Simulation</button>
</div>
<div id="term-recur_fibo" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation เพื่อจำลองการทำงาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การคำนวณอนุกรมลำดับฟีโบนักชีแบบแตกกิ่งก้าน:</p>
<ul>
<li><strong>fibonacci(n-1) + fibonacci(n-2)</strong>: คำนวณแบบย้อนหลับไปขุดหาค่าก่อนหน้า 2 ตัว</li>
</ul>
</div>
</div>

<!-- 7. Reading Files -->
<div id="panel-file_read" class="w-sand-panel">
<div class="w-sand-hdr"><span>7. Reading Files</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">with open("passwords.txt", "r") as f:
    content = f.read()
    print(content)</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startAutoSim('file_read')">▶ Run Simulation</button>
</div>
<div id="term-file_read" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation เพื่อจำลองการทำงาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การเขียนโค้ดเปิดสแกนดูไฟล์ในเครื่องปลายทาง:</p>
<ul>
<li><strong>with open</strong>: บังคับปิดท่อเชื่อมต่อทรัพยากรอัตโนมัติเมื่อสิ้นสุดการใช้งาน ป้องกันบั๊ก Resource leaks</li>
</ul>
</div>
</div>

<!-- 8. Writing Files -->
<div id="panel-file_write" class="w-sand-panel">
<div class="w-sand-hdr"><span>8. Writing Files</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">with open("log.txt", "w") as f:
    f.write("System checked!")</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startAutoSim('file_write')">▶ Run Simulation</button>
</div>
<div id="term-file_write" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation เพื่อจำลองการทำงาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การล้างเขียนไฟล์ข้อมูลดิบแบบเคลียร์ข้อความเก่า:</p>
<ul>
<li><strong>"w" mode</strong>: เขียนทับข้อมูลของไฟล์เดิมทั้งหมดให้ว่างเปล่าและใส่ข้อความใหม่แทน</li>
</ul>
</div>
</div>

<!-- 9. Appending Files -->
<div id="panel-file_append" class="w-sand-panel">
<div class="w-sand-hdr"><span>9. Appending Files</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">with open("log.txt", "a") as f:
    f.write("\\nNew event detected!")</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startAutoSim('file_append')">▶ Run Simulation</button>
</div>
<div id="term-file_append" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation เพื่อจำลองการทำงาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การบันทึกประวัติการบุกรุกแบบยื่นเขียนต่อท้ายข้อความเดิม:</p>
<ul>
<li><strong>"a" mode</strong>: อัปเดตข้อมูลไฟล์โดยเขียนแทรกต่อท้ายบรรทัดเดิมเพื่อไม่ให้บันทึกเก่าสูญหาย</li>
</ul>
</div>
</div>

<!-- 10. Command Line Arguments -->
<div id="panel-sys_args" class="w-sand-panel">
<div class="w-sand-hdr"><span>10. Command Line Arguments</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import sys
print("Arguments list:", sys.argv)
if len(sys.argv) &gt; 1:
    print("Executing target IP:", sys.argv[1])</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startAutoSim('sys_args')">▶ Run Simulation</button>
</div>
<div id="term-sys_args" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation เพื่อจำลองการทำงาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การพัฒนาเครื่องมือรันคำสั่งโดยเปิดให้ผู้ใช้งานแนบตัวแปรมาตอนรันผ่าน CMD:</p>
<ul>
<li><strong>sys.argv</strong>: ดักจับรายการพารามิเตอร์ทั้งหมดที่ส่งมาตอนรันคำสั่ง</li>
</ul>
</div>
</div>

<!-- 11. Parsing JSON -->
<div id="panel-json_parse" class="w-sand-panel">
<div class="w-sand-hdr"><span>11. Parsing JSON</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import json
raw_data = '{"status": "ok", "port": 80}'
parsed = json.loads(raw_data)
print("Parsed Port:", parsed["port"])</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startAutoSim('json_parse')">▶ Run Simulation</button>
</div>
<div id="term-json_parse" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation เพื่อจำลองการทำงาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การแปลงข้อความรูปแบบ JSON ให้กลายเป็นพารามิเตอร์ตรรกะพร้อมใช้งาน:</p>
<ul>
<li><strong>json.loads</strong>: แปลงรูปแบบสตริงแบบมีระเบียบให้เข้าถึงฟิลด์ข้างในได้ทันที</li>
</ul>
</div>
</div>

<!-- 12. Exception Handling -->
<div id="panel-try_except" class="w-sand-panel">
<div class="w-sand-hdr"><span>12. Exception Handling</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startAutoSim('try_except')">▶ Run Simulation</button>
</div>
<div id="term-try_except" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation เพื่อจำลองการทำงาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การดักจับข้อผิดพลาดรันไทม์เพื่อรักษาความปลอดภัยระบบไม่ให้โปรแกรมหลุดพัง:</p>
<ul>
<li><strong>try-except</strong>: ป้องกันการพ่นข้อมูล Stack Trace และขวางไม่ให้แอปพลิเคชันค้าง</li>
</ul>
</div>
</div>

<!-- 13. Declaring Functions -->
<div id="panel-custom_func" class="w-sand-panel">
<div class="w-sand-hdr"><span>13. Declaring Functions</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">def verify_user(username):
    if username == "admin":
        return "Access Granted"
    return "Access Denied"
print(verify_user("admin"))</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startAutoSim('custom_func')">▶ Run Simulation</button>
</div>
<div id="term-custom_func" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation เพื่อจำลองการทำงาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การประกาศฟังก์ชันตรวจสอบสิทธิ์เฉพาะงานเพื่อความเป็นสัดส่วนข้อมูล:</p>
<ul>
<li><strong>def function_name()</strong>: ห่อหุ้มตรรกะระบบให้เรียกใช้งานซ้ำได้จากหลายช่องทาง</li>
</ul>
</div>
</div>

<!-- 14. Math Module -->
<div id="panel-math_mod" class="w-sand-panel">
<div class="w-sand-hdr"><span>14. Math Module</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import math
print("Square Root of 16 is:", math.sqrt(16))</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startAutoSim('math_mod')">▶ Run Simulation</button>
</div>
<div id="term-math_mod" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation เพื่อจำลองการทำงาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>เรียกใช้ฟังก์ชันคำนวณมาตรฐานประสิทธิภาพสูงของระบบ:</p>
<ul>
<li><strong>math.sqrt</strong>: สั่งคำนวณถอดค่ารากที่สองของตัวเลข</li>
</ul>
</div>
</div>

<!-- 15. OS Command Run -->
<div id="panel-os_system" class="w-sand-panel">
<div class="w-sand-hdr"><span>15. OS command run</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import os
# Run a terminal command
os.system("whoami")</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startAutoSim('os_system')">▶ Run Simulation</button>
</div>
<div id="term-os_system" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation เพื่อจำลองการทำงาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>คำสั่งสัญญาระดับล่างสั่งระบบปฏิบัติการรันระบบโดยตรง:</p>
<ul>
<li><strong>os.system()</strong>: ยื่นรันคำสั่งโดยตรงกับ Shell ระบบ เป็นช่องโหว่ประเภท Command Injection สูงหากนำอินพุตดิบจากผู้ใช้เข้ามาใส่</li>
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

// Automation Simulation logic
window.startAutoSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;

  term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 script.py</span>\\n[.] Executing automatic commands...';

  setTimeout(() => {
    if (itemKey === 'iter_list') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 list_iter.py</span>\\napple\\nbanana\\ncherry';
    } else if (itemKey === 'iter_dict') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 dict_iter.py</span>\\nUser: admin | Role: root\\nUser: user1 | Role: guest';
    } else if (itemKey === 'iter_range') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 range_iter.py</span>\\nAttempt: 1\\nAttempt: 2\\nAttempt: 3';
    } else if (itemKey === 'iter_nested') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 brute_matrix.py</span>\\nBypassing: admin : 123\\nBypassing: admin : abc\\nBypassing: user : 123\\nBypassing: user : abc';
    } else if (itemKey === 'recur_fact') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 factorial.py</span>\\n120';
    } else if (itemKey === 'recur_fibo') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 fibonacci.py</span>\\n8';
    } else if (itemKey === 'file_read') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 read_pass.py</span>\\n[+] passwords.txt contents:\\nadmin123\\npassword321\\nroot_pass_key';
    } else if (itemKey === 'file_write') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 write_file.py</span>\\n[+] Saved to log.txt successfully.';
    } else if (itemKey === 'file_append') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 append_file.py</span>\\n[+] Log entries appended successfully.';
    } else if (itemKey === 'sys_args') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 exploit.py 192.168.1.100</span>\\nArguments list: [\\'exploit.py\\', \\'192.168.1.100\\']\\nExecuting target IP: 192.168.1.100';
    } else if (itemKey === 'json_parse') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 parse_json.py</span>\\nParsed Port: 80';
    } else if (itemKey === 'try_except') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 error_handling.py</span>\\nCannot divide by zero!';
    } else if (itemKey === 'custom_func') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 check_auth.py</span>\\nAccess Granted';
    } else if (itemKey === 'math_mod') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 math_calc.py</span>\\nSquare Root of 16 is: 4.0';
    } else if (itemKey === 'os_system') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 run_whoami.py</span>\\nkali';
    }
  }, 1000);
}
</script>"""

l170.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=170).update({"content": l170.content})
db.session.commit()
print("Lesson 170 Automation Sandbox Live Simulation integrated successfully!")
ctx.pop()
