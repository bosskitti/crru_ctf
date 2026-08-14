import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l168 = db.session.query(TutorialLesson).filter_by(id=168).first()
blocks = json.loads(l168.content)

# ─── 1. Block 39: Linux vs Windows Comparison Table (Cyberpunk Style) ───
blocks[39]['value'] = """### ⚖️ Linux vs Windows: Comparison Table

เปรียบเทียบข้อแตกต่างที่สำคัญในด้านสถาปัตยกรรม บัญชีผู้ใช้งาน และระบบรักษาความปลอดภัยระหว่างสองระบบปฏิบัติการ:

<style>
.comp-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.comp-card{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,0.2);}
.comp-tbl{width:100%;border-collapse:collapse;table-layout:fixed;}
.comp-tbl th{padding:12px 16px;text-align:left;font-size:0.82rem;text-transform:uppercase;letter-spacing:0.08em;font-weight:700;border-bottom:1px solid rgba(255,255,255,0.08);}
.comp-tbl th.cat{width:15%;color:#fbbf24;background:rgba(251,191,36,0.02);}
.comp-tbl th.lin{width:42.5%;color:#3ddc84;background:rgba(61,220,132,0.02);border-left:1px solid rgba(255,255,255,0.05);}
.comp-tbl th.win{width:42.5%;color:#00f0ff;background:rgba(0,240,255,0.02);border-left:1px solid rgba(255,255,255,0.05);}
.comp-tbl td{padding:14px 16px;border-bottom:1px solid rgba(255,255,255,0.04);font-size:0.88rem;vertical-align:top;line-height:1.6;}
.comp-tbl tr:last-child td{border-bottom:none;}
.comp-tbl tr:hover td{background:rgba(255,255,255,0.015);}
.comp-cat{font-weight:700;color:#8a94a6;font-size:0.8rem;text-transform:uppercase;}
.comp-tbl td.lin-val{border-left:1px solid rgba(255,255,255,0.04);color:#cbd5e1;}
.comp-tbl td.win-val{border-left:1px solid rgba(255,255,255,0.04);color:#cbd5e1;}
.comp-tbl td strong{color:#ffffff;}
.comp-lin-tag{display:inline-block;padding:2px 6px;border-radius:4px;font-size:0.72rem;font-weight:700;color:#3ddc84;background:rgba(61,220,132,0.08);border:1px solid rgba(61,220,132,0.2);margin-bottom:6px;}
.comp-win-tag{display:inline-block;padding:2px 6px;border-radius:4px;font-size:0.72rem;font-weight:700;color:#00f0ff;background:rgba(0,240,255,0.08);border:1px solid rgba(0,240,255,0.2);margin-bottom:6px;}
</style>

<div class="comp-wrap">
<div class="comp-card">
<table class="comp-tbl">
<thead>
<tr>
<th class="cat">Category</th>
<th class="lin">🐧 Linux OS</th>
<th class="win">🟦 Windows OS</th>
</tr>
</thead>
<tbody>
<tr>
<td class="comp-cat">License & Source</td>
<td class="comp-val lin-val">
<span class="comp-lin-tag">Open-Source</span><br>
เป็นระบบปฏิบัติการแบบเปิดเผยโค้ด (Open-Source) ใช้งานได้ฟรี นักพัฒนาทั่วโลกสามารถมีส่วนร่วมแก้ไขบั๊กและพัฒนาฟีเจอร์ความปลอดภัยได้อย่างรวดเร็ว
</td>
<td class="comp-val win-val">
<span class="comp-win-tag">Commercial</span><br>
เป็นระบบปฏิบัติการเพื่อการค้า (Commercial/Proprietary) มีค่าลิขสิทธิ์ การอัปเดตและแก้ไขบั๊กความปลอดภัยทำได้โดยทีมพัฒนาของ Microsoft เท่านั้น
</td>
</tr>
<tr>
<td class="comp-cat">System Kernel</td>
<td class="comp-val lin-val">
<span class="comp-lin-tag">Monolithic Kernel</span><br>
ใช้เคอร์เนลแบบ <strong>Monolithic</strong> บริการระบบทั้งหมดรันในพื้นที่เคอร์เนลเดียวกันเพื่อประสิทธิภาพสูงสุด และมองอุปกรณ์ฮาร์ดแวร์ภายนอกทุกชิ้นเป็น <strong>"ไฟล์" (Everything is a file)</strong>
</td>
<td class="comp-val win-val">
<span class="comp-win-tag">Hybrid / Micro Kernel</span><br>
ใช้เคอร์เนลแบบ <strong>Hybrid</strong> (อิงสถาปัตยกรรม Microkernel) แยกการทำงานของส่วนบริการต่างๆ และมองอุปกรณ์เชื่อมต่อเป็นไดรฟ์หรือพาร์ติชันแยกกัน (เช่น <strong>C:, D:</strong>)
</td>
</tr>
<tr>
<td class="comp-cat">User Accounts</td>
<td class="comp-val lin-val">
<span class="comp-lin-tag">3 User Types</span><br>
แบ่งระดับบัญชีผู้ใช้เป็น 3 ประเภท:<br>
1. <strong>Root</strong> (สิทธิ์สูงสุด/ผู้ดูแลระบบ)<br>
2. <strong>Regular User</strong> (ผู้ใช้ทั่วไป)<br>
3. <strong>Service User</strong> (ผู้ใช้ของระบบบริการ)
</td>
<td class="comp-val win-val">
<span class="comp-win-tag">5 User Types</span><br>
แบ่งระดับบัญชีผู้ใช้ละเอียดกว่าเป็น 5 ประเภท:<br>
1. <strong>Administrator</strong> (ผู้ดูแลระบบ)<br>
2. <strong>Standard</strong> (ผู้ใช้ทั่วไป)<br>
3. <strong>Work/School</strong> | 4. <strong>Child</strong> | 5. <strong>Guest</strong>
</td>
</tr>
<tr>
<td class="comp-cat">Cyber Security</td>
<td class="comp-val lin-val">
<span class="comp-lin-tag">High Security</span><br>
มีความปลอดภัยสูงมากเมื่อเปรียบเทียบกัน เนื่องจากสิทธิ์การรันโค้ดคุมเข้ม (ต้องใช้ <code>sudo</code>) และเป็นระบบปฏิบัติการหลักที่รันเครื่องมือทดสอบความปลอดภัยทางไซเบอร์ส่วนใหญ่
</td>
<td class="comp-val win-val">
<span class="comp-win-tag">Target of Attacks</span><br>
มีโอกาสตกเป็นเป้าหมายของการโจมตีและไวรัส/มัลแวร์สูงกว่าเนื่องจากผู้ใช้งานทั่วไปมีจำนวนมาก และการตั้งค่าเริ่มต้นบางอย่างให้สิทธิ์ผู้ใช้ทำงานในระดับแอดมินโดยง่าย
</td>
</tr>
</tbody>
</table>
</div>
</div>"""


