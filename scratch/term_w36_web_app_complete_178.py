import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

def save_lesson(lid, val0, val1, val2):
    l = db.session.query(TutorialLesson).filter_by(id=lid).first()
    blocks = [
        {"type": "markdown", "value": val0},
        {"type": "markdown", "value": val1},
        {"type": "markdown", "value": val2}
    ]
    l.content = json.dumps(blocks, ensure_ascii=False)
    db.session.query(TutorialLesson).filter_by(id=lid).update({"content": l.content})
    db.session.commit()
    print(f"Lesson {lid} complete upgrade finished!")

# ─── Lesson 178: Path Traversal, HTTP Messages & SQLi Intro ───
val178_0 = """## 💉 Path Traversal, HTTP Messages & SQLi Intro (ช่องโหว่ประเภท Injection)
---

ยินดีต้อนรับสู่บทเรียนการสืบค้นข้อมูลเชิงลึกผ่านเส้นทางโฟลเดอร์เครือข่าย, โครงสร้าง HTTP Message และปูพื้นฐานการโจมตี SQL Injection

### 📄 SLIDE 51-58: เครื่องมือสแกนหาความสัมพันธ์ไฟล์ระบบ (Path Traversal Tools)
การค้นหาไดเรกทอรีลับหรือหน้าล็อกอินระบบหลังบ้านโดยใช้โปรแกรมแสกนความปลอดภัยอัตโนมัติ:

#### 📁 Dirb (Directory brute-forcing)
- **คุณลักษณะ**: สั่งรันผ่าน Command Line เพื่อสุ่มเดาชื่อไฟล์และโฟลเดอร์ โดยส่งอิงจาก Wordlist มาตรฐาน
- **ตัวอย่างการสแกนปกติ**:
  ```bash
  dirb https://target.com /usr/share/wordlists/dirb/common.txt
  ```
- **ตัวอย่างการสแกนหาไฟล์แบ็คอัปตามประเภทนามสกุล**:
  ```bash
  dirb https://target.com /usr/share/wordlists/dirb/common.txt -X .bak,.zip,.tar
  ```

#### 📁 Dirbuster (GUI-based fuzzer)
- **คุณลักษณะ**: เวอร์ชัน Graphic User Interface (มีหน้าต่างให้กดปรับแต่ง) เหมาะสำหรับการรันหาพาเนลแอดมินหรือทรัพยากรเว็บแบบเห็นภาพ

#### 📁 FFUF (Fast Web Fuzzer)
- **คุณลักษณะ**: fuzzer ความเร็วสูงในสายงานเจาะระบบ มีลูกเล่น recursive ค้นหาเส้นทางเชิงลึกแบบซับซ้อน
- **ตัวอย่างการสแกน**:
  ```bash
  ffuf -u https://target.com/admin/FUZZ -w /usr/share/wordlists/rockyou.txt
  ```

#### 📁 Gobuster (Go-written scanner)
- **คุณลักษณะ**: พัฒนาขึ้นมาด้วยภาษา Go ทำให้ข้ามขีดจำกัดความเร็วของเครื่องมืออื่นๆ มาก
- **ตัวอย่างการค้นหาไฟล์ .php**:
  ```bash
  gobuster dir -u https://target.com -w /usr/share/wordlists/dirb/common.txt -x php
  ```

---

### 📄 SLIDE 59-75: HTTP Message Anatomy (โครงสร้างทราฟฟิกเว็บ)
- **HTTP Request**: ทราฟฟิกข้อมูลที่ฝั่ง Client ส่งหาเซิร์ฟเวอร์ ประกอบด้วย:
  - **Method**: คำสั่งการทำงาน เช่น GET (ดึงข้อมูล), POST (ส่งประมวลผล), PUT (ปรับปรุงไฟล์), DELETE (ลบไฟล์)
  - **Path**: พิกัดเป้าหมาย เช่น `/api/user?id=123`
  - **Protocol**: ระบุรุ่นการส่ง เช่น `HTTP/1.1` หรือ `HTTP/2`
  - **Headers**: เมทาดาตาเสริม เช่น User-Agent (ระบุประเภทบราวเซอร์), Cookie (ระบุสิทธิ์)
  - **Body**: ข้อมูลชุดใหญ่ที่ฝั่งเซิร์ฟเวอร์นำไปประมวลผล (มีผลเฉพาะ POST/PUT)
- **HTTP Response**: ทราฟฟิกตอบกลับจากเซิร์ฟเวอร์ ประกอบด้วย:
  - **Status Line**: แจ้งรหัสผลลัพธ์ เช่น `200 OK` (สำเร็จ), `301 Moved` (ย้ายหน้า), `401 Unauthorized` (ไม่ผ่านสิทธิ์), `403 Forbidden` (ห้ามเข้า), `404 Not Found` (ไม่พบไฟล์), `500 Server Error` (เซิร์ฟเวอร์พัง)
  - **Server**: แจ้งโปรแกรมที่รันบนเครื่อง เช่น Apache, Nginx
  - **Headers**: เช่น Content-Type (ประเภทผลลัพธ์)
  - **Body**: ซอร์สโค้ด HTML หรือข้อมูล JSON ที่บราวเซอร์นำมาวาดแสดงผล
- **cURL Command**: โปรแกรมรัน Command Line ยอดนิยมในการยิงขอเรียกข้อมูลดิบจากเซิร์ฟเวอร์
  - **ตัวอย่าง**: สั่งดึงเฉพาะ Header ของเป้าหมายเพื่อตรวจความปลอดภัย:
    ```bash
    curl -I https://www.example.com
    ```

---

### 📄 SLIDE 76-90: Malicious HTTP Message Detections (การตรวจสอบภัยคุกคาม)
- **Unusual HTTP Methods**: นักโจมตีใช้ประโยชน์จากเมธอดพิเศษ เช่น OPTIONS, TRACE หรือ WebDAV (MKCOL, COPY) เพื่อตรวจและควบคุมไฟล์เซิร์ฟเวอร์
- **Unusual User-Agents**: แฮกเกอร์ใช้โปรแกรมโจมตี ซึ่งตัวโปรแกรมจะแนบ User-Agent แปลกปลอมมา (เช่น `sqlmap/1.5.2`, `HackerTool/1.0`, `python-requests`, `Nmap compatible`) แอดมินจึงควรเฝ้าระวังหรือปิดกั้นทราฟฟิกเหล่านี้
- **Large/Encoded POST**: การลอบส่ง Web Shell หรือคำสั่งยิงเจาะโดยเข้ารหัส Base64 หรือ Hex เพื่อให้ผ่านพ้นระบบ WAF (Web Application Firewall)

---

### 📄 SLIDE 91-100: SQL Injection (SQLi) Introduction
- **คำจำกัดความ**: ช่องโหว่ที่เกิดจากการเชื่อมต่อซอร์สโค้ดแอปพลิเคชันกับฐานข้อมูล SQL ผิดพลาด ปล่อยให้นำค่าอินพุตที่ผู้ใช้พิมพ์เข้ามาไปรวมเข้ากับประโยคคิวรีตรงๆ ส่งผลให้แฮกเกอร์สามารถควบคุมการประมวลผลฐานข้อมูลหลังบ้านได้
- **สไลด์ความต่างระหว่าง Query**:
  - คิวรีปกติ: `SELECT * FROM users WHERE username = 'admin' AND password = 'p@ssW0rd';`
  - คิวรีเมื่อโดนยิง bypass: `SELECT * FROM users WHERE username = 'admin' --' AND password = 'xxx';` (สัญลักษณ์ `--` ปิดประโยคตรวจรหัสผ่านด้านหลัง)"""

