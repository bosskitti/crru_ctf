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
        
        # 1. Update Block 7 with beautiful visual introduction to Tree Structure
        blocks[7]['value'] = (
            "### 📌 Linux File System (ระบบการจัดเก็บไฟล์ของ Linux)\n\n"
            "<div style=\"background: rgba(0, 240, 255, 0.03); border-left: 4px solid #00f0ff; padding: 18px 22px; border-radius: 0 12px 12px 0; margin: 1.5rem 0; text-align: left; line-height: 1.7;\">\n"
            "  <p style=\"margin-bottom: 8px; font-weight: 700; color: #00f0ff; font-size: 1.02rem; display: flex; align-items: center; gap: 8px;\">🌳 ระบบไฟล์แบบ \"ต้นไม้กลับหัว\" (Tree Structure)</p>\n"
            "  <p style=\"color: #cbd5e1; font-size: 0.92rem; margin: 0;\">\n"
            "    น้องๆ เคยมองกิ่งไม้ไหมครับ? ระบบจัดเก็บข้อมูลของ Linux จะจัดโครงสร้างเหมือน <strong>\"ต้นไม้กลับหัว\"</strong> เลยครับ! โดยจุดเริ่มต้นจะอยู่ที่ <strong>\"รากไม้หลัก (Root)\"</strong> ด้านบนสุด แล้วค่อยๆ แตกกิ่งก้านสาขาแยกย่อยออกมาเป็นโฟลเดอร์ต่างๆ ลงมาด้านล่าง ทำให้การหาไฟล์และจัดหมวดหมู่ทำได้เป็นระเบียบสุดๆ เลยครับ!\n"
            "  </p>\n"
            "</div>"
        )
        
        # 2. Update Block 9 with gorgeous card boxes for the 3 types of files
        blocks[9]['value'] = (
            "### 📌 Linux File System (Cont)\n\n"
            "<div style=\"background: rgba(251, 191, 36, 0.03); border: 1px solid rgba(251, 191, 36, 0.12); border-radius: 12px; padding: 24px; margin: 1.5rem 0; text-align: left;\">\n"
            "  <p style=\"margin-bottom: 12px; font-weight: 700; color: #fbbf24; font-size: 1.05rem; display: flex; align-items: center; gap: 8px;\">💡 คอนเซปต์หลัก: \"ทุกสิ่งคือไฟล์ (Everything is a file)\"</p>\n"
            "  <p style=\"color: #cbd5e1; font-size: 0.92rem; line-height: 1.7; margin-bottom: 16px;\">\n"
            "    ในโลกของ Linux มีกฎเหล็กอยู่ข้อหนึ่งคือ <strong>\"ทุกสิ่งทุกอย่างคือไฟล์\"</strong> ครับ! ไม่ว่าจะเป็นรูปภาพ, ตัวหนังสือ, แอปพลิเคชัน หรือแม้กระทั่งเมาส์, แป้นพิมพ์ และฮาร์ดดิสก์ ระบบจะมองเห็นเป็นไฟล์ทั้งหมดเลย! ซึ่งตัวไฟล์เหล่านั้นจะถูกแบ่งออกเป็น <strong>3 ประเภทหลัก</strong> ให้เข้าใจง่ายๆ ดังนี้ครับ:\n"
            "  </p>\n"
            "  <div style=\"display: flex; flex-direction: column; gap: 12px;\">\n"
            "    <div style=\"background: rgba(255,255,255,0.01); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 14px;\">\n"
            "      <span style=\"font-weight: 700; color: #fbbf24; font-size: 0.9rem;\">1. 📄 ไฟล์ทั่วไป (General Files)</span>\n"
            "      <p style=\"color: #cbd5e1; font-size: 0.82rem; margin: 4px 0 0; line-height: 1.5;\">เป็นไฟล์บรรจุข้อมูลธรรมดาที่เราเจอในชีวิตประจำวัน เช่น ไฟล์เอกสารจดบันทึก (.txt), รูปภาพแมวสุดน่ารัก, ไฟล์เพลง, หรือโปรแกรมประมวลผลโค้ดทั่วไป</p>\n"
            "    </div>\n"
            "    <div style=\"background: rgba(255,255,255,0.01); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 14px;\">\n"
            "      <span style=\"font-weight: 700; color: #ab20fd; font-size: 0.9rem;\">2. 📂 ไฟล์ไดเรกทอรี / โฟลเดอร์ (Directory Files)</span>\n"
            "      <p style=\"color: #cbd5e1; font-size: 0.82rem; margin: 4px 0 0; line-height: 1.5;\">เปรียบเสมือนกล่องแฟ้มเอกสารหลัก คอยทำหน้าที่เก็บไฟล์อื่นๆ หรือสามารถเก็บโฟลเดอร์ซ้อนโฟลเดอร์ย่อยๆ ข้างในเข้าไปได้เรื่อยๆ เพื่อความเป็นระเบียบ</p>\n"
            "    </div>\n"
            "    <div style=\"background: rgba(255,255,255,0.01); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 14px;\">\n"
            "      <span style=\"font-weight: 700; color: #00f0ff; font-size: 0.9rem;\">3. 🔌 ไฟล์อุปกรณ์ (Device Files)</span>\n"
            "      <p style=\"color: #cbd5e1; font-size: 0.82rem; margin: 4px 0 0; line-height: 1.5;\">เป็นไฟล์พิเศษที่ระบบสร้างขึ้นมาเพื่อควบคุมฮาร์ดแวร์จริง เช่น ไดรฟ์เก็บข้อมูลพกพา หรือพอร์ตเชื่อมต่อเครือข่าย โดยระบุที่อยู่ในระบบเป็นไฟล์ เช่น <code>/dev/sda</code> (ตัวแทนของฮาร์ดดิสก์หลัก)</p>\n"
            "    </div>\n"
            "  </div>\n"
            "</div>"
        )
        
        # 3. Update Block 11 intro text (keep CSS/JS and Interactive Tree intact)
        b11_val = blocks[11]['value']
        
        # We need to replace the introduction text at the beginning of Block 11
        # Let's locate the <style> tag which starts the interactive tree code
        style_idx = b11_val.find("<style>")
        if style_idx != -1:
            interactive_tree_code = b11_val[style_idx:]
        else:
            print("Error: <style> not found in block 11!")
            exit(1)
            
        new_intro_b11 = (
            "### 📂 Linux Directory Structure (โครงสร้างไดเรกทอรีลินุกซ์)\n\n"
            "โครงสร้างระบบโฟลเดอร์ของ Linux มีกติกาง่ายๆ คือ ทุกอย่างต้องเริ่มต้นที่ **\"รากไม้หลัก\"** ซึ่งก็คือเครื่องหมายสแลชตัวเดียว (**Root Directory /**) จากนั้นค่อยแตกกิ่งแยกออกเป็นกล่องเก็บข้อมูลย่อยๆ ครับ! น้องๆ ลองเลื่อนเมาส์ชี้ไปที่แต่ละโฟลเดอร์ในแผนภาพด้านล่าง เพื่อแอบดูรายละเอียดหน้าที่ของแต่ละกล่องได้เลยนะ! *(สามารถเลื่อนหน้าจอตามแนวนอนเพื่อดูโครงสร้างทั้งหมดได้เลยครับ)* 👇\n\n"
        )
        
        blocks[11]['value'] = new_intro_b11 + interactive_tree_code
        
        lesson.content = json.dumps(blocks, ensure_ascii=False)
        db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
        db.session.commit()
        print("Lesson 165 Blocks 7, 9, and 11 updated successfully with friendly Thai explanations!")
    else:
        print("Error: Lesson 165 not found!")
