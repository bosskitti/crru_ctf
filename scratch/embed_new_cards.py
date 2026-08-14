import json
import sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

# ============================================================
# Card HTML definitions with customized accent colors
# ============================================================

# XSS Cards (Amber/Orange accent)
card_xss_reflected = """<div style="background:#070a13;border:1px solid rgba(251,191,36,0.3);border-radius:12px;padding:24px;margin:2.5rem auto 1.5rem;max-width:1000px;box-shadow:0 10px 30px rgba(251,191,36,0.15);position:relative;overflow:hidden;">
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg, #fbbf24, #f59e0b);"></div>
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
    <h4 style="margin:0;font-size:1.15rem;font-weight:800;color:#ffffff;display:flex;align-items:center;gap:8px;">
      <span style="font-size:1.3rem;">🎯</span> เป้าหมายการทำแล็บ (OBJECTIVE) - Reflected XSS (Cookie Theft)
    </h4>
    <span style="font-size:0.68rem;font-family:monospace;font-weight:700;padding:3px 10px;border-radius:20px;background:rgba(251,191,36,0.1);color:#fbbf24;border:1px solid rgba(251,191,36,0.25);">LAB: APPRENTICE</span>
  </div>
  <p style="margin:0 0 16px;font-size:0.83rem;color:#cbd5e1;line-height:1.6;">
    เรียนรู้การโจมตีประเภท Cross-Site Scripting (XSS) ในรูปแบบ Reflected ซึ่งแอปพลิเคชันจะรับอินพุตผ่านพารามิเตอร์ URL แล้วสะท้อนกลับมาแสดงบนหน้าเว็บทันทีโดยไม่มีการกรองความปลอดภัย
  </p>
  <div style="background:rgba(0,0,0,0.25);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:16px;margin:0;">
    <h5 style="margin:0 0 8px;font-size:0.8rem;color:#fbbf24;font-weight:bold;text-transform:uppercase;letter-spacing:0.05em;">📌 ภารกิจการเจาะระบบ (Mission details)</h5>
    <ul style="margin:0;padding-left:20px;font-size:0.78rem;color:#94a3b8;line-height:1.6;">
      <li>ป้อน Script Payload ลงในช่องค้นหาสินค้าเพื่อทดสอบการรันโค้ดฝั่งไคลเอนต์</li>
      <li>เขียนคำสั่งอ่านค่าคุกกี้เซสชันส่วนบุคคล (<code>document.cookie</code>) เพื่อดึงรหัส Flag ที่ถูกบันทึกไว้ในเบราว์เซอร์</li>
      <li>นำรหัส Flag ที่ได้ไปส่งเพื่อผ่านด่าน</li>
    </ul>
  </div>
</div>"""

card_xss_stored = """<div style="background:#070a13;border:1px solid rgba(251,191,36,0.3);border-radius:12px;padding:24px;margin:2.5rem auto 1.5rem;max-width:1000px;box-shadow:0 10px 30px rgba(251,191,36,0.15);position:relative;overflow:hidden;">
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg, #fbbf24, #f59e0b);"></div>
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
    <h4 style="margin:0;font-size:1.15rem;font-weight:800;color:#ffffff;display:flex;align-items:center;gap:8px;">
      <span style="font-size:1.3rem;">🎯</span> เป้าหมายการทำแล็บ (OBJECTIVE) - Stored XSS (Persistent Attack)
    </h4>
    <span style="font-size:0.68rem;font-family:monospace;font-weight:700;padding:3px 10px;border-radius:20px;background:rgba(251,191,36,0.1);color:#fbbf24;border:1px solid rgba(251,191,36,0.25);">LAB: PRACTITIONER</span>
  </div>
  <p style="margin:0 0 16px;font-size:0.83rem;color:#cbd5e1;line-height:1.6;">
    ทดสอบการโจมตีประเภท Stored XSS หรือแบบฝังตัวถาวร โดยสคริปต์ที่ส่งจะถูกบันทึกลงในฐานข้อมูลหลังบ้าน และเริ่มทำงานอัตโนมัติสำหรับทุกคนที่เปิดเข้ามาอ่านเนื้อหาในภายหลัง
  </p>
  <div style="background:rgba(0,0,0,0.25);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:16px;margin:0;">
    <h5 style="margin:0 0 8px;font-size:0.8rem;color:#fbbf24;font-weight:bold;text-transform:uppercase;letter-spacing:0.05em;">📌 ภารกิจการเจาะระบบ (Mission details)</h5>
    <ul style="margin:0;padding-left:20px;font-size:0.78rem;color:#94a3b8;line-height:1.6;">
      <li>เขียนสคริปต์ประสงค์ร้ายลงในฟอร์มช่องแสดงความคิดเห็น (Comment Box)</li>
      <li>ใช้ JavaScript เพื่อเข้าถึงค่าความลับของระบบที่ถูกเซ็ตไว้ในตัวแปรภาษาเบราว์เซอร์ ชื่อ <code>secretFlag</code></li>
      <li>โพสต์ความเห็นแล้วรับรหัส Flag จากหน้าต่างแจ้งเตือนที่ป็อปอัปแสดงขึ้นมา</li>
    </ul>
  </div>
</div>"""

