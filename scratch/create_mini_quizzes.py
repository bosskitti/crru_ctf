import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

# Helper function to generate Interactive Mini-Quiz HTML/JS for each lesson
def make_mini_quiz_html(lesson_num, q1, q1_opts, q1_ans, q2, q2_opts, q2_ans):
    opts1_html = ""
    for idx, opt in enumerate(q1_opts):
        bullet = chr(65 + idx)
        opts1_html += f'<div class="mini-opt" data-val="{bullet}"><span class="mini-bullet">{bullet}</span>{opt}</div>\\n'

    opts2_html = ""
    for idx, opt in enumerate(q2_opts):
        bullet = chr(65 + idx)
        opts2_html += f'<div class="mini-opt" data-val="{bullet}"><span class="mini-bullet">{bullet}</span>{opt}</div>\\n'

    return f"""---
### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการผ่านบทเรียนย่อยนี้ (Lesson Clear):

<style>
.mini-quiz-box{{width:100%;max-width:1050px;margin:2rem auto;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:24px;box-shadow:0 8px 32px rgba(0,0,0,0.3);box-sizing:border-box;}}
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

<div id="mq-box-{lesson_num}" class="mini-quiz-box">
<!-- Question 1 -->
<div class="mq-q" data-correct="{q1_ans}">
<div class="mq-title"><span>Q1.</span> {q1}</div>
<div class="mini-opts">
{opts1_html}</div>
</div>

<!-- Question 2 -->
<div class="mq-q" data-correct="{q2_ans}">
<div class="mq-title"><span>Q2.</span> {q2}</div>
<div class="mini-opts">
{opts2_html}</div>
</div>

<button class="mq-btn-check" onclick="checkMiniQuiz({lesson_num})">Check Answers / ตรวจคำตอบ</button>
<div id="mq-status-{lesson_num}" class="mq-status-bar"></div>
</div>

<script>
// Attach click listeners
document.querySelectorAll('#mq-box-{lesson_num} .mini-opt').forEach(opt => {{
  opt.addEventListener('click', function() {{
    const parent = this.closest('.mq-q');
    parent.querySelectorAll('.mini-opt').forEach(o => o.classList.remove('selected'));
    this.classList.add('selected');
  }});
}});

function checkMiniQuiz(lnum) {{
  const box = document.getElementById('mq-box-' + lnum);
  const groups = box.querySelectorAll('.mq-q');
  let score = 0;
  let allAnswered = true;

  groups.forEach(g => {{
    const selected = g.querySelector('.mini-opt.selected');
    if (!selected) allAnswered = false;
  }});

  if (!allAnswered) {{
    alert("กรุณาตอบคำถามท้ายบทให้ครบถ้วนทั้ง 2 ข้อก่อนส่งตรวจคำตอบครับ!");
    return;
  }}

  groups.forEach(g => {{
    const correctVal = g.getAttribute('data-correct');
    const selected = g.querySelector('.mini-opt.selected');
    const selectedVal = selected.getAttribute('data-val');

    g.querySelectorAll('.mini-opt').forEach(o => {{
      o.classList.remove('correct', 'incorrect');
      const val = o.getAttribute('data-val');
      if (val === correctVal) {{
        o.classList.add('correct');
      }} else if (o.classList.contains('selected')) {{
        o.classList.add('incorrect');
      }}
    }});

    if (selectedVal === correctVal) score++;
  }});

  const status = document.getElementById('mq-status-' + lnum);
  status.style.display = 'block';

  if (score === 2) {{
    status.style.background = 'rgba(61,220,132,0.08)';
    status.style.border = '1px solid rgba(61,220,132,0.25)';
    status.style.color = '#3ddc84';
    status.innerHTML = '🏆 <strong>LESSON CLEARED!</strong> คุณผ่านการประเมินความรู้ท้ายบทเรียนย่อยนี้เรียบร้อย (คะแนน 2/2) สามารถเดินทางไปศึกษาบทเรียนถัดไปได้ครับ!';
  }} else {{
    status.style.background = 'rgba(255,0,127,0.08)';
    status.style.border = '1px solid rgba(255,0,127,0.25)';
    status.style.color = '#ff007f';
    status.innerHTML = '❌ <strong>ยังไม่ผ่าน!</strong> คุณได้คะแนน ' + score + '/2 กรุณาทบทวนบทเรียนและตรวจเลือกคำตอบใหม่อีกครั้งเพื่อผ่านบทเรียนย่อยนี้';
  }}
}}
</script>"""

