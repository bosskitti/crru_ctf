import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l174 = db.session.query(TutorialLesson).filter_by(id=174).first()
blocks = json.loads(l174.content)

# ─── Upgrade Block 0 (Premium Neon styling, Icons, and clear Cards for Passive OSINT, Shodan filters, TTL profiling) ───
blocks[0]['value'] = """## 🔍 Vulnerability Assessment (การวิเคราะห์หาช่องโหว่ทางเครือข่าย)
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
.w-ttl-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}
.w-ttl-table th, .w-ttl-table td {
  border: 1px solid rgba(255,255,255,0.08);
  padding: 8px 12px;
  font-size: 0.8rem;
  text-align: left;
}
.w-ttl-table th {
  background: rgba(255,255,255,0.03);
  color: #ffffff;
  font-weight: 700;
}
</style>

### 🔎 1. Passive OSINT: Offensive Search Engine & Stack Survey
<div class="w-neon-card">
  <p class="text-white mb-3" style="font-size:0.9rem; font-weight:600;"><i class="fas fa-search-plus mr-2 text-warning"></i> การหาข้อมูลเป้าหมายแบบไม่พึ่งพาการเชื่อมโยงตรงไปยังเครื่องปลายทาง</p>
  <div class="w-dork-item">
    <strong class="text-white" style="font-size:0.8rem;">🕵️‍♂️ Google Dorking operators</strong><br>
    <p class="text-muted mb-2" style="font-size:0.75rem;">คิวรีคัดหาเอกสารความลับของเป้าหมายบนดัชนีกูเกิล:</p>
    <span class="w-dork-code">site:ac.th intitle:"index of" "backup"</span> (หาโฟลเดอร์ไฟล์สำรองข้อมูล)
  </div>
  <div class="w-dork-item">
    <strong class="text-white" style="font-size:0.8rem;">📄 Metagoofil Metadata Extract</strong><br>
    <p class="text-muted mb-0" style="font-size:0.75rem;">โปรแกรมดาวน์โหลดและดูประวัติบันทึกไฟล์ (เช่น PDF, DOC) ของเป้าหมายเพื่อนำมาแรนสกัดหาชื่อบัญชีแอดมินหรือรุ่นซอฟต์แวร์ต้นแบบที่ใช้เขียน</p>
  </div>
  <div class="w-dork-item">
    <strong class="text-white" style="font-size:0.8rem;">🧱 Stack Survey extensions</strong><br>
    <p class="text-muted mb-0" style="font-size:0.75rem;">ระบบตรวจสอบ CMS หรือโปรแกรมเบื้องหลังเซิร์ฟเวอร์ เช่น <strong>Wappalyzer</strong>, <strong>BuiltWith</strong> และ <strong>PublicWWW</strong></p>
  </div>
</div>

---

### 🌐 2. Network Artifacts: Shodan & Censys
<div class="w-neon-card">
  <div class="row">
    <div class="col-md-6 mb-3 mb-md-0">
      <h6 class="text-white font-weight-bold"><i class="fas fa-globe mr-2 text-info"></i> DNS & Domain Artifacts</h6>
      <p class="text-muted" style="font-size:0.78rem;">การกวาดตรวจสอบประวัติ Domain และ Subdomains ดิบผ่านเว็บสาธารณะ เช่น <strong>WHOIS</strong> หรือ <strong>DNSdumpster</strong> เพื่อทำแผนผังเป้าหมาย</p>
    </div>
    <div class="col-md-6">
      <h6 class="text-white font-weight-bold"><i class="fas fa-satellite mr-2 text-violet" style="color:#a855f7;"></i> Shodan Search Filters</h6>
      <p class="text-muted mb-2" style="font-size:0.75rem;">เสิร์ชเอนจินส่องดูอุปกรณ์ IoT และพอร์ตเซิร์ฟเวอร์ที่เปิดต่อโลก:</p>
      <ul style="padding-left:16px; font-size:0.75rem; color:#cbd5e1; line-height:1.6;">
        <li><span class="w-dork-code">port:22</span> (กรองหาเฉพาะเครื่องที่เปิดพอร์ต SSH)</li>
        <li><span class="w-dork-code">org:"Google"</span> (ค้นหากลุ่มไอพีภายใต้องค์กรเป้าหมาย)</li>
        <li><span class="w-dork-code">vuln:"CVE-2019-19781"</span> (ค้นหาโฮสต์ที่ยังไม่แพตช์ช่องโหว่)</li>
      </ul>
    </div>
  </div>
</div>

---

### 🩺 3. Active Scanning: Ping OS Profiling & ARP
<div class="w-neon-card">
  <h6 class="text-white font-weight-bold mb-3"><i class="fas fa-fingerprint mr-2 text-success"></i> ระบบการจำแนกระบบปฏิบัติการผ่าน TTL และข้อมูล ARP</h6>
  <p class="text-muted" style="font-size:0.78rem;">ค่า <strong>TTL (Time to Live)</strong> ใน Echo Reply จากโปรแกรม Ping สามารถบอกได้ว่าเป้าหมายรัน OS อะไร:</p>
  <table class="w-ttl-table">
    <thead>
      <tr>
        <th>ระบบปฏิบัติการ (OS Target)</th>
        <th>ค่า TTL เริ่มต้นขากลับ (Default TTL)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="color:#84cc16; font-weight:bold;">Linux / Unix / macOS</td>
        <td style="font-family:\'JetBrains Mono\',monospace;">64</td>
      </tr>
      <tr>
        <td style="color:#38bdf8; font-weight:bold;">Microsoft Windows</td>
        <td style="font-family:\'JetBrains Mono\',monospace;">128</td>
      </tr>
      <tr>
        <td style="color:#eab308; font-weight:bold;">Network Devices (Cisco, Routers)</td>
        <td style="font-family:\'JetBrains Mono\',monospace;">255</td>
      </tr>
    </tbody>
  </table>
</div>"""

