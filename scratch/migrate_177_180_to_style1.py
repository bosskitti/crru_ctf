import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

def make_style1_quiz_html(lid, q1_title, q1_opts, q1_correct, q2_title, q2_opts, q2_correct):
    # q1_opts and q2_opts are lists of tuples: (val_letter, text)
    
    q1_opts_html = ""
    for letter, text in q1_opts:
        q1_opts_html += f'<div class="mini-opt" data-val="{letter}"><span class="mini-bullet">{letter}</span> {text}</div>\n'
        
    q2_opts_html = ""
    for letter, text in q2_opts:
        q2_opts_html += f'<div class="mini-opt" data-val="{letter}"><span class="mini-bullet">{letter}</span> {text}</div>\n'

    html = f"""### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการผ่านบทเรียนย่อยนี้ (Lesson Clear):

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
<!-- Question 1 -->
<div class="mq-q" data-correct="{q1_correct}">
<div class="mq-title"><span>Q1.</span> {q1_title}</div>
<div class="mini-opts">
{q1_opts_html}</div>
</div>

<!-- Question 2 -->
<div class="mq-q" data-correct="{q2_correct}">
<div class="mq-title"><span>Q2.</span> {q2_title}</div>
<div class="mini-opts">
{q2_opts_html}</div>
</div>

<button class="mq-btn-check" onclick="checkMiniQuiz{lid}({lid})">Check Answers / ตรวจคำตอบ</button>
<div id="mq-status-{lid}" class="mq-status-bar"></div>
</div>

<div class="mq-gauge-col">
  <span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em; text-align:center;">Lesson Progress</span>
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
  <span id="lesson-status-txt-{lid}" class="mt-3 d-block text-muted" style="font-size:0.78rem; text-align:center;">โปรดตอบคำถามให้ครบ 2 ข้อ</span>
</div>
</div>
</div>

<script>
// Attach click listeners to manage selection state
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
      status.innerHTML = '<span style="color:#00f0ff; font-weight:bold;">กรุณากดตรวจคำตอบ</span>';
    }} else if (pct > 0) {{
      status.textContent = 'ตอบคำถามแล้ว ' + answeredCount + '/' + qGroups.length + ' ข้อ';
    }} else {{
      status.textContent = 'โปรดตอบคำถามให้ครบ 2 ข้อ';
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
    alert("กรุณาตอบคำถามท้ายบทให้ครบถ้วนทั้ง 2 ข้อก่อนส่งตรวจคำตอบครับ!");
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

  if (score === 2) {{
    if (fill) {{ fill.setAttribute('stroke-dasharray', '100, 100'); fill.style.stroke = '#3ddc84'; }}
    if (text) text.textContent = '100%';
    if (status_txt) status_txt.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
    
    status.style.background = 'rgba(61,220,132,0.08)';
    status.style.border = '1px solid rgba(61,220,132,0.25)';
    status.style.color = '#3ddc84';
    status.innerHTML = '🏆 <strong>LESSON CLEARED!</strong> คุณผ่านการประเมินความรู้ท้ายบทเรียนย่อยนี้เรียบร้อย (คะแนน 2/2) สามารถเดินทางไปศึกษาบทเรียนถัดไปได้ครับ!';
    
    localStorage.setItem('solved_lesson_{lid}', 'solved');
    groups.forEach(function(g) {{
      g.querySelectorAll('.mini-opt').forEach(function(o) {{
        o.style.pointerEvents = 'none';
      }});
    }});
    box.querySelector('.mq-btn-check').disabled = true;
  }} else {{
    var errorPct = Math.round((score / groups.length) * 100);
    if (fill) {{ fill.setAttribute('stroke-dasharray', errorPct + ', 100'); fill.style.stroke = '#ff007f'; }}
    if (text) text.textContent = errorPct + '%';
    if (status_txt) status_txt.textContent = 'ตอบไม่ถูกต้อง ลองใหม่!';

    status.style.background = 'rgba(255,0,127,0.08)';
    status.style.border = '1px solid rgba(255,0,127,0.25)';
    status.style.color = '#ff007f';
    status.innerHTML = '❌ <strong>ยังไม่ผ่าน!</strong> คุณได้คะแนน ' + score + '/2 (ทำข้อสอบไม่จบตาม Gauge Bar Progress) กรุณาทบทวนบทเรียนและตรวจเลือกคำตอบใหม่อีกครั้ง';
  }}
}}

// Load saved state
setTimeout(function() {{
  var solved = localStorage.getItem('solved_lesson_{lid}');
  if (solved === 'solved') {{
    var box = document.getElementById('mq-box-' + {lid});
    var groups = box.querySelectorAll('.mq-q');
    groups.forEach(function(g) {{
      var correctVal = g.getAttribute('data-correct');
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
    }});
    box.querySelector('.mq-btn-check').disabled = true;
    
    var fill = document.getElementById('lesson-gauge-fill-' + {lid});
    var text = document.getElementById('lesson-gauge-text-' + {lid});
    var status_txt = document.getElementById('lesson-status-txt-' + {lid});
    var status = document.getElementById('mq-status-' + {lid});
    
    if (fill) {{ fill.setAttribute('stroke-dasharray', '100, 100'); fill.style.stroke = '#3ddc84'; }}
    if (text) text.textContent = '100%';
    if (status_txt) status_txt.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
    
    status.style.display = 'block';
    status.style.background = 'rgba(61,220,132,0.08)';
    status.style.border = '1px solid rgba(61,220,132,0.25)';
    status.style.color = '#3ddc84';
    status.innerHTML = '🏆 <strong>LESSON CLEARED!</strong> คุณผ่านการประเมินความรู้ท้ายบทเรียนย่อยนี้เรียบร้อย (คะแนน 2/2) สามารถเดินทางไปศึกษาบทเรียนถัดไปได้ครับ!';
  }}
}}, 200);
</script>
"""
    return html

