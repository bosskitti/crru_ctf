import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

lesson = db.session.query(TutorialLesson).filter_by(id=165).first()
if not lesson:
    print("Lesson not found!")
    exit(1)

blocks = json.loads(lesson.content)

# ---- Block 17: Unix in Linux System (with concentric circles diagram) ----
block_17 = """### 📌 Unix in Linux System

<style>
.unix-layout{display:flex;align-items:center;gap:40px;width:100%;max-width:1050px;margin:2rem auto;background:rgba(15,17,26,0.4);border:1px solid rgba(255,255,255,0.05);border-radius:12px;padding:32px;box-shadow:inset 0 0 20px rgba(0,0,0,0.3);}
.unix-circles{flex-shrink:0;display:flex;align-items:center;justify-content:center;width:220px;height:220px;position:relative;}
.circle-outer{width:200px;height:200px;border-radius:50%;background:radial-gradient(circle,rgba(0,240,255,0.12) 0%,rgba(0,240,255,0.04) 100%);border:2px solid rgba(0,240,255,0.4);display:flex;align-items:center;justify-content:center;position:relative;box-shadow:0 0 20px rgba(0,240,255,0.1),inset 0 0 20px rgba(0,240,255,0.05);}
.circle-inner{width:110px;height:110px;border-radius:50%;background:radial-gradient(circle,rgba(171,32,253,0.25) 0%,rgba(171,32,253,0.08) 100%);border:2px solid rgba(171,32,253,0.5);display:flex;align-items:center;justify-content:center;box-shadow:0 0 15px rgba(171,32,253,0.2),inset 0 0 15px rgba(171,32,253,0.08);}
.circle-label-outer{position:absolute;top:12px;right:16px;font-size:0.9rem;font-weight:800;color:#00f0ff;text-shadow:0 0 10px rgba(0,240,255,0.5);letter-spacing:0.05em;}
.circle-label-inner{font-size:0.85rem;font-weight:800;color:#ab20fd;text-shadow:0 0 8px rgba(171,32,253,0.6);letter-spacing:0.05em;}
.unix-points{flex:1;display:flex;flex-direction:column;gap:14px;}
.unix-point{display:flex;align-items:flex-start;gap:10px;padding:10px 14px;border-radius:8px;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.04);transition:all 0.2s ease;cursor:default;}
.unix-point:hover{background:rgba(255,255,255,0.04);border-color:rgba(0,240,255,0.15);transform:translateX(4px);}
.unix-bullet{width:6px;height:6px;border-radius:50%;background:#00f0ff;margin-top:7px;flex-shrink:0;box-shadow:0 0 6px rgba(0,240,255,0.6);}
.unix-point p{margin:0;font-size:0.95rem;color:#cbd5e1;line-height:1.65;}
.unix-point p .hl-cyan{color:#00f0ff;font-weight:700;}
.unix-point p .hl-purple{color:#ab20fd;font-weight:700;}
.unix-point p .hl-amber{color:#fbbf24;font-weight:700;}
@media(max-width:768px){.unix-layout{flex-direction:column;align-items:center;}}
</style>

<div class="unix-layout">
<div class="unix-circles">
<div class="circle-outer">
<span class="circle-label-outer">Linux</span>
<div class="circle-inner">
<span class="circle-label-inner">Unix</span>
</div>
</div>
</div>
<div class="unix-points">
<div class="unix-point">
<div class="unix-bullet"></div>
<p><span class="hl-cyan">Unix</span> คือระบบปฏิบัติการที่ถูกพัฒนาขึ้นครั้งแรกในช่วง <span class="hl-amber">ทศวรรษ 1960s</span> โดย <span class="hl-cyan">Ken Thompson</span>, <span class="hl-cyan">Dennis Ritchie</span> และทีมงานอื่นๆ</p>
</div>
<div class="unix-point">
<div class="unix-bullet"></div>
<p><span class="hl-amber">Bell Laboratories</span> และ <span class="hl-amber">MIT</span> ได้ร่วมพัฒนาระบบปฏิบัติการชื่อ <span class="hl-purple">Multics</span> ก่อนจะเปลี่ยนชื่อมาเป็น <span class="hl-cyan">Unix</span> ซึ่งเขียนด้วยภาษา <span class="hl-purple">C</span></p>
</div>
<div class="unix-point">
<div class="unix-bullet"></div>
<p>Unix เป็นระบบที่มีความเสถียรสูง รองรับการใช้งานแบบ <span class="hl-cyan">Multi-user</span> และ <span class="hl-cyan">Multi-tasking</span> เหมาะสำหรับ Server, Desktop และ Laptop</p>
</div>
<div class="unix-point">
<div class="unix-bullet"></div>
<p><span class="hl-cyan">Linux</span> คือระบบปฏิบัติการที่ออกแบบมาในแนวทางเดียวกับ <span class="hl-purple">Unix (Unix-like)</span> โดยสืบทอดหลักการออกแบบและโครงสร้างจาก Unix</p>
</div>
</div>
</div>"""

