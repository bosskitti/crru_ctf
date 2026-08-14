import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l168 = db.session.query(TutorialLesson).filter_by(id=168).first()
blocks = json.loads(l168.content)

# ─── Replace Block 5 with Clean Minimalist Glowing Rings (Matching Unix/Linux design style) ───
blocks[5]['value'] = """### 🏛️ Windows System Architecture

<style>
.wsa-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;gap:36px;align-items:center;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:32px;box-shadow:0 4px 20px rgba(0,0,0,0.25);box-sizing:border-box;}
@media(max-width:820px){.wsa-wrap{flex-direction:column;}}

/* Clean Minimalist Ring Diagram Side */
.wsa-diagram-wrap{flex-shrink:0;position:relative;width:280px;height:280px;display:flex;align-items:center;justify-content:center;}
.wsa-ring{border-radius:50%;position:absolute;display:flex;align-items:center;justify-content:center;box-sizing:border-box;transition:all 0.3s ease;}

/* Outer Ring: User Mode (Cyan) */
.wsa-ring.user{width:260px;height:260px;border:1px solid #00f0ff;background:rgba(0,240,255,0.01);box-shadow:0 0 12px rgba(0,240,255,0.15), inset 0 0 12px rgba(0,240,255,0.05);}
.wsa-ring.user::after{content:"User Mode";position:absolute;top:-10px;left:50%;transform:translateX(-50%);font-family:'JetBrains Mono',monospace;font-size:0.75rem;font-weight:800;color:#00f0ff;background:#0d0e15;padding:0 8px;letter-spacing:0.05em;}

/* Middle Ring: Kernel Mode (Pink) */
.wsa-ring.kernel{width:170px;height:170px;border:1px solid #ff007f;background:rgba(255,0,127,0.01);box-shadow:0 0 12px rgba(255,0,127,0.15), inset 0 0 12px rgba(255,0,127,0.05);}
.wsa-ring.kernel::after{content:"Kernel Mode";position:absolute;top:-10px;left:50%;transform:translateX(-50%);font-family:'JetBrains Mono',monospace;font-size:0.72rem;font-weight:800;color:#ff007f;background:#0d0e15;padding:0 8px;letter-spacing:0.05em;}

/* Inner Ring: Hardware (Amber) */
.wsa-ring.hardware{width:80px;height:80px;border:1px solid #fbbf24;background:rgba(251,191,36,0.03);box-shadow:0 0 15px rgba(251,191,36,0.2), inset 0 0 8px rgba(251,191,36,0.05);display:flex;align-items:center;justify-content:center;}
.wsa-hw-text{font-family:'JetBrains Mono',monospace;font-size:0.68rem;font-weight:800;color:#fbbf24;letter-spacing:0.05em;text-align:center;}

/* Subtle Hover Glow on the wrapper */
.wsa-diagram-wrap:hover .wsa-ring.user{border-color:#00f0ff;box-shadow:0 0 20px rgba(0,240,255,0.3), inset 0 0 15px rgba(0,240,255,0.1);}
.wsa-diagram-wrap:hover .wsa-ring.kernel{border-color:#ff007f;box-shadow:0 0 20px rgba(255,0,127,0.3), inset 0 0 15px rgba(255,0,127,0.1);}
.wsa-diagram-wrap:hover .wsa-ring.hardware{border-color:#fbbf24;box-shadow:0 0 25px rgba(251,191,36,0.4), inset 0 0 12px rgba(251,191,36,0.15);}

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
<div class="wsa-ring user">
<div class="wsa-ring kernel">
<div class="wsa-ring hardware">
<span class="wsa-hw-text">Hardware</span>
</div>
</div>
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
print("Windows System Architecture Rings redesigned to match the Unix/Linux clean minimalist style!")
