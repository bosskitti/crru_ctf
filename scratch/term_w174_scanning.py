import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l174 = db.session.query(TutorialLesson).filter_by(id=174).first()

# ─── Block 0: Core Theoretical Contents (Vulnerability Assessment & Passive Recon) ───
val0 = """## 🔍 Vulnerability Assessment (การวิเคราะห์หาช่องโหว่ทางเครือข่าย)
---

ขั้นตอนถัดจากการเรียนรู้พื้นฐานเน็ตเวิร์ก คือการใช้เทคนิคสืบค้นช่องโหว่ของเป้าหมายผ่านการวิเคราะห์ประวัติทางสาธารณะ (Passive) และสแกนจุดบกพร่องเครือข่ายเชิงรับ

### 🔎 1. Passive OSINT: Offensive Search Engine & Stack Survey
การสืบค้นหาไฟล์ความลับหรือหน้าเพจผู้ดูแลระบบด้วยคิวรีพิเศษที่ไม่ต้องการการเชื่อมต่อตรงไปยังโฮสต์:
- 🕵️‍♂️ **Google Dorking**: การเขียน Search Operators บน Google เพื่อควักไฟล์ข้อมูลลับที่ลืมซ่อน:
  - `site:ac.th intitle:index.of inurl:ftp` (กวาดหาหน้าสารบัญ FTP ของสถาบันการศึกษา)
  - `allintext:username filetype:log` (ค้นหาล็อกไฟล์ที่หลุดคำว่า username)
  - `site:th intitle:"admin login" inurl:login` (ค้นหาระบบล็อกอินสตาฟฟ์ในไทย)
- 📄 **Metagoofil**: เครื่องมือดาวน์โหลดเอกสาร (PDF, DOCX, XLSX) และ **สกัดดึงข้อมูล Metadata** ของไฟล์ออกมาเพื่อวิเคราะห์หาชื่อบัญชีผู้ใช้ (Usernames), เวอร์ชันโปรแกรม และเส้นทางที่อยู่ไฟล์ในเซิร์ฟเวอร์
- 🧱 **Technology stack survey**: การใช้สแกนเนอร์กวาดหา CMS (Content Management System) หรือเวอร์ชันซอฟต์แวร์บนหน้าเว็บ:
  - **Wappalyzer**: ส่วนขยายบราวเซอร์ชี้พิกัด Engine เว็บไซต์
  - **PublicWWW**: เสิร์ชเอนจินสแกนหาข้อความตรรกะในไฟล์ HTML/JS/CSS ในเว็บทั้งหมด
  - **BuiltWith**: ระบบวิเคราะห์เทคโนโลยีดิบของเป้าหมาย

---

### 🌐 2. Network Artifacts: Shodan & Censys
- 📡 **Host Artifacts**: วิเคราะห์ข้อมูลจดทะเบียน เช่น **WHOIS**, ค้นหาพิกัด Subdomains ดิบด้วย **DNSdumpster** หรือ Subdomain Finder
- ⚙️ **Service Artifacts**: เครื่องมือกวาดสแกนพอร์ตทั่วโลกทางสาธารณะ:
  - **Shodan**: เสิร์ชเอนจินค้นหาพิกัด IoT และอุปกรณ์ต่อเชื่อมเครือข่ายทั้งหมด ดึงข้อมูลดิบจาก Banner ที่ตอบรับกลับมา
  - **Filters สำคัญใน Shodan**:
    - `port:22` (หาพอร์ต SSH)
    - `org:"University"` (สแกนหาเฉพาะไอพีของสถาบัน)
    - `version:"1.0"` (สแกนหาเฉพาะรุ่นซอฟต์แวร์ที่มีช่องโหว่)
    - `vuln:"CVE-2021-44228"` (หาไอพีที่ติดช่องโหว่ Log4Shell)
  - **ZoomEye / Censys**: ระบบสแกนพิกัดไซเบอร์คล้ายคลึง Shodan ที่รองรับการสแกนเชิงลึก

---

### 🩺 3. Active Scanning: Ping OS Profiling & ARP
- 🏷️ **Ping Operating System Profiling**: การจำแนกประเภท OS ของเครื่องเซิร์ฟเวอร์เป้าหมายผ่านการสังเกตค่า **TTL (Time to Live)** ในผลลัพธ์ ICMP Reply:
  - **Linux / MacOS**: จะตอบรับกลับมาด้วยค่า TTL เริ่มต้นประมาณ `64`
  - **Windows (ทุกเวอร์ชัน)**: จะตอบรับกลับมาด้วยค่า TTL เริ่มต้นประมาณ `128`
  - **Network Devices / Routers**: มักมีค่า TTL เริ่มต้นเป็น `255`
- 🖇️ **ARP (Address Resolution Protocol)**: โปรโตคอลสกัดแปลง IP Address ให้กลายเป็น MAC Address สำหรับสายเน็ตเวิร์กแลนวงเดียวกัน"""

