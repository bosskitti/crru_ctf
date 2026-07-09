import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l171 = db.session.query(TutorialLesson).filter_by(id=171).first()
blocks = json.loads(l171.content)

# ─── Rewrite Block 1 to balance the main cards and lay out Back-End internals horizontally below them ───
blocks[1]['value'] = """### 🏢 Web Application Architecture & Protocols

การตรวจสอบความปลอดภัยของเว็บแอปพลิเคชัน (Web Security) จำเป็นต้องมีความรู้ความเข้าใจในโครงสร้างสถาปัตยกรรม 3 ระดับหลัก (Three-Tier Architecture) และกระบวนการแลกเปลี่ยนข้อมูลผ่านโปรโตคอล HTTP:

<style>
/* Main 3-tier grid */
.web-arch-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:2rem auto 1rem;max-width:1050px;}
@media(max-width:820px){.web-arch-grid{grid-template-columns:1fr;}}
.web-arch-card{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:20px;box-sizing:border-box;transition:all 0.25s ease;display:flex;flex-direction:column;justify-content:between;}
.web-arch-card:hover{border-color:#00f0ff;background:rgba(0,240,255,0.02);transform:translateY(-2px);box-shadow:0 0 15px rgba(0,240,255,0.25);}
.web-arch-title{font-size:0.92rem;font-weight:800;color:#00f0ff;margin-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.05);padding-bottom:6px;}
.web-arch-desc{font-size:0.8rem;color:#94a3b8;line-height:1.65;margin:0;}
.web-arch-desc strong{color:#fbbf24;}

/* Horizontal Sub-grid for Back-End internals */
.be-internals-title{font-size:0.85rem;font-weight:800;color:#ffffff;margin:2rem auto 0.8rem;max-width:1050px;font-family:'JetBrains Mono',monospace;display:flex;align-items:center;gap:8px;}
.be-internals-title::before{content:"";display:inline-block;width:4px;height:14px;background:#fbbf24;}

.be-internals-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:0 auto 2rem;max-width:1050px;}
@media(max-width:820px){.be-internals-grid{grid-template-columns:1fr;}}
.be-internal-card{background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:16px;box-sizing:border-box;}
.be-internal-hdr{font-size:0.78rem;font-weight:800;color:#fbbf24;margin-bottom:6px;text-transform:uppercase;letter-spacing:0.04em;}
.be-internal-desc{font-size:0.76rem;color:#94a3b8;line-height:1.6;margin:0;}

.web-arch-img{display:block;width:100%;max-width:1050px;margin:2rem auto 1rem;border-radius:10px;border:1px solid rgba(255,255,255,0.08);box-shadow:0 8px 24px rgba(0,0,0,0.35);}
</style>

<!-- Top level 3-tier Grid (Balanced heights) -->
<div class="web-arch-grid">
<!-- Front-End -->
<div class="web-arch-card">
<div>
<div class="web-arch-title">🌐 Web Front-End (Client)</div>
<p class="web-arch-desc">ส่วนนำเสนอผลลัพธ์บนเครื่องของฝั่งผู้ใช้งานหลัก รันและจัดโครงสร้างด้วยภาษา <strong>HTML, CSS และ JavaScript</strong> เพื่อสร้างและวาดหน้าจอรับส่งข้อมูล</p>
</div>
</div>

<!-- Back-End (Balanced description) -->
<div class="web-arch-card">
<div>
<div class="web-arch-title">⚙️ Web Back-End (Server)</div>
<p class="web-arch-desc">ส่วนประมวลผลตรรกะระบบบนเครื่องเซิร์ฟเวอร์หลัก ทำหน้าที่รับข้อมูลอินพุต ตรวจสอบสิทธิ์ และรันโค้ดระบบหลังบ้าน (ดูรายละเอียดองค์ประกอบภายในด้านล่าง)</p>
</div>
</div>

<!-- Database -->
<div class="web-arch-card">
<div>
<div class="web-arch-title">🗄️ Web Database (Database)</div>
<p class="web-arch-desc">ส่วนจัดเก็บและจัดการข้อมูลหลักของระบบ (Database Server) ด้วยภาษา <strong>SQL</strong> คอยประมวลผล Query ข้อมูลผ่านสคริปต์ส่งคำสั่งหลังบ้าน</p>
</div>
</div>
</div>

<!-- Section Title for Internals -->
<div class="be-internals-title">⚙️ Web Back-End Internal Components (องค์ประกอบภายในระบบหลังบ้าน)</div>

<!-- Horizontal Sub-grid detailing Back-End internals -->
<div class="be-internals-grid">
<!-- Web Server -->
<div class="be-internal-card" style="border-left:2px solid #00f0ff;">
<div class="be-internal-hdr">1. Web Server</div>
<p class="be-internal-desc">ทำหน้าที่จัดการรับส่งข้อมูลและสัญญาณ HTTP Requests/Responses และคอยจัดการไฟล์นิ่งภายนอก (e.g. Apache, Nginx, IIS)</p>
</div>

<!-- Application Server -->
<div class="be-internal-card" style="border-left:2px solid #fbbf24;">
<div class="be-internal-hdr">2. Application Server</div>
<p class="be-internal-desc">ทำหน้าที่รันและประมวลผลตรรกะคำสั่งเชิงลึก (Business Logic) ตรวจสอบความถูกต้อง และประมวลผลซอร์สโค้ด (e.g. PHP, Python, Node.js)</p>
</div>

<!-- Session Management -->
<div class="be-internal-card" style="border-left:2px solid #3ddc84;">
<div class="be-internal-hdr">🔑 Session Management</div>
<p class="be-internal-desc">ระบบควบคุมดูแลรักษาความปลอดภัยและจดจำสถานะการล็อกอินของผู้ใช้ (State) ระหว่าง Web Server และ Application Server</p>
</div>
</div>

<!-- Image placed AFTER the explanations -->
<img class="web-arch-img" src="/home/kali/.gemini/antigravity/brain/c824c6d8-15e7-4399-b27b-1656c82fe65a/media__1783560903040.png" alt="Web Application Architecture Diagram" />"""

l171.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=171).update({"content": l171.content})
db.session.commit()
print("Web Back-End internals successfully redesigned into balanced horizontal rows!")
ctx.pop()
