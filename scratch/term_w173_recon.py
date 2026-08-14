import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l173 = db.session.query(TutorialLesson).filter_by(id=173).first()

# ─── Block 0: Core Theoretical Contents (Network & Pentesting Foundation) ───
val0 = """## 🧠 Network Scanning & Enumeration (การสำรวจระบบเครือข่ายและการสแกน)
---

ยินดีต้อนรับสู่บทเรียนการสำรวจข้อมูลและตรวจสอบเครือข่ายเป้าหมาย ขั้นตอนแรกในการเข้าทำลายหรือป้องกันช่องโหว่ความปลอดภัยคือการเรียนรู้แผนผังที่ตั้งทางเครือข่าย

### 🗺️ 1. Computer Network & Protocols Foundation
โครงสร้างเครือข่ายคอมพิวเตอร์ประกอบไปด้วยสถาปัตยกรรมและโปรโตคอลที่สื่อสารกันในระดับต่างๆ:

<div class="row mb-4">
<div class="col-md-6">
<div class="p-3 card-neon" style="background:rgba(6,8,20,0.6); border:1px solid rgba(0,240,255,0.15); border-radius:8px; height:100%;">
<h5 class="text-cyan font-weight-bold"><i class="fas fa-project-diagram mr-2"></i> OSI 7 Layers Model</h5>
<ul style="padding-left:20px; font-size:0.82rem; color:#cbd5e1; line-height:1.6;">
<li><strong>Layer 7 Application</strong>: บริการระดับโปรแกรมประยุกต์ (HTTP, SSH, DNS)</li>
<li><strong>Layer 6 Presentation</strong>: การแปลรูปฟอร์แมตข้อมูลดิบ</li>
<li><strong>Layer 5 Session</strong>: จัดการและดูแลเซสชันเชื่อมต่อ</li>
<li><strong>Layer 4 Transport</strong>: จัดการส่งข้อมูลต้นทางไปปลายทาง (TCP/UDP)</li>
<li><strong>Layer 3 Network</strong>: การกำหนดทิศทางและการนำส่งข้อมูล (IP/Routing)</li>
<li><strong>Layer 2 Data Link</strong>: ส่งข้อมูลระหว่างโหนดเครือข่ายเดียว (MAC/Ethernet)</li>
<li><strong>Layer 1 Physical</strong>: การส่งบิตดิบผ่านสายนำสัญญาณกายภาพ</li>
</ul>
</div>
</div>
<div class="col-md-6">
<div class="p-3 card-neon" style="background:rgba(6,8,20,0.6); border:1px solid rgba(139,92,246,0.15); border-radius:8px; height:100%;">
<h5 class="text-violet font-weight-bold"><i class="fas fa-network-wired mr-2"></i> TCP/IP Protocol Layers</h5>
<ul style="padding-left:20px; font-size:0.82rem; color:#cbd5e1; line-height:1.6;">
<li><strong>Application Layer</strong>: รวมชั้น Application, Presentation, Session (เช่น FTP, DNS)</li>
<li><strong>Transport Layer</strong>: ดูแลความถูกต้องของการส่งข้อมูลต้นทาง-ปลายทาง (TCP, UDP)</li>
<li><strong>Internet Layer</strong>:Logical Addressing, Routing และการส่งแพ็กเก็ต (IP, ICMP, ARP)</li>
<li><strong>Network Interface/Link</strong>: คุมการ์ดแลนและการแปลงเฟรมสายส่ง (Ethernet, Wi-Fi)</li>
</ul>
</div>
</div>
</div>

### 🔑 2. Network Ports & Ranges
พอร์ตการเชื่อมต่อแบ่งออกเป็น 3 ช่วงหลัก (ตั้งแต่พอร์ต 0 ถึง 65535) เพื่อควบคุมเส้นทางบริการ:
- 🌐 **Well-Known Ports (0-1023)**: พอร์ตบริการมาตรฐานที่ควบคุมโดย IANA เช่น **FTP (20/21)**, **SSH (22)**, **Telnet (23)**, **SMTP (25)**, **DNS (53)**, **HTTP (80)**, **HTTPS (443)**, **SMB (445)**
- ⚙️ **Registered Ports (1024-49151)**: พอร์ตลงทะเบียนสำหรับระบบซอฟต์แวร์ เช่น **MSSQL (1433)**, **MySQL (3306)**, **PostgreSQL (5432)**, **RDP (3389)**, **HTTP-Alt (8080)**
- 🔒 **Dynamic or Private Ports (49152-65535)**: พอร์ตฝั่ง Client ที่สร้างขึ้นชั่วคราวเพื่อส่งคำสั่งสื่อสาร

---

### 🛡️ 3. CVE & CVSS System
- 🔖 **CVE (Common Vulnerabilities and Exposures)**: ระบบการจัดทำดัชนีชื่อช่องโหว่ความปลอดภัยระดับสากล เช่น **CVE-YYYY-NNNN** ดูแลโดย MITRE Corporation
- 📊 **CVSS (Common Vulnerability Scoring System)**: คะแนนระดับความรุนแรงของช่องโหว่ (0.0 ถึง 10.0 คะแนน)
  - `9.0 - 10.0`: **Critical (วิกฤต)**
  - `7.0 - 8.9`: **High (สูง)**
  - `4.0 - 6.9`: **Medium (ปานกลาง)**
  - `0.1 - 3.9`: **Low (ต่ำ)**

---

### 🚀 4. Gaining Access & Penetration Testing Stages
วงจรการเจาะระบบเพื่อประเมินความปลอดภัยประกอบไปด้วย 6 ขั้นตอนหลัก:
1. **Reconnaissance (การสำรวจ)**: เก็บข้อมูลเป้าหมายแบบไม่ให้รู้ตัว (Passive Information Gathering เช่น Google Dork, WHOIS)
2. **Scanning (การสแกนเชิงรุก)**: ระดมเครื่องมือค้นหาช่องโหว่ของเป้าหมายตรงๆ (Active Information Gathering เช่น Nmap, Nessus)
3. **Gaining Access (การบุกยึดระบบ)**: โจมตีและเจาะทะลุช่องโหว่ระบบเพื่อสร้างสิทธิ์รันคำสั่ง (Metasploit, Hydra)
4. **Maintaining Access (การคงสิทธิ์)**: ติดตั้ง Backdoor หรือเพิ่มผู้ดูแลระบบเพื่อให้รันระบบได้ถาวร (Persistence)
5. **Covering Tracks (การกลบร่องรอย)**: ลบไฟล์ประวัติ ล้างไฟล์ Log ระบบเพื่อสวมรอยเงียบ
6. **Reporting (การรายงานผล)**: สรุปหัวข้อช่องโหว่และเสนอแนวทางแก้ไขให้หน่วยงานแก้ไข"""