val178_1 = """### 💻 Directory & HTTP Diagnostic Sandbox (จำลองค้นหาไฟล์และยิงคำสั่ง)

คลิกหัวข้อด้านซ้ายมือเพื่อศึกษาตัวอย่างการทำแล็บจำลองความปลอดภัย และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลลัพธ์:

<div class="w-sandbox-main" style="display: flex; gap: 20px; margin: 1.5rem auto; max-width: 1000px;">
  <div class="w-sandbox-nav" style="width: 220px; display: flex; flex-direction: column; gap: 8px; flex-shrink: 0;">
    <button id="nav-item-dirb" class="w-nav-item active" style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 6px; padding: 10px 14px; color: #cbd5e1; text-align: left; cursor: pointer; font-size: 0.78rem; transition: all 0.2s;" onclick="showSandboxItem('dirb', this)">1. Dirb Backup Scan</button>
    <button id="nav-item-curl" class="w-nav-item" style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 6px; padding: 10px 14px; color: #cbd5e1; text-align: left; cursor: pointer; font-size: 0.78rem; transition: all 0.2s;" onclick="showSandboxItem('curl', this)">2. cURL HTTP Audit</button>
  </div>
  <div class="w-sandbox-panels" style="flex-grow: 1; display: flex; flex-direction: column; gap: 14px;">
    <!-- DIRB PANEL -->
    <div id="panel-dirb" class="w-sand-panel active" style="background: #05070f; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 10px; padding: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.45);">
      <div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
        <span>1. Brute-forcing Web Backups with Dirb</span>
        <span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(168,85,247,0.08); border: 1px solid rgba(168,85,247,0.2); color: #a855f7; font-family: monospace;">Dirb Scanner</span>
      </div>
      <pre style="font-family: monospace; font-size: 0.8rem; color: #a855f7; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">dirb http://ctf.rpca.ac.th/ /usr/share/wordlists/dirb/common.txt -X .zip,.bak</pre>
      <div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
        <div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
          <button style="background: rgba(168,85,247,0.1); border: 1px solid rgba(168,85,247,0.3); border-radius: 4px; color: #a855f7; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700; transition: all 0.15s;" onclick="startWebSim('dirb')">▶ Run Simulation</button>
        </div>
        <div id="term-dirb" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 90px;">
          <span style="color: #3ddc84;">kali$</span> [กดปุ่ม Run Simulation เพื่อยิงคำสั่ง Dirb]
        </div>
      </div>
      <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 16px; font-size: 0.83rem; color: #cbd5e1; line-height: 1.65;">
        <h5 style="margin: 0 0 8px; font-size: 0.85rem; color: #fbbf24; font-weight: bold;">⚙️ Command Description</h5>
        <p style="margin: 0;">คำสั่งค้นหาไฟล์สำรอง (เช่น .zip หรือ .bak) ในรากโฮสต์เป้าหมาย เพื่อตรวจจับความเสื่อมสภาพของข้อมูลสำคัญ</p>
      </div>
    </div>
    
    <!-- CURL PANEL -->
    <div id="panel-curl" class="w-sand-panel" style="background: #05070f; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 10px; padding: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.45); display: none;">
      <div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
        <span>2. cURL HTTP OPTIONS Audit</span>
        <span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(168,85,247,0.08); border: 1px solid rgba(168,85,247,0.2); color: #a855f7; font-family: monospace;">cURL Tool</span>
      </div>
      <pre style="font-family: monospace; font-size: 0.8rem; color: #a855f7; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">curl -X OPTIONS -i http://ctf.rpca.ac.th/</pre>
      <div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
        <div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
          <button style="background: rgba(168,85,247,0.1); border: 1px solid rgba(168,85,247,0.3); border-radius: 4px; color: #a855f7; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700; transition: all 0.15s;" onclick="startWebSim('curl')">▶ Run Simulation</button>
        </div>
        <div id="term-curl" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 90px;">
          <span style="color: #3ddc84;">kali$</span> [กดปุ่ม Run Simulation เพื่อรันคำสั่ง cURL]
        </div>
      </div>
      <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 16px; font-size: 0.83rem; color: #cbd5e1; line-height: 1.65;">
        <h5 style="margin: 0 0 8px; font-size: 0.85rem; color: #fbbf24; font-weight: bold;">⚙️ Command Description</h5>
        <p style="margin: 0;">เมธอด OPTIONS ใช้ทดสอบเพื่อขอข้อมูลรายการ HTTP methods ทั้งหมดที่เว็บเซิร์ฟเวอร์เปิดไว้ทำงาน</p>
      </div>
    </div>
  </div>
</div>

<script>
window.showSandboxItem = function(itemKey, element) {
  // Clear active buttons
  const navButtons = document.querySelectorAll('.w-sandbox-nav button');
  navButtons.forEach(btn => {
    btn.style.borderColor = 'rgba(255, 255, 255, 0.06)';
    btn.style.color = '#cbd5e1';
    btn.style.background = 'rgba(255, 255, 255, 0.02)';
  });
  // Set current active button
  element.style.borderColor = '#a855f7';
  element.style.color = '#ffffff';
  element.style.background = 'rgba(168, 85, 247, 0.05)';
  
  // Hide all panels
  const panels = document.querySelectorAll('.w-sand-panel');
  panels.forEach(p => {
    p.style.display = 'none';
  });
  
  // Show target panel
  const target = document.getElementById('panel-' + itemKey);
  if (target) {
    target.style.display = 'block';
  }
}

window.startWebSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#ffffff; font-weight:bold;">Running audit checks...</span>\\n[.] Connecting target server...';
  setTimeout(() => {
    if (itemKey === 'dirb') {
      term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#3ddc84; font-weight:bold;">DIRB scan results:</span>\\nFOUND: http://ctf.rpca.ac.th/backup.zip (CODE: 200)\\nFOUND: http://ctf.rpca.ac.th/old_site.bak (CODE: 200)\\n\\n[+] Dirb completed successfully!';
    } else if (itemKey === 'curl') {
      term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#a855f7; font-weight:bold;">HTTP/1.1 200 OK</span>\\nAllow: GET, POST, OPTIONS, TRACE, WebDAV\\nServer: Apache/2.4.41 (Ubuntu)\\nContent-Length: 0\\n\\n[+] OPTIONS check finished.';
    }
  }, 1000);
}
</script>"""

