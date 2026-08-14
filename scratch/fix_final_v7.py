"""
FINAL FIX: Restore lesson 177-180 sandbox & quiz blocks to match the working
pattern from Chapter 4 (lessons 169-176):

Key changes:
1. RESTORE onclick on nav buttons and Run Simulation buttons
2. Use window.xxx global functions (same as Chapter 4)
3. For quiz blocks: use UNIQUE function/variable names per lesson to avoid
   const redeclaration errors (the REAL root cause)
4. NO IIFE wrapping (Chapter 4 doesn't use it and works fine)
"""
import json, re, sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app

app = create_app()

###############################################################################
# LESSON 177 SANDBOX (Block 1) - HTTP Headers Diagnostic
###############################################################################
SANDBOX_177 = r"""### 💻 HTTP Headers Diagnostic Sandbox (จำลองวิเคราะห์โครงสร้างข้อมูลเว็บ)

คลิกหัวข้อด้านซ้ายมือเพื่อจำลองวิเคราะห์โครงสร้าง และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อตรวจสอบทราฟฟิกข้อมูล:

<style type="text/css">
.w-sandbox-main { display: flex !important; gap: 20px !important; margin: 1.5rem auto !important; max-width: 1000px !important; }
.w-sandbox-nav { width: 220px !important; display: flex !important; flex-direction: column !important; gap: 8px !important; flex-shrink: 0 !important; }
.w-nav-item { background: rgba(255, 255, 255, 0.02) !important; border: 1px solid rgba(255, 255, 255, 0.06) !important; border-radius: 6px !important; padding: 10px 14px !important; color: #cbd5e1 !important; text-align: left !important; cursor: pointer !important; font-size: 0.78rem !important; transition: all 0.2s !important; }
.w-nav-item:hover, .w-nav-item.active { border-color: #00f0ff !important; color: #ffffff !important; background: rgba(0, 240, 255, 0.05) !important; }
.w-nav-item.active { font-weight: 700 !important; box-shadow: 0 0 8px rgba(0, 240, 255, 0.15) !important; }
.w-sandbox-panels { flex-grow: 1 !important; }
.w-sand-panel { background: #05070f !important; border: 1px solid rgba(255, 255, 255, 0.08) !important; border-radius: 10px !important; padding: 20px !important; box-shadow: 0 8px 24px rgba(0,0,0,0.45) !important; }
</style>
<div class="w-sandbox-main">
<div class="w-sandbox-nav">
<button id="nav-item-httpget" class="w-nav-item active" onclick="showSandboxItem('httpget', this)">1. Send HTTP GET</button>
<button id="nav-item-httppost" class="w-nav-item" onclick="showSandboxItem('httppost', this)">2. Send HTTP POST</button>
</div>
<div class="w-sandbox-panels">
<div id="panel-httpget" class="w-sand-panel" style="display: block;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>1. HTTP GET Request Method</span>
<span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(0,240,255,0.08); border: 1px solid rgba(0,240,255,0.2); color: #00f0ff; font-family: monospace;">HTTP Client</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #00f0ff; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">GET /index.php HTTP/1.1
Host: ctf.rpca.ac.th
User-Agent: Mozilla/5.0
Accept: text/html
Cookie: session_id=abc123xyz</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startPostSim('httpget')" style="background: rgba(0,240,255,0.1); border: 1px solid rgba(0,240,255,0.3); border-radius: 4px; color: #00f0ff; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700;">▶ Run Simulation</button>
</div>
<div id="term-httpget" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 90px;">
<span style="color: #3ddc84;">client$</span> [กดปุ่ม Run Simulation เพื่อส่ง Request]
</div>
</div>
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 16px; font-size: 0.83rem; color: #cbd5e1; line-height: 1.65;">
<h5 style="margin: 0 0 8px; font-size: 0.85rem; color: #fbbf24; font-weight: bold;">⚙️ Command Description</h5>
<p style="margin: 0;">เมธอด GET ใช้เพื่อดึงหน้าเพจขึ้นมาแสดงผล โดยบราวเซอร์ส่ง Cookie ยืนยันสิทธิ์เซสชันแอดมิน</p>
</div>
</div>
<div id="panel-httppost" class="w-sand-panel" style="display: none;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>2. HTTP POST Request Method</span>
<span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(0,240,255,0.08); border: 1px solid rgba(0,240,255,0.2); color: #00f0ff; font-family: monospace;">HTTP Client</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #00f0ff; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">POST /login.php HTTP/1.1
Host: ctf.rpca.ac.th
Content-Type: application/x-www-form-urlencoded
Content-Length: 29

username=admin&password=secret</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startPostSim('httppost')" style="background: rgba(0,240,255,0.1); border: 1px solid rgba(0,240,255,0.3); border-radius: 4px; color: #00f0ff; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700;">▶ Run Simulation</button>
</div>
<div id="term-httppost" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 90px;">
<span style="color: #3ddc84;">client$</span> [กดปุ่ม Run Simulation เพื่อส่ง Request]
</div>
</div>
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 16px; font-size: 0.83rem; color: #cbd5e1; line-height: 1.65;">
<h5 style="margin: 0 0 8px; font-size: 0.85rem; color: #fbbf24; font-weight: bold;">⚙️ Command Description</h5>
<p style="margin: 0;">เมธอด POST ใช้เพื่อส่งข้อมูลชุดใหญ่ที่เป็นความลับ (เช่น รหัสผ่าน) ไปประมวลผลบนเซิร์ฟเวอร์โดยไม่โชว์บน URL</p>
</div>
</div>
</div>
</div>
<script>
window.showSandboxItem = function(itemKey, element) {
  var items = document.querySelectorAll('.w-sandbox-nav .w-nav-item');
  items.forEach(function(i) { i.classList.remove('active'); });
  element.classList.add('active');
  var panels = document.querySelectorAll('.w-sand-panel');
  panels.forEach(function(p) { p.style.setProperty('display', 'none', 'important'); });
  var targetPanel = document.getElementById('panel-' + itemKey);
  if (targetPanel) { targetPanel.style.setProperty('display', 'block', 'important'); }
}
window.startPostSim = function(itemKey) {
  var term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span style="color:#64748b;">client$</span> <span style="color:#ffffff; font-weight:bold;">Sending HTTP Request...</span>\n[.] Accessing remote port 80/443\n[.] Reading Response Headers...';
  setTimeout(function() {
    if (itemKey === 'httpget') {
      term.innerHTML = '<span style="color:#64748b;">client$</span> <span style="color:#3ddc84; font-weight:bold;">HTTP/1.1 200 OK</span>\nServer: Apache/2.4.41 (Ubuntu)\nContent-Type: text/html\nContent-Length: 1042\n\n&lt;html&gt;&lt;body&gt;&lt;h1&gt;Welcome to RPCA Cyber Club&lt;/h1&gt;&lt;/body&gt;&lt;/html&gt;';
    } else if (itemKey === 'httppost') {
      term.innerHTML = '<span style="color:#64748b;">client$</span> <span style="color:#fbbf24; font-weight:bold;">HTTP/1.1 302 Found</span>\nServer: Apache/2.4.41 (Ubuntu)\nLocation: /dashboard.php\nSet-Cookie: session_id=abc123xyz; Path=/; HttpOnly\n\n[+] Redirecting to dashboard...';
    }
  }, 1000);
}
setTimeout(function() {
  var activeBtn = document.querySelector('.w-sandbox-nav .w-nav-item.active');
  if (activeBtn) { activeBtn.click(); }
}, 100);
</script>"""

