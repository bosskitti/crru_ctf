import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l168 = db.session.query(TutorialLesson).filter_by(id=168).first()
blocks = json.loads(l168.content)

# ─── Replace Block 5 with High-End Offset Rings & floating labels (No text clipping, no ugly black boxes) ───
blocks[5]['value'] = """### 🏛️ Windows System Architecture

<style>
.wsa-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;gap:36px;align-items:center;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:32px;box-shadow:0 4px 20px rgba(0,0,0,0.25);box-sizing:border-box;}
@media(max-width:820px){.wsa-wrap{flex-direction:column;}}

/* Offset Minimalist Ring Diagram */
.wsa-diagram-wrap{flex-shrink:0;position:relative;width:280px;height:280px;background:rgba(255,255,255,0.01);border-radius:50%;}
.wsa-r-user{position:absolute;width:250px;height:250px;border:1.2px solid #00f0ff;border-radius:50%;top:15px;left:15px;box-shadow:0 0 10px rgba(0,240,255,0.1), inset 0 0 10px rgba(0,240,255,0.05);pointer-events:none;}
.wsa-r-kernel{position:absolute;width:160px;height:160px;border:1.2px solid #ff007f;border-radius:50%;bottom:25px;left:25px;box-shadow:0 0 10px rgba(255,0,127,0.1), inset 0 0 10px rgba(255,0,127,0.05);pointer-events:none;}
.wsa-r-hardware{position:absolute;width:80px;height:80px;border:1.2px solid #fbbf24;border-radius:50%;bottom:25px;left:25px;box-shadow:0 0 12px rgba(251,191,36,0.15), inset 0 0 8px rgba(251,191,36,0.05);display:flex;align-items:center;justify-content:center;pointer-events:none;}

/* Floating Labels (luminous, absolute position, no black boxes, no text wraps) */
.wsa-lbl{position:absolute;font-family:'JetBrains Mono',monospace;font-size:0.75rem;font-weight:800;letter-spacing:0.04em;text-shadow:0 0 8px currentColor;white-space:nowrap;}
.wsa-lbl-user{color:#00f0ff;top:28px;right:45px;}
.wsa-lbl-kernel{color:#ff007f;top:105px;right:95px;}
.wsa-lbl-hw{color:#fbbf24;font-size:0.72rem;}

/* Interactive hover glow */
.wsa-diagram-wrap:hover .wsa-r-user{border-color:#00f0ff;box-shadow:0 0 18px rgba(0,240,255,0.25), inset 0 0 15px rgba(0,240,255,0.1);}
.wsa-diagram-wrap:hover .wsa-r-kernel{border-color:#ff007f;box-shadow:0 0 18px rgba(255,0,127,0.25), inset 0 0 15px rgba(255,0,127,0.1);}
.wsa-diagram-wrap:hover .wsa-r-hardware{border-color:#fbbf24;box-shadow:0 0 22px rgba(251,191,36,0.35), inset 0 0 12px rgba(251,191,36,0.15);}
.wsa-diagram-wrap:hover .wsa-lbl{text-shadow:0 0 12px currentColor;}

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
<div class="wsa-r-user"></div>
<div class="wsa-r-kernel"></div>
<div class="wsa-r-hardware">
<span class="wsa-lbl wsa-lbl-hw">Hardware</span>
</div>
<span class="wsa-lbl wsa-lbl-user">User Mode</span>
<span class="wsa-lbl wsa-lbl-kernel">Kernel Mode</span>
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
print("Windows System Architecture Rings redesigned with offset layout and floating labels!")