# ─── Data definitions for quizzes in Lessons 1 to 7 ───
quizzes = {
    164: { # Lesson 1
        "num": 1,
        "q1": "หน้าที่หลักและเป้าหมายสูงสุดของระบบปฏิบัติการ (Operating System) คือข้อใด?",
        "q1_opts": ["จัดเตรียมพื้นที่และเป็นตัวกลางประสานงานฮาร์ดแวร์กับโปรแกรมประยุกต์", "พัฒนาและดีไซน์เว็บไซต์สำเร็จรูปสำหรับผู้ใช้", "ตกแต่งและตกแต่งกราฟิกรูปภาพระดับสูง"],
        "q1_ans": "A",
        "q2": "ส่วนประกอบย่อยใดของ OS ที่ประมวลผลอยู่บนระดับสิทธิ์สูงสุด (Ring 0) และมีสิทธิ์ควบคุมฮาร์ดแวร์โดยตรง?",
        "q2_opts": ["User Mode Applications", "System Services (Background)", "Kernel Mode (เคอร์เนล)"],
        "q2_ans": "C"
    },
    165: { # Lesson 2
        "num": 2,
        "q1": "ในระบบปฏิบัติการ Linux ไดเรกทอรีใดทำหน้าที่รวบรวมไฟล์ Configuration (ไฟล์ตั้งค่าหลัก) ของเครื่องและบริการ?",
        "q1_opts": ["/var (Variable data)", "/etc (System settings)", "/home (User directories)"],
        "q1_ans": "B",
        "q2": "ตามปรัชญาของ Unix/Linux อุปกรณ์ต่อพ่วงภายนอก (Peripherals) ทั้งหมดจะถูกเก็บรักษาและเข้าถึงในตำแหน่งใด?",
        "q2_opts": ["/dev (Device nodes)", "/bin (System executables)", "/usr (User programs)"],
        "q2_ans": "A"
    },
    166: { # Lesson 3
        "num": 3,
        "q1": "สิทธิ์การเข้าถึงแบบสัญลักษณ์ `-rwxr-xr-x` สามารถเปลี่ยนค่าเป็นรหัสฐานแปด (Octal notation) ได้ตรงกับข้อใด?",
        "q1_opts": ["สิทธิ์ระดับ 644", "สิทธิ์ระดับ 755", "สิทธิ์ระดับ 700"],
        "q1_ans": "B",
        "q2": "หากไฟล์โปรแกรมรันตัวหนึ่งติดสิทธิ์พิเศษระดับ SUID เมื่อผู้ใช้ธรรมดาเปิดรันไฟล์นั้น จะประมวลผลด้วยระดับสิทธิ์ของใครชั่วขณะ?",
        "q2_opts": ["ระดับสิทธิ์ของผู้ใช้งานคนนั้นเอง", "ระดับสิทธิ์ของบัญชีเกสต์ชั่วคราว", "ระดับสิทธิ์ของเจ้าของไฟล์ดั้งเดิม (มักเป็น root)"],
        "q2_ans": "C"
    },
    167: { # Lesson 4
        "num": 4,
        "q1": "ปุ่มลัดคีย์ควบคุมใดใน Linux Terminal ที่ทำหน้าที่ส่งสัญญาณยุติการทำงาน (SIGINT) ของโปรแกรมหลักทันที?",
        "q1_opts": ["ปุ่มกด Ctrl-Z", "ปุ่มกด Ctrl-C", "ปุ่มกด Ctrl-D"],
        "q1_ans": "B",
        "q2": "ตัวแปรสภาพแวดล้อมระบบปฏิบัติการ Linux ข้อใดใช้ชี้พิกัดตำแหน่งที่อยู่ของโฮมโฟลเดอร์ของผู้ใช้ปัจจุบัน?",
        "q2_opts": ["ตัวแปร $PATH", "ตัวแปร $USER", "ตัวแปร $HOME"],
        "q2_ans": "C"
    },
    168: { # Lesson 5
        "num": 5,
        "q1": "ในระบบบัญชีความปลอดภัยของ Windows บัญชีข้อใดที่เป็นบัญชีสิทธิ์มาตรฐาน (Standard) แต่มีขอบเขตปกป้องความปลอดภัยพิเศษเพิ่มเติม?",
        "q1_opts": ["Standard Account", "Guest Account", "Child Account (บัญชีสำหรับเด็ก)"],
        "q1_ans": "C",
        "q2": "ในสิทธิ์เข้าใช้ข้อมูล NTFS Permissions หากกลุ่ม User ได้รับสิทธิ์อนุญาตเข้าถึง แต่บัญชีส่วนบุคคลติดสิทธิ์ปฏิเสธเด่นชัด (Explicit Deny) ผลจะเป็นอย่างไร?",
        "q2_opts": ["สิทธิ์ Deny ชนะสิทธิ์อื่น ทำให้เข้าถึงโฟลเดอร์หรือไฟล์ไม่ได้เด็ดขาด", "สามารถเข้าถึงได้ตามปกติเนื่องจากได้รับสิทธิ์อนุญาตผ่านกลุ่มผู้ใช้แล้ว", "ระบบจะเรียกให้ทำการขอยกระดับสิทธิ์ผู้ดูแลระบบหลักผ่านหน้าจอ UAC"],
        "q2_ans": "A"
    },
    195: { # Lesson 6
        "num": 6,
        "q1": "หากต้องการสั่งลบไฟล์และโฟลเดอร์ย่อยทั้งหมดที่อยู่ในเส้นทางประมวลผลด้วยคีย์เวิร์ดพิเศษใน CMD ของ Windows ต้องใช้ออปชันใดร่วมกับคำสั่ง del?",
        "q1_opts": ["ออปชันสวิตช์ /a:h", "ออปชันสวิตช์ /s", "ออปชันสวิตช์ /w"],
        "q1_ans": "B",
        "q2": "ตัวแปรสภาพแวดล้อมระบบ Windows ข้อใดที่จัดเก็บที่อยู่โฟลเดอร์ชั่วคราวสำหรับเขียนและบันทึกไฟล์สั้นๆ ระหว่างใช้งานโปรแกรม?",
        "q2_opts": ["ตัวแปรระบบ %PATH%", "ตัวแปรระบบ %TEMP% หรือ %TMP%", "ตัวแปรระบบ %USERPROFILE%"],
        "q2_ans": "B"
    },
    196: { # Lesson 7
        "num": 7,
        "q1": "ข้อใดอธิบายความต่างในการตรวจจับอักษรพิมพ์ใหญ่พิมพ์เล็ก (Case Sensitivity) ของชื่อไฟล์ใน Linux และ Windows ได้ถูกต้อง?",
        "q1_opts": ["Linux ตรวจจับพิมพ์ใหญ่เล็ก (Case-Sensitive) / Windows ไม่สนใจพิมพ์ใหญ่เล็ก (Case-Insensitive)", "ทั้งสองระบบปฏิบัติการตรวจจับพิมพ์ใหญ่เล็กเข้มงวดเหมือนกันทั้งหมด", "ทั้งสองระบบปฏิบัติการไม่สนใจพิมพ์ใหญ่เล็กเลยในทุกกรณีการตั้งชื่อ"],
        "q1_ans": "A",
        "q2": "สถาปัตยกรรมเคอร์เนลหลักของระบบปฏิบัติการ Linux และ Windows มีข้อแตกต่างกันอย่างไร?",
        "q2_opts": ["Linux ทำงานแบบ Microkernel / Windows เป็นแบบ Monolithic Kernel", "ทั้งคู่ใช้แกนหลักการเขียนและคอมไพล์แบบ Hybrid Kernel เหมือนกัน", "Linux ทำงานแบบ Monolithic Kernel / Windows ทำงานแบบ Microkernel / Hybrid Kernel"],
        "q2_ans": "C"
    }
}

