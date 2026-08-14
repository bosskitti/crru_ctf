import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l170 = db.session.query(TutorialLesson).filter_by(id=170).first()

# ─── Construct Premium Blocks for Lesson 170 ───
blocks_170 = []

# Block 0: Title & Introduction
blocks_170.append({
    "type": "markdown",
    "value": "## 🧠 ทักษะโปรแกรมมิ่งเพื่อการเขียนระบบอัตโนมัติและวิเคราะห์ช่องโหว่ (Programming Skills for Automation & Web)"
})

# Block 1: Interactive Programming Skill Map
blocks_170.append({
    "type": "markdown",
    "value": """### 🗺️ Cyber Security Programming Skill Map

การเขียนโปรแกรมเป็นทักษะแกนหลักที่ขาดไม่ได้ในงาน Cybersecurity และ Ethical Hacking เพื่อช่วยให้นักเจาะระบบสร้างเครื่องมือเฉพาะกิจ ทำงานอัตโนมัติ และสแกนช่องโหว่ได้อย่างลึกซึ้ง:

<style>
.w-skill-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:2rem auto;max-width:1050px;}
@media(max-width:820px){.w-skill-grid{grid-template-columns:repeat(2,1fr);}}
@media(max-width:550px){.w-skill-grid{grid-template-columns:1fr;}}
.w-skill-card{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:20px;box-sizing:border-box;transition:all 0.2s ease;}
.w-skill-card:hover{border-color:#00f0ff;background:rgba(0,240,255,0.02);transform:translateY(-2px);box-shadow:0 0 15px rgba(0,240,255,0.25);}
.w-skill-hdr{display:flex;align-items:center;gap:10px;margin-bottom:10px;}
.w-skill-icon{font-size:1.6rem;}
.w-skill-name{font-size:0.92rem;font-weight:800;color:#ffffff;}
.w-skill-desc{font-size:0.78rem;color:#94a3b8;line-height:1.6;margin:0;}
</style>

<div class="w-skill-grid">
<div class="w-skill-card">
<div class="w-skill-hdr"><span class="w-skill-icon">🤖</span><span class="w-skill-name">Automation</span></div>
<p class="w-skill-desc">เขียนสคริปต์เพื่อประมวลผลงานซ้ำๆ เช่น การลูปเดารหัสผ่าน หรือค้นหารายการโฟลเดอร์เว็บแบบอัตโนมัติ</p>
</div>
<div class="w-skill-card">
<div class="w-skill-hdr"><span class="w-skill-icon">🌐</span><span class="w-skill-name">Networking</span></div>
<p class="w-skill-desc">ทำความเข้าใจโปรโตคอล (TCP/IP, HTTP) และใช้ไลบรารีส่งแพ็กเก็ตจำลอง (เช่น Socket, Scapy) เพื่อสแกนระบบ</p>
</div>
<div class="w-skill-card">
<div class="w-skill-hdr"><span class="w-skill-icon">🕸️</span><span class="w-skill-name">Web Vulnerabilities</span></div>
<p class="w-skill-desc">ทำความเข้าใจการทำงานของโค้ดส่วนหน้าและระบบเซิร์ฟเวอร์หลังบ้านเพื่อวิเคราะห์ช่องโหว่ SQLi, XSS, CSRF</p>
</div>
<div class="w-skill-card">
<div class="w-skill-hdr"><span class="w-skill-icon">🔐</span><span class="w-skill-name">Cryptography</span></div>
<p class="w-skill-desc">ทำความเข้าใจสถาปัตยกรรมเข้ารหัส (AES, RSA) และการทำ hashing (SHA, MD5) เพื่อป้องกันและกู้คืนข้อมูล</p>
</div>
<div class="w-skill-card">
<div class="w-skill-hdr"><span class="w-skill-icon">🔎</span><span class="w-skill-name">Reverse Engineering</span></div>
<p class="w-skill-desc">แกะโครงสร้างไฟล์ไบนารีที่ไม่มีซอร์สโค้ดเพื่อค้นหาช่องโหว่ความเสถียรและวิเคราะห์พฤติกรรมมัลแวร์</p>
</div>
<div class="w-skill-card">
<div class="w-skill-hdr"><span class="w-skill-icon">💥</span><span class="w-skill-name">Exploit Dev</span></div>
<p class="w-skill-desc">วิเคราะห์ข้อผิดพลาดหน่วยความจำ (Buffer Overflow) และสร้างสคริปต์ควบคุมควบคุมระบบด้วยเครื่องมือเช่น Pwntools</p>
</div>
</div>"""
})