card_xss_dom = """<div style="background:#070a13;border:1px solid rgba(251,191,36,0.3);border-radius:12px;padding:24px;margin:2.5rem auto 1.5rem;max-width:1000px;box-shadow:0 10px 30px rgba(251,191,36,0.15);position:relative;overflow:hidden;">
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg, #fbbf24, #f59e0b);"></div>
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
    <h4 style="margin:0;font-size:1.15rem;font-weight:800;color:#ffffff;display:flex;align-items:center;gap:8px;">
      <span style="font-size:1.3rem;">🎯</span> เป้าหมายการทำแล็บ (OBJECTIVE) - DOM-Based XSS (Client-Side Injection)
    </h4>
    <span style="font-size:0.68rem;font-family:monospace;font-weight:700;padding:3px 10px;border-radius:20px;background:rgba(251,191,36,0.1);color:#fbbf24;border:1px solid rgba(251,191,36,0.25);">LAB: PRACTITIONER</span>
  </div>
  <p style="margin:0 0 16px;font-size:0.83rem;color:#cbd5e1;line-height:1.6;">
    เรียนรู้การโจมตีช่องโหว่ XSS ที่เกิดขึ้นบนฝั่งไคลเอนต์โดยตรง ผ่านการจัดการข้อมูลบนหน้าเว็บ (DOM) ที่ไม่มีการกรอง ซึ่งช่องโหว่นี้จะไม่ผ่านการตรวจสอบจากฝั่งเซิร์ฟเวอร์หลังบ้านเลย
  </p>
  <div style="background:rgba(0,0,0,0.25);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:16px;margin:0;">
    <h5 style="margin:0 0 8px;font-size:0.8rem;color:#fbbf24;font-weight:bold;text-transform:uppercase;letter-spacing:0.05em;">📌 ภารกิจการเจาะระบบ (Mission details)</h5>
    <ul style="margin:0;padding-left:20px;font-size:0.78rem;color:#94a3b8;line-height:1.6;">
      <li>วิเคราะห์โครงสร้างโค้ดหน้าเว็บที่มีตรรกะอ่านค่าจาก URL Hash Fragment (เครื่องหมาย <code>#</code>)</li>
      <li>ป้อนอินพุตพิเศษผ่าน URL (เช่น แท็กรูปภาพ <code>&lt;img&gt;</code> ที่ทำงานผ่านเหตุการณ์ผิดพลาด <code>onerror</code>)</li>
      <li>รันคำสั่งสั่งงานให้แสดงผลค่าลับ <code>FLAG</code> บนระบบกล่องแจ้งเตือนความปลอดภัย</li>
    </ul>
  </div>
</div>"""

