import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    # Query lesson 165
    lesson = db.session.query(TutorialLesson).filter_by(id=165).first()
    if lesson:
        blocks = json.loads(lesson.content)
        
        # Overwrite Block 20 with clean triple-quoted string
        blocks[20]['value'] = """---
### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

น้องๆ เรียนจบเนื้อหาบทนี้แล้ว มาลองทดสอบฝีมือตอบคำถามประเมินความรู้ 4 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนกันหน่อยนะครับ! (ถ้าจิ้มครบทุกข้อแล้วกดตรวจคำตอบได้เลยนะ) 🎯👇

<style>
.mini-quiz-box{width:100%;max-width:1050px;margin:2rem auto;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:24px;box-shadow:0 8px 32px rgba(0,0,0,0.3);box-sizing:border-box;}
.mq-q{margin-bottom:28px;}
.mq-intro{font-size:0.82rem;color:#8a94a6;line-height:1.5;margin-bottom:6px;background:rgba(255,255,255,0.02);padding:6px 12px;border-radius:6px;border-left:3px solid #00f0ff;}
.mq-title{font-size:0.92rem;font-weight:800;color:#e2e8f0;margin-bottom:12px;line-height:1.6;}
.mq-title span{color:#00f0ff;font-family:'JetBrains Mono',monospace;margin-right:6px;}
.mini-opts{display:flex;flex-direction:column;gap:8px;}
.mini-opt{display:flex;align-items:center;gap:12px;padding:12px 16px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.05);border-radius:8px;cursor:pointer;transition:all 0.15s ease;user-select:none;font-size:0.85rem;color:#cbd5e1;line-height:1.4;}
.mini-opt:hover{border-color:rgba(0,240,255,0.25);background:rgba(0,240,255,0.02);}
.mini-opt.selected{border-color:#00f0ff;background:rgba(0,240,255,0.08);color:#ffffff;box-shadow:0 0 10px rgba(0,240,255,0.15);}
.mini-opt.correct{border-color:#3ddc84;background:rgba(61,220,132,0.08);color:#ffffff;}
.mini-opt.incorrect{border-color:#ff007f;background:rgba(255,0,127,0.08);color:#ffffff;}
.mini-bullet{width:18px;height:18px;border:1px solid rgba(255,255,255,0.3);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.6rem;font-weight:bold;flex-shrink:0;}
.mini-opt.selected .mini-bullet{border-color:#00f0ff;background:#00f0ff;color:#070910;}
.mq-layout-container {display:flex; gap:24px; align-items:stretch;}
.mq-questions-col {flex:1;}
.mq-gauge-col {width:180px; display:flex; flex-direction:column; align-items:center; justify-content:center; border-left:1px solid rgba(255,255,255,0.06); padding-left:24px;}
@media (max-width: 768px) {
  .mq-layout-container {flex-direction:column;}
  .mq-gauge-col {width:100%; border-left:none; padding-left:0; border-top:1px solid rgba(255,255,255,0.06); padding-top:24px;}
}
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:url(#gauge-grad-2); stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease; filter:drop-shadow(0 0 5px rgba(0,240,255,0.4));}
.neon-gauge-text {fill:#ffffff; font-family:'JetBrains Mono',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}
.mq-btn-check{padding:12px 24px;background:#00f0ff;border:none;border-radius:6px;font-family:'JetBrains Mono',monospace;font-size:0.85rem;font-weight:800;color:#070910;cursor:pointer;box-shadow:0 0 10px rgba(0,240,255,0.25);transition:all 0.15s ease;margin-top:16px;}
.mq-btn-check:hover{background:#ffffff;box-shadow:0 0 15px rgba(255,255,255,0.4);transform:translateY(-1px);}
.mq-status-bar{display:none;padding:12px 16px;border-radius:8px;font-size:0.85rem;margin-top:16px;font-weight:700;line-height:1.5;}
</style>

<div id="mq-box-2" class="mini-quiz-box">
<div class="mq-layout-container">
<div class="mq-questions-col">

<!-- Question 1 -->
<div class="mq-q" data-correct="B">
<div class="mq-intro">📝 เกริ่นเรื่อง: เวลาเราติดตั้งแอปพลิเคชันหรือเซ็ตอัปเครื่องเซิร์ฟเวอร์ในลินุกซ์ ไฟล์กำหนดค่าและรหัสผ่านต่างๆ จะต้องถูกนำไปเซฟรวมกันเป็นที่เป็นทางอย่างเป็นระเบียบ...</div>
<div class="mq-title"><span>Q1.</span> น้องๆ คิดว่าในระบบไฟล์ของลินุกซ์ ไดเรกทอรีใดทำหน้าที่รวบรวมไฟล์ Configuration (ตั้งค่าหลัก) ทั้งหมดของระบบคอมพิวเตอร์และโปรแกรมต่างๆ ครับ?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A" onclick="updateMiniProgress(2)"><span class="mini-bullet">A</span>/bin (กล่องเก็บคำสั่งพื้นฐาน)</div>
<div class="mini-opt" data-val="B" onclick="updateMiniProgress(2)"><span class="mini-bullet">B</span>/etc (กล่องเก็บไฟล์คอนฟิกูเรชัน)</div>
<div class="mini-opt" data-val="C" onclick="updateMiniProgress(2)"><span class="mini-bullet">C</span>/var (กล่องเก็บไฟล์ข้อมูลแปรผัน)</div>
<div class="mini-opt" data-val="D" onclick="updateMiniProgress(2)"><span class="mini-bullet">D</span>/dev (กล่องเก็บไฟล์จำลองอุปกรณ์)</div>
</div>
</div>

<!-- Question 2 -->
<div class="mq-q" data-correct="C">
<div class="mq-intro">📝 เกริ่นเรื่อง: ลินุกซ์มีกฎเหล็กที่เด็กไซเบอร์ต้องจำให้ขึ้นใจเลยคือ "ทุกสิ่งทุกอย่างคือไฟล์ (Everything is a file)" ไม่ว่าจะเป็นฮาร์ดดิสก์ แฟลชไดรฟ์ USB แป้นพิมพ์ หรือพอร์ตอุปกรณ์เชื่อมต่อจริง...</div>
<div class="mq-title"><span>Q2.</span> น้องๆ จำได้ไหมว่าอุปกรณ์กายภาพภายนอกคอมพิวเตอร์เหล่านี้ จะถูกแสดงผลในระบบปฏิบัติการให้อยู่ในรูปของไฟล์อุปกรณ์ (Device Files) ที่โฟลเดอร์ใดครับ?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A" onclick="updateMiniProgress(2)"><span class="mini-bullet">A</span>ถูกแปลงเป็นไฟล์ชั่วคราวซ่อนใน /tmp</div>
<div class="mini-opt" data-val="B" onclick="updateMiniProgress(2)"><span class="mini-bullet">B</span>ถูกแสดงเป็นโปรแกรมช่วยบูตเครื่องใน /boot</div>
<div class="mini-opt" data-val="C" onclick="updateMiniProgress(2)"><span class="mini-bullet">C</span>ถูกแสดงเป็นไฟล์จำลองฮาร์ดแวร์ใน /dev</div>
<div class="mini-opt" data-val="D" onclick="updateMiniProgress(2)"><span class="mini-bullet">D</span>ถูกแปลงเป็นคู่มือคำสั่งช่วยเหลือใน /usr/share</div>
</div>
</div>

<!-- Question 3 -->
<div class="mq-q" data-correct="A">
<div class="mq-intro">📝 เกริ่นเรื่อง: ในระบบปฏิบัติการ (OS) จะมีสองคู่หูหลักที่มาจาก OS ทำงานช่วยกัน โดยฝ่ายหนึ่งคอยคุยรับคำสั่งกับเราเพื่อจดรายการไปส่งให้อีกฝ่ายที่เป็นแกนกลางคอยคุมเครื่องยนต์และชิปในคอมทำงาน...</div>
<div class="mq-title"><span>Q3.</span> ข้อใดที่น้องๆ คิดว่าอธิบายหน้าที่การประสานงานและการแบ่งบทบาทระหว่าง Shell และ Kernel ได้อย่างถูกต้องและเข้าใจง่ายที่สุดครับ?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A" onclick="updateMiniProgress(2)"><span class="mini-bullet">A</span>Shell เป็นเด็กเสิร์ฟรับคำสั่งภาษาคนแล้วส่งต่อให้ Kernel ซึ่งเป็นเชฟใหญ่ในครัวคุมเตาฮาร์ดแวร์ทำงาน</div>
<div class="mini-opt" data-val="B" onclick="updateMiniProgress(2)"><span class="mini-bullet">B</span>Shell เป็นฮาร์ดแวร์ตัวกระทะ ส่วน Kernel เป็นโปรแกรมเบราว์เซอร์เปิดหาข้อมูล</div>
<div class="mini-opt" data-val="C" onclick="updateMiniProgress(2)"><span class="mini-bullet">C</span>Shell เป็นสมองส่วนลึกคุมแรม ส่วน Kernel เป็นปุ่มแป้นคีย์บอร์ดให้เราจิ้มอย่างเดียว</div>
<div class="mini-opt" data-val="D" onclick="updateMiniProgress(2)"><span class="mini-bullet">D</span>ทั้ง Shell และ Kernel ทำหน้าที่เหมือนกันคือสร้างไฟล์แคชชั่วคราวรันโปรแกรมความบันเทิง</div>
</div>
</div>

<!-- Question 4 -->
<div class="mq-q" data-correct="D">
<div class="mq-intro">📝 เกริ่นเรื่อง: เพื่อป้องกันไม่ให้แอปพลิเคชันที่โดนแฮกสามารถคุมเครื่องคอมพิวเตอร์ของเราได้ทั้งหมด ระบบจึงทำกลไกแยกส่วนแบ่งสิทธิ์การทำงานออกจากกัน (Privilege Separation) โดยสร้างยูสเซอร์เฉพาะงานขึ้นมา...</div>
<div class="mq-title"><span>Q4.</span> การรันโปรแกรมบริการหลังบ้าน เช่น บริการเว็บไซต์ด้วยบัญชี Service User (System User) ช่วยเพิ่มความปลอดภัยให้ระบบเครือข่ายอย่างไรครับ?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A" onclick="updateMiniProgress(2)"><span class="mini-bullet">A</span>ช่วยเปิดสิทธิ์ให้แฮกเกอร์ล็อกอินเข้ามาพิมพ์คำสั่ง Root ยึดครองระบบจากภายนอกได้เร็วขึ้น</div>
<div class="mini-opt" data-val="B" onclick="updateMiniProgress(2)"><span class="mini-bullet">B</span>ช่วยเก็บประวัติล็อกเหตุการณ์การเปิดเครื่องและการคำนวณทั้งหมดไว้ในโฟลเดอร์ /mnt</div>
<div class="mini-opt" data-val="C" onclick="updateMiniProgress(2)"><span class="mini-bullet">C</span>ช่วยให้ผู้ใช้ทั่วไปเปิดแก้สิทธิ์ไฟล์งานของคนอื่นได้โดยไม่มีกฎการจำกัดความเป็นส่วนตัว</div>
<div class="mini-opt" data-val="D" onclick="updateMiniProgress(2)"><span class="mini-bullet">D</span>จำกัดสิทธิ์เฉพาะงาน หากบริการโดนเจาะ แฮกเกอร์จะได้สิทธิ์จำกัดแค่บอทบริการนั้นและขยายสิทธิ์ไปยึดครองระดับ Root ไม่ได้</div>
</div>
</div>

<button class="mq-btn-check" onclick="checkMiniQuiz(2)">Check Answers / ตรวจคำตอบ</button>
<div id="mq-status-2" class="mq-status-bar"></div>
</div>

<div class="mq-gauge-col">
<span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em; text-align:center;">Lesson Progress</span>
<div class="neon-gauge-container">
<svg class="neon-gauge" viewBox="0 0 36 36">
<defs>
<linearGradient id="gauge-grad-2" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#ff007f" />
<stop offset="50%" stop-color="#fbbf24" />
<stop offset="100%" stop-color="#00f0ff" />
</linearGradient>
</defs>
<path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
<path class="neon-gauge-fill" id="lesson-gauge-fill-2" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
<text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text-2">0%</text>
</svg>
</div>
<span id="lesson-status-txt-2" class="mt-3 d-block text-muted" style="font-size:0.78rem; text-align:center;">โปรดตอบคำถามให้ครบ 4 ข้อ</span>
</div>
</div>
</div>

<script>
document.querySelectorAll('#mq-box-2 .mini-opt').forEach(opt => {
  opt.addEventListener('click', function() {
    const parent = this.closest('.mq-q');
    parent.querySelectorAll('.mini-opt').forEach(o => o.classList.remove('selected'));
    this.classList.add('selected');
  });
});
function updateMiniProgress(lnum) {
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
      status.innerHTML = '<span style="color:#00f0ff; font-weight:bold;">กรุณากดตรวจคำตอบ</span>';
    } else if (pct > 0) {
      status.textContent = 'ตอบคำถามแล้ว ' + answeredCount + '/' + qGroups.length + ' ข้อ';
    } else {
      status.textContent = 'โปรดตอบคำถามให้ครบ ' + qGroups.length + ' ข้อ';
    }
  }
}
function checkMiniQuiz(lnum) {
  const box = document.getElementById('mq-box-' + lnum);
  const groups = box.querySelectorAll('.mq-q');
  let score = 0;
  let allAnswered = true;
  groups.forEach(g => {
    const selected = g.querySelector('.mini-opt.selected');
    if (!selected) allAnswered = false;
  });
  if (!allAnswered) {
    alert("กรุณาตอบคำถามท้ายบทให้ครบถ้วนทั้ง 4 ข้อก่อนส่งตรวจคำตอบครับ!");
    return;
  }
  groups.forEach(g => {
    const correctVal = g.getAttribute('data-correct');
    const selected = g.querySelector('.mini-opt.selected');
    const selectedVal = selected.getAttribute('data-val');
    g.querySelectorAll('.mini-opt').forEach(o => {
      o.classList.remove('correct', 'incorrect');
      const val = o.getAttribute('data-val');
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
  const status = document.getElementById('mq-status-' + lnum);
  status.style.display = 'block';
  if (score === 4) {
    if (fill) { fill.setAttribute('stroke-dasharray', '100, 100'); fill.style.stroke = '#3ddc84'; }
    if (text) text.textContent = '100%';
    if (status_txt) status_txt.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
    status.style.background = 'rgba(61,220,132,0.08)';
    status.style.border = '1px solid rgba(61,220,132,0.25)';
    status.style.color = '#3ddc84';
    status.innerHTML = '🏆 <strong>LESSON CLEARED!</strong> คุณผ่านการประเมินความรู้ท้ายบทเรียนย่อยนี้เรียบร้อย (คะแนน 4/4) สามารถเดินทางไปศึกษาบทเรียนถัดไปได้ครับ!';
  } else {
    const errorPct = Math.round((score / groups.length) * 100);
    if (fill) { fill.setAttribute('stroke-dasharray', errorPct + ', 100'); fill.style.stroke = '#ff007f'; }
    if (text) text.textContent = errorPct + '%';
    if (status_txt) status_txt.textContent = 'ตอบไม่ถูกต้อง ลองใหม่!';
    status.style.background = 'rgba(255,0,127,0.08)';
    status.style.border = '1px solid rgba(255,0,127,0.25)';
    status.style.color = '#ff007f';
    status.innerHTML = '❌ <strong>ยังไม่ผ่าน!</strong> คุณได้คะแนน ' + score + '/4 (ทำข้อสอบไม่ผ่าน) กรุณาทบทวนบทเรียนและตรวจเลือกคำตอบใหม่อีกครั้ง';
  }
}
</script>"""
        
        lesson.content = json.dumps(blocks, ensure_ascii=False)
        db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
        db.session.commit()
        print("Lesson 165 Block 20 successfully updated using clean python triple-quotes!")
    else:
        print("Error: Lesson 165 not found!")
