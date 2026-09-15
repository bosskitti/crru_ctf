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
    # BLOCK 1: Command Line Structure with Fox Terminal Mascot
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

    # ─────────────────────────────────────────────────────────────────────────────
    # BLOCK 4: File and Directory Commands with Inspect Fox Mascot
    # ─────────────────────────────────────────────────────────────────────────────
    with open('/opt/CTFd/scratch/block3_l166.txt', 'r', encoding='utf-8') as f:
        b4_content = f.read()

    b4_banner = """<div style="display: flex; align-items: center; gap: 18px; background: rgba(0, 240, 255, 0.03); border: 1px solid rgba(0, 240, 255, 0.15); border-radius: 12px; padding: 16px 20px; margin: 1.5rem 0 2rem;">
  <img src="/themes/core/static/img/stickers/fox_02_inspect_file.png" alt="Inspect Fox" style="width: 100px; height: auto; flex-shrink: 0; filter: drop-shadow(0 4px 12px rgba(0, 240, 255, 0.3));">
  <div>
    <strong style="color: #00f0ff; font-size: 1.05rem; display: block; margin-bottom: 4px;">📁 คลังคำสั่งจัดการไฟล์และไดเรกทอรี (File & Directory Manipulation)</strong>
    <p style="margin: 0; color: #cbd5e1; font-size: 0.88rem; line-height: 1.6;">
      คำสั่งกลุ่มนี้เป็นพื้นฐานสำคัญที่สุดในการท่องไปในระบบ Linux — ใช้สำหรับสร้าง คัดลอก ย้าย และค้นหาไฟล์ลับในด่าน CTF!
    </p>
  </div>
</div>"""
    
    b4_warning = """<div style="display: flex; align-items: center; gap: 16px; background: rgba(239, 68, 68, 0.05); border: 1px solid rgba(239, 68, 68, 0.25); border-radius: 10px; padding: 14px 18px; margin: 1.5rem 0;">
  <img src="/themes/core/static/img/stickers/robot_06_warning_alert.png" alt="Warning Alert" style="width: 80px; height: auto; flex-shrink: 0; filter: drop-shadow(0 4px 10px rgba(239, 68, 68, 0.3));">
  <div>
    <strong style="color: #ef4444; font-size: 0.92rem; display: block; margin-bottom: 3px;">⚠️ ข้อควรระวังสูงสุดเกี่ยวกับคำสั่ง rm -rf:</strong>
    <span style="color: #cbd5e1; font-size: 0.84rem; line-height: 1.5;">การใช้ <code>rm -rf /</code> ด้วยสิทธิ์ root จะทำการลบไฟล์ทั้งหมดในระบบปฏิบัติการทันทีโดยไม่มีการถามยืนยันและไม่สามารถกู้คืนได้ ห้ามรันคำสั่งนี้บนระบบจริงโดยเด็ดขาด!</span>
  </div>
</div>"""

    b4_updated = b4_banner + "\n" + b4_content + "\n" + b4_warning

    # ─────────────────────────────────────────────────────────────────────────────
    # BLOCK 7: File Examining & Printing with Guide Fox Mascot
    # ─────────────────────────────────────────────────────────────────────────────
    with open('/opt/CTFd/scratch/block5_l166.txt', 'r', encoding='utf-8') as f:
        b7_content = f.read()

    b7_banner = """<div style="display: flex; align-items: center; gap: 18px; background: rgba(251, 191, 36, 0.03); border: 1px solid rgba(251, 191, 36, 0.15); border-radius: 12px; padding: 16px 20px; margin: 1.5rem 0 2rem;">
  <img src="/themes/core/static/img/stickers/fox_06_guide_point.png" alt="Guide Fox" style="width: 100px; height: auto; flex-shrink: 0; filter: drop-shadow(0 4px 12px rgba(251, 191, 36, 0.3));">
  <div>
    <strong style="color: #fbbf24; font-size: 1.05rem; display: block; margin-bottom: 4px;">🔍 อาวุธลับล่า Flag: เครื่องมืออ่านและสืบค้นเนื้อหา (Examining & Printing)</strong>
    <p style="margin: 0; color: #cbd5e1; font-size: 0.88rem; line-height: 1.6;">
      ในการแข่ง CTF คุณจะได้ใช้ <code style="color:#fbbf24;">grep</code> ค้นหา Flag จากไฟล์ขนาดมหึมา หรือใช้ <code style="color:#fbbf24;">find</code> ล่าไฟล์ที่ซ่อนอยู่ในลืบระบบ — จำเทคนิคเหล่านี้ไว้ให้ดีครับ!
    </p>
  </div>
</div>"""
    b7_updated = b7_banner + "\n" + b7_content

    # ─────────────────────────────────────────────────────────────────────────────
    # BLOCK 9: Privilege Escalation (sudo) with Root Fox Mascot
    # ─────────────────────────────────────────────────────────────────────────────
    b9_sudo = """<div style="background: linear-gradient(135deg, rgba(239, 68, 68, 0.06), rgba(15, 23, 42, 0.8)); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 14px; padding: 22px 26px; margin: 2rem auto; max-width: 1000px; display: flex; align-items: center; gap: 24px; flex-wrap: wrap;">
  <div style="text-align: center; flex-shrink: 0; margin: 0 auto;">
    <img src="/themes/core/static/img/stickers/fox_04_root_key.png" alt="Root Fox" style="width: 120px; height: auto; filter: drop-shadow(0 6px 16px rgba(239, 68, 68, 0.4));">
    <div style="font-size: 0.75rem; color: #f87171; font-weight: 700; margin-top: 4px; font-family: 'JetBrains Mono', monospace;">MASTER OF ROOT</div>
  </div>
  <div style="flex: 1; min-width: 280px;">
    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
      <span style="background: #ef4444; color: #fff; font-size: 0.7rem; font-weight: 800; padding: 2px 8px; border-radius: 4px; font-family: monospace;">PRIVILEGE ESCALATION</span>
      <h4 style="margin: 0; color: #ffffff; font-size: 1.15rem; font-weight: 800;">⚡ การยกระดับสิทธิ์สู่ Superuser ด้วยคำสั่ง sudo</h4>
    </div>
    <p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.6; margin: 0 0 10px 0;">
      ในระบบ Linux ผู้ใช้ทั่วไปจะมีสิทธิ์จำกัด ไม่สามารถเข้าถึงไดเรกทอรีสำคัญอย่าง <code>/root</code> ได้ คำสั่ง <code>sudo</code> (Superuser Do) ช่วยให้ผู้ใช้ที่ได้รับอนุญาตสามารถสั่งรันคำสั่งด้วยสิทธิ์สูงสุดของระบบ เพื่ออ่านไฟล์ที่ถูกคุ้มครองพิเศษ
    </p>
    <div style="background: #070913; border: 1px solid rgba(239, 68, 68, 0.2); border-radius: 8px; padding: 10px 16px; font-family: 'JetBrains Mono', monospace; font-size: 0.9rem; color: #fca5a5;">
      $ sudo cat /root/flag4.txt
    </div>
  </div>
</div>"""

    # ─────────────────────────────────────────────────────────────────────────────
    # BLOCK 11: File Permissions (chmod) with Robot 755 & Graduation
    # ─────────────────────────────────────────────────────────────────────────────
    b11_perm = """<!-- File Permissions deep dive -->
<div style="background: linear-gradient(135deg, rgba(15, 23, 42, 0.8), rgba(11, 15, 25, 0.95)); border: 1px solid rgba(61, 220, 132, 0.25); border-radius: 14px; padding: 24px 28px; margin: 2rem auto; max-width: 1000px; display: flex; align-items: center; gap: 24px; flex-wrap: wrap;">
  <div style="text-align: center; flex-shrink: 0; margin: 0 auto;">
    <img src="/themes/core/static/img/stickers/robot_02_chmod_755.png" alt="Permissions Robot" style="width: 125px; height: auto; filter: drop-shadow(0 6px 16px rgba(61, 220, 132, 0.35));">
    <div style="font-size: 0.75rem; color: #4ade80; font-weight: 700; margin-top: 4px; font-family: 'JetBrains Mono', monospace;">SYSADMIN CHMOD 755</div>
  </div>
  <div style="flex: 1; min-width: 280px;">
    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
      <span style="background: #22c55e; color: #000; font-size: 0.7rem; font-weight: 800; padding: 2px 8px; border-radius: 4px; font-family: monospace;">SECURITY PERMISSIONS</span>
      <h4 style="margin: 0; color: #ffffff; font-size: 1.15rem; font-weight: 800;">🛡️ โครงสร้างสิทธิ์ใน Linux: r (Read), w (Write), x (Execute)</h4>
    </div>
    <p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.6; margin: 0 0 10px 0;">
      Linux ควบคุมสิทธิ์ด้วยเลขฐานแปด (Octal Math): <code>r=4</code>, <code>w=2</code>, <code>x=1</code> สำหรับ 3 กลุ่มผู้ใช้ (Owner, Group, Others) เช่น <strong>755 = rwxr-xr-x</strong> (เจ้าของทำได้ทุกอย่าง ผู้อื่นอ่านและรันได้)
    </p>
    <div style="background: #070913; border: 1px solid rgba(61, 220, 132, 0.2); border-radius: 8px; padding: 10px 16px; font-family: 'JetBrains Mono', monospace; font-size: 0.85rem; color: #86efac;">
      rwx r-x r-x = (4+2+1) (4+0+1) (4+0+1) = 755
    </div>
  </div>
</div>

<!-- Lesson Graduation Banner -->
<div style="background: radial-gradient(circle at center, rgba(30, 41, 59, 0.9), rgba(15, 23, 42, 0.95)); border: 2px solid rgba(251, 191, 36, 0.3); border-radius: 16px; padding: 28px; margin: 3rem auto 1.5rem; text-align: center; max-width: 950px; box-shadow: 0 12px 35px rgba(0,0,0,0.5);">
  <div style="display: flex; align-items: center; justify-content: center; gap: 24px; margin-bottom: 14px;">
    <img src="/themes/core/static/img/stickers/fox_09_victory_cheer.png" alt="Victory Fox" style="width: 85px; height: auto; filter: drop-shadow(0 4px 12px rgba(239, 68, 68, 0.4));">
    <div>
      <h3 style="color: #fbbf24; font-size: 1.45rem; font-weight: 800; margin: 0 0 4px 0;">🎉 ยินดีด้วย! คุณผ่านบทเรียนคำสั่งและสิทธิ์ใน Linux สำเร็จ</h3>
      <p style="color: #94a3b8; font-size: 0.9rem; margin: 0;">ทักษะเหล่านี้คืออาวุธสำคัญที่จะนำไปใช้ต่อในบทเรียนกระบวนการ Process และการเจาะระบบใน Chapter ถัดไป!</p>
    </div>
    <img src="/themes/core/static/img/stickers/robot_09_celebrate_star.png" alt="Celebrate Robot" style="width: 85px; height: auto; filter: drop-shadow(0 4px 12px rgba(0, 240, 255, 0.4));">
  </div>
</div>"""

    # Assemble updated blocks
    blocks = json.loads(lesson.content)
    blocks[0]['value'] = b0_header
    blocks[1]['value'] = b1_structure
    blocks[4]['value'] = b4_updated
    blocks[7]['value'] = b7_updated
    blocks[9]['value'] = b9_sudo
    blocks[11]['value'] = b11_perm

    lesson.content = json.dumps(blocks, ensure_ascii=False)
    db.session.commit()
    print("Lesson 166 successfully upgraded with unified lab mission control and mascot stickers!")
