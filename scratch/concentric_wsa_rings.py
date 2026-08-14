import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l168 = db.session.query(TutorialLesson).filter_by(id=168).first()
blocks = json.loads(l168.content)

# ─── Replace Block 5 with Expanded Concentric Rings, Color on Inner hardware core, floating labels ───
blocks[5]['value'] = """### 🏛️ Windows System Architecture

<style>
.wsa-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;gap:36px;align-items:center;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:32px;box-shadow:0 4px 20px rgba(0,0,0,0.25);box-sizing:border-box;}
@media(max-width:820px){.wsa-wrap{flex-direction:column;}}

/* Large Concentric Rings Diagram (Expanded size) */
.wsa-diagram-wrap{flex-shrink:0;position:relative;width:340px;height:340px;display:flex;align-items:center;justify-content:center;}
.wsa-r-user{width:320px;height:320px;border:1.2px solid #00f0ff;border-radius:50%;background:transparent;box-shadow:0 0 12px rgba(0,240,255,0.12), inset 0 0 10px rgba(0,240,255,0.04);position:relative;display:flex;align-items:center;justify-content:center;}
.wsa-r-kernel{width:220px;height:220px;border:1.2px solid #ff007f;border-radius:50%;background:transparent;box-shadow:0 0 12px rgba(255,0,127,0.12), inset 0 0 10px rgba(255,0,127,0.04);position:relative;display:flex;align-items:center;justify-content:center;}

/* Innermost Hardware Ring: Colored background for focus */
.wsa-r-hardware{width:120px;height:120px;border:1.2px solid #fbbf24;border-radius:50%;background:rgba(251,191,36,0.12);box-shadow:0 0 18px rgba(251,191,36,0.2), inset 0 0 10px rgba(251,191,36,0.08);display:flex;align-items:center;justify-content:center;position:relative;}

/* Clean floating label positions - No black masking boxes, no text wrapping */
.wsa-lbl{position:absolute;font-family:'JetBrains Mono',monospace;font-size:0.75rem;font-weight:800;letter-spacing:0.04em;text-shadow:0 0 8px currentColor;white-space:nowrap;pointer-events:none;}
.wsa-lbl-user{color:#00f0ff;top:14px;left:50%;transform:translateX(-50%);}
.wsa-lbl-kernel{color:#ff007f;top:12px;left:50%;transform:translateX(-50%);}
.wsa-lbl-hw{color:#fbbf24;position:static;}

/* Subtle Hover Glow on concentric rings */
.wsa-diagram-wrap:hover .wsa-r-user{border-color:#00f0ff;box-shadow:0 0 20px rgba(0,240,255,0.25), inset 0 0 15px rgba(0,240,255,0.08);}
.wsa-diagram-wrap:hover .wsa-r-kernel{border-color:#ff007f;box-shadow:0 0 20px rgba(255,0,127,0.25), inset 0 0 15px rgba(255,0,127,0.08);}
.wsa-diagram-wrap:hover .wsa-r-hardware{border-color:#fbbf24;background:rgba(251,191,36,0.18);box-shadow:0 0 25px rgba(251,191,36,0.4), inset 0 0 15px rgba(251,191,36,0.12);}
</style>

<div class="wsa-wrap">
<div class="wsa-diagram-wrap">
<div class="wsa-r-user">
<span class="wsa-lbl wsa-lbl-user">User Mode</span>
<div class="wsa-r-kernel">
<span class="wsa-lbl wsa-lbl-kernel">Kernel Mode</span>
<div class="wsa-r-hardware">
<span class="wsa-lbl wsa-lbl-hw">Hardware</span>
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
print("Windows system architecture concentric rings updated and expanded!")
