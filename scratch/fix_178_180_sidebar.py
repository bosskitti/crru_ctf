"""
Fix Lessons 178, 179, 180 Block 1 sidebar to match Chapter 4 CSS class pattern.
Each lesson gets its own accent color:
- 178: purple (#a855f7)
- 179: blue (#3b82f6)
- 180: green (#10b981)
"""
import json, sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app

app = create_app()

# ── LESSON 178: Directory & HTTP Diagnostic (purple theme) ──
SANDBOX_178 = r"""### 💻 Directory & HTTP Diagnostic Sandbox (จำลองค้นหาไฟล์และยิงคำสั่ง)

คลิกหัวข้อด้านซ้ายมือเพื่อศึกษาตัวอย่างการทำแล็บจำลองความปลอดภัย และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลลัพธ์:

<style>
.w-sandbox-main{display:flex;gap:20px;margin:2rem auto;max-width:1050px;}
@media(max-width:820px){.w-sandbox-main{flex-direction:column;}}
.w-sandbox-nav{width:220px;display:flex;flex-direction:column;gap:6px;flex-shrink:0;}
@media(max-width:820px){.w-sandbox-nav{width:100%;flex-direction:row;flex-wrap:wrap;}}
.w-nav-item{padding:8px 12px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.04);border-radius:6px;font-size:0.75rem;color:#cbd5e1;cursor:pointer;text-align:left;transition:all 0.15s ease;}
.w-nav-item:hover, .w-nav-item.active{border-color:#a855f7;color:#ffffff;background:rgba(168,85,247,0.04);}
.w-nav-item.active{font-weight:bold;box-shadow:0 0 8px rgba(168,85,247,0.15);}
.w-sandbox-panels{flex:1;display:flex;flex-direction:column;gap:14px;}
.w-sand-panel{display:none;background:#05070f;border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:20px;box-shadow:0 8px 24px rgba(0,0,0,0.45);box-sizing:border-box;}
.w-sand-panel.active{display:block !important;}
.w-sand-hdr{font-size:0.95rem;font-weight:800;color:#ffffff;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:10px;margin-bottom:14px;display:flex;justify-content:space-between;align-items:center;}
.w-sand-hdr span.tag{font-size:0.65rem;padding:2px 8px;border-radius:4px;background:rgba(168,85,247,0.08);border:1px solid rgba(168,85,247,0.2);color:#a855f7;font-family:'JetBrains Mono',monospace;}
.w-sand-code{font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#a855f7;white-space:pre-wrap;margin:0 0 12px;background:rgba(0,0,0,0.2);padding:14px;border-radius:8px;border:1px solid rgba(255,255,255,0.02);}
.w-sand-term-container{position:relative;background:#02040a;border:1px solid rgba(255,255,255,0.06);border-radius:8px;margin-bottom:16px;box-shadow:inset 0 2px 8px rgba(0,0,0,0.9);overflow:hidden;}
.w-sand-term-bar{background:rgba(255,255,255,0.03);padding:6px 12px;border-bottom:1px solid rgba(255,255,255,0.05);display:flex;justify-content:space-between;align-items:center;}
.w-sand-term-title{font-size:0.65rem;color:#64748b;font-weight:800;letter-spacing:0.06em;font-family:'JetBrains Mono',monospace;}
.w-sand-term-btn{background:rgba(168,85,247,0.1);border:1px solid rgba(168,85,247,0.3);border-radius:4px;color:#a855f7;font-size:0.68rem;padding:3px 8px;cursor:pointer;font-family:'JetBrains Mono',monospace;font-weight:700;transition:all 0.15s ease;display:flex;align-items:center;gap:4px;}
.w-sand-term-btn:hover{background:#a855f7;color:#02040a;box-shadow:0 0 8px rgba(168,85,247,0.4);}
.w-sand-term{font-family:'JetBrains Mono',monospace;font-size:0.76rem;color:#a7f3d0;padding:12px 16px;white-space:pre-wrap;min-height:90px;}
.w-sand-term span.prompt{color:#3ddc84;}
.w-sand-term span.cmd{color:#ffffff;font-weight:bold;}
.w-sand-expl{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:16px;font-size:0.83rem;color:#cbd5e1;line-height:1.65;}
.w-sand-expl h5{margin:0 0 8px;font-size:0.85rem;color:#fbbf24;font-weight:bold;}
.w-sand-expl p{margin:0 0 10px;}
.w-sand-expl p:last-child{margin-bottom:0;}
</style>
<div class="w-sandbox-main"><div class="w-sandbox-nav"><button id="nav-item-dirb" class="w-nav-item active" onclick="showSandboxItem('dirb', this)">1. Dirb Backup Scan</button><button id="nav-item-curl" class="w-nav-item" onclick="showSandboxItem('curl', this)">2. cURL HTTP Audit</button></div><div class="w-sandbox-panels"><div id="panel-dirb" class="w-sand-panel active"><div class="w-sand-hdr"><span>1. Brute-forcing Web Backups with Dirb</span> <span class="tag">Dirb Scanner</span></div><pre class="w-sand-code">dirb http://ctf.rpca.ac.th/ /usr/share/wordlists/dirb/common.txt -X .zip,.bak</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startPostSim('dirb')">▶ Run Simulation</button></div><div id="term-dirb" class="w-sand-term"><span class="prompt">kali$</span> [กดปุ่ม Run Simulation เพื่อยิงคำสั่ง Dirb]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>คำสั่งค้นหาไฟล์สำรอง (เช่น .zip หรือ .bak) ในรากโฮสต์เป้าหมาย เพื่อตรวจจับความเสื่อมสภาพของข้อมูลสำคัญ</p></div></div><div id="panel-curl" class="w-sand-panel"><div class="w-sand-hdr"><span>2. cURL HTTP OPTIONS Audit</span> <span class="tag">cURL Tool</span></div><pre class="w-sand-code">curl -X OPTIONS -i http://ctf.rpca.ac.th/</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startPostSim('curl')">▶ Run Simulation</button></div><div id="term-curl" class="w-sand-term"><span class="prompt">kali$</span> [กดปุ่ม Run Simulation เพื่อรันคำสั่ง cURL]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>เมธอด OPTIONS ใช้ทดสอบเพื่อขอข้อมูลรายการ HTTP methods ทั้งหมดที่เว็บเซิร์ฟเวอร์เปิดไว้ทำงาน</p></div></div></div></div>
<script>
window.showSandboxItem = function(itemKey, element) {
  var items = document.querySelectorAll('.w-sandbox-nav .w-nav-item');
  items.forEach(function(i) { i.classList.remove('active'); });
  element.classList.add('active');
  var panels = document.querySelectorAll('.w-sand-panel');
  panels.forEach(function(p) { p.classList.remove('active'); });
  var targetPanel = document.getElementById('panel-' + itemKey);
  if (targetPanel) { targetPanel.classList.add('active'); }
}
window.startPostSim = function(itemKey) {
  var term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span class="prompt">kali$</span> <span class="cmd">Running audit checks...</span>\n[.] Connecting target server...';
  setTimeout(function() {
    if (itemKey === 'dirb') {
      term.innerHTML = '<span class="prompt">kali$</span> <span style="color:#3ddc84; font-weight:bold;">DIRB scan results:</span>\nFOUND: http://ctf.rpca.ac.th/backup.zip (CODE: 200)\nFOUND: http://ctf.rpca.ac.th/old_site.bak (CODE: 200)\n\n[+] Dirb completed successfully!';
    } else if (itemKey === 'curl') {
      term.innerHTML = '<span class="prompt">kali$</span> <span style="color:#a855f7; font-weight:bold;">HTTP/1.1 200 OK</span>\nAllow: GET, POST, OPTIONS, TRACE, WebDAV\nServer: Apache/2.4.41 (Ubuntu)\nContent-Length: 0\n\n[+] OPTIONS check finished.';
    }
  }, 1000);
}
setTimeout(function() {
  var activeBtn = document.querySelector('.w-sandbox-nav .w-nav-item.active');
  if (activeBtn) { activeBtn.click(); }
}, 100);
</script>"""

