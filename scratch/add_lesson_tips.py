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
        
        # 1. Add Tip 1 about /etc/shadow into Block 13 (before the tree chart)
        tip_1_html = (
            "<div style=\"background: rgba(255, 0, 127, 0.04); border: 1px dashed rgba(255, 0, 127, 0.3); border-radius: 12px; padding: 20px; margin: 1.5rem auto; max-width: 820px; text-align: left; box-shadow: 0 0 15px rgba(255, 0, 127, 0.05);\">\n"
            "  <div style=\"font-weight: 800; color: #ff007f; font-size: 0.95rem; display: flex; align-items: center; gap: 8px; margin-bottom: 8px;\">\n"
            "    🏴‍☠️ HACKER TIP: คลังแสงความลับใน /etc/shadow\n"
            "  </div>\n"
            "  <p style=\"color: #cbd5e1; font-size: 0.85rem; line-height: 1.6; margin: 0;\">\n"
            "    น้องๆ รู้ไหมครับว่า ในสมัยก่อนรหัสผ่านของระบบจะถูกเก็บไว้ดื้อๆ ในไฟล์ <code>/etc/passwd</code> เลย แต่เพราะไฟล์นี้จำเป็นต้องเปิดให้ใครก็ได้เปิดอ่านได้ (World-Readable) เพื่อเช็กข้อมูลยูสเซอร์ มันจึงอันตรายมาก! ลินุกซ์ยุคใหม่จึงย้ายรหัสผ่านจริงที่เข้ารหัสลับแล้วไปเก็บไว้ที่ <strong><code>/etc/shadow</code></strong> ซึ่งล็อกไว้ให้เฉพาะสิทธิ์ <strong>Root User</strong> อ่านได้เท่านั้น! เวลาที่แฮกเกอร์โจมตีเป้าหมายด้วยช่องโหว่ประเภท LFI (Local File Inclusion) สิ่งที่พวกเขาพยายามค้นหาและดึงออกมาแครกถอดรหัสก็คือไฟล์ shadow นี้นี่เองครับ!\n"
            "  </p>\n"
            "</div>\n\n"
        )
        
        b13_val = blocks[13]['value']
        style_idx_13 = b13_val.find("<style>")
        if style_idx_13 != -1:
            interactive_code_13 = b13_val[style_idx_13:]
        else:
            interactive_code_13 = b13_val
            
        new_intro_b13 = (
            "### 📂 Linux Important Files & Sub-Trees Map (แผนผังไฟล์สำคัญในระบบ Linux)\n\n"
            "ในป่าโฟลเดอร์ของ Linux มี **\"ไฟล์การตั้งค่าระบบที่สำคัญ\"** ซ่อนอยู่ตามกิ่งก้านต่างๆ เต็มไปหมดเลยครับ! เปรียบเหมือนแผนผังห้องลับที่น้องๆ ต้องรู้ว่าไฟล์ไหนควบคุมอะไร (เช่น ไฟล์เก็บชื่อผู้ใช้ หรือไฟล์เก็บรหัสผ่านที่เข้ารหัสลับไว้) \n\n"
            "น้องๆ ลองเลื่อนเมาส์ชี้หรือจิ้มไปที่ชื่อไฟล์แต่ละกิ่งด้านล่าง เพื่อแอบดูรายละเอียดและสืบค้นความสำคัญของมันได้เลยครับ! 👇\n\n"
        )
        blocks[13]['value'] = new_intro_b13 + tip_1_html + interactive_code_13
        
        # 2. Add Tip 2 about sudo vs root into Block 15 (after the cards grid)
        tip_2_html = (
            "\n\n<div style=\"background: rgba(0, 240, 255, 0.04); border: 1px dashed rgba(0, 240, 255, 0.3); border-radius: 12px; padding: 20px; margin: 2rem auto 0 auto; max-width: 820px; text-align: left; box-shadow: 0 0 15px rgba(0, 240, 255, 0.05);\">\n"
            "  <div style=\"font-weight: 800; color: #00f0ff; font-size: 0.95rem; display: flex; align-items: center; gap: 8px; margin-bottom: 8px;\">\n"
            "    🛡️ CYBER SECURITY TIP: ทำไมแฮกเกอร์ตัวจริงถึงไม่ชอบล็อกอินเป็น Root?\n"
            "  </div>\n"
            "  <p style=\"color: #cbd5e1; font-size: 0.85rem; line-height: 1.6; margin: 0;\">\n"
            "    ในการใช้งานจริงและระบบรักษาความปลอดภัยระดับสากล <strong>เราจะไม่ใช้งานสิทธิ์ Root โดยตรง</strong> เด็ดขาดครับ! เพราะการพิมพ์คำสั่งภายใต้ Root หากเผลอพิมพ์ผิด เช่น <code>rm -rf /</code> เครื่องจะลบตัวเองพังพินาศทันทีโดยไม่มีการเตือน! แฮกเกอร์และผู้ดูแลระบบที่ชาญฉลาดจึงมักล็อกอินด้วยสิทธิ์บัญชีผู้ใช้ทั่วไป (Regular User) แล้วใช้คำสั่ง <strong><code>sudo</code> (SuperUser DO)</strong> เพื่อขอยืมพลังของ Root มารันคำสั่งเดี่ยวๆ เป็นครั้งคราวเท่านั้น ซึ่งวิธีนี้นอกจากจะปลอดภัยแล้ว ยังช่วยให้ระบบสามารถบันทึกประวัติการใช้สิทธิ์ (Audit Logs) เพื่อตรวจสอบได้ด้วยว่าใครเป็นคนขอยืมสิทธิ์ไปแก้ไขระบบครับ!\n"
            "  </p>\n"
            "</div>"
        )
        
        b15_val = blocks[15]['value']
        # Append the tip to the end of b15_val
        blocks[15]['value'] = b15_val + tip_2_html
        
        lesson.content = json.dumps(blocks, ensure_ascii=False)
        db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
        db.session.commit()
        print("Lesson 165 successfully updated with Cybersecurity Hacker & Security tips!")
    else:
        print("Error: Lesson 165 not found!")
