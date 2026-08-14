import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

# Query lesson 165
lesson = db.session.query(TutorialLesson).filter_by(id=165).first()
if not lesson:
    print("Lesson not found!")
    exit(1)

blocks = json.loads(lesson.content)

# The HTML/CSS code for premium user account cards (completely flat, 0-indentation)
html_user_cards = """### 👥 Linux User Accounts

ประเภทของบัญชีผู้ใช้งานระบบปฏิบัติการ Linux แบ่งตามระดับสิทธิ์ความปลอดภัยและการทำงานออกเป็น 3 ประเภทหลัก ดังนี้:

<style>
.user-grid{display:flex;gap:20px;width:100%;max-width:820px;margin:2rem 0;}
.user-card{flex:1;background:rgba(15, 17, 26, 0.6);border:1px solid rgba(255, 255, 255, 0.05);border-radius:12px;padding:24px 20px;display:flex;flex-direction:column;align-items:center;box-shadow:0 8px 32px rgba(0, 0, 0, 0.35);transition:all 0.3s ease;position:relative;}
.user-card:hover{transform:translateY(-5px);}
.user-card.type-root:hover{border-color:#ff007f;box-shadow:0 0 20px rgba(255, 0, 127, 0.25), 0 8px 32px rgba(0, 0, 0, 0.35);}
.user-card.type-regular:hover{border-color:#00f0ff;box-shadow:0 0 20px rgba(0, 240, 255, 0.25), 0 8px 32px rgba(0, 0, 0, 0.35);}
.user-card.type-service:hover{border-color:#3ddc84;box-shadow:0 0 20px rgba(61, 220, 132, 0.25), 0 8px 32px rgba(0, 0, 0, 0.35);}
.user-icon{font-size:2.2rem;margin-bottom:16px;transition:transform 0.3s ease;}
.user-card:hover .user-icon{transform:scale(1.1);}
.user-card.type-root .user-icon{color:#ff007f;text-shadow:0 0 10px rgba(255, 0, 127, 0.4);}
.user-card.type-regular .user-icon{color:#00f0ff;text-shadow:0 0 10px rgba(0, 240, 255, 0.4);}
.user-card.type-service .user-icon{color:#3ddc84;text-shadow:0 0 10px rgba(61, 220, 132, 0.4);}

.user-title{font-size:1.15rem;font-weight:800;margin-bottom:12px;color:#ffffff;}
.user-badge{font-size:0.7rem;font-weight:800;padding:3px 8px;border-radius:4px;text-transform:uppercase;margin-bottom:18px;letter-spacing:0.05em;}
.user-card.type-root .user-badge{background:rgba(255, 0, 127, 0.15);color:#ff007f;border:1px solid rgba(255, 0, 127, 0.25);}
.user-card.type-regular .user-badge{background:rgba(0, 240, 255, 0.15);color:#00f0ff;border:1px solid rgba(0, 240, 255, 0.25);}
.user-card.type-service .user-badge{background:rgba(61, 220, 132, 0.15);color:#3ddc84;border:1px solid rgba(61, 220, 132, 0.25);}

.user-perms{list-style:none;padding:0;margin:0;width:100%;text-align:left;}
.user-perms li{font-size:0.85rem;color:#cbd5e1;line-height:1.6;margin-bottom:10px;position:relative;padding-left:18px;}
.user-perms li::before{content:'⚡';position:absolute;left:0;top:0;font-size:0.75rem;}
.user-perms li span.highlight{color:#ffffff;font-weight:600;}
@media (max-width:768px){
.user-grid{flex-direction:column;}
}
</style>

<div class="user-grid">

<!-- Card 1: Root User -->
<div class="user-card type-root">
<div class="user-icon"><i class="fas fa-user-shield"></i></div>
<div class="user-title">Root User</div>
<div class="user-badge">Super User</div>
<ul class="user-perms">
<li>ถูกสร้างขึ้นโดยอัตโนมัติระหว่างการติดตั้งระบบ</li>
<li>มีสิทธิ์สูงสุด (<span class="highlight">Superuser</span>) ในการเข้าถึงและควบคุมระบบปฏิบัติการทั้งหมด</li>
<li>สามารถเข้าถึง อ่าน เขียน หรือแก้ไขไฟล์ที่ถูกจำกัด (<span class="highlight">Restricted files</span>) ได้ทุกไฟล์</li>
<li>มีสิทธิ์ติดตั้งหรือลบโปรแกรม และแก้ไขไฟล์กำหนดการทำงานหลักระบบ</li>
<li>จำเป็นสำหรับงานดูแลระบบ แต่ไม่แนะนำให้ใช้ล็อกอินทั่วไปเพื่อความปลอดภัย</li>
</ul>
</div>

<!-- Card 2: Regular User -->
<div class="user-card type-regular">
<div class="user-icon"><i class="fas fa-user"></i></div>
<div class="user-title">Regular User</div>
<div class="user-badge">Standard User</div>
<ul class="user-perms">
<li>ถูกสร้างขึ้นโดยผู้ดูแลระบบเพื่อใช้ในการทำงานทั่วไป</li>
<li>ไฟล์และโฟลเดอร์ส่วนตัวทั้งหมดจะถูกเก็บในโฮมไดเรกทอรี (<span class="highlight">~/home/$USER</span>)</li>
<li>ไม่มีสิทธิ์เข้าถึงหรือยุ่งเกี่ยวในไดเรกทอรีส่วนตัวของผู้ใช้รายอื่น</li>
<li>ไม่ได้รับอนุญาตให้แก้ไขไฟล์ระบบหลัก หรือติดตั้งซอฟต์แวร์โดยไม่มีคำสั่งพิเศษ</li>
<li>เหมาะสำหรับการใช้งานเอกสาร ท่องเว็บ และทำงานส่วนตัวที่ไม่ส่งผลกระทบต่อแกนระบบ</li>
</ul>
</div>

<!-- Card 3: Service User -->
<div class="user-card type-service">
<div class="user-icon"><i class="fas fa-server"></i></div>
<div class="user-title">Service User</div>
<div class="user-badge">System User</div>
<ul class="user-perms">
<li>ถูกสร้างขึ้นโดยระบบเพื่อรองรับกระบวนการทำงานเบื้องหลังของบริการต่างๆ</li>
<li>ผู้ให้บริการหลักอย่าง <span class="highlight">Apache</span>, <span class="highlight">Squid</span>, อีเมล หรือฐานข้อมูล จะมีบัญชีเฉพาะตัวนี้รันงาน</li>
<li>ถูกจำกัดการเข้าถึงและสิทธิ์ทรัพยากรเฉพาะจุดตามหน้าที่งานบริการเท่านั้น</li>
<li>เพิ่มความปลอดภัยโดยป้องกันการถูกแฮกแอปพลิเคชันไปยึดครองระดับสิทธิ์ root</li>
<li>มักจะถูกระงับสิทธิ์ไม่ให้ล็อกอินเข้าใช้เครื่องคอมพิวเตอร์ผ่าน Terminal โดยตรง</li>
</ul>
</div>

</div>"""

# Replace block 15 with our premium user cards
blocks[15]['value'] = html_user_cards

# Save and Commit
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
db.session.commit()

print("User Accounts block 15 updated with card grid layout successfully!")
