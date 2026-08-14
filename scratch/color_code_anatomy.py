import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

new_anatomy_html = """### 🔎 โครงสร้างกายวิภาคของข้อความ HTTP Request & Response (HTTP Message Anatomy)

ข้อความ HTTP มีการจัดเรียงรูปแบบโครงสร้างที่เป็นแบบแผนเดียวกัน ทั้งฝั่งที่ส่งออกไป (Request) และฝั่งที่รับกลับมา (Response) โดยมีการจำแนกสัดส่วนแยกส่วนด้วยสีหลัก 4 สีอย่างชัดเจน เพื่อความง่ายต่อการจดจำโครงสร้าง:

<div style="display:flex;flex-direction:column;gap:16px;margin:2rem auto;max-width:950px;font-family:'JetBrains Mono',monospace;font-size:0.83rem;">
<div style="display:flex;gap:12px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.05);border-radius:10px;padding:16px;align-items:stretch;">
<div style="flex:1;background:#05070f;border:1px solid rgba(0,240,255,0.2);border-radius:6px;padding:12px;text-align:left;line-height:1.5;">
<span style="color:#64748b;font-size:0.72rem;display:block;margin-bottom:6px;"># HTTP Request Structure</span>
<div style="background:rgba(0,240,255,0.12);color:#00f0ff;padding:3px 6px;border-radius:4px;font-weight:bold;margin-bottom:4px;">POST /login HTTP/1.1</div>
<div style="background:rgba(234,179,8,0.08);color:#eab308;padding:4px 6px;border-radius:4px;margin-bottom:4px;">
Host: www.example.com<br>
Content-Type: application/json<br>
Content-Length: 32
</div>
<div style="border-top:1px dashed rgba(255,0,127,0.3);height:12px;margin:4px 0;position:relative;" title="Empty Line">
<span style="position:absolute;top:-8px;left:6px;background:#05070f;padding:0 4px;color:#ff007f;font-size:0.6rem;font-weight:bold;">(Empty Line)</span>
</div>
<div style="background:rgba(61,220,132,0.08);color:#3ddc84;padding:6px;border-radius:4px;">
{"username":"admin"}
</div>
</div>
<div style="width:140px;display:flex;flex-direction:column;justify-content:space-between;text-align:center;font-size:0.75rem;font-weight:bold;padding:12px 0;">
<div style="color:#00f0ff;">◀ Start Line ▶</div>
<div style="color:#eab308;margin:12px 0;">◀ Headers ▶</div>
<div style="color:#ff007f;margin:8px 0;">◀ Empty Line ▶</div>
<div style="color:#3ddc84;">◀ Body (Data) ▶</div>
</div>
<div style="flex:1;background:#05070f;border:1px solid rgba(61,220,132,0.2);border-radius:6px;padding:12px;text-align:left;line-height:1.5;">
<span style="color:#64748b;font-size:0.72rem;display:block;margin-bottom:6px;"># HTTP Response Structure</span>
<div style="background:rgba(0,240,255,0.12);color:#00f0ff;padding:3px 6px;border-radius:4px;font-weight:bold;margin-bottom:4px;">HTTP/1.1 200 OK</div>
<div style="background:rgba(234,179,8,0.08);color:#eab308;padding:4px 6px;border-radius:4px;margin-bottom:4px;">
Server: Apache/2.4.41<br>
Content-Type: text/html<br>
Content-Length: 1024
</div>
<div style="border-top:1px dashed rgba(255,0,127,0.3);height:12px;margin:4px 0;position:relative;" title="Empty Line">
<span style="position:absolute;top:-8px;left:6px;background:#05070f;padding:0 4px;color:#ff007f;font-size:0.6rem;font-weight:bold;">(Empty Line)</span>
</div>
<div style="background:rgba(61,220,132,0.08);color:#3ddc84;padding:6px;border-radius:4px;">
&lt;html&gt;Hello World&lt;/html&gt;
</div>
</div>
</div>
</div>"""

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        try:
            blocks = json.loads(l.content)
            val = blocks[0]["value"]
            
            start_marker = "### 🔎 โครงสร้างกายวิภาคของข้อความ HTTP Request & Response (HTTP Message Anatomy)"
            end_marker = "#### โครงสร้างองค์ประกอบสำคัญ (Component Breakdowns):"
            
            start_idx = val.find(start_marker)
            end_idx = val.find(end_marker)
            
            if start_idx != -1 and end_idx != -1:
                # Replace with the new color-coded anatomy view
                new_val = val[:start_idx] + new_anatomy_html + "\n\n" + val[end_idx:]
                blocks[0]["value"] = new_val
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print("Successfully updated HTTP Message Anatomy with premium color-coding!")
            else:
                print(f"Error: Markers not found. Start: {start_idx}, End: {end_idx}")
        except Exception as e:
            print(f"Error: {e}")
