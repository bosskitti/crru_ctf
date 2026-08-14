import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

dom_explanation_html = """

#### 💡 ความรู้พื้นฐาน: DOM (Document Object Model) คืออะไร?

เมื่อเบราว์เซอร์ดาวน์โหลดไฟล์ซอร์สโค้ด HTML จากเซิร์ฟเวอร์ มันจะนำโค้ดบรรทัดคำสั่งข้อความดิบเหล่านั้นมาจัดโครงสร้างใหม่ในหน่วยความจำ (RAM) ให้กลายเป็นวัตถุรูปต้นไม้ที่เรียกว่า **DOM (Document Object Model)** เพื่อให้โปรแกรมคอมพิวเตอร์ (เช่น JavaScript) สามารถเข้าไปอ่าน ดึงข้อมูล หรือดัดแปลงแก้ไขหน้าเว็บได้แบบสดเรียลไทม์

<div style="background:#070a13;border:1px solid rgba(0,240,255,0.15);border-radius:12px;padding:20px;margin:1.5rem auto;max-width:850px;box-shadow:0 8px 32px rgba(0,0,0,0.4);font-family:'Inter',sans-serif;">
<div style="font-size:0.82rem;color:#00f0ff;font-weight:bold;margin-bottom:12px;text-transform:uppercase;letter-spacing:0.08em;text-align:left;"><i class="fas fa-sitemap mr-1"></i> โครงสร้างต้นไม้ของ DOM (DOM Tree Structure)</div>
<div style="background:#03050a;border-radius:6px;padding:16px;text-align:left;font-family:'JetBrains Mono',monospace;font-size:0.75rem;line-height:1.5;color:#cbd5e1;border:1px solid rgba(255,255,255,0.03);overflow-x:auto;">
Document (หน้าเพจทั้งหมด)<br>
└── &lt;html&gt; (Root Element)<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── &lt;head&gt; (ส่วนหัวข้อมูลเว็บ)<br>
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└── &lt;title&gt; (ชื่อหัวข้อเว็บ)<br>
&nbsp;&nbsp;&nbsp;&nbsp;└── &lt;body&gt; (ส่วนแสดงเนื้อหาเว็บ)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── &lt;h1&gt; (หัวข้อเรื่องหลัก)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── &lt;p&gt; (ย่อหน้าข้อความ)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── &lt;form&gt; (กล่องรับข้อมูล)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── &lt;input&gt; (กล่องพารามิเตอร์ลับ)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── &lt;button&gt; (ปุ่มกดยืนยันชำระเงิน)<br>
</div>
</div>

##### 🔄 ความแตกต่างระหว่าง HTML (Source Code) และ DOM:
- **HTML (Source Code)**: คือไฟล์ข้อความดิบ (Static text) ที่ถูกส่งมาจากเว็บเซิร์ฟเวอร์แบบดั้งเดิม **ไม่สามารถเปลี่ยนแปลงได้** หลังจากที่ดาวน์โหลดลงมาแล้ว (ถ้าแฮกเกอร์ใช้คำสั่ง View Source ก็จะเห็นโค้ดชุดนี้เสมอ)
- **DOM (Document Object Model)**: คือโครงสร้างต้นไม้ที่ทำงานอยู่บนหน้าจอบราวเซอร์จริง (Dynamic structure) **สามารถเปลี่ยนแปลงสไตล์และค่าได้ตลอดเวลา** ผ่านการเขียนสคริปต์ JavaScript หรือการดัดแปลงในแท็บ Elements ของ DevTools

> [!IMPORTANT]
> **ทำไมแฮกเกอร์ถึงเน้นแก้ไขโครงสร้าง DOM?**:
> เพราะความปลอดภัยของเว็บแอปพลิเคชันบางตัว ดำเนินการตรวจสอบเงื่อนไขความถูกต้องแค่ฝั่งเบราเซอร์ (Client-side validation) เช่น สั่งล็อกปุ่มชำระเงินไม่ให้กดหากค่าราคาต่ำเกินไป แฮกเกอร์สามารถเปิด F12 ไปที่แท็บ **Elements** เพื่อเข้าไปดัดแปลงแก้ไขกิ่งก้านวัตถุของ DOM สั่งเปิดสิทธิ์ (Enable button) หรือแก้ตัวแปรลับ แล้วกดยิงส่งข้อมูลประมวลผลกลับไปที่เซิร์ฟเวอร์ได้ทันที

"""

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        try:
            blocks = json.loads(l.content)
            val = blocks[0]["value"]
            
            # Find the end of the DevTools mockup section
            # The mockup section ends right before "### 🍪 การสำรวจระบบจัดเก็บคุกกี้เว็บ (Web Cookies Explorations)"
            target_cookies = "### 🍪 การสำรวจระบบจัดเก็บคุกกี้เว็บ (Web Cookies Explorations)"
            idx = val.find(target_cookies)
            
            if idx != -1:
                # Insert right before the cookies section
                new_val = val[:idx] + dom_explanation_html + "\n\n" + val[idx:]
                blocks[0]["value"] = new_val
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print("Successfully inserted DOM explanation section!")
            else:
                print("Error: Could not find transition header to insert DOM explanation.")
        except Exception as e:
            print(f"Error: {e}")
