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

    # === BLOCK 0: Add friendly intro paragraph before the Command Anatomy card ===
    block0_original = blocks[0]['value']
    # The block starts with "## 🐧 คำสั่ง..."
    # We prepend a friendly greeting paragraph right after the heading line
    heading_line = "## 🐧 คำสั่งควบคุมไฟล์และจัดการสิทธิ์ใน Linux (Linux File & Permission Commands)\n"
    friendly_intro_b0 = """<div style="width:100%;max-width:1050px;margin:0.5rem auto 1.5rem auto;background:rgba(0,240,255,0.04);border-left:4px solid #00f0ff;border-radius:0 10px 10px 0;padding:14px 20px;font-size:0.88rem;color:#94a3b8;line-height:1.7;box-sizing:border-box;">
สวัสดีครับน้องๆ! 👋 บทเรียนนี้เราจะมาเรียนรู้ <strong style="color:#e2e8f0;">คำสั่งพื้นฐานของ Linux Terminal</strong> ซึ่งเป็นเครื่องมือหลักที่นักรบไซเบอร์ทุกคนต้องใช้งานในชีวิตประจำวันเลยครับ!<br>
ก่อนอื่น เราต้องรู้จัก <strong style="color:#00f0ff;">โครงสร้างของคำสั่ง Linux</strong> ก่อนว่ามันประกอบด้วยอะไรบ้าง — ดูตัวอย่างด้านล่างนี้ได้เลยครับ 👇
</div>
"""
    if heading_line in block0_original:
        blocks[0]['value'] = block0_original.replace(heading_line, heading_line + friendly_intro_b0, 1)
        print("Block 0: intro added ✓")
    else:
        print("Block 0: heading not found, skipping")

    # === BLOCK 3: Replace the .s-intro text with a friendlier version ===
    old_b3_intro_p = "คำสั่งในกลุ่มนี้ใช้สำหรับ <strong>จัดการไฟล์และ directory</strong> ใน Linux ทั้งการแสดงรายการ สร้าง คัดลอก ย้าย และลบ ถือเป็นคำสั่งพื้นฐานที่ผู้ใช้ Linux ทุกคนต้องรู้ และใช้งานทุกวัน — เรียนรู้คำสั่งเหล่านี้จะช่วยให้คุณนำทางใน Terminal ได้อย่างคล่องตัว"
    new_b3_intro_p = "น้องๆ ลองนึกภาพว่า Terminal คือ \"ห้องควบคุม\" ของคอมพิวเตอร์ทั้งเครื่องเลยครับ! 🖥️ คำสั่งกลุ่มนี้คือ <strong>ชุดคำสั่งจัดการไฟล์และโฟลเดอร์</strong> ที่น้องๆ จะต้องใช้ตั้งแต่วันแรกที่เปิด Terminal — ทั้งการดูรายการไฟล์ (<code>ls</code>) เปลี่ยนโฟลเดอร์ (<code>cd</code>) คัดลอก (<code>cp</code>) ย้าย (<code>mv</code>) หรือลบไฟล์ (<code>rm</code>) ถ้าจำพวกนี้ได้ขึ้นใจ รับรองว่าใช้ Linux ได้คล่องแน่นอนครับ! 💪"
    if old_b3_intro_p in blocks[3]['value']:
        blocks[3]['value'] = blocks[3]['value'].replace(old_b3_intro_p, new_b3_intro_p, 1)
        print("Block 3: intro updated ✓")
    else:
        print("Block 3: original intro text not found, skipping")

    # === BLOCK 5: Replace the .s-intro text with a friendlier version ===
    b5_val = blocks[5]['value']
    old_b5_intro_p = "คำสั่งในกลุ่มนี้ใช้สำหรับ <strong>อ่าน ค้นหา และวิเคราะห์เนื้อหาภายในไฟล์</strong> โดยไม่ต้องเปิด text editor ใช้บ่อยมากในงาน Cybersecurity เช่น การหา flag ที่ซ่อนในไฟล์ (cat, grep, find) หรือการเปรียบเทียบไฟล์ (diff) และการเรียงข้อมูล (sort)"
    new_b5_intro_p = "นี่คือคำสั่งที่แฮกเกอร์จริงๆ ใช้บ่อยที่สุดเลยครับ! 🔍 กลุ่มนี้ใช้สำหรับ <strong>อ่านและค้นหาข้อมูลภายในไฟล์</strong> โดยไม่ต้องเปิด text editor เลย — เช่น ใช้ <code>cat</code> อ่านเนื้อหาไฟล์ทีเดียว หรือใช้ <code>grep</code> ค้นหาคำหรือ pattern ที่ซ่อนอยู่ในไฟล์ขนาดยักษ์ หรือ <code>find</code> ล่าไฟล์ที่ซ่อนอยู่ในระบบทั้งหมด! ในการแข่งขัน CTF คำสั่งพวกนี้คือ \"อาวุธลับ\" ที่ช่วยล่า flag ได้เร็วมากครับ! 🚩"
    if old_b5_intro_p in b5_val:
        blocks[5]['value'] = b5_val.replace(old_b5_intro_p, new_b5_intro_p, 1)
        print("Block 5: intro updated ✓")
    else:
        print("Block 5: original intro text not found, skipping")

    # === BLOCK 6: Replace the Permission section intro text with friendlier version ===
    old_b6_intro_p = "Linux กำหนด <strong>สิทธิ์การเข้าถึง (Permission)</strong> ให้กับทุกไฟล์และ directory เพื่อควบคุมว่า <em>ใคร</em> จะสามารถ <em>ทำอะไร</em> ได้บ้าง โดยแบ่งออกเป็น 3 ระดับ ได้แก่ <code>owner</code> (เจ้าของ), <code>group</code> (กลุ่ม), และ <code>others</code> (ผู้อื่น) และ 3 ประเภทสิทธิ์ ได้แก่ <code>r</code> (read), <code>w</code> (write), <code>x</code> (execute) — การเข้าใจ Permission เป็นพื้นฐานสำคัญของ Linux Security"
    new_b6_intro_p = "น้องๆ เคยเห็นข้อความแบบ <code>-rwxr-xr-x</code> แล้วงงไหมครับ? 😅 นั่นคือ <strong>สิทธิ์การเข้าถึงไฟล์ (Permission)</strong> ของ Linux ที่บอกว่า \"ใครมีสิทธิ์ทำอะไรกับไฟล์นี้ได้บ้าง!\" — ระบบ Linux จะแบ่งสิทธิ์ออกเป็น 3 กลุ่มคือ เจ้าของ (<code>owner</code>) กลุ่ม (<code>group</code>) และคนอื่นๆ (<code>others</code>) แล้วแต่ละกลุ่มก็จะมีสิทธิ์ 3 แบบคือ อ่าน (<code>r</code>) เขียน (<code>w</code>) รัน (<code>x</code>) ถ้าเข้าใจหมวดนี้ดีๆ จะช่วยให้เข้าใจ Linux Security ได้ลึกขึ้นมากเลยครับ! 🔐"
    if old_b6_intro_p in blocks[6]['value']:
        blocks[6]['value'] = blocks[6]['value'].replace(old_b6_intro_p, new_b6_intro_p, 1)
        print("Block 6: intro updated ✓")
    else:
        print("Block 6: original intro text not found, skipping")

    # === BLOCK 10: Replace the Frequently Used Commands intro text ===
    b10_val = blocks[10]['value']
    old_b10_intro_p = "คำสั่งเหล่านี้เป็นคำสั่งทั่วไปที่ใช้ใน <strong>การบริหารและตรวจสอบระบบ</strong> ครอบคลุมตั้งแต่การดูข้อมูลระบบ (uname, uptime, df) การจัดการ process (ps, kill, top) การตรวจสอบ user (who, id, last) ไปจนถึงการตั้งค่า network (ifconfig) — ควรจดจำไว้เพราะใช้ประจำในงาน Cybersecurity"
    new_b10_intro_p = "ถึงจะไม่ได้ใช้ทุกวัน แต่คำสั่งพวกนี้ \"ต้องรู้ไว้ก่อน\" ครับ! ⚡ ครอบคลุมตั้งแต่การเช็คข้อมูลระบบ (<code>uname</code>, <code>uptime</code>) ดูพื้นที่ดิสก์ (<code>df</code>) จัดการโปรแกรมที่รันอยู่ (<code>ps</code>, <code>kill</code>, <code>top</code>) เช็คว่าใคร login อยู่บ้าง (<code>who</code>, <code>id</code>, <code>last</code>) ไปจนถึงดู IP Address ของเครื่อง (<code>ifconfig</code>) — ในงาน Cybersecurity ต้องใช้พวกนี้ตลอดเวลาเลยครับ ท่องให้ขึ้นใจไว้ก่อนเลย! 📌"
    if old_b10_intro_p in b10_val:
        blocks[10]['value'] = b10_val.replace(old_b10_intro_p, new_b10_intro_p, 1)
        print("Block 10: intro updated ✓")
    else:
        print("Block 10: original intro text not found, skipping")

    # Save to DB
    lesson.content = json.dumps(blocks, ensure_ascii=False)
    db.session.query(TutorialLesson).filter_by(id=166).update({"content": lesson.content})
    db.session.commit()
    print("\nLesson 166 all friendly intros updated successfully!")
