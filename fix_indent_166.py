# -*- coding: utf-8 -*-
import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    lesson = db.session.query(TutorialLesson).filter_by(id=166).first()
    if not lesson:
        print("Lesson 166 not found!")
        exit(1)

    # ─────────────────────────────────────────────────────────────────────────────
    # BLOCK 0: Header with Welcoming Robot Mascot
    # ─────────────────────────────────────────────────────────────────────────────
    b0_header = """<div style="background: linear-gradient(135deg, rgba(15, 23, 42, 0.8), rgba(11, 15, 25, 0.95)); border: 1px solid rgba(0, 240, 255, 0.25); border-radius: 16px; padding: 28px 32px; margin: 1.5rem 0 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.5), inset 0 0 20px rgba(0, 240, 255, 0.05); display: flex; align-items: center; justify-content: space-between; gap: 24px; flex-wrap: wrap;">
<div style="flex: 1; min-width: 280px;">
<div style="display: inline-flex; align-items: center; gap: 8px; background: rgba(0, 240, 255, 0.1); border: 1px solid rgba(0, 240, 255, 0.3); border-radius: 20px; padding: 4px 14px; font-size: 0.78rem; font-family: 'JetBrains Mono', monospace; color: #00f0ff; margin-bottom: 12px; letter-spacing: 0.05em;">
<span style="width: 8px; height: 8px; background: #00f0ff; border-radius: 50%; box-shadow: 0 0 8px #00f0ff;"></span>
CHAPTER 02 • LESSON 03 • CORE TERMINAL SKILLS
</div>
<h2 style="color: #ffffff; font-size: 1.85rem; font-weight: 800; margin: 0 0 10px 0; letter-spacing: -0.02em; line-height: 1.3;">
🐧 คำสั่งควบคุมไฟล์และจัดการสิทธิ์ใน Linux
</h2>
<p style="color: #94a3b8; font-size: 0.95rem; margin: 0; line-height: 1.6;">
เรียนรู้โครงสร้างคำสั่งพื้นฐาน (Syntax), เทคนิคการจัดการไฟล์และไดเรกทอรี, ค้นหาข้อมูลเชิงลึกด้วย <code style="color:#38bdf8;">grep</code>/<code style="color:#38bdf8;">find</code>, และเจาะลึกระบบสิทธิ์ <code style="color:#fbbf24;">chmod</code> / <code style="color:#ef4444;">sudo</code> พร้อมลงมือปฏิบัติจริงบน Docker Lab ต่อเนื่อง 4 ด่าน!
</p>
</div>
<div style="text-align: center; flex-shrink: 0;">
<img src="/themes/core/static/img/stickers/robot_03_waving_hello.png" alt="Welcome Robot" style="width: 140px; height: auto; filter: drop-shadow(0 6px 16px rgba(0, 240, 255, 0.35)); transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
<div style="margin-top: 6px; font-size: 0.75rem; color: #38bdf8; font-weight: 600; font-family: 'JetBrains Mono', monospace;">น้องหุ่นยนต์นำทาง</div>
</div>
</div>"""

    # ─────────────────────────────────────────────────────────────────────────────
    # BLOCK 1: Command Line Structure with Fox Terminal Mascot (NO 4-space indentation!)
    # ─────────────────────────────────────────────────────────────────────────────
    b1_structure = """### 🖥️ Unix Command Line Structure (โครงสร้างคำสั่งบนเทอร์มินัล)

<div style="background: rgba(15, 17, 26, 0.6); border: 1px solid rgba(0, 240, 255, 0.18); border-radius: 14px; padding: 26px; margin: 1.8rem auto; box-shadow: 0 8px 32px rgba(0,0,0,0.45); max-width: 1000px;">
<div style="display: flex; align-items: center; gap: 24px; flex-wrap: wrap;">
<div style="text-align: center; flex-shrink: 0; margin: 0 auto;">
<img src="/themes/core/static/img/stickers/fox_01_terminal.png" alt="Fox Hacker" style="width: 135px; height: auto; filter: drop-shadow(0 6px 16px rgba(239, 68, 68, 0.35));">
<div style="font-size: 0.75rem; color: #f87171; font-weight: 700; margin-top: 6px; font-family: 'JetBrains Mono', monospace;">จิ้งจอกแฮกเกอร์สายรุก</div>
</div>
<div style="flex: 1; min-width: 280px;">
<div style="background: #070913; border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 16px 20px; font-family: 'JetBrains Mono', monospace; font-size: 1.45rem; font-weight: 700; display: flex; gap: 12px; align-items: center; justify-content: center; flex-wrap: wrap; margin-bottom: 18px;">
<span style="color: #34d399; background: rgba(52, 211, 153, 0.1); padding: 4px 10px; border-radius: 6px; border: 1px solid rgba(52, 211, 153, 0.3);">$</span>
<span style="color: #00f0ff; background: rgba(0, 240, 255, 0.1); padding: 4px 12px; border-radius: 6px; border: 1px solid rgba(0, 240, 255, 0.3);">ls</span>
<span style="color: #fbbf24; background: rgba(251, 191, 36, 0.1); padding: 4px 12px; border-radius: 6px; border: 1px solid rgba(251, 191, 36, 0.3);">-la</span>
<span style="color: #c084fc; background: rgba(192, 132, 252, 0.1); padding: 4px 14px; border-radius: 6px; border: 1px solid rgba(192, 132, 252, 0.3);">/home/kali</span>
</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px;">
<div style="background: rgba(52, 211, 153, 0.05); border: 1px solid rgba(52, 211, 153, 0.2); border-radius: 8px; padding: 10px 14px;">
<div style="color: #34d399; font-weight: 800; font-size: 0.88rem; font-family: 'JetBrains Mono', monospace;">$ • Prompt</div>
<div style="color: #94a3b8; font-size: 0.8rem; margin-top: 3px;">บอกความพร้อมรับคำสั่ง (<code>$</code> = user, <code>#</code> = root)</div>
</div>
<div style="background: rgba(0, 240, 255, 0.05); border: 1px solid rgba(0, 240, 255, 0.2); border-radius: 8px; padding: 10px 14px;">
<div style="color: #00f0ff; font-weight: 800; font-size: 0.88rem; font-family: 'JetBrains Mono', monospace;">ls • Command</div>
<div style="color: #94a3b8; font-size: 0.8rem; margin-top: 3px;">ชื่อโปรแกรมหลักที่ต้องการสั่งให้รันทำงาน</div>
</div>
<div style="background: rgba(251, 191, 36, 0.05); border: 1px solid rgba(251, 191, 36, 0.2); border-radius: 8px; padding: 10px 14px;">
<div style="color: #fbbf24; font-weight: 800; font-size: 0.88rem; font-family: 'JetBrains Mono', monospace;">-la • Options / Flags</div>
<div style="color: #94a3b8; font-size: 0.8rem; margin-top: 3px;">ตัวเลือกพฤติกรรม (รวม <code>-l</code> ละเอียด + <code>-a</code> ไฟล์ซ่อน)</div>
</div>
<div style="background: rgba(192, 132, 252, 0.05); border: 1px solid rgba(192, 132, 252, 0.2); border-radius: 8px; padding: 10px 14px;">
<div style="color: #c084fc; font-weight: 800; font-size: 0.88rem; font-family: 'JetBrains Mono', monospace;">/home • Arguments</div>
<div style="color: #94a3b8; font-size: 0.8rem; margin-top: 3px;">เป้าหมายหรือพารามิเตอร์ที่ต้องการให้คำสั่งกระทำด้วย</div>
</div>
</div>
</div>
</div>
</div>

<!-- Unified Mission Control / Lab Summary -->
<div style="background: linear-gradient(135deg, rgba(16, 24, 39, 0.95), rgba(7, 10, 19, 0.98)); border: 2px solid rgba(0, 240, 255, 0.35); border-radius: 16px; padding: 24px 28px; margin: 2rem auto; box-shadow: 0 12px 40px rgba(0,0,0,0.6), 0 0 25px rgba(0, 240, 255, 0.1); max-width: 1000px;">
<div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 14px; margin-bottom: 18px; flex-wrap: wrap; gap: 12px;">
<div style="display: flex; align-items: center; gap: 14px;">
<img src="/themes/core/static/img/stickers/fox_08_checklist.png" alt="Mission Checklist" style="width: 54px; height: auto; filter: drop-shadow(0 4px 10px rgba(0, 240, 255, 0.3));">
<div>
<h3 style="margin: 0; color: #00f0ff; font-size: 1.25rem; font-weight: 800; letter-spacing: -0.01em;">
🎯 CRRU CTF LINUX MISSION CONTROL (ศูนย์รวมปฏิบัติการ 4 ด่านต่อเนื่อง)
</h3>
<span style="color: #94a3b8; font-size: 0.83rem;">กดเปิดเซสชันคอนเทนเนอร์เพียง <strong>ครั้งเดียว</strong> ในข้อ Part 1 แล้วทำต่อเนื่องครบทั้ง 4 ข้อในเครื่องเดียวกันทันที!</span>
</div>
</div>
<div style="background: rgba(34, 197, 94, 0.1); border: 1px solid rgba(34, 197, 94, 0.3); border-radius: 20px; padding: 5px 14px; font-size: 0.8rem; color: #4ade80; font-weight: 700; display: inline-flex; align-items: center; gap: 6px;">
<span style="width: 8px; height: 8px; background: #22c55e; border-radius: 50%; box-shadow: 0 0 8px #22c55e;"></span>
1 DOCKER INSTANCE FOR ALL 4 PARTS
</div>
</div>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin-bottom: 16px;">
<!-- Step 1 -->
<div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(0, 240, 255, 0.2); border-radius: 10px; padding: 14px 16px;">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
<span style="font-weight: 800; color: #00f0ff; font-size: 0.85rem;">1️⃣ PART 1: NAVIGATION</span>
<span style="color: #94a3b8; font-size: 0.75rem; font-family: monospace;">50 Pts</span>
</div>
<div style="color: #cbd5e1; font-size: 0.82rem; margin-bottom: 8px;">ค้นหาไฟล์ลับที่ซ่อนอยู่ใน <code>documents</code></div>
<div style="background: #070913; border: 1px solid rgba(255,255,255,0.06); border-radius: 6px; padding: 6px 10px; font-family: monospace; font-size: 0.78rem; color: #38bdf8;">$ cd documents && ls -la</div>
</div>

<!-- Step 2 -->
<div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(251, 191, 36, 0.2); border-radius: 10px; padding: 14px 16px;">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
<span style="font-weight: 800; color: #fbbf24; font-size: 0.85rem;">2️⃣ PART 2: PERMISSIONS</span>
<span style="color: #94a3b8; font-size: 0.75rem; font-family: monospace;">100 Pts</span>
</div>
<div style="color: #cbd5e1; font-size: 0.82rem; margin-bottom: 8px;">เปิดสิทธิ์อ่านไฟล์ <code>flag2.txt</code> ด้วย chmod</div>
<div style="background: #070913; border: 1px solid rgba(255,255,255,0.06); border-radius: 6px; padding: 6px 10px; font-family: monospace; font-size: 0.78rem; color: #fbbf24;">$ chmod 755 flag2.txt && cat flag2.txt</div>
</div>

<!-- Step 3 -->
<div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(192, 132, 252, 0.2); border-radius: 10px; padding: 14px 16px;">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
<span style="font-weight: 800; color: #c084fc; font-size: 0.85rem;">3️⃣ PART 3: DASH FILENAME</span>
<span style="color: #94a3b8; font-size: 0.75rem; font-family: monospace;">100 Pts</span>
</div>
<div style="color: #cbd5e1; font-size: 0.82rem; margin-bottom: 8px;">อ่านไฟล์ <code>-flag3.txt</code> ที่ขึ้นต้นด้วยขีดลบ</div>
<div style="background: #070913; border: 1px solid rgba(255,255,255,0.06); border-radius: 6px; padding: 6px 10px; font-family: monospace; font-size: 0.78rem; color: #c084fc;">$ cat -- -flag3.txt</div>
</div>

<!-- Step 4 -->
<div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(239, 68, 68, 0.2); border-radius: 10px; padding: 14px 16px;">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
<span style="font-weight: 800; color: #f87171; font-size: 0.85rem;">4️⃣ PART 4: PRIVILEGE ESC</span>
<span style="color: #94a3b8; font-size: 0.75rem; font-family: monospace;">150 Pts</span>
</div>
<div style="color: #cbd5e1; font-size: 0.82rem; margin-bottom: 8px;">ยกระดับสิทธิ์เป็น Root อ่านไฟล์ระบบ</div>
<div style="background: #070913; border: 1px solid rgba(255,255,255,0.06); border-radius: 6px; padding: 6px 10px; font-family: monospace; font-size: 0.78rem; color: #f87171;">$ sudo cat /root/flag4.txt</div>
</div>
</div>

<div style="background: rgba(0, 240, 255, 0.04); border-left: 3px solid #00f0ff; padding: 10px 14px; font-size: 0.83rem; color: #94a3b8; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px;">
<span>👇 <strong>ขั้นตอนเริ่มทำ:</strong> คลิกปุ่ม <em>Launch Lab Instance</em> ที่ข้อด้านล่างนี้เพื่อสตาร์ตเทอร์มินัล แล้วนำ Flag แต่ละข้อมาส่งตามลำดับ</span>
<span style="color: #38bdf8; font-weight: 700; font-family: monospace;">Total Score: 400 Points</span>
</div>
</div>"""

    # Update blocks 0 and 1
    blocks = json.loads(lesson.content)
    blocks[0]['value'] = b0_header
    blocks[1]['value'] = b1_structure
    lesson.content = json.dumps(blocks, ensure_ascii=False)
    db.session.commit()
    print("Lesson 166 cleaned indentation and updated in DB!")