# ─── 2. Block 41: Q&A Accordion (Interactive Cyberpunk Style) ───
blocks[41]['value'] = """### ❓ Questions & Answers (Q&A)

ไขข้อสงสัยพื้นฐานเกี่ยวกับการเรียนรู้คำสั่งและการจัดการระบบปฏิบัติการ:

<style>
.qa-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:12px;}
.qa-item{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:10px;overflow:hidden;transition:all 0.25s ease;}
.qa-item:hover{border-color:rgba(0,240,255,0.25);background:rgba(0,240,255,0.01);box-shadow:0 4px 15px rgba(0,0,0,0.3);}
.qa-q{padding:16px 20px;font-size:0.92rem;font-weight:700;color:#e2e8f0;cursor:pointer;display:flex;justify-content:between;align-items:center;user-select:none;}
.qa-q::after{content:"▼";font-size:0.65rem;color:#64748b;margin-left:auto;transition:transform 0.2s ease;}
.qa-item.active .qa-q::after{transform:rotate(180deg);color:#00f0ff;}
.qa-a{max-height:0;overflow:hidden;padding:0 20px;font-size:0.86rem;color:#94a3b8;line-height:1.7;transition:all 0.25s ease-out;background:rgba(0,0,0,0.15);}
.qa-item.active .qa-a{max-height:300px;padding:16px 20px;border-top:1px solid rgba(255,255,255,0.03);}
.qa-item.active .qa-q{color:#00f0ff;}
</style>

<div class="qa-wrap">

<div class="qa-item active">
<div class="qa-q" onclick="toggleQA(this)">1. ทำไมเราต้องเรียนรู้ทั้งคำสั่ง Linux (Terminal) และ Windows (DOS/Command Prompt) ในงานความปลอดภัยไซเบอร์?</div>
<div class="qa-a">
ในสายงาน Cybersecurity เราจำเป็นต้องวิเคราะห์ ตรวจสอบ หรือเจาะระบบปฏิบัติการทั้งสองฝั่ง ระบบเซิร์ฟเวอร์และแอปพลิเคชันส่วนใหญ่ทำงานบน Linux ในขณะที่เครื่องของผู้ใช้งานทั่วไป (Client) มักเป็นระบบ Windows การเข้าใจโครงสร้างสิทธิ์ (Permissions) และคำสั่งควบคุมระบบทั้งคู่ จะช่วยให้ผู้ควบคุมระบบสามารถสแกน ตรวจจับช่องโหว่ หรือค้นหาจุดบกพร่องได้อย่างครอบคลุม
</div>
</div>

<div class="qa-item">
<div class="qa-q" onclick="toggleQA(this)">2. คำสั่ง 'findstr' ใน Windows แตกต่างจาก 'find' อย่างไร?</div>
<div class="qa-a">
คำสั่ง <code>find</code> ใน Windows ใช้ค้นหาคำในไฟล์แบบระบุข้อความตรงตัวเท่านั้น ไม่มีฟีเจอร์ขั้นสูง ส่วนคำสั่ง <code>findstr</code> เป็นคำสั่งที่พัฒนาให้มีประสิทธิภาพสูงขึ้นมาก โดยรองรับการค้นหาด้วย <strong>Regular Expressions (Regex)</strong> และการค้นหาไฟล์ย้อนกลับลงไปในโฟลเดอร์ย่อย (Recursive search) ทำหน้าที่คล้ายกับ <code>grep</code> ใน Linux
</div>
</div>

<div class="qa-item">
<div class="qa-q" onclick="toggleQA(this)">3. การปฏิเสธสิทธิ์ด้วย 'icacls /deny' มีผลต่างจากการยกเลิกการอนุญาตปกติอย่างไร?</div>
<div class="qa-a">
ในระบบความปลอดภัย Windows NTFS Permissions กฎการปฏิเสธสิทธิ์ (Explicit Deny) จะมีผล **สำคัญที่สุด (Override)** เสมอ หมายความว่า แม้กลุ่มผู้ใช้งานของ User นั้นจะได้รับสิทธิ์ <code>Full Control</code> ผ่านระบบ <code>/grant</code> แต่หากตัวบัญชีผู้ใช้งานส่วนตัวถูกระบุในรายการ <code>/deny</code> แม้เพียงสิทธิ์เดียว ระบบความปลอดภัยจะบล็อกและห้าม User คนนั้นเข้าถึงทรัพยากรทันที
</div>
</div>

</div>

<script>
function toggleQA(element) {
    const item = element.parentElement;
    item.classList.toggle("active");
}
</script>"""

l168.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=168).update({"content": l168.content})
db.session.commit()
print("Linux vs Windows table and FAQ/Q&A Accordion blocks updated successfully!")
