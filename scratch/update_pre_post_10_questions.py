import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialModule, TutorialLesson

app = create_app()

def make_style1_exam_html(lid, title_exam, is_pre, questions_list):
    label_prefix = "ก่อนเรียน" if is_pre else "หลังเรียน"
    title_head = f"แบบทดสอบ{label_prefix} (Pre-test)" if is_pre else f"แบบทดสอบ{label_prefix} (Post-test)"
    comment_success = f"🏆 <strong>ประเมินผลสำเร็จ!</strong> คุณทำการทดสอบ{label_prefix}เสร็จเรียบร้อยแล้ว!"
    
    q_groups_html = ""
    for idx, qd in enumerate(questions_list):
        num = idx + 1
        opts_html = ""
        for letter, text in qd["opts"]:
            opts_html += f'<div class="mini-opt" data-val="{letter}"><span class="mini-bullet">{letter}</span> {text}</div>\n'
            
        q_groups_html += f"""
<div class="mq-q" data-correct="{qd['correct']}">
<div class="mq-title"><span>Q{num}.</span> {qd['q']}</div>
<div class="mini-opts">
{opts_html}</div>
</div>
"""

    N = len(questions_list)

    html = f"""### 📊 {title_exam}

ทำแบบทดสอบประเมินความรู้{label_prefix} {N} ข้อด้านล่างนี้เพื่อวัดระดับความสามารถพื้นฐานของตนเอง (หลังจากกดยืนยันคำตอบแล้ว ระบบจะทำเครื่องหมายผ่านบททดสอบเพื่อใช้เปรียบเทียบผลลัพธ์ระดับชั้นเรียน):

<style>
.mini-quiz-box{{width:100%;max-width:1050px;margin:2rem auto;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:24px;box-shadow:0 8px 32px rgba(0,0,0,0.3);box-sizing:border-box;}}
.mq-layout-container {{display:flex; gap:24px; align-items:stretch;}}
.mq-questions-col {{flex:1;}}
.mq-gauge-col {{width:160px; display:flex; flex-direction:column; align-items:center; justify-content:center; border-left:1px solid rgba(255,255,255,0.06); padding-left:24px;}}
@media (max-width: 768px) {{
  .mq-layout-container {{flex-direction:column;}}
  .mq-gauge-col {{width:100%; border-left:none; padding-left:0; border-top:1px solid rgba(255,255,255,0.06); padding-top:24px;}}
}}
.neon-gauge-container {{position:relative; width:120px; height:120px;}}
.neon-gauge {{width:100%; height:100%;}}
.neon-gauge-bg {{fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}}
.neon-gauge-fill {{fill:none; stroke:url(#gauge-grad-{lid}); stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease; filter:drop-shadow(0 0 5px rgba(0,240,255,0.4));}}
.neon-gauge-text {{fill:#ffffff; font-family:'JetBrains Mono',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}}

.mq-q{{margin-bottom:20px;}}
.mq-title{{font-size:0.9rem;font-weight:800;color:#e2e8f0;margin-bottom:10px;}}
.mq-title span{{color:#00f0ff;font-family:'JetBrains Mono',monospace;margin-right:6px;}}
.mini-opts{{display:flex;flex-direction:column;gap:6px;}}
.mini-opt{{display:flex;align-items:center;gap:10px;padding:10px 14px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.05);border-radius:8px;cursor:pointer;transition:all 0.15s ease;user-select:none;font-size:0.83rem;color:#cbd5e1;}}
.mini-opt:hover{{border-color:rgba(0,240,255,0.2);background:rgba(0,240,255,0.02);}}
.mini-opt.selected{{border-color:#00f0ff;background:rgba(0,240,255,0.08);color:#ffffff;}}
.mini-opt.correct{{border-color:#3ddc84;background:rgba(61,220,132,0.08);color:#ffffff;}}
.mini-opt.incorrect{{border-color:#ff007f;background:rgba(255,0,127,0.08);color:#ffffff;}}
.mini-bullet{{width:15px;height:15px;border:1px solid rgba(255,255,255,0.3);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.58rem;font-weight:bold;}}
.mini-opt.selected .mini-bullet{{border-color:#00f0ff;background:#00f0ff;color:#070910;}}

.mq-btn-check{{padding:10px 20px;background:#00f0ff;border:none;border-radius:6px;font-family:'JetBrains Mono',monospace;font-size:0.82rem;font-weight:800;color:#070910;cursor:pointer;box-shadow:0 0 10px rgba(0,240,255,0.25);transition:all 0.15s ease;}}
.mq-btn-check:hover{{background:#ffffff;box-shadow:0 0 15px rgba(255,255,255,0.4);transform:translateY(-1px);}}
.mq-status-bar{{display:none;padding:12px 16px;border-radius:8px;font-size:0.85rem;margin-top:16px;font-weight:700;line-height:1.5;}}
</style>

<div id="mq-box-{lid}" class="mini-quiz-box">
<div class="mq-layout-container">
<div class="mq-questions-col">
{q_groups_html}
<button class="mq-btn-check" onclick="checkMiniQuiz{lid}({lid})">Submit Test / ส่งคำตอบ</button>
<div id="mq-status-{lid}" class="mq-status-bar"></div>
</div>

<div class="mq-gauge-col">
  <span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em; text-align:center;">{label_prefix} Progress</span>
  <div class="neon-gauge-container">
    <svg class="neon-gauge" viewBox="0 0 36 36">
      <defs>
        <linearGradient id="gauge-grad-{lid}" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#ff007f" />
          <stop offset="50%" stop-color="#fbbf24" />
          <stop offset="100%" stop-color="#00f0ff" />
        </linearGradient>
      </defs>
      <path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
      <path class="neon-gauge-fill" id="lesson-gauge-fill-{lid}" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
      <text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text-{lid}">0%</text>
    </svg>
  </div>
  <span id="lesson-status-txt-{lid}" class="mt-3 d-block text-muted" style="font-size:0.78rem; text-align:center;">โปรดตอบคำถามให้ครบ {N} ข้อ</span>
</div>
</div>
</div>

<script>
document.querySelectorAll('#mq-box-{lid} .mini-opt').forEach(function(opt) {{
  opt.addEventListener('click', function() {{
    var parent = this.closest('.mq-q');
    parent.querySelectorAll('.mini-opt').forEach(function(o) {{ o.classList.remove('selected'); }});
    this.classList.add('selected');
    updateMiniProgress{lid}({lid});
  }});
}});

function updateMiniProgress{lid}(lnum) {{
  var box = document.getElementById('mq-box-' + lnum);
  var qGroups = box.querySelectorAll('.mq-q');
  var answeredCount = 0;
  qGroups.forEach(function(g) {{
    if (g.querySelector('.mini-opt.selected')) {{
      answeredCount++;
    }}
  }});
  var pct = Math.round((answeredCount / qGroups.length) * 100);
  var fill = document.getElementById('lesson-gauge-fill-' + lnum);
  var text = document.getElementById('lesson-gauge-text-' + lnum);
  var status = document.getElementById('lesson-status-txt-' + lnum);
  if (fill) fill.setAttribute('stroke-dasharray', pct + ', 100');
  if (text) text.textContent = pct + '%';
  if (status) {{
    if (pct === 100) {{
      status.innerHTML = '<span style="color:#00f0ff; font-weight:bold;">กรุณากดส่งคำตอบ</span>';
    }} else if (pct > 0) {{
      status.textContent = 'ตอบคำถามแล้ว ' + answeredCount + '/' + qGroups.length + ' ข้อ';
    }} else {{
      status.textContent = 'โปรดตอบคำถามให้ครบ ' + qGroups.length + ' ข้อ';
    }}
  }}
}}

function checkMiniQuiz{lid}(lnum) {{
  var box = document.getElementById('mq-box-' + lnum);
  var groups = box.querySelectorAll('.mq-q');
  var score = 0;
  var allAnswered = true;

  groups.forEach(function(g) {{
    var selected = g.querySelector('.mini-opt.selected');
    if (!selected) allAnswered = false;
  }});

  if (!allAnswered) {{
    alert("กรุณาตอบคำถามให้ครบถ้วนก่อนส่งตรวจคำตอบครับ!");
    return;
  }}

  groups.forEach(function(g) {{
    var correctVal = g.getAttribute('data-correct');
    var selected = g.querySelector('.mini-opt.selected');
    var selectedVal = selected.getAttribute('data-val');

    g.querySelectorAll('.mini-opt').forEach(function(o) {{
      o.classList.remove('correct', 'incorrect');
      var val = o.getAttribute('data-val');
      if (val === correctVal) {{
        o.classList.add('correct');
      }} else if (o.classList.contains('selected')) {{
        o.classList.add('incorrect');
      }}
    }});

    if (selectedVal === correctVal) score++;
  }});

  var fill = document.getElementById('lesson-gauge-fill-' + lnum);
  var text = document.getElementById('lesson-gauge-text-' + lnum);
  var status_txt = document.getElementById('lesson-status-txt-' + lnum);
  var status = document.getElementById('mq-status-' + lnum);
  status.style.display = 'block';

  if (fill) {{ fill.setAttribute('stroke-dasharray', '100, 100'); fill.style.stroke = '#3ddc84'; }}
  if (text) text.textContent = '100%';
  if (status_txt) status_txt.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
  
  status.style.background = 'rgba(61,220,132,0.08)';
  status.style.border = '1px solid rgba(61,220,132,0.25)';
  status.style.color = '#3ddc84';
  status.innerHTML = `{comment_success} (ทำได้ถูกต้องทั้งหมด หรือบันทึกคะแนนเฉลี่ย ${{score}}/{N} เป็นคะแนนฐานเรียบร้อย!)`;
  
  localStorage.setItem('solved_lesson_{lid}', 'solved');
  if (typeof updateProgressUI === 'function') updateProgressUI();
  fetch('/api/v1/tutorials/progress', {{
    method: 'POST',
    headers: {{
      'Content-Type': 'application/json',
      'CSRF-Token': window.init.csrfNonce
    }},
    body: JSON.stringify({{
      lesson_id: {lid},
      type: 'quiz',
      item_key: 'quick_quiz',
      solved: true
    }})
  }}).catch(e => console.error("Error syncing progress:", e));

  groups.forEach(function(g) {{
    g.querySelectorAll('.mini-opt').forEach(function(o) {{
      o.style.pointerEvents = 'none';
    }});
  }});
  box.querySelector('.mq-btn-check').disabled = true;
}}

setTimeout(function() {{
  var solved = localStorage.getItem('solved_lesson_{lid}');
  if (solved === 'solved') {{
    var box = document.getElementById('mq-box-' + {lid});
    var groups = box.querySelectorAll('.mq-q');
    groups.forEach(function(g) {{
      var correctVal = g.getAttribute('data-correct');
      g.querySelectorAll('.mini-opt').forEach(function(o) {{
        var val = o.getAttribute('data-val');
        if (val === correctVal) {{
          o.classList.add('selected', 'correct');
        }}
        o.style.pointerEvents = 'none';
      }});
    }});
    box.querySelector('.mq-btn-check').disabled = true;
    
    var fill = document.getElementById('lesson-gauge-fill-' + {lid});
    var text = document.getElementById('lesson-gauge-text-' + {lid});
    var status_txt = document.getElementById('lesson-status-txt-' + {lid});
    var status = document.getElementById('mq-status-' + {lid});
    
    if (fill) {{ fill.setAttribute('stroke-dasharray', '100, 100'); fill.style.stroke = '#3ddc84'; }}
    if (text) text.textContent = '100%';
    if (status_txt) status_txt.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ผ่านการทดสอบแล้ว</span>';
    
    status.style.display = 'block';
    status.style.background = 'rgba(61,220,132,0.08)';
    status.style.border = '1px solid rgba(61,220,132,0.25)';
    status.style.color = '#3ddc84';
    status.innerHTML = `{comment_success}`;
  }}
}}, 200);
</script>
"""
    return html

