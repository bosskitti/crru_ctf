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
        
        # 1. Update Block 13 (Linux Important Files & Sub-Trees Map)
        b13_val = blocks[13]['value']
        # Locate the interactive file map section or style tag
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
        blocks[13]['value'] = new_intro_b13 + interactive_code_13
        
        # 2. Update Block 15 (Linux User Accounts) with beautiful cards layout
        blocks[15]['value'] = (
            "### 👥 Linux User Accounts (ประเภทบัญชีผู้ใช้ใน Linux)\n\n"
            "ในโลกของ Linux ไม่ใช่ทุกคนที่จะมีอำนาจเท่ากันนะครับ! 🔐 ระบบจะแบ่งประเภทผู้ใช้งานออกเป็น **3 ยศหลักๆ** ตามระดับความปลอดภัยและการเข้าถึงไฟล์ เพื่อป้องกันไม่ให้คนทั่วไป (หรือผู้ร้าย) แอบเข้ามาสั่งลบไฟล์ระบบคอมพิวเตอร์พัง ดังนี้ครับ:\n\n"
            "<div style=\"display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin: 1.5rem 0; text-align: left;\">\n"
            "  <div style=\"background: rgba(239, 68, 68, 0.03); border: 1px solid rgba(239, 68, 68, 0.15); border-radius: 12px; padding: 20px; display: flex; flex-direction: column; gap: 8px;\">\n"
            "    <span style=\"font-weight: 800; color: #ef4444; font-size: 1.05rem; display: flex; align-items: center; gap: 8px;\">👑 Root User (Super User)</span>\n"
            "    <span style=\"font-size: 0.75rem; color: #ef4444; font-weight: 700; background: rgba(239, 68, 68, 0.1); padding: 2px 8px; border-radius: 4px; width: fit-content; text-transform: uppercase;\">สิทธิ์สูงสุด / หัวหน้าใหญ่</span>\n"
            "    <ul style=\"color: #cbd5e1; font-size: 0.85rem; padding-left: 18px; margin: 4px 0 0; line-height: 1.6; list-style-type: square;\">\n"
            "      <li>ถูกสร้างขึ้นมาโดยอัตโนมัติเมื่อติดตั้งระบบ</li>\n"
            "      <li>มีอำนาจสูงสุด สามารถเปิด อ่าน แก้ไข หรือลบไฟล์ใดๆ ในเครื่องก็ได้ (ไม่มีสิ่งใดห้ามได้!)</li>\n"
            "      <li>มีสิทธิ์ติดตั้งหรือถอนการติดตั้งทุกแอปพลิเคชัน</li>\n"
            "      <li style=\"color: #f87171;\">⚠️ <strong>คำเตือน:</strong> ไม่แนะนำให้ใช้บัญชีนี้ทำงานทั่วไป เพราะถ้าเผลอกดผิดระบบอาจพังทันที!</li>\n"
            "    </ul>\n"
            "  </div>\n"
            "  <div style=\"background: rgba(34, 197, 94, 0.03); border: 1px solid rgba(34, 197, 94, 0.15); border-radius: 12px; padding: 20px; display: flex; flex-direction: column; gap: 8px;\">\n"
            "    <span style=\"font-weight: 800; color: #22c55e; font-size: 1.05rem; display: flex; align-items: center; gap: 8px;\">🧑 Regular User (Standard User)</span>\n"
            "    <span style=\"font-size: 0.75rem; color: #22c55e; font-weight: 700; background: rgba(34, 197, 94, 0.1); padding: 2px 8px; border-radius: 4px; width: fit-content; text-transform: uppercase;\">ผู้ใช้งานทั่วไป / พลเมือง</span>\n"
            "    <ul style=\"color: #cbd5e1; font-size: 0.85rem; padding-left: 18px; margin: 4px 0 0; line-height: 1.6; list-style-type: square;\">\n"
            "      <li>บัญชีที่สร้างขึ้นมาให้ผู้ใช้ทั่วไปเปิดทำงานในแต่ละวัน</li>\n"
            "      <li>ไฟล์ส่วนตัวทั้งหมดจะถูกล็อกไว้ในโฮมไดเรกทอรีส่วนตัว (เช่น <code>/home/user</code>)</li>\n"
            "      <li>ไม่สามารถเข้าไปอ่านหรือแก้ไขไฟล์ของคนอื่นได้</li>\n"
            "      <li>ไม่มีสิทธิ์แก้ไขไฟล์ระบบหลัก เว้นแต่จะใช้คำสั่งขอยืมสิทธิ์พิเศษ (เช่น <code>sudo</code>)</li>\n"
            "    </ul>\n"
            "  </div>\n"
            "  <div style=\"background: rgba(59, 130, 246, 0.03); border: 1px solid rgba(59, 130, 246, 0.15); border-radius: 12px; padding: 20px; display: flex; flex-direction: column; gap: 8px;\">\n"
            "    <span style=\"font-weight: 800; color: #3b82f6; font-size: 1.05rem; display: flex; align-items: center; gap: 8px;\">🤖 Service User (System User)</span>\n"
            "    <span style=\"font-size: 0.75rem; color: #3b82f6; font-weight: 700; background: rgba(59, 130, 246, 0.1); padding: 2px 8px; border-radius: 4px; width: fit-content; text-transform: uppercase;\">ผู้ช่วยหุ่นยนต์ระบบ</span>\n"
            "    <ul style=\"color: #cbd5e1; font-size: 0.85rem; padding-left: 18px; margin: 4px 0 0; line-height: 1.6; list-style-type: square;\">\n"
            "      <li>สร้างขึ้นโดยอัตโนมัติเพื่อให้ระบบเบื้องหลัง (Services) นำไปรันโปรแกรม</li>\n"
            "      <li>เช่น เว็บเซิร์ฟเวอร์ (Apache) หรือระบบฐานข้อมูล จะมีบัญชีเหล่านี้รันอยู่</li>\n"
            "      <li>ทำงานเฉพาะขอบเขตหน้าที่ที่ได้รับมอบหมายเท่านั้น</li>\n"
            "      <li>เพื่อความปลอดภัย บัญชีจำพวกนี้จะไม่ได้รับอนุญาตให้พิมพ์คำสั่งล็อกอินเข้าระบบโดยตรง</li>\n"
            "    </ul>\n"
            "  </div>\n"
            "</div>"
        )
        
        # 3. Update Block 17 (Unix in Linux System) with relationship visual box
        blocks[17]['value'] = (
            "### 📌 Unix in Linux System (ย้อนรอยความสัมพันธ์: Unix กับ Linux)\n\n"
            "น้องๆ อาจจะงงว่า **\"อ้าว! สรุปแล้วระบบที่เราเรียนอยู่ชื่อ Unix หรือ Linux กันแน่?\"** 🤔 \n\n"
            "เรื่องนี้มีที่มาที่ไปแสนสนุกครับ! ลองคิดง่ายๆ ว่า **Unix** คือ **\"คุณพ่อผู้ให้กำเนิดสถาปัตยกรรมสุดเก๋า\"** ส่วน **Linux** คือ **\"ลูกชายที่เติบโตขึ้นมารับช่วงต่อและแจกจ่ายความรู้ฟรี\"** นั่นเองครับ! ลองมาดูสรุปการเดินทางของพวกเขากันเลย:\n\n"
            "<div style=\"background: rgba(15, 17, 26, 0.45); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 12px; padding: 24px; margin: 1.5rem 0; text-align: left;\">\n"
            "  <div style=\"display: flex; gap: 20px; flex-wrap: wrap;\">\n"
            "    <div style=\"flex: 1; min-width: 250px; display: flex; flex-direction: column; gap: 12px;\">\n"
            "      <div style=\"font-weight: 700; color: #00f0ff; font-size: 1.05rem; display: flex; align-items: center; gap: 8px;\">\n"
            "        👴 คุณพ่อสุดเก๋า: Unix (ทศวรรษ 1960s)\n"
            "      </div>\n"
            "      <p style=\"color: #cbd5e1; font-size: 0.88rem; line-height: 1.6; margin: 0;\">\n"
            "        ถูกพัฒนาขึ้นในห้องแล็บชื่อดัง **Bell Labs** เขียนขึ้นด้วยภาษา **C** เป็นระบบที่เสถียรมาก รองรับผู้ใช้งานหลายคนพร้อมกัน แต่มันมีลิขสิทธิ์เชิงพาณิชย์ที่แพงมาก ทำให้คนทั่วไปเข้าถึงยาก\n"
            "      </p>\n"
            "    </div>\n"
            "    <div style=\"display: flex; align-items: center; justify-content: center; font-size: 1.8rem; color: #8a94a6;\">\n"
            "      ➡️\n"
            "    </div>\n"
            "    <div style=\"flex: 1; min-width: 250px; display: flex; flex-direction: column; gap: 12px;\">\n"
            "      <div style=\"font-weight: 700; color: #22c55e; font-size: 1.05rem; display: flex; align-items: center; gap: 8px;\">\n"
            "        🐧 ลูกชายสายเปิด: Linux (1991)\n"
            "      </div>\n"
            "      <p style=\"color: #cbd5e1; font-size: 0.88rem; line-height: 1.6; margin: 0;\">\n"
            "        ลุง Linus Torvalds เขียนโค้ดระบบขึ้นมาใหม่ทั้งหมดโดยอ้างอิงสถาปัตยกรรมและกฎการทำงานของ Unix (เราจึงเรียกลินุกซ์ว่า **Unix-like**) แต่มีข้อดีที่สุดคือ **เปิดให้ทุกคนใช้ฟรีและแจกโค้ดทั้งหมด (Open Source)** นั่นเอง!\n"
            "      </p>\n"
            "    </div>\n"
            "  </div>\n"
            "</div>"
        )
        
        # 4. Update Block 19 (Unix in Linux System (Cont)) with terminal mockup intro
        b19_val = blocks[19]['value']
        style_idx_19 = b19_val.find("<style>")
        if style_idx_19 != -1:
            interactive_code_19 = b19_val[style_idx_19:]
        else:
            interactive_code_19 = b19_val
            
        new_intro_b19 = (
            "### 📌 Unix in Linux System (Cont) (ทำความรู้จักกับหน้าต่างคำสั่ง Terminal)\n\n"
            "เวลาที่แฮกเกอร์รันเครื่องมือต่างๆ หรือสั่งการคอมพิวเตอร์ ส่วนใหญ่พวกเขาจะไม่ใช้เม้าส์คลิกแบบเราครับ 🖱️ แต่พวกเขาจะใช้ **\"อินเตอร์เฟซบรรทัดคำสั่ง (Command-Line Interface หรือ Terminal)\"** คุยกับ Shell ตรงๆ \n\n"
            "เพื่อให้น้องๆ คุ้นเคย ลองดู **\"เครื่องจำลองหน้าจอ Terminal\"** ด้านล่างนี้ว่าเวลาที่แฮกเกอร์ใช้ Terminal สั่งงานระบบปฏิบัติการ หน้าตาของคำสั่งเริ่มต้นมีอะไรบ้างครับ: 👇\n\n"
        )
        blocks[19]['value'] = new_intro_b19 + interactive_code_19
        
        lesson.content = json.dumps(blocks, ensure_ascii=False)
        db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
        db.session.commit()
        print("Lesson 165 final blocks 13, 15, 17, 19 updated successfully with friendly Thai explanations!")
    else:
        print("Error: Lesson 165 not found!")