val178_2 = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการบันทึกความสำเร็จและปลดล็อกปุ่มบทเรียนถัดไป:

<div class="row align-items-center" style="margin:1.5rem auto; max-width:980px;"><div class="col-md-8"><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. ช่องโหว่ประเภทใดเกิดขึ้นจากการที่เซิร์ฟเวอร์นำอินพุตของผู้ใช้ไปเรียกประมวลผลเป็นคำสั่งระบบปฏิบัติการโดยตรง?</p><div class="options-container" data-q="q1"><label class="w-quiz-option"><input type="radio" name="inj_type" value="SQLi" data-hash="false">SQL Injection</label><label class="w-quiz-option"><input type="radio" name="inj_type" value="Command Injection" data-hash="23c7f5c90b6b80d90bd93d8435d648b26e03fb21884be5e38f6b864a66e4a2cd">Command Injection</label><label class="w-quiz-option"><input type="radio" name="inj_type" value="XSS" data-hash="false">Cross-Site Scripting (XSS)</label><label class="w-quiz-option"><input type="radio" name="inj_type" value="LFI" data-hash="false">Local File Inclusion (LFI)</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. คิวรีเป้าหมายพิเศษระดับมาตรฐาน \' OR 1=1 -- นิยมใช้ส่งเข้าไปในฐานข้อมูลเพื่อทำลายเงื่อนไขข้อใด?</p><div class="options-container" data-q="q2"><label class="w-quiz-option"><input type="radio" name="sqli_opt" value="Data Exfiltration" data-hash="false">ขโมยดูข้อมูลทั้งหมด (Data Exfiltration)</label><label class="w-quiz-option"><input type="radio" name="sqli_opt" value="Bypass Auth" data-hash="a95aa975765796245d8b8ff716d0046522bb33f749eb721867c4e515d18d451">ข้ามขั้นตอนตรวจสอบยืนยันตน (Bypass Authentication)</label><label class="w-quiz-option"><input type="radio" name="sqli_opt" value="DoS" data-hash="false">ทำลายเซิร์ฟเวอร์ระบบล่ม (Denial of Service)</label><label class="w-quiz-option"><input type="radio" name="sqli_opt" value="Password cracking" data-hash="false">ค้นหารหัสผ่านระบบ (Password Cracking)</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div></div><div class="col-md-4 text-center"><div class="p-4" style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); border-radius:12px; min-height:220px; display:flex; flex-direction:column; justify-content:center; align-items:center;"><span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;">Lesson Progress</span><div class="neon-gauge-container"><svg class="neon-gauge" viewBox="0 0 36 36"><path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><path class="neon-gauge-fill" id="lesson-gauge-fill" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text">0%</text></svg></div><span id="lesson-status-txt" class="mt-3 d-block text-muted" style="font-size:0.78rem;">โปรดตอบคำถามให้ครบ 2 ข้อ</span></div></div></div>
<style>
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:#a855f7; stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease, stroke 0.5s ease; filter:drop-shadow(0 0 5px rgba(168,85,247,0.5));}
.neon-gauge-text {fill:#ffffff; font-family:\'JetBrains Mono\',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}
</style>
<script>
const lessonKey = 'solved_lesson_178';
function getSavedSolves() { try { return JSON.parse(localStorage.getItem(lessonKey) || '[]'); } catch(e) { return []; } }
function updateLocalProgress() {
  const solved = getSavedSolves();
  const total = 2;
  const percent = Math.round((solved.length / total) * 100);
  const fill = document.getElementById('lesson-gauge-fill');
  const text = document.getElementById('lesson-gauge-text');
  const status = document.getElementById('lesson-status-txt');
  if (fill) fill.setAttribute('stroke-dasharray', `${percent}, 100`);
  if (text) text.textContent = `${percent}%`;
  if (solved.length === total) {
    if (fill) fill.style.stroke = '#3ddc84';
    if (status) status.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
  } else {
    if (fill) fill.style.stroke = '#a855f7';
    if (status) status.textContent = `ทำเสร็จแล้ว ${solved.length}/${total} ข้อ`;
  }
}
document.addEventListener('click', function(e) {
  const label = e.target.closest('.w-quiz-option');
  if (label) {
    const container = label.closest('.options-container');
    if (container) {
      container.querySelectorAll('.w-quiz-option').forEach(opt => opt.classList.remove('selected'));
      label.classList.add('selected');
      const radio = label.querySelector('input[type="radio"]');
      if (radio) radio.checked = true;
    }
  }
});
window.verifyMultipleChoice = function(button) {
  const cell = button.closest('.question-cell');
  const selectedRadio = cell.querySelector('input[type="radio"]:checked');
  const feedback = cell.querySelector('.feedback-msg');
  if (!selectedRadio) {
    feedback.className = "feedback-msg mt-2 alert-warning py-1.5 px-3 text-dark";
    feedback.innerHTML = '<i class="fas fa-exclamation-triangle mr-1"></i> กรุณาเลือกคำตอบ';
    feedback.style.setProperty('display', 'block', 'important');
    return;
  }
  const hashVal = selectedRadio.getAttribute('data-hash');
  if (hashVal !== 'false') {
    feedback.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
    feedback.innerHTML = '<i class="fas fa-check-circle mr-1"></i> คำตอบถูกต้อง!';
    feedback.style.setProperty('display', 'block', 'important');
    cell.querySelectorAll('input[type="radio"]').forEach(r => r.disabled = true);
    cell.querySelectorAll('.w-quiz-option').forEach(opt => opt.style.pointerEvents = 'none');
    button.disabled = true;
    const solved = getSavedSolves();
    if (!solved.includes(hashVal)) {
      solved.push(hashVal);
      localStorage.setItem(lessonKey, JSON.stringify(solved));
    }
    updateLocalProgress();
  } else {
    feedback.className = "feedback-msg mt-2 alert-danger py-1.5 px-3 text-white bg-danger border-0";
    feedback.innerHTML = '<i class="fas fa-times-circle mr-1"></i> คำตอบไม่ถูกต้อง ลองใหม่!';
    feedback.style.setProperty('display', 'block', 'important');
  }
}
setTimeout(() => {
  const solved = getSavedSolves();
  document.querySelectorAll('.options-container').forEach(container => {
    container.querySelectorAll('input[type="radio"]').forEach(radio => {
      const hash = radio.getAttribute('data-hash');
      if (solved.includes(hash)) {
        radio.checked = true;
        const label = radio.closest('.w-quiz-option');
        if (label) label.classList.add('selected');
        container.querySelectorAll('input[type="radio"]').forEach(r => r.disabled = true);
        container.querySelectorAll('.w-quiz-option').forEach(opt => opt.style.pointerEvents = 'none');
        const cell = container.closest('.question-cell');
        if (cell) {
          const btn = cell.querySelector('button');
          if (btn) btn.disabled = true;
          const fb = cell.querySelector('.feedback-msg');
          if (fb) {
            fb.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
            fb.innerHTML = '<i class="fas fa-check-circle mr-1"></i> เรียบร้อยแล้ว';
            fb.style.setProperty('display', 'block', 'important');
          }
        }
      }
    });
  });
  updateLocalProgress();
}, 200);
</script>"""

save_lesson(178, val178_0, val178_1, val178_2)
ctx.pop()