# 10 questions per chapter
ch2_qs = [
    {"q": "โครงสร้างของระบบปฏิบัติการ (Kernel Architecture) ข้อใดต่อไปนี้ที่อธิบายลักษณะของ Linux และ Windows ได้ถูกต้อง?", "opts": [("A", "Linux เป็น Monolithic Kernel / Windows NT เป็น Hybrid Kernel"), ("B", "Linux เป็น Microkernel / Windows NT เป็น Monolithic Kernel"), ("C", "Linux เป็น Hybrid Kernel / Windows NT เป็น Microkernel"), ("D", "ทั้งคู่มีสถาปัตยกรรมแบบ Exo-kernel เหมือนกันเพื่อเน้นประสิทธิภาพ")], "correct": "A"},
    {"q": "หากผู้ดูแลระบบต้องการตั้งสิทธิ์การเข้าถึงสคริปต์เพื่อให้ \"เจ้าของไฟล์คนเดียวเท่านั้นที่สามารถอ่าน เขียน และรันสคริปต์นี้ได้\" ควรเลือกตั้งค่าสิทธิ์ข้อใด?", "opts": [("A", "chmod 777 script.sh"), ("B", "chmod 755 script.sh"), ("C", "chmod 700 script.sh"), ("D", "chmod 644 script.sh")], "correct": "C"},
    {"q": "เมื่อมีการตรวจสอบสิทธิ์เข้าถึงไฟล์ในระบบปฏิบัติการ Windows (NTFS Permissions) สิทธิ์ในข้อใดมีลำดับความสำคัญสูงสุดและจะถูกบังคับใช้ก่อนเสมอ?", "opts": [("A", "Explicit Allow (สิทธิ์อนุญาตโดยตรง)"), ("B", "Inherited Allow (สิทธิ์อนุญาตที่สืบทอดมา)"), ("C", "Inherited Deny (สิทธิ์ปฏิเสธที่สืบทอดมา)"), ("D", "Explicit Deny (สิทธิ์ปฏิเสธโดยตรง)")], "correct": "D"},
    {"q": "ตัวแปรสภาพแวดล้อม (Environment Variable) มาตรฐานใดในระบบปฏิบัติการ Windows ที่ใช้จัดเก็บรายการพาธระบบที่ใช้สืบค้นโปรแกรมเวลาเรียกใช้งานใน CMD?", "opts": [("A", "%USERPROFILE%"), ("B", "%PATH%"), ("C", "%SYSTEMROOT%"), ("D", "%OS%")], "correct": "B"},
    {"q": "ข้อใดอธิบายความแตกต่างของมุมมองและวิธีการจัดการอุปกรณ์ต่อพ่วง (Peripherals) ใน Linux และ Windows ได้ตรงหลักการ?", "opts": [("A", "Linux มองเป็นพาร์ติชันตัวอักษรดิสก์ (A:, B:) / Windows มองเป็นโหนดการเชื่อมต่อพอร์ต"), ("B", "Linux มองอุปกรณ์ภายนอกเป็น \"ไฟล์ข้อมูลปกติ\" / Windows มองอุปกรณ์เหล่านั้นแยกต่างหากเป็น \"Devices\""), ("C", "Linux มองเป็นหน่วยฮาร์ดแวร์ / Windows มองเป็นไลบรารีระบบเชื่อมร่วม"), ("D", "ไม่มีข้อใดถูก ทั้งคู่จัดการผ่านไดรฟ์ C:\\ และสิทธิ์แอดมินเหมือนกันทุกประการ")], "correct": "B"},
    {"q": "คำสั่งใดใน Linux ใช้เปลี่ยนเจ้าของไฟล์หรือกลุ่มเจ้าของไฟล์?", "opts": [("A", "chown"), ("B", "chmod"), ("C", "chgrp"), ("D", "ls")], "correct": "A"},
    {"q": "ใน Windows Registry, Hive ใดใช้เก็บข้อมูลการตั้งค่าและคอนฟิกูเรชันเฉพาะของผู้ใช้งานปัจจุบันที่ล็อกอินอยู่?", "opts": [("A", "HKEY_CURRENT_USER"), ("B", "HKEY_LOCAL_MACHINE"), ("C", "HKEY_CLASSES_ROOT"), ("D", "HKEY_USERS")], "correct": "A"},
    {"q": "สิทธิ์การอนุญาตใน Linux ค่าสัญลักษณ์ drwxr-xr-x เมื่อแปลงเป็นเลขฐานแปด (Octal) จะได้ค่าใด?", "opts": [("A", "755"), ("B", "644"), ("C", "700"), ("D", "777")], "correct": "A"},
    {"q": "ไฟล์ใดใน Linux ที่เก็บข้อมูลบัญชีรายชื่อผู้ใช้ระบบและเชลล์เริ่มต้น (Default Shell) ของแต่ละคน?", "opts": [("A", "/etc/passwd"), ("B", "/etc/shadow"), ("C", "/etc/group"), ("D", "/etc/hosts")], "correct": "A"},
    {"q": "ใน Windows Security, บัญชีผู้ใช้ที่มีสิทธิ์ในการจัดการระบบสูงสุด (เทียบเท่า root ใน Linux) คือข้อใด?", "opts": [("A", "Administrator"), ("B", "SYSTEM"), ("C", "Guest"), ("D", "User")], "correct": "A"}
]

