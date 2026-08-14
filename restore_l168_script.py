from CTFd import create_app
from CTFd.models import db
from CTFd.plugins.tutorials import TutorialLesson
import json

app = create_app()
with app.app_context():
    l168 = TutorialLesson.query.get(168)

    b0_header = {'type': 'markdown', 'value': '## 🛡️ โครงสร้างระบบและการจัดการสิทธิ์ใน WINDOWS (WINDOWS ARCHITECTURE & PERMISSIONS)'}

    b1_intro = {'type': 'markdown', 'value': '''<div class="s-intro cyan" style="margin-top: 1rem; margin-bottom: 2rem;">
  <div class="s-intro-icon">💻</div>
  <div class="s-intro-body">
    <strong style="font-size: 1.1rem; color: #ffffff; margin-bottom: 8px; display: block;">ภาพรวมโครงสร้างระบบและการจัดการสิทธิ์ใน Windows (Windows Architecture & Permissions)</strong>
    <p style="margin-bottom: 8px; color: #cbd5e1; font-size: 0.9rem;">ยินดีต้อนรับสู่บทเรียนระบบปฏิบัติการ <strong>Microsoft Windows</strong> ซึ่งเป็นระบบปฏิบัติการฝั่ง Desktop ที่มีผู้ใช้งานมากที่สุดในโลก (กว่า 75% ของตลาด) 💻</p>
    <p style="margin-bottom: 0; color: #cbd5e1; font-size: 0.9rem;">ในบทเรียนนี้เราจะได้เรียนรู้สถาปัตยกรรมภายในแบบ <strong>Hybrid Kernel (User Mode vs Kernel Mode)</strong>, ระบบจัดเก็บข้อมูลแบบหลายไดรฟ์ (<code>C:\\</code>, <code>D:\\</code>), โครงสร้างโฟลเดอร์สำคัญ ตลอดจนการบริหารจัดการสิทธิ์ความปลอดภัยในระบบครับ 🛡️</p>
  </div>
</div>'''}

    b2_overview = {'type': 'markdown', 'value': '''### 📌 Overviews of Windows (ภาพรวมระบบปฏิบัติการ Windows)

น้องๆ น่าจะคุ้นเคยกับ **Microsoft Windows** กันดีอยู่แล้วใช่มั้ยครับ? 😊 Windows ถือเป็น OS สำหรับคอมพิวเตอร์ตั้งโต๊ะที่มีผู้ใช้งานมากที่สุดในโลก (มากกว่า 75% ของตลาด Desktop) พัฒนาโดยบริษัท Microsoft ตั้งแต่ปี 1985 บนฐานของ MS-DOS จนวิวัฒนาการมาเป็น Windows 10 และ Windows 11 ที่เราใช้กันในปัจจุบันครับ! 🚀'''}

    b3_rings = {'type': 'markdown', 'value': '''### 🏛️ Windows System Architecture (สถาปัตยกรรมภายในของระบบปฏิบัติการ Windows)

สถาปัตยกรรมของ Windows ถูกออกแบบในลักษณะ **Hybrid Kernel** ที่แบ่งพื้นที่ทำงานออกเป็น 2 ระดับหลักคือ **User Mode** (สำหรับแอปพลิเคชันของผู้ใช้ทั่วไป) และ **Kernel Mode** (สำหรับระบบแกนกลางและไดรเวอร์อุปกรณ์) ซึ่งเป็นกลไกสำคัญในการรักษาความเสถียรและความปลอดภัยของระบบครับ! 🛡️

<style>
.wsa-wrap{width:100%;margin:2rem auto;display:flex;gap:36px;align-items:center;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:32px;box-shadow:0 4px 20px rgba(0,0,0,0.25);box-sizing:border-box;}
@media(max-width:820px){.wsa-wrap{flex-direction:column;}}
.wsa-diagram-wrap{flex-shrink:0;position:relative;width:340px;height:340px;display:flex;align-items:center;justify-content:center;}
.wsa-r-user{width:320px;height:320px;border:1.2px solid #00f0ff;border-radius:50%;background:transparent;box-shadow:0 0 12px rgba(0,240,255,0.12), inset 0 0 10px rgba(0,240,255,0.04);position:relative;display:flex;align-items:center;justify-content:center;}
.wsa-r-kernel{width:220px;height:220px;border:1.2px solid #ff007f;border-radius:50%;background:transparent;box-shadow:0 0 12px rgba(255,0,127,0.12), inset 0 0 10px rgba(255,0,127,0.04);position:relative;display:flex;align-items:center;justify-content:center;}
.wsa-r-hardware{width:120px;height:120px;border:1.2px solid #fbbf24;border-radius:50%;background:rgba(251,191,36,0.12);box-shadow:0 0 18px rgba(251,191,36,0.2), inset 0 0 10px rgba(251,191,36,0.08);display:flex;align-items:center;justify-content:center;position:relative;}
.wsa-lbl{position:absolute;font-family:'JetBrains Mono',monospace;font-size:0.75rem;font-weight:800;letter-spacing:0.04em;text-shadow:0 0 8px currentColor;white-space:nowrap;pointer-events:none;}
.wsa-lbl-user{color:#00f0ff;top:14px;left:50%;transform:translateX(-50%);}
.wsa-lbl-kernel{color:#ff007f;top:12px;left:50%;transform:translateX(-50%);}
.wsa-lbl-hw{color:#fbbf24;position:static;}
.wsa-content{display:flex;flex-direction:column;gap:16px;flex-grow:1;}
.wsa-mode-card{padding:16px 20px;border-radius:10px;background:rgba(15,17,26,0.6);border:1px solid rgba(255,255,255,0.06);}
.kernel-card{border-left:4px solid #ff007f;}
.user-card{border-left:4px solid #00f0ff;}
.wsa-mode-title{font-size:0.95rem;font-weight:800;margin-bottom:6px;}
.wsa-mode-desc{font-size:0.85rem;color:#94a3b8;line-height:1.6;margin:0;}
</style>

<div class="wsa-wrap">
<div class="wsa-diagram-wrap">
<div class="wsa-r-user">
<span class="wsa-lbl wsa-lbl-user">User Mode</span>
<div class="wsa-r-kernel">
<span class="wsa-lbl wsa-lbl-kernel">Kernel Mode</span>
<div class="wsa-r-hardware">
<span class="wsa-lbl wsa-lbl-hw">Hardware</span>
</div>
</div>
</div>
</div>
<div class="wsa-content">
<div class="wsa-mode-card kernel-card">
<div class="wsa-mode-title" style="color:#ff007f;">🔴 Kernel Mode (โหมดเคอร์เนล)</div>
<p class="wsa-mode-desc">เป็นส่วนสิทธิ์ระบบระดับสูงที่มี <strong>การเข้าถึงฮาร์ดแวร์โดยตรงและไม่มีข้อจำกัด</strong> การประมวลผลคำสั่งเคอร์เนลทั้งหมดแชร์หน่วยความจำเสมือนเพียงพื้นที่เดียว หากมีข้อผิดพลาดระบบ Windows จะล่มลงในลักษณะจอฟ้า (BSOD) ทันทีเพื่อความปลอดภัยของข้อมูล</p>
</div>
<div class="wsa-mode-card user-card">
<div class="wsa-mode-title" style="color:#00f0ff;">🔵 User Mode (โหมดผู้ใช้)</div>
<p class="wsa-mode-desc">เป็นระดับสิทธิ์ใช้งานทั่วไปสำหรับแอปพลิเคชันของผู้ใช้ ระบบ Windows จะแบ่งสัดส่วนเนื้อที่การทำงานแยกขาดจากกัน (Isolated Process Space) หากโปรแกรมใดทำงานล้มเหลวหรือปิดตัวลง จะไม่กระทบต่อระบบปฏิบัติการหลักให้เสียหายตาม</p>
</div>
</div>
</div>'''}

    b4_accounts = {'type': 'markdown', 'value': '''### 👥 Windows User Accounts (ประเภทบัญชีผู้ใช้ในระบบ Windows)

ระบบปฏิบัติการ Windows สนับสนุนการจัดการบัญชีผู้ใช้งานหลักทั้งหมด 5 ประเภท เพื่อจัดสรรสิทธิ์และควบคุมระดับความปลอดภัยในลักษณะที่แตกต่างกัน:

<style>
.w-acc-grid{display:grid;grid-template-columns:repeat(auto-fit, minmax(180px, 1fr));gap:12px;margin:1.5rem 0;}
.w-acc-card{background:rgba(15,17,26,0.5);border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:16px;display:flex;flex-direction:column;gap:8px;}
.w-acc-hdr{display:flex;align-items:center;gap:8px;}
.w-acc-icon{font-size:1.4rem;}
.w-acc-title{font-size:0.85rem;font-weight:800;font-family:'JetBrains Mono',monospace;}
.w-acc-desc{font-size:0.8rem;color:#94a3b8;line-height:1.5;margin:0;}
.clr-admin{color:#ff007f;}.clr-std{color:#00f0ff;}.clr-work{color:#a855f7;}.clr-child{color:#fbbf24;}.clr-guest{color:#94a3b8;}
</style>

<div class="w-acc-grid">
<div class="w-acc-card">
<div class="w-acc-hdr"><span class="w-acc-icon">👑</span><span class="w-acc-title clr-admin">Administrator</span></div>
<p class="w-acc-desc">บัญชีผู้ดูแลระบบสูงสุด มีสิทธิ์สร้าง/ลบ บัญชีอื่น และแก้ไขทุกอย่างในเครื่องได้โดยไม่มีข้อจำกัด</p>
</div>
<div class="w-acc-card">
<div class="w-acc-hdr"><span class="w-acc-icon">⚙️</span><span class="w-acc-title clr-admin">SYSTEM</span></div>
<p class="w-acc-desc">บัญชีบริการระบบระดับสูงสุด มีสิทธิ์เหนือ Administrator ในการจัดการเคอร์เนลและไฟล์ระบบป้องกัน</p>
</div>
<div class="w-acc-card">
<div class="w-acc-hdr"><span class="w-acc-icon">👤</span><span class="w-acc-title clr-std">Standard User</span></div>
<p class="w-acc-desc">บัญชีผู้ใช้ทั่วไป ทำงานทั่วไปได้ แต่ไม่สามารถเปลี่ยนค่าระบบหลักหรือติดตั้งซอฟต์แวร์ที่กระทบเครื่องได้</p>
</div>
<div class="w-acc-card">
<div class="w-acc-hdr"><span class="w-acc-icon">🧸</span><span class="w-acc-title clr-child">Child Account</span></div>
<p class="w-acc-desc">บัญชีประเภท Standard พิเศษที่มีระบบควบคุมโดยผู้ปกครอง (Parental Controls) ดักกรองเนื้อหาไม่ปลอดภัย</p>
</div>
<div class="w-acc-card">
<div class="w-acc-hdr"><span class="w-acc-icon">👥</span><span class="w-acc-title clr-guest">Guest Account</span></div>
<p class="w-acc-desc">บัญชีสำหรับผู้ใช้ชั่วคราว มีสิทธิ์การใช้งานต่ำสุด ไม่มีรหัสผ่าน และไม่สามารถเซฟค่าการตั้งค่าใดๆ ได้ถาวร</p>
</div>
</div>'''}

    quiz_html_168 = {'type': 'markdown', 'value': '''<style>
.mini-quiz-card { background: rgba(12, 15, 29, 0.85); border: 1px solid rgba(0, 240, 255, 0.3); border-radius: 14px; padding: 28px; margin: 2.5rem 0; box-shadow: 0 0 30px rgba(0, 240, 255, 0.12); }
.mq-hdr { display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px; padding-bottom: 14px; border-bottom: 1px solid rgba(255, 255, 255, 0.08); }
.mq-item { background: rgba(15, 17, 26, 0.6); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 10px; padding: 18px; margin-bottom: 16px; }
.mq-title { font-weight: 700; color: #ffffff; font-size: 0.92rem; margin-bottom: 12px; }
.mq-opt-btn { width: 100%; text-align: left; background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); color: #cbd5e1; padding: 10px 14px; border-radius: 8px; font-size: 0.85rem; margin-bottom: 8px; transition: all 0.2s ease; cursor: pointer; }
.mq-opt-btn:hover { background: rgba(0, 240, 255, 0.1); border-color: #00f0ff; color: #ffffff; }
.mq-opt-btn.correct { background: rgba(34, 197, 94, 0.2) !important; border-color: #22c55e !important; color: #4ade80 !important; font-weight: bold; }
.mq-opt-btn.wrong { background: rgba(239, 68, 68, 0.2) !important; border-color: #ef4444 !important; color: #fca5a5 !important; }
</style>

<div class="mini-quiz-card">
  <div class="mq-hdr">
    <div style="font-weight: 800; color: #00f0ff; font-size: 1.1rem;"><i class="fas fa-tasks mr-2"></i> Lesson Quiz (แบบทดสอบท้ายบทเรียน 05)</div>
    <span class="badge" style="background: rgba(0,240,255,0.15); color: #00f0ff; border: 1px solid #00f0ff; padding: 4px 10px; border-radius: 20px;">4 QUESTIONS</span>
  </div>

  <!-- Q1 -->
  <div class="mq-item" data-q="1">
    <div class="mq-title">Q1. ในระบบบัญชีความปลอดภัยของ Windows บัญชีข้อใดที่เป็นบัญชีสิทธิ์มาตรฐาน (Standard) แต่มีขอบเขตปกป้องความปลอดภัยพิเศษเพิ่มเติม?</div>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 0, 'A')">A. Administrator Account</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 0, 'B')">B. Guest Account</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 0, 'C')">C. Child Account</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 0, 'D')">D. SYSTEM Account</button>
  </div>

  <!-- Q2 -->
  <div class="mq-item" data-q="2">
    <div class="mq-title">Q2. ในสิทธิ์เข้าใช้ข้อมูล NTFS Permissions หากกลุ่ม User ได้รับสิทธิ์อนุญาตเข้าถึง แต่บัญชีส่วนบุคคลติดสิทธิ์ปฏิเสธเด่นชัด (Explicit Deny) ผลจะเป็นอย่างไร?</div>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 1, 'A')">A. โดนปฏิเสธการเข้าถึงทันที (Explicit Deny มีผลครอบสิทธิ์อนุญาตเสมอ)</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 1, 'B')">B. เข้าถึงได้ปกติเพราะสิทธิ์ของกลุ่มมีค่าสูงกว่า</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 1, 'C')">C. ระบบจะสุ่มขอรหัสผ่าน Administrator อีกครั้ง</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 1, 'D')">D. สามารถอ่านไฟล์ได้แต่อ่านโฟลเดอร์ไม่ได้</button>
  </div>

  <!-- Q3 -->
  <div class="mq-item" data-q="3">
    <div class="mq-title">Q3. โครงสร้างระบบปฏิบัติการ Windows ส่วนใดที่ทำหน้าที่เป็นชั้นล่างสุดในการเชื่อมต่อและควบคุมฮาร์ดแวร์โดยตรง เพื่อให้ระบบระดับบนทำงานข้ามฮาร์ดแวร์ต่างรุ่นกันได้?</div>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 2, 'A')">A. User Mode Subsystems</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 2, 'B')">B. Hardware Abstraction Layer (HAL)</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 2, 'C')">C. Windows Registry Hives</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 2, 'D')">D. Command Prompt (cmd.exe)</button>
  </div>

  <!-- Q4 -->
  <div class="mq-item" data-q="4">
    <div class="mq-title">Q4. โฟลเดอร์ระบบโฟลเดอร์ใดใน Windows ที่ใช้จัดเก็บไฟล์ระบบ 32-bit บนระบบปฏิบัติการสถาปัตยกรรมแบบ 64-bit เพื่อให้แอปย้อนหลังทำงานได้?</div>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 3, 'A')">A. C:\\Windows\\System32</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 3, 'B')">B. C:\\Windows\\SysWOW64</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 3, 'C')">C. C:\\ProgramData</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 3, 'D')">D. C:\\Users\\Public</button>
  </div>
</div>'''}

    card_168_p1 = {'type': 'markdown', 'value': '''<div style="border: 1px solid #00f0ff; background: rgba(8, 12, 25, 0.85); border-radius: 12px; padding: 24px 28px; margin-top: 2rem; margin-bottom: 1.5rem; box-shadow: 0 0 25px rgba(0, 240, 255, 0.15);">
  <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 12px;">
    <div style="font-size: 1.1rem; font-weight: 800; color: #ffffff; display: flex; align-items: center;">
      <span style="font-size: 1.4rem; margin-right: 10px;">🎯</span> เป้าหมายการทำแล็บ PART 1 - WINDOWS SYSTEM32 SECURITY AUDIT
    </div>
    <span class="badge" style="background: rgba(0, 240, 255, 0.18); color: #00f0ff; border: 1px solid #00f0ff; padding: 5px 14px; border-radius: 20px; font-size: 0.75rem; font-family: monospace; font-weight: 700;">PRIMARY LAB</span>
  </div>
  <p style="color: #cbd5e1; font-size: 0.9rem; margin-bottom: 16px; line-height: 1.6;">
    กดเปิดเซสชันคอนเทนเนอร์ Docker Instance Lab ด้านล่างเพื่อเข้าสู่ Windows Command Prompt (CMD) และใช้เซสชันนี้ในการทำแล็บย่อยทุกข้อในบทนี้ครับ!
  </p>
  <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 8px; padding: 14px 18px;">
    <div style="font-weight: 700; color: #38bdf8; font-size: 0.88rem; margin-bottom: 8px;">📌 ภารกิจปฏิบัติการ (MISSION DETAILS)</div>
    <ul style="margin: 0; padding-left: 20px; color: #cbd5e1; font-size: 0.85rem; line-height: 1.7;">
      <li>กดปุ่ม "Launch Lab Instance" ด้านล่างเพื่อเปิดการใช้งานคอนเทนเนอร์เซิร์ฟเวอร์หลัก</li>
      <li>พิมพ์คำสั่ง <code>cd C:\\Windows\\System32\\config</code> แล้วใช้ <code>type sec_flag.txt</code> อ่านเนื้อหาไฟล์ลับเพื่อนำ Flag มาตอบส่งในช่องด้านล่าง</li>
    </ul>
  </div>
</div>'''}

    card_168_p2 = {'type': 'markdown', 'value': '''<div style="border: 1px solid #a855f7; background: rgba(15, 11, 28, 0.85); border-radius: 12px; padding: 24px 28px; margin-top: 2rem; margin-bottom: 1.5rem; box-shadow: 0 0 25px rgba(168, 85, 247, 0.15);">
  <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 12px;">
    <div style="font-size: 1.1rem; font-weight: 800; color: #ffffff; display: flex; align-items: center;">
      <span style="font-size: 1.4rem; margin-right: 10px;">🎯</span> เป้าหมายการทำแล็บ PART 2 - WINDOWS TEXT FILTERING (FINDSTR)
    </div>
    <span class="badge" style="background: rgba(168, 85, 247, 0.18); color: #c084fc; border: 1px solid #a855f7; padding: 5px 14px; border-radius: 20px; font-size: 0.75rem; font-family: monospace; font-weight: 700;">SUBMISSION ONLY</span>
  </div>
  <p style="color: #cbd5e1; font-size: 0.9rem; margin-bottom: 16px; line-height: 1.6;">
    ใช้เซิร์ฟเวอร์จำลองเครื่องเดียวกับ Part 1 ในการกรองค้นหาบรรทัดที่มีข้อความ Flag ในไฟล์ Log ระบบขนาดใหญ่
  </p>
  <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 8px; padding: 14px 18px;">
    <div style="font-weight: 700; color: #c084fc; font-size: 0.88rem; margin-bottom: 8px;">📌 ภารกิจปฏิบัติการ (MISSION DETAILS)</div>
    <ul style="margin: 0; padding-left: 20px; color: #cbd5e1; font-size: 0.85rem; line-height: 1.7;">
      <li>สลับไปยังหน้าต่าง Terminal ของ Part 1 แล้วพิมพ์คำสั่ง <code>findstr "FLAG" C:\\ProgramData\\Microsoft\\Logs\\system_env.log</code></li>
      <li>นำ Flag ที่ได้ส่งคำตอบในช่องด้านล่าง <em>(ไม่ต้องกดเปิดเครื่องใหม่)</em></li>
    </ul>
  </div>
</div>'''}

    card_168_p3 = {'type': 'markdown', 'value': '''<div style="border: 1px solid #22c55e; background: rgba(8, 24, 18, 0.85); border-radius: 12px; padding: 24px 28px; margin-top: 2rem; margin-bottom: 1.5rem; box-shadow: 0 0 25px rgba(34, 197, 94, 0.15);">
  <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 12px;">
    <div style="font-size: 1.1rem; font-weight: 800; color: #ffffff; display: flex; align-items: center;">
      <span style="font-size: 1.4rem; margin-right: 10px;">🎯</span> เป้าหมายการทำแล็บ PART 3 - SYSTEM RESOURCES SEARCH
    </div>
    <span class="badge" style="background: rgba(34, 197, 94, 0.18); color: #4ade80; border: 1px solid #22c55e; padding: 5px 14px; border-radius: 20px; font-size: 0.75rem; font-family: monospace; font-weight: 700;">SUBMISSION ONLY</span>
  </div>
  <p style="color: #cbd5e1; font-size: 0.9rem; margin-bottom: 16px; line-height: 1.6;">
    ใช้เซิร์ฟเวอร์จำลองเครื่องเดียวกับ Part 1 ในการสำรวจโฟลเดอร์ทรัพยากรสถาปัตยกรรมระบบ
  </p>
  <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 8px; padding: 14px 18px;">
    <div style="font-weight: 700; color: #4ade80; font-size: 0.88rem; margin-bottom: 8px;">📌 ภารกิจปฏิบัติการ (MISSION DETAILS)</div>
    <ul style="margin: 0; padding-left: 20px; color: #cbd5e1; font-size: 0.85rem; line-height: 1.7;">
      <li>สลับไปยังหน้าต่าง Terminal ของ Part 1 แล้วพิมพ์คำสั่ง <code>type C:\\Windows\\SystemResources\\arch_flag.txt</code></li>
      <li>นำ Flag ที่ได้ส่งคำตอบในช่องด้านล่าง <em>(ไม่ต้องกดเปิดเครื่องใหม่)</em></li>
    </ul>
  </div>
</div>'''}

    lab_header_168 = {'type': 'markdown', 'value': '## 🛠️ WINDOWS SECURITY & ARCHITECTURE PRACTICE LABS (ห้องปฏิบัติการจำลองการใช้คำสั่ง WINDOWS)'}

    final_168 = [
        b0_header,
        b1_intro,
        b2_overview,
        b3_rings,
        b4_accounts,
        lab_header_168,
        card_168_p1,
        {'type': 'challenge', 'challenge_id': 46},
        card_168_p2,
        {'type': 'challenge', 'challenge_id': 47},
        card_168_p3,
        {'type': 'challenge', 'challenge_id': 48},
        quiz_html_168
    ]

    l168.content = json.dumps(final_168, ensure_ascii=False)
    db.session.commit()
    print("SUCCESSFULLY RESTORED LESSON 168 FULL LECTURE AND QUIZ VIA FILE!")