# Brute Force Cards (Cyan/Blue accent)
card_brute_pin = """<div style="background:#070a13;border:1px solid rgba(0,240,255,0.3);border-radius:12px;padding:24px;margin:2.5rem auto 1.5rem;max-width:1000px;box-shadow:0 10px 30px rgba(0,240,255,0.15);position:relative;overflow:hidden;">
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg, #00f0ff, #3b82f6);"></div>
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
    <h4 style="margin:0;font-size:1.15rem;font-weight:800;color:#ffffff;display:flex;align-items:center;gap:8px;">
      <span style="font-size:1.3rem;">🎯</span> เป้าหมายการทำแล็บ (OBJECTIVE) - Brute Force (PIN Lock)
    </h4>
    <span style="font-size:0.68rem;font-family:monospace;font-weight:700;padding:3px 10px;border-radius:20px;background:rgba(0,240,255,0.1);color:#00f0ff;border:1px solid rgba(0,240,255,0.25);">LAB: APPRENTICE</span>
  </div>
  <p style="margin:0 0 16px;font-size:0.83rem;color:#cbd5e1;line-height:1.6;">
    โจมตีระบบรักษาความปลอดภัยแบบตัวเลขสี่หลัก (PIN) บนเว็บแอปพลิเคชันที่ไม่มีนโยบายการป้องกันการคาดเดาข้อมูลจำนวนมาก (No Rate Limiting หรือ Lockout)
  </p>
  <div style="background:rgba(0,0,0,0.25);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:16px;margin:0;">
    <h5 style="margin:0 0 8px;font-size:0.8rem;color:#fbbf24;font-weight:bold;text-transform:uppercase;letter-spacing:0.05em;">📌 ภารกิจการเจาะระบบ (Mission details)</h5>
    <ul style="margin:0;padding-left:20px;font-size:0.78rem;color:#94a3b8;line-height:1.6;">
      <li>วิเคราะห์การส่งข้อมูลในขั้นตอน POST Request สำหรับปลดล็อก PIN</li>
      <li>เขียนสคริปต์สั้นๆ ด้วยภาษา Python เพื่อวนลูปส่งค่าตัวเลขตั้งแต่ <code>0000</code> ถึง <code>9999</code></li>
      <li>ดึงผลลัพธ์รหัส Flag เมื่อป้อน PIN ได้ถูกต้องสมบูรณ์</li>
    </ul>
  </div>
</div>"""

card_brute_login = """<div style="background:#070a13;border:1px solid rgba(0,240,255,0.3);border-radius:12px;padding:24px;margin:2.5rem auto 1.5rem;max-width:1000px;box-shadow:0 10px 30px rgba(0,240,255,0.15);position:relative;overflow:hidden;">
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg, #00f0ff, #3b82f6);"></div>
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
    <h4 style="margin:0;font-size:1.15rem;font-weight:800;color:#ffffff;display:flex;align-items:center;gap:8px;">
      <span style="font-size:1.3rem;">🎯</span> เป้าหมายการทำแล็บ (OBJECTIVE) - Brute Force (Dictionary Attack)
    </h4>
    <span style="font-size:0.68rem;font-family:monospace;font-weight:700;padding:3px 10px;border-radius:20px;background:rgba(0,240,255,0.1);color:#00f0ff;border:1px solid rgba(0,240,255,0.25);">LAB: PRACTITIONER</span>
  </div>
  <p style="margin:0 0 16px;font-size:0.83rem;color:#cbd5e1;line-height:1.6;">
    เจาะระบบล็อกอินผ่านการใช้พจนานุกรมรหัสผ่าน (Wordlist) ในการคาดเดารหัสผ่านที่ใช้คำทั่วไปในภาษาอังกฤษ โดยที่ระบบเป้าหมายไม่มีกลไกแจ้งเตือนการโจมตีแบบเดาสุ่ม
  </p>
  <div style="background:rgba(0,0,0,0.25);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:16px;margin:0;">
    <h5 style="margin:0 0 8px;font-size:0.8rem;color:#fbbf24;font-weight:bold;text-transform:uppercase;letter-spacing:0.05em;">📌 ภารกิจการเจาะระบบ (Mission details)</h5>
    <ul style="margin:0;padding-left:20px;font-size:0.78rem;color:#94a3b8;line-height:1.6;">
      <li>ล็อกเป้าหมายฟอร์มล็อกอินแอดมินที่มีชื่อผู้ใช้ว่า <code>admin</code></li>
      <li>ใช้เครื่องมือโจมตีรหัสผ่านเช่น Hydra/WFUZZ หรือเขียนสคริปต์เรียกเทียบข้อมูลคำศัพท์จาก <code>rockyou.txt</code></li>
      <li>จำแนกการตอบสนองของความยาวเว็บ (Response Size) หรือสถานะเพื่อชิง Flag สิทธิ์ดูแลระบบ</li>
    </ul>
  </div>
</div>"""

