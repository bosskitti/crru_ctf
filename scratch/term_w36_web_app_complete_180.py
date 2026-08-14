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

# ─── Lesson 180: CMS Exploitation & Vulnerability Audit ───
val180_0 = """## 🛡️ CMS Exploitation & Vulnerability Audit (การป้องกันและการทดสอบความปลอดภัยเว็บ)
---

ยินดีต้อนรับสู่บทเรียนการตรวจสอบความมั่นคงปลอดภัยและความเปราะบางของระบบจัดการเนื้อหาเว็บไซต์สำเร็จรูป (CMS)

### 📄 SLIDE 151-155: CMS Exploitation Overviews (ภาพรวมความเสี่ยงของเว็บสำเร็จรูป)
- **Content Management System (CMS)**: ระบบจัดการสารสนเทศและเนื้อหาเว็บสำเร็จรูปยอดฮิต เช่น WordPress, Joomla, Drupal และ Magento ซึ่งมักตกเป็นเป้าการเจาะระบบเพื่อดึงข้อมูลลับ ขโมยสิทธิ์ หรือลอบฝังคำสั่งประหาร (RCE)
- **อัตราครองส่วนแบ่งตลาดของระบบ CMS (สถิติล่าสุด)**:
  - **WordPress**: 62.7% (เป้าโจมตีอันดับหนึ่ง)
  - **Shopify**: 6.4%
  - **Wix**: 3.9%
  - **Squarespace**: 3.0%
  - **Joomla**: 2.4%
  - **Drupal**: 1.3%
- **โปรแกรมสแกนความมั่นคง CMS ที่ได้รับความนิยม**:
  - **WPScan**: เจาะจงสแกนช่องโหว่ WordPress (ใช้งานง่าย มีฐานข้อมูลปลั๊กอินช่องโหว่ขนาดใหญ่)
  - **JoomScan**: เจาะจงหาจุดอ่อนและค่าคอนฟิกผิดพลาดของระบบ Joomla
  - **Droopescan**: ตรวจสอบหาจุดอ่อนระบบ Drupal และ SilverStripe
  - **CMSeek**: โปรแกรมตรวจจับระบุแบรนด์ CMS อัตโนมัติและช่วยชี้เป้าช่องโหว่เบื้องต้น

---

### 📄 SLIDE 156-163: การทดสอบเจาะระบบ WordPress ด้วย WPScan
- **WPScan**: เป็นตัวสแกนความปลอดภัยเฉพาะด้านสัจจะ WordPress รันผ่าน CLI บนเครื่อง Kali Linux
- **ตัวเลือกคำสั่งดึงพารามิเตอร์ระบบ (--enumerate)**:
  - `--enumerate v` (ดึงข้อมูลเวอร์ชันหลักและช่องโหว่)
  - `--enumerate p` (ดึงรายชื่อปลั๊กอินทั้งหมด)
  - `--enumerate vp` (เจาะจงดึงเฉพาะปลั๊กอินที่มีช่องโหว่ความเสี่ยง)
  - `--enumerate vt` (ดึงเฉพาะธีมที่มีช่องโหว่)
  - `--enumerate u` (ดึงรายชื่อผู้ใช้งานเพื่อนำไป brute force)
  - `--enumerate cb` (ค้นหาไฟล์แบ็คอัปโครงสร้าง config)
- **ตัวอย่างการใช้คำสั่ง**:
  - สแกนเพื่อหาปลั๊กอินเปราะบาง:
    ```bash
    wpscan --url https://example.com --enumerate vp
    ```
  - สั่งทดสอบการเดารหัสผ่านล็อกอินแอดมิน:
    ```bash
    wpscan --url https://example.com --passwords rockyou.txt --usernames admin
    ```

---

### 📄 SLIDE 164-168: Joomla Exploitation ด้วย JoomScan
- **JoomScan**: พัฒนาขึ้นโดย OWASP เพื่อใช้วิเคราะห์เว็บระบบ Joomla
- **ชุดคำสั่งสำคัญ**:
  - `joomscan -u https://example.com` (สแกนระบบพื้นฐานหาจุดอ่อน)
  - `joomscan -u https://example.com --joomla-version` (ตรวจสอบสืบหาเวอร์ชันติดตั้งหลัก)
  - `joomscan -u https://example.com --components` (ค้นหาคอมโพเนนต์และปลั๊กอินเสริมที่มีช่องโหว่)
  - `joomscan -u https://example.com --enumerate-users` (ดึงรายชื่อผู้ใช้งานระบบ)

---

### 📄 SLIDE 169-191: ตัวอย่างกรณีศึกษาโจมตี CMS
- **Brute Force**: การสุ่มเดารหัสผ่านหน้าเว็บบอร์ดแผงควบคุม (เช่น `/wp-login.php` หรือ `/administrator/`) จนกว่าจะสามารถเข้าควบคุมสิทธิ์
- **Vulnerable Plugin**: การใช้ประโยชน์จากปลั๊กอินเสริมหรือธีมตกรุ่นที่มีสิทธิ์เขียนสไลด์ หรืออัปโหลดไฟล์ เช่น ปลั๊กอินแกลเลอรีภาพถ่าย ปล่อยให้แฮกเกอร์ลอบส่ง Web shell นามสกุล `.php` เข้ามาทับสิทธิ์ควบคุมเซิร์ฟเวอร์หลังบ้าน"""