ch3_qs = [
    {"q": "โครงสร้าง Hello World ข้อใดคือคำสั่งแสดงผลมาตรฐานในภาษา C?", "opts": [("A", "printf(\"Hello World\\n\");"), ("B", "print(\"Hello World\")"), ("C", "echo \"Hello World\""), ("D", "System.out.println(\"Hello World\");")], "correct": "A"},
    {"q": "เครื่องมือใดนิยมใช้รันสคริปต์อัตโนมัติในการทดสอบความปลอดภัยเครือข่ายและสแกนพอร์ตแบบโปรแกรมมิ่ง?", "opts": [("A", "Python (socket library)"), ("B", "HTML5"), ("C", "CSS3"), ("D", "JSON")], "correct": "A"},
    {"q": "ในการเขียนสคริปต์ส่งคำขอ HTTP Request เพื่อข้ามสิทธิ์หรือดึงหน้าเว็บเป้าหมาย นิยมใช้โมดูลหรือคลาสใดของ Python?", "opts": [("A", "requests"), ("B", "math"), ("C", "sys"), ("D", "os")], "correct": "A"},
    {"q": "ในการป้องกันช่องโหว่ประเภท Injection (เช่น SQLi/Command Injection) แนวทางการพัฒนาโค้ดแบบใดมีความปลอดภัยสูงสุด?", "opts": [("A", "Parameterized Queries (Prepared Statements)"), ("B", "การเชื่อมต่อสตริงคำสั่งโดยตรง (String Concatenation)"), ("C", "การใช้ Base64 เข้ารหัสข้อมูลดิบ"), ("D", "การตรวจสอบขนาดตัวอักษรของอินพุตเท่านั้น")], "correct": "A"},
    {"q": "ช่องโหว่ประเภท Buffer Overflow ในภาษา C/C++ มักเกิดจากการใช้งานฟังก์ชันจัดการสตริงข้อใดที่ไม่มีการตรวจสอบขนาดอินพุตก่อนคัดลอกลงเมมโมรี่?", "opts": [("A", "strcpy()"), ("B", "strlen()"), ("C", "strcmp()"), ("D", "printf()")], "correct": "A"},
    {"q": "ใน Python, เมธอดหรือคีย์เวิร์ดใดใช้สำหรับแปลงวัตถุโครงสร้างข้อมูลประเภท Dictionary ให้เป็น JSON String?", "opts": [("A", "json.dumps()"), ("B", "json.loads()"), ("C", "str()"), ("D", "json.parse()")], "correct": "A"},
    {"q": "ลูปประเภทใดในภาษาคอมพิวเตอร์ที่เหมาะสำหรับประมวลผลคำสั่งซ้ำเมื่อทราบจำนวนครั้งที่แน่นอนในการทำงานล่วงหน้า?", "opts": [("A", "for loop"), ("B", "while loop"), ("C", "do-while loop"), ("D", "infinite loop")], "correct": "A"},
    {"q": "ในภาษา Python, ฟังก์ชันใดใช้สำหรับตรวจสอบและรับอินพุตผ่านคีย์บอร์ดจากผู้ใช้งานระบบทางหน้าจอคอนโซล?", "opts": [("A", "input()"), ("B", "print()"), ("C", "sys.argv"), ("D", "read()")], "correct": "A"},
    {"q": "การสร้างการเชื่อมต่อ socket ในภาษา Python เพื่อรอรับการเชื่อมต่อจากภายนอก (Listening) ต้องเรียกใช้เมธอดใดตามลำดับขั้นถัดจาก bind()?", "opts": [("A", "listen()"), ("B", "connect()"), ("C", "accept()"), ("D", "recv()")], "correct": "A"},
    {"q": "ตัวดำเนินการเปรียบเทียบข้อใดในภาษา Python ที่ใช้ทดสอบว่าค่าสองตัวมีค่าเท่ากันหรือไม่?", "opts": [("A", "=="), ("B", "="), ("C", "!="), ("D", "===")], "correct": "A"}
]

