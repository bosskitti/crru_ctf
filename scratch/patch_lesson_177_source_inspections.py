import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

new_html_section = """### 🛠️ เครื่องมือแกะรหัสหน้าเว็บ (Web Page Source Inspections)

การตรวจสอบซอร์สโค้ดหน้าเว็บ (Inspecting a web page) ช่วยให้คุณวิเคราะห์โครงสร้าง (Structure), ค้นหาช่องโหว่ความมั่นคงปลอดภัย (Identify Vulnerabilities) และทำความเข้าใจกลไกการทำงานของเว็บแอปพลิเคชัน ซึ่งเป็นทักษะพื้นฐานและกุญแจสำคัญสำหรับ **Web Exploitation, Debugging และ Web Development**

Most modern web browsers have built-in **Developer Tools (DevTools)** to inspect and analyze web pages:

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 1.5rem auto;">
  <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.25);">
    <strong style="color: #00f0ff; display: block; margin-bottom: 8px; font-size: 0.95rem;"><i class="fab fa-chrome text-info mr-2"></i> Google Chrome / Microsoft Edge</strong>
    <span style="color: #cbd5e1; font-size: 0.82rem; line-height: 1.5; display: block; mb-2;">กดปุ่ม <kbd style="background: #202430; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); font-family: monospace; font-size: 0.75rem;">F12</kbd> หรือกดคีย์บอร์ดลัด <kbd style="background: #202430; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); font-family: monospace; font-size: 0.75rem;">Ctrl + Shift + I</kbd> เพื่อเรียกใช้ DevTools</span>
  </div>
  <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.25);">
    <strong style="color: #ff9f43; display: block; margin-bottom: 8px; font-size: 0.95rem;"><i class="fab fa-firefox-browser text-warning mr-2"></i> Mozilla Firefox</strong>
    <span style="color: #cbd5e1; font-size: 0.82rem; line-height: 1.5; display: block; mb-2;">กดปุ่ม <kbd style="background: #202430; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); font-family: monospace; font-size: 0.75rem;">F12</kbd> หรือกดคีย์บอร์ดลัด <kbd style="background: #202430; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); font-family: monospace; font-size: 0.75rem;">Ctrl + Shift + I</kbd></span>
  </div>
  <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.25);">
    <strong style="color: #a29bfe; display: block; margin-bottom: 8px; font-size: 0.95rem;"><i class="fab fa-safari text-primary mr-2"></i> Apple Safari</strong>
    <span style="color: #cbd5e1; font-size: 0.82rem; line-height: 1.5; display: block; mb-2;">เปิดใช้งาน "Show Developer Menu" ใน Settings จากนั้นกดคีย์บอร์ดลัด <kbd style="background: #202430; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); font-family: monospace; font-size: 0.75rem;">Cmd + Option + I</kbd></span>
  </div>
</div>

<div style="background: rgba(16,185,129,0.04); border: 1px solid rgba(16,185,129,0.2); border-radius: 12px; padding: 20px; margin: 1.5rem auto; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
  <h4 style="margin: 0 0 10px 0; font-size: 1rem; color: #3ddc84; font-weight: bold;"><i class="fas fa-code mr-2"></i> การดูซอร์สโค้ดหน้าเว็บโดยตรง (View Page Source)</h4>
  <p style="margin: 0; font-size: 0.84rem; color: #cbd5e1; line-height: 1.6;">
    คุณสามารถเรียกดูซอร์สโค้ด (Source Code) ดิบของไฟล์ HTML ได้โดยการคลิกขวาบนพื้นที่ว่างของหน้าเว็บแล้วเลือก <strong>"View page source" (ดูซอร์สโค้ดหน้าเพจ)</strong> หรือใช้คีย์ลัด:<br>
    - 💻 สำหรับ Windows: <kbd style="background: #202430; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); font-family: monospace; font-size: 0.75rem;">Ctrl + U</kbd><br>
    - 🍎 สำหรับ Mac: <kbd style="background: #202430; padding: 2px 6px; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2); font-family: monospace; font-size: 0.75rem;">Command + Option + U</kbd>
  </p>
</div>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin: 1.5rem auto;">
  <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.25);">
    <strong style="color: #00f0ff; display: block; margin-bottom: 6px; font-size: 0.95rem;">📄 Elements</strong>
    <span style="color: #cbd5e1; font-size: 0.8rem; line-height: 1.5;">ตรวจสอบโครงสร้าง HTML เพื่อดัดแปลงพารามิเตอร์ลับที่นักพัฒนาซ่อนไว้ เช่น ปุ่มแก้ไขราคา หรือปุ่มสิทธิ์</span>
  </div>
  <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.25);">
    <strong style="color: #00f0ff; display: block; margin-bottom: 6px; font-size: 0.95rem;">💻 Console</strong>
    <span style="color: #cbd5e1; font-size: 0.8rem; line-height: 1.5;">หน้ารันคำสั่งสคริปต์สด ช่วยทดสอบคำสั่งการทำงานหรือพิมพ์ข้อความดักจับตัวแปรเซสชันปัจจุบัน</span>
  </div>
  <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.25);">
    <strong style="color: #00f0ff; display: block; margin-bottom: 6px; font-size: 0.95rem;">💾 Application</strong>
    <span style="color: #cbd5e1; font-size: 0.8rem; line-height: 1.5;">ใช้ตรวจสอบและดึงรายละเอียดที่เครื่อง Client เก็บสะสมไว้ เช่น คุกกี้เซสชัน บันทึก local storage</span>
  </div>
</div>"""

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        try:
            blocks = json.loads(l.content)
            val = blocks[0].get('value', '')
            
            target_start = val.find('### 🛠️ เครื่องมือแกะรหัสหน้าเว็บ (Web Page Source Inspections)')
            # find next header --- or 🍪 วิเคราะห์คุณลักษณะ
            target_end = val.find('---', target_start + 50)
            
            if target_start != -1 and target_end != -1:
                # Replace the old section
                new_val = val[:target_start] + new_html_section + '\n\n' + val[target_end:]
                blocks[0]['value'] = new_val
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print("Successfully updated Web Page Source Inspections section in Lesson 177!")
            else:
                print("Error: Could not find target tags in block value.")
        except Exception as e:
            print(f"Error: {e}")