# LFI Cards (Purple/Magenta accent)
card_lfi_simple = """<div style="background:#070a13;border:1px solid rgba(168,85,247,0.3);border-radius:12px;padding:24px;margin:2.5rem auto 1.5rem;max-width:1000px;box-shadow:0 10px 30px rgba(168,85,247,0.15);position:relative;overflow:hidden;">
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg, #a855f7, #ec4899);"></div>
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
    <h4 style="margin:0;font-size:1.15rem;font-weight:800;color:#ffffff;display:flex;align-items:center;gap:8px;">
      <span style="font-size:1.3rem;">🎯</span> เป้าหมายการทำแล็บ (OBJECTIVE) - Local File Inclusion (Simple)
    </h4>
    <span style="font-size:0.68rem;font-family:monospace;font-weight:700;padding:3px 10px;border-radius:20px;background:rgba(168,85,247,0.1);color:#a855f7;border:1px solid rgba(168,85,247,0.25);">LAB: APPRENTICE</span>
  </div>
  <p style="margin:0 0 16px;font-size:0.83rem;color:#cbd5e1;line-height:1.6;">
    เรียกเข้าถึงไฟล์ความลับบนเซิร์ฟเวอร์หลักผ่านฟังก์ชันเรียกโหลดเพจย่อย <code>include()</code> ที่มีช่องโหว่ Local File Inclusion (LFI) เนื่องจากไม่มีการกรองเส้นทางข้อมูลพาธเลย
  </p>
  <div style="background:rgba(0,0,0,0.25);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:16px;margin:0;">
    <h5 style="margin:0 0 8px;font-size:0.8rem;color:#fbbf24;font-weight:bold;text-transform:uppercase;letter-spacing:0.05em;">📌 ภารกิจการเจาะระบบ (Mission details)</h5>
    <ul style="margin:0;padding-left:20px;font-size:0.78rem;color:#94a3b8;line-height:1.6;">
      <li>วิเคราะห์พารามิเตอร์ URL ในระบบที่ใช้โหลดไดนามิกคอนเทนต์ (เช่น <code>?page=home.php</code>)</li>
      <li>ใช้เทคนิค Path Traversal ดึงประวัติย้อนกลับออกไปด้านนอก (เช่น <code>../</code>)</li>
      <li>อ่านไฟล์สำคัญ <code>/flag.txt</code> ในระบบเพื่อชิง Flag</li>
    </ul>
  </div>
</div>"""