# ---- Block 19: Unix in Linux System (Cont) — Terminal mockup ----
block_19 = """### 📌 Unix in Linux System (Cont)

<style>
.unix-term-wrapper{width:100%;max-width:1050px;margin:2rem auto;}
.unix-term-card{background:rgba(15,17,26,0.5);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:28px;box-shadow:inset 0 0 20px rgba(0,0,0,0.3);}
.unix-term-card p{font-size:0.95rem;color:#cbd5e1;line-height:1.7;margin-bottom:1rem;}
.unix-term-card p .hl-cyan{color:#00f0ff;font-weight:700;}
.unix-term-window{border-radius:10px;overflow:hidden;border:1px solid rgba(255,255,255,0.08);box-shadow:0 8px 32px rgba(0,0,0,0.5);margin-top:8px;}
.unix-term-titlebar{background:rgba(30,32,48,0.95);padding:10px 16px;display:flex;align-items:center;gap:8px;border-bottom:1px solid rgba(255,255,255,0.06);}
.unix-term-dot{width:12px;height:12px;border-radius:50%;}
.unix-term-dot.red{background:#ff5f57;}
.unix-term-dot.yellow{background:#ffbd2e;}
.unix-term-dot.green{background:#28c840;}
.unix-term-title{flex:1;text-align:center;font-size:0.78rem;color:#8a94a6;font-family:'JetBrains Mono',monospace;letter-spacing:0.05em;}
.unix-term-body{background:#070910;padding:20px 24px;font-family:'JetBrains Mono','Courier New',monospace;font-size:0.88rem;line-height:1.9;}
.unix-term-body .prompt{color:#3ddc84;}
.unix-term-body .cmd{color:#ffffff;}
.unix-term-body .out{color:#8a94a6;}
.unix-term-body .out-cyan{color:#00f0ff;}
.unix-term-body .out-amber{color:#fbbf24;}
</style>

<div class="unix-term-wrapper">
<div class="unix-term-card">
<p>Unix Terminal คืออินเตอร์เฟซบรรทัดคำสั่ง (<span class="hl-cyan">Command-Line Interface</span>) สำหรับสื่อสารกับ Shell และสั่งงานระบบปฏิบัติการโดยตรง ซึ่ง Linux ก็ใช้ Terminal ในรูปแบบเดียวกัน เนื่องจากสืบทอดโครงสร้างมาจาก Unix</p>
<div class="unix-term-window">
<div class="unix-term-titlebar">
<span class="unix-term-dot red"></span>
<span class="unix-term-dot yellow"></span>
<span class="unix-term-dot green"></span>
<span class="unix-term-title">Unix / Linux Terminal — bash</span>
</div>
<div class="unix-term-body">
<div><span class="prompt">user@linux:~$</span> <span class="cmd">uname -a</span></div>
<div><span class="out-cyan">Linux kali 6.1.0-kali9-amd64 #1 SMP PREEMPT Debian x86_64 GNU/Linux</span></div>
<div>&nbsp;</div>
<div><span class="prompt">user@linux:~$</span> <span class="cmd">whoami</span></div>
<div><span class="out-amber">user</span></div>
<div>&nbsp;</div>
<div><span class="prompt">user@linux:~$</span> <span class="cmd">ls /</span></div>
<div><span class="out">bin  boot  dev  etc  home  lib  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var</span></div>
<div>&nbsp;</div>
<div><span class="prompt">user@linux:~$</span> <span class="cmd">echo "Hello from Unix-like terminal!"</span></div>
<div><span class="out-cyan">Hello from Unix-like terminal!</span></div>
<div>&nbsp;</div>
<div><span class="prompt">user@linux:~$</span> <span class="cmd">_</span></div>
</div>
</div>
</div>
</div>"""

# Update blocks 17 and 19
blocks[17]['value'] = block_17
blocks[19]['value'] = block_19

# Save and Commit
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
db.session.commit()

print("Unix slides (blocks 17 and 19) upgraded successfully!")
print(f"Block 17 length: {len(block_17)}")
print(f"Block 19 length: {len(block_19)}")