# ── LESSON 179: SQLi & Command Injection Lab (blue theme) ──
SANDBOX_179 = r"""### 💻 SQLi & Command Injection Lab Simulator (จำลองการแทรกคำสั่งประมวลผล)

คลิกหัวข้อด้านซ้ายมือเพื่อศึกษาช่องโหว่ และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลการแทรกคำสั่ง:

<style>
.w-sandbox-main{display:flex;gap:20px;margin:2rem auto;max-width:1050px;}
@media(max-width:820px){.w-sandbox-main{flex-direction:column;}}
.w-sandbox-nav{width:220px;display:flex;flex-direction:column;gap:6px;flex-shrink:0;}
@media(max-width:820px){.w-sandbox-nav{width:100%;flex-direction:row;flex-wrap:wrap;}}
.w-nav-item{padding:8px 12px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.04);border-radius:6px;font-size:0.75rem;color:#cbd5e1;cursor:pointer;text-align:left;transition:all 0.15s ease;}
.w-nav-item:hover, .w-nav-item.active{border-color:#3b82f6;color:#ffffff;background:rgba(59,130,246,0.04);}
.w-nav-item.active{font-weight:bold;box-shadow:0 0 8px rgba(59,130,246,0.15);}
.w-sandbox-panels{flex:1;display:flex;flex-direction:column;gap:14px;}
.w-sand-panel{display:none;background:#05070f;border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:20px;box-shadow:0 8px 24px rgba(0,0,0,0.45);box-sizing:border-box;}
.w-sand-panel.active{display:block !important;}
.w-sand-hdr{font-size:0.95rem;font-weight:800;color:#ffffff;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:10px;margin-bottom:14px;display:flex;justify-content:space-between;align-items:center;}
.w-sand-hdr span.tag{font-size:0.65rem;padding:2px 8px;border-radius:4px;background:rgba(59,130,246,0.08);border:1px solid rgba(59,130,246,0.2);color:#3b82f6;font-family:'JetBrains Mono',monospace;}
.w-sand-code{font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#3b82f6;white-space:pre-wrap;margin:0 0 12px;background:rgba(0,0,0,0.2);padding:14px;border-radius:8px;border:1px solid rgba(255,255,255,0.02);}
.w-sand-term-container{position:relative;background:#02040a;border:1px solid rgba(255,255,255,0.06);border-radius:8px;margin-bottom:16px;box-shadow:inset 0 2px 8px rgba(0,0,0,0.9);overflow:hidden;}
.w-sand-term-bar{background:rgba(255,255,255,0.03);padding:6px 12px;border-bottom:1px solid rgba(255,255,255,0.05);display:flex;justify-content:space-between;align-items:center;}
.w-sand-term-title{font-size:0.65rem;color:#64748b;font-weight:800;letter-spacing:0.06em;font-family:'JetBrains Mono',monospace;}
.w-sand-term-btn{background:rgba(59,130,246,0.1);border:1px solid rgba(59,130,246,0.3);border-radius:4px;color:#3b82f6;font-size:0.68rem;padding:3px 8px;cursor:pointer;font-family:'JetBrains Mono',monospace;font-weight:700;transition:all 0.15s ease;display:flex;align-items:center;gap:4px;}
.w-sand-term-btn:hover{background:#3b82f6;color:#02040a;box-shadow:0 0 8px rgba(59,130,246,0.4);}
.w-sand-term{font-family:'JetBrains Mono',monospace;font-size:0.76rem;color:#a7f3d0;padding:12px 16px;white-space:pre-wrap;min-height:90px;}
.w-sand-term span.prompt{color:#3ddc84;}
.w-sand-term span.cmd{color:#ffffff;font-weight:bold;}
.w-sand-expl{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:16px;font-size:0.83rem;color:#cbd5e1;line-height:1.65;}
.w-sand-expl h5{margin:0 0 8px;font-size:0.85rem;color:#fbbf24;font-weight:bold;}
.w-sand-expl p{margin:0 0 10px;}
.w-sand-expl p:last-child{margin-bottom:0;}
</style>
<div class="w-sandbox-main"><div class="w-sandbox-nav"><button id="nav-item-sqlitest" class="w-nav-item active" onclick="showSandboxItem('sqlitest', this)">1. UNION SQLi Test</button><button id="nav-item-cmdtest" class="w-nav-item" onclick="showSandboxItem('cmdtest', this)">2. OS Command Injection</button></div><div class="w-sandbox-panels"><div id="panel-sqlitest" class="w-sand-panel active"><div class="w-sand-hdr"><span>1. UNION-Based SQL Injection Simulation</span> <span class="tag">UNION SQLi</span></div><pre class="w-sand-code">' UNION SELECT null, username, password FROM users --</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startPostSim('sqlitest')">▶ Run Simulation</button></div><div id="term-sqlitest" class="w-sand-term"><span class="prompt">db-cli$</span> [กดปุ่ม Run Simulation เพื่อส่ง UNION payload]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>คิวรีผสาน UNION SELECT ช่วยให้เราแอบไปดึงข้อมูลผู้ใช้งานและรหัสผ่านจากตารางอื่นออกมาทางเว็บบอร์ดแสดงผล</p></div></div><div id="panel-cmdtest" class="w-sand-panel"><div class="w-sand-hdr"><span>2. OS Command Injection Bypass Space</span> <span class="tag">OS Command</span></div><pre class="w-sand-code">cat${IFS}/etc/passwd</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startPostSim('cmdtest')">▶ Run Simulation</button></div><div id="term-cmdtest" class="w-sand-term"><span class="prompt">kali$</span> [กดปุ่ม Run Simulation เพื่อส่งคำสั่ง]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>การเขียนตัวแปร IFS ช่วยเลี่ยงการกรองช่องว่าง ทำให้คำสั่งสามารถรันเพื่อเรียกดูไฟล์ระบบปฏิบัติการได้เหมือนเดิม</p></div></div></div></div>
<script>
window.showSandboxItem = function(itemKey, element) {
  var items = document.querySelectorAll('.w-sandbox-nav .w-nav-item');
  items.forEach(function(i) { i.classList.remove('active'); });
  element.classList.add('active');
  var panels = document.querySelectorAll('.w-sand-panel');
  panels.forEach(function(p) { p.classList.remove('active'); });
  var targetPanel = document.getElementById('panel-' + itemKey);
  if (targetPanel) { targetPanel.classList.add('active'); }
}
window.startPostSim = function(itemKey) {
  var term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span class="prompt">kali$</span> <span class="cmd">Executing commands...</span>\n[.] Verifying backend sanitization checks...';
  setTimeout(function() {
    if (itemKey === 'sqlitest') {
      term.innerHTML = '<span class="prompt">db-cli$</span> <span style="color:#3ddc84; font-weight:bold;">UNION select output:</span>\nID: null | User: admin | Pass: <span style="color:#ef4444;">$2y$10$xyzPasswordHash...</span>\nID: null | User: user1 | Pass: <span style="color:#ef4444;">$2y$10$abcHashUser1...</span>\n\n[+] Data exfiltration successful!';
    } else if (itemKey === 'cmdtest') {
      term.innerHTML = '<span class="prompt">kali$</span> <span style="color:#3ddc84; font-weight:bold;">cat /etc/passwd:</span>\nroot:x:0:0:root:/root:/bin/bash\nbin:x:1:1:bin:/bin:/sbin/nologin\n\n[+] Command completed without spaces.';
    }
  }, 1000);
}
setTimeout(function() {
  var activeBtn = document.querySelector('.w-sandbox-nav .w-nav-item.active');
  if (activeBtn) { activeBtn.click(); }
}, 100);
</script>"""