# ─── Replace or append the quiz block for each lesson 1 to 7 ───
for lid, info in quizzes.items():
    l = db.session.query(TutorialLesson).filter_by(id=lid).first()
    blocks = json.loads(l.content)
    
    # Generate the mini-quiz HTML value
    quiz_html = make_mini_quiz_html(
        info["num"],
        info["q1"],
        info["q1_opts"],
        info["q1_ans"],
        info["q2"],
        info["q2_opts"],
        info["q2_ans"]
    )
    
    # We want to replace the last block if it was previously a Q&A / Practice Questions
    # or append it if it is not there.
    last_val = blocks[-1].get("value", "")
    if "Practice Questions" in last_val or "Quick Quiz" in last_val or "❓" in last_val or "✏️" in last_val:
        # Replace the last block
        blocks[-1] = {"type": "markdown", "value": quiz_html}
        print(f"Replaced existing quiz/Q&A block in Lesson {lid}")
    else:
        # Append as new block
        blocks.append({"type": "markdown", "value": quiz_html})
        print(f"Appended new quiz block to Lesson {lid}")
        
    l.content = json.dumps(blocks, ensure_ascii=False)
    db.session.query(TutorialLesson).filter_by(id=lid).update({"content": l.content})
    db.session.commit()

print("All Lessons 1 to 7 successfully updated with Interactive Mini-Quizzes!")
