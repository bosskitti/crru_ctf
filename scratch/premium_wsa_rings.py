import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l168 = db.session.query(TutorialLesson).filter_by(id=168).first()
blocks = json.loads(l168.content)

# ─── Replace Block 5 with Premium Glowing & Animated Cyberpunk Rings ───
blocks[5]['value'] = """### 🏛️ Windows System Architecture

<style>
.wsa-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;gap:36px;align-items:center;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:32px;box-shadow:0 4px 20px rgba(0,0,0,0.25);box-sizing:border-box;}
@media(max-width:820px){.wsa-wrap{flex-direction:column;}}

/* Ring Diagram Side */
.wsa-diagram-wrap{flex-shrink:0;position:relative;width:280px;height:280px;display:flex;align-items:center;justify-content:center;}
.wsa-ring{border-radius:50%;position:absolute;display:flex;align-items:center;justify-content:center;box-sizing:border-box;}

/* User Mode Ring: Outer, Cyan theme */
.wsa-ring.user{width:280px;height:280px;background:rgba(0,240,255,0.02);border:2px dashed rgba(0,240,255,0.35);box-shadow:0 0 25px rgba(0,240,255,0.15), inset 0 0 15px rgba(0,240,255,0.05);animation:wsa-spin-cw 30s linear infinite;}

/* Kernel Mode Ring: Middle, Pink theme */
.wsa-ring.kernel{width:190px;height:190px;background:rgba(255,0,127,0.03);border:2px dashed rgba(255,0,127,0.35);box-shadow:0 0 20px rgba(255,0,127,0.15), inset 0 0 12px rgba(255,0,127,0.05);animation:wsa-spin-ccw 20s linear infinite;}

/* Hardware Ring: Inner Solid, Amber theme */
.wsa-ring.hardware{width:100px;height:100px;background:rgba(251,191,36,0.08);border:2px solid rgba(251,191,36,0.6);box-shadow:0 0 30px rgba(251,191,36,0.25);animation:wsa-pulse-slow 3s ease-in-out infinite;}

/* Labels: Placed cleanly, not spinning */
.wsa-labels-overlay{position:absolute;width:100%;height:100%;top:0;left:0;pointer-events:none;}
.wsa-label{position:absolute;left:50%;transform:translateX(-50%);font-family:'JetBrains Mono',monospace;font-size:0.72rem;font-weight:800;letter-spacing:0.08em;padding:2px 8px;border-radius:4px;border:1px solid;}
.lbl-user{top:20px;color:#00f0ff;background:rgba(7,9,16,0.95);border-color:rgba(0,240,255,0.4);box-shadow:0 0 8px rgba(0,240,255,0.3);}
.lbl-kernel{top:68px;color:#ff007f;background:rgba(7,9,16,0.95);border-color:rgba(255,0,127,0.4);box-shadow:0 0 8px rgba(255,0,127,0.3);}
.lbl-hw{top:128px;color:#fbbf24;background:rgba(7,9,16,0.9);border-color:rgba(251,191,36,0.5);box-shadow:0 0 10px rgba(251,191,36,0.3);}

/* Animations */
@keyframes wsa-spin-cw{from{transform:rotate(0deg);}to{transform:rotate(36deg);}}
@keyframes wsa-spin-ccw{from{transform:rotate(0deg);}to{transform:rotate(-36deg);}}
@keyframes wsa-pulse-slow{0%,100%{transform:scale(1);box-shadow:0 0 25px rgba(251,191,36,0.2);}50%{transform:scale(1.05);box-shadow:0 0 35px rgba(251,191,36,0.45);}}

/* Content side */
.wsa-content{flex:1;display:flex;flex-direction:column;gap:16px;}
.wsa-mode-card{padding:18px;border-radius:10px;border:1px solid;background:rgba(255,255,255,0.02);box-sizing:border-box;}
.wsa-mode-card.kernel-card{border-color:rgba(255,0,127,0.15);background:rgba(255,0,127,0.015);}
.wsa-mode-card.user-card{border-color:rgba(0,240,255,0.15);background:rgba(0,240,255,0.015);}
.wsa-mode-title{font-size:0.95rem;font-weight:700;margin-bottom:6px;display:flex;align-items:center;gap:8px;}
.kernel-card .wsa-mode-title{color:#ff007f;}
.user-card .wsa-mode-title{color:#00f0ff;}
.wsa-mode-desc{font-size:0.85rem;color:#94a3b8;line-height:1.65;margin:0;}
</style>

<div class="wsa-wrap">
<div class="wsa-diagram-wrap">
<div class="wsa-ring user"></div>
<div class="wsa-ring kernel"></div>
<div class="wsa-ring hardware"></div>
<div class="wsa-labels-overlay">
<span class="wsa-label lbl-user">USER MODE</span>
<span class="wsa-label lbl-kernel">KERNEL MODE</span>
<span class="wsa-label lbl-hw">HARDWARE</span>
</div>
</div>
<div class="wsa-content">
<div class="wsa-mode-card kernel-card">
<div class="wsa-mode-title">🔴 Kernel Mode (โหมดเคอร์เนล)</div>
<p class="wsa-mode-desc">เป็นส่วนสิทธิ์ระบบระดับสูงที่มี <strong>การเข้าถึงฮาร์ดแวร์โดยตรงและไม่มีข้อจำกัด</strong> การประมวลผลคำสั่งเคอร์เนลทั้งหมดแชร์หน่วยความจำเสมือนเพียงพื้นที่เดียว หากมีข้อผิดพลาดระบบ Windows จะล่มลงในลักษณะจอฟ้า (BSOD) ทันทีเพื่อความปลอดภัยของข้อมูล</p>
</div>
<div class="wsa-mode-card user-card">
<div class="wsa-mode-title">🔵 User Mode (โหมดผู้ใช้)</div>
<p class="wsa-mode-desc">เป็นระดับสิทธิ์ใช้งานทั่วไปสำหรับแอปพลิเคชันของผู้ใช้ ระบบ Windows จะแบ่งสัดส่วนเนื้อที่การทำงานแยกขาดจากกัน (Isolated Process Space) หากโปรแกรมใดทำงานล้มเหลวหรือปิดตัวลง จะไม่กระทบต่อระบบปฏิบัติการหลักให้เสียหายตาม</p>
</div>
</div>
</div>"""

l168.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=168).update({"content": l168.content})
db.session.commit()
print("Premium Animated Cyberpunk Ring Diagram updated in Block 5!")
