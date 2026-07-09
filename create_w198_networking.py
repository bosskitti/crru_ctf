import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

# ─── 1. Shift and rename ID 171 and 172 to make room for Lesson 3 ───
l171 = db.session.query(TutorialLesson).filter_by(id=171).first()
if l171:
    l171.position = 4
    l171.title = "04. ทักษะโปรแกรมมิ่งสำหรับการวิเคราะห์เว็บและดีไซน์ปลอดภัย (Programming Skills for Web Vulnerabilities & SSDLC)"
    db.session.commit()
    print("Lesson 171 shifted to Position 4 and renamed.")

l172 = db.session.query(TutorialLesson).filter_by(id=172).first()
if l172:
    l172.position = 5
    l172.title = "05. การเขียนโค้ดที่ไม่มีความปลอดภัยและช่องโหว่ (Insecure Coding & Buffer Overflows)"
    db.session.commit()
    print("Lesson 172 shifted to Position 5 and renamed.")

# ─── 2. Create the content blocks for the new Lesson 198 (03. Programming for Networking) ───
blocks_198 = []

# Block 0: Title & Header
blocks_198.append({
    "type": "markdown",
    "value": "## 🌐 ทักษะโปรแกรมมิ่งสำหรับการวิเคราะห์และสแกนเครือข่าย (Programming Skills for Networking)"
})

# Block 1: Networking & Port Scanning Concepts
blocks_198.append({
    "type": "markdown",
    "value": """### 📡 Overview of Network Scanning Concepts

การเขียนโปรแกรมเครือข่าย (Network Programming) และสแกนเน็ตเวิร์ก เป็นทักษะแกนหลักของแฮกเกอร์และนักวิเคราะห์ความปลอดภัยในการตรวจหาอุปกรณ์ที่ออนไลน์อยู่ (Active hosts), ตรวจพอร์ตที่เปิดบริการ (Open ports) และสแกนหาช่องโหว่ของโปรโตคอลระบบ:

<style>
.net-concept-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin:2rem auto;max-width:1050px;}
@media(max-width:768px){.net-concept-grid{grid-template-columns:1fr;}}
.net-card{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:20px;box-sizing:border-box;transition:all 0.25s ease;}
.net-card:hover{border-color:#00f0ff;background:rgba(0,240,255,0.02);transform:translateY(-2px);box-shadow:0 0 15px rgba(0,240,255,0.25);}
.net-hdr{display:flex;align-items:center;gap:12px;margin-bottom:10px;}
.net-icon{font-size:1.6rem;}
.net-title{font-size:0.95rem;font-weight:800;color:#ffffff;}
.net-desc{font-size:0.8rem;color:#94a3b8;line-height:1.65;margin:0;}
.net-desc strong{color:#fbbf24;}
</style>

<div class="net-concept-grid">
<div class="net-card">
<div class="net-hdr"><span class="net-icon">📡</span><span class="net-title">Ping Sweep</span></div>
<p class="net-desc">ส่งแพ็กเก็ตคำขอ <strong>ICMP Echo Requests (Ping)</strong> ไปยังช่วงหมายเลขไอพีปลายทางทั้งหมด เพื่อระบุว่ามีหมายเลขโฮสต์ใดกำลังเปิดเครื่องออนไลน์อยู่ในเครือข่าย</p>
</div>
<div class="net-card">
<div class="net-hdr"><span class="net-icon">🚪</span><span class="net-title">Port Scanning</span></div>
<p class="net-desc">ทำการกวาดตรวจสอบพอร์ตการสื่อสารทั้งแบบ <strong>TCP และ UDP</strong> ของเป้าหมาย เพื่อค้นหาว่าบริการใดเปิดช่องทางรับการเชื่อมต่อจากภายนอกอยู่</p>
</div>
<div class="net-card">
<div class="net-hdr"><span class="net-icon">👣</span><span class="net-title">OS Fingerprinting</span></div>
<p class="net-desc">วิเคราะห์พฤติกรรมค่าสถานะในส่วนหัวของแพ็กเก็ต (เช่น TTL, TCP Window Size) เพื่อคาดเดาและระบุรุ่น **ระบบปฏิบัติการ (OS)** ของเป้าหมาย</p>
</div>
<div class="net-card">
<div class="net-hdr"><span class="net-icon">🕵️</span><span class="net-title">Service & Version Detection</span></div>
<p class="net-desc">สืบค้นหา **ประเภทเวอร์ชันของบริการ** (เช่น Apache HTTPD 2.4.41, OpenSSH 8.2) เพื่อนำไปเปรียบเทียบกับฐานข้อมูล CVE ค้นหาช่องโหว่เจาะระบบ</p>
</div>
</div>"""
})