###############################################################################
# LESSON 177 QUIZ (Block 2) - unique names: lessonKey177, getSavedSolves177, etc.
###############################################################################
QUIZ_177 = r"""### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการบันทึกความสำเร็จและปลดล็อกปุ่มบทเรียนถัดไป:

<div class="row align-items-center" style="margin:1.5rem auto; max-width:980px;"><div class="col-md-8"><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. พอร์ตบริการเครือข่ายมาตรฐานสำหรับการเข้าถึงหน้าเว็บเพจแบบเข้ารหัสปลอดภัย (HTTPS) คือพอร์ตใด?</p><div class="options-container" data-q="q1"><label class="w-quiz-option"><input type="radio" name="web_port" value="80" data-hash="false">Port 80</label><label class="w-quiz-option"><input type="radio" name="web_port" value="443" data-hash="868846c4f8d48e0259b38466e3fb0c4b26090cfa4b6f1f457788be4fbf0fa8fb">Port 443 (HTTPS)</label><label class="w-quiz-option"><input type="radio" name="web_port" value="22" data-hash="false">Port 22</label><label class="w-quiz-option"><input type="radio" name="web_port" value="8080" data-hash="false">Port 8080</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. โครงการมาตรฐานสากลด้านความปลอดภัยเว็บที่จัดอันดับ 10 ความเสี่ยงสูงสุดของเว็บแอปพลิเคชันคือองค์กรใด?</p><div class="options-container" data-q="q2"><label class="w-quiz-option"><input type="radio" name="owasp_q" value="W3C" data-hash="false">W3C</label><label class="w-quiz-option"><input type="radio" name="owasp_q" value="OWASP" data-hash="3367b846e49226cb100416972049d5bf59892cfa76e4a2cdbbf24c56e2978000">OWASP</label><label class="w-quiz-option"><input type="radio" name="owasp_q" value="SANS" data-hash="false">SANS Institute</label><label class="w-quiz-option"><input type="radio" name="owasp_q" value="MITRE" data-hash="false">MITRE Corporation</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div></div><div class="col-md-4 text-center"><div class="p-4" style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); border-radius:12px; min-height:220px; display:flex; flex-direction:column; justify-content:center; align-items:center;"><span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;">Lesson Progress</span><div class="neon-gauge-container"><svg class="neon-gauge" viewBox="0 0 36 36"><path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><path class="neon-gauge-fill" id="lesson-gauge-fill" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text">0%</text></svg></div><span id="lesson-status-txt" class="mt-3 d-block text-muted" style="font-size:0.78rem;">โปรดตอบคำถามให้ครบ 2 ข้อ</span></div></div></div>
<style>
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:#00f0ff; stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease, stroke 0.5s ease; filter:drop-shadow(0 0 5px rgba(0,240,255,0.5));}
.neon-gauge-text {fill:#ffffff; font-family:'JetBrains Mono',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}
</style>
<script>
var lessonKey177 = 'solved_lesson_177';
function getSavedSolves177() { try { return JSON.parse(localStorage.getItem(lessonKey177) || '[]'); } catch(e) { return []; } }
function updateLocalProgress177() {
  var solved = getSavedSolves177();
  var total = 2;
  var percent = Math.round((solved.length / total) * 100);
  var fill = document.getElementById('lesson-gauge-fill');
  var text = document.getElementById('lesson-gauge-text');
  var status = document.getElementById('lesson-status-txt');
  if (fill) fill.setAttribute('stroke-dasharray', percent + ', 100');
  if (text) text.textContent = percent + '%';
  if (solved.length === total) {
    if (fill) fill.style.stroke = '#3ddc84';
    if (status) status.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
  } else {
    if (fill) fill.style.stroke = '#00f0ff';
    if (status) status.textContent = 'ทำเสร็จแล้ว ' + solved.length + '/' + total + ' ข้อ';
  }
}
document.addEventListener('click', function(e) {
  var label = e.target.closest('.w-quiz-option');
  if (label) {
    var container = label.closest('.options-container');
    if (container) {
      container.querySelectorAll('.w-quiz-option').forEach(function(opt) { opt.classList.remove('selected'); });
      label.classList.add('selected');
      var radio = label.querySelector('input[type="radio"]');
      if (radio) radio.checked = true;
    }
  }
});
window.verifyMultipleChoice = function(button) {
  var cell = button.closest('.question-cell');
  var selectedRadio = cell.querySelector('input[type="radio"]:checked');
  var feedback = cell.querySelector('.feedback-msg');
  if (!selectedRadio) {
    feedback.className = "feedback-msg mt-2 alert-warning py-1.5 px-3 text-dark";
    feedback.innerHTML = '<i class="fas fa-exclamation-triangle mr-1"></i> กรุณาเลือกคำตอบ';
    feedback.style.setProperty('display', 'block', 'important');
    return;
  }
  var hashVal = selectedRadio.getAttribute('data-hash');
  if (hashVal !== 'false') {
    feedback.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
    feedback.innerHTML = '<i class="fas fa-check-circle mr-1"></i> คำตอบถูกต้อง!';
    feedback.style.setProperty('display', 'block', 'important');
    cell.querySelectorAll('input[type="radio"]').forEach(function(r) { r.disabled = true; });
    cell.querySelectorAll('.w-quiz-option').forEach(function(opt) { opt.style.pointerEvents = 'none'; });
    button.disabled = true;
    var solved = getSavedSolves177();
    if (solved.indexOf(hashVal) === -1) {
      solved.push(hashVal);
      localStorage.setItem(lessonKey177, JSON.stringify(solved));
    }
    updateLocalProgress177();
  } else {
    feedback.className = "feedback-msg mt-2 alert-danger py-1.5 px-3 text-white bg-danger border-0";
    feedback.innerHTML = '<i class="fas fa-times-circle mr-1"></i> คำตอบไม่ถูกต้อง ลองใหม่!';
    feedback.style.setProperty('display', 'block', 'important');
  }
}
setTimeout(function() {
  var solved = getSavedSolves177();
  document.querySelectorAll('.options-container').forEach(function(container) {
    container.querySelectorAll('input[type="radio"]').forEach(function(radio) {
      var hash = radio.getAttribute('data-hash');
      if (solved.indexOf(hash) !== -1) {
        radio.checked = true;
        var label = radio.closest('.w-quiz-option');
        if (label) label.classList.add('selected');
        container.querySelectorAll('input[type="radio"]').forEach(function(r) { r.disabled = true; });
        container.querySelectorAll('.w-quiz-option').forEach(function(opt) { opt.style.pointerEvents = 'none'; });
        var cell = container.closest('.question-cell');
        if (cell) {
          var btn = cell.querySelector('button');
          if (btn) btn.disabled = true;
          var fb = cell.querySelector('.feedback-msg');
          if (fb) {
            fb.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
            fb.innerHTML = '<i class="fas fa-check-circle mr-1"></i> เรียบร้อยแล้ว';
            fb.style.setProperty('display', 'block', 'important');
          }
        }
      }
    });
  });
  updateLocalProgress177();
}, 200);
</script>"""