card_lfi_filter = """<div style="background:#070a13;border:1px solid rgba(168,85,247,0.3);border-radius:12px;padding:24px;margin:2.5rem auto 1.5rem;max-width:1000px;box-shadow:0 10px 30px rgba(168,85,247,0.15);position:relative;overflow:hidden;">
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg, #a855f7, #ec4899);"></div>
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
    <h4 style="margin:0;font-size:1.15rem;font-weight:800;color:#ffffff;display:flex;align-items:center;gap:8px;">
      <span style="font-size:1.3rem;">🎯</span> เป้าหมายการทำแล็บ (OBJECTIVE) - LFI (PHP Stream Filter Bypass)
    </h4>
    <span style="font-size:0.68rem;font-family:monospace;font-weight:700;padding:3px 10px;border-radius:20px;background:rgba(168,85,247,0.1);color:#a855f7;border:1px solid rgba(168,85,247,0.25);">LAB: PRACTITIONER</span>
  </div>
  <p style="margin:0 0 16px;font-size:0.83rem;color:#cbd5e1;line-height:1.6;">
    หลบเลี่ยงการสแกนความปลอดภัยที่ตัดหรือระงับตัวอักษรย้อนพาธ <code>..</code> ด้วยการเรียกใช้กลไก PHP Stream Wrapper ในการแปลงข้อมูลของซอร์สโค้ดไฟล์เป้าหมายก่อนโดนระบบประมวลผล
  </p>
  <div style="background:rgba(0,0,0,0.25);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:16px;margin:0;">
    <h5 style="margin:0 0 8px;font-size:0.8rem;color:#fbbf24;font-weight:bold;text-transform:uppercase;letter-spacing:0.05em;">📌 ภารกิจการเจาะระบบ (Mission details)</h5>
    <ul style="margin:0;padding-left:20px;font-size:0.78rem;color:#94a3b8;line-height:1.6;">
      <li>ระบบตัดตัวอักษรย้อนพาธทั้งหมดและบังคับเติมนามสกุลไฟล์ <code>.php</code> ต่อท้าย</li>
      <li>ใช้ Stream Wrapper พิเศษ (<code>php://filter/...</code>) สั่งให้แอปพลิเคชันแปลงโค้ดเป้าหมายออกมาเป็น Base64 String</li>
      <li>ถอดรหัส Base64 ของไฟล์ <code>secret_config.php</code> ที่ชิงออกมาได้สำเร็จ เพื่อกู้รหัส Flag</li>
    </ul>
  </div>
</div>"""

# Command Injection Card (Red/Pink accent)
card_cmd_blind = """<div style="background:#070a13;border:1px solid rgba(239,68,68,0.3);border-radius:12px;padding:24px;margin:2.5rem auto 1.5rem;max-width:1000px;box-shadow:0 10px 30px rgba(239,68,68,0.15);position:relative;overflow:hidden;">
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg, #ef4444, #ec4899);"></div>
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
    <h4 style="margin:0;font-size:1.15rem;font-weight:800;color:#ffffff;display:flex;align-items:center;gap:8px;">
      <span style="font-size:1.3rem;">🎯</span> เป้าหมายการทำแล็บ (OBJECTIVE) - Blind Command Injection
    </h4>
    <span style="font-size:0.68rem;font-family:monospace;font-weight:700;padding:3px 10px;border-radius:20px;background:rgba(239,68,68,0.1);color:#ef4444;border:1px solid rgba(239,68,68,0.25);">LAB: PRACTITIONER</span>
  </div>
  <p style="margin:0 0 16px;font-size:0.83rem;color:#cbd5e1;line-height:1.6;">
    โจมตีฝั่งระบบปฏิบัติการเป้าหมายผ่านช่องโหว่ OS Command Injection โดยที่แอปพลิเคชันไม่มีการคืนค่าประมวลผล (Output) หรือข้อความแจ้งเตือนใดๆ กลับมาแสดงบนหน้าเว็บ (Blind)
  </p>
  <div style="background:rgba(0,0,0,0.25);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:16px;margin:0;">
    <h5 style="margin:0 0 8px;font-size:0.8rem;color:#fbbf24;font-weight:bold;text-transform:uppercase;letter-spacing:0.05em;">📌 ภารกิจการเจาะระบบ (Mission details)</h5>
    <ul style="margin:0;padding-left:20px;font-size:0.78rem;color:#94a3b8;line-height:1.6;">
      <li>แทรกสัญลักษณ์คำสั่งต่อเนื่อง (เช่น <code>;</code>) ลงในกล่องคิวรีเครื่องมือ DNS Lookup</li>
      <li>ทดลองใช้เทคนิคหน่วงเวลาเพื่อเช็คผลตอบสนองของเว็บโฮสต์หลังบ้าน (เช่น สั่งป้อน <code>; sleep 5</code>)</li>
      <li>คัดลอกไฟล์แฟลก <code>/flag.txt</code> ไปไว้ที่เส้นทางเว็บแชร์ปกติ (เช่น <code>/var/www/html/flag_out.txt</code>) เพื่อเปิดอ่านและเก็บ Flag</li>
    </ul>
  </div>
</div>"""

