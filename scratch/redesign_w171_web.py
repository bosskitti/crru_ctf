import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l171 = db.session.query(TutorialLesson).filter_by(id=171).first()

# ─── 1. Construct Premium Blocks for Lesson 171 ───
blocks_171 = []

# Block 0: Title & Header
blocks_171.append({
    "type": "markdown",
    "value": "## 🕸️ ทักษะโปรแกรมมิ่งสำหรับการวิเคราะห์เว็บและดีไซน์ปลอดภัย (Programming Skills for Web Vulnerabilities & SSDLC)"
})

# Block 1: Web Application Architecture (with the embedded image)
blocks_171.append({
    "type": "markdown",
    "value": """### 🏢 Web Application Architecture & Protocols

การตรวจสอบความปลอดภัยของเว็บแอปพลิเคชัน (Web Security) จำเป็นต้องมีความรู้ความเข้าใจในโครงสร้างสถาปัตยกรรม 3 ระดับหลัก (Three-Tier Architecture) และกระบวนการแลกเปลี่ยนข้อมูลผ่านโปรโตคอล HTTP:

![Web Application Architecture](/home/kali/.gemini/antigravity/brain/c824c6d8-15e7-4399-b27b-1656c82fe65a/media__1783560903040.png)

<style>
.web-arch-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:2rem auto;max-width:1050px;}
@media(max-width:768px){.web-arch-grid{grid-template-columns:1fr;}}
.web-arch-card{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:20px;box-sizing:border-box;transition:all 0.25s ease;}
.web-arch-card:hover{border-color:#00f0ff;background:rgba(0,240,255,0.02);transform:translateY(-2px);box-shadow:0 0 15px rgba(0,240,255,0.25);}
.web-arch-title{font-size:0.92rem;font-weight:800;color:#00f0ff;margin-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.05);padding-bottom:6px;}
.web-arch-desc{font-size:0.8rem;color:#94a3b8;line-height:1.65;margin:0;}
.web-arch-desc strong{color:#fbbf24;}
</style>

<div class="web-arch-grid">
<div class="web-arch-card">
<div class="web-arch-title">🌐 Web Front-End</div>
<p class="web-arch-desc">ส่วนนำเสนอผลลัพธ์บนเครื่องของฝั่งผู้ใช้ (Client-Side) เขียนด้วย <strong>HTML, CSS, JavaScript</strong> หน้าที่ทางความปลอดภัยคือตรวจสอบโครงสร้างหน้าเว็บและพฤติกรรมสคริปต์สิทธิ์สูง</p>
</div>
<div class="web-arch-card">
<div class="web-arch-title">⚙️ Web Back-End</div>
<p class="web-arch-desc">ส่วนประมวลผลคำขอระดับระบบเซิร์ฟเวอร์ (Server-Side) เช่น <strong>PHP, Python, Node.js</strong> ทำหน้าที่กรองข้อมูลอินพุตของผู้ใช้ จัดการเซสชันล็อกอิน และคุ้มครองไฟล์บนเว็บเซิร์ฟเวอร์</p>
</div>
<div class="web-arch-card">
<div class="web-arch-title">🗄️ Web Database</div>
<p class="web-arch-desc">ส่วนจัดเก็บข้อมูลหลักและประวัติบัญชี (Database Server) ด้วยภาษา <strong>SQL</strong> (MySQL, PostgreSQL) หากแอปพลิเคชันไม่กรองโค้ดอินพุตที่ดี จะส่งผลให้โดนโจมตีช่องโหว่ SQL Injection ได้</p>
</div>
</div>"""
})

blocks_171.append({"type": "markdown", "value": "---"})

# Block 2: HTTP Protocol & Web Servers
blocks_171.append({
    "type": "markdown",
    "value": """### 📄 HTTP Protocol & Web Servers

- **HTTP/HTTPS**: ทำความเข้าใจรอบคำขอและคำตอบกลับ (Request/Response Cycle), โครงสร้าง HTTP Headers (เช่น User-Agent, Content-Type), คุกกี้ (Cookies) เพื่อควบคุมการเก็บล็อกอิน และเมธอดคำขอหลัก ได้แก่ **GET** (ดึงข้อมูล), **POST** (ส่งข้อมูลใหม่), **PUT** (แก้ไข), และ **DELETE** (ลบข้อมูล)
- **Web Servers**: ความคุ้นเคยและเข้าใจระบบตั้งค่าเว็บเซิร์ฟเวอร์ เช่น **Apache, Nginx, IIS** ซึ่งการตั้งค่าความปลอดภัยที่บกพร่อง (Misconfigured headers) อาจเปิดช่องทางให้เกิดช่องโหว่ความเสถียรระบบหลักได้"""
})

blocks_171.append({"type": "markdown", "value": "---"})