###############################################################################
# LESSON 178 SANDBOX (Block 1) - Directory & HTTP Diagnostic
###############################################################################
SANDBOX_178 = r"""### 💻 Directory & HTTP Diagnostic Sandbox (จำลองค้นหาไฟล์และยิงคำสั่ง)

คลิกหัวข้อด้านซ้ายมือเพื่อศึกษาตัวอย่างการทำแล็บจำลองความปลอดภัย และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลลัพธ์:

<style type="text/css">
.w-sandbox-main { display: flex !important; gap: 20px !important; margin: 1.5rem auto !important; max-width: 1000px !important; }
.w-sandbox-nav { width: 220px !important; display: flex !important; flex-direction: column !important; gap: 8px !important; flex-shrink: 0 !important; }
.w-nav-item { background: rgba(255, 255, 255, 0.02) !important; border: 1px solid rgba(255, 255, 255, 0.06) !important; border-radius: 6px !important; padding: 10px 14px !important; color: #cbd5e1 !important; text-align: left !important; cursor: pointer !important; font-size: 0.78rem !important; transition: all 0.2s !important; }
.w-nav-item:hover, .w-nav-item.active { border-color: #a855f7 !important; color: #ffffff !important; background: rgba(168, 85, 247, 0.05) !important; }
.w-nav-item.active { font-weight: 700 !important; box-shadow: 0 0 8px rgba(168, 85, 247, 0.15) !important; }
.w-sandbox-panels { flex-grow: 1 !important; }
.w-sand-panel { background: #05070f !important; border: 1px solid rgba(255, 255, 255, 0.08) !important; border-radius: 10px !important; padding: 20px !important; box-shadow: 0 8px 24px rgba(0,0,0,0.45) !important; }
</style>
<div class="w-sandbox-main">
<div class="w-sandbox-nav">
<button id="nav-item-dirb" class="w-nav-item active" onclick="showSandboxItem('dirb', this)">1. Dirb Backup Scan</button>
<button id="nav-item-curl" class="w-nav-item" onclick="showSandboxItem('curl', this)">2. cURL HTTP Audit</button>
</div>
<div class="w-sandbox-panels">
<div id="panel-dirb" class="w-sand-panel" style="display: block;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>1. Brute-forcing Web Backups with Dirb</span>
<span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(168,85,247,0.08); border: 1px solid rgba(168,85,247,0.2); color: #a855f7; font-family: monospace;">Dirb Scanner</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #a855f7; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">dirb http://ctf.rpca.ac.th/ /usr/share/wordlists/dirb/common.txt -X .zip,.bak</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startPostSim('dirb')" style="background: rgba(168,85,247,0.1); border: 1px solid rgba(168,85,247,0.3); border-radius: 4px; color: #a855f7; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700;">▶ Run Simulation</button>
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
<div id="panel-curl" class="w-sand-panel" style="display: none;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>2. cURL HTTP OPTIONS Audit</span>
<span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(168,85,247,0.08); border: 1px solid rgba(168,85,247,0.2); color: #a855f7; font-family: monospace;">cURL Tool</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #a855f7; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">curl -X OPTIONS -i http://ctf.rpca.ac.th/</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startPostSim('curl')" style="background: rgba(168,85,247,0.1); border: 1px solid rgba(168,85,247,0.3); border-radius: 4px; color: #a855f7; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700;">▶ Run Simulation</button>
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
  var items = document.querySelectorAll('.w-sandbox-nav .w-nav-item');
  items.forEach(function(i) { i.classList.remove('active'); });
  element.classList.add('active');
  var panels = document.querySelectorAll('.w-sand-panel');
  panels.forEach(function(p) { p.style.setProperty('display', 'none', 'important'); });
  var targetPanel = document.getElementById('panel-' + itemKey);
  if (targetPanel) { targetPanel.style.setProperty('display', 'block', 'important'); }
}
window.startPostSim = function(itemKey) {
  var term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#ffffff; font-weight:bold;">Running audit checks...</span>\n[.] Connecting target server...';
  setTimeout(function() {
    if (itemKey === 'dirb') {
      term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#3ddc84; font-weight:bold;">DIRB scan results:</span>\nFOUND: http://ctf.rpca.ac.th/backup.zip (CODE: 200)\nFOUND: http://ctf.rpca.ac.th/old_site.bak (CODE: 200)\n\n[+] Dirb completed successfully!';
    } else if (itemKey === 'curl') {
      term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#a855f7; font-weight:bold;">HTTP/1.1 200 OK</span>\nAllow: GET, POST, OPTIONS, TRACE, WebDAV\nServer: Apache/2.4.41 (Ubuntu)\nContent-Length: 0\n\n[+] OPTIONS check finished.';
    }
  }, 1000);
}
setTimeout(function() {
  var activeBtn = document.querySelector('.w-sandbox-nav .w-nav-item.active');
  if (activeBtn) { activeBtn.click(); }
}, 100);
</script>"""

