import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

# Helper function to generate standardized 3-blocks content
def save_lesson(lid, block0_val, block1_val, block2_val):
    l = db.session.query(TutorialLesson).filter_by(id=lid).first()
    blocks = [
        {"type": "markdown", "value": block0_val},
        {"type": "markdown", "value": block1_val},
        {"type": "markdown", "value": block2_val}
    ]
    l.content = json.dumps(blocks, ensure_ascii=False)
    db.session.query(TutorialLesson).filter_by(id=lid).update({"content": l.content})
    db.session.commit()
    print(f"Lesson {lid} successfully upgraded to 3-blocks structure!")

# ─── 1. Lesson 181: Introduction & Encoding ───
val181_0 = """## 🔑 Cryptography & Encoding (วิทยาการรหัสลับและการแปลงรหัสพื้นฐาน)
---

ยินดีต้อนรับสู่บทเรียนวิทยาการรหัสลับและพื้นฐานการแปลงสภาพข้อมูลดิบให้เป็นตัวอักษรเพื่อใช้สื่อสารอย่างปลอดภัย

<style>
.w-neon-card {
  background: rgba(6, 8, 20, 0.45) !important;
  border: 1px solid rgba(236, 72, 153, 0.15) !important;
  border-radius: 12px !important;
  padding: 20px !important;
  margin-bottom: 24px !important;
  box-shadow: 0 8px 32px rgba(0,0,0,0.3), inset 0 0 15px rgba(236,72,153,0.02) !important;
}
.w-enc-badge {
  font-family: 'JetBrains Mono', monospace;
  background: rgba(236, 72, 153, 0.08);
  color: #ec4899;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 0.72rem;
  font-weight: 700;
}
</style>

### 📄 1. Data Encoding vs Encryption
- 🌐 **Encoding**: การแปลงสภาพข้อมูลดิบเพื่อให้เหมาะสมแก่การรับส่งข้ามระบบ เช่น การส่งภาพดิบข้ามเครือข่าย หรือป้องกันตัวอักษรพิเศษพัง (เช่น **Base64**, **Hex**, **URL Encoding**) โดยไม่มีการพึ่งพากุญแจลับ
- 🔒 **Encryption**: การเข้ารหัสลับเพื่อป้องกันความลับรั่วไหล โดยผู้สืบข้อมูลต้องใช้กุญแจถอดรหัส (Key) เท่านั้น

---

### 🧱 2. Common Encodings
- **Base64**: แปลงข้อมูลไบนารีเป็นตัวอักษร ASCII 64 ตัวอักษร มักลงท้ายด้วยสัญลักษณ์ `=`
- **Hex (Hexadecimal)**: แปลงเป็นรหัสเลขฐาน 16 (0-9, A-F)"""

val181_1 = """### 💻 Data Encoding Sandbox (จำลองระบบแปลงค่ารหัส)

คลิกหัวข้อด้านซ้ายมือเพื่อจำลอง และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูรหัสผลลัพธ์:

<style>
.w-sandbox-main{display:flex;gap:20px;margin:2rem auto;max-width:1050px;}
@media(max-width:820px){.w-sandbox-main{flex-direction:column;}}
.w-sandbox-nav{width:220px;display:flex;flex-direction:column;gap:6px;flex-shrink:0;}
@media(max-width:820px){.w-sandbox-nav{width:100%;flex-direction:row;flex-wrap:wrap;}}
.w-nav-item{padding:8px 12px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.04);border-radius:6px;font-size:0.75rem;color:#cbd5e1;cursor:pointer;text-align:left;transition:all 0.15s ease;}
.w-nav-item:hover, .w-nav-item.active{border-color:#ec4899;color:#ffffff;background:rgba(236,72,153,0.04);}
.w-nav-item.active{font-weight:bold;box-shadow:0 0 8px rgba(236,72,153,0.15);}
.w-sandbox-panels{flex:1;display:flex;flex-direction:column;gap:14px;}
.w-sand-panel{display:none;background:#05070f;border:1px solid rgba(255, 255, 255, 0.08);border-radius:10px;padding:20px;box-shadow:0 8px 24px rgba(0,0,0,0.45);box-sizing:border-box;}
.w-sand-panel.active{display:block !important;}
.w-sand-hdr{font-size:0.95rem;font-weight:800;color:#ffffff;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:10px;margin-bottom:14px;display:flex;justify-content:between;align-items:center;}
.w-sand-hdr span.tag{font-size:0.65rem;padding:2px 8px;border-radius:4px;background:rgba(236,72,153,0.08);border:1px solid rgba(236,72,153,0.2);color:#ec4899;font-family:'JetBrains Mono',monospace;}
.w-sand-code{font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#ec4899;white-space:pre-wrap;margin:0 0 12px;background:rgba(0,0,0,0.2);padding:14px;border-radius:8px;border:1px solid rgba(255,255,255,0.02);}
.w-sand-term-container{position:relative;background:#02040a;border:1px solid rgba(255,255,255,0.06);border-radius:8px;margin-bottom:16px;box-shadow:inset 0 2px 8px rgba(0,0,0,0.9);overflow:hidden;}
.w-sand-term-bar{background:rgba(255,255,255,0.03);padding:6px 12px;border-bottom:1px solid rgba(255,255,255,0.05);display:flex;justify-content:space-between;align-items:center;}
.w-sand-term-title{font-size:0.65rem;color:#64748b;font-weight:800;letter-spacing:0.06em;font-family:'JetBrains Mono',monospace;}
.w-sand-term-btn{background:rgba(236,72,153,0.1);border:1px solid rgba(236,72,153,0.3);border-radius:4px;color:#ec4899;font-size:0.68rem;padding:3px 8px;cursor:pointer;font-family:'JetBrains Mono',monospace;font-weight:700;transition:all 0.15s ease;display:flex;align-items:center;gap:4px;}
.w-sand-term-btn:hover{background:#ec4899;color:#02040a;box-shadow:0 0 8px rgba(236,72,153,0.4);}
.w-sand-term{font-family:'JetBrains Mono',monospace;font-size:0.76rem;color:#a7f3d0;padding:12px 16px;white-space:pre-wrap;min-height:90px;}
.w-sand-term span.prompt{color:#3ddc84;}
.w-sand-term span.cmd{color:#ffffff;font-weight:bold;}
.w-sand-expl{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:16px;font-size:0.83rem;color:#cbd5e1;line-height:1.65;}
.w-sand-expl h5{margin:0 0 8px;font-size:0.85rem;color:#fbbf24;font-weight:bold;}
.w-sand-expl p{margin:0 0 10px;}
</style>
<div class="w-sandbox-main"><div class="w-sandbox-nav"><button id="nav-item-base64" class="w-nav-item active" onclick="showSandboxItem('base64', this)">1. Base64 Encode</button><button id="nav-item-hex" class="w-nav-item" onclick="showSandboxItem('hex', this)">2. Hex/Base16 Encode</button></div><div class="w-sandbox-panels"><div id="panel-base64" class="w-sand-panel"><div class="w-sand-hdr"><span>1. Base64 Text Encoding</span> <span class="tag">Base64</span></div><pre class="w-sand-code">echo -n "RPCA Cyber" | base64</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startEncSim('base64')">▶ Run Simulation</button></div><div id="term-base64" class="w-sand-term"><span class="prompt">kali$</span> [กดปุ่ม Run Simulation เพื่อจำลองแปลง Base64]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>Base64 รับประมวลผลข้อความและส่งผลอักษร ASCII ที่มีตัวอักษรพิมพ์ใหญ่ พิมพ์เล็ก ตัวเลข และสัญลักษณ์ padding = ปิดท้าย</p></div></div><div id="panel-hex" class="w-sand-panel"><div class="w-sand-hdr"><span>2. Hexadecimal Text Encoding</span> <span class="tag">Hex/Base16</span></div><pre class="w-sand-code">echo -n "RPCA Cyber" | xxd -p</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startEncSim('hex')">▶ Run Simulation</button></div><div id="term-hex" class="w-sand-term"><span class="prompt">kali$</span> [กดปุ่ม Run Simulation เพื่อจำลองแปลง Hex]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>Hex แปลงอักขระทีละบิตให้เป็นเลขฐาน 16 ยอดนิยม (0-9 และ A-F) เหมาะกับการส่งแพ็กเก็ตข้อมูลเน็ตเวิร์กดิบ</p></div></div></div></div>
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
window.startEncSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span class="prompt">kali$</span> <span class="cmd">Converting payload...</span>\\n[.] Accessing binary encoders...';
  setTimeout(() => {
    if (itemKey === 'base64') {
      term.innerHTML = '<span class="prompt">kali$</span> <span class="cmd">base64 result:</span>\\n<span style="color:#ec4899; font-weight:bold;">UlBDQSBDeWJlcg==</span>';
    } else if (itemKey === 'hex') {
      term.innerHTML = '<span class="prompt">kali$</span> <span class="cmd">xxd result:</span>\\n<span style="color:#ec4899; font-weight:bold;">52504341204379626572</span>';
    }
  }, 1000);
}
</script>"""

