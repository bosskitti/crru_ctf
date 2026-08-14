import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

http_understanding_html = """### 🌐 ความเข้าใจเกี่ยวกับข้อความสื่อสาร HTTP (HTTP Message Understanding)

ข้อความ **HTTP Messages** คือบล็อกโครงสร้างพื้นฐานในการรับส่งข้อมูลระหว่างไคลเอนต์ (เช่น Web Browser) และเว็บเซิร์ฟเวอร์ (Web Server) โดยแบ่งออกเป็น 2 ประเภทหลักคือ:
- **HTTP Request**: ข้อความที่ส่งจากฝั่งเบราเซอร์ (Client) ไปหาเซิร์ฟเวอร์เพื่อร้องขอข้อมูลหรือส่งค่าประมวลผล
- **HTTP Response**: ข้อความที่เซิร์ฟเวอร์ตอบรับและส่งไฟล์ข้อมูล (เช่น HTML, JSON, รูปภาพ) กลับมาแสดงผล

<div style="background:#070a13;border:1px solid rgba(0,240,255,0.15);border-radius:12px;padding:24px;text-align:center;margin:2rem auto;max-width:850px;box-shadow:0 8px 32px rgba(0,0,0,0.4);">
<div style="font-size:0.85rem;color:#00f0ff;font-weight:bold;margin-bottom:16px;text-transform:uppercase;letter-spacing:0.08em;text-shadow:0 0 8px rgba(0,240,255,0.4);"><i class="fas fa-exchange-alt mr-2"></i> แผนภาพการรับส่งข้อความ HTTP Request / Response</div>
<svg viewBox="0 0 700 200" style="width:100%;height:auto;display:block;margin:0 auto;background:#03050a;border-radius:8px;">
<defs>
<linearGradient id="blue-grad" x1="0%" y1="0%" x2="100%" y2="0%">
<stop offset="0%" stop-color="#00f0ff" />
<stop offset="100%" stop-color="#3b82f6" />
</linearGradient>
<linearGradient id="green-grad" x1="0%" y1="0%" x2="100%" y2="0%">
<stop offset="0%" stop-color="#3ddc84" />
<stop offset="100%" stop-color="#10b981" />
</linearGradient>
<filter id="glow-b" x="-20%" y="-20%" width="140%" height="140%">
<feGaussianBlur stdDeviation="3" result="blur" />
<feComposite in="SourceGraphic" in2="blur" operator="over" />
</filter>
</defs>
<g transform="translate(30, 45)">
<rect x="0" y="0" width="130" height="110" rx="8" fill="#0f1322" stroke="#3b82f6" stroke-width="1.5" filter="url(#glow-b)"/>
<text x="65" y="45" fill="#ffffff" font-size="10" font-family="sans-serif" font-weight="bold" text-anchor="middle">Browser Client</text>
<rect x="15" y="65" width="100" height="28" rx="4" fill="#1e293b" stroke="#3b82f6" stroke-width="1"/>
<text x="65" y="82" fill="#00f0ff" font-size="9" font-family="sans-serif" text-anchor="middle">User Interface</text>
</g>
<path d="M175,75 L455,75" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,2"/>
<polygon points="455,75 447,71 447,79" fill="#ef4444"/>
<text x="315" y="65" fill="#ef4444" font-size="9.5" font-family="monospace" text-anchor="middle" font-weight="bold">HTTP Request</text>
<path d="M455,120 L175,120" fill="none" stroke="#3ddc84" stroke-width="2" filter="url(#glow-b)"/>
<polygon points="175,120 183,116 183,124" fill="#3ddc84"/>
<text x="315" y="140" fill="#3ddc84" font-size="9.5" font-family="monospace" text-anchor="middle" font-weight="bold">HTTP Response</text>
<g transform="translate(470, 45)">
<rect x="0" y="0" width="200" height="110" rx="8" fill="#0f1322" stroke="#00f0ff" stroke-width="1.5" filter="url(#glow-b)"/>
<text x="100" y="30" fill="#00f0ff" font-size="10" font-family="sans-serif" font-weight="bold" text-anchor="middle">Server-side Systems</text>
<rect x="15" y="50" width="80" height="45" rx="4" fill="#1e293b" stroke="#3b82f6" stroke-width="1"/>
<text x="55" y="70" fill="#ffffff" font-size="8.5" font-family="sans-serif" text-anchor="middle">Web Server</text>
<rect x="105" y="50" width="80" height="45" rx="4" fill="#1e293b" stroke="#eab308" stroke-width="1"/>
<text x="145" y="70" fill="#ffffff" font-size="8.5" font-family="sans-serif" text-anchor="middle">Data-store</text>
</g>
</svg>
</div>

---

### 🔎 โครงสร้างกายวิภาคของข้อความ HTTP Request & Response (HTTP Message Anatomy)

ข้อความ HTTP มีการจัดเรียงรูปแบบโครงสร้างที่เป็นแบบแผนเดียวกัน ทั้งฝั่งที่ส่งออกไป (Request) และฝั่งที่รับกลับมา (Response) โดยแบ่งโครงสร้างหลักออกเป็น 4 ส่วน:

<div style="display:flex;flex-direction:column;gap:16px;margin:2rem auto;max-width:950px;font-family:'JetBrains Mono',monospace;font-size:0.83rem;">
<div style="display:flex;gap:12px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.05);border-radius:10px;padding:16px;align-items:stretch;">
<div style="flex:1;background:#05070f;border:1px solid rgba(0,240,255,0.2);border-radius:6px;padding:12px;text-align:left;">
<span style="color:#64748b;font-size:0.72rem;display:block;margin-bottom:6px;"># HTTP Request Structure</span>
<span style="background:rgba(59,130,246,0.15);color:#00f0ff;padding:2px 6px;border-radius:4px;display:inline-block;margin-bottom:6px;">POST /login HTTP/1.1</span><br>
Host: www.example.com<br>
Content-Type: application/json<br>
Content-Length: 32<br>
<br>
{"username":"admin"}
</div>
<div style="width:120px;display:flex;flex-direction:column;justify-content:space-between;text-align:center;color:#eab308;font-size:0.75rem;font-weight:bold;padding:12px 0;">
<div>Start Line ──</div>
<div>Headers ──</div>
<div>Empty Line ──</div>
<div>Body (Data) ──</div>
</div>
<div style="flex:1;background:#05070f;border:1px solid rgba(61,220,132,0.2);border-radius:6px;padding:12px;text-align:left;">
<span style="color:#64748b;font-size:0.72rem;display:block;margin-bottom:6px;"># HTTP Response Structure</span>
<span style="background:rgba(16,185,129,0.15);color:#3ddc84;padding:2px 6px;border-radius:4px;display:inline-block;margin-bottom:6px;">HTTP/1.1 200 OK</span><br>
Server: Apache/2.4.41<br>
Content-Type: text/html<br>
Content-Length: 1024<br>
<br>
&lt;html&gt;Hello World&lt;/html&gt;
</div>
</div>
</div>

#### โครงสร้างองค์ประกอบสำคัญ (Component Breakdowns):

1. **Start Line / Status Line**:
   - **Request (Start Line)**: ระบุ **Method** การส่ง (เช่น `GET`, `POST`), **Path URL** (ตำแหน่งทรัพยากร) และ **Protocol** ชนิดรุ่นเวอร์ชัน (เช่น `HTTP/1.1` หรือ `HTTP/2`)
   - **Response (Status Line)**: แสดงข้อมูลรุ่นของ HTTP และ **รหัสสถานะตอบรับ (Status Code)** เช่น `200 OK`
2. **Headers**: แหล่งรวบรวมข้อมูลรายละเอียดเมตาดาต้า (Metadata) ต่างๆ ของคำขอ/การตอบรับ เช่น `Host`, `User-Agent` (ระบุชนิดเบราว์เซอร์), `Content-Type` (รูปแบบข้อมูล) หรือ `Cookie` (ข้อมูลเซสชัน)
3. **Empty Line**: บรรทัดว่างเปล่าที่ไม่มีตัวอักษรใดๆ ซึ่งเว็บเซิร์ฟเวอร์จะใช้ตรวจเช็คเพื่อแบ่งแยกส่วนหัว (Headers) ออกจากตัวเนื้อหาหลัก (Body)
4. **Body (เนื้อหาข้อมูล)**: ส่วนเก็บข้อมูลจริงสำหรับการส่งหรือรับ (Optional) เช่น รหัสผ่าน หรือโครงสร้างหน้าเว็บเพจ HTML/JSON

---

### 📦 ตารางสรุป HTTP Methods & HTTP Headers ยอดนิยม

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(380px,1fr));gap:20px;margin:2rem auto;max-width:1000px;">
<div style="overflow-x:auto;border:1px solid rgba(6,182,212,0.25);border-radius:12px;background:#05070f;">
<table style="width:100%;border-collapse:collapse;text-align:left;font-family:sans-serif;font-size:0.82rem;color:#cbd5e1;">
<thead>
<tr style="background:rgba(6,182,212,0.08);border-bottom:1px solid rgba(6,182,212,0.2);">
<th style="padding:10px 14px;font-weight:bold;color:#00f0ff;width:25%;">HTTP Method</th>
<th style="padding:10px 14px;font-weight:bold;color:#ffffff;width:75%;">วัตถุประสงค์หลัก (Purpose)</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:10px 14px;color:#ffffff;font-weight:bold;"><code style="color:#00f0ff;">GET</code></td>
<td style="padding:10px 14px;">เรียกคืน/ขอรับข้อมูลหลักจากเซิร์ฟเวอร์ (ห้ามใช้ส่งข้อมูลความลับ)</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:10px 14px;color:#ffffff;font-weight:bold;"><code style="color:#fbbf24;">POST</code></td>
<td style="padding:10px 14px;">จัดส่งค่าข้อมูลหรืออัปโหลดไฟล์ไปที่หลังบ้านเพื่อรันประมวลผล</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:10px 14px;color:#ffffff;font-weight:bold;"><code style="color:#a855f7;">PUT</code></td>
<td style="padding:10px 14px;">เขียนทับ/อัปเดตไฟล์ทรัพยากรบนเครื่องเซิร์ฟเวอร์ทั้งหมด</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:10px 14px;color:#ffffff;font-weight:bold;"><code style="color:#ef4444;">DELETE</code></td>
<td style="padding:10px 14px;">ลบไฟล์หรือข้อมูลทรัพยากรออกจากที่จัดเก็บ</td>
</tr>
</tbody>
</table>
</div>
<div style="overflow-x:auto;border:1px solid rgba(168,85,247,0.25);border-radius:12px;background:#05070f;">
<table style="width:100%;border-collapse:collapse;text-align:left;font-family:sans-serif;font-size:0.82rem;color:#cbd5e1;">
<thead>
<tr style="background:rgba(168,85,247,0.08);border-bottom:1px solid rgba(168,85,247,0.2);">
<th style="padding:10px 14px;font-weight:bold;color:#a855f7;width:30%;">HTTP Header</th>
<th style="padding:10px 14px;font-weight:bold;color:#ffffff;width:70%;">ความหมายและการใช้งาน (Description)</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:10px 14px;color:#ffffff;font-weight:bold;"><code style="color:#a855f7;">User-Agent</code></td>
<td style="padding:10px 14px;">ข้อมูลระบุชื่อรุ่นเบราว์เซอร์หรือเครื่องไคลเอนต์ที่เรียกเข้ามา</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:10px 14px;color:#ffffff;font-weight:bold;"><code style="color:#a855f7;">Referer</code></td>
<td style="padding:10px 14px;">ระบุ URL หน้าเว็บก่อนหน้าที่ผู้ใช้กดลิงก์เดินทางผ่านมา</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:10px 14px;color:#ffffff;font-weight:bold;"><code style="color:#a855f7;">Cookie</code></td>
<td style="padding:10px 14px;">คีย์ข้อมูลบันทึกเซสชันหรือสถานะล็อกอินของผู้เรียนปลายทาง</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:10px 14px;color:#ffffff;font-weight:bold;"><code style="color:#a855f7;">X-Frame-Options</code></td>
<td style="padding:10px 14px;">ส่วนหัวป้องกันภัยความปลอดภัยเพื่อสกัดกันการโดนฝัง Clickjacking</td>
</tr>
</tbody>
</table>
</div>
</div>

> [!NOTE]
> **การวิเคราะห์รายละเอียด HTTP Status Codes**:
> สำหรับรายละเอียดและความหมายของแต่ละ **รหัสสถานะตอบรับ HTTP (HTTP Status Codes เช่น 200, 301, 403, 404, 500)** ทางหลักสูตรได้มีการจัดทำแบบจำลองพร้อมตารางสรุปคำอธิบายไว้อย่างครบถ้วนแล้ว แอดมินและผู้เรียนสามารถคลิกข้ามไปศึกษาและทบทวนรายละเอียดได้ที่นี่ทันทีครับ: [🔗 ตารางคำอธิบาย HTTP Status Codes จากผลการทดสอบเจาะระบบเครื่องมือ DIRB](#💡-การทำความเข้าใจ-http-status-codes-จากผลลัพธ์ของ-dirb)

"""

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        try:
            blocks = json.loads(l.content)
            val = blocks[0]["value"]
            
            # We want to place this HTTP Message Understanding section right at the beginning of the lesson
            # Just after the main slide headers, which end around the F12 inspections or before OWASP Top 10
            # Wait, let's find the header for F12 tool inspections:
            target_inspections = "### 🛠️ เครื่องมือแกะรหัสหน้าเว็บ (Web Page Source Inspections)"
            idx = val.find(target_inspections)
            
            if idx != -1:
                # Insert right before the inspections header
                new_val = val[:idx] + http_understanding_html + "\n\n" + val[idx:]
                blocks[0]["value"] = new_val
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print("Successfully inserted the premium HTTP Message Understanding section!")
            else:
                # If target is not found, prepend to the value
                new_val = http_understanding_html + "\n\n" + val
                blocks[0]["value"] = new_val
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print("Prepended HTTP Message Understanding section successfully!")
        except Exception as e:
            print(f"Error: {e}")