ch4_qs = [
    {"q": "ในแบบจำลอง OSI Layer ใดทำหน้าที่ในการกำหนดทิศทางการส่งข้อมูล (Routing)?", "opts": [("A", "Transport Layer"), ("B", "Network Layer (Layer 3)"), ("C", "Data Link Layer"), ("D", "Application Layer")], "correct": "B"},
    {"q": "หากผลลัพธ์ Ping ไปยังเครื่องเป้าหมายมีค่า TTL เริ่มต้นเป็น 128 ระบบปฏิบัติการเป้าหมายมีแนวโน้มเป็นอะไร?", "opts": [("A", "Linux / Unix"), ("B", "Windows"), ("C", "macOS"), ("D", "Cisco Router")], "correct": "B"},
    {"q": "พารามิเตอร์ของ Nmap ตัวใดใช้สำหรับดึงรุ่นซอฟต์แวร์และบริการ (Service Version Detection) บนพอร์ตเป้าหมาย?", "opts": [("A", "-sT"), ("B", "-sS"), ("C", "-sV"), ("D", "-O")], "correct": "C"},
    {"q": "การเปลี่ยนสิทธิ์จากผู้ใช้งานทั่วไป (Normal user) ขึ้นเป็นสิทธิ์ผู้ดูแลระบบ (Root/Admin) เรียกว่าอะไร?", "opts": [("A", "Horizontal Privilege Escalation"), ("B", "Vertical Privilege Escalation"), ("C", "Lateral Movement"), ("D", "Data Exfiltration")], "correct": "B"},
    {"q": "เครื่องมือสแกนเครือข่าย Nmap เมื่อพิมพ์คำสั่งสแกนโดยระบุพารามิเตอร์ -sS จะทำการสแกนรูปแบบใด?", "opts": [("A", "TCP SYN Scan"), ("B", "TCP Connect Scan"), ("C", "UDP Scan"), ("D", "FIN Scan")], "correct": "A"},
    {"q": "เฟรมเวิร์กยอดนิยมที่ใช้ในการรวบรวมช่องโหว่และรันโค้ดเจาะระบบ (Exploit) สำหรับนักทดสอบความปลอดภัยคืออะไร?", "opts": [("A", "Metasploit Framework"), ("B", "Wireshark"), ("C", "Burp Suite"), ("D", "Nessus")], "correct": "A"},
    {"q": "ในขั้นตอนการเจาะระบบ (Exploitation), ส่วนประกอบของโค้ดที่ทำหน้าที่ประมวลผลหลังเจาะระบบสำเร็จ เช่น การส่ง Shell ย้อนกลับมาหาแฮกเกอร์ เรียกว่าอะไร?", "opts": [("A", "Payload (เช่น Reverse Shell)"), ("B", "Exploit"), ("C", "Encoder"), ("D", "NOP Sled")], "correct": "A"},
    {"q": "ช่องโหว่ประเภทใดที่เกิดจากการอนุญาตให้อัปโหลดไฟล์สกุลอันตราย (เช่น .php) ไปรันคำสั่งบนเซิร์ฟเวอร์โดยไม่มีการตรวจสอบ?", "opts": [("A", "Arbitrary File Upload (Remote Code Execution)"), ("B", "SQL Injection"), ("C", "Directory Traversal"), ("D", "Cross-Site Scripting")], "correct": "A"},
    {"q": "บริการยอดนิยมใดที่ทำงานบนพอร์ต 22 และนิยมใช้รีโมตคอนโทรลควบคุมเซิร์ฟเวอร์อย่างปลอดภัย?", "opts": [("A", "SSH"), ("B", "Telnet"), ("C", "FTP"), ("D", "HTTP")], "correct": "A"},
    {"q": "การเจาะระบบในเฟสใดที่มุ่งเน้นการรวบรวมข้อมูลเกี่ยวกับเป้าหมาย (เช่น การหาพอร์ตที่เปิดใช้งานหรือไอพีเป้าหมาย) โดยไม่มีการโจมตีโดยตรง?", "opts": [("A", "Reconnaissance & Information Gathering"), ("B", "Exploitation"), ("C", "Post-Exploitation"), ("D", "Covering Tracks")], "correct": "A"}
]

