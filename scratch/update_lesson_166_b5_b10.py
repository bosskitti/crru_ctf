import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    lesson = db.session.query(TutorialLesson).filter_by(id=166).first()
    if not lesson:
        print("Lesson 166 not found!")
        exit()

    blocks = json.loads(lesson.content)

    # === BLOCK 5: File Examining intro ===
    old_b5 = "คำสั่งในกลุ่มนี้ใช้สำหรับ <strong>อ่าน ค้นหา และวิเคราะห์เนื้อหาภายในไฟล์</strong> โดยไม่ต้องเปิด text editor ใช้บ่อยมากในงาน Cybersecurity เช่น การหา flag ที่ซ่อนในไฟล์ (<code>cat</code>, <code>grep</code>, <code>find</code>) หรือการเปรียบเทียบไฟล์ (<code>diff</code>) และการเรียงข้อมูล (<code>sort</code>)"
    new_b5 = "นี่คือคำสั่งที่แฮกเกอร์จริงๆ ใช้บ่อยที่สุดเลยครับ! 🔍 กลุ่มนี้ใช้สำหรับ <strong>อ่านและค้นหาข้อมูลภายในไฟล์</strong> โดยไม่ต้องเปิด text editor เลย — เช่น ใช้ <code>cat</code> อ่านเนื้อหาไฟล์ทีเดียว หรือใช้ <code>grep</code> ค้นหาคำหรือ pattern ที่ซ่อนอยู่ในไฟล์ขนาดยักษ์ หรือ <code>find</code> ล่าไฟล์ที่ซ่อนอยู่ในระบบทั้งหมด! ในการแข่งขัน CTF คำสั่งพวกนี้คือ \"อาวุธลับ\" ที่ช่วยล่า flag ได้เร็วมากครับ! 🚩"
    if old_b5 in blocks[5]['value']:
        blocks[5]['value'] = blocks[5]['value'].replace(old_b5, new_b5, 1)
        print("Block 5: intro updated ✓")
    else:
        print(f"Block 5: text not found. Snippet: {repr(blocks[5]['value'][200:400])}")

    # === BLOCK 10: Frequently Used Commands intro ===
    old_b10 = "คำสั่งเหล่านี้เป็นคำสั่งทั่วไปที่ใช้ใน <strong>การบริหารและตรวจสอบระบบ</strong> ครอบคลุมตั้งแต่การดูข้อมูลระบบ (<code>uname</code>, <code>uptime</code>, <code>df</code>) การจัดการ process (<code>ps</code>, <code>kill</code>, <code>top</code>) การตรวจสอบ user (<code>who</code>, <code>id</code>, <code>last</code>) ไปจนถึงการตั้งค่า network (<code>ifconfig</code>) — ควรจดจำไว้เพราะใช้ประจำในงาน Cybersecurity"
    new_b10 = "ถึงจะไม่ได้ใช้ทุกวัน แต่คำสั่งพวกนี้ \"ต้องรู้ไว้ก่อน\" ครับ! ⚡ ครอบคลุมตั้งแต่การเช็คข้อมูลระบบ (<code>uname</code>, <code>uptime</code>) ดูพื้นที่ดิสก์ (<code>df</code>) จัดการโปรแกรมที่รันอยู่ (<code>ps</code>, <code>kill</code>, <code>top</code>) เช็คว่าใคร login อยู่บ้าง (<code>who</code>, <code>id</code>, <code>last</code>) ไปจนถึงดู IP Address ของเครื่อง (<code>ifconfig</code>) — ในงาน Cybersecurity ต้องใช้พวกนี้ตลอดเวลาเลยครับ ท่องให้ขึ้นใจไว้ก่อนเลย! 📌"
    if old_b10 in blocks[10]['value']:
        blocks[10]['value'] = blocks[10]['value'].replace(old_b10, new_b10, 1)
        print("Block 10: intro updated ✓")
    else:
        print(f"Block 10: text not found. Snippet: {repr(blocks[10]['value'][200:600])}")

    # Save to DB
    lesson.content = json.dumps(blocks, ensure_ascii=False)
    db.session.query(TutorialLesson).filter_by(id=166).update({"content": lesson.content})
    db.session.commit()
    print("\nLesson 166 blocks 5 and 10 updated!")