# ─── Block 1: Vulnerability Assessment Sandbox (Live Terminal Simulator) ───
val1 = """### 💻 Passive Recon & Scan Coding Sandbox (จำลองเครื่องมือสแกนหาช่องโหว่)

คลิกหัวข้อด้านซ้ายมือเพื่อศึกษาตัวอย่างเครื่องมือสำรวจหาช่องโหว่ และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลลัพธ์ผ่านเทอร์มินัลระบบ:

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
<button id="nav-item-dork" class="w-nav-item active" onclick="showSandboxItem('dork', this)">1. Google Dorking</button>
<button id="nav-item-metagoofil" class="w-nav-item" onclick="showSandboxItem('metagoofil', this)">2. Metagoofil Extraction</button>
<button id="nav-item-shodan" class="w-nav-item" onclick="showSandboxItem('shodan', this)">3. Shodan Scanner Query</button>
<button id="nav-item-pingttl" class="w-nav-item" onclick="showSandboxItem('pingttl', this)">4. Ping TTL Fingerprint</button>
<button id="nav-item-arp" class="w-nav-item" onclick="showSandboxItem('arp', this)">5. ARP cache (arp -a)</button>
</div>

<!-- Panel details right side -->
<div class="w-sandbox-panels">

<!-- 1. Google Dork -->
<div id="panel-dork" class="w-sand-panel">
<div class="w-sand-hdr"><span>1. Google Dorking Operator</span> <span class="tag">Google API</span></div>
<pre class="w-sand-code"># สแกนหาล็อกไฟล์ของระบบที่มีคำว่า username ในหน่วยงานไทย
"allintext:username filetype:log site:th"</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startScanSim('dork')">▶ Run Simulation</button>
</div>
<div id="term-dork" class="w-sand-term"><span class="prompt">google-dork-tool$</span> [กดปุ่ม Run Simulation เพื่อจำลองคิวรี]</div>
</div>
<div class="w-sand-expl">
<h5>⚙️ Command Description</h5>
<p>คิวรีนี้สั่งให้กูเกิลกรองแสดงเฉพาะล็อกไฟล์ระบบบนโดเมนของประเทศไทย เพื่อเป้าหมายประเมินระบบที่ลืมจำกัดสิทธิ์ความลับ</p>
</div>
</div>

<!-- 2. Metagoofil -->
<div id="panel-metagoofil" class="w-sand-panel">
<div class="w-sand-hdr"><span>2. Metagoofil Metadata Extractor</span> <span class="tag">Linux CLI</span></div>
<pre class="w-sand-code"># ดาวน์โหลดและสกัด Metadata ไฟล์ PDF ทั้งหมดของหน่วยงานเป้าหมาย
metagoofil -d rpca.ac.th -t pdf -l 20 -n 10 -o target_docs</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startScanSim('metagoofil')">▶ Run Simulation</button>
</div>
<div id="term-metagoofil" class="w-sand-term"><span class="prompt">root@kali:~#</span> [กดปุ่ม Run Simulation เพื่อจำลองประมวลผล]</div>
</div>
<div class="w-sand-expl">
<h5>⚙️ Command Description</h5>
<p><strong>Metagoofil</strong> จะดาวน์โหลดไฟล์ PDF สูงสุด 10 ไฟล์จากเป้าหมายมาสกัดดูชื่อโปรแกรมเอกสารและ Usernames ที่เป็นผู้บันทึกสร้างไฟล์</p>
</div>
</div>

<!-- 3. Shodan -->
<div id="panel-shodan" class="w-sand-panel">
<div class="w-sand-hdr"><span>3. Shodan Cyberspace Search</span> <span class="tag">Shodan API</span></div>
<pre class="w-sand-code"># ค้นหาโฮสต์ที่ติดตั้งโปรแกรม Apache HTTPD ในโดเมนประเทศไทย
"product:\"Apache HTTPD\" country:\"TH\""</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startScanSim('shodan')">▶ Run Simulation</button>
</div>
<div id="term-shodan" class="w-sand-term"><span class="prompt">shodan-cli$</span> [กดปุ่ม Run Simulation เพื่อจำลองคิวรี]</div>
</div>
<div class="w-sand-expl">
<h5>⚙️ Command Description</h5>
<p>สืบค้นหาบริการ Apache Web Server เฉพาะในวง IP Address ที่ถูกพิกัดขึ้นตรงอยู่ในประเทศไทย (TH)</p>
</div>
</div>

<!-- 4. Ping TTL -->
<div id="panel-pingttl" class="w-sand-panel">
<div class="w-sand-hdr"><span>4. OS Fingerprinting via TTL</span> <span class="tag">Linux CLI</span></div>
<pre class="w-sand-code"># ตรวจสอบแพ็กเก็ตตอบรับกลับมาจากการส่ง Ping
ping -c 2 172.19.19.130</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startScanSim('pingttl')">▶ Run Simulation</button>
</div>
<div id="term-pingttl" class="w-sand-term"><span class="prompt">root@kali:~#</span> [กดปุ่ม Run Simulation เพื่อจำลองการวิเคราะห์]</div>
</div>
<div class="w-sand-expl">
<h5>⚙️ Command Description</h5>
<p>การดูฟีเจอร์ TTL ใน ICMP packet ช่วยให้สลัดหาเป้าหมายได้รวดเร็วโดยไม่จำเป็นต้องสแกนพอร์ตแบบเปิดเผยร่องรอยการยิงมากนัก</p>
</div>
</div>

<!-- 5. arp -a -->
<div id="panel-arp" class="w-sand-panel">
<div class="w-sand-hdr"><span>5. Address Resolution Cache (arp)</span> <span class="tag">Linux CLI</span></div>
<pre class="w-sand-code"># แสดงตารางประวัติ MAC Address ที่คุยกันในระบบ LAN
arp -a</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startScanSim('arp')">▶ Run Simulation</button>
</div>
<div id="term-arp" class="w-sand-term"><span class="prompt">root@kali:~#</span> [กดปุ่ม Run Simulation เพื่อจำลองคำสั่ง]</div>
</div>
<div class="w-sand-expl">
<h5>⚙️ Command Description</h5>
<p><strong>arp</strong> ดึงตารางประวัติ ARP cache ที่เก็บรักษาพิกัดคู่ IP และ MAC Address ของการ์ดเน็ตเวิร์กที่คุยกันล่าสุด</p>
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
window.startScanSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;

  term.innerHTML = '<span class="prompt">root@kali:~#</span> <span class="cmd">Searching cyberspace indexes...</span>\\n[.] Accessing remote caches\\n[.] Filtering records...';

  setTimeout(() => {
    if (itemKey === 'dork') {
      term.innerHTML = '<span class="prompt">google-dork-tool$</span> <span class="cmd">query="allintext:username filetype:log site:th"</span>\\n[+] Results found: 2\\n\\n1. http://example.in.th/sys.log (Exposed root logins)\\n2. http://ctf-target.ac.th/logs/error.log (Apache Auth debug info)';
    } else if (itemKey === 'metagoofil') {
      term.innerHTML = '<span class="prompt">root@kali:~#</span> <span class="cmd">metagoofil -d rpca.ac.th -t pdf -n 2</span>\\n[*] Searching for pdf files in rpca.ac.th...\\n[+] Found 2 pdf files. Downloading...\\n\\n[+] Extracting metadata...\\n- File: handbook.pdf | Creator: <span style="color:#00f0ff;">wongyos.k</span> | OS: Windows 10\\n- File: rules.pdf | Creator: <span style="color:#00f0ff;">admin_staff</span> | Software: Microsoft Word 2016';
    } else if (itemKey === 'shodan') {
      term.innerHTML = '<span class="prompt">shodan-cli$</span> <span class="cmd">shodan search product:"Apache HTTPD" country:"TH"</span>\\nIP: 202.79.45.13 | Port: 80 | ISP: TOT | Version: 2.4.41\\nIP: 202.79.45.54 | Port: 80 | ISP: AIS | Version: 2.4.29\\nIP: 110.164.5.12 | Port: 8080 | ISP: True | Version: 2.4.41';
    } else if (itemKey === 'pingttl') {
      term.innerHTML = '<span class="prompt">root@kali:~#</span> <span class="cmd">ping -c 1 172.19.19.130</span>\\nPING 172.19.19.130 (172.19.19.130) 56(84) bytes of data.\\n64 bytes from 172.19.19.130: icmp_seq=1 <span style="color:#3ddc84; font-weight:bold;">ttl=64</span> time=2.1 ms\\n\\n--- OS profiling summary: <span style="color:#3ddc84;">Target is running LINUX/UNIX (TTL=64)</span> ---';
    } else if (itemKey === 'arp') {
      term.innerHTML = '<span class="prompt">root@kali:~#</span> <span class="cmd">arp -a</span>\\ngateway (192.168.1.1) at 00:50:56:c0:00:01 [ether] on eth0\\ntarget_host (192.168.1.102) at <span style="color:#fbbf24;">00:0c:29:b4:ee:12</span> [ether] on eth0';
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
<p class="text-white mb-2" style="font-size:0.88rem; font-weight:600;">1. หากผลลัพธ์ Ping ไปยังเครื่องเป้าหมายในเครือข่ายมีค่า TTL เริ่มต้นตอบรับกลับมาเป็น 128 ระบบปฏิบัติการเป้าหมายมีแนวโน้มรันด้วยอะไร? (ตอบชื่อระบบปฏิบัติการภาษาอังกฤษตัวพิมพ์ใหญ่ตัวแรก เช่น Linux, Windows, macOS)</p>
<div class="input-group">
<input type="text" class="form-control question-input" placeholder="คำตอบของคุณ..." data-hash="dbb48a804b49cb376e107297e64177d612e694fb4e8ecfde4e0735cf1f3918a5" style="background:rgba(15,17,26,0.8) !important; border:1px solid rgba(255,255,255,0.12) !important; color:#ffffff !important; font-family:\'JetBrains Mono\',monospace; font-size:0.9rem; border-radius:6px 0 0 6px !important;">
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
<p class="text-white mb-2" style="font-size:0.88rem; font-weight:600;">2. Google Dorking query tag ใดใช้เพื่อระบุขอบเขตการสแกนหาเฉพาะเจาะจงเว็บไซต์เป้าหมาย? (ระบุคีย์เวิร์ดรวมเครื่องหมายโคลอน เช่น ext:)</p>
<div class="input-group">
<input type="text" class="form-control question-input" placeholder="คำตอบของคุณ..." data-hash="476ca8cf30a3b2b3cc76785dc9ebf3bc4cd22d8d85f81e7d23a1058ad646c075" style="background:rgba(15,17,26,0.8) !important; border:1px solid rgba(255,255,255,0.12) !important; color:#ffffff !important; font-family:\'JetBrains Mono\',monospace; font-size:0.9rem; border-radius:6px 0 0 6px !important;">
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
const lessonKey = 'solved_lesson_174';

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

l174.content = json.dumps(content_json, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=174).update({"content": l174.content})
db.session.commit()
print("Lesson 174 successfully updated and structured!")
ctx.pop()