###############################################################################
# LESSON 178 QUIZ (Block 2) - unique names: lessonKey178
###############################################################################
QUIZ_178 = r"""### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการบันทึกความสำเร็จและปลดล็อกปุ่มบทเรียนถัดไป:

<div class="row align-items-center" style="margin:1.5rem auto; max-width:980px;"><div class="col-md-8"><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. ช่องโหว่ประเภทใดเกิดขึ้นจากการที่เซิร์ฟเวอร์นำอินพุตของผู้ใช้ไปเรียกประมวลผลเป็นคำสั่งระบบปฏิบัติการโดยตรง?</p><div class="options-container" data-q="q1"><label class="w-quiz-option"><input type="radio" name="inj_type" value="SQLi" data-hash="false">SQL Injection</label><label class="w-quiz-option"><input type="radio" name="inj_type" value="Command Injection" data-hash="23c7f5c90b6b80d90bd93d8435d648b26e03fb21884be5e38f6b864a66e4a2cd">Command Injection</label><label class="w-quiz-option"><input type="radio" name="inj_type" value="XSS" data-hash="false">Cross-Site Scripting (XSS)</label><label class="w-quiz-option"><input type="radio" name="inj_type" value="LFI" data-hash="false">Local File Inclusion (LFI)</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. คิวรีเป้าหมายพิเศษระดับมาตรฐาน ' OR 1=1 -- นิยมใช้ส่งเข้าไปในฐานข้อมูลเพื่อทำลายเงื่อนไขข้อใด?</p><div class="options-container" data-q="q2"><label class="w-quiz-option"><input type="radio" name="sqli_opt" value="Data Exfiltration" data-hash="false">ขโมยดูข้อมูลทั้งหมด (Data Exfiltration)</label><label class="w-quiz-option"><input type="radio" name="sqli_opt" value="Bypass Auth" data-hash="a95aa975765796245d8b8ff716d0046522bb33f749eb721867c4e515d18d451">ข้ามขั้นตอนตรวจสอบยืนยันตน (Bypass Authentication)</label><label class="w-quiz-option"><input type="radio" name="sqli_opt" value="DoS" data-hash="false">ทำลายเซิร์ฟเวอร์ระบบล่ม (Denial of Service)</label><label class="w-quiz-option"><input type="radio" name="sqli_opt" value="Password cracking" data-hash="false">ค้นหารหัสผ่านระบบ (Password Cracking)</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div></div><div class="col-md-4 text-center"><div class="p-4" style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); border-radius:12px; min-height:220px; display:flex; flex-direction:column; justify-content:center; align-items:center;"><span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;">Lesson Progress</span><div class="neon-gauge-container"><svg class="neon-gauge" viewBox="0 0 36 36"><path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><path class="neon-gauge-fill" id="lesson-gauge-fill" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text">0%</text></svg></div><span id="lesson-status-txt" class="mt-3 d-block text-muted" style="font-size:0.78rem;">โปรดตอบคำถามให้ครบ 2 ข้อ</span></div></div></div>
<style>
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:#a855f7; stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease, stroke 0.5s ease; filter:drop-shadow(0 0 5px rgba(168,85,247,0.5));}
.neon-gauge-text {fill:#ffffff; font-family:'JetBrains Mono',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}
</style>
<script>
var lessonKey178 = 'solved_lesson_178';
function getSavedSolves178() { try { return JSON.parse(localStorage.getItem(lessonKey178) || '[]'); } catch(e) { return []; } }
function updateLocalProgress178() {
  var solved = getSavedSolves178();
  var total = 2;
  var percent = Math.round((solved.length / total) * 100);
  var fill = document.getElementById('lesson-gauge-fill');
  var text = document.getElementById('lesson-gauge-text');
  var status = document.getElementById('lesson-status-txt');
  if (fill) fill.setAttribute('stroke-dasharray', percent + ', 100');
  if (text) text.textContent = percent + '%';
  if (solved.length === total) {
    if (fill) fill.style.stroke = '#3ddc84';
    if (status) status.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
  } else {
    if (fill) fill.style.stroke = '#a855f7';
    if (status) status.textContent = 'ทำเสร็จแล้ว ' + solved.length + '/' + total + ' ข้อ';
  }
}
document.addEventListener('click', function(e) {
  var label = e.target.closest('.w-quiz-option');
  if (label) {
    var container = label.closest('.options-container');
    if (container) {
      container.querySelectorAll('.w-quiz-option').forEach(function(opt) { opt.classList.remove('selected'); });
      label.classList.add('selected');
      var radio = label.querySelector('input[type="radio"]');
      if (radio) radio.checked = true;
    }
  }
});
window.verifyMultipleChoice = function(button) {
  var cell = button.closest('.question-cell');
  var selectedRadio = cell.querySelector('input[type="radio"]:checked');
  var feedback = cell.querySelector('.feedback-msg');
  if (!selectedRadio) {
    feedback.className = "feedback-msg mt-2 alert-warning py-1.5 px-3 text-dark";
    feedback.innerHTML = '<i class="fas fa-exclamation-triangle mr-1"></i> กรุณาเลือกคำตอบ';
    feedback.style.setProperty('display', 'block', 'important');
    return;
  }
  var hashVal = selectedRadio.getAttribute('data-hash');
  if (hashVal !== 'false') {
    feedback.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
    feedback.innerHTML = '<i class="fas fa-check-circle mr-1"></i> คำตอบถูกต้อง!';
    feedback.style.setProperty('display', 'block', 'important');
    cell.querySelectorAll('input[type="radio"]').forEach(function(r) { r.disabled = true; });
    cell.querySelectorAll('.w-quiz-option').forEach(function(opt) { opt.style.pointerEvents = 'none'; });
    button.disabled = true;
    var solved = getSavedSolves178();
    if (solved.indexOf(hashVal) === -1) {
      solved.push(hashVal);
      localStorage.setItem(lessonKey178, JSON.stringify(solved));
    }
    updateLocalProgress178();
  } else {
    feedback.className = "feedback-msg mt-2 alert-danger py-1.5 px-3 text-white bg-danger border-0";
    feedback.innerHTML = '<i class="fas fa-times-circle mr-1"></i> คำตอบไม่ถูกต้อง ลองใหม่!';
    feedback.style.setProperty('display', 'block', 'important');
  }
}
setTimeout(function() {
  var solved = getSavedSolves178();
  document.querySelectorAll('.options-container').forEach(function(container) {
    container.querySelectorAll('input[type="radio"]').forEach(function(radio) {
      var hash = radio.getAttribute('data-hash');
      if (solved.indexOf(hash) !== -1) {
        radio.checked = true;
        var label = radio.closest('.w-quiz-option');
        if (label) label.classList.add('selected');
        container.querySelectorAll('input[type="radio"]').forEach(function(r) { r.disabled = true; });
        container.querySelectorAll('.w-quiz-option').forEach(function(opt) { opt.style.pointerEvents = 'none'; });
        var cell = container.closest('.question-cell');
        if (cell) {
          var btn = cell.querySelector('button');
          if (btn) btn.disabled = true;
          var fb = cell.querySelector('.feedback-msg');
          if (fb) {
            fb.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
            fb.innerHTML = '<i class="fas fa-check-circle mr-1"></i> เรียบร้อยแล้ว';
            fb.style.setProperty('display', 'block', 'important');
          }
        }
      }
    });
  });
  updateLocalProgress178();
}, 200);
</script>"""

