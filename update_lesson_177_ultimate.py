import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

ultimate_content = """<div style="text-align: center; margin-bottom: 2rem; padding: 24px; background: linear-gradient(135deg, rgba(6,182,212,0.15) 0%, rgba(59,130,246,0.15) 100%); border: 1px solid rgba(6,182,212,0.3); border-radius: 16px; box-shadow: 0 0 20px rgba(6,182,212,0.15);">
<h2 style="margin: 0; font-size: 1.9rem; font-weight: 800; color: #ffffff; text-shadow: 0 0 12px rgba(6,182,212,0.6); letter-spacing: 0.03em;">🌐 Web Application Security & OWASP</h2>
<p style="margin: 8px 0 0 0; font-size: 0.92rem; color: #cbd5e1;">เรียนรู้สถาปัตยกรรมเว็บแอปพลิเคชัน โครงสร้างความเสี่ยง OWASP Top 10 และเทคนิคการตรวจสอบความปลอดภัยฝั่งเบราว์เซอร์</p>
</div>

### 🌐 ภาพรวมวิทยาการการโจมตีเว็บ (Web Exploitation Overviews)
- **Web Exploitation**: หมายถึงกระบวนการค้นหา วิเคราะห์ และการใช้ประโยชน์จากช่องโหว่ความมั่นคงปลอดภัยในแอปพลิเคชันเว็บ เพื่อเข้าถึงข้อมูลโดยไม่ได้รับอนุญาต (Unauthorized Access), ดึงสารสนเทศที่เป็นความลับ หรือครอบครองสิทธิ์การเข้าถึงระบบควบคุมเซิร์ฟเวอร์หลังบ้าน
- เป็นแกนหลักที่สำคัญมากในสายงานความปลอดภัยไซเบอร์ โดยเฉพาะอย่างยิ่งในการทำงานด้าน **การเจาะระบบแบบมีคุณธรรม (Ethical Hacking)** และ **การทดสอบเจาะระบบ (Penetration Testing)**

---

### 📄 มาตรฐานความเสี่ยง OWASP Top 10
- **OWASP Top 10**: เป็นเอกสารรายงานเชิงความมั่นคงสากลที่ชี้เป้า 10 อันดับความเสี่ยงสูงสุดที่เป็นอันตรายต่อแอปพลิเคชันเว็บ โดยจัดทำและเผยแพร่โดยองค์กรไม่แสวงหากำไร **Open Web Application Security Project (OWASP)** เพื่อให้นักพัฒนาและผู้ดูแลระบบนำไปตั้งรับและแก้ไข
- การปรับปรุงมาตรฐานเกิดขึ้นเป็นรอบปี โดยมีรุ่นแก้ไขสำคัญ ได้แก่ รุ่น 2003 (รุ่นแรก), 2004, 2007, 2010, 2013, 2017, 2021 และรุ่นล่าสุดในปัจจุบัน **(OWASP Top 10 Release 2025/2026)**

---

### 🛡️ รายละเอียดช่องโหว่ OWASP Top 10 (A01 - A10)

<div style="display: flex; flex-direction: column; gap: 16px; margin: 1.5rem auto;">

  <div style="background: rgba(255,255,255,0.015); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
    <strong style="color: #ff007f; font-size: 1rem; display: block; margin-bottom: 6px;">🔴 A01:2025 - Broken Access Control (การควบคุมสิทธิ์บกพร่อง)</strong>
    <span style="color: #cbd5e1; font-size: 0.84rem; line-height: 1.6; display: block;">
      • <strong>คำจำกัดความ</strong>: เกิดขึ้นเมื่อระบบไม่บังคับการควบคุมสิทธิ์อย่างถูกต้อง ทำให้ผู้ใช้ธรรมดาสามารถข้ามไปดึงข้อมูลหรือเข้าถึงฟังก์ชันระดับสูงที่ตนเองไม่มีสิทธิ์ใช้งาน<br>
      • <strong>ตัวอย่าง</strong>: การแอบเข้าถึงหน้าจัดการแอดมินหลังบ้านตรงๆ โดยไม่ผ่านการล็อกอิน (เช่น พิมพ์เข้าทาง <code style="color: #00f0ff;">/admin</code>) หรือการเปลี่ยนตัวเลขพารามิเตอร์เพื่อเข้าดูข้อมูลผู้ใช้อื่น เช่น เปลี่ยน URL จาก <code style="color: #00f0ff;">/profile/view/12345</code> เป็น <code style="color: #00f0ff;">/profile/view/12346</code>
    </span>
  </div>

  <div style="background: rgba(255,255,255,0.015); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
    <strong style="color: #ff007f; font-size: 1rem; display: block; margin-bottom: 6px;">🔴 A02:2025 - Security Misconfiguration (การกำหนดค่าความปลอดภัยผิดพลาด)</strong>
    <span style="color: #cbd5e1; font-size: 0.84rem; line-height: 1.6; display: block;">
      • <strong>คำจำกัดความ</strong>: เกิดขึ้นจากการกำหนดสิทธิ์และการตั้งค่าความปลอดภัยของแอปพลิเคชัน เซิร์ฟเวอร์ หรือฐานข้อมูลไม่รัดกุมเพียงพอ<br>
      • <strong>ตัวอย่าง</strong>: การปล่อยบัญชีและรหัสผ่านเริ่มต้นของระบบไว้ เช่น <code style="color: #00f0ff;">admin:admin</code> หรือการเปิดสิทธิ์การเข้าถึงสารบัญโฟลเดอร์แบบดิบ (Directory Listing Enabled) เช่น พิมพ์เข้าเว็บแล้วเห็นรายการไฟล์ในโฟลเดอร์ทั้งหมด
    </span>
  </div>

  <div style="background: rgba(255,255,255,0.015); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
    <strong style="color: #ff007f; font-size: 1rem; display: block; margin-bottom: 6px;">🔴 A03:2025 - Software Supply Chain Failures (ความล้มเหลวในห่วงโซ่อุปทานซอฟต์แวร์)</strong>
    <span style="color: #cbd5e1; font-size: 0.84rem; line-height: 1.6; display: block;">
      • <strong>คำจำกัดความ</strong>: ความเสี่ยงจากการใช้ไลบรารี สัญญาภายนอก หรือซอร์สโค้ดเฟรมเวิร์กของผู้พัฒนาอื่นมาพัฒนาเว็บแอปพลิเคชัน ซึ่งถูกโจมตีแฝงมัลแวร์<br>
      • <strong>ตัวอย่าง</strong>: การเรียกใช้งาน NPM, Pip หรือ Composer package ที่ถูกแฮกเกอร์แอบอัปเดตเวอร์ชันใหม่ประสงค์ร้ายเพื่อส่งขโมยตัวแปรระบบ (.env) ออกไป
    </span>
  </div>

  <div style="background: rgba(255,255,255,0.015); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
    <strong style="color: #ff007f; font-size: 1rem; display: block; margin-bottom: 6px;">🔴 A04:2025 - Cryptographic Failures (ความล้มเหลวทางวิทยาการเข้ารหัส)</strong>
    <span style="color: #cbd5e1; font-size: 0.84rem; line-height: 1.6; display: block;">
      • <strong>คำจำกัดความ</strong>: ความเสี่ยงที่เกิดจากการใช้กลไกเข้ารหัสที่ไม่รัดกุม หรือความบกพร่องในการปกป้องข้อมูลที่เป็นความลับ<br>
      • <strong>ตัวอย่าง</strong>: การเก็บรหัสผ่านผู้เรียนในฐานข้อมูลเป็นข้อความธรรมดา (Plaintext) แทนที่จะคำนวณแฮช หรือการใช้อัลกอริทึมเข้ารหัสโบราณที่มีลูปชนกันง่าย เช่น MD5, SHA-1
    </span>
  </div>

  <div style="background: rgba(255,255,255,0.015); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
    <strong style="color: #ff007f; font-size: 1rem; display: block; margin-bottom: 6px;">🔴 A05:2025 - Injection (SQLi, XSS, Command Injection)</strong>
    <span style="color: #cbd5e1; font-size: 0.84rem; line-height: 1.6; display: block;">
      • <strong>คำจำกัดความ</strong>: การที่ระบบนำข้อมูลอินพุตจากผู้ใช้ไปรวมเข้าเป็นคำสั่งประมวลผลระบบหลังบ้านโดยไม่มีการคัดกรองอักขระพิเศษออกไปก่อน<br>
      • <strong>ตัวอย่าง</strong>: **SQL Injection** แทรกคำสั่งคิวรีเพื่อดึงข้อมูลทั้งหมดจากฐานข้อมูล, **Cross-Site Scripting (XSS)** ฝังแทรกสคริปต์ JavaScript ประสงค์ร้ายเข้ามาทำงานในบราวเซอร์ผู้ใช้
    </span>
  </div>

  <div style="background: rgba(255,255,255,0.015); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
    <strong style="color: #ff007f; font-size: 1rem; display: block; margin-bottom: 6px;">🔴 A06:2025 - Insecure Design (การออกแบบที่ขาดความปลอดภัย)</strong>
    <span style="color: #cbd5e1; font-size: 0.84rem; line-height: 1.6; display: block;">
      • <strong>คำจำกัดความ</strong>: ช่องโหว่จากการวางโครงสร้างสถาปัตยกรรมและตรรกะระบบตั้งแต่เริ่มออกแบบโดยไม่มีการจำลองภัยคุกคาม (Threat Modeling)<br>
      • <strong>ตัวอย่าง</strong>: ระบบยอมให้แก้ไขรหัสผ่านได้ทันทีโดยไม่ต้องกรอกรหัสผ่านเก่าเพื่อยืนยัน หรือการไม่มีฟังก์ชัน Rate Limiting ป้องกันการเดารหัสผ่านซ้ำๆ
    </span>
  </div>

  <div style="background: rgba(255,255,255,0.015); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
    <strong style="color: #ff007f; font-size: 1rem; display: block; margin-bottom: 6px;">🔴 A07:2025 - Authentication Failures (ความล้มเหลวในการยืนยันตัวตน)</strong>
    <span style="color: #cbd5e1; font-size: 0.84rem; line-height: 1.6; display: block;">
      • <strong>คำจำกัดความ</strong>: ความบกพร่องของระบบตรวจรับและอนุญาตสิทธิ์การล็อกอินเข้าใช้งานระบบ ทำให้แฮกเกอร์เดารหัสผ่านได้ง่าย<br>
      • <strong>ตัวอย่าง</strong>: การปล่อยให้ตั้งรหัสผ่านสั้นและคาดเดาง่าย เช่น <code style="color: #00f0ff;">123456</code> หรือไม่มีระบบ Account Lockout หน่วงเวลาการพยายามเดารหัสผ่าน
    </span>
  </div>

  <div style="background: rgba(255,255,255,0.015); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
    <strong style="color: #ff007f; font-size: 1rem; display: block; margin-bottom: 6px;">🔴 A08:2025 - Software and Data Integrity Failures (ความล้มเหลวของความถูกต้องของซอฟต์แวร์และข้อมูล)</strong>
    <span style="color: #cbd5e1; font-size: 0.84rem; line-height: 1.6; display: block;">
      • <strong>คำจำกัดความ</strong>: ความบกพร่องในการทบทวนความถูกต้องของตัวติดตั้ง การอัปเดตระบบ หรือโครงสร้างข้อมูลแบบ serialize<br>
      • <strong>ตัวอย่าง</strong>: การประมวลผลวัตถุข้อมูลที่มีการ Serialize โดยตรงโดยไม่มีระบบลงลายเซ็นดิจิทัล (Digital Signature) เพื่อรับรองความปลอดภัย
    </span>
  </div>

  <div style="background: rgba(255,255,255,0.015); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
    <strong style="color: #ff007f; font-size: 1rem; display: block; margin-bottom: 6px;">🔴 A09:2025 - Security Logging and Monitoring Failures (ความล้มเหลวในการบันทึกและตรวจสอบประวัติการทำรายการ)</strong>
    <span style="color: #cbd5e1; font-size: 0.84rem; line-height: 1.6; display: block;">
      • <strong>คำจำกัดความ</strong>: การไม่ได้ตั้งค่าจัดทำบันทึกประวัติการใช้สิทธิ์ (Log Files) หรือระบบแจ้งเตือนเมื่อเกิดกรณีการโจมตีแอปพลิเคชัน<br>
      • <strong>ตัวอย่าง</strong>: ระบบถูกสแกนพอร์ตหรือรันสคริปต์ Brute-force หลายพันครั้งแต่ไม่มีการแจ้งเตือนหรือการจดบันทึกประวัติทำให้ไม่สามารถตรวจพบเหตุการณ์ได้ทันท่วงที
    </span>
  </div>

  <div style="background: rgba(255,255,255,0.015); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
    <strong style="color: #ff007f; font-size: 1rem; display: block; margin-bottom: 6px;">🔴 A10:2025 - Mishandling of Exceptional Conditions (การจัดการกับเงื่อนไขยกเว้นอย่างไม่ปลอดภัย)</strong>
    <span style="color: #cbd5e1; font-size: 0.84rem; line-height: 1.6; display: block;">
      • <strong>คำจำกัดความ</strong>: ระบบจัดการกับสถานการณ์เอเรอร์ที่คาดเดาไม่ได้อย่างหละหลวม ส่งผลให้ข้ามขั้นตอนการยืนยันตัวตนหรืออนุญาตสิทธิ์เข้าถึงระบบไปอย่างง่ายดาย
    </span>
  </div>

</div>

---

### 🛠️ เครื่องมือแกะรหัสหน้าเว็บ (Web Page Source Inspections)

การตรวจสอบซอร์สโค้ดหน้าเว็บ (Inspecting a web page) ช่วยให้คุณวิเคราะห์โครงสร้าง (Structure), ค้นหาช่องโหว่ความมั่นคงปลอดภัย (Identify Vulnerabilities) และทำความเข้าใจกลไกการทำงานของเว็บแอปพลิเคชัน ซึ่งเป็นทักษะพื้นฐานและกุญแจสำคัญสำหรับ **Web Exploitation, Debugging และ Web Development**

Most modern web browsers have built-in **Developer Tools (DevTools)** to inspect and analyze web pages:
- **Google Chrome / Microsoft Edge**: กดปุ่ม <kbd style="background: #202430; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); font-family: monospace; font-size: 0.75rem;">F12</kbd> หรือกดคีย์บอร์ดลัด <kbd style="background: #202430; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); font-family: monospace; font-size: 0.75rem;">Ctrl + Shift + I</kbd> เพื่อเรียกใช้ DevTools
- **Mozilla Firefox**: กดปุ่ม <kbd style="background: #202430; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); font-family: monospace; font-size: 0.75rem;">F12</kbd> หรือกดคีย์บอร์ดลัด <kbd style="background: #202430; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); font-family: monospace; font-size: 0.75rem;">Ctrl + Shift + I</kbd>
- **Apple Safari**: เปิดใช้งาน "Show Developer Menu" ใน Settings จากนั้นกดคีย์บอร์ดลัด <kbd style="background: #202430; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); font-family: monospace; font-size: 0.75rem;">Cmd + Option + I</kbd>

#### 1. การดูซอร์สโค้ดหน้าเว็บโดยตรง (View Page Source)
คุณสามารถเรียกดูซอร์สโค้ด (Source Code) ดิบของไฟล์ HTML ได้โดยการคลิกขวาบนพื้นที่ว่างของหน้าเว็บแล้วเลือก **"View page source" (ดูซอร์สโค้ดหน้าเพจ)** หรือใช้คีย์ลัด:
- 💻 สำหรับ Windows: <kbd style="background: #202430; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); font-family: monospace; font-size: 0.75rem;">Ctrl + U</kbd>
- 🍎 สำหรับ Mac: <kbd style="background: #202430; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); font-family: monospace; font-size: 0.75rem;">Command + Option + U</kbd>

#### 2. การดัดแปลงและตรวจสอบ HTML (Modifying HTML)
- **วิธีการใช้งาน**: เปิด DevTools ไปยังแท็บ **Elements** จากนั้นเลื่อนเมาส์ไปชี้ที่โครงสร้างโค้ดหน้าจอในส่วน DOM (Document Object Model) ระบบจะทำการไฮไลต์พื้นที่บนหน้าเว็บจริงให้คุณเห็น หรือคลิกขวาที่จุดใดๆ บนหน้าเพจแล้วเลือก **"Inspect" (ตรวจสอบ)** เพื่อดู HTML ของส่วนนั้นทันที
- **กรณีตัวอย่าง (Use Case)**:
  - ดัดแปลงข้อความหรือรูปภาพสดบนบราวเซอร์ของตนเอง (Client-side)
  - **ตรวจสอบกล่องข้อมูลฟอร์มที่ถูกซ่อนไว้ (Hidden Form Fields)** เช่น ค้นหาแท็ก `<input type="hidden" name="admin_role" value="false">` แล้วลองเปลี่ยนประเภทจาก `hidden` ให้กลายเป็น `text` เพื่อแก้ไขค่าพารามิเตอร์ส่งกลับไปให้เซิร์ฟเวอร์

#### 3. การดัดแปลงและตรวจสอบ CSS (Modifying CSS)
- **วิธีการใช้งาน**: ในแท็บ Elements แผงด้านล่าง/ขวามือจะมีส่วน **Styles** ซึ่งแสดงสไตล์ชีตทั้งหมดของคลาสที่เลือก คุณสามารถเพิ่ม แก้ไข หรือปิดใช้งานกฎ CSS เพื่อดูการเปลี่ยนแปลงแบบสดเรียลไทม์ได้ทันที
- **กรณีตัวอย่าง (Use Case)**:
  - ทดลองปรับสี ปุ่ม หรือฟอนต์เพื่อตรวจสอบการแสดงผล
  - **ค้นหาความบกพร่องของ CSS (Weak CSS Rules)** เช่น การซ่อนส่วนอินเทอร์เฟซลับที่เกี่ยวข้องกับสิทธิ์แอดมินด้วยคลาส CSS ง่ายๆ (เช่น สั่งแค่ `display: none;` หรือ `visibility: hidden;` ในหน้าเว็บสำหรับบุคคลทั่วไปแทนที่จะบล็อกจากหลังบ้าน) ซึ่งแฮกเกอร์สามารถปิดใช้คุณสมบัตินี้ในสไตล์ชีตเพื่อกดเข้าใช้งานได้ทันที

#### 4. การดีบักสคริปต์ JavaScript (Debugging JavaScript)
- **วิธีการใช้งาน**: 
  - ไปยังแท็บ **Sources** เพื่อตรวจสอบไฟล์ JavaScript ทั้งหมดที่ถูกโหลดเข้ามาในหน้านั้น
  - สามารถทำการคลิกที่ตัวเลขบรรทัดเพื่อเพิ่ม **Breakpoint (จุดหยุดชะงัก)** เพื่อให้โค้ดหยุดประมวลผลชั่วคราวขณะรันงาน ทำให้นักพัฒนา/แฮกเกอร์สามารถตรวจสอบค่าตัวแปรภายในหน่วยความจำขณะนั้นได้
  - สามารถประมวลผลสคริปต์สดเพิ่มเติมในแท็บ **Console** เพื่อทดสอบฟังก์ชันในเบราว์เซอร์
- **กรณีตัวอย่าง (Use Case)**:
  - **การข้ามการตรวจสอบข้อมูลฝั่ง Client (Bypass Client-side Validation)** เช่น แก้ไขค่าตัวแปรใน Console หรือสั่งหยุดการตรวจสอบความยาว/รูปแบบอีเมลก่อนกดส่งฟอร์ม
  - ปรับเปลี่ยนกลไกการรับสิทธิ์เข้าใช้งานฝั่งเบราว์เซอร์ (JS-based Auth mechanisms)

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin: 1.5rem auto;">
  <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.25);">
    <strong style="color: #00f0ff; display: block; margin-bottom: 6px; font-size: 0.95rem;">📄 Elements Tab</strong>
    <span style="color: #cbd5e1; font-size: 0.8rem; line-height: 1.5;">วิเคราะห์ DOM แก้ไข HTML และตรวจสอบ Hidden input fields</span>
  </div>
  <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.25);">
    <strong style="color: #00f0ff; display: block; margin-bottom: 6px; font-size: 0.95rem;">💻 Console Tab</strong>
    <span style="color: #cbd5e1; font-size: 0.8rem; line-height: 1.5;">รันคำสั่งสคริปต์สด ดึงค่าคุกกี้ หรือดักจับค่าตัวแปร JavaScript</span>
  </div>
  <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.25);">
    <strong style="color: #00f0ff; display: block; margin-bottom: 6px; font-size: 0.95rem;">💾 Application Tab</strong>
    <span style="color: #cbd5e1; font-size: 0.8rem; line-height: 1.5;">ตรวจสอบ Local Storage, Session Storage และวิเคราะห์/แก้ไข Cookies</span>
  </div>
</div>

---

### 🍪 การสำรวจระบบจัดเก็บคุกกี้เว็บ (Web Cookies Explorations)

**คุกกี้ (HTTP Cookies / Web Cookies)** คือข้อมูลชิ้นเล็กๆ ที่เว็บเซิร์ฟเวอร์สร้างขึ้นและจัดส่งมาเก็บบันทึกไว้ในเครื่องผู้ใช้งาน (Client-side) ผ่านเว็บบราวเซอร์ คุกกี้จะถูกแนบส่งกลับไปหาเซิร์ฟเวอร์ในทุกการเข้าถึงหน้าเว็บของโดเมนนั้นเพื่อยืนยันตัวตนเซสชัน (Session Tracking) และจดจำการตั้งค่าผู้ใช้

สำหรับนักทดสอบเจาะระบบและนักพัฒนา การสืบสวนค่าคุกกี้มีความสำคัญมากเพื่อตรวจสอบความเสี่ยงต่อการโดนขโมยเซสชัน (**Session Hijacking**) หรือช่องโหว่ **Cross-Site Scripting (XSS)**

#### การตรวจสอบและแก้ไขคุกกี้ใน DevTools:
- **วิธีเข้าดู**: เปิด DevTools ➡️ เลือกแท็บ **Application** ➡️ หัวข้อ **Storage** ทางซ้ายมือ ➡️ เลือกคลิกที่ **Cookies** ➡️ เลือกชื่อเว็บปัจจุบัน
- **การปรับเปลี่ยน**: คุณสามารถดับเบิลคลิกเพื่อทำการ **แก้ไขค่า (Edit), เพิ่มค่า (Create) หรือลบค่าคุกกี้ (Delete)** ได้ทันทีผ่านอินเทอร์เฟซนี้

#### คุณลักษณะสำคัญของคุกกี้ (Key Cookie Attributes) ที่ต้องใส่ใจความปลอดภัย:
1. **Name & Value**: ข้อมูลชื่อและค่าคีย์ของคุกกี้ (เช่น `session=abc123xyz`)
2. **Domain & Path**: ขอบเขตขอบข่ายเว็บไซต์ที่มีผลเรียกใช้งานคุกกี้ชิ้นนี้
3. **Expires**: กำหนดวันเวลาหมดอายุการใช้งานของคุกกี้
4. **HttpOnly**: คุณสมบัติความปลอดภัยที่ **ป้องกันไม่ให้ JavaScript (เช่นคำสั่ง XSS) เข้าถึงข้อมูลคุกกี้ชิ้นนี้ได้** ซึ่งจะช่วยบล็อกการขโมยคุกกี้ไปใช้งานต่อ
5. **Secure**: คุณสมบัติที่บังคับให้เบราว์เซอร์ส่งคุกกี้นี้เฉพาะเมื่อเชื่อมต่อผ่านช่องทางเข้ารหัสความปลอดภัย **HTTPS** เท่านั้น
6. **SameSite**: การตั้งค่าสกัดกั้นการโจมตีประเภท **CSRF (Cross-Site Request Forgery)** โดยการจำกัดสิทธิ์การส่งคุกกี้ข้ามโดเมนอื่น

---

### 📂 ช่องโหว่การไต่พาธระบบและข้ามไดเรกทอรี (Path and Directory Traversal)

**ช่องโหว่การไต่ไดเรกทอรี (Path and Directory Traversal)** คือจุดอ่อนความมั่นคงปลอดภัยบนเว็บแอปพลิเคชันที่ยินยอมให้ผู้โจมตีทำการส่งคีย์เวิร์ดรหัสอักขระพิเศษเพื่อควบคุมพาธการเข้าถึงไฟล์ระบบ (File Parameter Manipulation) นอกขอบเขตโฟลเดอร์ราก (Web Root) ไปยังไดเรกทอรีอื่นๆ บนระบบปฏิบัติการของเซิร์ฟเวอร์หลังบ้านได้

<div style="text-align: center; margin: 2rem auto; padding: 15px; background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 12px; max-width: 900px;">
  <img src="/tutorials/static/uploads/path_traversal_custom_diagram_1783910274465.png" alt="Path Traversal Diagram" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);" />
  <span style="color: #cbd5e1; display: block; mt-3; font-size: 0.8rem; line-height: 1.5; text-align: center; margin-top: 10px;">
    <strong>แผนภาพกระบวนการโจมตี Directory Traversal (กราฟิกจำลองการทำงานของเรา):</strong><br>
    1. แฮกเกอร์ส่งเส้นทางไฟล์ที่ตนต้องการข้ามสิทธิ์ขึ้นไปยังเซิร์ฟเวอร์ผ่านพารามิเตอร์อินพุต (เช่น LFI parameter)<br>
    2. เซิร์ฟเวอร์ที่ไม่มีระบบตรวจสอบที่ดี (X) จะยินยอมดึงข้อมูลในระบบไฟล์เครื่องเซิร์ฟเวอร์ตามที่แฮกเกอร์ร้องขอแทนที่จะเรียกเฉพาะไฟล์ของเว็บไซต์ปกติ<br>
    3. เซิร์ฟเวอร์ดึงข้อมูลจากพาร์ติชันส่วนบุคคล (Private Directory/File) ส่งกลับไปแสดงผลหน้าเว็บให้แฮกเกอร์อ่านได้สำเร็จ
  </span>
</div>

#### ไฟล์สำคัญและไฟล์ระบบที่แฮกเกอร์มักมุ่งเป้าโจมตีขโมยข้อมูล:
- **ไฟล์ระบบ (System Files)**:
  - 🐧 สำหรับ Linux: `/etc/passwd` (รายชื่อบัญชีผู้ใช้ระบบ)
  - 💻 สำหรับ Windows: `C:\\Windows\\System32\\config\\SAM` หรือไฟล์ในโฟลเดอร์ระบบอื่นๆ
- **ซอร์สโค้ดของแอปพลิเคชัน (Application Source Code)**: ไฟล์เขียนระบบหลักที่อาจมีอัลกอริทึมที่เป็นความลับ
- **ไฟล์การตั้งค่าระบบ (Configuration Files)**: เช่น ไฟล์เก็บกู้อินเทอร์เฟซคีย์ส่วนตัว `.env` หรือ `config.php`
- **ไฟล์แนะนำบอตเสิร์ชเอนจิน**: เช่น `robots.txt`

---

### 🤖 ไฟล์ Robots.txt กับความมั่นคงปลอดภัย (Path and Directory Traversal: Robots.txt)

ไฟล์ **robots.txt** เป็นไฟล์มาตรฐานสำหรับจัดเก็บบันทึกบนเว็บเซิร์ฟเวอร์ที่ระบุข้อมูลแนะนำตัวสแกนเก็บข้อมูล (Search Engine Crawlers เช่น Googlebot) ว่าไดเรกทอรีหรือหน้าเพจใดของเว็บไซต์ที่ไม่ควรนำไปทำดัชนีผลการค้นหา (Index) ในสาธารณะ

**ข้อควรระวังสำคัญสำหรับความปลอดภัย**:
นักพัฒนาและผู้ดูแลระบบเว็บไซต์จำนวนมากมักเข้าใจผิด โดยการนำไดเรกทอรีหรือโฟลเดอร์เก็บข้อมูลส่วนตัวมาพิมพ์ระบุไว้ใน robots.txt เพื่อป้องกันไม่ให้คนอื่นสืบค้นเจอ ซึ่งการทำเช่นนี้จะเท่ากับเป็นการ **"ชี้เป้า" (Directory exposure)** ให้ผู้โจมตีทราบทันทีว่าควรเดินทางไปเจาะระบบหรือแอบดูไฟล์ในพาธลับพิกัดใดของเว็บไซต์!
"""

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        try:
            blocks = json.loads(l.content)
            blocks[0]['value'] = ultimate_content
            l.content = json.dumps(blocks, ensure_ascii=False)
            app.db.session.commit()
            print("Successfully updated Lesson 177 Block 0 with ultimate merged slides content!")
        except Exception as e:
            print(f"Error: {e}")