# ── LESSON 180: CMS Security Audit (green theme) ──
SANDBOX_180 = r"""### 💻 CMS Security Audit Sandbox (จำลองเรียกสแกนความปลอดภัย CMS)

คลิกหัวข้อด้านซ้ายมือเพื่อศึกษาขั้นตอน และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลการสแกนความเปราะบาง:

<style>
.w-sandbox-main{display:flex;gap:20px;margin:2rem auto;max-width:1050px;}
@media(max-width:820px){.w-sandbox-main{flex-direction:column;}}
.w-sandbox-nav{width:220px;display:flex;flex-direction:column;gap:6px;flex-shrink:0;}
@media(max-width:820px){.w-sandbox-nav{width:100%;flex-direction:row;flex-wrap:wrap;}}
.w-nav-item{padding:8px 12px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.04);border-radius:6px;font-size:0.75rem;color:#cbd5e1;cursor:pointer;text-align:left;transition:all 0.15s ease;}
.w-nav-item:hover, .w-nav-item.active{border-color:#10b981;color:#ffffff;background:rgba(16,185,129,0.04);}
.w-nav-item.active{font-weight:bold;box-shadow:0 0 8px rgba(16,185,129,0.15);}
.w-sandbox-panels{flex:1;display:flex;flex-direction:column;gap:14px;}
.w-sand-panel{display:none;background:#05070f;border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:20px;box-shadow:0 8px 24px rgba(0,0,0,0.45);box-sizing:border-box;}
.w-sand-panel.active{display:block !important;}
.w-sand-hdr{font-size:0.95rem;font-weight:800;color:#ffffff;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:10px;margin-bottom:14px;display:flex;justify-content:space-between;align-items:center;}
.w-sand-hdr span.tag{font-size:0.65rem;padding:2px 8px;border-radius:4px;background:rgba(16,185,129,0.08);border:1px solid rgba(16,185,129,0.2);color:#10b981;font-family:'JetBrains Mono',monospace;}
.w-sand-code{font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#10b981;white-space:pre-wrap;margin:0 0 12px;background:rgba(0,0,0,0.2);padding:14px;border-radius:8px;border:1px solid rgba(255,255,255,0.02);}
.w-sand-term-container{position:relative;background:#02040a;border:1px solid rgba(255,255,255,0.06);border-radius:8px;margin-bottom:16px;box-shadow:inset 0 2px 8px rgba(0,0,0,0.9);overflow:hidden;}
.w-sand-term-bar{background:rgba(255,255,255,0.03);padding:6px 12px;border-bottom:1px solid rgba(255,255,255,0.05);display:flex;justify-content:space-between;align-items:center;}
.w-sand-term-title{font-size:0.65rem;color:#64748b;font-weight:800;letter-spacing:0.06em;font-family:'JetBrains Mono',monospace;}
.w-sand-term-btn{background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.3);border-radius:4px;color:#10b981;font-size:0.68rem;padding:3px 8px;cursor:pointer;font-family:'JetBrains Mono',monospace;font-weight:700;transition:all 0.15s ease;display:flex;align-items:center;gap:4px;}
.w-sand-term-btn:hover{background:#10b981;color:#02040a;box-shadow:0 0 8px rgba(16,185,129,0.4);}
.w-sand-term{font-family:'JetBrains Mono',monospace;font-size:0.76rem;color:#a7f3d0;padding:12px 16px;white-space:pre-wrap;min-height:90px;}
.w-sand-term span.prompt{color:#3ddc84;}
.w-sand-term span.cmd{color:#ffffff;font-weight:bold;}
.w-sand-expl{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:16px;font-size:0.83rem;color:#cbd5e1;line-height:1.65;}
.w-sand-expl h5{margin:0 0 8px;font-size:0.85rem;color:#fbbf24;font-weight:bold;}
.w-sand-expl p{margin:0 0 10px;}
.w-sand-expl p:last-child{margin-bottom:0;}
</style>
<div class="w-sandbox-main"><div class="w-sandbox-nav"><button id="nav-item-wpscan" class="w-nav-item active" onclick="showSandboxItem('wpscan', this)">1. WPScan Vulnerability</button><button id="nav-item-joomscan" class="w-nav-item" onclick="showSandboxItem('joomscan', this)">2. JoomScan Audit</button></div><div class="w-sandbox-panels"><div id="panel-wpscan" class="w-sand-panel active"><div class="w-sand-hdr"><span>1. Scanning WordPress Vulnerabilities with WPScan</span> <span class="tag">WPScan Tool</span></div><pre class="w-sand-code">wpscan --url http://ctf.rpca.ac.th/wp/ --enumerate vp,u</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startPostSim('wpscan')">▶ Run Simulation</button></div><div id="term-wpscan" class="w-sand-term"><span class="prompt">kali$</span> [กดปุ่ม Run Simulation เพื่อยิงสแกน WPScan]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>คำสั่งค้นหาระบุปลั๊กอินที่มีช่องโหว่ความเสี่ยง (vp) และตรวจสอบรายชื่อผู้ใช้งาน (u) เพื่อวางสเปกประเมินความปลอดภัย</p></div></div><div id="panel-joomscan" class="w-sand-panel"><div class="w-sand-hdr"><span>2. Assessing Joomla Website Security with JoomScan</span> <span class="tag">JoomScan Tool</span></div><pre class="w-sand-code">joomscan -u http://ctf.rpca.ac.th/joomla/ --components</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startPostSim('joomscan')">▶ Run Simulation</button></div><div id="term-joomscan" class="w-sand-term"><span class="prompt">kali$</span> [กดปุ่ม Run Simulation เพื่อเริ่มทำ JoomScan]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>เมธอดตรวจสอบส่วนประกอบเสริม Joomla (components) เพื่อสืบค้นจุดรั่วไหลของซอร์สโค้ดและไลบรารีส่วนตัว</p></div></div></div></div>
<script>
window.showSandboxItem = function(itemKey, element) {
  var items = document.querySelectorAll('.w-sandbox-nav .w-nav-item');
  items.forEach(function(i) { i.classList.remove('active'); });
  element.classList.add('active');
  var panels = document.querySelectorAll('.w-sand-panel');
  panels.forEach(function(p) { p.classList.remove('active'); });
  var targetPanel = document.getElementById('panel-' + itemKey);
  if (targetPanel) { targetPanel.classList.add('active'); }
}
window.startPostSim = function(itemKey) {
  var term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span class="prompt">kali$</span> <span class="cmd">Running CMS mapping audits...</span>\n[.] Executing target scanner engines...';
  setTimeout(function() {
    if (itemKey === 'wpscan') {
      term.innerHTML = '<span class="prompt">kali$</span> <span style="color:#3ddc84; font-weight:bold;">WPScan Output:</span>\nWordPress version: 6.2.2 (Outdated)\nFOUND User: admin (ID: 1)\nFOUND Vulnerable Plugin: contact-form-7 v5.7.1 (XSS vulnerable)\n\n[+] WPScan Completed!';
    } else if (itemKey === 'joomscan') {
      term.innerHTML = '<span class="prompt">kali$</span> <span style="color:#3ddc84; font-weight:bold;">OWASP Joomla! Vulnerability Scanner:</span>\nJoomla! version: 3.9.22 (Outdated)\nFOUND: http://ctf.rpca.ac.th/joomla/configuration.php-bak (CODE: 200)\n\n[+] JoomScan completed successfully.';
    }
  }, 1000);
}
setTimeout(function() {
  var activeBtn = document.querySelector('.w-sandbox-nav .w-nav-item.active');
  if (activeBtn) { activeBtn.click(); }
}, 100);
</script>"""

with app.app_context():
    from CTFd.plugins.tutorials import TutorialLesson
    db = app.db
    updates = {
        178: SANDBOX_178,
        179: SANDBOX_179,
        180: SANDBOX_180,
    }
    for lid, new_val in updates.items():
        lesson = db.session.query(TutorialLesson).filter_by(id=lid).first()
        if not lesson:
            print(f"[!] Lesson {lid} not found")
            continue
        blocks = json.loads(lesson.content)
        blocks[1]["value"] = new_val
        lesson.content = json.dumps(blocks, ensure_ascii=False)
        db.session.commit()
        print(f"[OK] Lesson {lid} Block 1 updated with Chapter-4 style sidebar!")

    print("\n[DONE] All Module 5 sandboxes now use Chapter-4 CSS class pattern!")
