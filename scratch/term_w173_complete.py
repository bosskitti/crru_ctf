import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l173 = db.session.query(TutorialLesson).filter_by(id=173).first()
blocks = json.loads(l173.content)

# ─── Block 0: Full Network Protocols, Ports, and IP Calculation Content ───
val0 = """## 🧠 Network Scanning & Enumeration (การสำรวจระบบเครือข่ายและการสแกน)
---

ยินดีต้อนรับสู่บทเรียนการสำรวจข้อมูลและตรวจสอบเครือข่ายเป้าหมาย ขั้นตอนแรกในการเข้าทำลายหรือป้องกันช่องโหว่ความปลอดภัยคือการเรียนรู้แผนผังที่ตั้งทางเครือข่าย

### 🗺️ 1. Computer Network & Protocols Foundation
โครงสร้างเครือข่ายคอมพิวเตอร์และรูปแบบการเชื่อมโยงโปรโตคอลเปรียบเทียบระหว่างแบบจำลองมาตรฐาน OSI 7 Layers และชุดการสื่อสารอินเทอร์เน็ต TCP/IP Model:

<style>
.w-stack-wrapper {
  margin: 2rem auto;
  max-width: 1050px;
  background: rgba(6, 8, 20, 0.45);
  border: 1px solid rgba(0, 240, 255, 0.15);
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), inset 0 0 15px rgba(0, 240, 255, 0.05);
}
.w-stack-header-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-bottom: 16px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  padding-bottom: 12px;
}
@media (max-width: 768px) {
  .w-stack-header-grid {
    grid-template-columns: 1fr;
    gap: 8px;
    border-bottom: none;
    padding-bottom: 0;
  }
}
.w-model-title {
  font-size: 1.1rem;
  font-weight: 800;
  letter-spacing: 0.05em;
  display: flex;
  align-items: center;
  gap: 8px;
}
.w-osi-title { color: #f472b6; text-shadow: 0 0 10px rgba(244, 114, 182, 0.3); }
.w-tcp-title { color: #38bdf8; text-shadow: 0 0 10px rgba(56, 189, 248, 0.3); }
.w-grid-comparison {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: repeat(7, 1fr);
  gap: 10px 20px;
}
@media (max-width: 768px) {
  .w-grid-comparison {
    grid-template-columns: 1fr;
    grid-template-rows: auto !important;
    gap: 12px;
  }
}
.w-layer-card {
  display: flex;
  align-items: center;
  padding: 10px 16px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.015);
  border: 1px solid rgba(255, 255, 255, 0.04);
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  height: 100%;
}
.w-layer-card:hover {
  background: rgba(255, 255, 255, 0.035);
  transform: translateX(4px);
}
.w-layer-num {
  font-family: 'JetBrains Mono', monospace;
  font-weight: 800;
  font-size: 0.8rem;
  padding: 2px 8px;
  border-radius: 4px;
  margin-right: 14px;
  min-width: 32px;
  text-align: center;
}
.w-layer-info {
  flex: 1;
}
.w-layer-name {
  font-weight: 700;
  font-size: 0.85rem;
  color: #ffffff;
  margin-bottom: 2px;
}
.w-layer-desc {
  font-size: 0.72rem;
  color: #94a3b8;
}
.w-map-tag {
  font-size: 0.65rem;
  padding: 2px 6px;
  background: rgba(255,255,255,0.05);
  border-radius: 4px;
  color: #94a3b8;
  font-family: 'JetBrains Mono', monospace;
  margin-left: auto;
}
.w-osi-7 { border-left: 3px solid #ec4899; grid-column: 1; grid-row: 1; }
.w-osi-7 .w-layer-num { background: rgba(236, 72, 153, 0.15); color: #ec4899; }
.w-osi-7:hover { border-color: #ec4899; box-shadow: 0 0 10px rgba(236, 72, 153, 0.15); }
.w-osi-6 { border-left: 3px solid #d946ef; grid-column: 1; grid-row: 2; }
.w-osi-6 .w-layer-num { background: rgba(217, 70, 239, 0.15); color: #d946ef; }
.w-osi-6:hover { border-color: #d946ef; box-shadow: 0 0 10px rgba(217, 70, 239, 0.15); }
.w-osi-5 { border-left: 3px solid #a855f7; grid-column: 1; grid-row: 3; }
.w-osi-5 .w-layer-num { background: rgba(168, 85, 247, 0.15); color: #a855f7; }
.w-osi-5:hover { border-color: #a855f7; box-shadow: 0 0 10px rgba(168, 85, 247, 0.15); }
.w-osi-4 { border-left: 3px solid #6366f1; grid-column: 1; grid-row: 4; }
.w-osi-4 .w-layer-num { background: rgba(99, 102, 241, 0.15); color: #6366f1; }
.w-osi-4:hover { border-color: #6366f1; box-shadow: 0 0 10px rgba(99, 102, 241, 0.15); }
.w-osi-3 { border-left: 3px solid #3b82f6; grid-column: 1; grid-row: 5; }
.w-osi-3 .w-layer-num { background: rgba(59, 128, 246, 0.15); color: #3b82f6; }
.w-osi-3:hover { border-color: #3b82f6; box-shadow: 0 0 10px rgba(59, 128, 246, 0.15); }
.w-osi-2 { border-left: 3px solid #10b981; grid-column: 1; grid-row: 6; }
.w-osi-2 .w-layer-num { background: rgba(16, 185, 129, 0.15); color: #10b981; }
.w-osi-2:hover { border-color: #10b981; box-shadow: 0 0 10px rgba(16, 185, 129, 0.15); }
.w-osi-1 { border-left: 3px solid #84cc16; grid-column: 1; grid-row: 7; }
.w-osi-1 .w-layer-num { background: rgba(132, 204, 22, 0.15); color: #84cc16; }
.w-osi-1:hover { border-color: #84cc16; box-shadow: 0 0 10px rgba(132, 204, 22, 0.15); }
.w-tcp-4 { border-left: 3px solid #38bdf8; grid-column: 2; grid-row: 1 / span 3; }
.w-tcp-4 .w-layer-num { background: rgba(56, 189, 248, 0.15); color: #38bdf8; }
.w-tcp-4:hover { border-color: #38bdf8; box-shadow: 0 0 10px rgba(56, 189, 248, 0.15); }
.w-tcp-3 { border-left: 3px solid #6366f1; grid-column: 2; grid-row: 4; }
.w-tcp-3 .w-layer-num { background: rgba(99, 102, 241, 0.15); color: #6366f1; }
.w-tcp-3:hover { border-color: #6366f1; box-shadow: 0 0 10px rgba(99, 102, 241, 0.15); }
.w-tcp-2 { border-left: 3px solid #3b82f6; grid-column: 2; grid-row: 5; }
.w-tcp-2 .w-layer-num { background: rgba(59, 128, 246, 0.15); color: #3b82f6; }
.w-tcp-2:hover { border-color: #3b82f6; box-shadow: 0 0 10px rgba(59, 128, 246, 0.15); }
.w-tcp-1 { border-left: 3px solid #10b981; grid-column: 2; grid-row: 6 / span 2; }
.w-tcp-1 .w-layer-num { background: rgba(16, 185, 129, 0.15); color: #10b981; }
.w-tcp-1:hover { border-color: #10b981; box-shadow: 0 0 10px rgba(16, 185, 129, 0.15); }
@media (max-width: 768px) {
  .w-osi-7, .w-osi-6, .w-osi-5, .w-osi-4, .w-osi-3, .w-osi-2, .w-osi-1,
  .w-tcp-4, .w-tcp-3, .w-tcp-2, .w-tcp-1 {
    grid-column: auto !important;
    grid-row: auto !important;
  }
  .w-tcp-panel-title-mobile {
    margin-top: 20px;
    padding-top: 14px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
  }
}
</style>
<div class="w-stack-wrapper"><div class="w-stack-header-grid"><div class="w-model-title w-osi-title"><i class="fas fa-layer-group"></i> OSI 7 LAYERS MODEL</div><div class="w-model-title w-tcp-title d-none d-md-flex"><i class="fas fa-network-wired"></i> TCP/IP PROTOCOL LAYERS</div></div><div class="w-grid-comparison"><div class="w-layer-card w-osi-7"><div class="w-layer-num">L7</div><div class="w-layer-info"><div class="w-layer-name">Application Layer</div><div class="w-layer-desc">โปรแกรมประยุกต์ใช้งาน (HTTP, SSH, DNS)</div></div></div><div class="w-layer-card w-osi-6"><div class="w-layer-num">L6</div><div class="w-layer-info"><div class="w-layer-name">Presentation Layer</div><div class="w-layer-desc">การจัดการรูปแบบโครงสร้างการนำเสนอข้อมูลดิบ</div></div></div><div class="w-layer-card w-osi-5"><div class="w-layer-num">L5</div><div class="w-layer-info"><div class="w-layer-name">Session Layer</div><div class="w-layer-desc">การควบคุมและประสานระหว่างเซสชันสื่อสาร</div></div></div><div class="w-layer-card w-osi-4"><div class="w-layer-num">L4</div><div class="w-layer-info"><div class="w-layer-name">Transport Layer</div><div class="w-layer-desc">การนำส่งข้อมูลปลายทางถึงปลายทาง (TCP/UDP)</div></div></div><div class="w-layer-card w-osi-3"><div class="w-layer-num">L3</div><div class="w-layer-info"><div class="w-layer-name">Network Layer</div><div class="w-layer-desc">การกำหนดเส้นทางและส่งแพ็กเก็ต (IP, Routing)</div></div></div><div class="w-layer-card w-osi-2"><div class="w-layer-num">L2</div><div class="w-layer-info"><div class="w-layer-name">Data Link Layer</div><div class="w-layer-desc">การควบคุมเฟรมและที่อยู่ทางกายภาพ (MAC, Switch)</div></div></div><div class="w-layer-card w-osi-1"><div class="w-layer-num">L1</div><div class="w-layer-info"><div class="w-layer-name">Physical Layer</div><div class="w-layer-desc">การส่งสัญญาณบิตไฟฟ้าผ่านตัวกลางสายรับส่ง (Cables)</div></div></div><div class="w-model-title w-tcp-title d-flex d-md-none w-tcp-panel-title-mobile"><i class="fas fa-network-wired"></i> TCP/IP PROTOCOL LAYERS</div><div class="w-layer-card w-tcp-4"><div class="w-layer-num" style="align-self: flex-start; margin-top: 4px;">L4</div><div class="w-layer-info" style="display: flex; flex-direction: column; height: 100%; justify-content: center;"><div class="w-layer-name">Application Layer</div><div class="w-layer-desc">รวมหน้าที่ชั้น Application, Presentation, Session เพื่อสั่งรันบริการบนเว็บ</div><div style="font-size:0.68rem; color:#60a5fa; margin-top: 6px;"><i class="fas fa-link mr-1"></i> เทียบเท่า OSI Layer 5, 6, 7</div></div><span class="w-map-tag" style="align-self: flex-start;">L5-L7</span></div><div class="w-layer-card w-tcp-3"><div class="w-layer-num">L3</div><div class="w-layer-info"><div class="w-layer-name">Transport Layer</div><div class="w-layer-desc">จัดการช่องทางรับส่งข้อมูลอย่างถูกต้องครบถ้วน (TCP/UDP)</div></div><span class="w-map-tag">L4</span></div><div class="w-layer-card w-tcp-2"><div class="w-layer-num">L2</div><div class="w-layer-info"><div class="w-layer-name">Internet Layer</div><div class="w-layer-desc">การกำหนด Logical Address และนำส่งแพ็กเก็ต (IP, ICMP)</div></div><span class="w-map-tag">L3</span></div><div class="w-layer-card w-tcp-1"><div class="w-layer-num" style="align-self: flex-start; margin-top: 4px;">L1</div><div class="w-layer-info" style="display: flex; flex-direction: column; height: 100%; justify-content: center;"><div class="w-layer-name">Network Access Layer</div><div class="w-layer-desc">ควบคุมการสื่อสารกับอุปกรณ์การ์ดแลนและสายสัญญาณเน็ต</div><div style="font-size:0.68rem; color:#10b981; margin-top: 4px;"><i class="fas fa-link mr-1"></i> เทียบเท่า OSI Layer 1, 2</div></div><span class="w-map-tag" style="align-self: flex-start;">L1-L2</span></div></div></div>

<style>
.w-neon-card {
  background: rgba(6, 8, 20, 0.45) !important;
  border: 1px solid rgba(0, 240, 255, 0.1) !important;
  border-radius: 12px !important;
  padding: 20px !important;
  margin-bottom: 24px !important;
  box-shadow: 0 8px 32px rgba(0,0,0,0.3), inset 0 0 15px rgba(0,240,255,0.02) !important;
  transition: all 0.25s ease !important;
}
.w-neon-card:hover {
  border-color: rgba(0, 240, 255, 0.3) !important;
  box-shadow: 0 8px 32px rgba(0,240,255,0.08), inset 0 0 20px rgba(0,240,255,0.03) !important;
}
.w-tab-nav {
  display: flex;
  gap: 8px;
  margin-bottom: 14px;
  overflow-x: auto;
  padding-bottom: 4px;
}
.w-tab-btn {
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.08);
  padding: 6px 12px;
  border-radius: 6px;
  color: #cbd5e1;
  font-size: 0.72rem;
  cursor: pointer;
  white-space: nowrap;
}
.w-tab-btn.active {
  background: rgba(0,240,255,0.08);
  border-color: #00f0ff;
  color: #ffffff;
  font-weight: 700;
}
.w-tab-panel {
  display: none;
}
.w-tab-panel.active {
  display: block;
}
.w-proto-item {
  background: rgba(0,0,0,0.2);
  border: 1px solid rgba(255,255,255,0.04);
  border-radius: 8px;
  padding: 12px;
  margin-bottom: 10px;
}
.w-code-lbl {
  font-family: 'JetBrains Mono', monospace;
  background: rgba(0,240,255,0.08);
  color: #00f0ff;
  padding: 1px 6px;
  border-radius: 4px;
  font-size: 0.72rem;
}
</style>

### 📡 2. Network Protocols (โปรโตคอลระบบเครือข่าย)
<div class="w-neon-card">
  <p class="text-white mb-3" style="font-size:0.9rem; font-weight:600;"><i class="fas fa-network-wired mr-2 text-cyan"></i> ตรรกะโปรโตคอลจำแนกตามชั้นการทำงานของแบบจำลอง TCP/IP</p>
  <div class="w-tab-nav">
    <button class="w-tab-btn active" onclick="switchProtoTab('link', this)">Link Layer</button>
    <button class="w-tab-btn" onclick="switchProtoTab('internet', this)">Internet Layer</button>
    <button class="w-tab-btn" onclick="switchProtoTab('transport', this)">Transport Layer</button>
    <button class="w-tab-btn" onclick="switchProtoTab('app', this)">Application Layer</button>
  </div>
  <div id="proto-link" class="w-tab-panel active">
    <div class="w-proto-item">
      <div class="d-flex justify-content-between align-items-center mb-2"><strong class="text-white">Ethernet (Wired)</strong><span class="w-code-lbl">IEEE 802.3</span></div>
      <p class="text-muted mb-0" style="font-size:0.75rem;">เชื่อมต่อเน็ตผ่านสายแลน (LAN) ใช้ที่อยู่ MAC Address และรองรับความเร็วระดับ 10Mbps ถึง 10Gbps พร้อมระบบตรวจสอบชนสัญญาณ (CSMA/CD)</p>
    </div>
    <div class="w-proto-item">
      <div class="d-flex justify-content-between align-items-center mb-2"><strong class="text-white">Wi-Fi (Wireless)</strong><span class="w-code-lbl">IEEE 802.11</span></div>
      <p class="text-muted mb-0" style="font-size:0.75rem;">สื่อสารไร้สายผ่านคลื่นวิทยุความถี่ 2.4GHz / 5GHz เข้ารหัสความปลอดภัยด้วย WEP, WPA, WPA2</p>
    </div>
  </div>
  <div id="proto-internet" class="w-tab-panel">
    <div class="w-proto-item">
      <div class="d-flex justify-content-between align-items-center mb-2"><strong class="text-white">IP (Internet Protocol)</strong><span class="w-code-lbl">IPv4 & IPv6</span></div>
      <p class="text-muted mb-0" style="font-size:0.75rem;">การกำหนดที่อยู่เส้นทางส่งแพ็กเก็ตข้ามระบบ (IPv4 ขนาด 32 บิต | IPv6 ขนาด 128 บิต)</p>
    </div>
    <div class="w-proto-item">
      <div class="d-flex justify-content-between align-items-center mb-2"><strong class="text-white">ICMP (Internet Control Message Protocol)</strong><span class="w-code-lbl">Diagnostics</span></div>
      <p class="text-muted mb-0" style="font-size:0.75rem;">วิเคราะห์เครือข่ายและแจ้งสถานะข้อผิดพลาด เช่น คำสั่ง ping หรือแจ้งระบบปลายทางขัดข้อง</p>
    </div>
    <div class="w-proto-item">
      <div class="d-flex justify-content-between align-items-center mb-2"><strong class="text-white">ARP (Address Resolution Protocol)</strong><span class="w-code-lbl">IP to MAC</span></div>
      <p class="text-muted mb-0" style="font-size:0.75rem;">สืบหาความสัมพันธ์เพื่อแปลง IP Address เป็นที่อยู่กายภาพ MAC Address ในเครือข่าย LAN</p>
    </div>
  </div>
  <div id="proto-transport" class="w-tab-panel">
    <div class="w-proto-item">
      <div class="d-flex justify-content-between align-items-center mb-2"><strong class="text-white">TCP (Transmission Control Protocol)</strong><span class="w-code-lbl">Connection-Oriented</span></div>
      <p class="text-muted mb-0" style="font-size:0.75rem;">การรับส่งแบบรับประกันผลความถูกต้อง ล็อกช่องเชื่อมต่อแน่นหนา (Three-Way Handshake) คุมส่งลำดับแพ็กเก็ตไม่ให้สูญหาย</p>
    </div>
    <div class="w-proto-item">
      <div class="d-flex justify-content-between align-items-center mb-2"><strong class="text-white">UDP (User Datagram Protocol)</strong><span class="w-code-lbl">Connectionless</span></div>
      <p class="text-muted mb-0" style="font-size:0.75rem;">ส่งผ่านแบบเน้นความเร็วสูงสุดโดยไม่สร้างการเชื่อมต่อ ไม่การันตีความถูกต้อง เหมาะสำหรับการตรีมมิ่ง เกมมิ่ง หรือ VoIP</p>
    </div>
  </div>
  <div id="proto-app" class="w-tab-panel">
    <div class="w-proto-item">
      <div class="d-flex justify-content-between align-items-center mb-2"><strong class="text-white">HTTP / HTTPS (Port 80/443)</strong><span class="w-code-lbl">Web Services</span></div>
      <p class="text-muted mb-0" style="font-size:0.75rem;">รับส่งข้อมูลหน้าเว็บ โดย HTTPS มีการเข้ารหัสระดับชั้นความปลอดภัยด้วยโปรโตคอล SSL/TLS</p>
    </div>
    <div class="w-proto-item">
      <div class="d-flex justify-content-between align-items-center mb-2"><strong class="text-white">SSH / FTP (Port 22, 20/21)</strong><span class="w-code-lbl">Control & Transfer</span></div>
      <p class="text-muted mb-0" style="font-size:0.75rem;">SSH คุมระบบระยะไกลแบบเข้ารหัสลับ และ FTP สำหรับขนย้ายส่งไฟล์แชร์เครือข่าย</p>
    </div>
    <div class="w-proto-item">
      <div class="d-flex justify-content-between align-items-center mb-2"><strong class="text-white">DNS / SMTP (Port 53, 25)</strong><span class="w-code-lbl">Services</span></div>
      <p class="text-muted mb-0" style="font-size:0.75rem;">DNS แปลงชื่อเว็บไซต์เป็นไอพี และ SMTP สำหรับส่งต่อ Relay จดหมายอีเมลระหว่างเมล์เซิร์ฟเวอร์</p>
    </div>
  </div>
</div>
<script>
window.switchProtoTab = function(tabId, btn) {
  const container = btn.closest('.w-neon-card');
  container.querySelectorAll('.w-tab-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  container.querySelectorAll('.w-tab-panel').forEach(p => p.classList.remove('active'));
  const target = container.querySelector('#proto-' + tabId);
  if (target) target.classList.add('active');
}
</script>

<style>
.w-port-tbl {
  width: 100%;
  border-collapse: collapse;
}
.w-port-tbl th, .w-port-tbl td {
  padding: 8px 12px;
  border-bottom: 1px solid rgba(255,255,255,0.05);
  font-size: 0.76rem;
}
.w-port-tbl th {
  background: rgba(255,255,255,0.02);
  color: #ffffff;
  font-weight: 700;
  text-align: left;
}
.w-port-tbl tr:hover {
  background: rgba(255,255,255,0.01);
}
</style>

### 🔑 3. Common Ports & Ranges
<div class="w-neon-card">
  <p class="text-white mb-3" style="font-size:0.9rem; font-weight:600;"><i class="fas fa-door-open mr-2 text-warning"></i> รายชื่อพอร์ตบริการเครือข่ายมาตรฐานที่มักใช้ในการโจมตี</p>
  <div style="max-height:240px; overflow-y:auto; border:1px solid rgba(255,255,255,0.06); border-radius:8px;">
    <table class="w-port-tbl">
      <thead>
        <tr>
          <th>พอร์ต / โปรโตคอล</th>
          <th>คำอธิบายและการใช้งานหลัก</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><span class="w-code-lbl">Port 21: FTP</span></td><td class="text-muted">โปรโตคอลย้ายส่งไฟล์ ควบคุมคำสั่ง (Command Control)</td></tr>
        <tr><td><span class="w-code-lbl">Port 22: SSH</span></td><td class="text-muted">รีโมทควบคุมเซิร์ฟเวอร์แบบเข้ารหัสผ่านช่องทางปลอดภัย</td></tr>
        <tr><td><span class="w-code-lbl">Port 23: Telnet</span></td><td class="text-muted" style="color:#ef4444 !important;">รีโมทแบบไม่เข้ารหัส (อันตรายมาก ดักจับข้อมูลดิบได้ง่าย)</td></tr>
        <tr><td><span class="w-code-lbl">Port 25: SMTP</span></td><td class="text-muted">ใช้สำหรับส่ง Relay เมลระหว่างเซิร์ฟเวอร์</td></tr>
        <tr><td><span class="w-code-lbl">Port 53: DNS</span></td><td class="text-muted">ระบบแปลชื่อโดเมนเป็น IP Address ปลายทาง</td></tr>
        <tr><td><span class="w-code-lbl">Port 80: HTTP</span></td><td class="text-muted">บริการเปิดหน้าเว็บทั่วไปแบบปกติ</td></tr>
        <tr><td><span class="w-code-lbl">Port 143: IMAP</span></td><td class="text-muted">ดึงข้อมูลและบริหารโฟลเดอร์อีเมลบนเครื่องเซิร์ฟเวอร์</td></tr>
        <tr><td><span class="w-code-lbl">Port 443: HTTPS</span></td><td class="text-muted" style="color:#10b981 !important;">บริการเปิดหน้าเว็บเข้ารหัสปลอดภัยด้วย SSL/TLS</td></tr>
        <tr><td><span class="w-code-lbl">Port 445: SMB</span></td><td class="text-muted">บริการแชร์ไฟล์แชร์ปริ้นเตอร์ภายใต้ระบบ Windows</td></tr>
        <tr><td><span class="w-code-lbl">Port 3306: MySQL</span></td><td class="text-muted">เชื่อมต่อจัดการฐานข้อมูลยอดนิยม MySQL</td></tr>
        <tr><td><span class="w-code-lbl">Port 3389: RDP</span></td><td class="text-muted">รีโมทหน้าจอขอบระบบปฏิบัติการ Windows</td></tr>
      </tbody>
    </table>
  </div>
</div>

<style>
.w-calc-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(460px, 1fr));
  gap: 16px;
  margin-top: 14px;
}
@media(max-width: 520px){
  .w-calc-grid { grid-template-columns: 1fr; }
}
.w-calc-box {
  background: rgba(0,0,0,0.25);
  border: 1px solid rgba(255,255,255,0.05);
  border-radius: 8px;
  padding: 14px;
}
.w-calc-code {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.72rem;
  color: #3ddc84;
  white-space: pre-wrap;
  margin-top: 8px;
  background: rgba(0,0,0,0.3);
  padding: 10px;
  border-radius: 6px;
}
</style>

### 🛡️ 4. IP Classes & Subnet Calculations
<div class="w-neon-card">
  <p class="text-white mb-2" style="font-size:0.9rem; font-weight:600;"><i class="fas fa-calculator mr-2 text-success"></i> คลาสที่อยู่ไอพี (IP Classes) และคำนวณเครือข่ายย่อย (Subnetting)</p>
  <p class="text-muted" style="font-size:0.75rem;">คลาสที่อยู่ IPv4:</p>
  <ul style="padding-left:16px; font-size:0.75rem; color:#cbd5e1; line-height:1.6; margin-bottom:14px;">
    <li><strong>Class A</strong>: `1.0.0.0` ถึง `126.255.255.255` (Subnet: `255.0.0.0`)</li>
    <li><strong>Class B</strong>: `128.0.0.0` ถึง `191.255.255.255` (Subnet: `255.255.0.0`)</li>
    <li><strong>Class C</strong>: `192.0.0.0` ถึง `223.255.255.255` (Subnet: `255.255.255.0`)</li>
    <li><strong>Private IPs</strong>: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16` (ไม่สามารถออกเน็ตตรงได้)</li>
  </ul>
  <div class="w-calc-grid">
    <div class="w-calc-box">
      <strong class="text-white" style="font-size:0.8rem;">IP Address /24 Subnetting</strong>
      <div class="w-calc-code">IP: 192.168.43.125
Binary: 11000000.10101000.00101011.01111101
Mask: 255.255.255.0 (/24)
Host bits: 8 (256 IPs) | Net bits: 24</div>
    </div>
    <div class="w-calc-box">
      <strong class="text-white" style="font-size:0.8rem;">IP Address /23 Subnetting</strong>
      <div class="w-calc-code">IP: 192.168.43.125
Binary: 11000000.10101000.00101011.01111101
Mask: 255.255.254.0 (/23)
Host bits: 9 (512 IPs) | Net bits: 23</div>
    </div>
  </div>
</div>

---

### 🚀 5. Gaining Access & Penetration Testing Stages
<div class="w-neon-card">
  <h6 class="text-white font-weight-bold mb-3"><i class="fas fa-route mr-2 text-info"></i> ขั้นตอนการดำเนินงานประเมินและเจาะระบบ (6 Stages)</h6>
  <div class="w-flow-step">
    <div class="w-flow-num">1</div>
    <div class="w-layer-info">
      <div class="text-white font-weight-bold" style="font-size:0.8rem;">Reconnaissance (การสืบข้อมูลข่าวกรอง)</div>
      <div class="text-muted" style="font-size:0.72rem;">สืบค้นประวัติระบบเป้าหมายแบบไม่เปิดเผยตัวตน (Google Dork, WHOIS)</div>
    </div>
  </div>
  <div class="w-flow-step">
    <div class="w-flow-num">2</div>
    <div class="w-layer-info">
      <div class="text-white font-weight-bold" style="font-size:0.8rem;">Scanning (การสแกนเป้าหมายเชิงรุก)</div>
      <div class="text-muted" style="font-size:0.72rem;">ระดมคำสั่งสแกนพอร์ตและประมวลจุดบกพร่องระบบโดยตรง (Nmap, Nessus)</div>
    </div>
  </div>
  <div class="w-flow-step">
    <div class="w-flow-num">3</div>
    <div class="w-layer-info">
      <div class="text-white font-weight-bold" style="font-size:0.8rem;">Gaining Access (การบุกยึดเพื่อรับสิทธิ์)</div>
      <div class="text-muted" style="font-size:0.72rem;">โจมตีช่องโหว่เพื่อขโมยรับสิทธิ์รันคำสั่งสั่งการระดับสูง (Metasploit)</div>
    </div>
  </div>
  <div class="w-flow-step">
    <div class="w-flow-num">4</div>
    <div class="w-layer-info">
      <div class="text-white font-weight-bold" style="font-size:0.8rem;">Maintaining Access (การคงสิทธิ์ถาวร)</div>
      <div class="text-muted" style="font-size:0.72rem;">ติดตั้งเครื่องมือสั่งรันสวมรอยระบบเผื่อล็อกอินกลับเข้ามาใหม่ (Persistence)</div>
    </div>
  </div>
  <div class="w-flow-step">
    <div class="w-flow-num">5</div>
    <div class="w-layer-info">
      <div class="text-white font-weight-bold" style="font-size:0.8rem;">Covering Tracks (การลบร่องรอย)</div>
      <div class="text-muted" style="font-size:0.72rem;">ล้างไฟล์ประวัติสั่งการและบันทึกล็อกไฟล์ความปลอดภัย เพื่อปิดบังพฤติกรรม</div>
    </div>
  </div>
  <div class="w-flow-step">
    <div class="w-flow-num">6</div>
    <div class="w-layer-info">
      <div class="text-white font-weight-bold" style="font-size:0.8rem;">Reporting (รายงานประเมินช่องโหว่)</div>
      <div class="text-muted" style="font-size:0.72rem;">รวบรวมแนวทางช่องโหว่และจัดทำรายงานชี้ทิศทางแก้ไขให้กับผู้ดูแลเซิร์ฟเวอร์</div>
    </div>
  </div>
</div>"""

l173.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=173).update({"content": l173.content})
db.session.commit()
print("Lesson 173 Block 0 upgraded with full raw protocols & IP calculation layout!")
ctx.pop()
