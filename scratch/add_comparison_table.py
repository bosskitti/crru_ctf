import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

comparison_table_html = """

#### 📊 ตารางเปรียบเทียบเครื่องมือสแกนพาธ (Path Scanning Tools Comparison Table)

<div style="overflow-x:auto;margin:2rem auto;max-width:1000px;border:1px solid rgba(0,240,255,0.25);border-radius:12px;background:#05070f;box-shadow:0 10px 30px rgba(0,0,0,0.65);">
<table style="width:100%;border-collapse:collapse;text-align:left;font-family:sans-serif;font-size:0.85rem;color:#cbd5e1;">
<thead>
<tr style="background:rgba(0,240,255,0.08);border-bottom:1px solid rgba(0,240,255,0.2);">
<th style="padding:14px 16px;font-weight:bold;color:#00f0ff;width:20%;">คุณลักษณะ (Features)</th>
<th style="padding:14px 16px;font-weight:bold;color:#ffffff;width:25%;">DIRB / DirBuster</th>
<th style="padding:14px 16px;font-weight:bold;color:#fbbf24;width:25%;">FFUF (Fast Web Fuzzer)</th>
<th style="padding:14px 16px;font-weight:bold;color:#3ddc84;width:25%;">Gobuster</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:14px 16px;color:#ffffff;font-weight:bold;">1. อินเตอร์เฟส (UI)</td>
<td style="padding:14px 16px;">CLI (DIRB) / GUI (DirBuster)</td>
<td style="padding:14px 16px;">CLI (Command Line Only)</td>
<td style="padding:14px 16px;">CLI (Command Line Only)</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:14px 16px;color:#ffffff;font-weight:bold;">2. ภาษาที่ใช้พัฒนา</td>
<td style="padding:14px 16px;"><span style="background:rgba(239,68,68,0.1);color:#ef4444;padding:2px 6px;border-radius:4px;font-size:0.75rem;border:1px solid rgba(239,68,68,0.2);">C / Java</span></td>
<td style="padding:14px 16px;"><span style="background:rgba(59,130,246,0.1);color:#60a5fa;padding:2px 6px;border-radius:4px;font-size:0.75rem;border:1px solid rgba(59,130,246,0.2);">Go (Golang)</span></td>
<td style="padding:14px 16px;"><span style="background:rgba(59,130,246,0.1);color:#60a5fa;padding:2px 6px;border-radius:4px;font-size:0.75rem;border:1px solid rgba(59,130,246,0.2);">Go (Golang)</span></td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:14px 16px;color:#ffffff;font-weight:bold;">3. ความเร็วการทำงาน</td>
<td style="padding:14px 16px;color:#ef4444;">ช้า - ปานกลาง (ตามเกณฑ์ Thread)</td>
<td style="padding:14px 16px;color:#3ddc84;font-weight:bold;">เร็วมากเป็นพิเศษ (High-Speed)</td>
<td style="padding:14px 16px;color:#3ddc84;font-weight:bold;">เร็วมาก (High-Speed)</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:14px 16px;color:#ffffff;font-weight:bold;">4. การทำงานแบบลึก (Recursion)</td>
<td style="padding:14px 16px;color:#3ddc84;">รองรับโดยอัตโนมัติ (Default)</td>
<td style="padding:14px 16px;">รองรับ (ต้องเปิดตัวเลือกเสริม)</td>
<td style="padding:14px 16px;color:#ef4444;">ไม่รองรับ (เน้นการสแกนแนวราบเร็ว)</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:14px 16px;color:#ffffff;font-weight:bold;">5. ฟังก์ชัน Fuzzing อื่นๆ</td>
<td style="padding:14px 16px;color:#94a3b8;">ไม่รองรับ (ทำได้เฉพาะหาไฟล์/พาธ)</td>
<td style="padding:14px 16px;color:#34d399;">ครบเครื่อง (Headers, POST parameters, etc.)</td>
<td style="padding:14px 16px;color:#94a3b8;">รองรับ DNS Subdomain และ Vhost scan</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:14px 16px;color:#ffffff;font-weight:bold;">6. จุดประสงค์หลักที่เหมาะใช้</td>
<td style="padding:14px 16px;">มือใหม่ศึกษา หรือต้องการรันสแกนลึกทีละโฟลเดอร์แบบออโต้</td>
<td style="padding:14px 16px;">ทำ Fuzzing พารามิเตอร์ลับ หรือยิงทดสอบแบบข้ามพาธละเอียด</td>
<td style="padding:14px 16px;">กวาดหา Subdomains ของเซิร์ฟเวอร์ หรือทำ Enumeration สกุลไฟล์ด่วน</td>
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
            
            # Find where "### 🛠️ เครื่องมืออัตโนมัติสำหรับการสแกนพาธ" grid container ends
            target_start = val.find("### 🛠️ เครื่องมืออัตโนมัติสำหรับการสแกนพาธ (Automated Scanning Tools)")
            target_end_tag = "</div>"
            
            # Find the first </div> tag after the header
            if target_start != -1:
                # Find the close container tag
                div_close = val.find(target_end_tag, target_start)
                # Find the very last </div> if there is a grid (there are 4 <div>s, let's find the closing of the grid container)
                # The grid container ends right before "---" or "### 📂 การใช้งานเครื่องมือ DIRB"
                grid_end_idx = val.find("---", target_start)
                
                if grid_end_idx != -1:
                    # Insert right before the horizontal separator
                    new_val = val[:grid_end_idx] + comparison_table_html + "\n\n" + val[grid_end_idx:]
                    blocks[0]["value"] = new_val
                    l.content = json.dumps(blocks, ensure_ascii=False)
                    app.db.session.commit()
                    print("Successfully inserted the comparison table into the database!")
                else:
                    print("Error: Could not find separator after scanning tools header.")
            else:
                print("Error: Could not find scanning tools header in database.")
        except Exception as e:
            print(f"Error: {e}")
