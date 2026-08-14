import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

new_table_html = """#### 📊 ตารางเปรียบเทียบเครื่องมือสแกนพาธ (Path Scanning Tools Comparison Table)

<div style="overflow-x:auto;margin:2rem auto;max-width:1100px;border:1px solid rgba(0,240,255,0.25);border-radius:12px;background:#05070f;box-shadow:0 10px 30px rgba(0,0,0,0.65);">
<table style="width:100%;border-collapse:collapse;text-align:left;font-family:sans-serif;font-size:0.83rem;color:#cbd5e1;">
<thead>
<tr style="background:rgba(0,240,255,0.08);border-bottom:1px solid rgba(0,240,255,0.2);">
<th style="padding:14px 12px;font-weight:bold;color:#00f0ff;width:16%;">คุณลักษณะ (Features)</th>
<th style="padding:14px 12px;font-weight:bold;color:#ffffff;width:21%;">DIRB / DirBuster</th>
<th style="padding:14px 12px;font-weight:bold;color:#fbbf24;width:21%;">FFUF (Fast Web Fuzzer)</th>
<th style="padding:14px 12px;font-weight:bold;color:#3ddc84;width:21%;">Gobuster</th>
<th style="padding:14px 12px;font-weight:bold;color:#ff007f;width:21%;">Burp Suite (Intruder)</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:14px 12px;color:#ffffff;font-weight:bold;">1. อินเตอร์เฟส (UI)</td>
<td style="padding:14px 12px;">CLI (DIRB) / GUI (DirBuster)</td>
<td style="padding:14px 12px;">CLI (Command Line Only)</td>
<td style="padding:14px 12px;">CLI (Command Line Only)</td>
<td style="padding:14px 12px;color:#ff007f;font-weight:bold;">GUI (ตัวโปรแกรมดักจับและส่งซ้ำ)</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:14px 12px;color:#ffffff;font-weight:bold;">2. ภาษาที่ใช้พัฒนา</td>
<td style="padding:14px 12px;"><span style="background:rgba(239,68,68,0.1);color:#ef4444;padding:2px 6px;border-radius:4px;font-size:0.75rem;border:1px solid rgba(239,68,68,0.2);">C / Java</span></td>
<td style="padding:14px 12px;"><span style="background:rgba(59,130,246,0.1);color:#60a5fa;padding:2px 6px;border-radius:4px;font-size:0.75rem;border:1px solid rgba(59,130,246,0.2);">Go (Golang)</span></td>
<td style="padding:14px 12px;"><span style="background:rgba(59,130,246,0.1);color:#60a5fa;padding:2px 6px;border-radius:4px;font-size:0.75rem;border:1px solid rgba(59,130,246,0.2);">Go (Golang)</span></td>
<td style="padding:14px 12px;"><span style="background:rgba(239,68,68,0.1);color:#ef4444;padding:2px 6px;border-radius:4px;font-size:0.75rem;border:1px solid rgba(239,68,68,0.2);">Java</span></td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:14px 12px;color:#ffffff;font-weight:bold;">3. ความเร็วการทำงาน</td>
<td style="padding:14px 12px;color:#ef4444;">ช้า - ปานกลาง (ตามเกณฑ์ Thread)</td>
<td style="padding:14px 12px;color:#3ddc84;font-weight:bold;">เร็วมากเป็นพิเศษ (High-Speed)</td>
<td style="padding:14px 12px;color:#3ddc84;font-weight:bold;">เร็วมาก (High-Speed)</td>
<td style="padding:14px 12px;color:#ef4444;">ช้า (เนื่องจากเน้นจำลอง Proxy และมีข้อจำกัดในรุ่น Free)</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:14px 12px;color:#ffffff;font-weight:bold;">4. การทำงานแบบลึก (Recursion)</td>
<td style="padding:14px 12px;color:#3ddc84;">รองรับโดยอัตโนมัติ (Default)</td>
<td style="padding:14px 12px;">รองรับ (ต้องเปิดตัวเลือกเสริม)</td>
<td style="padding:14px 12px;color:#ef4444;">ไม่รองรับ (เน้นการสแกนแนวราบเร็ว)</td>
<td style="padding:14px 12px;color:#ef4444;">ไม่รองรับ (ผู้ตรวจสอบต้องกำหนดเป้าหมายตรงจุด)</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:14px 12px;color:#ffffff;font-weight:bold;">5. ฟังก์ชัน Fuzzing อื่นๆ</td>
<td style="padding:14px 12px;color:#94a3b8;">ไม่รองรับ (ทำได้เฉพาะหาไฟล์/พาธ)</td>
<td style="padding:14px 12px;color:#34d399;">ครบเครื่อง (Headers, POST parameters, etc.)</td>
<td style="padding:14px 12px;color:#94a3b8;">รองรับ DNS Subdomain และ Vhost scan</td>
<td style="padding:14px 12px;color:#34d399;font-weight:bold;">สูงสุดยอดเยี่ยม (แก้ไข ปรับรูปแบบ และยิง Payload ได้ทุกตำแหน่งหัวข้อมูล)</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:14px 12px;color:#ffffff;font-weight:bold;">6. จุดประสงค์หลักที่เหมาะใช้</td>
<td style="padding:14px 12px;">มือใหม่ศึกษา หรือสแกนหาพาธลึกแบบออโต้</td>
<td style="padding:14px 12px;">ทำ Fuzzing พารามิเตอร์ลับ หรือสแกนหาพาธความเร็วสูงมาก</td>
<td style="padding:14px 12px;">กวาดหา Subdomains ของเซิร์ฟเวอร์ หรือทำสแกนไฟล์ด่วน</td>
<td style="padding:14px 12px;color:#cbd5e1;">การทดสอบเจาะระบบเฉพาะจุดอย่างละเอียด (เช่น ป้อนค่าทดสอบบิดเบือนพารามิเตอร์ หรือ Brute Force รหัสผ่าน)</td>
</tr>
</tbody>
</table>
</div>"""

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        try:
            blocks = json.loads(l.content)
            val = blocks[0]["value"]
            
            # Find the old table block to replace
            start_marker = "#### 📊 ตารางเปรียบเทียบเครื่องมือสแกนพาธ (Path Scanning Tools Comparison Table)"
            # The table ends at "</div>"
            start_idx = val.find(start_marker)
            
            # Find the first closing </div> after the start_marker
            end_idx = val.find("</div>", start_idx) + 6 if start_idx != -1 else -1
            
            if start_idx != -1 and end_idx != -1:
                # Replace with the new 5-column version
                new_val = val[:start_idx] + new_table_html + val[end_idx:]
                blocks[0]["value"] = new_val
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print("Successfully updated comparison table to include Burp Suite (Intruder) column!")
            else:
                print(f"Error: Markers not found. Start: {start_idx}, End: {end_idx}")
        except Exception as e:
            print(f"Error: {e}")