ch5_qs = [
    {"q": "ช่องโหว่เว็บระดับวิกฤตประเภทใดที่ติดอันดับ OWASP Top 10 ที่เกิดจากการนำข้อมูลอินพุตจากผู้ใช้มารวมกับคำสั่งฐานข้อมูลโดยไม่มีการสกรีน?", "opts": [("A", "Broken Authentication"), ("B", "Injection (SQL Injection / Command Injection)"), ("C", "Cross-Site Scripting (XSS)"), ("D", "Security Misconfiguration")], "correct": "B"},
    {"q": "การโจมตีประเภท SQL Injection เพื่อตรวจสอบว่ามีจำนวนคอลัมน์ในตารางเป้าหมายกี่คอลัมน์ นิยมใช้คำสั่ง SQL ข้อใดรันค้นหา?", "opts": [("A", "ORDER BY"), ("B", "GROUP BY"), ("C", "WHERE"), ("D", "LIMIT")], "correct": "A"},
    {"q": "ช่องโหว่ประเภทใดที่ทำให้แฮกเกอร์สามารถส่งสคริปต์อันตราย (เช่น Javascript) ไปฝังตัวในหน้าเว็บและรันบนเบราว์เซอร์ของเหยื่อรายอื่นได้?", "opts": [("A", "SQL Injection"), ("B", "Cross-Site Scripting (XSS)"), ("C", "Insecure Deserialization"), ("D", "Command Injection")], "correct": "B"},
    {"q": "การตั้งค่า HTTP Header ข้อใดที่ช่วยให้เบราว์เซอร์ตรวจสอบและป้องกันการรันทรัพยากร/สคริปต์ที่อยู่นอกขอบเขตของโดเมนที่ได้รับอนุญาต?", "opts": [("A", "Content-Security-Policy (CSP)"), ("B", "Strict-Transport-Security (HSTS)"), ("C", "X-Frame-Options"), ("D", "Cross-Origin-Resource-Sharing (CORS)")], "correct": "A"},
    {"q": "การโจมตีประเภท SQL Injection เพื่อดึงข้อมูลข้ามตาราง (Combine results) นิยมใช้คีย์เวิร์ด SQL ข้อใดในการเชื่อมตารางคำสั่ง?", "opts": [("A", "UNION"), ("B", "JOIN"), ("C", "GROUP BY"), ("D", "WHERE")], "correct": "A"},
    {"q": "ช่องโหว่ประเภทใดในเว็บแอปพลิเคชันที่เกิดจากเซิร์ฟเวอร์นำพาธพารามิเตอร์ที่กรอกผ่าน URL ไปเรียกเปิดไฟล์ระบบโดยตรง ทำให้แฮกเกอร์สามารถอ่านไฟล์ /etc/passwd ได้?", "opts": [("A", "Directory Traversal (Local File Inclusion - LFI)"), ("B", "Cross-Site Request Forgery (CSRF)"), ("C", "SQL Injection"), ("D", "Broken Object Level Authorization (BOLA)")], "correct": "A"},
    {"q": "พอร์ตมาตรฐานใดที่โปรโตคอล HTTPS ใช้ในการสื่อสารเว็บแบบเข้ารหัสลับอย่างปลอดภัย?", "opts": [("A", "443"), ("B", "80"), ("C", "8080"), ("D", "21")], "correct": "A"},
    {"q": "การป้องกันช่องโหว่ประเภท Cross-Site Scripting (XSS) ในส่วนของการแสดงผลลัพธ์อินพุตที่รับมาจากผู้ใช้งานหน้าเว็บ ควรทำอย่างไรก่อนแสดงผล?", "opts": [("A", "Output Encoding (HTML Entity Encoding)"), ("B", "การเข้ารหัสข้อมูลด้วย MD5"), ("C", "การจำกัดขนาดความยาวสตริงเหลือ 10 ตัวอักษร"), ("D", "การเก็บบันทึกข้อมูลลงใน Session คุกกี้")], "correct": "A"},
    {"q": "คำสั่งประเภทใดใน SQL Injection ที่แฮกเกอร์สามารถนำมาต่อท้ายเพื่อให้เงื่อนไขคำสั่งหลัง WHERE เป็นจริงเสมอ (เช่น OR '1'='1') เพื่อข้ามหน้าล็อกอิน?", "opts": [("A", "Tautology"), ("B", "Union-based"), ("C", "Error-based"), ("D", "Blind Boolean")], "correct": "A"},
    {"q": "ช่องโหว่เว็บประเภทใดที่หลอกให้เหยื่อส่งคำร้องขอกระทำบางอย่างที่เป็นอันตรายโดยที่เหยื่อไม่ได้ตั้งใจ (เช่น แฮกเกอร์แนบลิงก์ให้กดเพื่อแอบโอนเงิน)?", "opts": [("A", "CSRF (Cross-Site Request Forgery)"), ("B", "XSS"), ("C", "SQLi"), ("D", "SSRF (Server-Side Request Forgery)")], "correct": "A"}
]