# Block 2: Brute-forcing Live Attack Simulation
blocks_170.append({
    "type": "markdown",
    "value": """### 🛡️ Brute-forcing & Automation Skills

**การรันระบบอัตโนมัติ (Automation)** นิยมใช้สำหรับการประมวลผลงานซ้ำๆ และกู้คืนรหัสผ่านด้วยกระบวนการ **Brute-forcing** ซึ่งจำลองการโจมตีพจนานุกรม (Dictionary Attack) โดยทดสอบคู่คำรหัสผ่านทั้งหมดจาก Wordlist จนกว่าจะเข้าระบบได้สำเร็จ:

<style>
.bf-console{background:#070910;border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:20px;max-width:1050px;margin:2rem auto;box-shadow:0 8px 24px rgba(0,0,0,0.5);box-sizing:border-box;}
.bf-header{display:flex;justify-content:between;align-items:center;border-bottom:1px solid rgba(255,255,255,0.08);padding-bottom:10px;margin-bottom:14px;}
.bf-title{font-family:'JetBrains Mono',monospace;font-size:0.82rem;color:#e2e8f0;font-weight:bold;}
.bf-title span{color:#00f0ff;}
.bf-btn{padding:6px 14px;background:#00f0ff;border:none;border-radius:4px;font-family:'JetBrains Mono',monospace;font-size:0.75rem;font-weight:800;color:#070910;cursor:pointer;}
.bf-btn:hover{background:#ffffff;}

.bf-table{width:100%;border-collapse:collapse;font-family:'JetBrains Mono',monospace;font-size:0.78rem;}
.bf-table th{text-align:left;color:#8a94a6;padding:8px;border-bottom:1px solid rgba(255,255,255,0.06);}
.bf-table td{padding:8px;color:#cbd5e1;}
.bf-status{font-weight:bold;}
.bf-status.trying{color:#fbbf24;}
.bf-status.failed{color:#ff007f;}
.bf-status.success{color:#3ddc84;text-shadow:0 0 8px rgba(61,220,132,0.45);}
</style>

<div class="bf-console">
<div class="bf-header">
<div class="bf-title">⚡ <span>Brute-force Live Attack Simulator</span></div>
<button id="run-bf-btn" class="bf-btn" onclick="startBruteForceSimulation()">Start Attack Simulation</button>
</div>
<table class="bf-table">
<thead>
<tr>
<th>Username</th>
<th>Password Attempt</th>
<th>Status</th>
</tr>
</thead>
<tbody id="bf-tbody">
<tr>
<td colspan="3" style="color:#64748b; text-align:center; padding:20px;">กดปุ่มเพื่อจำลองลำดับกระบวนการรันเจาะระบบแบบเรียลไทม์</td>
</tr>
</tbody>
</table>
</div>

<script>
let bfInterval = null;
window.startBruteForceSimulation = function() {
  const btn = document.getElementById('run-bf-btn');
  btn.disabled = true;
  btn.textContent = "Attacking...";

  const tbody = document.getElementById('bf-tbody');
  tbody.innerHTML = '';

  const wordlist = [
    { u: 'admin', p: 'a1234567', s: 'FAILED' },
    { u: 'admin', p: 'aa123456', s: 'FAILED' },
    { u: 'admin', p: 'aaa12345', s: 'FAILED' },
    { u: 'admin', p: 'aaaa1234', s: 'FAILED' },
    { u: 'admin', p: 'aaaaa123', s: 'SUCCESS' }
  ];

  let step = 0;
  
  if (bfInterval) clearInterval(bfInterval);

  bfInterval = setInterval(() => {
    if (step < wordlist.length) {
      const current = wordlist[step];
      
      // Update previous attempts to FAILED instantly
      const rows = tbody.querySelectorAll('tr');
      if (rows.length > 0) {
        const lastRow = rows[rows.length - 1];
        const statusTd = lastRow.querySelector('.bf-status');
        if (statusTd && statusTd.textContent === 'TRYING...') {
          statusTd.textContent = 'FAILED';
          statusTd.className = 'bf-status failed';
        }
      }

      // Add new row with TRYING status
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td>\${current.u}</td>
        <td>\${current.p}</td>
        <td class="bf-status trying">TRYING...</td>
      `;
      tbody.appendChild(tr);
      
      if (current.s === 'SUCCESS') {
        setTimeout(() => {
          const statusTd = tr.querySelector('.bf-status');
          statusTd.textContent = 'SUCCESS';
          statusTd.className = 'bf-status success';
          btn.disabled = false;
          btn.textContent = "Attack Done!";
          clearInterval(bfInterval);
        }, 600);
      }
      
      step++;
    }
  }, 900);
}
</script>"""
})

