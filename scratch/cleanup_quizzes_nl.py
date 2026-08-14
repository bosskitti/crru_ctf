import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

# Helper function to generate Interactive Mini-Quiz HTML/JS WITHOUT raw "\n" escape characters
def make_mini_quiz_clean(lesson_num, q1, q1_opts, q1_ans, q2, q2_opts, q2_ans):
    # We write lines with normal python newline in triple quotes to prevent raw "\n" leaks
    opts1_html = ""
    for idx, opt in enumerate(q1_opts):
        bullet = chr(65 + idx)
        opts1_html += f'<div class="mini-opt" data-val="{bullet}" onclick="updateMiniProgress({lesson_num})"><span class="mini-bullet">{bullet}</span>{opt}</div>\n'

    opts2_html = ""
    for idx, opt in enumerate(q2_opts):
        bullet = chr(65 + idx)
        opts2_html += f'<div class="mini-opt" data-val="{bullet}" onclick="updateMiniProgress({lesson_num})"><span class="mini-bullet">{bullet}</span>{opt}</div>\n'

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

/* Neon Gauge Progress Bar styling */
.mq-progress-container{{width:100%;background:rgba(7,9,16,0.8);border:1px solid rgba(255,255,255,0.08);height:26px;border-radius:13px;position:relative;overflow:hidden;margin:20px 0;display:flex;align-items:center;box-shadow:inset 0 2px 8px rgba(0,0,0,0.6);}}
.mq-progress-bar{{width:0%;height:100%;background:linear-gradient(90deg, #ff007f 0%, #fbbf24 50%, #00f0ff 100%);transition:all 0.35s cubic-bezier(0.4, 0, 0.2, 1);box-shadow:0 0 12px rgba(0,240,255,0.2);}}
.mq-progress-text{{position:absolute;width:100%;text-align:center;font-family:\'JetBrains Mono\',monospace;font-size:0.75rem;font-weight:800;color:#ffffff;text-shadow:0 1px 3px rgba(0,0,0,0.9);z-index:2;letter-spacing:0.05em;}}

.mq-btn-check{{padding:10px 20px;background:#00f0ff;border:none;border-radius:6px;font-family:\'JetBrains Mono\',monospace;font-size:0.82rem;font-weight:800;color:#070910;cursor:pointer;box-shadow:0 0 10px rgba(0,240,255,0.25);transition:all 0.15s ease;}}
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

<!-- Neon Gauge Bar Progress -->
<div class="mq-progress-container">
<div id="mq-progress-bar-{lesson_num}" class="mq-progress-bar"></div>
<span id="mq-progress-text-{lesson_num}" class="mq-progress-text">Lesson Progress: 0% (ยังไม่ผ่าน)</span>
</div>

<button class="mq-btn-check" onclick="checkMiniQuiz({lesson_num})">Check Answers / ตรวจคำตอบ</button>
<div id="mq-status-{lesson_num}" class="mq-status-bar"></div>
</div>

<script>
// Attach click listeners to manage selection state
document.querySelectorAll('#mq-box-{lesson_num} .mini-opt').forEach(opt => {{
  opt.addEventListener('click', function() {{
    const parent = this.closest('.mq-q');
    parent.querySelectorAll('.mini-opt').forEach(o => o.classList.remove('selected'));
    this.classList.add('selected');
  }});
}});

// Realtime progress updater based on answers selected
function updateMiniProgress(lnum) {{
  const box = document.getElementById('mq-box-' + lnum);
  const qGroups = box.querySelectorAll('.mq-q');
  let answeredCount = 0;
  
  qGroups.forEach(g => {{
    if (g.querySelector('.mini-opt.selected')) {{
      answeredCount++;
    }}
  }});

  const pct = Math.round((answeredCount / qGroups.length) * 100);
  const pbar = document.getElementById('mq-progress-bar-' + lnum);
  const ptext = document.getElementById('mq-progress-text-' + lnum);

  if (pct > 0) {{
    pbar.style.width = pct + '%';
    pbar.style.background = 'linear-gradient(90deg, #ff007f 0%, #fbbf24 100%)';
    ptext.textContent = 'Lesson Progress: ' + pct + '% (ตอบคำถามค้างอยู่)';
  }}
}}

// Check correctness and update gauge status
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

  const pbar = document.getElementById('mq-progress-bar-' + lnum);
  const ptext = document.getElementById('mq-progress-text-' + lnum);
  const status = document.getElementById('mq-status-' + lnum);
  status.style.display = 'block';

  if (score === 2) {{
    pbar.style.width = '100%';
    pbar.style.background = '#3ddc84';
    pbar.style.boxShadow = '0 0 15px rgba(61,220,132,0.6)';
    ptext.textContent = 'Lesson Progress: 100% (ผ่านเรียบร้อย)';
    
    status.style.background = 'rgba(61,220,132,0.08)';
    status.style.border = '1px solid rgba(61,220,132,0.25)';
    status.style.color = '#3ddc84';
    status.innerHTML = '🏆 <strong>LESSON CLEARED!</strong> คุณผ่านการประเมินความรู้ท้ายบทเรียนย่อยนี้เรียบร้อย (คะแนน 2/2) สามารถเดินทางไปศึกษาบทเรียนถัดไปได้ครับ!';
  }} else {{
    const errorPct = Math.round((score / groups.length) * 100);
    pbar.style.width = errorPct + '%';
    pbar.style.background = '#ff007f';
    pbar.style.boxShadow = '0 0 15px rgba(255,0,127,0.6)';
    ptext.textContent = 'Lesson Progress: ' + errorPct + '% (ไม่ผ่าน - ทำไม่จบ)';

    status.style.background = 'rgba(255,0,127,0.08)';
    status.style.border = '1px solid rgba(255,0,127,0.25)';
    status.style.color = '#ff007f';
    status.innerHTML = '❌ <strong>ยังไม่ผ่าน!</strong> คุณได้คะแนน ' + score + '/2 (ทำข้อสอบไม่จบตาม Gauge Bar Progress) กรุณาทบทวนบทเรียนและตรวจเลือกคำตอบใหม่อีกครั้ง';
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
        "q1": "ปุ่มลัดคีย์ควบคุมใด in Linux Terminal ที่ทำหน้าที่ส่งสัญญาณยุติการทำงาน (SIGINT) ของโปรแกรมหลักทันที?",
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

# ─── Replace existing quiz blocks with the clean HTML ───
for lid, info in quizzes.items():
    l = db.session.query(TutorialLesson).filter_by(id=lid).first()
    blocks = json.loads(l.content)
    
    quiz_html = make_mini_quiz_clean(
        info["num"],
        info["q1"],
        info["q1_opts"],
        info["q1_ans"],
        info["q2"],
        info["q2_opts"],
        info["q2_ans"]
    )
    
    # Replace in blocks
    for i, b in enumerate(blocks):
        val = b.get("value", "")
        if "Quick Quiz" in val or "Practice Questions" in val or "✏️" in val or "❓" in val:
            blocks[i] = {"type": "markdown", "value": quiz_html}
            print(f"Cleaned quiz block in Lesson {lid} at index {i}")
            break
            
    l.content = json.dumps(blocks, ensure_ascii=False)
    db.session.query(TutorialLesson).filter_by(id=lid).update({"content": l.content})
    db.session.commit()

print("Cleanup script executed: all raw '\\n' characters removed successfully!")
ctx.pop()