with app.app_context():
    # Update Chapter 2
    # Pre-test (Lesson 202)
    pre_2 = app.db.session.query(TutorialLesson).filter_by(id=202).first()
    if pre_2:
        blocks = json.loads(pre_2.content)
        blocks[1]['value'] = make_style1_exam_html(pre_2.id, "Linux & Windows OS Security Pre-test (แบบทดสอบก่อนเรียน)", True, ch2_qs)
        pre_2.content = json.dumps(blocks, ensure_ascii=False)
        
    # Post-test (Lesson 197)
    post_2 = app.db.session.query(TutorialLesson).filter_by(id=197).first()
    if post_2:
        blocks = json.loads(post_2.content)
        blocks[1]['value'] = make_style1_exam_html(post_2.id, "Linux & Windows OS Security Post-test (แบบทดสอบหลังเรียน)", False, ch2_qs)
        post_2.content = json.dumps(blocks, ensure_ascii=False)
        
    # Update Chapter 3
    # Pre-test (Lesson 203)
    pre_3 = app.db.session.query(TutorialLesson).filter_by(id=203).first()
    if pre_3:
        blocks = json.loads(pre_3.content)
        blocks[1]['value'] = make_style1_exam_html(pre_3.id, "Programming for Ethical Hacking Pre-test (แบบทดสอบก่อนเรียน)", True, ch3_qs)
        pre_3.content = json.dumps(blocks, ensure_ascii=False)
        
    # Post-test (Lesson 204)
    post_3 = app.db.session.query(TutorialLesson).filter_by(id=204).first()
    if post_3:
        blocks = json.loads(post_3.content)
        blocks[1]['value'] = make_style1_exam_html(post_3.id, "Programming for Ethical Hacking Post-test (แบบทดสอบหลังเรียน)", False, ch3_qs)
        post_3.content = json.dumps(blocks, ensure_ascii=False)
        
    # Update Chapter 4
    # Pre-test (Lesson 205)
    pre_4 = app.db.session.query(TutorialLesson).filter_by(id=205).first()
    if pre_4:
        blocks = json.loads(pre_4.content)
        blocks[1]['value'] = make_style1_exam_html(pre_4.id, "System Exploitations Pre-test (แบบทดสอบก่อนเรียน)", True, ch4_qs)
        pre_4.content = json.dumps(blocks, ensure_ascii=False)
        
    # Post-test (Lesson 206)
    post_4 = app.db.session.query(TutorialLesson).filter_by(id=206).first()
    if post_4:
        blocks = json.loads(post_4.content)
        blocks[1]['value'] = make_style1_exam_html(post_4.id, "System Exploitations Post-test (แบบทดสอบหลังเรียน)", False, ch4_qs)
        post_4.content = json.dumps(blocks, ensure_ascii=False)
        
    # Update Chapter 5
    # Pre-test (Lesson 207)
    pre_5 = app.db.session.query(TutorialLesson).filter_by(id=207).first()
    if pre_5:
        blocks = json.loads(pre_5.content)
        blocks[1]['value'] = make_style1_exam_html(pre_5.id, "Web Exploitations Pre-test (แบบทดสอบก่อนเรียน)", True, ch5_qs)
        pre_5.content = json.dumps(blocks, ensure_ascii=False)
        
    # Post-test (Lesson 208)
    post_5 = app.db.session.query(TutorialLesson).filter_by(id=208).first()
    if post_5:
        blocks = json.loads(post_5.content)
        blocks[1]['value'] = make_style1_exam_html(post_5.id, "Web Exploitations Post-test (แบบทดสอบหลังเรียน)", False, ch5_qs)
        post_5.content = json.dumps(blocks, ensure_ascii=False)

    app.db.session.commit()
    print("Rebuilt all pre-tests and post-tests for Chapters 2-5 with exactly 10 questions each!")
