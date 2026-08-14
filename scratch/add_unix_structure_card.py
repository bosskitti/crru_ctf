import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

unix_structure_card = """<div style="background: #0b0f19; border: 1px solid rgba(0, 240, 255, 0.15); border-radius: 12px; padding: 24px; margin: 2rem auto; max-width: 850px; box-shadow: 0 8px 32px rgba(0,0,0,0.45); font-family: 'Inter', sans-serif;">
  <div style="display: flex; align-items: center; justify-content: space-between; background: #161b26; border-radius: 8px 8px 0 0; padding: 10px 16px; border-bottom: 1px solid rgba(255,255,255,0.05);">
    <div style="display: flex; gap: 6px;">
      <span style="width: 10px; height: 10px; background: #ef4444; border-radius: 50%; display: inline-block;"></span>
      <span style="width: 10px; height: 10px; background: #f59e0b; border-radius: 50%; display: inline-block;"></span>
      <span style="width: 10px; height: 10px; background: #10b981; border-radius: 50%; display: inline-block;"></span>
    </div>
    <span style="color: #94a3b8; font-family: monospace; font-size: 0.75rem; font-weight: bold;">bash — kali@linux</span>
    <div style="width: 36px;"></div>
  </div>
  <div style="background: #070913; border-radius: 0 0 8px 8px; padding: 24px; text-align: left; position: relative; overflow-x: auto;">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.15rem; line-height: 1.5; margin-bottom: 24px;">
      <span style="color: #34d399; font-weight: bold; margin-right: 12px;">$</span>
      <span style="color: #00f0ff; font-weight: bold; margin-right: 12px;">ls</span>
      <span style="color: #fbbf24; font-weight: bold; margin-right: 12px;">-la</span>
      <span style="color: #a29bfe; font-weight: bold;">/home/kali</span>
    </div>
    <div style="display: flex; flex-direction: column; gap: 12px; font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; color: #cbd5e1; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 20px;">
      <div style="display: flex; align-items: center; gap: 12px;">
        <span style="width: 80px; text-align: right; color: #34d399; font-weight: bold;">$</span>
        <span style="color: #64748b;">───</span>
        <strong style="color: #34d399; width: 90px; display: inline-block;">Prompt</strong>
        <span style="color: #94a3b8;">บอกสถานะว่าระบบพร้อมรับชุดคำสั่ง (Command Prompt)</span>
      </div>
      <div style="display: flex; align-items: center; gap: 12px;">
        <span style="width: 80px; text-align: right; color: #00f0ff; font-weight: bold;">ls</span>
        <span style="color: #64748b;">───</span>
        <strong style="color: #00f0ff; width: 90px; display: inline-block;">Command</strong>
        <span style="color: #94a3b8;">ชื่อคำสั่งหลักที่สั่งให้ระบบปฏิบัติการรันทำงาน (เช่น List directories)</span>
      </div>
      <div style="display: flex; align-items: center; gap: 12px;">
        <span style="width: 80px; text-align: right; color: #fbbf24; font-weight: bold;">-la</span>
        <span style="color: #64748b;">───</span>
        <strong style="color: #fbbf24; width: 90px; display: inline-block;">Options</strong>
        <span style="color: #94a3b8;">ตัวเลือกเพิ่มเติมหรือเรียกว่า Flag (เช่น -l แสดงรายละเอียดแถว, -a แสดงไฟล์ซ่อน)</span>
      </div>
      <div style="display: flex; align-items: center; gap: 12px;">
        <span style="width: 80px; text-align: right; color: #a29bfe; font-weight: bold;">/home/kali</span>
        <span style="color: #64748b;">───</span>
        <strong style="color: #a29bfe; width: 90px; display: inline-block;">Arguments</strong>
        <span style="color: #94a3b8;">เป้าหมายหรือพารามิเตอร์ที่ต้องการให้คำสั่งรันทำงานกระทำด้วย (เช่น พาธโฟลเดอร์)</span>
      </div>
    </div>
  </div>
</div>"""