# Define all 4 lessons data
lessons_data = {
    177: {
        "q1_title": "พอร์ตบริการเครือข่ายมาตรฐานสำหรับการเข้าถึงหน้าเว็บเพจแบบเข้ารหัสปลอดภัย (HTTPS) คือพอร์ตใด?",
        "q1_opts": [("A", "Port 80"), ("B", "Port 443 (HTTPS)"), ("C", "Port 22"), ("D", "Port 8080")],
        "q1_correct": "B",
        "q2_title": "โครงการมาตรฐานสากลด้านความปลอดภัยเว็บที่จัดอันดับ 10 ความเสี่ยงสูงสุดของเว็บแอปพลิเคชันคือองค์กรใด?",
        "q2_opts": [("A", "W3C"), ("B", "OWASP"), ("C", "SANS Institute"), ("D", "MITRE Corporation")],
        "q2_correct": "B"
    },
    178: {
        "q1_title": "ช่องโหว่ประเภทใดเกิดขึ้นจากการที่เซิร์ฟเวอร์นำอินพุตของผู้ใช้ไปเรียกประมวลผลเป็นคำสั่งระบบปฏิบัติการโดยตรง?",
        "q1_opts": [("A", "SQL Injection"), ("B", "Command Injection"), ("C", "Cross-Site Scripting (XSS)"), ("D", "Local File Inclusion (LFI)")],
        "q1_correct": "B",
        "q2_title": "คิวรีเป้าหมายพิเศษระดับมาตรฐาน ' OR 1=1 -- นิยมใช้ส่งเข้าไปในฐานข้อมูลเพื่อทำลายเงื่อนไขข้อใด?",
        "q2_opts": [("A", "ขโมยดูข้อมูลทั้งหมด (Data Exfiltration)"), ("B", "ข้ามขั้นตอนตรวจสอบยืนยันตน (Bypass Authentication)"), ("C", "ทำลายเซิร์ฟเวอร์ระบบล่ม (Denial of Service)"), ("D", "ค้นหารหัสผ่านระบบ (Password Cracking)")],
        "q2_correct": "B"
    },
    179: {
        "q1_title": "ช่องโหว่ Cross-Site Scripting (XSS) เกิดจากการลอบฝังแทรกสคริปต์โค้ดประเภทใดเข้ามาทำงานฝั่ง Client Browser?",
        "q1_opts": [("A", "SQL Query code"), ("B", "JavaScript"), ("C", "Bash Shell command"), ("D", "PHP Server Script")],
        "q1_correct": "B",
        "q2_title": "คีย์เวิร์ดมาตรฐาน HTML tag ใดที่นักโจมตีใช้ส่ง XSS Payload เพื่อเปิดจำลองกล่องป๊อปอัพ?",
        "q2_opts": [("A", "<script>"), ("B", "<iframe>"), ("C", "<div>"), ("D", "<img>")],
        "q2_correct": "A"
    },
    180: {
        "q1_title": "ส่วนหัว (Header) ความปลอดภัยใด in HTTP Response ที่ใช้ป้องกันหน้าเว็บไม่ให้ถูกนำไปฝังใน Iframe เพื่อเลี่ยงช่องโหว่ Clickjacking?",
        "q1_opts": [("A", "X-Frame-Options"), ("B", "Content-Security-Policy"), ("C", "Strict-Transport-Security"), ("D", "X-XSS-Protection")],
        "q1_correct": "A",
        "q2_title": "หลักปฏิบัติเพื่อความปลอดภัยในการป้องกันการแทรกโค้ดทำลายระบบเครือข่ายฐานข้อมูล (Injection) ทุกประเภทคือข้อใด?",
        "q2_opts": [("A", "การกรองตรวจสอบความถูกต้องข้อมูลนำเข้า (Input Validation)"), ("B", "การเข้ารหัสฐานข้อมูล (Database Encryption)"), ("C", "การสำรองไฟล์ข้อมูลประจำวัน (Daily Backup)"), ("D", "การติดตั้งระบบแจ้งเตือนแฮกเกอร์ (Intrusion Detection)")],
        "q2_correct": "A"
    }
}

with app.app_context():
    for lid, d in lessons_data.items():
        lesson = app.db.session.query(TutorialLesson).filter_by(id=lid).first()
        if not lesson:
            print(f"Lesson {lid} not found")
            continue
        
        try:
            blocks = json.loads(lesson.content)
            # The quiz is in block 2
            blocks[2]['value'] = make_style1_quiz_html(
                lid,
                d["q1_title"], d["q1_opts"], d["q1_correct"],
                d["q2_title"], d["q2_opts"], d["q2_correct"]
            )
            lesson.content = json.dumps(blocks, ensure_ascii=False)
            app.db.session.commit()
            print(f"Successfully migrated Lesson ID {lid} to Style 1 Layout!")
        except Exception as e:
            print(f"Error migrating Lesson {lid}: {e}")