val181_2 = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

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
  background: rgba(236, 72, 153, 0.04);
  border-color: rgba(236, 72, 153, 0.25);
  color: #ffffff;
}
.w-quiz-option.selected {
  background: rgba(236, 72, 153, 0.08);
  border-color: #ec4899;
  color: #ffffff;
  box-shadow: 0 0 10px rgba(236, 72, 153, 0.2);
  font-weight: 700;
}
.w-quiz-option input[type="radio"] {
  display: none;
}
</style>
<div class="row align-items-center" style="margin:1.5rem auto; max-width:980px;"><div class="col-md-8"><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. กระบวนการแปลงสภาพข้อมูลดิบให้เหมาะสมในการส่งผ่าน โดยไม่มีความลับและไม่พึ่งพาคีย์ลับคืออะไร?</p><div class="options-container" data-q="q1"><label class="w-quiz-option"><input type="radio" name="enc_opt" value="Encoding" data-hash="847eb221f75355694a08ba1c38fa8b79f38ebcb5c8a41df5718dfd38a0f9a2e61">การแปลงรหัส (Encoding)</label><label class="w-quiz-option"><input type="radio" name="enc_opt" value="Encryption" data-hash="false">การเข้ารหัสลับ (Encryption)</label><label class="w-quiz-option"><input type="radio" name="enc_opt" value="Hashing" data-hash="false">การทำแฮช (Hashing)</label><label class="w-quiz-option"><input type="radio" name="enc_opt" value="Stegano" data-hash="false">การซ่อนข้อมูล (Steganography)</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. รูปแบบการเข้ารหัส Base64 นิยมส่งผ่านตัวอักขระพิเศษตัวใดปิดท้ายข้อความ (Padding)?</p><div class="options-container" data-q="q2"><label class="w-quiz-option"><input type="radio" name="base64_pad" value="=" data-hash="2e61a2cdbbf24c56e2978000bd93d8435d648b26e03fb21884be5e38f6b864a66e4a2cd">เครื่องหมายเท่ากับ (=)</label><label class="w-quiz-option"><input type="radio" name="base64_pad" value="*" data-hash="false">เครื่องหมายดอกจัน (*)</label><label class="w-quiz-option"><input type="radio" name="base64_pad" value="?" data-hash="false">เครื่องหมายคำถาม (?)</label><label class="w-quiz-option"><input type="radio" name="base64_pad" value="#" data-hash="false">เครื่องหมายชาร์ป (#)</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div></div><div class="col-md-4 text-center"><div class="p-4" style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); border-radius:12px; min-height:220px; display:flex; flex-direction:column; justify-content:center; align-items:center;"><span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;">Lesson Progress</span><div class="neon-gauge-container"><svg class="neon-gauge" viewBox="0 0 36 36"><path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><path class="neon-gauge-fill" id="lesson-gauge-fill" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text">0%</text></svg></div><span id="lesson-status-txt" class="mt-3 d-block text-muted" style="font-size:0.78rem;">โปรดตอบคำถามให้ครบ 2 ข้อ</span></div></div></div>
<style>
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:#ec4899; stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease, stroke 0.5s ease; filter:drop-shadow(0 0 5px rgba(236,72,153,0.5));}
.neon-gauge-text {fill:#ffffff; font-family:\'JetBrains Mono\',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}
</style>
<script>
const lessonKey = 'solved_lesson_181';
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
    if (fill) fill.style.stroke = '#ec4899';
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

save_lesson(181, val181_0, val181_1, val181_2)

# ─── 2. Lesson 182: Symmetric & Asymmetric Crypto ───
val182_0 = """## 🔑 Symmetric & Asymmetric Crypto (การเข้ารหัสแบบกุญแจสมมาตรและอสมมาตร)
---

ยินดีต้อนรับสู่บทเรียนการเข้ารหัสลับเชิงพาณิชย์และวิธีการจัดการกุญแจ (Keys) เพื่อการคุ้มครองข้อมูลการสื่อสารขั้นสูง

<style>
.w-neon-card {
  background: rgba(6, 8, 20, 0.45) !important;
  border: 1px solid rgba(139, 92, 246, 0.15) !important;
  border-radius: 12px !important;
  padding: 20px !important;
  margin-bottom: 24px !important;
  box-shadow: 0 8px 32px rgba(0,0,0,0.3), inset 0 0 15px rgba(139,92,246,0.02) !important;
}
.w-code-inline {
  font-family: 'JetBrains Mono', monospace;
  background: rgba(139, 92, 246, 0.08);
  color: #a855f7;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 0.76rem;
  font-weight: 700;
}
</style>

### 🔒 1. Symmetric Encryption (กุญแจสมมาตร)
ใช้กุญแจเดี่ยวร่วมกัน (Shared key) ในการเข้ารหัสและถอดรหัสลับ:
- ⚡ **ข้อดี**: ประมวลผลได้รวดเร็วมาก เหมาะกับการเข้ารหัสไฟล์ขนาดใหญ่
- 🛡️ **ตัวอย่างมาตรฐาน**: **AES** (Advanced Encryption Standard), **DES**, **3DES**

---

### 🔑 2. Asymmetric Encryption (กุญแจอสมมาตร)
การทำงานแยกเป็นคู่กุญแจ (KeyPair) คือกุญแจสาธารณะ (Public Key) และกุญแจส่วนตัว (Private Key):
- 🤝 **การแลกเปลี่ยน**: ทุกคนสามารถเข้าใช้ **Public Key** เข้ารหัสข้อมูลส่งมาให้เราได้ แต่เฉพาะ **Private Key** ของเราเองเท่านั้นที่จะแกะอ่านได้
- 🛡️ **ตัวอย่างมาตรฐาน**: **RSA**, **ECC** (Elliptic Curve Cryptography)"""

val182_1 = """### 💻 Encryption & Decryption Sandbox (จำลองระบบการเข้ารหัสกุญแจคู่)

คลิกหัวข้อด้านซ้ายมือเพื่อศึกษาการใช้กุญแจเข้ารหัส และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูรหัสลับ:

<style>
.w-sandbox-main{display:flex;gap:20px;margin:2rem auto;max-width:1050px;}
@media(max-width:820px){.w-sandbox-main{flex-direction:column;}}
.w-sandbox-nav{width:220px;display:flex;flex-direction:column;gap:6px;flex-shrink:0;}
@media(max-width:820px){.w-sandbox-nav{width:100%;flex-direction:row;flex-wrap:wrap;}}
.w-nav-item{padding:8px 12px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.04);border-radius:6px;font-size:0.75rem;color:#cbd5e1;cursor:pointer;text-align:left;transition:all 0.15s ease;}
.w-nav-item:hover, .w-nav-item.active{border-color:#a855f7;color:#ffffff;background:rgba(168,85,247,0.04);}
.w-nav-item.active{font-weight:bold;box-shadow:0 0 8px rgba(168,85,247,0.15);}
.w-sandbox-panels{flex:1;display:flex;flex-direction:column;gap:14px;}
.w-sand-panel{display:none;background:#05070f;border:1px solid rgba(255, 255, 255, 0.08);border-radius:10px;padding:20px;box-shadow:0 8px 24px rgba(0,0,0,0.45);box-sizing:border-box;}
.w-sand-panel.active{display:block !important;}
.w-sand-hdr{font-size:0.95rem;font-weight:800;color:#ffffff;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:10px;margin-bottom:14px;display:flex;justify-content:between;align-items:center;}
.w-sand-hdr span.tag{font-size:0.65rem;padding:2px 8px;border-radius:4px;background:rgba(168,85,247,0.08);border:1px solid rgba(168,85,247,0.2);color:#a855f7;font-family:'JetBrains Mono',monospace;}
.w-sand-code{font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#a855f7;white-space:pre-wrap;margin:0 0 12px;background:rgba(0,0,0,0.2);padding:14px;border-radius:8px;border:1px solid rgba(255,255,255,0.02);}
.w-sand-term-container{position:relative;background:#02040a;border:1px solid rgba(255,255,255,0.06);border-radius:8px;margin-bottom:16px;box-shadow:inset 0 2px 8px rgba(0,0,0,0.9);overflow:hidden;}
.w-sand-term-bar{background:rgba(255,255,255,0.03);padding:6px 12px;border-bottom:1px solid rgba(255,255,255,0.05);display:flex;justify-content:space-between;align-items:center;}
.w-sand-term-title{font-size:0.65rem;color:#64748b;font-weight:800;letter-spacing:0.06em;font-family:'JetBrains Mono',monospace;}
.w-sand-term-btn{background:rgba(168,85,247,0.1);border:1px solid rgba(168,85,247,0.3);border-radius:4px;color:#a855f7;font-size:0.68rem;padding:3px 8px;cursor:pointer;font-family:'JetBrains Mono',monospace;font-weight:700;transition:all 0.15s ease;display:flex;align-items:center;gap:4px;}
.w-sand-term-btn:hover{background:#a855f7;color:#02040a;box-shadow:0 0 8px rgba(168,85,247,0.4);}
.w-sand-term{font-family:'JetBrains Mono',monospace;font-size:0.76rem;color:#a7f3d0;padding:12px 16px;white-space:pre-wrap;min-height:90px;}
.w-sand-term span.prompt{color:#3ddc84;}
.w-sand-term span.cmd{color:#ffffff;font-weight:bold;}
.w-sand-expl{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:16px;font-size:0.83rem;color:#cbd5e1;line-height:1.65;}
.w-sand-expl h5{margin:0 0 8px;font-size:0.85rem;color:#fbbf24;font-weight:bold;}
.w-sand-expl p{margin:0 0 10px;}
</style>
<div class="w-sandbox-main"><div class="w-sandbox-nav"><button id="nav-item-aes" class="w-nav-item active" onclick="showSandboxItem('aes', this)">1. AES Symmetric</button><button id="nav-item-rsa" class="w-nav-item" onclick="showSandboxItem('rsa', this)">2. RSA Asymmetric</button></div><div class="w-sandbox-panels"><div id="panel-aes" class="w-sand-panel"><div class="w-sand-hdr"><span>1. AES-256 Symmetric Cipher</span> <span class="tag">AES Encryption</span></div><pre class="w-sand-code">openssl enc -aes-256-cbc -salt -in msg.txt -out cipher.enc -k key123</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startCryptSim('aes')">▶ Run Simulation</button></div><div id="term-aes" class="w-sand-term"><span class="prompt">crypt-cli$</span> [กดปุ่ม Run Simulation เพื่อเข้ารหัสสมมาตร]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>AES 256 บิตใช้คีย์ตัวหลัก `key123` สำหรับเข้ารหัสและถอดรหัส (Symmetric Key) มีความปลอดภัยของความลับสูง</p></div></div><div id="panel-rsa" class="w-sand-panel"><div class="w-sand-hdr"><span>2. RSA Asymmetric Keypair Generate</span> <span class="tag">RSA Crypt</span></div><pre class="w-sand-code">openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:2048
openssl pkey -in private.pem -pubout -out public.pem</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startCryptSim('rsa')">▶ Run Simulation</button></div><div id="term-rsa" class="w-sand-term"><span class="prompt">crypt-cli$</span> [กดปุ่ม Run Simulation เพื่อจำลองรัน RSA]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>สร้างคู่กุญแจความยาว 2048 บิต โดยสกัดกุญแจสาธารณะ (public.pem) ส่งมอบเพื่อใช้เข้ารหัสลับจากทุกแห่งทั่วโลก</p></div></div></div></div>
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
window.startCryptSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span class="prompt">crypt-cli$</span> <span class="cmd">Processing cryptographic math...</span>\\n[.] Executing OpenSSL cipher block...';
  setTimeout(() => {
    if (itemKey === 'aes') {
      term.innerHTML = '<span class="prompt">crypt-cli$</span> <span class="cmd">cat cipher.enc</span>\\nU2FsdGVkX18mNq7Lg4P6/4O9HpqkL12N4d7xS8123kL/==\\n\\n[+] AES Symmetric Encryption completed successfully!';
    } else if (itemKey === 'rsa') {
      term.innerHTML = '<span class="prompt">crypt-cli$</span> <span class="cmd">cat public.pem</span>\\n-----BEGIN PUBLIC KEY-----\\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0...\\n-----END PUBLIC KEY-----\\n[+] RSA Asymmetric Keypair successfully generated!';
    }
  }, 1000);
}
</script>"""

val182_2 = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

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
  box-shadow: 0 0 10px rgba(139, 92, 246, 0.2);
  font-weight: 700;
}
.w-quiz-option input[type="radio"] {
  display: none;
}
</style>
<div class="row align-items-center" style="margin:1.5rem auto; max-width:980px;"><div class="col-md-8"><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. ระบบการเข้ารหัสลับที่ใช้กุญแจลับเดี่ยว (Single Shared Key) ทั้งการเข้ารหัสและถอดรหัสเรียกว่าอะไร?</p><div class="options-container" data-q="q1"><label class="w-quiz-option"><input type="radio" name="sym_type" value="Symmetric" data-hash="d3cbf07c6f0927dfa60ea57790b4d4814d4bc10b27b9c9f6d4d123e7f0b503db">การเข้ารหัสแบบกุญแจสมมาตร (Symmetric Encryption)</label><label class="w-quiz-option"><input type="radio" name="sym_type" value="Asymmetric" data-hash="false">การเข้ารหัสแบบกุญแจอสมมาตร (Asymmetric Encryption)</label><label class="w-quiz-option"><input type="radio" name="sym_type" value="Hashing" data-hash="false">การทำแฮช (Hashing)</label><label class="w-quiz-option"><input type="radio" name="sym_type" value="Encoding" data-hash="false">การแปลงรหัส (Encoding)</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. ในระบบกุญแจอสมมาตร (Asymmetric) กุญแจข้อใดใช้เผยแพร่ให้สาธารณะนำไปใช้เข้ารหัสข้อมูลก่อนจัดส่ง?</p><div class="options-container" data-q="q2"><label class="w-quiz-option"><input type="radio" name="asym_key" value="Public Key" data-hash="a95aa975765796245d8b8ff716d0046522bb33f749eb721867c4e515d18d451">กุญแจสาธารณะ (Public Key)</label><label class="w-quiz-option"><input type="radio" name="asym_key" value="Private Key" data-hash="false">กุญแจส่วนตัว (Private Key)</label><label class="w-quiz-option"><input type="radio" name="asym_key" value="Shared Key" data-hash="false">กุญแจใช้ร่วมกัน (Shared Key)</label><label class="w-quiz-option"><input type="radio" name="asym_key" value="Session Key" data-hash="false">กุญแจชั่วคราว (Session Key)</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div></div><div class="col-md-4 text-center"><div class="p-4" style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); border-radius:12px; min-height:220px; display:flex; flex-direction:column; justify-content:center; align-items:center;"><span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;">Lesson Progress</span><div class="neon-gauge-container"><svg class="neon-gauge" viewBox="0 0 36 36"><path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><path class="neon-gauge-fill" id="lesson-gauge-fill" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text">0%</text></svg></div><span id="lesson-status-txt" class="mt-3 d-block text-muted" style="font-size:0.78rem;">โปรดตอบคำถามให้ครบ 2 ข้อ</span></div></div></div>
<style>
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:#a855f7; stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease, stroke 0.5s ease; filter:drop-shadow(0 0 5px rgba(168,85,247,0.5));}
.neon-gauge-text {fill:#ffffff; font-family:\'JetBrains Mono\',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}
</style>
<script>
const lessonKey = 'solved_lesson_182';
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

save_lesson(182, val182_0, val182_1, val182_2)

# ─── 3. Lesson 183: Hashing & Message Digests ───
val183_0 = """## 🔑 Hashing & Message Digests (การทำแฮชและการตรวจสอบความถูกต้องข้อมูล)
---

ยินดีต้อนรับสู่บทเรียนการสกัดข้อมูลเป็นค่าความถูกต้องที่ไม่มีวันกู้คืน (Hashing) ตรรกะสำคัญในการเก็บรหัสผ่านและทวนค่าความปลอดภัยไฟล์

<style>
.w-neon-card {
  background: rgba(6, 8, 20, 0.45) !important;
  border: 1px solid rgba(59, 130, 246, 0.15) !important;
  border-radius: 12px !important;
  padding: 20px !important;
  margin-bottom: 24px !important;
  box-shadow: 0 8px 32px rgba(0,0,0,0.3), inset 0 0 15px rgba(59,130,246,0.02) !important;
}
.w-hash-code {
  font-family: 'JetBrains Mono', monospace;
  background: rgba(0,0,0,0.3);
  padding: 10px;
  border-radius: 6px;
  color: #3b82f6;
  font-size: 0.72rem;
  border: 1px solid rgba(59,130,246,0.15);
  margin-top: 6px;
}
</style>

### 📄 1. One-Way Property (การสื่อสารทางเดียว)
ฟังก์ชันแฮชรับข้อมูลขนาดใดก็ตามและประมวลผลออกมาเป็นค่าขนาดความยาวคงที่ (Fixed-length digest) โดยไม่มีทางย้อนถอดสมการกู้ข้อความตั้งต้นได้:
- 🚫 **ไม่มีกุญแจถอดรหัส**: การเปรียบเทียบรหัสผ่านต้องทำผ่านการคำนวณแฮชเทียบกันเท่านั้น
- 💥 **Collision Resistance**: หาข้อมูลสองชุดที่มีค่าแฮชตรงกันไม่ได้เลย

---

### 🛡️ 2. Common Hash Functions
- **MD5**: ผลลัพธ์ความยาว 128 บิต (พบลูปชนกันง่าย ปัจจุบันเลิกใช้เก็บรหัสผ่านแล้ว)
- **SHA-256**: ผลลัพธ์ความยาว 256 บิต (32 ไบต์) มาตรฐานความปลอดภัยสูงสุดปัจจุบัน
  <div class="w-hash-code">Text: "admin" -> MD5: 21232f297a57a5a743894a0e4a801fc3</div>"""

val183_1 = """### 💻 Cryptographic Hashing Sandbox (จำลองการคำนวณและกู้คืนแฮช)

คลิกหัวข้อด้านซ้ายมือเพื่อจำลอง และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลลัพธ์:

<style>
.w-sandbox-main{display:flex;gap:20px;margin:2rem auto;max-width:1050px;}
@media(max-width:820px){.w-sandbox-main{flex-direction:column;}}
.w-sandbox-nav{width:220px;display:flex;flex-direction:column;gap:6px;flex-shrink:0;}
@media(max-width:820px){.w-sandbox-nav{width:100%;flex-direction:row;flex-wrap:wrap;}}
.w-nav-item{padding:8px 12px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.04);border-radius:6px;font-size:0.75rem;color:#cbd5e1;cursor:pointer;text-align:left;transition:all 0.15s ease;}
.w-nav-item:hover, .w-nav-item.active{border-color:#3b82f6;color:#ffffff;background:rgba(59,130,246,0.04);}
.w-nav-item.active{font-weight:bold;box-shadow:0 0 8px rgba(59,130,246,0.15);}
.w-sandbox-panels{flex:1;display:flex;flex-direction:column;gap:14px;}
.w-sand-panel{display:none;background:#05070f;border:1px solid rgba(255, 255, 255, 0.08);border-radius:10px;padding:20px;box-shadow:0 8px 24px rgba(0,0,0,0.45);box-sizing:border-box;}
.w-sand-panel.active{display:block !important;}
.w-sand-hdr{font-size:0.95rem;font-weight:800;color:#ffffff;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:10px;margin-bottom:14px;display:flex;justify-content:between;align-items:center;}
.w-sand-hdr span.tag{font-size:0.65rem;padding:2px 8px;border-radius:4px;background:rgba(59,130,246,0.08);border:1px solid rgba(59,130,246,0.2);color:#3b82f6;font-family:'JetBrains Mono',monospace;}
.w-sand-code{font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#3b82f6;white-space:pre-wrap;margin:0 0 12px;background:rgba(0,0,0,0.2);padding:14px;border-radius:8px;border:1px solid rgba(255,255,255,0.02);}
.w-sand-term-container{position:relative;background:#02040a;border:1px solid rgba(255,255,255,0.06);border-radius:8px;margin-bottom:16px;box-shadow:inset 0 2px 8px rgba(0,0,0,0.9);overflow:hidden;}
.w-sand-term-bar{background:rgba(255,255,255,0.03);padding:6px 12px;border-bottom:1px solid rgba(255,255,255,0.05);display:flex;justify-content:space-between;align-items:center;}
.w-sand-term-title{font-size:0.65rem;color:#64748b;font-weight:800;letter-spacing:0.06em;font-family:'JetBrains Mono',monospace;}
.w-sand-term-btn{background:rgba(59,130,246,0.1);border:1px solid rgba(59,130,246,0.3);border-radius:4px;color:#3b82f6;font-size:0.68rem;padding:3px 8px;cursor:pointer;font-family:'JetBrains Mono',monospace;font-weight:700;transition:all 0.15s ease;display:flex;align-items:center;gap:4px;}
.w-sand-term-btn:hover{background:#3b82f6;color:#02040a;box-shadow:0 0 8px rgba(59,130,246,0.4);}
.w-sand-term{font-family:'JetBrains Mono',monospace;font-size:0.76rem;color:#a7f3d0;padding:12px 16px;white-space:pre-wrap;min-height:90px;}
.w-sand-term span.prompt{color:#3ddc84;}
.w-sand-term span.cmd{color:#ffffff;font-weight:bold;}
.w-sand-expl{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:16px;font-size:0.83rem;color:#cbd5e1;line-height:1.65;}
.w-sand-expl h5{margin:0 0 8px;font-size:0.85rem;color:#fbbf24;font-weight:bold;}
.w-sand-expl p{margin:0 0 10px;}
</style>
<div class="w-sandbox-main"><div class="w-sandbox-nav"><button id="nav-item-sha256" class="w-nav-item active" onclick="showSandboxItem('sha256', this)">1. SHA-256 Calculate</button><button id="nav-item-hashcat" class="w-nav-item" onclick="showSandboxItem('hashcat', this)">2. Hash Decrack/Brute</button></div><div class="w-sandbox-panels"><div id="panel-sha256" class="w-sand-panel"><div class="w-sand-hdr"><span>1. SHA-256 Digest Generation</span> <span class="tag">SHA-256</span></div><pre class="w-sand-code">echo -n "admin" | sha256sum</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startHashSim('sha256')">▶ Run Simulation</button></div><div id="term-sha256" class="w-sand-term"><span class="prompt">kali$</span> [กดปุ่ม Run Simulation เพื่อทำแฮช]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>คำนวณค่า SHA-256 ส่งผลแฮชขนาดความยาว 64 ตัวอักษรฐาน 16 (256 บิต) ป้องกันการนำกลับมาเดาเป็นข้อความธรรมดาได้แน่นหนา</p></div></div><div id="panel-hashcat" class="w-sand-panel"><div class="w-sand-hdr"><span>2. Hashcat Password Recovery</span> <span class="tag">Hash Cracking</span></div><pre class="w-sand-code">hashcat -m 0 -a 0 21232f297a57a5a743894a0e4a801fc3 rockyou.txt</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startHashSim('hashcat')">▶ Run Simulation</button></div><div id="term-hashcat" class="w-sand-term"><span class="prompt">kali$</span> [กดปุ่ม Run Simulation เพื่อจำลองกู้รหัสผ่าน]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>การกู้แฮช (Cracking) ไม่ใช่การถอดรหัสด้วยสูตรคณิตศาสตร์ แต่เป็นการแฮชคำศัพท์ใน Wordlist แล้วเอามาชนเปรียบเทียบ</p></div></div></div></div>
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
window.startHashSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span class="prompt">kali$</span> <span class="cmd">Processing hash verification...</span>\\n[.] Performing dictionary mapping...';
  setTimeout(() => {
    if (itemKey === 'sha256') {
      term.innerHTML = '<span class="prompt">kali$</span> <span class="cmd">sha256sum:</span>\\n<span style="color:#3b82f6; font-weight:bold;">8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918</span>';
    } else if (itemKey === 'hashcat') {
      term.innerHTML = '<span class="prompt">kali$</span> <span class="cmd">hashcat results:</span>\\n21232f297a57a5a743894a0e4a801fc3:<span style="color:#3ddc84; font-weight:bold;">admin</span>\\n\\n[+] Hash cracked! Key matched wordlist entry.';
    }
  }, 1000);
}
</script>"""

val183_2 = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

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
  background: rgba(59, 130, 246, 0.04);
  border-color: rgba(59, 130, 246, 0.25);
  color: #ffffff;
}
.w-quiz-option.selected {
  background: rgba(59, 130, 246, 0.08);
  border-color: #3b82f6;
  color: #ffffff;
  box-shadow: 0 0 10px rgba(59, 130, 246, 0.2);
  font-weight: 700;
}
.w-quiz-option input[type="radio"] {
  display: none;
}
</style>
<div class="row align-items-center" style="margin:1.5rem auto; max-width:980px;"><div class="col-md-8"><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. คุณสมบัติที่สำคัญที่สุดประการหนึ่งของฟังก์ชันการทำแฮช (Hashing) คือข้อใด?</p><div class="options-container" data-q="q1"><label class="w-quiz-option"><input type="radio" name="hash_prop" value="One-Way" data-hash="23c7f5c90b6b80d90bd93d8435d648b26e03fb21884be5e38f6b864a66e4a2cd">ไม่สามารถกู้ข้อความกลับคืนด้วยสูตรทางตรง (One-Way Function)</label><label class="w-quiz-option"><input type="radio" name="hash_prop" value="Reversible" data-hash="false">ย้อนถอดสูตรง่ายโดยใช้กุญแจลับร่วมกัน (Reversible)</label><label class="w-quiz-option"><input type="radio" name="hash_prop" value="Multi-key" data-hash="false">ต้องใช้คู่คีย์ในการคำนวณตลอดเวลา (Multi-key Access)</label><label class="w-quiz-option"><input type="radio" name="hash_prop" value="Fast" data-hash="false">ต้องปรับความเร็วตามขนาดความจุของไฟล์นำส่ง</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. ค่าแฮชระดับมาตรฐานความปลอดภัยในปัจจุบัน SHA-256 มีขนาดผลลัพธ์สุดท้ายกี่บิต?</p><div class="options-container" data-q="q2"><label class="w-quiz-option"><input type="radio" name="sha_bits" value="256" data-hash="3a95aa975765796245d8b8ff716d0046522bb33f749eb721867c4e515d18d451">256 บิต</label><label class="w-quiz-option"><input type="radio" name="sha_bits" value="128" data-hash="false">128 บิต (MD5)</label><label class="w-quiz-option"><input type="radio" name="sha_bits" value="512" data-hash="false">512 บิต</label><label class="w-quiz-option"><input type="radio" name="sha_bits" value="64" data-hash="false">64 บิต</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div></div><div class="col-md-4 text-center"><div class="p-4" style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); border-radius:12px; min-height:220px; display:flex; flex-direction:column; justify-content:center; align-items:center;"><span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;">Lesson Progress</span><div class="neon-gauge-container"><svg class="neon-gauge" viewBox="0 0 36 36"><path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><path class="neon-gauge-fill" id="lesson-gauge-fill" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text">0%</text></svg></div><span id="lesson-status-txt" class="mt-3 d-block text-muted" style="font-size:0.78rem;">โปรดตอบคำถามให้ครบ 2 ข้อ</span></div></div></div>
<style>
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:#3b82f6; stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease, stroke 0.5s ease; filter:drop-shadow(0 0 5px rgba(59,130,246,0.5));}
.neon-gauge-text {fill:#ffffff; font-family:\'JetBrains Mono\',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}
</style>
<script>
const lessonKey = 'solved_lesson_183';
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

save_lesson(183, val183_0, val183_1, val183_2)

# ─── 4. Lesson 184: Steganography & Crypto Attacks ───
val184_0 = """## 🔑 Steganography & Crypto Attacks (การซ่อนข้อความและการประยุกต์ใช้ในระบบ)
---

ยินดีต้อนรับสู่บทเรียนกระบวนการซ่อนไฟล์หรือข้อความลงในสื่อภาพถ่าย (Steganography) และตรรกะการวิเคราะห์ถอดคีย์การสื่อสาร (Cryptanalysis)

<style>
.w-neon-card {
  background: rgba(6, 8, 20, 0.45) !important;
  border: 1px solid rgba(16, 185, 129, 0.15) !important;
  border-radius: 12px !important;
  padding: 20px !important;
  margin-bottom: 24px !important;
  box-shadow: 0 8px 32px rgba(0,0,0,0.3), inset 0 0 15px rgba(16,185,129,0.02) !important;
}
.w-stego-inline {
  font-family: 'JetBrains Mono', monospace;
  background: rgba(16, 185, 129, 0.08);
  color: #10b981;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 0.72rem;
  font-weight: 700;
}
</style>

### 🖼️ 1. Steganography (ศาสตร์การปกปิดข้อมูล)
การหลีกเลี่ยงความสนใจด้วยการซ่อนตัวไฟล์ข้อมูล คีย์รหัส หรือไฟล์ซิปไว้ภายในไฟล์ที่มีหน้าตาปกติธรรมดา (เช่น ซ่อนในพิกเซลย่อยของภาพ JPEG/PNG):
- 🧬 **LSB (Least Significant Bit)**: เปลี่ยนค่าสีบิตที่ความสำคัญต่ำสุดในภาพเพื่อซ่อนอักษรโดยไม่กระทบต่อความสว่างตาของภาพ
- 📂 **ตัวอย่างคำสั่งยอดฮิต**:
  <div class="w-stego-inline">steghide embed -ef secret.txt -cf cover.jpg</div>

---

### 💥 2. Cryptanalysis (การทุบทำลายรหัสลับ)
- 📊 **Frequency Analysis**: การนับเปรียบเทียบสัดส่วนของตัวอักษรเพื่อวิเคราะห์การแปลงคำสลับภาษาในยุคเก่า
- 💥 **Known Plaintext Attack (KPA)**: นักเจาะรู้ข้อความธรรมดาก่อนหน้าบางส่วนแล้วเอามาแมปหาคีย์ลับตัวหลัก"""

val184_1 = """### 💻 Steganography Sandbox (จำลองระบบสกัดซ่อนไฟล์ลับ)

คลิกหัวข้อด้านซ้ายมือเพื่อจำลอง และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลการสลักข้อมูล:

<style>
.w-sandbox-main{display:flex;gap:20px;margin:2rem auto;max-width:1050px;}
@media(max-width:820px){.w-sandbox-main{flex-direction:column;}}
.w-sandbox-nav{width:220px;display:flex;flex-direction:column;gap:6px;flex-shrink:0;}
@media(max-width:820px){.w-sandbox-nav{width:100%;flex-direction:row;flex-wrap:wrap;}}
.w-nav-item{padding:8px 12px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.04);border-radius:6px;font-size:0.75rem;color:#cbd5e1;cursor:pointer;text-align:left;transition:all 0.15s ease;}
.w-nav-item:hover, .w-nav-item.active{border-color:#10b981;color:#ffffff;background:rgba(16,185,129,0.04);}
.w-nav-item.active{font-weight:bold;box-shadow:0 0 8px rgba(16,185,129,0.15);}
.w-sandbox-panels{flex:1;display:flex;flex-direction:column;gap:14px;}
.w-sand-panel{display:none;background:#05070f;border:1px solid rgba(255, 255, 255, 0.08);border-radius:10px;padding:20px;box-shadow:0 8px 24px rgba(0,0,0,0.45);box-sizing:border-box;}
.w-sand-panel.active{display:block !important;}
.w-sand-hdr{font-size:0.95rem;font-weight:800;color:#ffffff;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:10px;margin-bottom:14px;display:flex;justify-content:between;align-items:center;}
.w-sand-hdr span.tag{font-size:0.65rem;padding:2px 8px;border-radius:4px;background:rgba(16,185,129,0.08);border:1px solid rgba(16,185,129,0.2);color:#10b981;font-family:'JetBrains Mono',monospace;}
.w-sand-code{font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#10b981;white-space:pre-wrap;margin:0 0 12px;background:rgba(0,0,0,0.2);padding:14px;border-radius:8px;border:1px solid rgba(255,255,255,0.02);}
.w-sand-term-container{position:relative;background:#02040a;border:1px solid rgba(255,255,255,0.06);border-radius:8px;margin-bottom:16px;box-shadow:inset 0 2px 8px rgba(0,0,0,0.9);overflow:hidden;}
.w-sand-term-bar{background:rgba(255,255,255,0.03);padding:6px 12px;border-bottom:1px solid rgba(255,255,255,0.05);display:flex;justify-content:space-between;align-items:center;}
.w-sand-term-title{font-size:0.65rem;color:#64748b;font-weight:800;letter-spacing:0.06em;font-family:'JetBrains Mono',monospace;}
.w-sand-term-btn{background:rgba(16,185,129,0.1);border:1px solid rgba(16,185,129,0.3);border-radius:4px;color:#10b981;font-size:0.68rem;padding:3px 8px;cursor:pointer;font-family:'JetBrains Mono',monospace;font-weight:700;transition:all 0.15s ease;display:flex;align-items:center;gap:4px;}
.w-sand-term-btn:hover{background:#10b981;color:#02040a;box-shadow:0 0 8px rgba(16,185,129,0.4);}
.w-sand-term{font-family:'JetBrains Mono',monospace;font-size:0.76rem;color:#a7f3d0;padding:12px 16px;white-space:pre-wrap;min-height:90px;}
.w-sand-term span.prompt{color:#3ddc84;}
.w-sand-term span.cmd{color:#ffffff;font-weight:bold;}
.w-sand-expl{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:16px;font-size:0.83rem;color:#cbd5e1;line-height:1.65;}
.w-sand-expl h5{margin:0 0 8px;font-size:0.85rem;color:#fbbf24;font-weight:bold;}
.w-sand-expl p{margin:0 0 10px;}
</style>
<div class="w-sandbox-main"><div class="w-sandbox-nav"><button id="nav-item-stego" class="w-nav-item active" onclick="showSandboxItem('stego', this)">1. Steghide Embed</button><button id="nav-item-extract" class="w-nav-item" onclick="showSandboxItem('extract', this)">2. Steghide Extract</button></div><div class="w-sandbox-panels"><div id="panel-stego" class="w-sand-panel"><div class="w-sand-hdr"><span>1. Embedding Secret into Cover Image</span> <span class="tag">Steghide Embed</span></div><pre class="w-sand-code">steghide embed -ef flag.txt -cf photo.jpg -p secretkey</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startStegSim('stego')">▶ Run Simulation</button></div><div id="term-stego" class="w-sand-term"><span class="prompt">stego-cli$</span> [กดปุ่ม Run Simulation เพื่อจำลองการซ่อนไฟล์]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>ซ่อนไฟล์ธงข้อความ `flag.txt` แฝงเข้าไปในรูปถ่าย `photo.jpg` แบบใช้รหัสลับล็อกข้อมูลบิตสี</p></div></div><div id="panel-extract" class="w-sand-panel"><div class="w-sand-hdr"><span>2. Extracting Secret from Stego Image</span> <span class="tag">Steghide Extract</span></div><pre class="w-sand-code">steghide extract -sf photo.jpg -p secretkey</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startStegSim('extract')">▶ Run Simulation</button></div><div id="term-extract" class="w-sand-term"><span class="prompt">stego-cli$</span> [กดปุ่ม Run Simulation เพื่อกู้ข้อความลับ]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>สกัดสืบเสาะหาไฟล์ลับขากลับจากพิกเซลรูปถ่ายโดยนำคีย์ตัวรหัสผ่าน `secretkey` มาป้อนเพื่อถอดรหัสบิต</p></div></div></div></div>
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
window.startStegSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span class="prompt">stego-cli$</span> <span class="cmd">Scanning pixel arrays...</span>\\n[.] Accessing Least Significant Bits...';
  setTimeout(() => {
    if (itemKey === 'stego') {
      term.innerHTML = '<span class="prompt">stego-cli$</span> <span class="cmd">steghide results:</span>\\nembedding "flag.txt" in "photo.jpg"... done\\n\\n[+] Steganography embedding succeeded!';
    } else if (itemKey === 'extract') {
      term.innerHTML = '<span class="prompt">stego-cli$</span> <span class="cmd">steghide extract...</span>\\nwrote extracted data to "flag.txt"\\n\\n[+] flag.txt content: <span style="color:#10b981; font-weight:bold;">FLAG{stego_pixels_decoded}</span>';
    }
  }, 1000);
}
</script>"""

val184_2 = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

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
  background: rgba(16, 185, 129, 0.04);
  border-color: rgba(16, 185, 129, 0.25);
  color: #ffffff;
}
.w-quiz-option.selected {
  background: rgba(16, 185, 129, 0.08);
  border-color: #10b981;
  color: #ffffff;
  box-shadow: 0 0 10px rgba(16, 185, 129, 0.2);
  font-weight: 700;
}
.w-quiz-option input[type="radio"] {
  display: none;
}
</style>
<div class="row align-items-center" style="margin:1.5rem auto; max-width:980px;"><div class="col-md-8"><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. ศาสตร์ในการปกปิดข้อความความลับ เพื่อซ่อนตัวตนข้อมูลแฝงในไฟล์สื่อปกติ (เช่น แฝงในพิกเซลรูปถ่าย) เรียกว่าอะไร?</p><div class="options-container" data-q="q1"><label class="w-quiz-option"><input type="radio" name="stego_q" value="Steganography" data-hash="277bc1b69ad3178c775080e7221f75355694a08ba1c38fa8b79f38ebcb5c8a41">การซ่อนข้อความ (Steganography)</label><label class="w-quiz-option"><input type="radio" name="stego_q" value="Cryptography" data-hash="false">วิทยาการรหัสลับ (Cryptography)</label><label class="w-quiz-option"><input type="radio" name="stego_q" value="Encoding" data-hash="false">การแปลงรหัส (Encoding)</label><label class="w-quiz-option"><input type="radio" name="stego_q" value="Hashing" data-hash="false">การทำแฮช (Hashing)</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. การวิเคราะห์ความถี่ของตัวอักษร (Frequency Analysis) เพื่อสลายระบบการเข้ารหัส เหมาะใช้สอยถอดรหัสลับยุคโบราณข้อใด?</p><div class="options-container" data-q="q2"><label class="w-quiz-option"><input type="radio" name="cipher_q" value="Substitution" data-hash="c9b7f5256e2978000bd93d8435d648b26e03fb21884be5e38f6b864a66e4a2cd">Monoalphabetic Substitution Cipher</label><label class="w-quiz-option"><input type="radio" name="cipher_q" value="AES" data-hash="false">AES-256 Block Cipher</label><label class="w-quiz-option"><input type="radio" name="cipher_q" value="RSA" data-hash="false">RSA Key Exchange algorithm</label><label class="w-quiz-option"><input type="radio" name="cipher_q" value="OTP" data-hash="false">One-Time Pad encryption</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div></div><div class="col-md-4 text-center"><div class="p-4" style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); border-radius:12px; min-height:220px; display:flex; flex-direction:column; justify-content:center; align-items:center;"><span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;">Lesson Progress</span><div class="neon-gauge-container"><svg class="neon-gauge" viewBox="0 0 36 36"><path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><path class="neon-gauge-fill" id="lesson-gauge-fill" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text">0%</text></svg></div><span id="lesson-status-txt" class="mt-3 d-block text-muted" style="font-size:0.78rem;">โปรดตอบคำถามให้ครบ 2 ข้อ</span></div></div></div>
<style>
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:#10b981; stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease, stroke 0.5s ease; filter:drop-shadow(0 0 5px rgba(16,185,129,0.5));}
.neon-gauge-text {fill:#ffffff; font-family:\'JetBrains Mono\',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}
</style>
<script>
const lessonKey = 'solved_lesson_184';
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

save_lesson(184, val184_0, val184_1, val184_2)
ctx.pop()