# Block 3: Interactive Categorized Coding Sandbox with Detailed Line-by-Line analysis
blocks_170.append({
    "type": "markdown",
    "value": """### 💻 Categorized Coding Sandbox (วิเคราะห์เจาะลึก 15 ตัวอย่างโค้ด)

เลือกหมวดหมู่และคลิกหัวข้อด้านซ้ายมือเพื่อตรวจสอบตัวอย่างชุดคำสั่ง (Code) และ **การวิเคราะห์การทำงานอย่างละเอียดในเชิงความปลอดภัยไซเบอร์ (Detailed Security Analysis)**:

<style>
.w-sandbox-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:16px;}
.w-sandbox-cat-tabs{display:flex;gap:8px;justify-content:center;}
.w-sandbox-cat-btn{padding:10px 16px;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);border-radius:6px;font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#94a3b8;cursor:pointer;transition:all 0.15s ease;}
.w-sandbox-cat-btn:hover, .w-sandbox-cat-btn.active{border-color:#00f0ff;color:#ffffff;background:rgba(0,240,255,0.05);box-shadow:0 0 10px rgba(0,240,255,0.15);}

.w-sandbox-main{display:flex;gap:20px;}
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

<div class="w-sandbox-wrap">
<!-- Category Buttons -->
<div class="w-sandbox-cat-tabs">
<button id="cat-btn-bf" class="w-sandbox-cat-btn active" onclick="switchSandboxCat('bf')">🛡️ Brute-force & Automation</button>
<button id="cat-btn-iter" class="w-sandbox-cat-btn" onclick="switchSandboxCat('iter')">🔁 Iteration & Loops</button>
<button id="cat-btn-rec" class="w-sandbox-cat-btn" onclick="switchSandboxCat('rec')">🔄 Recursion & Stack Logic</button>
</div>

<div class="w-sandbox-main">
<!-- Navigation Left Side -->
<div class="w-sandbox-nav">
<!-- Navs for Brute-force & Automation -->
<button class="w-nav-item item-bf active" onclick="showSandboxItem('crunch', this)">1. Crunch Wordlist Generator</button>
<button class="w-nav-item item-bf" onclick="showSandboxItem('itertools', this)">2. Itertools PIN Generator</button>
<button class="w-nav-item item-bf" onclick="showSandboxItem('delay', this)">3. Time Delay Controller</button>
<button class="w-nav-item item-bf" onclick="showSandboxItem('threading', this)">4. Multi-threading Execution</button>
<button class="w-nav-item item-bf" onclick="showSandboxItem('atmcode', this)">5. Local Command popen Brute</button>
<button class="w-nav-item item-bf" onclick="showSandboxItem('ssh', this)">6. Paramiko SSH Dictionary</button>
<button class="w-nav-item item-bf" onclick="showSandboxItem('zipfile', this)">7. Zipfile password crack</button>
<button class="w-nav-item item-bf" onclick="showSandboxItem('hashlib', this)">8. Hashlib MD5 Brute-force</button>
<button class="w-nav-item item-bf" onclick="showSandboxItem('partial', this)">9. Partial Rockyou MD5 Flag</button>

<!-- Navs for Iteration & Loops -->
<button class="w-nav-item item-iter" style="display:none;" onclick="showSandboxItem('primes', this)">1. Next Hundred Primes</button>
<button class="w-nav-item item-iter" style="display:none;" onclick="showSandboxItem('palindrome', this)">2. Longest Palindrome Checker</button>
<button class="w-nav-item item-iter" style="display:none;" onclick="showSandboxItem('fibo_stream', this)">3. Fibonacci ASCII stream</button>
<button class="w-nav-item item-iter" style="display:none;" onclick="showSandboxItem('matrix', this)">4. Matrix Multiplication</button>

<!-- Navs for Recursion & Logic -->
<button class="w-nav-item item-rec" style="display:none;" onclick="showSandboxItem('rec_print', this)">1. Stack PrintFun Tracer</button>
<button class="w-nav-item item-rec" style="display:none;" onclick="showSandboxItem('rec_fibo', this)">2. Fibonacci Recursion</button>
<button class="w-nav-item item-rec" style="display:none;" onclick="showSandboxItem('gcd_ngong', this)">3. C GCD Algorithm (Ngong)</button>
<button class="w-nav-item item-rec" style="display:none;" onclick="showSandboxItem('power_jeng', this)">4. Power of 2 (Jeng)</button>
<button class="w-nav-item item-rec" style="display:none;" onclick="showSandboxItem('permutation', this)">5. Permutation MD5 Flag</button>
<button class="w-nav-item item-rec" style="display:none;" onclick="showSandboxItem('binary_search', this)">6. Recursive Binary Search</button>
</div>

<!-- Panel details right side -->
<div class="w-sandbox-panels">

<!-- ==================== BRUTE-FORCE & AUTOMATION PANELS ==================== -->
<div id="panel-crunch" class="w-sand-panel active">
<div class="w-sand-hdr"><span>1. Crunch Wordlist Generator</span> <span class="tag">Kali Linux Command</span></div>
<pre class="w-sand-code" style="color:#fbbf24;">$ crunch 6 8 0123456789 -o wordlist.txt</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>คำสั่งระดับระบบปฏิบัติการสำหรับสร้างไฟล์พจนานุกรมเพื่อนำไปสแกนหาข้อผิดพลาดรหัสผ่าน:</p>
<ul>
<li><strong>crunch</strong>: เป็นเครื่องมือยอดนิยมใน Kali Linux สำหรับเจนเนอเรต Wordlist ตามรูปแบบตัวอักษรที่ต้องการ</li>
<li><strong>6 8</strong>: กำหนดช่วงความยาวของคำรหัสผ่านขั้นต่ำ 6 ตัวอักษร และสูงสุดไม่เกิน 8 ตัวอักษร</li>
<li><strong>0123456789</strong>: ชุดตัวอักษรที่จะนำมาผสมกัน ซึ่งตัวอย่างนี้จำกัดเฉพาะหมายเลขตัวเลขเท่านั้น</li>
<li><strong>-o wordlist.txt</strong>: เขียนบันทึกผลลัพธ์ทั้งหมดลงในไฟล์ปลายทางชื่อ wordlist.txt เพื่อใช้อ้างอิงเข้าโปรแกรมแฮกเกอร์ตัวอื่น</li>
</ul>
</div>
</div>

<div id="panel-itertools" class="w-sand-panel">
<div class="w-sand-hdr"><span>2. Itertools PIN Generator</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import itertools
for pin in itertools.product("0123456789", repeat=4):
    print("".join(pin))</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>ชุดคำสั่ง Python สำหรับเจนเนอเรตรหัส PIN ขนาด 4 หลักเพื่อเตรียมนำไปจำลองเจาะระบบตู้เอทีเอ็มหรือรหัสล็อกอิน:</p>
<ul>
<li><strong>import itertools</strong>: เรียกใช้งานไลบรารีเครื่องมือคำนวณเซ็ตตัวเลขประสิทธิภาพสูงใน Python</li>
<li><strong>itertools.product("...", repeat=4)</strong>: ทำหน้าที่คำนวณผลคูณคาร์ทีเซียนของสตริงตัวเลข "0-9" จำนวน 4 ชุด เพื่อแปลงเป็นคู่เลขทุกรูปแบบที่เป็นไปได้</li>
<li><strong>"".join(pin)</strong>: แปลงผลลัพธ์ที่เป็นทูเพิลตัวอักษรกลับมาเป็นข้อความเดี่ยว (เช่น <code>('0','1','2','3')</code> ➡ <code>"0123"</code>) รันเรียงตั้งแต่ <code>0000</code> ถึง <code>9999</code> รวม 10,000 รูปแบบ</li>
</ul>
</div>
</div>

<div id="panel-delay" class="w-sand-panel">
<div class="w-sand-hdr"><span>3. Time Delay Controller</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import time
time.sleep(1)  # Wait 1 second between attempts</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>คำสั่งสำคัญสำหรับการจำกัดความเร็วในการส่งข้อมูล (Rate Limiting) ในการเขียนโปรแกรมความปลอดภัย:</p>
<ul>
<li><strong>import time</strong>: เรียกใช้โมดูลจัดการเวลาของระบบปฏิบัติการ</li>
<li><strong>time.sleep(1)</strong>: สั่งหยุดการประมวลผลคำสั่งของเธรดนั้นๆ เป็นเวลา 1 วินาทีเต็ม เพื่อป้องกันไม่ให้โปรแกรมเดารหัสผ่านยิงข้อมูลงามถี่เกินไป ซึ่งอาจทำให้โดนระงับบัญชี (Locked out) หรือป้องกันอุปกรณ์ป้องกันเช่น Web Application Firewall (WAF) บล็อกหมายเลขไอพี</li>
</ul>
</div>
</div>

<div id="panel-threading" class="w-sand-panel">
<div class="w-sand-hdr"><span>4. Multi-threading Execution</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import threading
def brute_force(start, end):
    for i in range(start, end):
        print(f"Trying {i}")
threads = []
for i in range(0, 1000, 100):
    thread = threading.Thread(target=brute_force, args=(i, i + 100))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การเขียนโปรแกรมทำงานคู่ขนานผ่าน Multi-threading เพื่อเร่งความเร็วในการประมวลผล Brute-forcing:</p>
<ul>
<li><strong>import threading</strong>: การใช้ระบบประมวลผลคู่ขนานของตัวประมวลผลหลักคอมพิวเตอร์</li>
<li><strong>brute_force(start, end)</strong>: ฟังก์ชันรับหน้าที่สแกนทดสอบรหัสในช่วงของตนเอง</li>
<li><strong>threading.Thread(target=..., args=...)</strong>: สร้างเธรดย่อยขึ้นมาทำงาน โดยแบ่งกลุ่มเป้าหมาย เช่น เธรดที่ 1 รันช่วง 0-99, เธรดที่ 2 รันช่วง 100-199 พร้อมกัน</li>
<li><strong>thread.start() / thread.join()</strong>: สั่งเริ่มต้นการรัน และคอยคำสั่งจนกว่าทุกเธรดจะทำงานเสร็จสิ้นทั้งหมดก่อนสรุปผลลัพธ์</li>
</ul>
</div>
</div>

<div id="panel-atmcode" class="w-sand-panel">
<div class="w-sand-hdr"><span>5. Local Command popen Brute</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import os
for i in range(1, 1000000):
    process = os.popen('./atmcode ' + str(i))
    preprocessed = process.read().strip()
    print(i, preprocessed)
    if 'Invalid ATM Code' not in preprocessed:
        break
    process.close()</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การเดารหัสผ่านแอปพลิเคชันระบบท้องถิ่นโดยการตรวจสอบผลลัพธ์การตอบสนองผ่านท่อส่งคำสั่ง (Pipeline):</p>
<ul>
<li><strong>os.popen('./atmcode ' + str(i))</strong>: คำสั่งสั่งรันโปรแกรมไฟล์ไบนารีระดับล่างชื่อ <code>./atmcode</code> โดยแนบค่าตัวเลขเดารหัส `i` เข้าไปเป็นอาร์กิวเมนต์ผ่าน Shell</li>
<li><strong>process.read().strip()</strong>: อ่านผลลัพธ์ข้อความที่ซอฟต์แวร์นั้นวาดคืนกลับมาและทำการลบช่องว่างหัวท้าย</li>
<li><strong>if 'Invalid ATM Code' not in...</strong>: ตรวจหาคีย์เวิร์ดของข้อความตอบปฏิเสธ หากวันใดตัวแปร `preprocessed` ไม่มีคำว่า 'Invalid ATM Code' แสดงว่าตัวเลข PIN ดังกล่าวคือรหัสผ่านที่ถูกต้อง และจะรันคำสั่ง <code>break</code> เพื่อยุติลูปทันที</li>
</ul>
</div>
</div>

<div id="panel-ssh" class="w-sand-panel">
<div class="w-sand-hdr"><span>6. Paramiko SSH Dictionary</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import paramiko
def ssh_brute_force(host, username, wordlist):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for password in wordlist:
        try:
            ssh.connect(host, username=username, password=password, timeout=1)
            print(f"Success! Password: {password}")
            break
        except:
            print(f"Failed: {password}")
    ssh.close()
ssh_brute_force("192.168.1.10", "admin", ["admin", "password", "123456"])</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การเขียนสคริปต์เดารหัสผ่านเพื่อเข้าควบคุมเครื่องเซิร์ฟเวอร์เป้าหมายผ่านพอร์ตการสื่อสาร SSH:</p>
<ul>
<li><strong>import paramiko</strong>: ไลบรารี Python สำหรับจัดการระบบเครือข่ายความปลอดภัย SSHv2</li>
<li><strong>ssh.set_missing_host_key_policy(...)</strong>: ตั้งนโยบายให้ยอมรับกุญแจความปลอดภัยของเซิร์ฟเวอร์ที่ไม่เคยรู้จักมาก่อนโดยอัตโนมัติ</li>
<li><strong>ssh.connect(..., password=password, timeout=1)</strong>: พยายามรันเซสชันเข้าเชื่อมต่อตามหมายเลขไอพี หากพาสเวิร์ดไม่ถูกต้องจะยิง Error เข้าบล็อก <code>except</code> เพื่อรันคำรอบถัดไป หากถูกต้องจะไม่มี Error ทำให้โปรแกรมพิมพ์แจ้งความสำเร็จและ `break` สิ้นสุดลูป</li>
</ul>
</div>
</div>

<div id="panel-zipfile" class="w-sand-panel">
<div class="w-sand-hdr"><span>7. Zipfile password crack</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import zipfile
def crack_zip(zip_file, wordlist):
    with zipfile.ZipFile(zip_file) as zf:
        for password in wordlist:
            try:
                zf.extractall(pwd=password.encode())
                print(f"Success! Password: {password}")
                break
            except:
                print(f"Failed: {password}")
crack_zip("protected.zip", ["123456", "password", "qwerty"])</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การเจาะระบบเพื่อคลี่ไฟล์บีบอัด ZIP ที่ติดสิทธิ์การตั้งค่ารหัสผ่านป้องกันไว้:</p>
<ul>
<li><strong>import zipfile</strong>: โมดูลในการอ่านและเขียนวิเคราะห์โครงสร้างไฟล์บีบอัด</li>
<li><strong>zf.extractall(pwd=password.encode())</strong>: สั่งแตกไฟล์ออกทั้งหมด โดยใช้รหัสผ่านเดาในตัวแปร `password` ซึ่งจำเป็นต้องแปลงเป็นรูปแบบไบต์ (`.encode()`) เสมอสำหรับไฟล์ ZIP</li>
<li>ถ้าพาสเวิร์ดไม่ถูกต้องจะพังและไปรันลูปถัดไป ถ้าถอดรหัสผ่านได้ถูกต้องจะแตกไฟล์สำเร็จและบันทึกข้อความสรุป</li>
</ul>
</div>
</div>

<div id="panel-hashlib" class="w-sand-panel">
<div class="w-sand-hdr"><span>8. Hashlib MD5 Brute-force</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import hashlib
def crack_hash(target_hash, wordlist):
    for word in wordlist:
        hashed_word = hashlib.md5(word.encode()).hexdigest()
        if hashed_word == target_hash:
            print(f"Success! Password: {word}")
            break
crack_hash("5f4dcc3b5aa765d61d8327deb882cf99", ["password", "admin", "123456"])</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การกู้คืนรหัสผ่านจากลายนิ้วมือข้อมูล MD5 Hash ที่รั่วไหลมาจากฐานข้อมูล:</p>
<ul>
<li><strong>import hashlib</strong>: คลังฟังก์ชันคณิตศาสตร์เพื่อคำนวณรหัสความปลอดภัยประเภทแฮช</li>
<li><strong>hashlib.md5(word.encode()).hexdigest()</strong>: นำคำพจนานุกรมมาแปลงเป็นไบต์ แล้วรันคำนวณแฮช MD5 เพื่อให้ได้ผลลัพธ์เป็นอักษรเลขฐานสิบหก 32 อักขระ</li>
<li><strong>if hashed_word == target_hash</strong>: นำผลลัพธ์ไปเทียบตรงกับค่าแฮชเป้าหมาย หากตรงกันแสดงว่าเราค้นพบคำรหัสผ่านต้นฉบับสำเร็จแล้ว (เช่น <code>password</code> ➡ <code>5f4dcc3...</code>)</li>
</ul>
</div>
</div>

<div id="panel-partial" class="w-sand-panel">
<div class="w-sand-hdr"><span>9. Partial Rockyou MD5 Flag</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import hashlib
infile = open('rockyou.txt')
par_flag = 'a112ebef507c2ecd9755539aef75'
for w in infile:
    word = w.strip()
    hash_flag = hashlib.md5(word.encode('utf-8')).hexdigest()
    ful_flag = hash_flag[:-4]
    if par_flag == ful_flag:
        print(hash_flag, word)
        break
infile.close()</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>เทคนิคการกู้คืนข้อมูลแบบเทียบแฮชบางส่วน (Partial Match) ซึ่งมักพบในโจทย์ CTF หรือระบบสืบสวนคดีไซเบอร์:</p>
<ul>
<li><strong>infile = open('rockyou.txt')</strong>: เปิดคลังข้อมูลรหัสผ่านระดับสากลที่มีข้อมูลเกือบ 14 ล้านรายการ</li>
<li><strong>hash_flag[:-4]</strong>: การหั่นข้อความสตริงแฮช MD5 ออกโดยตัดตัวอักษร 4 หลักสุดท้ายทิ้งไป เพื่อเทียบรหัสบางส่วน</li>
<li><strong>if par_flag == ful_flag</strong>: เปรียบเทียบรหัสที่คัดทิ้งแล้วกับสตริงเป้าหมาย `par_flag` ซึ่งช่วยให้ค้นหารหัสผ่านต้นฉบับได้ แม้ระบบเป้าหมายจะปิดบังหลักแฮชท้ายไว้บางส่วนก็ตาม</li>
</ul>
</div>
</div>


<!-- ==================== ITERATION & LOOPS PANELS ==================== -->
<div id="panel-primes" class="w-sand-panel">
<div class="w-sand-hdr"><span>1. Next Hundred Primes</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">def is_prime(n):
    for i in range(2, n // 2):
        if n % i == 0:
            return False
    return True
n, i, s = 2784274, 0, ''
while i < 100:
    if is_prime(n):
        i += 1
        print(i, n)
        s += str(n)
    n += 1
print(s)</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>สคริปต์สแกนตรวจสอบคุณลักษณะจำนวนเฉพาะ (Prime Numbers) ซึ่งมักใช้ในระบบกุญแจเข้ารหัสลับ (e.g. RSA):</p>
<ul>
<li><strong>is_prime(n)</strong>: ฟังก์ชันตรวจสอบจำนวนเฉพาะด้วยการหารร่วม หากมีตัวใดในลูปหาร `n` ลงตัวจะคืนค่าเป็น `False` ทันที</li>
<li><strong>while i < 100</strong>: วนลูปประมวลผลไปเรื่อยๆ จนกว่าจะพบจำนวนเฉพาะครบ 100 ตัวถัดไป โดยสะสมผลลัพธ์เข้าสู่ตัวแปรข้อความ `s`</li>
</ul>
</div>
</div>

<div id="panel-palindrome" class="w-sand-panel">
<div class="w-sand-hdr"><span>2. Longest Palindrome Checker</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">def open_text(f):
    file = open(f)
    s = ''
    for line in file:
        s += line.strip()
    return s
def get_longest_palindrome(s):
    p = ''
    for i in range(1, len(s) + 1):
        for j in range(len(s) - i):
            if is_palindrome(s[j:j + i]):
                p = s[j:j + i]
    return p
def is_palindrome(s):
    return s == s[::-1]
print(get_longest_palindrome(open_text('palindrome.txt')))</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>สคริปต์ค้นหาคำหรือรูปแบบประโยคที่มีสัดส่วนสมมาตรย้อนกลับที่มีขนาดใหญ่ที่สุดในไฟล์ข้อความ:</p>
<ul>
<li><strong>is_palindrome(s)</strong>: ตรวจสอบคำโดยเปรียบเทียบข้อความแบบปกติกับรูปแบบย้อนหลัง `s[::-1]` (Slice operation)</li>
<li><strong>Nested loops (i & j)</strong>: ลูปซ้อนกันเพื่อไล่ตรวจสอบความยาวของชุดคำย่อย (Substring) ในระดับความยาวต่างๆ เพื่อค้นหาคำที่ยาวที่สุดที่เข้าเงื่อนไขสมมาตร</li>
</ul>
</div>
</div>

<div id="panel-fibo_stream" class="w-sand-panel">
<div class="w-sand-hdr"><span>3. Fibonacci ASCII stream</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">def fibo(n):
    f0, f1, fn = 0, 1, 0
    for i in range(2, n + 1):
        fn = f1 + f0
        f0 = f1
        f1 = fn
    return fn
flag = 'flag{0c382b8f95de6332183e123fe676ec58}'
stream = ''
for c in flag:
    stream += str(fibo(ord(c)))
print(stream)</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การนำตัวเลขลำดับฟีโบนัชชี (Fibonacci Sequence) มาใช้สร้างสตรีมตัวเลขรหัสผ่านจากตัวอักษรของ Flag:</p>
<ul>
<li><strong>ord(c)</strong>: ดึงรหัสตัวเลข ASCII ของตัวอักษรแต่ละตัวในแฟลกย่อย (เช่น อักษร 'f' มีค่า ASCII คือ 102)</li>
<li><strong>fibo(ord(c))</strong>: นำรหัส ASCII ตัวเลขนั้นมาหาผลลัพธ์ของฟีโบนัชชีในตำแหน่งที่กำหนด เพื่อนำค่าผลรวมสะสมมาป้อนต่อกันเป็นคีย์หลักในการส่งข้อมูล</li>
</ul>
</div>
</div>

<div id="panel-matrix" class="w-sand-panel">
<div class="w-sand-hdr"><span>4. Matrix Multiplication</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">def matrix_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    if cols_A != rows_B:
        raise ValueError("Incompatible dimensions.")
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>คำนวณการคูณเมทริกซ์ 2 มิติ ซึ่งถูกประยุกต์ใช้งานอย่างหนักในระบบกราฟิกความปลอดภัยและการเข้ารหัสลับข้อมูลขั้นสูง:</p>
<ul>
<li><strong>cols_A != rows_B</strong>: ป้องกันข้อผิดพลาดโดยตรวจสอบความยาวคอลัมน์ของตัวแปร A ต้องตรงกับแถวของตัวแปร B</li>
<li><strong>Nested loops 3 ชั้น</strong>: ใช้ลูปทำงานเรียงแถวและคอลัมน์เพื่อประมวลผลเชิงตัวเลขทีละชุดและเขียนลงในตำแหน่งผลลัพธ์</li>
</ul>
</div>
</div>


<!-- ==================== RECURSION & LOGIC PANELS ==================== -->
<div id="panel-rec_print" class="w-sand-panel">
<div class="w-sand-hdr"><span>1. Stack PrintFun Tracer</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">def printFun(test): 
    if (test < 1): 
        return
    else: 
        print(test, end = " ") 
        printFun(test-1) 
        print(test, end = " ") 
        return
test = 3
printFun(test)  # Output: 3 2 1 1 2 3</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>ตัวอย่างการติดตามพฤติกรรมทำงานหน่วยความจำแบบ Stack Frame ในการทำงานเวียนเกิด (Recursion):</p>
<ul>
<li><strong>if (test < 1)</strong>: เป็นเงื่อนไขหยุดการทำงานของลูปย้อนศร (Base Case) เพื่อป้องกันปัญหาลูปไม่มีสิ้นสุด</li>
<li><strong>การไหลของข้อมูล</strong>:
  1. สั่งรันครั้งแรก `test=3` พิมพ์ตัวเลข `3` แล้วเรียกใช้ตัวเองด้วย `test=2`
  2. ในระดับสอง พิมพ์ตัวเลข `2` แล้วเรียกใช้ตัวเองด้วย `test=1`
  3. ในระดับสาม พิมพ์ตัวเลข `1` แล้วเรียกใช้ตัวเองด้วย `test=0` (หลุด Base Case คืนค่ากลับ)
  4. จากนั้นคำสั่งจะคลี่ตัวย้อนออกจาก Stack ทำให้คำสั่ง `print(test)` บรรทัดที่สองรันย้อนกลับ พิมพ์ตัวเลข `1 2 3` ออกมาทางหน้าจอ</li>
</ul>
</div>
</div>

<div id="panel-rec_fibo" class="w-sand-panel">
<div class="w-sand-hdr"><span>2. Fibonacci Recursion</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">def fibonacci(n):
    if n == 0:  # Base case
        return 0
    elif n == 1:  # Base case
        return 1
    else:  # Recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(6))  # Output: 8</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การคำนวณจำนวนฟีโบนัชชีโดยใช้การเขียนโปรแกรมแบบเรียกตัวเอง:</p>
<ul>
<li><strong>Base cases (n==0, n==1)</strong>: ตัวแปรตรวจสอบจุดหยุดหลักของระบบ</li>
<li><strong>Recursive case</strong>: ฟังก์ชันจะทำการสั่งแยกสาขาการคำนวณเรียกตัวเองเป็น 2 กิ่งย่อยมาบวกกันในแต่ละระดับความสูง แม้จะเขียนโค้ดได้กระชับแต่มีประสิทธิภาพต่ำหากค่า N สูงเนื่องจากเกิดการคำนวณซ้ำซ้อนในสาขาหน่วยความจำ</li>
</ul>
</div>
</div>

<div id="panel-gcd_ngong" class="w-sand-panel">
<div class="w-sand-hdr"><span>3. C GCD Algorithm (Ngong)</span> <span class="tag">C Code</span></div>
<pre class="w-sand-code" style="color:#3ddc84;">int ngong(int x, int y) {
    if (x < y) {
        return ngong(y, x);
    } else if (x % y == 0) {
        return y;
    } else {
        return ngong(y, x % y);
    }
}</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>ฟังก์ชันในภาษา C ที่ใช้ระบบการรันคำสั่ง **Euclidean Algorithm** สำหรับการหาค่า ห.ร.ม. (Greatest Common Divisor) ของตัวเลขสองตัว:</p>
<ul>
<li><strong>x < y</strong>: หากตัวเลขหน้ามีค่าน้อยกว่าตัวเลขหลัง จะสั่งสลับตำแหน่งโดยเรียกฟังก์ชันย้อนกลับ</li>
<li><strong>x % y == 0</strong>: เงื่อนไขสิ้นสุดการทำงานเมื่อตัวเลขทั้งสองหารลงตัว จะส่งคืนคำตอบตัวหารค่านั้น</li>
<li><strong>ngong(y, x % y)</strong>: การหารเศษเหลือแบบ Recursive ซึ่งเป็นขั้นตอนคณิตศาสตร์ที่รวดเร็วมากในการแยกตัวประกอบร่วม</li>
</ul>
</div>
</div>

<div id="panel-power_jeng" class="w-sand-panel">
<div class="w-sand-hdr"><span>4. Power of 2 (Jeng)</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">def jeng(n):
    if n <= 0:
        return 1
    else:
        return jeng(n - 1) + jeng(n - 1)
# Checking 2 ** n == x</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>ฟังก์ชันจำลองพฤติกรรมการคำนวณเลขยกกำลัง 2 ของตัวเลข N:</p>
<ul>
<li><strong>jeng(n)</strong>: คืนค่าเป็นผลคูณทวีคูณเท่าตัว ($2^n$) ผ่านลูปบวกเพิ่มขึ้นสองข้างในระดับ recursive</li>
<li><strong>2 ** n == x</strong>: ตรวจสอบการเติบโตแบบ Exponential ในคณิตศาสตร์รหัสผ่านเพื่อหาตัวแปรเลขชี้กำลังที่มีขนาดบิตสูง</li>
</ul>
</div>
</div>

<div id="panel-permutation" class="w-sand-panel">
<div class="w-sand-hdr"><span>5. Permutation MD5 Flag</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import hashlib
code = []
def wow1(s):
    wow2('', s)
def wow2(p, s):
    if len(s) == 0:
        code.append(p)
    else:
        for i in range(len(s)):
            wow2(p + s[i], s[:i] + s[i+1:])
# Matching MD5 '6a5a825a191dd7be45d258641f1de3af'</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การเจนเนอเรตค่าการสลับจัดหมู่ (Permutations) ทุกรูปแบบของตัวอักษรเพื่อกู้รหัสผ่าน:</p>
<ul>
<li><strong>wow2(p, s)</strong>: ฟังก์ชันเวียนเกิดที่ทำการตัดอักษรทีละหลักจากกลุ่มข้อความเดิมมาประกอบใหม่ในตำแหน่ง `p` เพื่อทำสับเปลี่ยนตัวอักษร</li>
<li><strong>'RPCACTF'</strong>: เมื่อสับเปลี่ยนครบทั้งหมดจะได้รูปแบบที่เป็นไปได้ และนำไปตรวจจับหาแฮช MD5 เป้าหมายเพื่อดึงค่าคีย์ Flag ที่ถูกต้อง</li>
</ul>
</div>
</div>

<div id="panel-binary_search" class="w-sand-panel">
<div class="w-sand-hdr"><span>6. Recursive Binary Search</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">def binary_search(arr, target, low, high):
    if low > high:  # Base case: target not found
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:  # Base case: target found
        return mid
    elif arr[mid] > target:  # Recursive case: search left
        return binary_search(arr, target, low, mid - 1)
    else:  # Recursive case: search right
        return binary_search(arr, target, mid + 1, high)
# arr = [1, 3, 5, 7, 9]</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>อัลกอริทึมการค้นหาข้อมูลแบบทวิภาค (Binary Search) โดยการลดทอนขอบเขตข้อมูลทีละ 50%:</p>
<ul>
<li><strong>arr[mid] == target</strong>: ตรวจพบค่าข้อมูลเป้าหมายในตำแหน่งกึ่งกลางอาเรย์แล้วจะคืนค่าตำแหน่ง</li>
<li><strong>low > high</strong>: คืนค่า -1 หากไม่พบตัวเลขเป้าหมายหลังการสแกน</li>
<li><strong>arr[mid] > target</strong>: สั่งส่งสแกนตัดครึ่งข้อมูลฝั่งขวาทิ้งไปทั้งหมดแล้วสั่งค้นหาในฝั่งซ้ายซ้ำ ช่วยลดเวลาค้นหาได้รวดเร็วมาก</li>
</ul>
</div>
</div>

</div>
</div>
</div>

<script>
// Category switching logic
window.switchSandboxCat = function(catKey) {
  // Update buttons
  const buttons = document.querySelectorAll('.w-sandbox-cat-btn');
  buttons.forEach(b => b.classList.remove('active'));
  document.getElementById('cat-btn-' + catKey).classList.add('active');

  // Toggle Nav Item lists
  const navItems = document.querySelectorAll('.w-nav-item');
  navItems.forEach(n => n.style.display = 'none');

  const targets = document.querySelectorAll('.item-' + catKey);
  targets.forEach(t => t.style.display = 'block');

  // Click the first active navigation item in this category automatically
  if (targets.length > 0) {
    targets[0].click();
  }
}

// Sandbox Item switching logic
window.showSandboxItem = function(itemKey, element) {
  // Update active navigation class
  const items = document.querySelectorAll('.w-nav-item');
  items.forEach(i => i.classList.remove('active'));
  element.classList.add('active');

  // Switch display panel
  const panels = document.querySelectorAll('.w-sand-panel');
  panels.forEach(p => p.classList.remove('active'));

  const targetPanel = document.getElementById('panel-' + itemKey);
  if (targetPanel) {
    targetPanel.classList.add('active');
  }
}
</script>"""
})