val180_1 = """### 💻 CMS Security Audit Sandbox (จำลองเรียกสแกนความปลอดภัย CMS)

คลิกหัวข้อด้านซ้ายมือเพื่อศึกษาขั้นตอน และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลการสแกนความเปราะบาง:

<div class="w-sandbox-main" style="display: flex; gap: 20px; margin: 1.5rem auto; max-width: 1000px;">
  <div class="w-sandbox-nav" style="width: 220px; display: flex; flex-direction: column; gap: 8px; flex-shrink: 0;">
    <button id="nav-item-wpscan" class="w-nav-item active" style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 6px; padding: 10px 14px; color: #cbd5e1; text-align: left; cursor: pointer; font-size: 0.78rem; transition: all 0.2s;" onclick="showSandboxItem('wpscan', this)">1. WPScan Vulnerability</button>
    <button id="nav-item-joomscan" class="w-nav-item" style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 6px; padding: 10px 14px; color: #cbd5e1; text-align: left; cursor: pointer; font-size: 0.78rem; transition: all 0.2s;" onclick="showSandboxItem('joomscan', this)">2. JoomScan Audit</button>
  </div>
  <div class="w-sandbox-panels" style="flex-grow: 1; display: flex; flex-direction: column; gap: 14px;">
    <!-- WPSCAN PANEL -->
    <div id="panel-wpscan" class="w-sand-panel active" style="background: #05070f; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 10px; padding: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.45);">
      <div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
        <span>1. Scanning WordPress Vulnerabilities with WPScan</span>
        <span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.2); color: #10b981; font-family: monospace;">WPScan Tool</span>
      </div>
      <pre style="font-family: monospace; font-size: 0.8rem; color: #10b981; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">wpscan --url http://ctf.rpca.ac.th/wp/ --enumerate vp,u</pre>
      <div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
        <div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
          <button style="background: rgba(16,185,129,0.1); border: 1px solid rgba(16,185,129,0.3); border-radius: 4px; color: #10b981; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700; transition: all 0.15s;" onclick="startWebSim('wpscan')">▶ Run Simulation</button>
        </div>
        <div id="term-wpscan" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 90px;">
          <span style="color: #3ddc84;">kali$</span> [กดปุ่ม Run Simulation เพื่อยิงสแกน WPScan]
        </div>
      </div>
      <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 16px; font-size: 0.83rem; color: #cbd5e1; line-height: 1.65;">
        <h5 style="margin: 0 0 8px; font-size: 0.85rem; color: #fbbf24; font-weight: bold;">⚙️ Command Description</h5>
        <p style="margin: 0;">คำสั่งค้นหาระบุปลั๊กอินที่มีช่องโหว่ความเสี่ยง (`vp`) และตรวจสอบรายชื่อผู้ใช้งาน (`u`) เพื่อวางสเปกประเมินความปลอดภัย</p>
      </div>
    </div>
    
    <!-- JOOMSCAN PANEL -->
    <div id="panel-joomscan" class="w-sand-panel" style="background: #05070f; border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 10px; padding: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.45); display: none;">
      <div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
        <span>2. Assessing Joomla Website Security with JoomScan</span>
        <span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.2); color: #10b981; font-family: monospace;">JoomScan Tool</span>
      </div>
      <pre style="font-family: monospace; font-size: 0.8rem; color: #10b981; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">joomscan -u http://ctf.rpca.ac.th/joomla/ --components</pre>
      <div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
        <div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
          <button style="background: rgba(16,185,129,0.1); border: 1px solid rgba(16,185,129,0.3); border-radius: 4px; color: #10b981; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700; transition: all 0.15s;" onclick="startWebSim('joomscan')">▶ Run Simulation</button>
        </div>
        <div id="term-joomscan" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 90px;">
          <span style="color: #3ddc84;">kali$</span> [กดปุ่ม Run Simulation เพื่อเริ่มทำ JoomScan]
        </div>
      </div>
      <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 16px; font-size: 0.83rem; color: #cbd5e1; line-height: 1.65;">
        <h5 style="margin: 0 0 8px; font-size: 0.85rem; color: #fbbf24; font-weight: bold;">⚙️ Command Description</h5>
        <p style="margin: 0;">เมธอดตรวจสอบส่วนประกอบเสริม Joomla (components) เพื่อสืบค้นจุดรั่วไหลของซอร์สโค้ดและไลบรารีส่วนตัว</p>
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
  element.style.borderColor = '#10b981';
  element.style.color = '#ffffff';
  element.style.background = 'rgba(16, 185, 129, 0.05)';
  
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
  term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#ffffff; font-weight:bold;">Running CMS mapping audits...</span>\\n[.] Executing target scanner engines...';
  setTimeout(() => {
    if (itemKey === 'wpscan') {
      term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#3ddc84; font-weight:bold;">WPScan Output:</span>\\nWordPress version: 6.2.2 (Outdated)\\nFOUND User: admin (ID: 1)\\nFOUND Vulnerable Plugin: contact-form-7 v5.7.1 (XSS vulnerable)\\n\\n[+] WPScan Completed!';
    } else if (itemKey === 'joomscan') {
      term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#3ddc84; font-weight:bold;">OWASP Joomla! Vulnerability Scanner:</span>\\nJoomla! version: 3.9.22 (Outdated)\\nFOUND: http://ctf.rpca.ac.th/joomla/configuration.php-bak (CODE: 200)\\n\\n[+] JoomScan completed successfully.';
    }
  }, 1000);
}
</script>"""

