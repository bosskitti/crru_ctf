import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l175 = db.session.query(TutorialLesson).filter_by(id=175).first()

# ─── Block 0: Core Theoretical Contents (Nmap, Nikto, OpenVAS, Metasploit Intro) ───
val0 = """## 🛠️ Exploitation Tools & Metasploit (เครื่องมือเจาะระบบและเมทาสปลอยต์)
---

หัวใจสำคัญของการประเมินระบบคือการสแกนเชิงลึกด้วยเครื่องมือระดับอุตสาหกรรม เพื่อตรวจสอบบริการ เวอร์ชัน และค้นหาช่องโหว่ความปลอดภัยที่นำไปสู่สิทธิ์ระดับแอดมิน

### 📡 1. Nmap CLI Commands & Scripting Engine (NSE)
**Nmap (Network Mapper)** ถือเป็นราชาแห่งการสแกนเครือข่าย มีพารามิเตอร์การสั่งงานระดับสูงเพื่อวิเคราะห์พฤติกรรมระบบ:
- 📌 **Scanning Techniques**:
  - `nmap -sT <target>`: สแกนแบบ TCP Connect (เชื่อมต่อ 3-way handshake เต็มรูปแบบ)
  - `nmap -sS <target>`: สแกนแบบ TCP SYN (แบบ Stealth ซ่อนร่องรอย ไม่จบ handshake)
  - `nmap -sU <target>`: สแกนพอร์ต UDP
  - `nmap -sP <target>`: Ping Sweep กวาดหาเครื่องที่เปิดทำงานอยู่
  - `nmap -sV <target>`: ตรวจหาเวอร์ชันของบริการ (Service Version Detection)
  - `nmap -O <target>`: ตรวจสอบระบบปฏิบัติการเป้าหมาย (OS Detection)
  - `nmap -A <target>`: สแกนแบบดุดัน (รวม OS, Version, และ Script สแกนไว้ในคำสั่งเดียว)
  - `nmap -Pn <target>`: สั่งข้ามการ Ping สแกน (สมมติว่าเป้าหมายเปิดอยู่ ป้องกันการโดนบล็อก ICMP)
- 🧰 **Nmap Scripting Engine (NSE)**: ระบบส่วนขยายเขียนด้วยภาษา Lua เพื่อรันสคริปต์สแกนช่องโหว่:
  - `nmap --script vuln <target>`: ตรวจหาช่องโหว่ทั้งหมดที่รู้จักในระบบ
  - `nmap --script smb-vuln-ms17-010 <target>`: ตรวจจับสแกนหาช่องโหว่ EternalBlue
  - `nmap --script http-title <target>`: สกัดหาข้อความ Title ของหน้าเว็บเป้าหมาย

---

### 🌐 2. Web Vulnerability Scanner: Nikto
**Nikto** เป็นเครื่องมือสแกนช่องโหว่ระดับ Web Server โดยเฉพาะ:
- ตรวจสอบหาไฟล์ขยะหรือไดเรกทอรีมาตรฐานที่มักหลงเหลือ เช่น `/admin/`, `/test/`, `config.php.bak`
- ตรวจสอบการตั้งค่าความปลอดภัยของ HTTP Headers
- สามารถสั่งเลี่ยงการดักจับ (IDS/IPS Evasion) ด้วยคำสั่ง `-Tuning` หรือสวมรอยผ่าน Tor/Proxy

---

### 🟢 3. OpenVAS (Greenbone GVM)
ระบบตรวจสอบหาช่องโหว่ทางเครือข่ายและระบบปฏิบัติการแบบอัตโนมัติระดับองค์กร:
- ทำงานผ่านเว็บอินเตอร์เฟสแบบพรีเมียม (พอร์ต `9392`)
- รองรับการทำ **Full and Fast Scan** เพื่อตรวจสอบระบบและนำเสนอรายงานแก้ไขแบบ PDF/HTML
- สามารถสั่งติดตั้งผ่านระบบคอนเทนเนอร์:
  `docker run -d -p 9392:9392 --name openvas mikesplain/openvas`

---

### 🐍 4. Python-Nmap integration & Gaining Access Intro
- **python-nmap**: การเรียกใช้เครื่องมือ Nmap เข้ามาประกอบลงในซอร์สโค้ด Python เพื่อประมวลผลเครือข่ายอัตโนมัติ
- **Gaining Access**: ขั้นตอนการโจมตีเป้าหมายด้วยเฟรมเวิร์กยอดนิยม **Metasploit Framework (MSF)** ประกอบไปด้วยโมดูลย่อย:
  - **Exploit**: โค้ดโจมตีช่องโหว่
  - **Auxiliary**: สคริปต์เสริมวิเคราะห์สแกนหาช่องโหว่
  - **Payload**: โค้ดที่รันหลังจากเจาะระบบผ่าน (เช่น Meterpreter, Shell)"""

