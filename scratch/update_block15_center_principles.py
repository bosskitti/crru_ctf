import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    # Query lesson 165
    lesson = db.session.query(TutorialLesson).filter_by(id=165).first()
    if lesson:
        blocks = json.loads(lesson.content)
        
        # Prepare Block 15 HTML with:
        # 1. Centered grid layout (margin: 2rem auto)
        # 2. Rich explanations containing technical principles (UID, privilege separation, etc.) translated in kid-friendly tone
        blocks[15]['value'] = (
            "### 👥 Linux User Accounts (ประเภทบัญชีผู้ใช้ใน Linux)\n\n"
            "ในโลกของ Linux ระบบจะแบ่งประเภทผู้ใช้งานออกเป็น **3 บัญชีหลัก** ตามระดับความปลอดภัยและการเข้าถึงไฟล์ (Security Boundary) เพื่อให้คอมพิวเตอร์ทำงานได้อย่างเป็นระบบ ปลอดภัย และป้องกันการพังของระบบปฏิบัติการครับ:\n\n"
            "<style>\n"
            ".user-grid{display:flex;gap:20px;width:100%;max-width:820px;margin:2rem auto;}\n"
            ".user-card{flex:1;background:rgba(15, 17, 26, 0.6);border:1px solid rgba(255, 255, 255, 0.05);border-radius:12px;padding:24px 20px;display:flex;flex-direction:column;align-items:center;box-shadow:0 8px 32px rgba(0, 0, 0, 0.35);transition:all 0.3s ease;position:relative;}\n"
            ".user-card:hover{transform:translateY(-5px);}\n"
            ".user-card.type-root:hover{border-color:#ff007f;box-shadow:0 0 20px rgba(255, 0, 127, 0.25), 0 8px 32px rgba(0, 0, 0, 0.35);}\n"
            ".user-card.type-regular:hover{border-color:#00f0ff;box-shadow:0 0 20px rgba(0, 240, 255, 0.25), 0 8px 32px rgba(0, 0, 0, 0.35);}\n"
            ".user-card.type-service:hover{border-color:#3ddc84;box-shadow:0 0 20px rgba(61, 220, 132, 0.25), 0 8px 32px rgba(0, 0, 0, 0.35);}\n"
            ".user-icon{font-size:2.2rem;margin-bottom:16px;transition:transform 0.3s ease;}\n"
            ".user-card:hover .user-icon{transform:scale(1.1);}\n"
            ".user-card.type-root .user-icon{color:#ff007f;text-shadow:0 0 10px rgba(255, 0, 127, 0.4);}\n"
            ".user-card.type-regular .user-icon{color:#00f0ff;text-shadow:0 0 10px rgba(0, 240, 255, 0.4);}\n"
            ".user-card.type-service .user-icon{color:#3ddc84;text-shadow:0 0 10px rgba(61, 220, 132, 0.4);}\n\n"
            ".user-title{font-size:1.15rem;font-weight:800;margin-bottom:12px;color:#ffffff;}\n"
            ".user-badge{font-size:0.7rem;font-weight:800;padding:3px 8px;border-radius:4px;text-transform:uppercase;margin-bottom:18px;letter-spacing:0.05em;}\n"
            ".user-card.type-root .user-badge{background:rgba(255, 0, 127, 0.15);color:#ff007f;border:1px solid rgba(255, 0, 127, 0.25);}\n"
            ".user-card.type-regular .user-badge{background:rgba(0, 240, 255, 0.15);color:#00f0ff;border:1px solid rgba(0, 240, 255, 0.25);}\n"
            ".user-card.type-service .user-badge{background:rgba(61, 220, 132, 0.15);color:#3ddc84;border:1px solid rgba(61, 220, 132, 0.25);}\n\n"
            ".user-perms{list-style:none;padding:0;margin:0;width:100%;text-align:left;}\n"
            ".user-perms li{font-size:0.85rem;color:#cbd5e1;line-height:1.6;margin-bottom:10px;position:relative;padding-left:18px;}\n"
            ".user-perms li::before{content:'⚡';position:absolute;left:0;top:0;font-size:0.75rem;}\n"
            ".user-perms li span.highlight{color:#ffffff;font-weight:600;}\n"
            "@media (max-width:768px){\n"
            ".user-grid{flex-direction:column;align-items:center;}\n"
            "}\n"
            "</style>\n\n"
            "<div class=\"user-grid\">\n\n"
            "<!-- Card 1: Root User -->\n"
            "<div class=\"user-card type-root\">\n"
            "<div class=\"user-icon\"><i class=\"fas fa-user-shield\"></i></div>\n"
            "<div class=\"user-title\">Root User</div>\n"
            "<div class=\"user-badge\">Super User</div>\n"
            "<ul class=\"user-perms\">\n"
            "<li><strong>หัวหน้าใหญ่รหัส UID 0</strong>: บัญชีพิเศษที่มีหมายเลขประจำตัวเท่ากับ 0 ทำให้ข้ามกฎความปลอดภัยได้ทุกข้อ</li>\n"
            "<li><strong>สิทธิ์สูงสุดแบบไร้ขีดจำกัด</strong>: มีอำนาจเปิด อ่าน แก้ไข หรือลบไฟล์โครงสร้างระบบปฏิบัติการทั้งหมดในเครื่อง</li>\n"
            "<li><strong>ผู้ดูแลระบบหลัก (Admin)</strong>: มีหน้าที่จัดการลงโปรแกรม อัปเกรดความปลอดภัย และตั้งสิทธิ์ใช้งานให้ผู้ใช้อื่น</li>\n"
            "<li style=\"color: #ff99bb;\">⚠️ <strong>ความปลอดภัย:</strong> ไม่แนะนำให้ล็อกอินมาทำงานทั่วไป เพราะสิทธิ์ที่สูงเกินไปหากเผลอทำพลาดหรือโดนแฮก เครื่องจะเสียหายทันที</li>\n"
            "</ul>\n"
            "</div>\n\n"
            "<!-- Card 2: Regular User -->\n"
            "<div class=\"user-card type-regular\">\n"
            "<div class=\"user-icon\"><i class=\"fas fa-user\"></i></div>\n"
            "<div class=\"user-title\">Regular User</div>\n"
            "<div class=\"user-badge\">Standard User</div>\n"
            "<ul class=\"user-perms\">\n"
            "<li><strong>ผู้ใช้ทั่วไป (UID >= 1000)</strong>: บัญชีสำหรับใช้งานทั่วไปในชีวิตประจำวัน</li>\n"
            "<li><strong>กฎสิทธิ์ต่ำสุด (Least Privilege)</strong>: รันงานภายใต้สิทธิ์จำกัดเฉพาะเพื่อจำกัดวงความเสียหายของระบบ</li>\n"
            "<li><strong>ขอบเขตพื้นที่ส่วนตัว (~/home)</strong>: แก้ไขได้เฉพาะไฟล์ภายในโฟลเดอร์ของตนเองเท่านั้น ไม่สามารถยุ่งเกี่ยวไฟล์ผู้อื่นได้</li>\n"
            "<li><strong>ขอสิทธิ์ชั่วคราว (sudo)</strong>: ไม่สามารถลงแอปหรือแก้ไฟล์ระบบหลักได้เอง เว้นแต่จะได้รับอนุญาตขอยืมสิทธิ์ชั่วคราว</li>\n"
            "</ul>\n"
            "</div>\n\n"
            "<!-- Card 3: Service User -->\n"
            "<div class=\"user-card type-service\">\n"
            "<div class=\"user-icon\"><i class=\"fas fa-server\"></i></div>\n"
            "<div class=\"user-title\">Service User</div>\n"
            "<div class=\"user-badge\">System User</div>\n"
            "<ul class=\"user-perms\">\n"
            "<li><strong>ผู้ใช้ของบริการระบบ (UID 1-999)</strong>: บัญชีที่ระบบสร้างให้บอทหรือบริการหลังบ้าน (เช่น Apache, MySQL)</li>\n"
            "<li><strong>การแยกสิทธิ์ (Privilege Separation)</strong>: คอยรันแอปเฉพาะส่วน ป้องกันไม่ให้แอปแชร์ไฟล์ข้ามสิทธิ์กัน</li>\n"
            "<li><strong>บล็อกการยึดครองสิทธิ์</strong>: ออกแบบมาเพื่อจำกัดวงความเสียหาย หากแอปโดนเจาะ แฮกเกอร์ก็จะได้สิทธิ์แค่บอทตัวนี้ ไม่สามารถคุมสิทธิ์ root ได้</li>\n"
            "<li><strong>ไม่มีหน้าจอคำสั่ง (No-login)</strong>: ถูกตั้งค่าบล็อกสิทธิ์เพื่อไม่ให้มนุษย์สามารถพิมพ์ล็อกอินเข้าใช้งาน Shell ได้โดยตรง</li>\n"
            "</ul>\n"
            "</div>\n\n"
            "</div>"
        )
        
        lesson.content = json.dumps(blocks, ensure_ascii=False)
        db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
        db.session.commit()
        print("Lesson 165 Block 15 centered and updated with high-quality technical explanations!")
    else:
        print("Error: Lesson 165 not found!")
