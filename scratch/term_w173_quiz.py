import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l173 = db.session.query(TutorialLesson).filter_by(id=173).first()
blocks = json.loads(l173.content)

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
  background: rgba(0, 240, 255, 0.04);
  border-color: rgba(0, 240, 255, 0.25);
  color: #ffffff;
}
.w-quiz-option.selected {
  background: rgba(0, 240, 255, 0.08);
  border-color: #00f0ff;
  color: #ffffff;
  box-shadow: 0 0 10px rgba(0, 240, 255, 0.2);
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
<p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. ในแบบจำลอง OSI Layer ใดทำหน้าที่ในการกำหนดทิศทางการส่งข้อมูล (Routing)?</p>
<div class="options-container" data-q="q1">
  <label class="w-quiz-option">
    <input type="radio" name="osi_layer" value="Transport Layer" data-hash="false">
    Transport Layer
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="osi_layer" value="Network Layer" data-hash="277bc1b69ad3178c775080e7221f75355694a08ba1c38fa8b79f38ebcb5c8a41">
    Network Layer (Layer 3)
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="osi_layer" value="Data Link Layer" data-hash="false">
    Data Link Layer
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="osi_layer" value="Application Layer" data-hash="false">
    Application Layer
  </label>
</div>
<button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)">
<i class="fas fa-paper-plane mr-1"></i> Submit
</button>
<div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div>
</div>

<!-- Question 2 -->
<div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;">
<p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. เครื่องมือส่งและรับข้อมูลระดับ Raw network connections ที่ได้ชื่อว่าเป็น Swiss Army Knife ของนักเจาะระบบคือ?</p>
<div class="options-container" data-q="q2">
  <label class="w-quiz-option">
    <input type="radio" name="swiss_knife" value="nmap" data-hash="false">
    nmap
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="swiss_knife" value="netcat" data-hash="c9b7f5256e2978000bd93d8435d648b26e03fb21884be5e38f6b864a66e4a2cd">
    netcat (nc)
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="swiss_knife" value="ping" data-hash="false">
    ping
  </label>
  <label class="w-quiz-option">
    <input type="radio" name="swiss_knife" value="wireshark" data-hash="false">
    wireshark
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
// Local storage progress tracking
const lessonKey = 'solved_lesson_173';

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
    if (fill) fill.style.stroke = '#00f0ff';
    if (status) status.textContent = `ทำเสร็จแล้ว ${solved.length}/${total} ข้อ`;
  }
}

// Option selection handler
document.addEventListener('click', function(e) {
  const label = e.target.closest('.w-quiz-option');
  if (label) {
    const container = label.closest('.options-container');
    if (container) {
      // Clear other selections in this question
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
    
    // Disable interaction
    cell.querySelectorAll('input[type="radio"]').forEach(r => r.disabled = true);
    cell.querySelectorAll('.w-quiz-option').forEach(opt => opt.style.pointerEvents = 'none');
    button.disabled = true;

    // Save solve status
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

// Auto init state on load
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

l173.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=173).update({"content": l173.content})
db.session.commit()
print("Lesson 173 Quiz updated to Multiple Choice!")
ctx.pop()