# ─── Block 1: Exploitation Sandbox (Live Terminal Simulator) ───
val1 = """### 💻 Active Scanning & Exploit Sandbox (จำลองชุดคำสั่งเครื่องมือตรวจสอบช่องโหว่)

คลิกหัวข้อด้านซ้ายมือเพื่อศึกษาตัวอย่างการใช้งานเครื่องมือเจาะระบบ และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลลัพธ์ผ่านเทอร์มินัลระบบ:

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
<button id="nav-item-nmapsyn" class="w-nav-item active" onclick="showSandboxItem('nmapsyn', this)">1. Nmap Stealth Scan</button>
<button id="nav-item-nmapnse" class="w-nav-item" onclick="showSandboxItem('nmapnse', this)">2. Nmap SMB Script (NSE)</button>
<button id="nav-item-nikto" class="w-nav-item" onclick="showSandboxItem('nikto', this)">3. Nikto Web Scanner</button>
<button id="nav-item-openvas" class="w-nav-item" onclick="showSandboxItem('openvas', this)">4. OpenVAS Container Setup</button>
<button id="nav-item-pynmap" class="w-nav-item" onclick="showSandboxItem('pynmap', this)">5. python-nmap Script</button>
</div>

<!-- Panel details right side -->
<div class="w-sandbox-panels">

<!-- 1. Nmap SYN -->
<div id="panel-nmapsyn" class="w-sand-panel">
<div class="w-sand-hdr"><span>1. Nmap Stealth SYN Scan</span> <span class="tag">Linux CLI</span></div>
<pre class="w-sand-code"># สแกนเวอร์ชันระบบปฏิบัติการและบริการเป้าหมายแบบดุดันและเร่งด่วน
nmap -sS -sV -O -T4 --open 172.19.19.129</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startMSFSim('nmapsyn')">▶ Run Simulation</button>
</div>
<div id="term-nmapsyn" class="w-sand-term"><span class="prompt">root@kali:~#</span> [กดปุ่ม Run Simulation เพื่อจำลองคำสั่ง]</div>
</div>
<div class="w-sand-expl">
<h5>⚙️ Command Description</h5>
<p><strong>-sS</strong> (SYN Stealth scan) จะยิงขอสิทธิ์แบบครึ่ง handshake ปลอดภัยจากการบันทึก log บราวเซอร์ และสั่งดึงเวอร์ชันซอฟต์แวร์ด้วย `-sV` และเดา OS ด้วย `-O` ในความเร็วระดับสูงสุด `-T4`</p>
</div>
</div>

<!-- 2. Nmap NSE -->
<div id="panel-nmapnse" class="w-sand-panel">
<div class="w-sand-hdr"><span>2. Nmap SMB Vulnerability NSE</span> <span class="tag">Linux CLI</span></div>
<pre class="w-sand-code"># สแกนหาช่องโหว่ EternalBlue (MS17-010) ในโปรโตคอลแชร์ไฟล์ SMB
nmap -p 445 --script smb-vuln-ms17-010 172.19.19.129</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startMSFSim('nmapnse')">▶ Run Simulation</button>
</div>
<div id="term-nmapnse" class="w-sand-term"><span class="prompt">root@kali:~#</span> [กดปุ่ม Run Simulation เพื่อจำลองคำสั่ง]</div>
</div>
<div class="w-sand-expl">
<h5>⚙️ Command Description</h5>
<p>NSE Script **smb-vuln-ms17-010** จะยิงตรวจสอบช่องโหว่วิกฤต EternalBlue บนพอร์ต 445 ของ Windows เพื่อเป้าหมายประเมินความปลอดภัย</p>
</div>
</div>

<!-- 3. Nikto -->
<div id="panel-nikto" class="w-sand-panel">
<div class="w-sand-hdr"><span>3. Nikto Web Vulnerability Scanner</span> <span class="tag">Linux CLI</span></div>
<pre class="w-sand-code"># สแกนหาช่องโหว่ความปลอดภัยและจุดบกพร่องคอนฟิกของเว็บเซิร์ฟเวอร์
nikto -h http://172.19.19.129 -Tuning 123</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startMSFSim('nikto')">▶ Run Simulation</button>
</div>
<div id="term-nikto" class="w-sand-term"><span class="prompt">root@kali:~#</span> [กดปุ่ม Run Simulation เพื่อจำลองคำสั่ง]</div>
</div>
<div class="w-sand-expl">
<h5>⚙️ Command Description</h5>
<p>คำสั่งสแกนหาข้อผิดพลาดเว็บด้วย **Nikto** โดยเจาะจง Tuning ไปที่ไฟล์สำคัญ (1), ข้อบกพร่องเซิร์ฟเวอร์ (2) และไฟล์เริ่มต้นระบบ (3)</p>
</div>
</div>

<!-- 4. OpenVAS -->
<div id="panel-openvas" class="w-sand-panel">
<div class="w-sand-hdr"><span>4. Docker OpenVAS Deployment</span> <span class="tag">Docker CLI</span></div>
<pre class="w-sand-code"># ดึงข้อมูลคอนเทนเนอร์และสั่งรันระบบ OpenVAS บนพอร์ต 9392
docker run -d -p 9392:9392 --name openvas mikesplain/openvas</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startMSFSim('openvas')">▶ Run Simulation</button>
</div>
<div id="term-openvas" class="w-sand-term"><span class="prompt">root@kali:~#</span> [กดปุ่ม Run Simulation เพื่อจำลองคำสั่ง]</div>
</div>
<div class="w-sand-expl">
<h5>⚙️ Command Description</h5>
<p>รันระบบตรวจสอบช่องโหว่อัตโนมัติในระดับเบื้องหลัง (Background Daemon) เพื่อเปิดเข้าใช้งานหน้าเว็บ UI ของ OpenVAS ที่พอร์ต 9392</p>
</div>
</div>

<!-- 5. Python-Nmap -->
<div id="panel-pynmap" class="w-sand-panel">
<div class="w-sand-hdr"><span>5. python-nmap Integration</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import nmap
nm = nmap.PortScanner()
nm.scan("172.19.19.129", "22-80", "-sS")
for host in nm.all_hosts():
    print("Host State:", nm[host].state())</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startMSFSim('pynmap')">▶ Run Simulation</button>
</div>
<div id="term-pynmap" class="w-sand-term"><span class="prompt">root@kali:~#</span> [กดปุ่ม Run Simulation เพื่อจำลองคำสั่ง]</div>
</div>
<div class="w-sand-expl">
<h5>⚙️ Command Description</h5>
<p>การเขียนโค้ดเรียกใช้งานชุดคำสั่ง Nmap เข้ามาทำงานใน Python เพื่อสั่งดำเนินการกวาดหาเป้าหมายและประมวลผลข้อมูลในสคริปต์อัตโนมัติ</p>
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

// Simulator logic
window.startMSFSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;

  term.innerHTML = '<span class="prompt">root@kali:~#</span> <span class="cmd">Starting security scanner...</span>\\n[.] Transmitting scan payloads\\n[.] Parsing signatures...';

  setTimeout(() => {
    if (itemKey === 'nmapsyn') {
      term.innerHTML = '<span class="prompt">root@kali:~#</span> <span class="cmd">nmap -sS -sV -O --open 172.19.19.129</span>\\nStarting Nmap 7.92...\\nNmap scan report for 172.19.19.129\\nHost is up (0.0024s latency).\\nNot shown: 998 closed tcp ports (reset)\\nPORT   STATE SERVICE VERSION\\n22/tcp open  ssh     <span style="color:#00f0ff;">OpenSSH 8.2p1</span> (Ubuntu)\\n80/tcp open  http    <span style="color:#00f0ff;">Apache httpd 2.4.41</span> ((Ubuntu))\\n\\nAggressive OS guesses: Linux 4.15 - 5.6 (98%)';
    } else if (itemKey === 'nmapnse') {
      term.innerHTML = '<span class="prompt">root@kali:~#</span> <span class="cmd">nmap -p 445 --script smb-vuln-ms17-010 172.19.19.129</span>\\nPORT    STATE SERVICE\\n445/tcp open  microsoft-ds\\n\\nHost script results:\\n| <span style="color:#dc3545; font-weight:bold;">smb-vuln-ms17-010: VULNERABLE</span>\\n|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010).\\n|   State: <span style="color:#dc3545;">VULNERABLE</span>\\n|   IDs:  CVE:CVE-2017-0144\\n|_  Risk factor: <span style="color:#dc3545; font-weight:bold;">HIGH</span>';
    } else if (itemKey === 'nikto') {
      term.innerHTML = '<span class="prompt">root@kali:~#</span> <span class="cmd">nikto -h http://172.19.19.129</span>\\n- Nikto v2.1.6\\n-----------------------------------------------------------------------\\n+ Target IP:          172.19.19.129\\n+ Target Hostname:    172.19.19.129\\n+ Target Port:        80\\n-----------------------------------------------------------------------\\n+ OSVDB-3092: /admin/: <span style="color:#fbbf24;">Admin login page found.</span>\\n+ OSVDB-3268: /config.php.bak: <span style="color:#fbbf24;">Backup file found containing database settings.</span>\\n+ 7548 items checked - 2 items found on remote host.';
    } else if (itemKey === 'openvas') {
      term.innerHTML = '<span class="prompt">root@kali:~#</span> <span class="cmd">docker ps -a | grep openvas</span>\\n9d8b120cf3a9   mikesplain/openvas   "/start"   30 seconds ago   Up 28 seconds   0.0.0.0:9392-&gt;9392/tcp   openvas\\n\\n[+] OpenVAS Web UI available at: <span style="color:#3ddc84;">https://localhost:9392</span>';
    } else if (itemKey === 'pynmap') {
      term.innerHTML = '<span class="prompt">root@kali:~#</span> <span class="cmd">python3 scan.py</span>\\nHost: 172.19.19.129 (ctf-target)\\nState: up\\n\\nProtocol: TCP\\nPort 22: open - ssh\\nPort 80: open - http';
    }
  }, 1000);
}
</script>"""