# ─── Upgrade Block 2 to Premium Multiple Choice Quiz ───
blocks[2]['value'] = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการบันทึกความสำเร็จและปลดล็อกปุ่มบทเรียนถัดไป:

<style>
.w-quiz-option {
  display: block;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 8px;
  padding: 12px 16px;
  margin-bottom: 10px;
  color: #cbd5e1;
  font-size: 0.84rem;
  cursor: pointer;
  transition: all 0.2s ease;
  position: relative;
}
.w-quiz-option:hover {
  background: rgba(139, 92, 246, 0.04);
  border-color: rgba(139, 92, 246, 0.25);
  color: #ffffff;
}
.w-quiz-option.selected {
  background: rgba(139, 92, 246, 0.08);
  border-color: #a855f7;
  color: #ffffff;
  box-shadow: 0 0 10px rgba(168, 85, 247, 0.2);
  font-weight: 700;
}
.w-quiz-option input[type="radio"] {
  display: none;
}
</style>

<div class="row align-items-center" style="margin:1.5rem auto; max-width:980px;">
<div class="col-md-8">

<!-- Question 1 -->
<div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;">
<p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. หากผลลัพธ์ Ping ไปยังเครื่องเป้าหมายมีค่า TTL เริ่มต้นเป็น 128 ระบบปฏิบัติการเป้าหมายมีแนวโน้มเป็นอะไร?</p>
<div class="options-container" data-q="q1">
  <label class="w-quiz-option">
    <input type="radio" name="ttl_os" value="Linux" data-hash="false">
    Linux / Unix
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="ttl_os" value="Windows" data-hash="dbb48a804b49cb376e107297e64177d612e694fb4e8ecfde4e0735cf1f3918a5">
    Windows
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="ttl_os" value="macOS" data-hash="false">
    macOS
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="ttl_os" value="Cisco Router" data-hash="false">
    Cisco Router
  </label>
</div>
<button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)">
<i class="fas fa-paper-plane mr-1"></i> Submit
</button>
<div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div>
</div>

<!-- Question 2 -->
<div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;">
<p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. Google Dorking query tag ใดใช้จำกัดผลลัพธ์ให้ค้นหาเฉพาะเว็บไซต์เป้าหมาย?</p>
<div class="options-container" data-q="q2">
  <label class="w-quiz-option">
    <input type="radio" name="dork_tag" value="ext:" data-hash="false">
    ext:
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="dork_tag" value="filetype:" data-hash="false">
    filetype:
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="dork_tag" value="site:" data-hash="476ca8cf30a3b2b3cc76785dc9ebf3bc4cd22d8d85f81e7d23a1058ad646c075">
    site:
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="dork_tag" value="intitle:" data-hash="false">
    intitle:
  </label>
</div>
<button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)">
<i class="fas fa-paper-plane mr-1"></i> Submit
</button>
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
<span id="lesson-status-txt" class="mt-3 d-block text-muted" style="font-size:0.78rem;">โปรดตอบคำถามให้ครบ 2 ข้อ</span>
</div>
</div>

</div>

<script>
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

  const fill = document.getElementById('lesson-gauge-fill');
  const text = document.getElementById('lesson-gauge-text');
  const status = document.getElementById('lesson-status-txt');

  if (fill) fill.setAttribute('stroke-dasharray', `${percent}, 100`);
  if (text) text.textContent = `${percent}%`;

  if (solved.length === total) {
    if (fill) fill.style.stroke = '#3ddc84';
    if (status) {
      status.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
    }
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
    feedback.innerHTML = '<i class="fas fa-times-circle mr-1"></i> คำตอบไม่ถูกต้อง ลองเลือกใหม่อีกครั้ง!';
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

l174.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=174).update({"content": l174.content})
db.session.commit()
print("Lesson 174 successfully upgraded and structured!")
ctx.pop()