###############################################################################
# LESSON 179 SANDBOX (Block 1) - SQLi & Command Injection Lab
###############################################################################
SANDBOX_179 = r"""### 💻 SQLi & Command Injection Lab Simulator (จำลองการแทรกคำสั่งประมวลผล)

คลิกหัวข้อด้านซ้ายมือเพื่อศึกษาช่องโหว่ และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลการแทรกคำสั่ง:

<style type="text/css">
.w-sandbox-main { display: flex !important; gap: 20px !important; margin: 1.5rem auto !important; max-width: 1000px !important; }
.w-sandbox-nav { width: 220px !important; display: flex !important; flex-direction: column !important; gap: 8px !important; flex-shrink: 0 !important; }
.w-nav-item { background: rgba(255, 255, 255, 0.02) !important; border: 1px solid rgba(255, 255, 255, 0.06) !important; border-radius: 6px !important; padding: 10px 14px !important; color: #cbd5e1 !important; text-align: left !important; cursor: pointer !important; font-size: 0.78rem !important; transition: all 0.2s !important; }
.w-nav-item:hover, .w-nav-item.active { border-color: #3b82f6 !important; color: #ffffff !important; background: rgba(59, 130, 246, 0.05) !important; }
.w-nav-item.active { font-weight: 700 !important; box-shadow: 0 0 8px rgba(59, 130, 246, 0.15) !important; }
.w-sandbox-panels { flex-grow: 1 !important; }
.w-sand-panel { background: #05070f !important; border: 1px solid rgba(255, 255, 255, 0.08) !important; border-radius: 10px !important; padding: 20px !important; box-shadow: 0 8px 24px rgba(0,0,0,0.45) !important; }
</style>
<div class="w-sandbox-main">
<div class="w-sandbox-nav">
<button id="nav-item-sqlitest" class="w-nav-item active" onclick="showSandboxItem('sqlitest', this)">1. UNION SQLi Test</button>
<button id="nav-item-cmdtest" class="w-nav-item" onclick="showSandboxItem('cmdtest', this)">2. OS Command Injection</button>
</div>
<div class="w-sandbox-panels">
<div id="panel-sqlitest" class="w-sand-panel" style="display: block;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>1. UNION-Based SQL Injection Simulation</span>
<span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(59,130,246,0.08); border: 1px solid rgba(59,130,246,0.2); color: #3b82f6; font-family: monospace;">UNION SQLi</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #3b82f6; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">' UNION SELECT null, username, password FROM users --</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startPostSim('sqlitest')" style="background: rgba(59,130,246,0.1); border: 1px solid rgba(59,130,246,0.3); border-radius: 4px; color: #3b82f6; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700;">▶ Run Simulation</button>
</div>
<div id="term-sqlitest" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 90px;">
<span style="color: #3ddc84;">db-cli$</span> [กดปุ่ม Run Simulation เพื่อส่ง UNION payload]
</div>
</div>
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 16px; font-size: 0.83rem; color: #cbd5e1; line-height: 1.65;">
<h5 style="margin: 0 0 8px; font-size: 0.85rem; color: #fbbf24; font-weight: bold;">⚙️ Command Description</h5>
<p style="margin: 0;">คิวรีผสาน UNION SELECT ช่วยให้เราแอบไปดึงข้อมูลผู้ใช้งานและรหัสผ่านจากตารางอื่นออกมาทางเว็บบอร์ดแสดงผล</p>
</div>
</div>
<div id="panel-cmdtest" class="w-sand-panel" style="display: none;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>2. OS Command Injection Bypass Space</span>
<span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(59,130,246,0.08); border: 1px solid rgba(59,130,246,0.2); color: #3b82f6; font-family: monospace;">OS Command</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #3b82f6; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">cat${IFS}/etc/passwd</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startPostSim('cmdtest')" style="background: rgba(59,130,246,0.1); border: 1px solid rgba(59,130,246,0.3); border-radius: 4px; color: #3b82f6; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700;">▶ Run Simulation</button>
</div>
<div id="term-cmdtest" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 90px;">
<span style="color: #3ddc84;">kali$</span> [กดปุ่ม Run Simulation เพื่อส่งคำสั่ง]
</div>
</div>
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 16px; font-size: 0.83rem; color: #cbd5e1; line-height: 1.65;">
<h5 style="margin: 0 0 8px; font-size: 0.85rem; color: #fbbf24; font-weight: bold;">⚙️ Command Description</h5>
<p style="margin: 0;">การเขียนตัวแปร IFS ช่วยเลี่ยงการกรองช่องว่าง ทำให้คำสั่งสามารถรันเพื่อเรียกดูไฟล์ระบบปฏิบัติการได้เหมือนเดิม</p>
</div>
</div>
</div>
</div>
<script>
window.showSandboxItem = function(itemKey, element) {
  var items = document.querySelectorAll('.w-sandbox-nav .w-nav-item');
  items.forEach(function(i) { i.classList.remove('active'); });
  element.classList.add('active');
  var panels = document.querySelectorAll('.w-sand-panel');
  panels.forEach(function(p) { p.style.setProperty('display', 'none', 'important'); });
  var targetPanel = document.getElementById('panel-' + itemKey);
  if (targetPanel) { targetPanel.style.setProperty('display', 'block', 'important'); }
}
window.startPostSim = function(itemKey) {
  var term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#ffffff; font-weight:bold;">Executing commands...</span>\n[.] Verifying backend sanitization checks...';
  setTimeout(function() {
    if (itemKey === 'sqlitest') {
      term.innerHTML = '<span style="color:#64748b;">db-cli$</span> <span style="color:#3ddc84; font-weight:bold;">UNION select output:</span>\nID: null | User: admin | Pass: <span style="color:#ef4444;">$2y$10$xyzPasswordHash...</span>\nID: null | User: user1 | Pass: <span style="color:#ef4444;">$2y$10$abcHashUser1...</span>\n\n[+] Data exfiltration successful!';
    } else if (itemKey === 'cmdtest') {
      term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#3ddc84; font-weight:bold;">cat /etc/passwd:</span>\nroot:x:0:0:root:/root:/bin/bash\nbin:x:1:1:bin:/bin:/sbin/nologin\n\n[+] Command completed without spaces.';
    }
  }, 1000);
}
setTimeout(function() {
  var activeBtn = document.querySelector('.w-sandbox-nav .w-nav-item.active');
  if (activeBtn) { activeBtn.click(); }
}, 100);
</script>"""

