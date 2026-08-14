import sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
app = create_app()

with app.app_context():
    from CTFd.models import db
    from CTFd.plugins.tutorials import TutorialLesson
    
    lesson = TutorialLesson.query.get(166)
    if not lesson or not lesson.content:
        print("Lesson 166 not found!")
        sys.exit(1)
        
    import json
    cells = json.loads(lesson.content.strip())
    print(f"Original cell count: {len(cells)}")
    
    # Define our 4 new cells
    cell_p5_md = {
        "type": "markdown",
        "value": "#### 📂 Part 5: System Users & Configuration (การตรวจสอบข้อมูลผู้ใช้ระบบ)\n\nตามที่สอนในเรื่องสถาปัตยกรรมไดเรกทอรี โฟลเดอร์ `/etc` ใช้สำหรับเก็บไฟล์ตั้งค่าคอมฟิกูเรชันต่างๆ ของระบบ และหนึ่งในไฟล์สำคัญที่สุดคือ `/etc/passwd` ซึ่งทำหน้าที่เก็บรายชื่อผู้ใช้ระบบทั้งหมดในเครื่อง รวมถึงข้อมูลส่วนตัวของบัญชีนั้นๆ ในรูปแบบตารางบรรทัดข้อมูล\n\n**ภารกิจของคุณ:**\n1. ตรวจสอบไฟล์ `/etc/passwd` โดยใช้คำสั่งอ่านไฟล์ (เช่น `cat` หรือ `grep` ร่วมกับชื่อไฟล์)\n2. ตามหายูสเซอร์ที่ชื่อ `flag5user` และสังเกตฟิลด์ข้อมูลเสริม (เช่น ส่วนคอมเมนต์ หรือ GECOS) เพื่อระบุตำแหน่งของ Flag\n3. คัดลอก Flag ดังกล่าวมาส่งในกล่องด้านล่าง"
    }
    
    cell_p5_chall = {
        "type": "challenge",
        "challenge_id": 40
    }
    
    cell_p6_md = {
        "type": "markdown",
        "value": "#### 🌐 Part 6: Host Network Mapping (การตรวจสอบแผนผังเครือข่ายจำลอง)\n\nตามที่ระบุในแผนผังไฟล์สำคัญ ไฟล์ `/etc/hosts` คือไฟล์แผนผังเครือข่ายระดับโลคอล (Local Hostname Resolution) ทำหน้าที่จับคู่ระหว่าง IP Address และ Domain Name ซึ่งเป็นหนึ่งในไฟล์ระบบสำคัญที่คุณควรตรวจสอบเพื่อหาความผิดปกติของ Network Route หรือ DNS Mapping\n\n**ภารกิจของคุณ:**\n1. ตรวจสอบไฟล์ `/etc/hosts` โดยใช้คำสั่งอ่านไฟล์\n2. ค้นหาความผิดปกติหรือแผนผัง IP Address ที่มีการจับคู่กับ Flag\n3. คัดลอก Flag ดังกล่าวมาส่งในกล่องด้านล่าง"
    }
    
    cell_p6_chall = {
        "type": "challenge",
        "challenge_id": 41
    }
    
    # We insert these 4 cells before the last cell (which is the Quick Quiz at index len(cells)-1)
    quiz_cell = cells.pop() # Remove the last cell
    
    # Append the new cells
    cells.append(cell_p5_md)
    cells.append(cell_p5_chall)
    cells.append(cell_p6_md)
    cells.append(cell_p6_chall)
    
    # Re-append the quiz cell at the very end
    cells.append(quiz_cell)
    
    # Save back to database
    lesson.content = json.dumps(cells, ensure_ascii=False)
    db.session.commit()
    print(f"Updated cell count: {len(cells)}")
    print("Successfully inserted Part 5 and Part 6 challenges into Lesson 166 content!")