# Block 4: Interactive Mini-Quiz 2 questions with Neon Gauge Bar
blocks_170.append({
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

<div id="mq-box-342" class="mini-quiz-box">
<!-- Question 1 -->
<div class="mq-q" data-correct="C">
<div class="mq-title"><span>Q1.</span> กลไกหรือกุญแจสำคัญข้อใดที่ช่วยปกป้องพอร์ตรหัสผ่านจากการโดนโจมตีเดาพาสเวิร์ด (Brute-forcing) แบบถี่ต่อเนื่องได้มีประสิทธิภาพที่สุด?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A" onclick="updateMiniProgress(342)"><span class="mini-bullet">A</span> การรันฟังก์ชัน Multi-threading ช่วยคัดกรองข้อมูล</div>
<div class="mini-opt" data-val="B" onclick="updateMiniProgress(342)"><span class="mini-bullet">B</span> การเปลี่ยนรูปแบบไปใช้พาสเวิร์ดที่มีเฉพาะตัวเลขล้วนเพื่อความจำง่าย</div>
<div class="mini-opt" data-val="C" onclick="updateMiniProgress(342)"><span class="mini-bullet">C</span> การจำกัดอัตราความเร็วและหน่วงเวลาส่งข้อมูล (Rate Limiting / time delay)</div>
</div>
</div>

<!-- Question 2 -->
<div class="mq-q" data-correct="B">
<div class="mq-title"><span>Q2.</span> ข้อจำกัดด้านหน่วยความจำ (Memory Limitation) ข้อใดที่อาจเกิดขึ้นหากฟังก์ชันเวียนเกิด (Recursion) รันเรียกตัวเองซ้ำเรื่อยๆ โดยไม่มีการหยุดหรือขีดจำกัดที่ปลอดภัย?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A" onclick="updateMiniProgress(342)"><span class="mini-bullet">A</span> เกิดช่องโหว่ประเภท SQL Injection บนพอร์ตเซิร์ฟเวอร์</div>
<div class="mini-opt" data-val="B" onclick="updateMiniProgress(342)"><span class="mini-bullet">B</span> หน่วยความจำส่วนเก็บข้อมูลเฟรมย้อนกลับเต็มขีดจำกัด (Stack Overflow)</div>
<div class="mini-opt" data-val="C" onclick="updateMiniProgress(342)"><span class="mini-bullet">C</span> โปรแกรมจะลดการใช้งานซีพียูลงเหลือ 0% และประมวลผลเร็วขึ้นชั่วคราว</div>
</div>
</div>

<!-- Neon Gauge Bar Progress -->
<div class="mq-progress-container">
<div id="mq-progress-bar-342" class="mq-progress-bar"></div>
<span id="mq-progress-text-342" class="mq-progress-text">Lesson Progress: 0% (ยังไม่ผ่าน)</span>
</div>

<button class="mq-btn-check" onclick="checkMiniQuiz(342)">Check Answers / ตรวจคำตอบ</button>
<div id="mq-status-342" class="mq-status-bar"></div>
</div>

<script>
// Attach click listeners to manage selection state
document.querySelectorAll('#mq-box-342 .mini-opt').forEach(opt => {
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

# ─── Save the new restructured content of Lesson 170 to Database ───
l170.content = json.dumps(blocks_170, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=170).update({"content": l170.content})
db.session.commit()
print("Lesson 170 content completely redesigned into high-fidelity premium blocks!")
ctx.pop()