expanded_dirb_dirbuster_html = """### 📂 การใช้งานเครื่องมือ DIRB (Directory Buster)

**DIRB** คือเครื่องมือในกลุ่ม Command-line เพื่อทำการ Brute-force ค้นหารายการพาธและไฟล์ข้อมูลบนเซิร์ฟเวอร์ โดยจะทดสอบเรียกข้อมูลผ่านรายการคำ (Wordlist) และประมวลผลหา URL ที่มีอยู่จริง (ไม่ว่าหน้าเว็บจะตั้งค่าสกัดกั้น หรือเขียนโปรแกรมป้องกันการส่งรหัส 404 บกพร่องก็ตาม)

#### ตัวอย่างผลลัพธ์การแสกนและรหัสตอบรับ (DIRB Output Logs):

<div style="background:#070a13;border:1px solid rgba(0,240,255,0.15);border-radius:8px;padding:20px;margin:15px auto;font-family:monospace;font-size:0.83rem;color:#3ddc84;text-align:left;max-width:650px;box-shadow:0 4px 15px rgba(0,0,0,0.45);">
<span style="color:#64748b;">(kali@kali)-[~] $ dirb https://www.google.com/ /usr/share/wordlists/dirb/common.txt</span><br>
-----------------<br>
DIRB v2.22 - By The Dark Raver<br>
START_TIME: Mon Mar 3 11:33:14 2025<br>
URL_BASE: https://www.google.com/<br>
WORDLIST_FILES: /usr/share/wordlists/dirb/common.txt<br>
-----------------<br>
GENERATED WORDS: 4612<br>
+ https://www.google.com/2007 (CODE:301|SIZE:239)<br>
+ https://www.google.com/about (CODE:302|SIZE:218)<br>
+ https://www.google.com/alerts (CODE:200|SIZE:154358)<br>
==> DIRECTORY: https://www.google.com/ads/<br>
+ https://www.google.com/advertise (CODE:301|SIZE:224)<br>
+ https://www.google.com/analytics (CODE:301|SIZE:250)
</div>

<div style="background:rgba(6,182,212,0.04);border:1px solid rgba(6,182,212,0.25);border-radius:10px;padding:16px;margin:1.5rem auto;font-size:0.82rem;color:#cbd5e1;line-height:1.6;">
<strong>💡 วิธีวิเคราะห์ข้อมูลผลลัพธ์ (How to read status codes):</strong><br>
- <strong>CODE 200</strong>: พบข้อมูลของหน้าเว็บหรือไฟล์เป้าหมายสำเร็จ สามารถเข้าดูได้โดยตรง<br>
- <strong>CODE 301 / 302</strong>: มีการเปลี่ยนเส้นทาง URL (Redirect) เพื่อส่งต่อไปยังตำแหน่งอื่น<br>
- <strong>DIRECTORY</strong>: ตรวจพบบัญชีรายชื่อห้องโฟลเดอร์ระบบ ที่โปรแกรมจะทำการสำรวจย่อยต่อในเฟสถัดไป
</div>

#### ตารางสรุปรูปแบบการใช้งานคำสั่ง DIRB (DIRB Command Cheat Sheet)

<div style="overflow-x:auto;margin:1.5rem auto;max-width:1000px;border:1px solid rgba(6,182,212,0.25);border-radius:12px;background:#05070f;box-shadow:0 10px 30px rgba(0,0,0,0.6);">
<table style="width:100%;border-collapse:collapse;text-align:left;font-family:sans-serif;font-size:0.85rem;">
<thead>
<tr style="background:rgba(6,182,212,0.08);border-bottom:1px solid rgba(6,182,212,0.2);">
<th style="padding:12px 16px;font-weight:bold;color:#00f0ff;width:35%;">คำอธิบายการใช้งาน (Use Case)</th>
<th style="padding:12px 16px;font-weight:bold;color:#3ddc84;width:65%;">รูปแบบคำสั่งคีย์เวิร์ด (Command)</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;vertical-align:middle;">1. การสแกนไดเรกทอรีขั้นพื้นฐาน (Basic Scan)</td>
<td style="padding:12px 16px;vertical-align:middle;">
<code style="color:#00f0ff;background:rgba(0,240,255,0.05);padding:4px 8px;border-radius:4px;border:1px solid rgba(0,240,255,0.1);font-family:monospace;display:block;font-size:0.78rem;">dirb https://target.com /usr/share/wordlists/dirb/common.txt</code>
<span style="font-size:0.75rem;color:#94a3b8;display:block;margin-top:4px;">สั่งรันค้นหาโฟลเดอร์ปกติโดยใช้ฐานคำศัพท์พื้นฐาน (common.txt)</span>
</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;vertical-align:middle;">2. ค้นหาไฟล์เฉพาะนามสกุล / แบ็คอัป (Find Backup Files)</td>
<td style="padding:12px 16px;vertical-align:middle;">
<code style="color:#00f0ff;background:rgba(0,240,255,0.05);padding:4px 8px;border-radius:4px;border:1px solid rgba(0,240,255,0.1);font-family:monospace;display:block;font-size:0.78rem;">dirb https://target.com /usr/share/wordlists/dirb/common.txt -X .bak,.zip,.tar</code>
<span style="font-size:0.75rem;color:#94a3b8;display:block;margin-top:4px;">เพิ่มออปชัน <code style="color:#ff007f;">-X</code> ตามด้วยชนิดไฟล์ เพื่อดักจับไฟล์สำรองข้อมูลหรือบีบอัดที่หลงเหลือบนเว็บ</span>
</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.005);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;vertical-align:middle;">3. การสแกนแบบไม่แบ่งขนาดตัวพิมพ์ (Case Insensitive)</td>
<td style="padding:12px 16px;vertical-align:middle;">
<code style="color:#00f0ff;background:rgba(0,240,255,0.05);padding:4px 8px;border-radius:4px;border:1px solid rgba(0,240,255,0.1);font-family:monospace;display:block;font-size:0.78rem;">dirb https://target.com -i</code>
<span style="font-size:0.75rem;color:#94a3b8;display:block;margin-top:4px;">ใช้พารามิเตอร์ <code style="color:#ff007f;">-i</code> เพื่อทดสอบเรียกชื่อพาร์ติชันทั้งตัวใหญ่และตัวเล็กสลับกัน</span>
</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);background:rgba(255,255,255,0.015);">
<td style="padding:12px 16px;color:#ffffff;font-weight:bold;vertical-align:middle;">4. บันทึกผลลัพธ์เป็นไฟล์เอกสาร (Save Output File)</td>
<td style="padding:12px 16px;vertical-align:middle;">
<code style="color:#00f0ff;background:rgba(0,240,255,0.05);padding:4px 8px;border-radius:4px;border:1px solid rgba(0,240,255,0.1);font-family:monospace;display:block;font-size:0.78rem;">dirb https://target.com -o result.txt</code>
<span style="font-size:0.75rem;color:#94a3b8;display:block;margin-top:4px;">ใช้พารามิเตอร์ <code style="color:#ff007f;">-o</code> ตามด้วยชื่อไฟล์ เพื่อเขียนประวัติผลการวิเคราะห์เก็บไว้ตรวจสิทธิ์ย้อนหลัง</span>
</td>
</tr>
</tbody>
</table>
</div>

---

### 🖥️ การใช้งานเครื่องมือ DirBuster (OWASP DirBuster GUI)

**DirBuster** เป็นเครื่องมือเวอร์ชันสเปกแผงควบคุมระบบ (GUI-based) ซึ่งเหมาะสำหรับการสแกน brute-force ค้นหาโฟลเดอร์และชื่อไฟล์ที่ซ่อนอยู่ในระดับสูง โดยทำงานผ่าน Threading เพื่อเพิ่มสปีดการทำงานได้อย่างรวดเร็ว

#### วิธีการตั้งค่าใช้งานเบื้องต้น:
1. **Target URL**: ป้อนชื่อโดเมนเว็บไซต์ที่ต้องการทดสอบ เช่น `http://example.com:80/`
2. **Work Method**: เลือกใช้แบบการสลับคำขอเรียกอัตโนมัติ (Auto Switch HEAD and GET)
3. **Number of Threads**: ปรับระดับสปีดการทำงาน (เช่น 10-200 Threads) เพื่อประมวลผลพร้อมๆ กัน
4. **Select scanning type**: เลือกวิธีการ Brute force ผ่าน Wordlist ที่จัดเตรียมไว้ (List based brute force)
5. **File extension**: ระบุชนิดสกุลไฟล์ที่ต้องการค้นหา (เช่น `.php`, `.txt`) จากนั้นกดปุ่ม **Start** เพื่อเริ่มทำงาน"""

