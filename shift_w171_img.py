import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l171 = db.session.query(TutorialLesson).filter_by(id=171).first()
blocks = json.loads(l171.content)

# ─── Adjust Block 1 content to place the image AFTER the explanations ───
blocks[1]['value'] = """### 🏢 Web Application Architecture & Protocols

การตรวจสอบความปลอดภัยของเว็บแอปพลิเคชัน (Web Security) จำเป็นต้องมีความรู้ความเข้าใจในโครงสร้างสถาปัตยกรรม 3 ระดับหลัก (Three-Tier Architecture) และกระบวนการแลกเปลี่ยนข้อมูลผ่านโปรโตคอล HTTP:

<style>
.web-arch-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:2rem auto;max-width:1050px;}
@media(max-width:768px){.web-arch-grid{grid-template-columns:1fr;}}
.web-arch-card{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:20px;box-sizing:border-box;transition:all 0.25s ease;}
.web-arch-card:hover{border-color:#00f0ff;background:rgba(0,240,255,0.02);transform:translateY(-2px);box-shadow:0 0 15px rgba(0,240,255,0.25);}
.web-arch-title{font-size:0.92rem;font-weight:800;color:#00f0ff;margin-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.05);padding-bottom:6px;}
.web-arch-desc{font-size:0.8rem;color:#94a3b8;line-height:1.65;margin:0;}
.web-arch-desc strong{color:#fbbf24;}

.web-arch-img{display:block;width:100%;max-width:1050px;margin:2rem auto 1rem;border-radius:10px;border:1px solid rgba(255,255,255,0.08);box-shadow:0 8px 24px rgba(0,0,0,0.35);}
</style>

<div class="web-arch-grid">
<div class="web-arch-card">
<div class="web-arch-title">🌐 Web Front-End</div>
<p class="web-arch-desc">ส่วนนำเสนอผลลัพธ์บนเครื่องของฝั่งผู้ใช้ (Client-Side) เขียนด้วย <strong>HTML, CSS, JavaScript</strong> หน้าที่ทางความปลอดภัยคือตรวจสอบโครงสร้างหน้าเว็บและพฤติกรรมสคริปต์สิทธิ์สูง</p>
</div>
<div class="web-arch-card">
<div class="web-arch-title">⚙️ Web Back-End</div>
<p class="web-arch-desc">ส่วนประมวลผลคำขอระดับระบบเซิร์ฟเวอร์ (Server-Side) เช่น <strong>PHP, Python, Node.js</strong> ทำหน้าที่กรองข้อมูลอินพุตของผู้ใช้ จัดการเซสชันล็อกอิน และคุ้มครองไฟล์บนเว็บเซิร์ฟเวอร์</p>
</div>
<div class="web-arch-card">
<div class="web-arch-title">🗄️ Web Database</div>
<p class="web-arch-desc">ส่วนจัดเก็บข้อมูลหลักและประวัติบัญชี (Database Server) ด้วยภาษา <strong>SQL</strong> (MySQL, PostgreSQL) หากแอปพลิเคชันไม่กรองโค้ดอินพุตที่ดี จะส่งผลให้โดนโจมตีช่องโหว่ SQL Injection ได้</p>
</div>
</div>

<!-- Image placed AFTER the explanations -->
<img class="web-arch-img" src="/home/kali/.gemini/antigravity/brain/c824c6d8-15e7-4399-b27b-1656c82fe65a/media__1783560903040.png" alt="Web Application Architecture Diagram" />"""

l171.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=171).update({"content": l171.content})
db.session.commit()
print("Web architecture diagram successfully shifted to be below the card explanations in Lesson 171!")
ctx.pop()