# Block 3: Categorized Code Console with Detailed Line-by-Line analysis
blocks_171.append({
    "type": "markdown",
    "value": """### 💻 Web Vulnerability Coding Console (วิเคราะห์ 4 ตัวอย่างโค้ดเว็บ)

คลิกหัวข้อด้านซ้ายมือเพื่อตรวจสอบตัวอย่างโค้ดการจัดการคำขอเว็บ (Code) และ **การวิเคราะห์การทำงานอย่างละเอียดในเชิงความปลอดภัยไซเบอร์ (Detailed Security Analysis)**:

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
<button class="w-nav-item active" onclick="showSandboxItem('readhtml', this)">1. Reading HTML & BeautifulSoup</button>
<button class="w-nav-item" onclick="showSandboxItem('readheaders', this)">2. Read HTTP Headers</button>
<button class="w-nav-item" onclick="showSandboxItem('postbrute', this)">3. POST Login Brute-forcing</button>
<button class="w-nav-item" onclick="showSandboxItem('getbrute', this)">4. GET Login Brute-forcing</button>
</div>

<!-- Panel details right side -->
<div class="w-sandbox-panels">

<!-- 1. Reading HTML -->
<div id="panel-readhtml" class="w-sand-panel active">
<div class="w-sand-hdr"><span>1. Reading HTML & BeautifulSoup</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "lxml")
print("Page Title:", soup.title.string)
print(soup.prettify())</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>สคริปต์สแกนดึงข้อมูลเว็บเพจภายนอกเพื่อวิเคราะห์และถอดโครงสร้าง:</p>
<ul>
<li><strong>requests.get(url)</strong>: ส่งแพ็กเก็ต HTTP GET Request ไปยังเซิร์ฟเวอร์เป้าหมายเพื่อดึงเนื้อหาเว็บ</li>
<li><strong>BeautifulSoup(html_content, "lxml")</strong>: เรียกใช้ตัววิเคราะห์ไวยากรณ์ (HTML Parser) เพื่อจัดระเบียบเนื้อหาให้พร้อมสืบค้นแท็กภายใน</li>
<li><strong>soup.title.string</strong>: ดึงข้อความที่อยู่ระหว่างแท็ก <code>&lt;title&gt;...&lt;/title&gt;</code> เพื่อตรวจสอบรายละเอียดหัวเรื่องของเว็บแอปพลิเคชันอย่างรวดเร็ว</li>
<li><strong>soup.prettify()</strong>: จัดย่อหน้าข้อความซอร์สโค้ด HTML ใหม่ให้อ่านเข้าใจง่าย เหมาะสำหรับใช้ตรวจสอบหาฟิลด์อินพุตที่ซ่อนอยู่ (Hidden fields)</li>
</ul>
</div>
</div>

<!-- 2. Read Headers -->
<div id="panel-readheaders" class="w-sand-panel">
<div class="w-sand-hdr"><span>2. Read HTTP Headers</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import requests
response = requests.get('https://www.example.com')
for key, value in response.headers.items():
    print(f"{key}: {value}")</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>สคริปต์สแกนวิเคราะห์ HTTP Response Headers เพื่อประเมินความปลอดภัยของเว็บเซิร์ฟเวอร์:</p>
<ul>
<li><strong>response.headers.items()</strong>: ดึงรายการส่วนหัวของการตอบกลับจากเซิร์ฟเวอร์</li>
<li><strong>บทวิเคราะห์ความปลอดภัย</strong>: ใช้สำหรับตรวจสอบว่าเว็บเซิร์ฟเวอร์เปิดใช้งานระบบป้องกันสิทธิ์สูงครบถ้วนหรือไม่ เช่น <code>X-Frame-Options</code> (ป้องกัน Clickjacking), <code>Content-Security-Policy</code> (ป้องกัน XSS), หรือตรวจสอบข้อมูลเทคโนโลยีหลังบ้านผ่านฟิลด์ <code>Server</code> (เช่น Apache/Nginx รุ่นที่มีช่องโหว่)</li>
</ul>
</div>
</div>

<!-- 3. POST Login Brute-forcing -->
<div id="panel-postbrute" class="w-sand-panel">
<div class="w-sand-hdr"><span>3. POST Login Brute-forcing</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import requests
url = "http://example.com/login"
wordlist = ["admin", "password", "123456", "qwerty"]
for password in wordlist:
    response = requests.post(url, data={"username": "admin", "password": password})
    if "Login failed" not in response.text:
        print(f"Success! Password: {password}")
        break</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>สคริปต์เดารหัสผ่านผ่านฟอร์มเข้าสู่ระบบด้วยเมธอดส่งข้อมูลแบบ POST:</p>
<ul>
<li><strong>requests.post(..., data=...)</strong>: จำลองการยื่นส่งข้อมูลแบบ HTTP POST โดยส่งพารามิเตอร์รหัสผ่านไปในกล่อง Body (เลียนแบบการกดปุ่ม Login ของมนุษย์)</li>
<li><strong>if "Login failed" not in response.text</strong>: ดักจับและวิเคราะห์ผลลัพธ์ข้อความจากเซิร์ฟเวอร์ หากวันใดไม่ปรากฏคีย์เวิร์ดข้อความปฏิเสธการเข้าระบบ แสดงว่ารหัสผ่านดังกล่าวถูกต้องและให้รันคำสั่ง <code>break</code> เพื่อจบลูปทันที</li>
</ul>
</div>
</div>

<!-- 4. GET Login Brute-forcing -->
<div id="panel-getbrute" class="w-sand-panel">
<div class="w-sand-hdr"><span>4. GET Login Brute-forcing</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import requests
url = "http://example.com/login"
usernames = ["admin", "user", "test"]
passwords = ["12345", "password", "admin123"]

for username in usernames:
    for password in passwords:
        params = {"username": username, "password": password}
        response = requests.get(url, params=params)
        if "Welcome" in response.text or response.status_code == 200:
            print(f"Success! Username: {username} | Password: {password}")
            break
        else:
            print(f"Failed attempt: Username: {username} | Password: {password}")</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>สคริปต์โจมตีเดารหัสผ่านโดยใช้วิธีแนบตัวแปรไปกับพาธที่อยู่ URL ด้วยเมธอด GET:</p>
<ul>
<li><strong>requests.get(..., params=params)</strong>: ส่งข้อมูลการเชื่อมต่อแบบ GET โดยแนบตัวแปรไปท้าย URL (เช่น <code>http://example.com/login?username=admin&password=12345</code>)</li>
<li><strong>"Welcome" in response.text or status_code == 200</strong>: วิเคราะห์ข้อความในระบบของหน้าเพจเพื่อยืนยันสิทธิ์ความปลอดภัยการเข้าสู่ระบบที่ถูกต้อง</li>
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

# Block 4: Interactive Mini-Quiz 2 questions with Neon Gauge Bar
blocks_171.append({
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

<div id="mq-box-344" class="mini-quiz-box">
<!-- Question 1 -->
<div class="mq-q" data-correct="C">
<div class="mq-title"><span>Q1.</span> ส่วนหัวของการตอบกลับเครือข่ายข้อใด (HTTP Headers) ที่ระบุกำหนดค่าตั้งค่ายืนยันตัวตน เพื่อควบคุมและกู้ข้อมูลเซสชันล็อกอินของเบราว์เซอร์ฝั่งผู้ใช้?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A" onclick="updateMiniProgress(344)"><span class="mini-bullet">A</span> User-Agent</div>
<div class="mini-opt" data-val="B" onclick="updateMiniProgress(344)"><span class="mini-bullet">B</span> Content-Type</div>
<div class="mini-opt" data-val="C" onclick="updateMiniProgress(344)"><span class="mini-bullet">C</span> Set-Cookie</div>
</div>
</div>

<!-- Question 2 -->
<div class="mq-q" data-correct="B">
<div class="mq-title"><span>Q2.</span> การดึงค่าและใช้ไลบรารี BeautifulSoup ร่วมกับ requests ใน Python มีวัตถุประสงค์หลักข้อใดในขั้นตอนวิเคราะห์เว็บ?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A" onclick="updateMiniProgress(344)"><span class="mini-bullet">A</span> คอมไพล์ซอร์สโค้ดของหลังบ้านให้กลายเป็นภาษาเครื่องเพื่อการยกรันประมวลผล</div>
<div class="mini-opt" data-val="B" onclick="updateMiniProgress(344)"><span class="mini-bullet">B</span> พาร์สโครงสร้างเพื่อสกัดแยกแท็กหรือข้อมูลเฉพาะส่วนที่ต้องการจาก HTML/XML</div>
<div class="mini-opt" data-val="C" onclick="updateMiniProgress(344)"><span class="mini-bullet">C</span> สั่งรันและส่งแพ็กเก็ตดิบ ICMP ไปกวาดค้นหาหมายเลขไอพีทั้งหมดในระบบ</div>
</div>
</div>

<!-- Neon Gauge Bar Progress -->
<div class="mq-progress-container">
<div id="mq-progress-bar-344" class="mq-progress-bar"></div>
<span id="mq-progress-text-344" class="mq-progress-text">Lesson Progress: 0% (ยังไม่ผ่าน)</span>
</div>

<button class="mq-btn-check" onclick="checkMiniQuiz(344)">Check Answers / ตรวจคำตอบ</button>
<div id="mq-status-344" class="mq-status-bar"></div>
</div>

<script>
// Attach click listeners to manage selection state
document.querySelectorAll('#mq-box-344 .mini-opt').forEach(opt => {
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

# ─── 2. Save and Commit the Restructured Lesson 171 to Database ───
l171.content = json.dumps(blocks_171, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=171).update({"content": l171.content})
db.session.commit()
print("Lesson 171 content completely redesigned and committed!")
ctx.pop()