# CSRF & Clickjacking Cards (Green/Emerald accent)
card_csrf = """<div style="background:#070a13;border:1px solid rgba(16,185,129,0.3);border-radius:12px;padding:24px;margin:2.5rem auto 1.5rem;max-width:1000px;box-shadow:0 10px 30px rgba(16,185,129,0.15);position:relative;overflow:hidden;">
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg, #10b981, #059669);"></div>
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
    <h4 style="margin:0;font-size:1.15rem;font-weight:800;color:#ffffff;display:flex;align-items:center;gap:8px;">
      <span style="font-size:1.3rem;">🎯</span> เป้าหมายการทำแล็บ (OBJECTIVE) - CSRF (Token Bypass)
    </h4>
    <span style="font-size:0.68rem;font-family:monospace;font-weight:700;padding:3px 10px;border-radius:20px;background:rgba(16,185,129,0.1);color:#10b981;border:1px solid rgba(16,185,129,0.25);">LAB: PRACTITIONER</span>
  </div>
  <p style="margin:0 0 16px;font-size:0.83rem;color:#cbd5e1;line-height:1.6;">
    โจมตีสิทธิ์ทำธุรกรรมออนไลน์แบบจำลองผ่านช่องโหว่ Cross-Site Request Forgery (CSRF) เนื่องจากแบบฟอร์มการโอนเงินของเป้าหมายไม่มีตัวป้องกันความถูกต้อง (No CSRF Token)
  </p>
  <div style="background:rgba(0,0,0,0.25);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:16px;margin:0;">
    <h5 style="margin:0 0 8px;font-size:0.8rem;color:#fbbf24;font-weight:bold;text-transform:uppercase;letter-spacing:0.05em;">📌 ภารกิจการเจาะระบบ (Mission details)</h5>
    <ul style="margin:0;padding-left:20px;font-size:0.78rem;color:#94a3b8;line-height:1.6;">
      <li>ล็อกอินเข้าระบบ SecureBank ด้วยสิทธิ์บัญชี <code>admin / password123</code> เพื่อเซ็ตระบบคุกกี้เซสชัน</li>
      <li>เปิดหน้าเว็บโจมตีของแฮกเกอร์ <code>/attacker.php</code> ในอีกหน้าต่างเบราว์เซอร์เดียวกัน</li>
      <li>ปล่อยให้สคริปต์แฮกเกอร์ส่งธุรกรรมถอนเงินแทนผู้ใช้เพื่อเผย Flag หลัก</li>
    </ul>
  </div>
</div>"""

card_clickjacking = """<div style="background:#070a13;border:1px solid rgba(16,185,129,0.3);border-radius:12px;padding:24px;margin:2.5rem auto 1.5rem;max-width:1000px;box-shadow:0 10px 30px rgba(16,185,129,0.15);position:relative;overflow:hidden;">
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg, #10b981, #059669);"></div>
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
    <h4 style="margin:0;font-size:1.15rem;font-weight:800;color:#ffffff;display:flex;align-items:center;gap:8px;">
      <span style="font-size:1.3rem;">🎯</span> เป้าหมายการทำแล็บ (OBJECTIVE) - Clickjacking (UI Redressing)
    </h4>
    <span style="font-size:0.68rem;font-family:monospace;font-weight:700;padding:3px 10px;border-radius:20px;background:rgba(16,185,129,0.1);color:#10b981;border:1px solid rgba(16,185,129,0.25);">LAB: APPRENTICE</span>
  </div>
  <p style="margin:0 0 16px;font-size:0.83rem;color:#cbd5e1;line-height:1.6;">
    ทดสอบการโจมตีฝั่งเป้าหมายด้วยการหลอกลวงองค์ประกอบอินเทอร์เฟซ (UI Redressing) ซ้อนทับหน้าควบคุมระบบจริงที่มองไม่เห็น บนหน้าเว็บไซต์รางวัลปลอม
  </p>
  <div style="background:rgba(0,0,0,0.25);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:16px;margin:0;">
    <h5 style="margin:0 0 8px;font-size:0.8rem;color:#fbbf24;font-weight:bold;text-transform:uppercase;letter-spacing:0.05em;">📌 ภารกิจการเจาะระบบ (Mission details)</h5>
    <ul style="margin:0;padding-left:20px;font-size:0.78rem;color:#94a3b8;line-height:1.6;">
      <li>เข้าวิเคราะห์หน้าเหยื่อ <code>/victim.php</code> ซึ่งไม่มีนโยบายการป้องกันการครอบเฟรม (X-Frame-Options)</li>
      <li>เปิดหน้าของแฮกเกอร์ <code>/attacker.php</code> แล้วกดคลิกรับของรางวัลที่ล่อลวงไว้</li>
      <li>กลับมาเช็คความเปลี่ยนแปลงที่หน้าของเหยื่อเพื่อกู้รหัส Flag</li>
    </ul>
  </div>
</div>"""


