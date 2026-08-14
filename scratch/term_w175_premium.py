import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l175 = db.session.query(TutorialLesson).filter_by(id=175).first()
blocks = json.loads(l175.content)

# ─── Upgrade Block 0 (Premium Neon styling, Icons, and clear Cards for Nmap scanning, NSE scripts, Nikto, OpenVAS) ───
blocks[0]['value'] = """## 🛠️ Exploitation Tools & Metasploit (เครื่องมือเจาะระบบและเมทาสปลอยต์)
---

หัวใจสำคัญของการประเมินระบบคือการสแกนเชิงลึกด้วยเครื่องมือระดับอุตสาหกรรม เพื่อตรวจสอบบริการ เวอร์ชัน และค้นหาช่องโหว่ความปลอดภัยที่นำไปสู่สิทธิ์ระดับแอดมิน

<style>
.w-neon-card {
  background: rgba(6, 8, 20, 0.45) !important;
  border: 1px solid rgba(244, 63, 94, 0.15) !important;
  border-radius: 12px !important;
  padding: 20px !important;
  margin-bottom: 24px !important;
  box-shadow: 0 8px 32px rgba(0,0,0,0.3), inset 0 0 15px rgba(244,63,94,0.02) !important;
  transition: all 0.25s ease !important;
}
.w-neon-card:hover {
  border-color: rgba(244, 63, 94, 0.35) !important;
  box-shadow: 0 8px 32px rgba(244,63,94,0.08), inset 0 0 20px rgba(244,63,94,0.03) !important;
}
.w-nmap-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 12px;
  margin-top: 14px;
}
.w-nmap-box {
  background: rgba(255,255,255,0.01);
  border: 1px solid rgba(255,255,255,0.04);
  border-radius: 6px;
  padding: 10px 14px;
  font-size: 0.8rem;
}
.w-code-inline {
  font-family: 'JetBrains Mono', monospace;
  color: #f43f5e;
  background: rgba(244,63,94,0.08);
  padding: 2px 6px;
  border-radius: 4px;
  font-weight: 700;
}
</style>

### 📡 1. Nmap CLI Commands & Scripting Engine (NSE)
<div class="w-neon-card">
  <p class="text-white mb-2" style="font-size:0.9rem; font-weight:600;"><i class="fas fa-satellite-dish mr-2 text-rose" style="color:#f43f5e;"></i> พารามิเตอร์การสั่งสแกน Nmap สแกนพอร์ตเป้าหมายเชิงลึก</p>
  <div class="w-nmap-grid">
    <div class="w-nmap-box"><span class="w-code-inline">-sT</span> TCP Connect Full Handshake</div>
    <div class="w-nmap-box"><span class="w-code-inline">-sS</span> TCP SYN Stealth Scan</div>
    <div class="w-nmap-box"><span class="w-code-inline">-sV</span> Service Version Detection</div>
    <div class="w-nmap-box"><span class="w-code-inline">-O</span> Operating System Detection</div>
    <div class="w-nmap-box"><span class="w-code-inline">-A</span> Aggressive Scan (All-in-One)</div>
    <div class="w-nmap-box"><span class="w-code-inline">-Pn</span> Skip Ping Host Discovery</div>
  </div>
  <p class="text-white mt-4 mb-2" style="font-size:0.85rem; font-weight:600;"><i class="fas fa-terminal mr-2 text-warning"></i> Nmap Scripting Engine (NSE) Categories</p>
  <p class="text-muted" style="font-size:0.75rem;">Lua scripts สำหรับยิงตรวจสอบหาช่องโหว่ความเสี่ยงสูงอัตโนมัติ:</p>
  <div class="w-nmap-grid">
    <div class="w-nmap-box" style="border-left: 2px solid #ef4444;"><strong style="color:#ffffff;">vuln</strong> ตรวจหาจุดบกพร่องรู้กันทั่วไป</div>
    <div class="w-nmap-box" style="border-left: 2px solid #f97316;"><strong style="color:#ffffff;">exploit</strong> จำลองยิงทำลายเพื่อรับสิทธิ์</div>
    <div class="w-nmap-box" style="border-left: 2px solid #3b82f6;"><strong style="color:#ffffff;">discovery</strong> ตรวจหารายละเอียดระบบเพิ่มเติม</div>
    <div class="w-nmap-box" style="border-left: 2px solid #10b981;"><strong style="color:#ffffff;">auth</strong> ตรวจสอบสิทธิ์ระบบล็อกอิน</div>
  </div>
</div>

---

### 🌐 2. Web Vulnerability Scanner: Nikto & OpenVAS GVM
<div class="w-neon-card">
  <div class="row">
    <div class="col-md-6 mb-3 mb-md-0">
      <h6 class="text-white font-weight-bold"><i class="fas fa-server mr-2 text-danger"></i> Nikto Web Server Scanner</h6>
      <p class="text-muted" style="font-size:0.78rem;">เครื่องมือกวาดหาไดเรกทอรีหลงเหลือ เช่น `/admin/`, แบ็กอัพไฟล์ `.bak` และระบบการตั้งค่า HTTP Header ผิดพลาดบนเป้าหมาย</p>
    </div>
    <div class="col-md-6">
      <h6 class="text-white font-weight-bold"><i class="fas fa-th-large mr-2 text-info"></i> OpenVAS (Greenbone GVM)</h6>
      <p class="text-muted" style="font-size:0.78rem;">ระบบสแกนเนอร์สถาปัตยกรรมขนาดใหญ่ กวาดช่องโหว่ระบบแบบอัตโนมัติ รันผ่านหน้าเว็บพรีเมียม (พอร์ต 9392) นำเสนอรายงานตรวจสอบครบวงจร</p>
    </div>
  </div>
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
  background: rgba(244, 63, 94, 0.04);
  border-color: rgba(244, 63, 94, 0.25);
  color: #ffffff;
}
.w-quiz-option.selected {
  background: rgba(244, 63, 94, 0.08);
  border-color: #f43f5e;
  color: #ffffff;
  box-shadow: 0 0 10px rgba(244, 63, 94, 0.2);
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
<p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. พารามิเตอร์ของ Nmap ตัวใดใช้สำหรับดึงรุ่นซอฟต์แวร์และบริการ (Service Version Detection) บนพอร์ตเป้าหมาย?</p>
<div class="options-container" data-q="q1">
  <label class="w-quiz-option">
    <input type="radio" name="nmap_ver" value="-sT" data-hash="false">
    -sT
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="nmap_ver" value="-sS" data-hash="false">
    -sS
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="nmap_ver" value="-sV" data-hash="b200b332bfa353a2f1b40d6cfa9286ebbc7e5c6a9b8979e2c65757d5f088198f">
    -sV
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="nmap_ver" value="-O" data-hash="false">
    -O
  </label>
</div>
<button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)">
<i class="fas fa-paper-plane mr-1"></i> Submit
</button>
<div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div>
</div>

<!-- Question 2 -->
<div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;">
<p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. พารามิเตอร์ใดของ Nmap ใช้สำหรับข้ามขั้นตอนการสแกน Ping (สมมติว่าโฮสต์เปิดใช้งานอยู่เสมอ)?</p>
<div class="options-container" data-q="q2">
  <label class="w-quiz-option">
    <input type="radio" name="nmap_ping" value="-Pn" data-hash="de6113ccf30f55cf643f8e401ec86eb61284d72851cf5718dfd38a0f9a2e61a2">
    -Pn
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="nmap_ping" value="-sP" data-hash="false">
    -sP
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="nmap_ping" value="-sC" data-hash="false">
    -sC
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="nmap_ping" value="-sV" data-hash="false">
    -sV
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
const lessonKey = 'solved_lesson_175';

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
    if (fill) fill.style.stroke = '#f43f5e';
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

l175.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=175).update({"content": l175.content})
db.session.commit()
print("Lesson 175 successfully upgraded and structured!")
ctx.pop()