with app.app_context():
    # 1. Update Chapter 2 Lesson 166 Block 0
    l2 = app.db.session.query(TutorialLesson).filter_by(id=166).first()
    if l2:
        try:
            blocks2 = json.loads(l2.content)
            val2 = blocks2[0]["value"]
            # Insert unix command structure card right after the main header
            target_h = "## คำสั่งควบคุมไฟล์และจัดการสิทธิ์ใน Linux"
            if target_h not in val2:
                target_h = "## 🐧 คำสั่งควบคุมไฟล์"
                
            idx2 = val2.find(target_h)
            if idx2 == -1:
                # find first header
                idx2 = val2.find("##")
                
            if idx2 != -1:
                end_h = val2.find("\n", idx2)
                if end_h != -1:
                    new_val2 = val2[:end_h+1] + unix_structure_card + "\n\n" + val2[end_h+1:]
                    blocks2[0]["value"] = new_val2
                    l2.content = json.dumps(blocks2, ensure_ascii=False)
                    print("Successfully added UNIX Command Line Structure card to Lesson 166 Block 0!")
        except Exception as e:
            print(f"Error updating Lesson 166: {e}")

    # 2. Update Chapter 5 Lesson 177 Block 0
    l5 = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l5:
        try:
            blocks5 = json.loads(l5.content)
            val5 = blocks5[0]["value"]
            
            # Find the DIRB header in Block 0
            target_marker = "### 📂 การใช้งานเครื่องมือ DIRB (Directory Buster)"
            idx5 = val5.find(target_marker)
            
            if idx5 != -1:
                # Replace with the new expanded DIRB + DirBuster contents
                new_val5 = val5[:idx5] + expanded_dirb_dirbuster_html
                blocks5[0]["value"] = new_val5
                l5.content = json.dumps(blocks5, ensure_ascii=False)
                app.db.session.commit()
                print("Successfully expanded DIRB outputs and DirBuster instructions in Lesson 177 Block 0!")
            else:
                print("Error: Could not find target DIRB header in Lesson 177 Block 0.")
        except Exception as e:
            print(f"Error updating Lesson 177: {e}")
            
    app.db.session.commit()