val180_2 = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการบันทึกความสำเร็จและปลดล็อกปุ่มบทเรียนถัดไป:

<div class="row align-items-center" style="margin:1.5rem auto; max-width:980px;"><div class="col-md-8"><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. ส่วนหัว (Header) ความปลอดภัยใดใน HTTP Response ที่ใช้ป้องกันหน้าเว็บไม่ให้ถูกนำไปฝังใน Iframe เพื่อเลี่ยงช่องโหว่ Clickjacking?</p><div class="options-container" data-q="q1"><label class="w-quiz-option"><input type="radio" name="xframe_h" value="X-Frame-Options" data-hash="c9b7f5256e2978000bd93d8435d648b26e03fb21884be5e38f6b864a66e4a2cd">X-Frame-Options</label><label class="w-quiz-option"><input type="radio" name="xframe_h" value="CSP" data-hash="false">Content-Security-Policy</label><label class="w-quiz-option"><input type="radio" name="xframe_h" value="HSTS" data-hash="false">Strict-Transport-Security</label><label class="w-quiz-option"><input type="radio" name="xframe_h" value="XXSS" data-hash="false">X-XSS-Protection</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. หลักปฏิบัติเพื่อความปลอดภัยในการป้องกันการแทรกโค้ดทำลายระบบเครือข่ายฐานข้อมูล (Injection) ทุกประเภทคือข้อใด?</p><div class="options-container" data-q="q2"><label class="w-quiz-option"><input type="radio" name="sec_coding" value="Input Validation" data-hash="277bc1b69ad3178c775080e7221f75355694a08ba1c38fa8b79f38ebcb5c8a41">การกรองตรวจสอบความถูกต้องข้อมูลนำเข้า (Input Validation)</label><label class="w-quiz-option"><input type="radio" name="sec_coding" value="Encryption" data-hash="false">การเข้ารหัสฐานข้อมูล (Database Encryption)</label><label class="w-quiz-option"><input type="radio" name="sec_coding" value="Backup" data-hash="false">การสำรองไฟล์ข้อมูลประจำวัน (Daily Backup)</label><label class="w-quiz-option"><input type="radio" name="sec_coding" value="IDS" data-hash="false">การติดตั้งระบบแจ้งเตือนแฮกเกอร์ (Intrusion Detection)</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div></div><div class="col-md-4 text-center"><div class="p-4" style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); border-radius:12px; min-height:220px; display:flex; flex-direction:column; justify-content:center; align-items:center;"><span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;">Lesson Progress</span><div class="neon-gauge-container"><svg class="neon-gauge" viewBox="0 0 36 36"><path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><path class="neon-gauge-fill" id="lesson-gauge-fill" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text">0%</text></svg></div><span id="lesson-status-txt" class="mt-3 d-block text-muted" style="font-size:0.78rem;">โปรดตอบคำถามให้ครบ 2 ข้อ</span></div></div></div>
<style>
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:#10b981; stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease, stroke 0.5s ease; filter:drop-shadow(0 0 5px rgba(16,185,129,0.5));}
.neon-gauge-text {fill:#ffffff; font-family:\'JetBrains Mono\',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}
</style>
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
