import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    # Read block 13's current value first
    lesson = db.session.query(TutorialLesson).filter_by(id=164).first()
    if lesson:
        blocks = json.loads(lesson.content)
        
        # 1. Update Block 11 (Download OS resources for testing)
        blocks[11]['value'] = (
            "### 📌 แหล่งดาวน์โหลดระบบปฏิบัติการสำหรับทดสอบ\n\n"
            "<div style=\"background: rgba(15, 17, 26, 0.45); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 12px; padding: 24px; margin: 1.5rem 0; text-align: left;\">"
            "<p style=\"color: #cbd5e1; font-size: 0.95rem; line-height: 1.7; margin: 0 0 20px;\">"
            "เคยสงสัยไหมว่านักทดสอบระบบหรือแฮกเกอร์หมวกขาวเขาฝึกเจาะระบบกันยังไงโดยไม่ทำให้คอมพิวเตอร์ตัวเองพัง? 🛠️ คำตอบคือพวกเขาจะใช้ <strong>\"เครื่องจำลองระบบ (Virtual Machine)\"</strong> เพื่อเปิดระบบปฏิบัติการเสมือนขึ้นมารันครับ! และนี่คือ <strong>\"3 แหล่งดาวน์โหลดขุมทรัพย์\"</strong> ที่แจกตัวระบบปฏิบัติการสำเร็จรูปให้น้องๆ โหลดไปลองรันเล่นเพื่อศึกษาได้ทันที:"
            "</p>"
            "<div style=\"display: flex; flex-direction: column; gap: 16px;\">"
            "<div style=\"display: flex; align-items: center; justify-content: space-between; gap: 16px; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 16px; transition: all 0.3s;\" onmouseover=\"this.style.borderColor='#00f0ff'; this.style.boxShadow='0 0 12px rgba(0,240,255,0.2)';\" onmouseout=\"this.style.borderColor='rgba(255,255,255,0.08)'; this.style.boxShadow='none';\">"
            "<div style=\"text-align: left;\">"
            "<span style=\"font-weight: 700; color: #00f0ff; font-size: 1rem;\">📦 OSBoxes</span>"
            "<p style=\"color: #cbd5e1; font-size: 0.85rem; margin: 4px 0 0;\">แหล่งแจกไฟล์เครื่องจำลอง Linux/Unix พร้อมใช้งานทันทีในเครื่องคอมพิวเตอร์ของเรา (รองรับ VirtualBox, VMware)</p>"
            "</div>"
            "<a href=\"https://www.osboxes.org/\" target=\"_blank\" style=\"background: #00f0ff; color: #000; padding: 6px 16px; border-radius: 6px; font-weight: 700; font-size: 0.8rem; text-decoration: none; white-space: nowrap; box-shadow: 0 4px 10px rgba(0,240,255,0.25);\">เยี่ยมชมเว็บไซต์ 🔗</a>"
            "</div>"
            "<div style=\"display: flex; align-items: center; justify-content: space-between; gap: 16px; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 16px; transition: all 0.3s;\" onmouseover=\"this.style.borderColor='#ab20fd'; this.style.boxShadow='0 0 12px rgba(171,32,253,0.2)';\" onmouseout=\"this.style.borderColor='rgba(255,255,255,0.08)'; this.style.boxShadow='none';\">"
            "<div style=\"text-align: left;\">"
            "<span style=\"font-weight: 700; color: #ab20fd; font-size: 1rem;\">💿 Virtual Disk Images</span>"
            "<p style=\"color: #cbd5e1; font-size: 0.85rem; margin: 4px 0 0;\">คลังรวมไฟล์ระบบปฏิบัติการเสมือน Linux ยอดฮิตค่ายต่างๆ ที่จัดหมวดหมู่ให้ดาวน์โหลดไปติดตั้งบนเครื่องจำลองได้ฟรี</p>"
            "</div>"
            "<a href=\"http://virtualdiskimages.weebly.com/\" target=\"_blank\" style=\"background: #ab20fd; color: #fff; padding: 6px 16px; border-radius: 6px; font-weight: 700; font-size: 0.8rem; text-decoration: none; white-space: nowrap; box-shadow: 0 4px 10px rgba(171,32,253,0.25);\">เยี่ยมชมเว็บไซต์ 🔗</a>"
            "</div>"
            "<div style=\"display: flex; align-items: center; justify-content: space-between; gap: 16px; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 16px; transition: all 0.3s;\" onmouseover=\"this.style.borderColor='#ff007f'; this.style.boxShadow='0 0 12px rgba(255,0,127,0.2)';\" onmouseout=\"this.style.borderColor='rgba(255,255,255,0.08)'; this.style.boxShadow='none';\">"
            "<div style=\"text-align: left;\">"
            "<span style=\"font-weight: 700; color: #ff007f; font-size: 1rem;\">🏛️ WinWorld</span>"
            "<p style=\"color: #cbd5e1; font-size: 0.85rem; margin: 4px 0 0;\"><strong>พิพิธภัณฑ์ซอฟต์แวร์โบราณ!</strong> รวบรวมระบบปฏิบัติการยุคเก่า ระบบปฏิบัติการที่ยกเลิกพัฒนาไปแล้ว รวมถึงซอฟต์แวร์วินเทจย้อนยุค</p>"
            "</div>"
            "<a href=\"https://winworldpc.com/library/operating-systems\" target=\"_blank\" style=\"background: #ff007f; color: #fff; padding: 6px 16px; border-radius: 6px; font-weight: 700; font-size: 0.8rem; text-decoration: none; white-space: nowrap; box-shadow: 0 4px 10px rgba(255,0,127,0.25);\">เยี่ยมชมเว็บไซต์ 🔗</a>"
            "</div>"
            "</div>"
            "</div>"
        )
        
        # 2. Update Block 13 (Windows Distribution Timeline)
        # We need to insert our friendly introduction text right below the heading
        b13_val = blocks[13]['value']
        target_header = "### 📅 Distribution Timelines (ไทม์ไลน์เวอร์ชัน OS)\n\n"
        intro_text = (
            "<p style=\"color: #cbd5e1; font-size: 0.95rem; line-height: 1.7; margin-bottom: 1.5rem; text-align: left;\">"
            "ระบบปฏิบัติการที่เราใช้กันอยู่ในปัจจุบัน ไม่ได้หน้าตาเท่และทำงานลื่นไหลแบบนี้ตั้งแต่แรกนะครับ! 📅 แต่ละค่ายต่างผ่านการพัฒนาและปรับปรุงฟีเจอร์มายาวนานหลายสิบปี น้องๆ ลองสไลด์เลื่อนแถบแนวนอนด้านล่างเพื่อศึกษา <strong>\"ไทม์ไลน์ประวัติศาสตร์\"</strong> การเดินทางของแต่ละเวอร์ชัน ตั้งแต่อดีตจนถึงปัจจุบันกันได้เลยครับ! (คลิกเลือกปุ่มเพื่อสลับค่ายได้เลยนะ)"
            "</p>\n\n"
        )
        
        # Replace the heading to include the introduction
        if target_header in b13_val:
            blocks[13]['value'] = b13_val.replace(target_header, target_header + intro_text)
            print("Block 13 intro added successfully.")
        else:
            # Alternate search
            print("Warning: Target header not found exactly in Block 13, trying alternate replace...")
            import re
            b13_val = re.sub(r"(### 📅 Distribution Timelines \(ไทม์ไลน์เวอร์ชัน OS\)\n*)", r"\1" + intro_text, b13_val)
            blocks[13]['value'] = b13_val
            
        lesson.content = json.dumps(blocks, ensure_ascii=False)
        db.session.query(TutorialLesson).filter_by(id=164).update({"content": lesson.content})
        db.session.commit()
        print("Lesson 164 Block 11 and Block 13 updated successfully!")
    else:
        print("Error: Lesson 164 not found in database!")
