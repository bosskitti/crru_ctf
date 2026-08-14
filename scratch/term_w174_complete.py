import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l174 = db.session.query(TutorialLesson).filter_by(id=174).first()
blocks = json.loads(l174.content)

# ─── Block 0: Core Vulnerability Assessments, VA vs Pentest, and CVE Timeline ───
val0 = """## 🔍 Vulnerability Assessment (การวิเคราะห์หาช่องโหว่ทางเครือข่าย)
---

ขั้นตอนถัดจากการเรียนรู้พื้นฐานเน็ตเวิร์ก คือการใช้เทคนิคสืบค้นช่องโหว่ของเป้าหมายผ่านการวิเคราะห์ประวัติทางสาธารณะ (Passive) และสแกนจุดบกพร่องเครือข่ายเชิงรับ

<style>
.w-neon-card {
  background: rgba(6, 8, 20, 0.45) !important;
  border: 1px solid rgba(139, 92, 246, 0.15) !important;
  border-radius: 12px !important;
  padding: 20px !important;
  margin-bottom: 24px !important;
  box-shadow: 0 8px 32px rgba(0,0,0,0.3), inset 0 0 15px rgba(139,92,246,0.02) !important;
  transition: all 0.25s ease !important;
}
.w-neon-card:hover {
  border-color: rgba(139, 92, 246, 0.35) !important;
  box-shadow: 0 8px 32px rgba(139,92,246,0.08), inset 0 0 20px rgba(139,92,246,0.03) !important;
}
.w-dork-item {
  background: rgba(255,255,255,0.015);
  border: 1px solid rgba(255,255,255,0.04);
  border-radius: 6px;
  padding: 10px 14px;
  margin-bottom: 10px;
}
.w-dork-code {
  font-family: 'JetBrains Mono', monospace;
  color: #a7f3d0;
  background: rgba(0,0,0,0.25);
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 0.76rem;
}
.w-comp-tbl {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}
.w-comp-tbl th, .w-comp-tbl td {
  border: 1px solid rgba(255,255,255,0.08);
  padding: 10px 14px;
  font-size: 0.8rem;
  text-align: left;
}
.w-comp-tbl th {
  background: rgba(139,92,246,0.08);
  color: #ffffff;
  font-weight: 700;
}
.w-vuln-timeline {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: 14px;
}
.w-vuln-node {
  background: rgba(255,255,255,0.015);
  border: 1px solid rgba(255,255,255,0.04);
  border-radius: 8px;
  padding: 14px;
}
.w-cve-badge {
  font-family: 'JetBrains Mono', monospace;
  background: rgba(239,68,68,0.1);
  border: 1px solid rgba(239,68,68,0.25);
  color: #ef4444;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 0.7rem;
}
</style>

### ⚖️ 1. Vulnerability Assessment vs Penetration Testing
ความแตกต่างระหว่างการประเมินช่องโหว่ (VA) และการเจาะระบบจริง (Pentest):
<div class="w-neon-card">
  <table class="w-comp-tbl">
    <thead>
      <tr>
        <th>คุณลักษณะ (Feature)</th>
        <th>Vulnerability Assessment (VA)</th>
        <th>Penetration Testing (Pentest)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>เป้าหมาย (Purpose)</strong></td>
        <td class="text-muted">ค้นหาและจัดหมวดหมู่ช่องโหว่ทั้งหมดในระบบ</td>
        <td class="text-muted">จำลองสถานการณ์จริงเพื่อโจมตีเจาะทะลุระบบ</td>
      </tr>
      <tr>
        <td><strong>วิธีการ (Approach)</strong></td>
        <td class="text-muted">สแกนอัตโนมัติด้วยเครื่องมือหาจุดอ่อนทั่วไป</td>
        <td class="text-muted">ผสมผสานสแกนเนอร์และโจมตีด้วยฝีมือแบบ manual</td>
      </tr>
      <tr>
        <td><strong>ผลกระทบ (Risk)</strong></td>
        <td class="text-muted">ต่ำมาก แทบไม่มีการขัดขวางการทำงานปกติ</td>
        <td class="text-muted">อาจเกิดระบบล่มหรือขัดข้องชั่วคราวจากการโจมตี</td>
      </tr>
      <tr>
        <td><strong>ผลลัพธ์ (Outcome)</strong></td>
        <td class="text-muted">รายงานรายการช่องโหว่และคำแนะนำแก้ไข</td>
        <td class="text-muted">รายงานช่องโหว่ที่บุกเจาะได้สำเร็จและระดับผลกระทบ</td>
      </tr>
    </tbody>
  </table>
</div>

---

### 🕵️‍♂️ 2. Google Dorking & OSINT Surveys
<div class="w-neon-card">
  <div class="w-dork-item">
    <strong class="text-white" style="font-size:0.8rem;">🕵️‍♂️ Google Dorking Operators</strong><br>
    <p class="text-muted mb-2" style="font-size:0.75rem;">คิวรีคัดหาเอกสารความลับของเป้าหมายบนดัชนีกูเกิล:</p>
    <span class="w-dork-code">site:ac.th intitle:"index of" "backup"</span> (หาโฟลเดอร์ไฟล์สำรองข้อมูล)
  </div>
  <div class="w-dork-item">
    <strong class="text-white" style="font-size:0.8rem;">🧱 Technology Stack Survey</strong><br>
    <p class="text-muted mb-0" style="font-size:0.75rem;">สแกนตรวจสอบซอฟต์แวร์เป้าหมายผ่าน <strong>Wappalyzer</strong> (ส่วนขยายเบราว์เซอร์), <strong>BuiltWith</strong> และ <strong>PublicWWW</strong> (สแกนโค้ด HTML/JS ทั่วอินเทอร์เน็ต)</p>
  </div>
</div>

---

### 🛡️ 3. Well-known Vulnerabilities (ช่องโหว่วิกฤตระดับโลก)
ตัวอย่างช่องโหว่ความปลอดภัยระดับสากลที่มีการบันทึกหมายเลข CVE เป็นทางการ:
<div class="w-neon-card">
  <div class="w-vuln-timeline">
    <div class="w-vuln-node">
      <div class="d-flex justify-content-between align-items-center mb-2"><strong class="text-white">Heartbleed (OpenSSL Memory Leak)</strong><span class="w-cve-badge">CVE-2014-0160</span></div>
      <p class="text-muted mb-0" style="font-size:0.72rem;">บกพร่องใน OpenSSL ทำให้ผู้โจมตีลอบอ่านข้อมูลความลับในหน่วยความจำ (เช่น คีย์เข้ารหัส หรือรหัสผ่าน) จากโฮสต์ปลายทางได้โดยตรง</p>
    </div>
    <div class="w-vuln-node">
      <div class="d-flex justify-content-between align-items-center mb-2"><strong class="text-white">EternalBlue (Windows SMBv1 RCE)</strong><span class="w-cve-badge">CVE-2017-0144</span></div>
      <p class="text-muted mb-0" style="font-size:0.72rem;">ช่องโหว่แชร์ไฟล์ SMB ของไมโครซอฟท์ นำไปสู่การแพร่กระจายตัวแบบเวิร์มของมัลแวร์เรียกค่าไถ่ WannaCry ทั่วโลก</p>
    </div>
    <div class="w-vuln-node">
      <div class="d-flex justify-content-between align-items-center mb-2"><strong class="text-white">Log4Shell (Apache Log4j RCE)</strong><span class="w-cve-badge">CVE-2021-44228</span></div>
      <p class="text-muted mb-0" style="font-size:0.72rem;">ความบกพร่องในระบบบันทึก Log4j ของภาษา Java ทำให้นักโจมตีรันคำสั่งยึดครองเซิร์ฟเวอร์ปลายทางผ่านการส่งข้อความคิวรีสั้นๆ</p>
    </div>
  </div>
</div>"""

l174.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=174).update({"content": l174.content})
db.session.commit()
print("Lesson 174 successfully upgraded with comprehensive VA vs Pentest comparison!")
ctx.pop()
