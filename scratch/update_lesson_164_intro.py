import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    # Query lesson 164
    lesson = db.session.query(TutorialLesson).filter_by(id=164).first()
    if lesson:
        blocks = json.loads(lesson.content)
        
        # Define friendly block 0 content wrapped in a beautiful, colorful cyber box with glowing text highlights
        blocks[0]['value'] = (
            "<div style=\"background: linear-gradient(135deg, rgba(15, 23, 42, 0.65), rgba(30, 41, 59, 0.45)); border: 1px solid rgba(0, 240, 255, 0.2); border-left: 5px solid #00f0ff; border-radius: 12px; padding: 24px; margin-bottom: 2rem; box-shadow: 0 8px 32px rgba(0, 240, 255, 0.05), inset 0 0 15px rgba(0, 240, 255, 0.02); text-align: left; line-height: 1.8;\">"
            "<h2 style=\"margin: 0 0 12px; font-size: 1.45rem; font-weight: 800; color: #00f0ff; text-shadow: 0 0 10px rgba(0,240,255,0.4); display: flex; align-items: center; gap: 10px;\">"
            "<span>🛡️</span> ความรู้เบื้องต้นเกี่ยวกับระบบปฏิบัติการ (Introduction to OS)"
            "</h2>"
            "<p style=\"margin: 0 0 16px; font-weight: 700; color: #ff007f; font-size: 0.95rem; text-transform: uppercase; letter-spacing: 0.05em; text-shadow: 0 0 8px rgba(255,0,127,0.3);\">"
            "🚀 Chapter 02: Cybersecurity Operating Systems"
            "</p>"
            "<hr style=\"border: 0; border-top: 1px solid rgba(255, 255, 255, 0.08); margin: 16px 0;\">"
            "<p style=\"color: #f1f5f9; font-size: 1rem; font-weight: 500; margin: 0 0 12px;\">"
            "สวัสดีครับน้องๆ! ยินดีต้อนรับเข้าสู่บทเรียนสุดเท่ใน <span style=\"color: #ff007f; font-weight: 700; text-shadow: 0 0 8px rgba(255,0,127,0.3);\">Chapter 02</span> นะครับ! 🎉"
            "</p>"
            "<p style=\"color: #cbd5e1; font-size: 0.95rem; margin: 0 0 12px;\">"
            "เคยวาดฝันอยากเป็น <span style=\"color: #fbbf24; font-weight: 700; text-shadow: 0 0 8px rgba(251,191,36,0.3);\">\"แฮกเกอร์\"</span> เท่ๆ แบบในหนังไหม? หรือเคยสงสัยไหมว่าเวลาที่พี่ๆ นักวิเคราะห์ความปลอดภัยเขาตามล่ามัลแวร์ตัวร้ายในโลกไซเบอร์ เขาทำได้ยังไงกัน?"
            "</p>"
            "<p style=\"color: #cbd5e1; font-size: 0.95rem; margin: 0 0 12px;\">"
            "คำตอบก็คือ... พวกเขาต้องรู้จักและควบคุม <span style=\"color: #00f0ff; font-weight: 700; text-shadow: 0 0 8px rgba(0,240,255,0.3);\">\"พี่ใหญ่\"</span> ที่คอยคุมเครื่องคอมพิวเตอร์และเซิร์ฟเวอร์ทุกเครื่องในโลกก่อนครับ ซึ่งนั่นก็คือ <span style=\"color: #3ddc84; font-weight: 700; text-shadow: 0 0 8px rgba(61,220,132,0.3);\">ระบบปฏิบัติการ (Operating System หรือ OS)</span> นั่นเอง!"
            "</p>"
            "<p style=\"color: #cbd5e1; font-size: 0.95rem; margin: 0;\">"
            "แต่ก่อนที่เราจะไปเจาะลึกระบบปฏิบัติการเจ๋งๆ อย่าง <span style=\"color: #a855f7; font-weight: 700; text-shadow: 0 0 8px rgba(168,85,247,0.3);\">Linux</span> ที่ใช้ในการแฮกข้อมูลและการป้องกันภัยไซเบอร์ เรามาลองรื้อดูชิ้นส่วนและสถาปัตยกรรมของคอมพิวเตอร์คู่ใจกันก่อนว่า มันมีองค์ประกอบอะไรบ้างและคุยกันอย่างไรในหัวข้อแรกกันเลยครับ! 🚀"
            "</p>"
            "</div>"
        )
        
        lesson.content = json.dumps(blocks, ensure_ascii=False)
        db.session.query(TutorialLesson).filter_by(id=164).update({"content": lesson.content})
        db.session.commit()
        print("Lesson 164 Block 0 updated successfully with colorful HTML box text!")
    else:
        print("Error: Lesson 164 not found in database!")
