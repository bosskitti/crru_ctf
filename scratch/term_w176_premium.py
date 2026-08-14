import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l176 = db.session.query(TutorialLesson).filter_by(id=176).first()
blocks = json.loads(l176.content)

# ─── Upgrade Block 0 (Premium Neon styling, Icons, and clear Cards for Metasploit, Persistence, PrivEsc, Lateral, Covering) ───
blocks[0]['value'] = """## 💀 Post-Exploitation & Privilege Escalation (การยึดสิทธิ์และการควบคุมระบบหลังเจาะ)
---

กระบวนการโจมตีเป้าหมายระยะสุดท้ายเพื่อสั่งยึดกุมควบคุมระบบถาวร เพิ่มระดับสิทธิ์ผู้ดูแลระบบ ลอบย้ายเครือข่าย ทำลายไฟล์ Log และส่งรายงานประเมินผลความปลอดภัย

<style>
.w-neon-card {
  background: rgba(6, 8, 20, 0.45) !important;
  border: 1px solid rgba(239, 68, 68, 0.15) !important;
  border-radius: 12px !important;
  padding: 20px !important;
  margin-bottom: 24px !important;
  box-shadow: 0 8px 32px rgba(0,0,0,0.3), inset 0 0 15px rgba(239,68,68,0.02) !important;
  transition: all 0.25s ease !important;
}
.w-neon-card:hover {
  border-color: rgba(239, 68, 68, 0.35) !important;
  box-shadow: 0 8px 32px rgba(239,68,68,0.08), inset 0 0 20px rgba(239,68,68,0.03) !important;
}
.w-list-item {
  background: rgba(255,255,255,0.015);
  border: 1px solid rgba(255,255,255,0.04);
  border-radius: 6px;
  padding: 10px 14px;
  margin-bottom: 10px;
}
.w-code-inline {
  font-family: 'JetBrains Mono', monospace;
  color: #ef4444;
  background: rgba(239,68,68,0.08);
  padding: 2px 6px;
  border-radius: 4px;
  font-weight: 700;
}
</style>

### 🚀 1. Metasploit Console & SearchSploit
<div class="w-neon-card">
  <p class="text-white mb-3" style="font-size:0.9rem; font-weight:600;"><i class="fas fa-terminal mr-2 text-danger"></i> ระบบควบคุม Payload และค้นหาโค้ดโจมตีจากเครื่อง Kali</p>
  <div class="w-list-item">
    <strong class="text-white" style="font-size:0.8rem;">🐚 msfconsole commands</strong><br>
    <p class="text-muted mb-2" style="font-size:0.75rem;">ชุดการสั่งรันโมดูลเจาะ Windows EternalBlue:</p>
    <span class="w-code-inline">use exploit/windows/smb/ms17_010_eternalblue</span>
  </div>
  <div class="w-list-item">
    <strong class="text-white" style="font-size:0.8rem;">📂 SearchSploit offline utility</strong><br>
    <p class="text-muted mb-2" style="font-size:0.75rem;">สืบหาโค้ดโจมตีช่องโหว่ความปลอดภัยโดยไม่ต้องเชื่อมอินเทอร์เน็ต:</p>
    <span class="w-code-inline">searchsploit linux kernel 5.4</span>
  </div>
</div>

---

### 🔑 2. Persistence: Creating Backdoors & Web Shells
<div class="w-neon-card">
  <div class="row">
    <div class="col-md-6 mb-3 mb-md-0">
      <h6 class="text-white font-weight-bold"><i class="fas fa-user-plus mr-2 text-warning"></i> User Creation & Backdoors</h6>
      <p class="text-muted" style="font-size:0.78rem;">การรักษาสิทธิ์รันถาวรโดยสร้างบัญชี User พิเศษสวมรอย (เช่น <span class="w-code-inline">useradd</span>) หรือฝัง Payload ดักรับสิทธิ์ควบคุม (เช่น msfvenom)</p>
    </div>
    <div class="col-md-6">
      <h6 class="text-white font-weight-bold"><i class="fas fa-file-code mr-2 text-success"></i> Web Shells (สคริปต์สลัดช่องโหว่)</h6>
      <p class="text-muted" style="font-size:0.78rem;">การอัปโหลดไฟล์คำสั่งขนาดสั้นไว้ในหน้าเว็บเพื่อประมวลผลคำสั่ง OS ผ่าน URL คิวรี:</p>
      <span class="w-code-inline">&lt;?php system($_GET[\'cmd\']); ?&gt;</span>
    </div>
  </div>
</div>

---

### 📈 3. Privilege Escalation & Lateral Movement
<div class="w-neon-card">
  <h6 class="text-white font-weight-bold mb-3"><i class="fas fa-long-arrow-alt-up mr-2 text-info"></i> แนวทางการยกระดับสิทธิ์และการย้ายเป้าหมาย</h6>
  <div class="w-list-item">
    <strong class="text-white" style="font-size:0.8rem;">📈 Vertical Privilege Escalation</strong><br>
    <p class="text-muted" style="font-size:0.72rem;">การไต่เต้าขโมยระดับสิทธิ์ขึ้นสู่ Administrator หรือ Root (เช่น การหาช่องโหว่ SUID)</p>
  </div>
  <div class="w-list-item">
    <strong class="text-white" style="font-size:0.8rem;">↔️ Horizontal Privilege Escalation</strong><br>
    <p class="text-muted" style="font-size:0.72rem;">การยึดสิทธิ์ข้ามไปสวมรอยใช้บัญชีของผู้อื่นที่มีระดับสิทธิ์ความปลอดภัยเทียบเท่ากัน</p>
  </div>
  <div class="w-list-item">
    <strong class="text-white" style="font-size:0.8rem;">🗺️ Lateral Movement (การขยับขยายควบคุมเครือข่าย)</strong><br>
    <p class="text-muted" style="font-size:0.72rem;">เจาะข้อมูลจากเครื่องที่ยึดได้ข้ามไปสวมสิทธิ์ควบคุมเครื่องอื่นๆ ในวงแลน เช่น เทคนิค Pass-the-Hash (PtH) หรือ Pass-the-Ticket (PtT)</p>
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
  background: rgba(239, 68, 68, 0.04);
  border-color: rgba(239, 68, 68, 0.25);
  color: #ffffff;
}
.w-quiz-option.selected {
  background: rgba(239, 68, 68, 0.08);
  border-color: #ef4444;
  color: #ffffff;
  box-shadow: 0 0 10px rgba(239, 68, 68, 0.2);
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
<p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. การเปลี่ยนสิทธิ์จากผู้ใช้งานทั่วไป (Normal user) ขึ้นเป็นสิทธิ์ผู้ดูแลระบบ (Root/Admin) เรียกว่าอะไร?</p>
<div class="options-container" data-q="q1">
  <label class="w-quiz-option">
    <input type="radio" name="priv_esc" value="Horizontal" data-hash="false">
    Horizontal Privilege Escalation
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="priv_esc" value="Vertical" data-hash="d3cbf07c6f0927dfa60ea57790b4d4814d4bc10b27b9c9f6d4d123e7f0b503db">
    Vertical Privilege Escalation
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="priv_esc" value="Lateral" data-hash="false">
    Lateral Movement
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="priv_esc" value="Exfiltration" data-hash="false">
    Data Exfiltration
  </label>
</div>
<button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)">
<i class="fas fa-paper-plane mr-1"></i> Submit
</button>
<div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div>
</div>

<!-- Question 2 -->
<div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;">
<p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. คำสั่งมาตรฐานใดใน Linux ที่สามารถสวมรอยใช้หาไฟล์ระบบที่ตั้งค่าสิทธิ์ SUID บกพร่อง เพื่อใช้ทำ Privilege Escalation?</p>
<div class="options-container" data-q="q2">
  <label class="w-quiz-option">
    <input type="radio" name="suid_cmd" value="grep" data-hash="false">
    grep
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="suid_cmd" value="cat" data-hash="false">
    cat
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="suid_cmd" value="find" data-hash="f8812c75a4da4d53860bb402131ab1053be4162464eb789c674251147a4eb31d">
    find
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="suid_cmd" value="chmod" data-hash="false">
    chmod
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
const lessonKey = 'solved_lesson_176';

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
    if (fill) fill.style.stroke = '#ef4444';
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

l176.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=176).update({"content": l176.content})
db.session.commit()
print("Lesson 176 successfully upgraded and structured!")
ctx.pop()