###############################################################################
# LESSON 179 QUIZ (Block 2) - unique names: lessonKey179
###############################################################################
QUIZ_179 = r"""### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการบันทึกความสำเร็จและปลดล็อกปุ่มบทเรียนถัดไป:

<div class="row align-items-center" style="margin:1.5rem auto; max-width:980px;"><div class="col-md-8"><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. ช่องโหว่ Cross-Site Scripting (XSS) เกิดจากการลอบฝังแทรกสคริปต์โค้ดประเภทใดเข้ามาทำงานฝั่ง Client Browser?</p><div class="options-container" data-q="q1"><label class="w-quiz-option"><input type="radio" name="xss_lang" value="SQL" data-hash="false">SQL Query code</label><label class="w-quiz-option"><input type="radio" name="xss_lang" value="JavaScript" data-hash="78ec09be8733f52e505820464fdbb19d45388047970d47d457cb146ef279ec3d">JavaScript</label><label class="w-quiz-option"><input type="radio" name="xss_lang" value="Bash" data-hash="false">Bash Shell command</label><label class="w-quiz-option"><input type="radio" name="xss_lang" value="PHP" data-hash="false">PHP Server Script</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. คีย์เวิร์ดมาตรฐาน HTML tag ใดที่นักโจมตีใช้ส่ง XSS Payload เพื่อเปิดจำลองกล่องป๊อปอัพ?</p><div class="options-container" data-q="q2"><label class="w-quiz-option"><input type="radio" name="xss_tag" value="script" data-hash="3a95aa975765796245d8b8ff716d0046522bb33f749eb721867c4e515d18d451"><span>&lt;script&gt;</span></label><label class="w-quiz-option"><input type="radio" name="xss_tag" value="iframe" data-hash="false"><span>&lt;iframe&gt;</span></label><label class="w-quiz-option"><input type="radio" name="xss_tag" value="div" data-hash="false"><span>&lt;div&gt;</span></label><label class="w-quiz-option"><input type="radio" name="xss_tag" value="img" data-hash="false"><span>&lt;img&gt;</span></label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div></div><div class="col-md-4 text-center"><div class="p-4" style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); border-radius:12px; min-height:220px; display:flex; flex-direction:column; justify-content:center; align-items:center;"><span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;">Lesson Progress</span><div class="neon-gauge-container"><svg class="neon-gauge" viewBox="0 0 36 36"><path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><path class="neon-gauge-fill" id="lesson-gauge-fill" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text">0%</text></svg></div><span id="lesson-status-txt" class="mt-3 d-block text-muted" style="font-size:0.78rem;">โปรดตอบคำถามให้ครบ 2 ข้อ</span></div></div></div>
<style>
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:#3b82f6; stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease, stroke 0.5s ease; filter:drop-shadow(0 0 5px rgba(59,130,246,0.5));}
.neon-gauge-text {fill:#ffffff; font-family:'JetBrains Mono',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}
</style>
<script>
var lessonKey179 = 'solved_lesson_179';
function getSavedSolves179() { try { return JSON.parse(localStorage.getItem(lessonKey179) || '[]'); } catch(e) { return []; } }
function updateLocalProgress179() {
  var solved = getSavedSolves179();
  var total = 2;
  var percent = Math.round((solved.length / total) * 100);
  var fill = document.getElementById('lesson-gauge-fill');
  var text = document.getElementById('lesson-gauge-text');
  var status = document.getElementById('lesson-status-txt');
  if (fill) fill.setAttribute('stroke-dasharray', percent + ', 100');
  if (text) text.textContent = percent + '%';
  if (solved.length === total) {
    if (fill) fill.style.stroke = '#3ddc84';
    if (status) status.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
  } else {
    if (fill) fill.style.stroke = '#3b82f6';
    if (status) status.textContent = 'ทำเสร็จแล้ว ' + solved.length + '/' + total + ' ข้อ';
  }
}
document.addEventListener('click', function(e) {
  var label = e.target.closest('.w-quiz-option');
  if (label) {
    var container = label.closest('.options-container');
    if (container) {
      container.querySelectorAll('.w-quiz-option').forEach(function(opt) { opt.classList.remove('selected'); });
      label.classList.add('selected');
      var radio = label.querySelector('input[type="radio"]');
      if (radio) radio.checked = true;
    }
  }
});
window.verifyMultipleChoice = function(button) {
  var cell = button.closest('.question-cell');
  var selectedRadio = cell.querySelector('input[type="radio"]:checked');
  var feedback = cell.querySelector('.feedback-msg');
  if (!selectedRadio) {
    feedback.className = "feedback-msg mt-2 alert-warning py-1.5 px-3 text-dark";
    feedback.innerHTML = '<i class="fas fa-exclamation-triangle mr-1"></i> กรุณาเลือกคำตอบ';
    feedback.style.setProperty('display', 'block', 'important');
    return;
  }
  var hashVal = selectedRadio.getAttribute('data-hash');
  if (hashVal !== 'false') {
    feedback.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
    feedback.innerHTML = '<i class="fas fa-check-circle mr-1"></i> คำตอบถูกต้อง!';
    feedback.style.setProperty('display', 'block', 'important');
    cell.querySelectorAll('input[type="radio"]').forEach(function(r) { r.disabled = true; });
    cell.querySelectorAll('.w-quiz-option').forEach(function(opt) { opt.style.pointerEvents = 'none'; });
    button.disabled = true;
    var solved = getSavedSolves179();
    if (solved.indexOf(hashVal) === -1) {
      solved.push(hashVal);
      localStorage.setItem(lessonKey179, JSON.stringify(solved));
    }
    updateLocalProgress179();
  } else {
    feedback.className = "feedback-msg mt-2 alert-danger py-1.5 px-3 text-white bg-danger border-0";
    feedback.innerHTML = '<i class="fas fa-times-circle mr-1"></i> คำตอบไม่ถูกต้อง ลองใหม่!';
    feedback.style.setProperty('display', 'block', 'important');
  }
}
setTimeout(function() {
  var solved = getSavedSolves179();
  document.querySelectorAll('.options-container').forEach(function(container) {
    container.querySelectorAll('input[type="radio"]').forEach(function(radio) {
      var hash = radio.getAttribute('data-hash');
      if (solved.indexOf(hash) !== -1) {
        radio.checked = true;
        var label = radio.closest('.w-quiz-option');
        if (label) label.classList.add('selected');
        container.querySelectorAll('input[type="radio"]').forEach(function(r) { r.disabled = true; });
        container.querySelectorAll('.w-quiz-option').forEach(function(opt) { opt.style.pointerEvents = 'none'; });
        var cell = container.closest('.question-cell');
        if (cell) {
          var btn = cell.querySelector('button');
          if (btn) btn.disabled = true;
          var fb = cell.querySelector('.feedback-msg');
          if (fb) {
            fb.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
            fb.innerHTML = '<i class="fas fa-check-circle mr-1"></i> เรียบร้อยแล้ว';
            fb.style.setProperty('display', 'block', 'important');
          }
        }
      }
    });
  });
  updateLocalProgress179();
}, 200);
</script>"""

