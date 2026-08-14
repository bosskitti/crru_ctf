import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

new_f12_html = """### 🛠️ เครื่องมือแกะรหัสหน้าเว็บ (Web Page Source Inspections)

การตรวจสอบโครงสร้างและซอร์สโค้ดหน้าเว็บ (Inspecting a web page) เป็นทักษะขั้นพื้นฐานและคีย์สำคัญสำหรับขั้นตอนการหาช่องโหว่ความเสถียร (Debugging) และการทดสอบเจาะระบบเว็บแอปพลิเคชัน (Web Exploitations) ช่วยทำให้แฮกเกอร์มองเห็นกลไกการรับค่าและสคริปต์ที่นักพัฒนาแอบเขียนซ่อนไว้

ตัวเรียกใช้เครื่องมือนักพัฒนา (Developer Tools หรือ DevTools) บนเบราว์เซอร์ยอดนิยม:
- **Google Chrome / Microsoft Edge / Mozilla Firefox**: กดปุ่ม <kbd style="background:#1e293b;border:1px solid #475569;border-radius:4px;padding:2px 6px;color:#ffffff;font-size:0.75rem;font-family:sans-serif;">F12</kbd> หรือกดปุ่มคีย์ลัด <kbd style="background:#1e293b;border:1px solid #475569;border-radius:4px;padding:2px 6px;color:#ffffff;font-size:0.75rem;font-family:sans-serif;">Ctrl + Shift + I</kbd>
- **Apple Safari**: เข้าเมนู Settings เลือกเปิดใช้งานตัวเลือก **Show Developer Menu** จากนั้นกดคีย์ลัด <kbd style="background:#1e293b;border:1px solid #475569;border-radius:4px;padding:2px 6px;color:#ffffff;font-size:0.75rem;font-family:sans-serif;">Cmd + Option + I</kbd>

#### 🖥️ จำลองหน้าจอการใช้งานเบราว์เซอร์ Developer Tools (DevTools Mockup)

<div style="background:#0b0f17;border:1px solid rgba(0,240,255,0.2);border-radius:12px;padding:24px;margin:2rem auto;max-width:950px;box-shadow:0 12px 40px rgba(0,0,0,0.55);font-family:'Inter',sans-serif;">
<div style="display:flex;align-items:center;justify-content:space-between;background:#151b26;border-radius:8px 8px 0 0;padding:10px 16px;border-bottom:1px solid rgba(255,255,255,0.05);margin:-24px -24px 20px -24px;">
<div style="display:flex;gap:6px;">
<span style="width:10px;height:10px;background:#ef4444;border-radius:50%;display:inline-block;"></span>
<span style="width:10px;height:10px;background:#f59e0b;border-radius:50%;display:inline-block;"></span>
<span style="width:10px;height:10px;background:#10b981;border-radius:50%;display:inline-block;"></span>
</div>
<span style="color:#94a3b8;font-family:monospace;font-size:0.75rem;font-weight:bold;">browser — developer tools (f12) mockup</span>
<div style="width:36px;"></div>
</div>

<p style="color:#cbd5e1;font-size:0.88rem;line-height:1.6;margin-bottom:20px;text-align:left;">
แผงหน้าต่างเครื่องมือนักพัฒนา (DevTools) จะแบ่งพื้นที่ออกเป็นแท็บตัวเลือกต่างๆ ตามภารกิจงาน โดยแฮกเกอร์มักมุ่งเน้นไปที่ 4 แท็บคุณลักษณะหลักดังต่อไปนี้:
</p>

<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(420px,1fr));gap:20px;text-align:left;">

<div style="background:#070911;border:1px solid rgba(6,182,212,0.15);border-radius:8px;padding:16px;">
<div style="font-weight:bold;color:#00f0ff;font-size:0.88rem;margin-bottom:8px;display:flex;align-items:center;gap:6px;">
<span>📄 Elements Tab (วิเคราะห์โครงสร้าง DOM & HTML)</span>
</div>
<p style="color:#94a3b8;font-size:0.78rem;line-height:1.4;margin-bottom:10px;">
ใช้สำหรับตรวจสอบโครงสร้างซอร์สโค้ด HTML เพื่อแก้ไขสลับค่าพารามิเตอร์ส่งกลับไปให้เครื่องแม่ข่ายประมวลผล เช่น การค้นหากล่องข้อมูลที่ถูกซ่อนไว้ (<code style="color:#fbbf24;">&lt;input type="hidden"&gt;</code>) แล้วลองแก้ไขเป็นแบบปกติเพื่อป้อนข้อมูล
</p>
<div style="background:#0b0e14;border-radius:6px;padding:10px;font-family:'JetBrains Mono',monospace;font-size:0.72rem;line-height:1.4;color:#94a3b8;border:1px solid rgba(255,255,255,0.03);">
&lt;form action="/submit-payment" method="POST"&gt;<br>
&nbsp;&nbsp;&lt;input type="text" name="price" value="1000"&gt;<br>
&nbsp;&nbsp;<span style="color:#ef4444;background:rgba(239,68,68,0.1);padding:1px 4px;border-radius:3px;">&lt;input type="hidden" name="admin_role" value="false"&gt;</span><br>
&nbsp;&nbsp;&lt;button type="submit"&gt;Pay Now&lt;/button&gt;<br>
&lt;/form&gt;<br>
<span style="color:#eab308;font-size:0.68rem;display:block;margin-top:6px;">💡 ดับเบิ้ลคลิกเพื่อเปลี่ยน type="hidden" เป็น type="text" หรือแก้ value="false" เป็น "true"</span>
</div>
</div>

<div style="background:#070911;border:1px solid rgba(168,85,247,0.15);border-radius:8px;padding:16px;">
<div style="font-weight:bold;color:#a855f7;font-size:0.88rem;margin-bottom:8px;display:flex;align-items:center;gap:6px;">
<span>💻 Console Tab (หน้ารันคำสั่งและพิมพ์ JavaScript สด)</span>
</div>
<p style="color:#94a3b8;font-size:0.78rem;line-height:1.4;margin-bottom:10px;">
ทำหน้าที่เหมือนหน้าพิมพ์สั่งรันคำสั่งสคริปต์ JavaScript สดบนหน้าเพจ ช่วยดักเก็บตัวแปรที่ค้างในหน่วยความจำ เรียกคำสั่งฟังก์ชันที่อยู่หน้าบ้าน หรือแอบดูค่าคุกกี้ที่เก็บล็อกอินเซสชันของผู้เล่น
</p>
<div style="background:#0b0e14;border-radius:6px;padding:10px;font-family:'JetBrains Mono',monospace;font-size:0.72rem;line-height:1.4;color:#cbd5e1;border:1px solid rgba(255,255,255,0.03);">
<span style="color:#64748b;">&gt; document.cookie</span><br>
<span style="color:#fbbf24;">"session_id=df930ce18fec4cb9b7d0474e6f; admin=0"</span><br>
<span style="color:#64748b;">&gt; bypassValidation = true</span><br>
<span style="color:#10b981;">true</span><br>
<span style="color:#64748b;">&gt; alert(document.cookie) <span style="color:#34d399;">// สั่งรันชุดคำสั่งดักจับข้อมูล</span></span>
</div>
</div>

<div style="background:#070911;border:1px solid rgba(234,179,8,0.15);border-radius:8px;padding:16px;">
<div style="font-weight:bold;color:#eab308;font-size:0.88rem;margin-bottom:8px;display:flex;align-items:center;gap:6px;">
<span>🛠️ Sources Tab (ตรวจสอบซอร์สโค้ดไฟล์ JS & ปัก Breakpoint)</span>
</div>
<p style="color:#94a3b8;font-size:0.78rem;line-height:1.4;margin-bottom:10px;">
ใช้ดีบั๊กและตรวจสอบไฟล์ซอร์สโค้ด JavaScript ทั้งหมด นักเจาะระบบนิยมใช้ปักจุดหยุดทำงานของโปรแกรมชั่วคราว (**Breakpoint**) ที่บรรทัดการประมวลผล เพื่อแอบหยุดดูค่าตัวแปรหรือปลอมแปลงค่าในแรมก่อนส่งค่าต่อ
</p>
<div style="background:#0b0e14;border-radius:6px;padding:10px;font-family:'JetBrains Mono',monospace;font-size:0.72rem;line-height:1.4;color:#94a3b8;border:1px solid rgba(255,255,255,0.03);">
12: function checkAuth(user) {<br>
13: &nbsp;&nbsp;let key = generateKey();<br>
<span style="background:rgba(239,68,68,0.15);color:#ffffff;display:block;padding:2px 0;">14: <span style="color:#ef4444;font-size:0.8rem;line-height:1;margin-right:4px;">●</span> if (user.role === "admin") { <span style="color:#94a3b8;font-size:0.65rem;">&lt;-- จุดหยุดคอย (Breakpoint)</span></span>
15: &nbsp;&nbsp;&nbsp;&nbsp;grantAccess();<br>
16: &nbsp;&nbsp;}<br>
17: }
</div>
</div>

<div style="background:#070911;border:1px solid rgba(16,185,129,0.15);border-radius:8px;padding:16px;">
<div style="font-weight:bold;color:#10b981;font-size:0.88rem;margin-bottom:8px;display:flex;align-items:center;gap:6px;">
<span>📦 Application Tab (แท็บสืบดูการบันทึกคุกกี้เซสชัน)</span>
</div>
<p style="color:#94a3b8;font-size:0.78rem;line-height:1.4;margin-bottom:10px;">
แท็บรายงานการเก็บข้อมูลบนเครื่องโลคัล (Cookies, Local Storage, Session Storage) ใช้ประเมินความปลอดภัยเพื่อตรวจดูว่าคุกกี้เซสชันมีสิทธิการป้องกันพิเศษจากฝั่งเบราว์เซอร์อย่าง <code style="color:#fbbf24;">HttpOnly</code> และ <code style="color:#60a5fa;">Secure</code> ครบถ้วนหรือไม่
</p>
<div style="background:#0b0e14;border-radius:6px;padding:8px;border:1px solid rgba(255,255,255,0.03);overflow-x:auto;">
<table style="width:100%;border-collapse:collapse;font-family:sans-serif;font-size:0.68rem;text-align:left;color:#94a3b8;">
<thead>
<tr style="border-bottom:1px solid rgba(255,255,255,0.08);color:#ffffff;">
<th style="padding:4px;">Cookie Name</th>
<th style="padding:4px;">Cookie Value</th>
<th style="padding:4px;">HttpOnly Protection</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.03);">
<td style="padding:4px;color:#fbbf24;">session</td>
<td style="padding:4px;">df930ce18fec...</td>
<td style="padding:4px;color:#10b981;">✔ Yes (ป้องกันคำสั่ง JS เรียกอ่าน)</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.03);">
<td style="padding:4px;color:#ef4444;">admin_role</td>
<td style="padding:4px;">false</td>
<td style="padding:4px;color:#ef4444;">✖ No (นักสแกนสามารถเข้ามาดัดแปลงแก้ค่าได้)</td>
</tr>
</tbody>
</table>
</div>
</div>

</div>
</div>

"""

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        try:
            blocks = json.loads(l.content)
            val = blocks[0]["value"]
            
            # Find the start of the DevTools section to replace
            start_marker = "### 🛠️ เครื่องมือแกะรหัสหน้าเว็บ (Web Page Source Inspections)"
            end_marker = "### 🍪 การสำรวจระบบจัดเก็บคุกกี้เว็บ (Web Cookies Explorations)"
            
            start_idx = val.find(start_marker)
            end_idx = val.find(end_marker)
            
            if start_idx != -1 and end_idx != -1:
                # Replace with the new premium HTML mockup
                new_val = val[:start_idx] + new_f12_html + "\n\n" + val[end_idx:]
                blocks[0]["value"] = new_val
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print("Successfully updated Web Page Source Inspections (F12) section!")
            else:
                print(f"Error: Markers not found. Start: {start_idx}, End: {end_idx}")
        except Exception as e:
            print(f"Error: {e}")
