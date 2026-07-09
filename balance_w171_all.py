import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l171 = db.session.query(TutorialLesson).filter_by(id=171).first()
blocks = json.loads(l171.content)

# ─── Upgrade Front-End and Database cards with sub-details for layout balance ───
blocks[1]['value'] = """### 🏢 Web Application Architecture & Protocols

การตรวจสอบความปลอดภัยของเว็บแอปพลิเคชัน (Web Security) จำเป็นต้องมีความรู้ความเข้าใจในโครงสร้างสถาปัตยกรรม 3 ระดับหลัก (Three-Tier Architecture) และกระบวนการแลกเปลี่ยนข้อมูลผ่านโปรโตคอล HTTP:

<style>
/* Main 3-tier grid: Middle column is twice as wide */
.web-arch-grid{display:grid;grid-template-columns:1.2fr 2fr 1.2fr;gap:16px;margin:2rem auto 1rem;max-width:1050px;}
@media(max-width:990px){.web-arch-grid{grid-template-columns:1fr;}}

.web-arch-card{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:20px;box-sizing:border-box;transition:all 0.25s ease;display:flex;flex-direction:column;justify-content:between;}
.web-arch-card:hover{border-color:#00f0ff;background:rgba(0,240,255,0.02);transform:translateY(-2px);box-shadow:0 0 15px rgba(0,240,255,0.25);}
.web-arch-title{font-size:0.92rem;font-weight:800;color:#00f0ff;margin-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.05);padding-bottom:6px;}
.web-arch-desc{font-size:0.8rem;color:#94a3b8;line-height:1.65;margin:0 0 8px;}
.web-arch-desc strong{color:#fbbf24;}

/* Horizontal layout inside cards */
.backend-internal-horizontal{display:flex;gap:12px;margin-top:12px;}
@media(max-width:600px){.backend-internal-horizontal{flex-direction:column;}}

.be-sub-card{flex:1;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:12px;box-sizing:border-box;display:flex;flex-direction:column;justify-content:between;}
.be-sub-hdr{font-size:0.75rem;font-weight:800;color:#fbbf24;margin-bottom:4px;text-transform:uppercase;letter-spacing:0.03em;}
.be-sub-desc{font-size:0.72rem;color:#94a3b8;line-height:1.55;margin:0;}

.web-arch-img{display:block;width:100%;max-width:1050px;margin:2rem auto 1rem;border-radius:10px;border:1px solid rgba(255,255,255,0.08);box-shadow:0 8px 24px rgba(0,0,0,0.35);}
</style>

<!-- 3-tier Grid with horizontal nested layouts -->
<div class="web-arch-grid">
<!-- Front-End (Left - Details added) -->
<div class="web-arch-card">
<div>
<div class="web-arch-title">🌐 Web Front-End (Client-Side)</div>
<p class="web-arch-desc">แสดงผลและรับอินพุตฝั่งผู้ใช้ผ่านเว็บเบราว์เซอร์ โดยมีสแต็คเทคโนโลยีการทำงานย่อย:</p>
<div class="backend-internal-horizontal" style="flex-direction:column; gap:6px; margin-top:8px;">
<div class="be-sub-card" style="border-left:2px solid #00f0ff; padding:8px 10px;">
<span class="be-sub-hdr" style="font-size:0.7rem; color:#00f0ff;">HTML & CSS</span>
<p class="be-sub-desc" style="font-size:0.68rem;">จัดโครงสร้างมาร์กอัปหน้าเว็บ และตกแต่งหน้ากาก UI</p>
</div>
<div class="be-sub-card" style="border-left:2px solid #fbbf24; padding:8px 10px;">
<span class="be-sub-hdr" style="font-size:0.7rem; color:#fbbf24;">JavaScript</span>
<p class="be-sub-desc" style="font-size:0.68rem;">ประมวลผลตรรกะฝั่งไคลเอนต์ ดักจับอีเวนต์ และรัน Dynamic DOM</p>
</div>
</div>
</div>
</div>

<!-- Back-End (Middle - 3 internal cards lined up horizontally) -->
<div class="web-arch-card" style="border-color:rgba(0,240,255,0.15);">
<div>
<div class="web-arch-title" style="color:#ffffff;">⚙️ Web Back-End (Server-Side)</div>
<p class="web-arch-desc">ส่วนประมวลผลตรรกะระบบบนเครื่องเซิร์ฟเวอร์หลัก โดยประกอบไปด้วย <strong>3 องค์ประกอบภายในหลัก</strong> จัดวางทำงานขนานกัน:</p>

<div class="backend-internal-horizontal">
<!-- Web Server -->
<div class="be-sub-card" style="border-top:2px solid #00f0ff;">
<div class="be-sub-hdr">1. Web Server</div>
<p class="be-sub-desc">รับส่ง HTTP Requests/Responses และกรองข้อมูลภายนอก (Apache, Nginx)</p>
</div>

<!-- Application Server -->
<div class="be-sub-card" style="border-top:2px solid #fbbf24;">
<div class="be-sub-hdr">2. App Server</div>
<p class="be-sub-desc">ประมวลผล Business Logic รันซอร์สโค้ด (PHP, Python, Node.js)</p>
</div>

<!-- Session Management -->
<div class="be-sub-card" style="border-top:2px solid #3ddc84;">
<div class="be-sub-hdr">🔑 Session</div>
<p class="be-sub-desc">ดูแลรักษาความปลอดภัยเซสชันล็อกอินระหว่าง Server และแอป</p>
</div>
</div>
</div>
</div>

<!-- Database (Right - Details added) -->
<div class="web-arch-card">
<div>
<div class="web-arch-title">🗄️ Web Database (Database)</div>
<p class="web-arch-desc">ส่วนจัดเก็บข้อมูลหลักที่เซิร์ฟเวอร์หลังบ้านเรียกขอและอ้างอิงเพื่อวิเคราะห์สิทธิ์:</p>
<div class="backend-internal-horizontal" style="flex-direction:column; gap:6px; margin-top:8px;">
<div class="be-sub-card" style="border-left:2px solid #3ddc84; padding:8px 10px;">
<span class="be-sub-hdr" style="font-size:0.7rem; color:#3ddc84;">SQL Language</span>
<p class="be-sub-desc" style="font-size:0.68rem;">ภาษาเขียนคำสั่งสืบค้นและจัดการตารางโครงสร้างข้อมูล</p>
</div>
<div class="be-sub-card" style="border-left:2px solid #ab20fd; padding:8px 10px;">
<span class="be-sub-hdr" style="font-size:0.7rem; color:#ab20fd;">DBMS Systems</span>
<p class="be-sub-desc" style="font-size:0.68rem;">ระบบจัดการฐานข้อมูลความปลอดภัยสูง (MySQL, PostgreSQL)</p>
</div>
</div>
</div>
</div>
</div>

<!-- Image placed AFTER the explanations -->
<img class="web-arch-img" src="/home/kali/.gemini/antigravity/brain/c824c6d8-15e7-4399-b27b-1656c82fe65a/media__1783560903040.png" alt="Web Application Architecture Diagram" />"""

l171.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=171).update({"content": l171.content})
db.session.commit()
print("Front-End and Database cards successfully updated with corresponding sub-details!")
ctx.pop()