###############################################################################
# LESSON 180 SANDBOX (Block 1) - CMS Security Audit
###############################################################################
SANDBOX_180 = r"""### 💻 CMS Security Audit Sandbox (จำลองเรียกสแกนความปลอดภัย CMS)

คลิกหัวข้อด้านซ้ายมือเพื่อศึกษาขั้นตอน และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลการสแกนความเปราะบาง:

<style type="text/css">
.w-sandbox-main { display: flex !important; gap: 20px !important; margin: 1.5rem auto !important; max-width: 1000px !important; }
.w-sandbox-nav { width: 220px !important; display: flex !important; flex-direction: column !important; gap: 8px !important; flex-shrink: 0 !important; }
.w-nav-item { background: rgba(255, 255, 255, 0.02) !important; border: 1px solid rgba(255, 255, 255, 0.06) !important; border-radius: 6px !important; padding: 10px 14px !important; color: #cbd5e1 !important; text-align: left !important; cursor: pointer !important; font-size: 0.78rem !important; transition: all 0.2s !important; }
.w-nav-item:hover, .w-nav-item.active { border-color: #10b981 !important; color: #ffffff !important; background: rgba(16, 185, 129, 0.05) !important; }
.w-nav-item.active { font-weight: 700 !important; box-shadow: 0 0 8px rgba(16, 185, 129, 0.15) !important; }
.w-sandbox-panels { flex-grow: 1 !important; }
.w-sand-panel { background: #05070f !important; border: 1px solid rgba(255, 255, 255, 0.08) !important; border-radius: 10px !important; padding: 20px !important; box-shadow: 0 8px 24px rgba(0,0,0,0.45) !important; }
</style>
<div class="w-sandbox-main">
<div class="w-sandbox-nav">
<button id="nav-item-wpscan" class="w-nav-item active" onclick="showSandboxItem('wpscan', this)">1. WPScan Vulnerability</button>
<button id="nav-item-joomscan" class="w-nav-item" onclick="showSandboxItem('joomscan', this)">2. JoomScan Audit</button>
</div>
<div class="w-sandbox-panels">
<div id="panel-wpscan" class="w-sand-panel" style="display: block;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>1. Scanning WordPress Vulnerabilities with WPScan</span>
<span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.2); color: #10b981; font-family: monospace;">WPScan Tool</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #10b981; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">wpscan --url http://ctf.rpca.ac.th/wp/ --enumerate vp,u</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startPostSim('wpscan')" style="background: rgba(16,185,129,0.1); border: 1px solid rgba(16,185,129,0.3); border-radius: 4px; color: #10b981; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700;">▶ Run Simulation</button>
</div>
<div id="term-wpscan" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 90px;">
<span style="color: #3ddc84;">kali$</span> [กดปุ่ม Run Simulation เพื่อยิงสแกน WPScan]
</div>
</div>
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 16px; font-size: 0.83rem; color: #cbd5e1; line-height: 1.65;">
<h5 style="margin: 0 0 8px; font-size: 0.85rem; color: #fbbf24; font-weight: bold;">⚙️ Command Description</h5>
<p style="margin: 0;">คำสั่งค้นหาระบุปลั๊กอินที่มีช่องโหว่ความเสี่ยง (vp) และตรวจสอบรายชื่อผู้ใช้งาน (u) เพื่อวางสเปกประเมินความปลอดภัย</p>
</div>
</div>
<div id="panel-joomscan" class="w-sand-panel" style="display: none;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>2. Assessing Joomla Website Security with JoomScan</span>
<span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.2); color: #10b981; font-family: monospace;">JoomScan Tool</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #10b981; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">joomscan -u http://ctf.rpca.ac.th/joomla/ --components</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startPostSim('joomscan')" style="background: rgba(16,185,129,0.1); border: 1px solid rgba(16,185,129,0.3); border-radius: 4px; color: #10b981; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700;">▶ Run Simulation</button>
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
  var items = document.querySelectorAll('.w-sandbox-nav .w-nav-item');
  items.forEach(function(i) { i.classList.remove('active'); });
  element.classList.add('active');
  var panels = document.querySelectorAll('.w-sand-panel');
  panels.forEach(function(p) { p.style.setProperty('display', 'none', 'important'); });
  var targetPanel = document.getElementById('panel-' + itemKey);
  if (targetPanel) { targetPanel.style.setProperty('display', 'block', 'important'); }
}
window.startPostSim = function(itemKey) {
  var term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#ffffff; font-weight:bold;">Running CMS mapping audits...</span>\n[.] Executing target scanner engines...';
  setTimeout(function() {
    if (itemKey === 'wpscan') {
      term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#3ddc84; font-weight:bold;">WPScan Output:</span>\nWordPress version: 6.2.2 (Outdated)\nFOUND User: admin (ID: 1)\nFOUND Vulnerable Plugin: contact-form-7 v5.7.1 (XSS vulnerable)\n\n[+] WPScan Completed!';
    } else if (itemKey === 'joomscan') {
      term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#3ddc84; font-weight:bold;">OWASP Joomla! Vulnerability Scanner:</span>\nJoomla! version: 3.9.22 (Outdated)\nFOUND: http://ctf.rpca.ac.th/joomla/configuration.php-bak (CODE: 200)\n\n[+] JoomScan completed successfully.';
    }
  }, 1000);
}
setTimeout(function() {
  var activeBtn = document.querySelector('.w-sandbox-nav .w-nav-item.active');
  if (activeBtn) { activeBtn.click(); }
}, 100);
</script>"""