# ============================================================
# Core logic to inject cards cleanly into lessons 178 and 179
# ============================================================

with app.app_context():
    # 1. Update Lesson 178
    l178 = TutorialLesson.query.get(178)
    if l178:
        # Load blocks
        blocks = json.loads(l178.content)
        print(f"Original Lesson 178 blocks count: {len(blocks)}")
        
        # We need to construct a new blocks array
        # Standard lesson 178 structure:
        #   Block 0: Content slides markdown
        #   Block 1: Sandbox markdown
        #   Blocks 2 to 9: Challenge Console blocks for challenges 25-32
        #   Block 10: Quiz markdown
        
        # Let's verify we have exactly 11 blocks right now (from create_labs.py)
        if len(blocks) == 11:
            content_slides = blocks[0]
            sandbox_slide = blocks[1]
            chal_25 = blocks[2]
            chal_26 = blocks[3]
            chal_27 = blocks[4]
            chal_28 = blocks[5]
            chal_29 = blocks[6]
            chal_30 = blocks[7]
            chal_31 = blocks[8]
            chal_32 = blocks[9]
            quiz_slide = blocks[10]
            
            # Reconstruct with markdown cards before each challenge block
            new_blocks = [
                content_slides,
                sandbox_slide,
                
                {"type": "markdown", "value": card_xss_reflected},
                chal_25,
                
                {"type": "markdown", "value": card_xss_stored},
                chal_26,
                
                {"type": "markdown", "value": card_xss_dom},
                chal_27,
                
                {"type": "markdown", "value": card_brute_pin},
                chal_28,
                
                {"type": "markdown", "value": card_brute_login},
                chal_29,
                
                {"type": "markdown", "value": card_lfi_simple},
                chal_30,
                
                {"type": "markdown", "value": card_lfi_filter},
                chal_31,
                
                {"type": "markdown", "value": card_cmd_blind},
                chal_32,
                
                quiz_slide
            ]
            
            l178.content = json.dumps(new_blocks, ensure_ascii=False)
            print("SUCCESS: Embedded Lesson 178 cards successfully!")
        else:
            print("WARNING: Lesson 178 blocks count is not 11. Skipping direct rebuild.")
            
    # 2. Update Lesson 179
    l179 = TutorialLesson.query.get(179)
    if l179:
        blocks = json.loads(l179.content)
        print(f"Original Lesson 179 blocks count: {len(blocks)}")
        
        # We need to construct a new blocks array
        # Standard lesson 179 structure:
        #   Block 0: Content slides markdown
        #   Block 1: Sandbox markdown
        #   Blocks 2 to 3: Challenge Console blocks for challenges 33-34
        #   Block 4: Quiz markdown
        
        if len(blocks) == 5:
            content_slides = blocks[0]
            sandbox_slide = blocks[1]
            chal_33 = blocks[2]
            chal_34 = blocks[3]
            quiz_slide = blocks[4]
            
            # Reconstruct with markdown cards before each challenge block
            new_blocks = [
                content_slides,
                sandbox_slide,
                
                {"type": "markdown", "value": card_csrf},
                chal_33,
                
                {"type": "markdown", "value": card_clickjacking},
                chal_34,
                
                quiz_slide
            ]
            
            l179.content = json.dumps(new_blocks, ensure_ascii=False)
            print("SUCCESS: Embedded Lesson 179 cards successfully!")
        else:
            print("WARNING: Lesson 179 blocks count is not 5. Skipping direct rebuild.")

    app.db.session.commit()
    print("Database committed successfully!")
