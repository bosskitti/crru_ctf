import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l173 = db.session.query(TutorialLesson).filter_by(id=173).first()
blocks = json.loads(l173.content)

# ─── Correct Block 0 (Clean HTML, No comments, No blank lines, Absolute compatibility) ───
blocks[0]['value'] = """## 🧠 Network Scanning & Enumeration (การสำรวจระบบเครือข่ายและการสแกน)
---

ยินดีต้อนรับสู่บทเรียนการสำรวจข้อมูลและตรวจสอบเครือข่ายเป้าหมาย ขั้นตอนแรกในการเข้าทำลายหรือป้องกันช่องโหว่ความปลอดภัยคือการเรียนรู้แผนผังที่ตั้งทางเครือข่าย

### 🗺️ 1. Computer Network & Protocols Foundation
โครงสร้างเครือข่ายคอมพิวเตอร์และรูปแบบการเชื่อมโยงโปรโตคอลเปรียบเทียบระหว่างแบบจำลองมาตรฐาน OSI 7 Layers และชุดการสื่อสารอินเทอร์เน็ต TCP/IP Model:

<style>
.w-stack-wrapper {
  margin: 2rem auto;
  max-width: 1050px;
  background: rgba(6, 8, 20, 0.45);
  border: 1px solid rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
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

l173.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=173).update({"content": l173.content})
db.session.commit()
print("Lesson 173 visual grid layout successfully corrected and compressed!")
ctx.pop()
