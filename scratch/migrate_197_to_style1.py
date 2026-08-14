import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

def make_lesson_197_html():
    html = """### 🖥️ Linux & Windows OS Security Final Exam

ประเมินความรู้ทางด้านระบบปฏิบัติการขั้นพื้นฐานและการจัดการสิทธิ์ความปลอดภัยในระบบไซเบอร์ด้วยแบบทดสอบประเมินความรู้จำลองแบบโต้ตอบได้ด้านล่างนี้ (มีทั้งหมด 5 ข้อ) ตอบถูกทั้งหมดเพื่อผ่านบทเรียนนี้:

<style>
.mini-quiz-box{width:100%;max-width:1050px;margin:2rem auto;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:24px;box-shadow:0 8px 32px rgba(0,0,0,0.3);box-sizing:border-box;}
.mq-layout-container {display:flex; gap:24px; align-items:stretch;}
.mq-questions-col {flex:1;}
.mq-gauge-col {width:160px; display:flex; flex-direction:column; align-items:center; justify-content:center; border-left:1px solid rgba(255,255,255,0.06); padding-left:24px;}
@media (max-width: 768px) {
  .mq-layout-container {flex-direction:column;}
  .mq-gauge-col {width:100%; border-left:none; padding-left:0; border-top:1px solid rgba(255,255,255,0.06); padding-top:24px;}
}
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:url(#gauge-grad-197); stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease; filter:drop-shadow(0 0 5px rgba(0,240,255,0.4));}
.neon-gauge-text {fill:#ffffff; font-family:'JetBrains Mono',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}

.mq-q{margin-bottom:20px;}
.mq-title{font-size:0.9rem;font-weight:800;color:#e2e8f0;margin-bottom:10px;}
.mq-title span{color:#00f0ff;font-family:'JetBrains Mono',monospace;margin-right:6px;}
.mini-opts{display:flex;flex-direction:column;gap:6px;}
.mini-opt{display:flex;align-items:center;gap:10px;padding:10px 14px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.05);border-radius:8px;cursor:pointer;transition:all 0.15s ease;user-select:none;font-size:0.83rem;color:#cbd5e1;}
.mini-opt:hover{border-color:rgba(0,240,255,0.2);background:rgba(0,240,255,0.02);}
.mini-opt.selected{border-color:#00f0ff;background:rgba(0,240,255,0.08);color:#ffffff;}
.mini-opt.correct{border-color:#3ddc84;background:rgba(61,220,132,0.08);color:#ffffff;}
.mini-opt.incorrect{border-color:#ff007f;background:rgba(255,0,127,0.08);color:#ffffff;}
.mini-bullet{width:15px;height:15px;border:1px solid rgba(255,255,255,0.3);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.58rem;font-weight:bold;}
.mini-opt.selected .mini-bullet{border-color:#00f0ff;background:#00f0ff;color:#070910;}

.mq-btn-check{padding:10px 20px;background:#00f0ff;border:none;border-radius:6px;font-family:'JetBrains Mono',monospace;font-size:0.82rem;font-weight:800;color:#070910;cursor:pointer;box-shadow:0 0 10px rgba(0,240,255,0.25);transition:all 0.15s ease;}
.mq-btn-check:hover{background:#ffffff;box-shadow:0 0 15px rgba(255,255,255,0.4);transform:translateY(-1px);}
.mq-status-bar{display:none;padding:12px 16px;border-radius:8px;font-size:0.85rem;margin-top:16px;font-weight:700;line-height:1.5;}

.w-expl-box{margin-top:15px;padding:15px;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);border-radius:8px;}
.w-expl-q{font-size:0.85rem;font-weight:bold;color:#fbbf24;margin-bottom:6px;}
.w-expl-a{font-size:0.82rem;color:#cbd5e1;margin-bottom:0;line-height:1.5;}
</style>

<div id="mq-box-197" class="mini-quiz-box">
<div class="mq-layout-container">
<div class="mq-questions-col">
<!-- Question 1 -->
<div class="mq-q" data-correct="A">
<div class="mq-title"><span>Q1.</span> โครงสร้างของระบบปฏิบัติการ (Kernel Architecture) ข้อใดต่อไปนี้ที่อธิบายลักษณะของ Linux และ Windows ได้ถูกต้อง?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A"><span class="mini-bullet">A</span> Linux เป็น Monolithic Kernel / Windows NT เป็น Hybrid Kernel</div>
<div class="mini-opt" data-val="B"><span class="mini-bullet">B</span> Linux เป็น Microkernel / Windows NT เป็น Monolithic Kernel</div>
<div class="mini-opt" data-val="C"><span class="mini-bullet">C</span> Linux เป็น Hybrid Kernel / Windows NT เป็น Microkernel</div>
<div class="mini-opt" data-val="D"><span class="mini-bullet">D</span> ทั้งคู่มีสถาปัตยกรรมแบบ Exo-kernel เหมือนกันเพื่อเน้นประสิทธิภาพ</div>
</div>
</div>

<!-- Question 2 -->
<div class="mq-q" data-correct="C">
<div class="mq-title"><span>Q2.</span> หากผู้ดูแลระบบต้องการตั้งสิทธิ์การเข้าถึงสคริปต์เพื่อให้ "เจ้าของไฟล์คนเดียวเท่านั้นที่สามารถอ่าน เขียน และรันสคริปต์นี้ได้" ควรเลือกตั้งค่าสิทธิ์ข้อใด?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A"><span class="mini-bullet">A</span> chmod 777 script.sh</div>
<div class="mini-opt" data-val="B"><span class="mini-bullet">B</span> chmod 755 script.sh</div>
<div class="mini-opt" data-val="C"><span class="mini-bullet">C</span> chmod 700 script.sh</div>
<div class="mini-opt" data-val="D"><span class="mini-bullet">D</span> chmod 644 script.sh</div>
</div>
</div>

<!-- Question 3 -->
<div class="mq-q" data-correct="D">
<div class="mq-title"><span>Q3.</span> เมื่อมีการตรวจสอบสิทธิ์เข้าถึงไฟล์ในระบบปฏิบัติการ Windows (NTFS Permissions) สิทธิ์ในข้อใดมีลำดับความสำคัญสูงสุดและจะถูกบังคับใช้ก่อนเสมอ?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A"><span class="mini-bullet">A</span> Explicit Allow (สิทธิ์อนุญาตโดยตรง)</div>
<div class="mini-opt" data-val="B"><span class="mini-bullet">B</span> Inherited Allow (สิทธิ์อนุญาตที่สืบทอดมา)</div>
<div class="mini-opt" data-val="C"><span class="mini-bullet">C</span> Inherited Deny (สิทธิ์ปฏิเสธที่สืบทอดมา)</div>
<div class="mini-opt" data-val="D"><span class="mini-bullet">D</span> Explicit Deny (สิทธิ์ปฏิเสธโดยตรง)</div>
</div>
</div>

<!-- Question 4 -->
<div class="mq-q" data-correct="B">
<div class="mq-title"><span>Q4.</span> ตัวแปรสภาพแวดล้อม (Environment Variable) มาตรฐานใดในระบบปฏิบัติการ Windows ที่ใช้จัดเก็บรายการพาธระบบที่ใช้สืบค้นโปรแกรมเวลาเรียกใช้งานใน CMD?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A"><span class="mini-bullet">A</span> %USERPROFILE%</div>
<div class="mini-opt" data-val="B"><span class="mini-bullet">B</span> %PATH%</div>
<div class="mini-opt" data-val="C"><span class="mini-bullet">C</span> %SYSTEMROOT%</div>
<div class="mini-opt" data-val="D"><span class="mini-bullet">D</span> %OS%</div>
</div>
</div>

<!-- Question 5 -->
<div class="mq-q" data-correct="B">
<div class="mq-title"><span>Q5.</span> ข้อใดอธิบายความแตกต่างของมุมมองและวิธีการจัดการอุปกรณ์ต่อพ่วง (Peripherals) ใน Linux และ Windows ได้ตรงหลักการ?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A"><span class="mini-bullet">A</span> Linux มองเป็นพาร์ติชันตัวอักษรดิสก์ (A:, B:) / Windows มองเป็นโหนดการเชื่อมต่อพอร์ต</div>
<div class="mini-opt" data-val="B"><span class="mini-bullet">B</span> Linux มองอุปกรณ์ภายนอกเป็น "ไฟล์ข้อมูลปกติ" / Windows มองอุปกรณ์เหล่านั้นแยกต่างหากเป็น "Devices"</div>
<div class="mini-opt" data-val="C"><span class="mini-bullet">C</span> Linux มองเป็นหน่วยฮาร์ดแวร์ / Windows มองเป็นไลบรารีระบบเชื่อมร่วม</div>
<div class="mini-opt" data-val="D"><span class="mini-bullet">D</span> ไม่มีข้อใดถูก ทั้งคู่จัดการผ่านไดรฟ์ C:\ และสิทธิ์แอดมินเหมือนกันทุกประการ</div>
</div>
</div>

<button class="mq-btn-check" onclick="checkMiniQuiz197(197)">Check Answers / ตรวจคำตอบ</button>
<div id="mq-status-197" class="mq-status-bar"></div>
</div>

<div class="mq-gauge-col">
  <span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em; text-align:center;">Exam Progress</span>
  <div class="neon-gauge-container">
    <svg class="neon-gauge" viewBox="0 0 36 36">
      <defs>
        <linearGradient id="gauge-grad-197" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#ff007f" />
          <stop offset="50%" stop-color="#fbbf24" />
          <stop offset="100%" stop-color="#00f0ff" />
        </linearGradient>
      </defs>
      <path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
      <path class="neon-gauge-fill" id="lesson-gauge-fill-197" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
      <text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text-197">0%</text>
    </svg>
  </div>
  <span id="lesson-status-txt-197" class="mt-3 d-block text-muted" style="font-size:0.78rem; text-align:center;">โปรดตอบคำถามให้ครบ 5 ข้อ</span>
</div>
</div>
</div>

<script>
// Attach click listeners to manage selection state
document.querySelectorAll('#mq-box-197 .mini-opt').forEach(function(opt) {
  opt.addEventListener('click', function() {
    var parent = this.closest('.mq-q');
    parent.querySelectorAll('.mini-opt').forEach(function(o) { o.classList.remove('selected'); });
    this.classList.add('selected');
    updateMiniProgress197(197);
  });
});

function updateMiniProgress197(lnum) {
  var box = document.getElementById('mq-box-' + lnum);
  var qGroups = box.querySelectorAll('.mq-q');
  var answeredCount = 0;
  qGroups.forEach(function(g) {
    if (g.querySelector('.mini-opt.selected')) {
      answeredCount++;
    }
  });
  var pct = Math.round((answeredCount / qGroups.length) * 100);
  var fill = document.getElementById('lesson-gauge-fill-' + lnum);
  var text = document.getElementById('lesson-gauge-text-' + lnum);
  var status = document.getElementById('lesson-status-txt-' + lnum);
  if (fill) fill.setAttribute('stroke-dasharray', pct + ', 100');
  if (text) text.textContent = pct + '%';
  if (status) {
    if (pct === 100) {
      status.innerHTML = '<span style="color:#00f0ff; font-weight:bold;">กรุณากดส่งคำตอบ</span>';
    } else if (pct > 0) {
      status.textContent = 'ตอบคำถามแล้ว ' + answeredCount + '/' + qGroups.length + ' ข้อ';
    } else {
      status.textContent = 'โปรดตอบคำถามให้ครบ 5 ข้อ';
    }
  }
}

function checkMiniQuiz197(lnum) {
  var box = document.getElementById('mq-box-' + lnum);
  var groups = box.querySelectorAll('.mq-q');
  var score = 0;
  var allAnswered = true;

  groups.forEach(function(g) {
    var selected = g.querySelector('.mini-opt.selected');
    if (!selected) allAnswered = false;
  });

  if (!allAnswered) {
    alert("กรุณาตอบคำถามให้ครบถ้วนทั้ง 5 ข้อก่อนส่งคำตอบครับ!");
    return;
  }}

  groups.forEach(function(g) {
    var correctVal = g.getAttribute('data-correct');
    var selected = g.querySelector('.mini-opt.selected');
    var selectedVal = selected.getAttribute('data-val');

    g.querySelectorAll('.mini-opt').forEach(function(o) {
      o.classList.remove('correct', 'incorrect');
      var val = o.getAttribute('data-val');
      if (val === correctVal) {
        o.classList.add('correct');
      } else if (o.classList.contains('selected')) {
        o.classList.add('incorrect');
      }
    });

    if (selectedVal === correctVal) score++;
  });

  var fill = document.getElementById('lesson-gauge-fill-' + lnum);
  var text = document.getElementById('lesson-gauge-text-' + lnum);
  var status_txt = document.getElementById('lesson-status-txt-' + lnum);
  var status = document.getElementById('mq-status-' + lnum);
  status.style.display = 'block';

  if (score === 5) {
    if (fill) { fill.setAttribute('stroke-dasharray', '100, 100'); fill.style.stroke = '#3ddc84'; }
    if (text) text.textContent = '100%';
    if (status_txt) status_txt.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ผ่านการสอบประเมินผลสัมฤทธิ์แล้ว</span>';
    
    status.style.background = 'rgba(61,220,132,0.08)';
    status.style.border = '1px solid rgba(61,220,132,0.25)';
    status.style.color = '#3ddc84';
    status.innerHTML = `🏆 <strong>EXAM CLEARED!</strong> คุณผ่านการประเมินวิชา Linux & Windows OS Security เรียบร้อย (คะแนน 5/5) ยอดเยี่ยมมากครับ!
    <div class="w-expl-box">
      <div class="w-expl-q">🔑 เฉลยข้อที่ 1 (Kernel Architecture)</div>
      <p class="w-expl-a">คำตอบคือ **A** เพราะ Linux เคอร์เนลเป็น Monolithic Kernel ขณะที่ Windows NT ใช้แนวคิด Microkernel แบบลูกผสม (Hybrid Kernel)</p>
    </div>
    <div class="w-expl-box">
      <div class="w-expl-q">🔑 เฉลยข้อที่ 2 (Linux chmod)</div>
      <p class="w-expl-a">คำตอบคือ **C** เพราะสิทธิ์ 700 ถอดรหัสฐานแปดได้เป็น rwx------ หมายถึง เจ้าของไฟล์ได้สิทธิ์อ่านเขียนและรันครบถ้วนคนเดียว</p>
    </div>
    <div class="w-expl-box">
      <div class="w-expl-q">🔑 เฉลยข้อที่ 3 (Windows NTFS permissions)</div>
      <p class="w-expl-a">คำตอบคือ **D** เพราะกฎการสั่งปฏิเสธสิทธิ์แบบระบุชัดเจน (Explicit Deny) จะมีน้ำหนักและความสำคัญสูงสุดเสมอ</p>
    </div>
    <div class="w-expl-box">
      <div class="w-expl-q">🔑 เฉลยข้อที่ 4 (Environment Variables)</div>
      <p class="w-expl-a">คำตอบคือ **B** เพราะตัวแปรระบบ %PATH% เก็บรายการพาธที่ระบบปฏิบัติการใช้สืบค้นหาไฟล์รันโปรแกรมเมื่อผู้ใช้ป้อนคำสั่งเข้ามาใน CMD</p>
    </div>
    <div class="w-expl-box">
      <div class="w-expl-q">🔑 เฉลยข้อที่ 5 (Peripherals)</div>
      <p class="w-expl-a">คำตอบคือ **B** เพราะตามปรัชญาของ Unix/Linux "Everything is a file" ทุกอุปกรณ์จะถูกเข้าถึงในฐานะไฟล์ย่อยบน /dev</p>
    </div>`;
    
    localStorage.setItem('solved_lesson_197', 'solved');
    if (typeof updateProgressUI === 'function') updateProgressUI();
    fetch('/api/v1/tutorials/progress', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'CSRF-Token': window.init.csrfNonce
      },
      body: JSON.stringify({
        lesson_id: 197,
        type: 'quiz',
        item_key: 'quick_quiz',
        solved: true
      })
    }).catch(e => console.error("Error syncing progress:", e));

    groups.forEach(function(g) {
      g.querySelectorAll('.mini-opt').forEach(function(o) {
        o.style.pointerEvents = 'none';
      });
    });
    box.querySelector('.mq-btn-check').disabled = true;
  } else {
    var errorPct = Math.round((score / groups.length) * 100);
    if (fill) { fill.setAttribute('stroke-dasharray', errorPct + ', 100'); fill.style.stroke = '#ff007f'; }
    if (text) text.textContent = errorPct + '%';
    if (status_txt) status_txt.textContent = 'ตอบไม่ถูกต้องทั้งหมด ลองใหม่!';

    status.style.background = 'rgba(255,0,127,0.08)';
    status.style.border = '1px solid rgba(255,0,127,0.25)';
    status.style.color = '#ff007f';
    status.innerHTML = '❌ <strong>ยังไม่ผ่านเกณฑ์!</strong> คุณได้คะแนน ' + score + '/5 (ต้องถูกครบ 5 ข้อเพื่อทำ Lesson Clear) กรุณาทบทวนบทเรียนและตรวจเลือกคำตอบใหม่อีกครั้ง';
  }
}

// Load saved state
setTimeout(function() {
  var solved = localStorage.getItem('solved_lesson_197');
  if (solved === 'solved') {
    var box = document.getElementById('mq-box-197');
    var groups = box.querySelectorAll('.mq-q');
    groups.forEach(function(g) {
      var correctVal = g.getAttribute('data-correct');
      g.querySelectorAll('.mini-opt').forEach(function(o) {
        var val = o.getAttribute('data-val');
        if (val === correctVal) {
          o.classList.add('selected', 'correct');
        }
        o.style.pointerEvents = 'none';
      });
    });
    box.querySelector('.mq-btn-check').disabled = true;
    
    var fill = document.getElementById('lesson-gauge-fill-197');
    var text = document.getElementById('lesson-gauge-text-197');
    var status_txt = document.getElementById('lesson-status-txt-197');
    var status = document.getElementById('mq-status-197');
    
    if (fill) { fill.setAttribute('stroke-dasharray', '100, 100'); fill.style.stroke = '#3ddc84'; }
    if (text) text.textContent = '100%';
    if (status_txt) status_txt.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ผ่านการสอบประเมินผลสัมฤทธิ์แล้ว</span>';
    
    status.style.display = 'block';
    status.style.background = 'rgba(61,220,132,0.08)';
    status.style.border = '1px solid rgba(61,220,132,0.25)';
    status.style.color = '#3ddc84';
    status.innerHTML = `🏆 <strong>EXAM CLEARED!</strong> คุณผ่านการประเมินวิชา Linux & Windows OS Security เรียบร้อย (คะแนน 5/5) ยอดเยี่ยมมากครับ!
    <div class="w-expl-box">
      <div class="w-expl-q">🔑 เฉลยข้อที่ 1 (Kernel Architecture)</div>
      <p class="w-expl-a">คำตอบคือ **A** เพราะ Linux เคอร์เนลเป็น Monolithic Kernel ขณะที่ Windows NT ใช้แนวคิด Microkernel แบบลูกผสม (Hybrid Kernel)</p>
    </div>
    <div class="w-expl-box">
      <div class="w-expl-q">🔑 เฉลยข้อที่ 2 (Linux chmod)</div>
      <p class="w-expl-a">คำตอบคือ **C** เพราะสิทธิ์ 700 ถอดรหัสฐานแปดได้เป็น rwx------ หมายถึง เจ้าของไฟล์ได้สิทธิ์อ่านเขียนและรันครบถ้วนคนเดียว</p>
    </div>
    <div class="w-expl-box">
      <div class="w-expl-q">🔑 เฉลยข้อที่ 3 (Windows NTFS permissions)</div>
      <p class="w-expl-a">คำตอบคือ **D** เพราะกฎการสั่งปฏิเสธสิทธิ์แบบระบุชัดเจน (Explicit Deny) จะมีน้ำหนักและความสำคัญสูงสุดเสมอ</p>
    </div>
    <div class="w-expl-box">
      <div class="w-expl-q">🔑 เฉลยข้อที่ 4 (Environment Variables)</div>
      <p class="w-expl-a">คำตอบคือ **B** เพราะตัวแปรระบบ %PATH% เก็บรายการพาธที่ระบบปฏิบัติการใช้สืบค้นหาไฟล์รันโปรแกรมเมื่อผู้ใช้ป้อนคำสั่งเข้ามาใน CMD</p>
    </div>
    <div class="w-expl-box">
      <div class="w-expl-q">🔑 เฉลยข้อที่ 5 (Peripherals)</div>
      <p class="w-expl-a">คำตอบคือ **B** เพราะตามปรัชญาของ Unix/Linux "Everything is a file" ทุกอุปกรณ์จะถูกเข้าถึงในฐานะไฟล์ย่อยบน /dev</p>
    </div>`;
  }
}, 200);
</script>
"""
    return html

with app.app_context():
    lesson = app.db.session.query(TutorialLesson).filter_by(id=197).first()
    if lesson:
        try:
            blocks = json.loads(lesson.content)
            # Upgrades Block 1
            blocks[1]['value'] = make_lesson_197_html()
            lesson.content = json.dumps(blocks, ensure_ascii=False)
            app.db.session.commit()
            print("Successfully migrated Lesson ID 197 Final Exam to Style 1 Layout with Gauge!")
        except Exception as e:
            print(f"Error: {e}")