# ─── Block 2: Quick Quiz and Progress Gauge ───
val2 = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการบันทึกความสำเร็จและปลดล็อกปุ่มบทเรียนถัดไป:

<div class="row align-items-center" style="margin:1.5rem auto; max-width:980px;">
<div class="col-md-8">

<!-- Question 1 -->
<div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;">
<p class="text-white mb-2" style="font-size:0.88rem; font-weight:600;">1. พารามิเตอร์ใดของชุดคำสั่ง Nmap ที่ใช้สั่งเพื่อดึงดูสถานะและหมายเลขรุ่นของซอฟต์แวร์บริการในพอร์ตเป้าหมาย? (ตอบระบุพารามิเตอร์ขีดลบพร้อมตัวอักษร เช่น -sT)</p>
<div class="input-group">
<input type="text" class="form-control question-input" placeholder="คำตอบของคุณ..." data-hash="b200b332bfa353a2f1b40d6cfa9286ebbc7e5c6a9b8979e2c65757d5f088198f" style="background:rgba(15,17,26,0.8) !important; border:1px solid rgba(255,255,255,0.12) !important; color:#ffffff !important; font-family:\'JetBrains Mono\',monospace; font-size:0.9rem; border-radius:6px 0 0 6px !important;">
<div class="input-group-append">
<button class="btn btn-warning px-4 text-dark font-weight-bold" type="button" onclick="verifyLessonQuiz(this)">
<i class="fas fa-paper-plane mr-1"></i> Submit
</button>
</div>
</div>
<div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div>
</div>