# ─── Block 1: Network Commands Sandbox (Live Terminal Simulator) ───
val1 = """### 💻 Network Diagnostics Coding Sandbox (จำลองคำสั่งเครือข่ายระบบ)

คลิกหัวข้อด้านซ้ายมือเพื่อศึกษาคำสั่งวิเคราะห์ระบบเครือข่าย และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลลัพธ์ผ่านเทอร์มินัลระบบ:

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
<button id="nav-item-ifconfig" class="w-nav-item active" onclick="showSandboxItem('ifconfig', this)">1. Interface Config (ifconfig)</button>
<button id="nav-item-ipaddr" class="w-nav-item" onclick="showSandboxItem('ipaddr', this)">2. IP Route Utility (ip)</button>
<button id="nav-item-ping" class="w-nav-item" onclick="showSandboxItem('ping', this)">3. Connectivity Test (ping)</button>
<button id="nav-item-dnslookup" class="w-nav-item" onclick="showSandboxItem('dnslookup', this)">4. DNS Queries (nslookup/dig)</button>
<button id="nav-item-netcat" class="w-nav-item" onclick="showSandboxItem('netcat', this)">5. Netcat Shell (nc)</button>
</div>

<!-- Panel details right side -->
<div class="w-sandbox-panels">

<!-- 1. ifconfig -->
<div id="panel-ifconfig" class="w-sand-panel">
<div class="w-sand-hdr"><span>1. Interface Configuration</span> <span class="tag">Linux CLI</span></div>
<pre class="w-sand-code"># แสดงรายละเอียด Interface เครือข่ายทั้งหมดในเครื่อง
ifconfig

# สั่งปิดและเปิด Interface ethernet card
ifconfig eth0 down
ifconfig eth0 up

# กำหนด IP Address และ Subnet Mask แบบชั่วคราว
ifconfig eth0 192.168.1.10 netmask 255.255.255.0</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startReconSim('ifconfig')">▶ Run Simulation</button>
</div>
<div id="term-ifconfig" class="w-sand-term"><span class="prompt">root@kali:~#</span> [กดปุ่ม Run Simulation เพื่อจำลองคำสั่ง]</div>
</div>
<div class="w-sand-expl">
<h5>⚙️ Command Description</h5>
<p><strong>ifconfig</strong> เป็นเครื่องมือมาตรฐานเดิมในการตรวจสอบการตั้งค่า IP Address และจัดสรรไอพีให้การ์ดแลนในตัวระบบ</p>
</div>
</div>

<!-- 2. ip addr -->
<div id="panel-ipaddr" class="w-sand-panel">
<div class="w-sand-hdr"><span>2. IP Route Management (ip)</span> <span class="tag">Linux CLI</span></div>
<pre class="w-sand-code"># แสดง IP Address ของ Interfaces ทั้งหมดแบบทันสมัย
ip addr

# สั่งตั้งค่าเปิดใช้งาน Interface
ip link set eth0 up

# แอด IP Address ในรูปแบบ CIDR
ip addr add 192.168.1.10/24 dev eth0</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startReconSim('ipaddr')">▶ Run Simulation</button>
</div>
<div id="term-ipaddr" class="w-sand-term"><span class="prompt">root@kali:~#</span> [กดปุ่ม Run Simulation เพื่อจำลองคำสั่ง]</div>
</div>
<div class="w-sand-expl">
<h5>⚙️ Command Description</h5>
<p><strong>ip</strong> เป็นเครื่องมือมาตรฐานระบบลินุกซ์ยุคใหม่ที่เข้ามาทดแทน `ifconfig` มีความแม่นยำในการสั่งจัดการเน็ตเวิร์กการ์ดและตั้งค่า Routing ได้มีประสิทธิภาพดีกว่า</p>
</div>
</div>

<!-- 3. ping -->
<div id="panel-ping" class="w-sand-panel">
<div class="w-sand-hdr"><span>3. Connectivity Diagnostic (ping)</span> <span class="tag">Linux CLI</span></div>
<pre class="w-sand-code"># ส่ง ICMP Echo Request ไปยังปลายทางเพื่อวัดค่า RTT
ping -c 4 8.8.8.8

# ตรวจหาเส้นทางเครือข่ายด้วย Traceroute
traceroute google.com</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startReconSim('ping')">▶ Run Simulation</button>
</div>
<div id="term-ping" class="w-sand-term"><span class="prompt">root@kali:~#</span> [กดปุ่ม Run Simulation เพื่อจำลองคำสั่ง]</div>
</div>
<div class="w-sand-expl">
<h5>⚙️ Command Description</h5>
<p><strong>ping</strong> ใช้สืบค้นการเปิดทำงานของโฮสต์ผ่านแพ็กเก็ต ICMP และค่า **TTL (Time to Live)** ในแพ็กเก็ตขากลับสามารถนำมาใช้อนุมานประเภท OS ปลายทางได้เบื้องต้น (เช่น Linux=64, Windows=128, Network Device=255)</p>
</div>
</div>

<!-- 4. DNS queries -->
<div id="panel-dnslookup" class="w-sand-panel">
<div class="w-sand-hdr"><span>4. DNS Lookup Utility</span> <span class="tag">Linux CLI</span></div>
<pre class="w-sand-code"># ค้นหา IP Address จาก Domain name
nslookup google.com

# สแกนหาประวัติ DNS record แบบละเอียด
dig google.com

# สืบค้นข้อมูล MX (Mail Server) record
dig google.com MX</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startReconSim('dnslookup')">▶ Run Simulation</button>
</div>
<div id="term-dnslookup" class="w-sand-term"><span class="prompt">root@kali:~#</span> [กดปุ่ม Run Simulation เพื่อจำลองคำสั่ง]</div>
</div>
<div class="w-sand-expl">
<h5>⚙️ Command Description</h5>
<p><strong>nslookup</strong> และ <strong>dig</strong> มีเป้าหมายในการดึงข้อมูล DNS records ของชื่อโดเมนเพื่อค้นหาเป้าหมายเครื่อง Mail Server หรือ Nameservers ที่เกี่ยวข้อง</p>
</div>
</div>

<!-- 5. Netcat -->
<div id="panel-netcat" class="w-sand-panel">
<div class="w-sand-hdr"><span>5. Netcat Swiss Army Knife</span> <span class="tag">Linux CLI</span></div>
<pre class="w-sand-code"># สแกนพอร์ตเป้าหมายเบื้องต้นแบบรวดเร็ว
nc -zv 192.168.1.1 1-100

# เปิด TCP Server ตั้งรับฟังเชื่อมต่อที่พอร์ต 4444
nc -lvnp 4444

# ฝังตัวรัน Shell ส่งข้ามเครือข่ายกลับมาเมื่อเชื่อมต่อสำเร็จ (Backdoor)
nc -l -p 12345 -e /bin/bash</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startReconSim('netcat')">▶ Run Simulation</button>
</div>
<div id="term-netcat" class="w-sand-term"><span class="prompt">root@kali:~#</span> [กดปุ่ม Run Simulation เพื่อจำลองคำสั่ง]</div>
</div>
<div class="w-sand-expl">
<h5>⚙️ Command Description</h5>
<p><strong>netcat (nc)</strong> เป็นเครื่องมือสารพัดประโยชน์ที่เขียนสคริปต์สแกนพอร์ต รับส่งไฟล์ หรือทำเป็น **Reverse/Bind Shell** เพื่อการขโมยสิทธิ์ควบคุมเครื่องข้ามเครือข่ายระยะไกลได้อย่างดีเยี่ยม</p>
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
window.startReconSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;

  term.innerHTML = '<span class="prompt">root@kali:~#</span> <span class="cmd">Invoking network command...</span>\\n[.] Accessing sockets\\n[.] Processing result...';

  setTimeout(() => {
    if (itemKey === 'ifconfig') {
      term.innerHTML = '<span class="prompt">root@kali:~#</span> <span class="cmd">ifconfig eth0</span>\\neth0: flags=4163&lt;UP,BROADCAST,RUNNING,MULTICAST&gt;  mtu 1500\\n        inet <span style="color:#00f0ff;">192.168.1.150</span>  netmask 255.255.255.0  broadcast 192.168.1.255\\n        ether 00:0c:29:f3:aa:5c  txqueuelen 1000  (Ethernet)\\n        RX packets 450123  bytes 12908234 (12.9 MB)\\n        TX packets 230911  bytes 29012938 (29.0 MB)';
    } else if (itemKey === 'ipaddr') {
      term.innerHTML = '<span class="prompt">root@kali:~#</span> <span class="cmd">ip -4 addr show eth0</span>\\n2: eth0: &lt;BROADCAST,MULTICAST,UP,LOWER_UP&gt; mtu 1500 qdisc fq_codel state UP group default qlen 1000\\n    inet <span style="color:#00f0ff;">192.168.1.150/24</span> brd 192.168.1.255 scope global dynamic noprefixroute eth0\\n       valid_lft 86120sec preferred_lft 86120sec';
    } else if (itemKey === 'ping') {
      term.innerHTML = '<span class="prompt">root@kali:~#</span> <span class="cmd">ping -c 3 8.8.8.8</span>\\nPING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.\\n64 bytes from 8.8.8.8: icmp_seq=1 <span style="color:#3ddc84;">ttl=128</span> time=12.5 ms\\n64 bytes from 8.8.8.8: icmp_seq=2 <span style="color:#3ddc84;">ttl=128</span> time=11.2 ms\\n64 bytes from 8.8.8.8: icmp_seq=3 <span style="color:#3ddc84;">ttl=128</span> time=14.1 ms\\n\\n--- 8.8.8.8 ping statistics ---\\n3 packets transmitted, 3 received, 0% packet loss, time 2003ms\\nrtt min/avg/max/mdev = 11.231/12.610/14.112/1.182 ms';
    } else if (itemKey === 'dnslookup') {
      term.innerHTML = '<span class="prompt">root@kali:~#</span> <span class="cmd">nslookup ctf.rpca.ac.th</span>\\nServer:         192.168.1.1\\nAddress:        192.168.1.1#53\\n\\nNon-authoritative answer:\\nName:   ctf.rpca.ac.th\\nAddress: <span style="color:#fbbf24;">202.79.45.13</span>';
    } else if (itemKey === 'netcat') {
      term.innerHTML = '<span class="prompt">root@kali:~#</span> <span class="cmd">nc -zv 192.168.1.150 21-80</span>\\nnc: connect to 192.168.1.150 port 21 (tcp) failed: Connection refused\\nnc: connect to 192.168.1.150 port 22 (tcp) <span style="color:#3ddc84;">succeeded!</span>\\nnc: connect to 192.168.1.150 port 80 (tcp) <span style="color:#3ddc84;">succeeded!</span>';
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
<p class="text-white mb-2" style="font-size:0.88rem; font-weight:600;">1. ในแบบจำลอง OSI Layer ใดทำหน้าที่ในการกำหนดทิศทางการส่งข้อมูล (Routing)? (ตอบเป็นคำภาษาอังกฤษตัวพิมพ์ใหญ่ตัวแรก เช่น Application หรือ Layer X)</p>
<div class="input-group">
<input type="text" class="form-control question-input" placeholder="คำตอบของคุณ..." data-hash="277bc1b69ad3178c775080e7221f75355694a08ba1c38fa8b79f38ebcb5c8a41" data-alt-hash="78ec09be8733f52e505820464fdbb19d45388047970d47d457cb146ef279ec3d" style="background:rgba(15,17,26,0.8) !important; border:1px solid rgba(255,255,255,0.12) !important; color:#ffffff !important; font-family:\'JetBrains Mono\',monospace; font-size:0.9rem; border-radius:6px 0 0 6px !important;">
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
<p class="text-white mb-2" style="font-size:0.88rem; font-weight:600;">2. เครื่องมือส่งและรับข้อมูลระดับ Raw network connections ที่ได้ชื่อว่าเป็น Swiss Army Knife ของนักเจาะระบบคือ? (ตอบเป็นชื่อโปรแกรมภาษาอังกฤษตัวพิมพ์เล็กทั้งหมด)</p>
<div class="input-group">
<input type="text" class="form-control question-input" placeholder="คำตอบของคุณ..." data-hash="c9b7f5256e2978000bd93d8435d648b26e03fb21884be5e38f6b864a66e4a2cd" data-alt-hash="3a95aa975765796245d8b8ff716d0046522bb33f749eb721867c4e515d18d451" style="background:rgba(15,17,26,0.8) !important; border:1px solid rgba(255,255,255,0.12) !important; color:#ffffff !important; font-family:\'JetBrains Mono\',monospace; font-size:0.9rem; border-radius:6px 0 0 6px !important;">
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
  const buf = new TextEncoder().encode(str.trim().toLowerCase());
  const hashBuf = await crypto.subtle.digest(\'SHA-256\', buf);
  const arr = Array.from(new Uint8Array(hashBuf));
  return arr.map(b => b.toString(16).padStart(2, \'0\').trim()).join(\'\');
}

// Local storage progress tracking
const lessonKey = 'solved_lesson_173';

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
  const altHash = input.getAttribute(\'data-alt-hash\');
  const val = input.value.trim();

  if (!val) {
    feedback.className = "feedback-msg mt-2 alert-warning py-1.5 px-3 text-dark";
    feedback.innerHTML = \'<i class="fas fa-exclamation-triangle mr-1"></i> กรุณากรอกคำตอบ\';
    feedback.style.setProperty(\'display\', \'block\', \'important\');
    return;
  }

  const userHash = await sha256hex(val);
  if (userHash === targetHash || (altHash && userHash === altHash)) {
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

l173.content = json.dumps(content_json, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=173).update({"content": l173.content})
db.session.commit()
print("Lesson 173 successfully updated and structured!")
ctx.pop()
