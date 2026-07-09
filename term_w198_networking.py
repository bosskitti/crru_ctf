import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l198 = db.session.query(TutorialLesson).filter_by(id=198).first()
blocks = json.loads(l198.content)

# ─── Upgrade Block 2 of Lesson 198 to include Live Flow Terminal Simulation ───
blocks[2]['value'] = """### 💻 Network Scanning Coding Console (วิเคราะห์ 3 ตัวอย่างโค้ดเครือข่าย)

คลิกหัวข้อด้านซ้ายมือเพื่อตรวจสอบตัวอย่างโค้ดวิเคราะห์เครือข่าย และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลลัพธ์ผ่านเทอร์มินัลระบบ:

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

/* Terminal simulation container */
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
<button id="nav-item-socket_scan" class="w-nav-item active" onclick="showSandboxItem('socket_scan', this)">1. Socket Port Scanning</button>
<button id="nav-item-scapy_arp" class="w-nav-item" onclick="showSandboxItem('scapy_arp', this)">2. Scapy Packet Crafting</button>
<button id="nav-item-nmap_scan" class="w-nav-item" onclick="showSandboxItem('nmap_scan', this)">3. python-nmap Wrapper</button>
</div>

<!-- Panel details right side -->
<div class="w-sandbox-panels">

<!-- 1. Socket Scan -->
<div id="panel-socket_scan" class="w-sand-panel">
<div class="w-sand-hdr"><span>1. Socket Port Scanning</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import socket

target = "127.0.0.1"
ports = [21, 22, 80, 443, 8080]

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port}: OPEN")
    s.close()</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startNetSim('socket_scan')">▶ Run Simulation</button>
</div>
<div id="term-socket_scan" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation ด้านขวาบนเพื่อจำลองการเรียกใช้งาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>สคริปต์สแกนตรวจสอบพอร์ตแบบระบายการเชื่อมต่อระดับล่าง (TCP Three-way Handshake):</p>
<ul>
<li><strong>connect_ex((target, port))</strong>: ดำเนินการลองเชื่อมต่อตรง หากสำเร็จจะส่งรหัสตอบรับกลับมาเป็น <code>0</code> (พอร์ตเปิดอยู่)</li>
</ul>
</div>
</div>

<!-- 2. Scapy ARP -->
<div id="panel-scapy_arp" class="w-sand-panel">
<div class="w-sand-hdr"><span>2. Scapy Packet Crafting</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">from scapy.all import ARP, Ether, srp

target_ip = "192.168.1.0/24"
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
arp = ARP(pdst=target_ip)
packet = ether/arp

result = srp(packet, timeout=2, verbose=0)[0]
for sent, received in result:
    print(f"IP: {received.psrc} | MAC: {received.hwsrc}")</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startNetSim('scapy_arp')">▶ Run Simulation</button>
</div>
<div id="term-scapy_arp" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation ด้านขวาบนเพื่อจำลองการเรียกใช้งาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การสร้างแพ็กเก็ต ARP Request เพื่อกวาดหาเครื่องที่เปิดทำงานในเครือข่าย:</p>
<ul>
<li><strong>Ether(dst="ff:ff:ff:ff:ff:ff")</strong>: ส่งสัญญาณแพร่ภาพ (Broadcast) ไปในวงเครือข่ายเพื่อดึงพิกัดจริง (MAC Address) กลับคืน</li>
</ul>
</div>
</div>

<!-- 3. Nmap Wrapper -->
<div id="panel-nmap_scan" class="w-sand-panel">
<div class="w-sand-hdr"><span>3. python-nmap Wrapper</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import nmap

nm = nmap.PortScanner()
nm.scan('192.168.1.1', '22-80')

for host in nm.all_hosts():
    print(f"Host: {host} ({nm[host].hostname()})")
    print(f"State: {nm[host].state()}")
    for proto in nm[host].all_protocols():
        lport = nm[host][proto].keys()
        for port in lport:
            print(f"Port {port}: {nm[host][proto][port]['state']}")</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startNetSim('nmap_scan')">▶ Run Simulation</button>
</div>
<div id="term-nmap_scan" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation ด้านขวาบนเพื่อจำลองการเรียกใช้งาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>สคริปต์สแกนพอร์ตแบบเชิงลึกด้วยการเรียกสวมใช้งานคอมมานด์ Nmap:</p>
<ul>
<li><strong>PortScanner()</strong>: เรียกใช้ตัวขับเคลื่อนเพื่อกวาดเก็บข้อมูลรายละเอียด OS และสถานะของพอร์ตทั้งหมด</li>
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

// Net Terminal Simulation
window.startNetSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;

  term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">Scanning target sockets...</span>\\n[.] Generating payload/packets\\n[.] Stepping through targets...';

  setTimeout(() => {
    if (itemKey === 'socket_scan') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 socket_scan.py</span>\\n<span style="color:#3ddc84;">Port 22: OPEN (ssh)</span>\\n<span style="color:#3ddc84;">Port 80: OPEN (http)</span>\\nPort 21: CLOSED\\nPort 443: CLOSED\\n<span style="color:#3ddc84;">Port 8080: OPEN (http-alt)</span>';
    } else if (itemKey === 'scapy_arp') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 arp_scan.py</span>\\nBegin emission: Finished sending 256 packets.\\nReceived 3 replies, got 3 answers\\n\\nIP: 192.168.1.1 | MAC: 00:50:56:c0:00:01\\nIP: 192.168.1.102 | MAC: 00:0c:29:b4:ee:12\\nIP: 192.168.1.150 | MAC: 00:0c:29:f3:aa:5c';
    } else if (itemKey === 'nmap_scan') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 nmap_scan.py</span>\\nHost: 192.168.1.1 (gateway)\\nState: up\\n<span style="color:#3ddc84;">Port 22: open (ssh)</span>\\n<span style="color:#3ddc84;">Port 80: open (http)</span>';
    }
  }, 1000);
}
</script>"""

l198.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=198).update({"content": l198.content})
db.session.commit()
print("Lesson 198 Live Terminal Simulation successfully integrated!")
ctx.pop()