<!-- Question 2 -->
<div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;">
<p class="text-white mb-2" style="font-size:0.88rem; font-weight:600;">2. พารามิเตอร์ใดของ Nmap ใช้ข้ามขั้นตอนการสแกนแบบ Ping ทำให้คิดว่าโฮสต์เปิดใช้งานอยู่เสมอ? (ตอบระบุพารามิเตอร์ขีดลบพร้อมตัวอักษร เช่น -sC)</p>
<div class="input-group">
<input type="text" class="form-control question-input" placeholder="คำตอบของคุณ..." data-hash="de6113ccf30f55cf643f8e401ec86eb61284d72851cf5718dfd38a0f9a2e61a2" style="background:rgba(15,17,26,0.8) !important; border:1px solid rgba(255,255,255,0.12) !important; color:#ffffff !important; font-family:\'JetBrains Mono\',monospace; font-size:0.9rem; border-radius:6px 0 0 6px !important;">
<div class="input-group-append">
<button class="btn btn-warning px-4 text-dark font-weight-bold" type="button" onclick="verifyLessonQuiz(this)">
<i class="fas fa-paper-plane mr-1"></i> Submit
</button>
</div>
</div>
<div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div>
</div>

</div>

<!-- Gauge Column -->
<div class="col-md-4 text-center">
<div class="p-4" style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); border-radius:12px; min-height:220px; display:flex; flex-direction:column; justify-content:center; align-items:center;">
<span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;">Lesson Progress</span>
<div class="neon-gauge-container">
<svg class="neon-gauge" viewBox="0 0 36 36">
<path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
<path class="neon-gauge-fill" id="lesson-gauge-fill" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
<text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text">0%</text>
</svg>
</div>
<span id="lesson-status-txt" class="mt-3 d-block text-muted" style="font-size:0.78rem;">โปรดส่งคำตอบให้ครบ 2 ข้อ</span>
</div>
</div>

