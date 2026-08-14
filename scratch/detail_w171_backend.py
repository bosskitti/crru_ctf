import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l171 = db.session.query(TutorialLesson).filter_by(id=171).first()
blocks = json.loads(l171.content)

# ─── Update Block 1 to explain the two internal parts of Web Back-End (Web Server & Application Server) ───
blocks[1]['value'] = """### 🏢 Web Application Architecture & Protocols

การตรวจสอบความปลอดภัยของเว็บแอปพลิเคชัน (Web Security) จำเป็นต้องมีความรู้ความเข้าใจในโครงสร้างสถาปัตยกรรม 3 ระดับหลัก (Three-Tier Architecture) และกระบวนการแลกเปลี่ยนข้อมูลผ่านโปรโตคอล HTTP:

<style>
.web-arch-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:2rem auto;max-width:1050px;}
@media(max-width:820px){.web-arch-grid{grid-template-columns:1fr;}}
.web-arch-card{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:20px;box-sizing:border-box;transition:all 0.25s ease;display:flex;flex-direction:column;}
.web-arch-card:hover{border-color:#00f0ff;background:rgba(0,240,255,0.02);transform:translateY(-2px);box-shadow:0 0 15px rgba(0,240,255,0.25);}
.web-arch-title{font-size:0.92rem;font-weight:800;color:#00f0ff;margin-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.05);padding-bottom:6px;}
.web-arch-desc{font-size:0.8rem;color:#94a3b8;line-height:1.65;margin:0 0 8px;}
.web-arch-desc:last-child{margin-bottom:0;}
.web-arch-desc strong{color:#fbbf24;}
.web-arch-subsect{margin-top:6px;padding-top:6px;border-top:1px dashed rgba(255,255,255,0.05);}
.web-arch-sub-title{font-size:0.78rem;font-weight:700;color:#fbbf24;margin-bottom:2px;}

.web-arch-img{display:block;width:100%;max-width:1050px;margin:2rem auto 1rem;border-radius:10px;border:1px solid rgba(255,255,255,0.08);box-shadow:0 8px 24px rgba(0,0,0,0.35);}
</style>

<div class="web-arch-grid">
<!-- Front-End -->
<div class="web-arch-card">
<div class="web-arch-title">🌐 Web Front-End (Client-Side)</div>
<p class="web-arch-desc">ส่วนประมวลผลบนบราวเซอร์ของผู้ใช้งานหลัก รันและจัดโครงสร้างด้วยภาษา <strong>HTML, CSS และ JavaScript</strong> เพื่อวาดหน้าจอรับส่งข้อมูล</p>
</div>

<!-- Back-End with 2 internal parts explained -->
<div class="web-arch-card">
<div class="web-arch-title">⚙️ Web Back-End (Server-Side)</div>
<p class="web-arch-desc">ประมวลผลตรรกะระบบบนเครื่องเซิร์ฟเวอร์ โดยประกอบด้วย <strong>2 ส่วนทำงานภายในหลัก</strong> ตามแผนภาพด้านล่าง:</p>

<div class="web-arch-subsect">
<div class="web-arch-sub-title">1. Web Server</div>
<p class="web-arch-desc" style="font-size:0.75rem;">(เช่น Apache, Nginx, IIS) ทำหน้าที่รับส่งสัญญาณ HTTP Requests/Responses และคอยกรองประมวลผลคำขอเบื้องต้น</p>
</div>

<div class="web-arch-subsect">
<div class="web-arch-sub-title">2. Application Server</div>
<p class="web-arch-desc" style="font-size:0.75rem;">(เช่น PHP Engine, Python, Node.js) ประมวลผลคำสั่งเชิงลึก (Business Logic) ตรวจสอบสิทธิ์ และรันงานซอร์สโค้ดหลัก</p>
</div>

<div class="web-arch-subsect" style="border-top:1px solid rgba(0,240,255,0.1); padding-top:4px;">
<p class="web-arch-desc" style="font-size:0.75rem; color:#00f0ff;">🔑 <strong>Session Management</strong>: ระบบคอยจัดการและรักษาความปลอดภัยเซสชันของผู้ใช้ระหว่าง Web Server และ Application Server</p>
</div>
</div>

<!-- Database -->
<div class="web-arch-card">
<div class="web-arch-title">🗄️ Web Database (Database Server)</div>
<p class="web-arch-desc">ส่วนเก็บข้อมูลหลักระดับฐานข้อมูล เช่น <strong>SQL Server</strong> (MySQL, PostgreSQL) คอยรับและประมวลผล Query ข้อมูลผ่านสคริปต์หลังบ้าน</p>
</div>
</div>

<!-- Image placed AFTER the explanations -->
<img class="web-arch-img" src="/home/kali/.gemini/antigravity/brain/c824c6d8-15e7-4399-b27b-1656c82fe65a/media__1783560903040.png" alt="Web Application Architecture Diagram" />"""

l171.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=171).update({"content": l171.content})
db.session.commit()
print("Web Back-End card successfully updated to detail Web Server and Application Server internals!")
ctx.pop()