###############################################################################
# LESSON 180 QUIZ (Block 2) - unique names: lessonKey180
###############################################################################
QUIZ_180 = r"""### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการบันทึกความสำเร็จและปลดล็อกปุ่มบทเรียนถัดไป:

<div class="row align-items-center" style="margin:1.5rem auto; max-width:980px;"><div class="col-md-8"><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. ส่วนหัว (Header) ความปลอดภัยใดใน HTTP Response ที่ใช้ป้องกันหน้าเว็บไม่ให้ถูกนำไปฝังใน Iframe เพื่อเลี่ยงช่องโหว่ Clickjacking?</p><div class="options-container" data-q="q1"><label class="w-quiz-option"><input type="radio" name="xframe_h" value="X-Frame-Options" data-hash="c9b7f5256e2978000bd93d8435d648b26e03fb21884be5e38f6b864a66e4a2cd">X-Frame-Options</label><label class="w-quiz-option"><input type="radio" name="xframe_h" value="CSP" data-hash="false">Content-Security-Policy</label><label class="w-quiz-option"><input type="radio" name="xframe_h" value="HSTS" data-hash="false">Strict-Transport-Security</label><label class="w-quiz-option"><input type="radio" name="xframe_h" value="XXSS" data-hash="false">X-XSS-Protection</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. หลักปฏิบัติเพื่อความปลอดภัยในการป้องกันการแทรกโค้ดทำลายระบบเครือข่ายฐานข้อมูล (Injection) ทุกประเภทคือข้อใด?</p><div class="options-container" data-q="q2"><label class="w-quiz-option"><input type="radio" name="sec_coding" value="Input Validation" data-hash="277bc1b69ad3178c775080e7221f75355694a08ba1c38fa8b79f38ebcb5c8a41">การกรองตรวจสอบความถูกต้องข้อมูลนำเข้า (Input Validation)</label><label class="w-quiz-option"><input type="radio" name="sec_coding" value="Encryption" data-hash="false">การเข้ารหัสฐานข้อมูล (Database Encryption)</label><label class="w-quiz-option"><input type="radio" name="sec_coding" value="Backup" data-hash="false">การสำรองไฟล์ข้อมูลประจำวัน (Daily Backup)</label><label class="w-quiz-option"><input type="radio" name="sec_coding" value="IDS" data-hash="false">การติดตั้งระบบแจ้งเตือนแฮกเกอร์ (Intrusion Detection)</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div></div><div class="col-md-4 text-center"><div class="p-4" style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); border-radius:12px; min-height:220px; display:flex; flex-direction:column; justify-content:center; align-items:center;"><span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;">Lesson Progress</span><div class="neon-gauge-container"><svg class="neon-gauge" viewBox="0 0 36 36"><path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><path class="neon-gauge-fill" id="lesson-gauge-fill" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text">0%</text></svg></div><span id="lesson-status-txt" class="mt-3 d-block text-muted" style="font-size:0.78rem;">โปรดตอบคำถามให้ครบ 2 ข้อ</span></div></div></div>
<style>
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:#10b981; stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease, stroke 0.5s ease; filter:drop-shadow(0 0 5px rgba(16,185,129,0.5));}
.neon-gauge-text {fill:#ffffff; font-family:'JetBrains Mono',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}
</style>
<script>
var lessonKey180 = 'solved_lesson_180';
function getSavedSolves180() { try { return JSON.parse(localStorage.getItem(lessonKey180) || '[]'); } catch(e) { return []; } }
function updateLocalProgress180() {
  var solved = getSavedSolves180();
  var total = 2;
  var percent = Math.round((solved.length / total) * 100);
  var fill = document.getElementById('lesson-gauge-fill');
  var text = document.getElementById('lesson-gauge-text');
  var status = document.getElementById('lesson-status-txt');
  if (fill) fill.setAttribute('stroke-dasharray', percent + ', 100');
  if (text) text.textContent = percent + '%';
  if (solved.length === total) {
    if (fill) fill.style.stroke = '#3ddc84';
    if (status) status.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
  } else {
    if (fill) fill.style.stroke = '#10b981';
    if (status) status.textContent = 'ทำเสร็จแล้ว ' + solved.length + '/' + total + ' ข้อ';
  }
}
document.addEventListener('click', function(e) {
  var label = e.target.closest('.w-quiz-option');
  if (label) {
    var container = label.closest('.options-container');
    if (container) {
      container.querySelectorAll('.w-quiz-option').forEach(function(opt) { opt.classList.remove('selected'); });
      label.classList.add('selected');
      var radio = label.querySelector('input[type="radio"]');
      if (radio) radio.checked = true;
    }
  }
});
window.verifyMultipleChoice = function(button) {
  var cell = button.closest('.question-cell');
  var selectedRadio = cell.querySelector('input[type="radio"]:checked');
  var feedback = cell.querySelector('.feedback-msg');
  if (!selectedRadio) {
    feedback.className = "feedback-msg mt-2 alert-warning py-1.5 px-3 text-dark";
    feedback.innerHTML = '<i class="fas fa-exclamation-triangle mr-1"></i> กรุณาเลือกคำตอบ';
    feedback.style.setProperty('display', 'block', 'important');
    return;
  }
  var hashVal = selectedRadio.getAttribute('data-hash');
  if (hashVal !== 'false') {
    feedback.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
    feedback.innerHTML = '<i class="fas fa-check-circle mr-1"></i> คำตอบถูกต้อง!';
    feedback.style.setProperty('display', 'block', 'important');
    cell.querySelectorAll('input[type="radio"]').forEach(function(r) { r.disabled = true; });
    cell.querySelectorAll('.w-quiz-option').forEach(function(opt) { opt.style.pointerEvents = 'none'; });
    button.disabled = true;
    var solved = getSavedSolves180();
    if (solved.indexOf(hashVal) === -1) {
      solved.push(hashVal);
      localStorage.setItem(lessonKey180, JSON.stringify(solved));
    }
    updateLocalProgress180();
  } else {
    feedback.className = "feedback-msg mt-2 alert-danger py-1.5 px-3 text-white bg-danger border-0";
    feedback.innerHTML = '<i class="fas fa-times-circle mr-1"></i> คำตอบไม่ถูกต้อง ลองใหม่!';
    feedback.style.setProperty('display', 'block', 'important');
  }
}
setTimeout(function() {
  var solved = getSavedSolves180();
  document.querySelectorAll('.options-container').forEach(function(container) {
    container.querySelectorAll('input[type="radio"]').forEach(function(radio) {
      var hash = radio.getAttribute('data-hash');
      if (solved.indexOf(hash) !== -1) {
        radio.checked = true;
        var label = radio.closest('.w-quiz-option');
        if (label) label.classList.add('selected');
        container.querySelectorAll('input[type="radio"]').forEach(function(r) { r.disabled = true; });
        container.querySelectorAll('.w-quiz-option').forEach(function(opt) { opt.style.pointerEvents = 'none'; });
        var cell = container.closest('.question-cell');
        if (cell) {
          var btn = cell.querySelector('button');
          if (btn) btn.disabled = true;
          var fb = cell.querySelector('.feedback-msg');
          if (fb) {
            fb.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
            fb.innerHTML = '<i class="fas fa-check-circle mr-1"></i> เรียบร้อยแล้ว';
            fb.style.setProperty('display', 'block', 'important');
          }
        }
      }
    });
  });
  updateLocalProgress180();
}, 200);
</script>"""

###############################################################################
# Execute the update
###############################################################################
with app.app_context():
    from CTFd.plugins.tutorials import TutorialLesson
    db = app.db

    updates = {
        177: {1: SANDBOX_177, 2: QUIZ_177},
        178: {1: SANDBOX_178, 2: QUIZ_178},
        179: {1: SANDBOX_179, 2: QUIZ_179},
        180: {1: SANDBOX_180, 2: QUIZ_180},
    }

    for lid, block_map in updates.items():
        lesson = db.session.query(TutorialLesson).filter_by(id=lid).first()
        if not lesson:
            print(f"[!] Lesson {lid} not found!")
            continue

        blocks = json.loads(lesson.content)
        for bi, new_val in block_map.items():
            blocks[bi]["value"] = new_val
            print(f"  [+] Lesson {lid} Block {bi}: replaced ({len(new_val)} chars)")

        lesson.content = json.dumps(blocks, ensure_ascii=False)
        db.session.commit()
        print(f"[OK] Lesson {lid} saved!")

    # Verify
    print("\n=== VERIFICATION ===")
    for lid in [177, 178, 179, 180]:
        lesson = db.session.query(TutorialLesson).filter_by(id=lid).first()
        blocks = json.loads(lesson.content)
        for bi in [1, 2]:
            val = blocks[bi].get("value", "")
            has_onclick = 'onclick=' in val
            has_script = '<script>' in val
            has_const = 'const lessonKey' in val
            has_var = 'var lessonKey' in val
            print(f"L{lid} B{bi}: onclick={has_onclick}, script={has_script}, const={has_const}, var={has_var}")

    print("\n[DONE] All lessons restored to working Chapter-4 pattern!")