blocks_198.append({"type": "markdown", "value": "---"})

# Block 2: Python Libraries Overview
blocks_198.append({
    "type": "markdown",
    "value": """### 📦 Python Networking Libraries

ภาษา Python รองรับไลบรารีในการพัฒนาเครื่องมือวิเคราะห์และจัดการเครือข่ายได้อย่างยืดหยุ่น:
- **`socket`**: ไลบรารีอินเทอร์เฟซมาตรฐานระดับล่าง (Low-level) สำหรับสร้างและเชื่อมพอร์ต TCP/UDP
- **`scapy`**: สุดยอดไลบรารีวิเคราะห์ เขียน แก้ไข และส่งผ่านแพ็กเก็ตระดับสูง (Packet Manipulation)
- **`python-nmap`**: ตัวเชื่อมประสานคำสั่ง (Wrapper) เพื่อเรียกสแกนระบบของเครื่องมือ Nmap ผ่านโค้ด Python
- **`asyncio`**: ระบบจัดการงานแบบอะซิงโครนัส (Asynchronous) เพื่อใช้เร่งความเร็วในการยิงสแกนพร้อมกัน"""
})

blocks_198.append({"type": "markdown", "value": "---"})

# Block 3: Interactive Categorized Code Console with Detailed Line-by-Line analysis
blocks_198.append({
    "type": "markdown",
    "value": """### 💻 Networking Coding Console (วิเคราะห์เจาะลึก 5 ตัวอย่างโค้ดเน็ตเวิร์ก)

คลิกหัวข้อด้านซ้ายมือเพื่อตรวจสอบตัวอย่างชุดคำสั่งสแกน (Code) และ **การวิเคราะห์การทำงานอย่างละเอียดในเชิงความปลอดภัยไซเบอร์ (Detailed Security Analysis)**:

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
<button class="w-nav-item active" onclick="showSandboxItem('pingsweep', this)">1. Basic Ping Sweep Script</button>
<button class="w-nav-item" onclick="showSandboxItem('portscan', this)">2. Socket Port Scanner</button>
<button class="w-nav-item" onclick="showSandboxItem('scapyarp', this)">3. Scapy Advanced ARP Scan</button>
<button class="w-nav-item" onclick="showSandboxItem('nmapscan', this)">4. Nmap Version Scanner</button>
<button class="w-nav-item" onclick="showSandboxItem('domainrecon', this)">5. Domain Recon (Whois & DNS)</button>
</div>

<!-- Panel details right side -->
<div class="w-sandbox-panels">

<!-- 1. Ping Sweep -->
<div id="panel-pingsweep" class="w-sand-panel active">
<div class="w-sand-hdr"><span>1. Basic Ping Sweep Script</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import os, platform, subprocess
def ping(host):
    param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    command = f"ping {param} {host}"
    response = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0
    return response

def ping_sweep(network):
    active_hosts = []
    for i in range(1, 255):
        ip = f"{network}.{i}"
        if ping(ip):
            active_hosts.append(ip)
            print(f"{ip} is up")
    return active_hosts</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>สคริปต์สแกนเครื่องออนไลน์ย่อยด้วยโปรโตคอล ICMP:</p>
<ul>
<li><strong>param = "-n 1" if ... else "-c 1"</strong>: ตรวจสอบระบบปฏิบัติการของแอดมิน หากเป็น Windows จะใช้สวิตช์ `-n 1` (ส่งแพ็กเก็ต 1 ครั้ง) หากเป็น Linux/Unix จะใช้สวิตช์ `-c 1`</li>
<li><strong>subprocess.call(command, ...)</strong>: เรียกคำสั่งระบบปฏิบัติการภายนอกเพื่อยิง Ping โดยดึงเอาท์พุตส่วนขยะทิ้งไปทั้งหมดเพื่อความสะอาด</li>
<li><strong>for i in range(1, 255)</strong>: ลูปไล่หมายเลขไอพีหลักสุดท้าย (Octet) ของซับเน็ต `/24` ตั้งแต่ 1 ถึง 254 เพื่อพยายามส่งสัญญาณเช็คความพร้อมเครื่อง</li>
</ul>
</div>
</div>

<!-- 2. Port Scanner -->
<div id="panel-portscan" class="w-sand-panel">
<div class="w-sand-hdr"><span>2. Socket Port Scanner</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import socket
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>สคริปต์สแกนตรวจสอบพอร์ตความปลอดภัย TCP โดยใช้ระบบเบื้องต้นของ Socket:</p>
<ul>
<li><strong>socket.AF_INET / SOCK_STREAM</strong>: กำหนดการเชื่อมต่อระดับเครือข่ายในรูปแบบ IPv4 และสร้างท่อเชื่อมต่อโปรโตคอลแบบ TCP (Stream socket)</li>
<li><strong>sock.settimeout(0.5)</strong>: หน่วงเวลาในการรอการติดต่อกลับเพียง 0.5 วินาที เพื่อไม่ให้ระบบค้างเวลากวาดสแกนพอร์ตที่ถูกไฟร์วอลล์ปิดกั้นไว้</li>
<li><strong>sock.connect_ex((ip, port))</strong>: พยายามทำการเชื่อมโยงแบบ 3-Way Handshake หากสำเร็จ ฟังก์ชันนี้จะ **ส่งคืนค่าเป็นหมายเลข 0** เสมอ หากพอร์ตปิดหรือหมดเวลาจะส่งคืนรหัส Error Code ตัวอื่น</li>
</ul>
</div>
</div>

<!-- 3. Scapy ARP Scan -->
<div id="panel-scapyarp" class="w-sand-panel">
<div class="w-sand-hdr"><span>3. Scapy Advanced ARP Scan</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">from scapy.all import ARP, Ether, srp
def arp_scan(network):
    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=2, verbose=0)[0]
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    return devices</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การส่งแพ็กเก็ตระดับ Layer 2 ของการเชื่อมโยงข้อมูล (Data Link) เพื่อสืบค้นข้อมูลในซับเน็ตท้องถิ่น:</p>
<ul>
<li><strong>ARP(pdst=network)</strong>: สร้างแพ็กเก็ตสอบถามหมายเลขเครื่อง (Address Resolution Protocol) เพื่อจับคู่เลขไอพีกับ MAC</li>
<li><strong>Ether(dst="ff:ff:ff:ff:ff:ff")</strong>: ทำการจำลอง Broadcast ส่วนหัวเฟรมอินเทอร์เน็ตส่งข้อมูลหาทุกจุดในซับเน็ตเครือข่าย</li>
<li><strong>packet = ether/arp</strong>: ใน Scapy ใช้เครื่องหมายหาร `/` ในการซ้อนทับเลเยอร์การสื่อสาร (Ethernet ครอบทับ ARP)</li>
<li><strong>received.psrc / received.hwsrc</strong>: แกะผลตอบรับที่ตอบกลับมาเพื่อดึงหมายเลข IP และหมายเลขการ์ดแลน MAC Address ของผู้ใช้ปลายทาง</li>
</ul>
</div>
</div>

<!-- 4. Nmap Version Scanner -->
<div id="panel-nmapscan" class="w-sand-panel">
<div class="w-sand-hdr"><span>4. Nmap Version Scanner</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import nmap
def nmap_scan(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, arguments='-sV')
    for host in scanner.all_hosts():
        print(f"Host: {host}")
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in ports:
                print(f"Port: {port}, State: {scanner[host][proto][port]['state']}")</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>เรียกใช้ความสามารถของ Nmap สแกนเพื่อวิเคราะห์ประเภทโปรแกรมด้านใน:</p>
<ul>
<li><strong>scanner.scan(target, arguments='-sV')</strong>: ป้อนอาร์กิวเมนต์ `-sV` เพื่อสั่งให้ Nmap วิเคราะห์หาเวอร์ชันของซอฟต์แวร์ที่รันหลังพอร์ตเปิดเหล่านั้น</li>
<li><strong>scanner[host][proto][port]['state']</strong>: ดึงข้อมูลสรุปสถานะการทำงานของบริการเครือข่าย ช่วยตรวจหาบริการที่หมดอายุหรือตกเป็นเป้าหมายช่องโหว่</li>
</ul>
</div>
</div>

<!-- 5. Domain Recon -->
<div id="panel-domainrecon" class="w-sand-panel">
<div class="w-sand-hdr"><span>5. Domain Recon (Whois & DNS)</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import os
def domain_recon(domain):
    print(f"Running whois on {domain}...")
    os.system(f"whois {domain}")
    print(f"Running nslookup on {domain}...")
    os.system(f"nslookup {domain}")</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>ขั้นตอนการรวบรวมข้อมูลภายนอกเชิงรุก (Information Gathering) ก่อนทำการเจาะระบบเป้าหมาย:</p>
<ul>
<li><strong>whois {domain}</strong>: ยิงค้นหาข้อมูลเจ้าของทะเบียนโดเมนเนม วันจดทะเบียน แหล่งที่อยู่ และหมายเลขไอพี Name Server ของเป้าหมาย</li>
<li><strong>nslookup {domain}</strong>: ค้นหาบันทึกระบบแผนที่ชื่อ (DNS Records) ของโดเมน เพื่อตรวจสอบหาที่อยู่เซิร์ฟเวอร์หลักหรือที่ตั้งเมล์เซิร์ฟเวอร์หลัก (MX records)</li>
</ul>
</div>
</div>

</div>
</div>

<script>
// Sandbox Item switching logic explicitly setting display block/none
window.showSandboxItem = function(itemKey, element) {
  // Update active navigation class
  const items = document.querySelectorAll('.w-sandbox-nav .w-nav-item');
  items.forEach(i => i.classList.remove('active'));
  element.classList.add('active');

  // Switch display panel
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
blocks_198.append({
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

<div id="mq-box-343" class="mini-quiz-box">
<!-- Question 1 -->
<div class="mq-q" data-correct="B">
<div class="mq-title"><span>Q1.</span> ไลบรารีใดในภาษา Python ที่ได้รับความนิยมสูงสุดในเรื่องการปรับแต่ง จัดการ และเขียนโครงสร้างส่งผ่านแพ็กเก็ตดิบ (Packet Manipulation) ได้ในระดับสูงสุด?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A" onclick="updateMiniProgress(343)"><span class="mini-bullet">A</span> socket library</div>
<div class="mini-opt" data-val="B" onclick="updateMiniProgress(343)"><span class="mini-bullet">B</span> scapy library</div>
<div class="mini-opt" data-val="C" onclick="updateMiniProgress(343)"><span class="mini-bullet">C</span> paramiko library</div>
</div>
</div>

<!-- Question 2 -->
<div class="mq-q" data-correct="A">
<div class="mq-title"><span>Q2.</span> ในระบบ Socket Programming ของภาษา Python หากฟังก์ชัน `.connect_ex((ip, port))` ส่งคืนค่ากลับมาเป็นเลข 0 หมายความว่าอย่างไร?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A" onclick="updateMiniProgress(343)"><span class="mini-bullet">A</span> พอร์ตการสื่อสารเปิดให้บริการอยู่ (Open Port)</div>
<div class="mini-opt" data-val="B" onclick="updateMiniProgress(343)"><span class="mini-bullet">B</span> พอร์ตการสื่อสารถดถอยและปิดกั้นการเข้าใช้งานอยู่ (Closed Port)</div>
<div class="mini-opt" data-val="C" onclick="updateMiniProgress(343)"><span class="mini-bullet">C</span> ระบบยับยั้งล้มเหลวในการเชื่อมโยงเนื่องจากข้อผิดพลาด Timeout</div>
</div>
</div>

<!-- Neon Gauge Bar Progress -->
<div class="mq-progress-container">
<div id="mq-progress-bar-343" class="mq-progress-bar"></div>
<span id="mq-progress-text-343" class="mq-progress-text">Lesson Progress: 0% (ยังไม่ผ่าน)</span>
</div>

<button class="mq-btn-check" onclick="checkMiniQuiz(343)">Check Answers / ตรวจคำตอบ</button>
<div id="mq-status-343" class="mq-status-bar"></div>
</div>

<script>
// Attach click listeners to manage selection state
document.querySelectorAll('#mq-box-343 .mini-opt').forEach(opt => {
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

# ─── 3. Save and Commit the New Lesson 198 into Database ───
new_lesson = TutorialLesson(
    id=198,
    module_id=34,
    title="03. ทักษะโปรแกรมมิ่งสำหรับการวิเคราะห์และสแกนเครือข่าย (Programming Skills for Networking)",
    content=json.dumps(blocks_198, ensure_ascii=False),
    position=3,
    challenge_id=None
)

db.session.add(new_lesson)
db.session.commit()
print("New Lesson 198 successfully created and shifts committed!")
ctx.pop()