</div>

<style>
/* CSS gauge animations and styles */
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:#00f0ff; stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease, stroke 0.5s ease; filter:drop-shadow(0 0 5px rgba(0,240,255,0.5));}
.neon-gauge-text {fill:#ffffff; font-family:\'JetBrains Mono\',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}
</style>

<script>
// SHA-256 calculator function
async function sha256hex(str) {
  const buf = new TextEncoder().encode(str.trim());
  const hashBuf = await crypto.subtle.digest(\'SHA-256\', buf);
  const arr = Array.from(new Uint8Array(hashBuf));
  return arr.map(b => b.toString(16).padStart(2, \'0\').trim()).join(\'\');
}

// Local storage progress tracking
const lessonKey = 'solved_lesson_175';

function getSavedSolves() {
  try {
    return JSON.parse(localStorage.getItem(lessonKey) || '[]');
  } catch(e) {
    return [];
  }
}

function updateLocalProgress() {
  const solved = getSavedSolves();
  const total = 2;
  const percent = Math.round((solved.length / total) * 100);

  const fill = document.getElementById(\'lesson-gauge-fill\');
  const text = document.getElementById(\'lesson-gauge-text\');
  const status = document.getElementById(\'lesson-status-txt\');

  if (fill) fill.setAttribute(\'stroke-dasharray\', `${percent}, 100`);
  if (text) text.textContent = `${percent}%`;

  if (solved.length === total) {
    if (fill) fill.style.stroke = \'#3ddc84\';
    if (status) {
      status.innerHTML = \'<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>\';
    }
  } else {
    if (fill) fill.style.stroke = \'#00f0ff\';
    if (status) status.textContent = `ทำเสร็จแล้ว ${solved.length}/${total} ข้อ`;
  }
}

window.verifyLessonQuiz = async function(button) {
  const cell = button.closest(\'.question-cell\');
  const input = cell.querySelector(\'.question-input\');
  const feedback = cell.querySelector(\'.feedback-msg\');
  const targetHash = input.getAttribute(\'data-hash\');
  const val = input.value.trim();

  if (!val) {
    feedback.className = "feedback-msg mt-2 alert-warning py-1.5 px-3 text-dark";
    feedback.innerHTML = \'<i class="fas fa-exclamation-triangle mr-1"></i> กรุณากรอกคำตอบ\';
    feedback.style.setProperty(\'display\', \'block\', \'important\');
    return;
  }

  const userHash = await sha256hex(val);
  if (userHash === targetHash) {
    feedback.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
    feedback.innerHTML = \'<i class="fas fa-check-circle mr-1"></i> คำตอบถูกต้อง!\';
    feedback.style.setProperty(\'display\', \'block\', \'important\');
    input.classList.remove(\'is-invalid\');
    input.classList.add(\'is-valid\');
    input.disabled = true;
    button.disabled = true;

    // Save solve status
    const solved = getSavedSolves();
    if (!solved.includes(targetHash)) {
      solved.push(targetHash);
      localStorage.setItem(lessonKey, JSON.stringify(solved));
    }
    updateLocalProgress();
  } else {
    feedback.className = "feedback-msg mt-2 alert-danger py-1.5 px-3 text-white bg-danger border-0";
    feedback.innerHTML = \'<i class="fas fa-times-circle mr-1"></i> คำตอบไม่ถูกต้อง ลองอีกครั้ง!\';
    feedback.style.setProperty(\'display\', \'block\', \'important\');
    input.classList.remove(\'is-valid\');
    input.classList.add(\'is-invalid\');
  }
}

// Auto init state on load
setTimeout(() => {
  const solved = getSavedSolves();
  document.querySelectorAll(\'.question-input\').forEach(input => {
    const hash = input.getAttribute(\'data-hash\');
    if (solved.includes(hash)) {
      input.value = "COMPLETED";
      input.disabled = true;
      input.classList.add(\'is-valid\');
      const cell = input.closest(\'.question-cell\');
      if (cell) {
        const btn = cell.querySelector(\'button\');
        if (btn) btn.disabled = true;
        const fb = cell.querySelector(\'.feedback-msg\');
        if (fb) {
          fb.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
          fb.innerHTML = \'<i class="fas fa-check-circle mr-1"></i> เรียบร้อยแล้ว\';
          fb.style.setProperty(\'display\', \'block\', \'important\');
        }
      }
    }
  });
  updateLocalProgress();
}, 200);
</script>"""

# Make structure list of content
content_json = [
    {"type": "markdown", "value": val0},
    {"type": "markdown", "value": val1},
    {"type": "markdown", "value": val2}
]

l175.content = json.dumps(content_json, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=175).update({"content": l175.content})
db.session.commit()
print("Lesson 175 successfully updated and structured!")
ctx.pop()
