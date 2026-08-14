import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

lesson = db.session.query(TutorialLesson).filter_by(id=166).first()
if not lesson:
    print("Lesson 166 not found!")
    exit(1)

blocks = json.loads(lesson.content)

INTRO_CSS = """<style>
.s-intro{display:flex;gap:14px;align-items:flex-start;padding:16px 18px;border-radius:10px;margin-bottom:20px;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);width:100%;max-width:1050px;margin-left:auto;margin-right:auto;box-sizing:border-box;}
.s-intro-icon{font-size:1.5rem;flex-shrink:0;margin-top:1px;}
.s-intro-body strong{display:block;font-size:0.9rem;color:#e2e8f0;margin-bottom:5px;}
.s-intro-body p{margin:0;font-size:0.85rem;color:#94a3b8;line-height:1.7;}
.s-intro-body code{font-family:'JetBrains Mono',monospace;font-size:0.82rem;color:#fbbf24;background:rgba(251,191,36,0.08);padding:1px 5px;border-radius:3px;}
.s-intro.cyan{border-color:rgba(0,240,255,0.15);background:rgba(0,240,255,0.03);}
.s-intro.amber{border-color:rgba(251,191,36,0.15);background:rgba(251,191,36,0.03);}
.s-intro.green{border-color:rgba(61,220,132,0.15);background:rgba(61,220,132,0.03);}
.s-intro.purple{border-color:rgba(171,32,253,0.15);background:rgba(171,32,253,0.03);}
.s-intro.pink{border-color:rgba(244,114,182,0.15);background:rgba(244,114,182,0.03);}
</style>"""

# ─── Block 3: File & Directory ───
old3 = blocks[3]['value']
intro3 = INTRO_CSS + """
<div class="s-intro cyan">
<span class="s-intro-icon">📁</span>
<div class="s-intro-body">
<strong>File and Directory Manipulation Commands</strong>
<p>คำสั่งในกลุ่มนี้ใช้สำหรับ <strong>จัดการไฟล์และ directory</strong> ใน Linux ทั้งการแสดงรายการ สร้าง คัดลอก ย้าย และลบ ถือเป็นคำสั่งพื้นฐานที่ผู้ใช้ Linux ทุกคนต้องรู้ และใช้งานทุกวัน — เรียนรู้คำสั่งเหล่านี้จะช่วยให้คุณนำทางใน Terminal ได้อย่างคล่องตัว</p>
</div>
</div>

"""
blocks[3]['value'] = intro3 + old3

# ─── Block 5: File Examining ───
old5 = blocks[5]['value']
intro5 = INTRO_CSS + """
<div class="s-intro amber">
<span class="s-intro-icon">🔍</span>
<div class="s-intro-body">
<strong>File Examining and Printing Commands</strong>
<p>คำสั่งในกลุ่มนี้ใช้สำหรับ <strong>อ่าน ค้นหา และวิเคราะห์เนื้อหาภายในไฟล์</strong> โดยไม่ต้องเปิด text editor ใช้บ่อยมากในงาน Cybersecurity เช่น การหา flag ที่ซ่อนในไฟล์ (<code>cat</code>, <code>grep</code>, <code>find</code>) หรือการเปรียบเทียบไฟล์ (<code>diff</code>) และการเรียงข้อมูล (<code>sort</code>)</p>
</div>
</div>

"""
blocks[5]['value'] = intro5 + old5

# ─── Block 6: Permission heading — add description ───
blocks[6]['value'] = """---

### 🔐 File and Directory Permission Commands

<style>.perm-sec-intro{width:100%;max-width:1050px;margin:1rem auto 0;display:flex;gap:14px;align-items:flex-start;padding:16px 18px;border-radius:10px;background:rgba(251,191,36,0.03);border:1px solid rgba(251,191,36,0.15);box-sizing:border-box;}.perm-sec-intro-icon{font-size:1.5rem;flex-shrink:0;}.perm-sec-intro-body strong{display:block;font-size:0.9rem;color:#e2e8f0;margin-bottom:5px;}.perm-sec-intro-body p{margin:0;font-size:0.85rem;color:#94a3b8;line-height:1.7;}.perm-sec-intro-body code{font-family:'JetBrains Mono',monospace;font-size:0.82rem;color:#fbbf24;background:rgba(251,191,36,0.08);padding:1px 5px;border-radius:3px;}</style>
<div class="perm-sec-intro">
<span class="perm-sec-intro-icon">🛡️</span>
<div class="perm-sec-intro-body">
<strong>Permission System ใน Linux</strong>
<p>Linux กำหนด <strong>สิทธิ์การเข้าถึง (Permission)</strong> ให้กับทุกไฟล์และ directory เพื่อควบคุมว่า <em>ใคร</em> จะสามารถ <em>ทำอะไร</em> ได้บ้าง โดยแบ่งออกเป็น 3 ระดับ ได้แก่ <code>owner</code> (เจ้าของ), <code>group</code> (กลุ่ม), และ <code>others</code> (ผู้อื่น) และ 3 ประเภทสิทธิ์ ได้แก่ <code>r</code> (read), <code>w</code> (write), <code>x</code> (execute) — การเข้าใจ Permission เป็นพื้นฐานสำคัญของ Linux Security</p>
</div>
</div>"""

# ─── Block 10: Frequently Used heading — add description ───
blocks[10]['value'] = """---

### ⚡ Frequently Used Commands

<style>.freq-sec-intro{width:100%;max-width:1050px;margin:1rem auto 0;display:flex;gap:14px;align-items:flex-start;padding:16px 18px;border-radius:10px;background:rgba(61,220,132,0.03);border:1px solid rgba(61,220,132,0.15);box-sizing:border-box;}.freq-sec-intro-icon{font-size:1.5rem;flex-shrink:0;}.freq-sec-intro-body strong{display:block;font-size:0.9rem;color:#e2e8f0;margin-bottom:5px;}.freq-sec-intro-body p{margin:0;font-size:0.85rem;color:#94a3b8;line-height:1.7;}.freq-sec-intro-body code{font-family:'JetBrains Mono',monospace;font-size:0.82rem;color:#3ddc84;background:rgba(61,220,132,0.08);padding:1px 5px;border-radius:3px;}</style>
<div class="freq-sec-intro">
<span class="freq-sec-intro-icon">⚡</span>
<div class="freq-sec-intro-body">
<strong>คำสั่งที่ใช้บ่อยใน Linux / Unix</strong>
<p>คำสั่งเหล่านี้เป็นคำสั่งทั่วไปที่ใช้ใน <strong>การบริหารและตรวจสอบระบบ</strong> ครอบคลุมตั้งแต่การดูข้อมูลระบบ (<code>uname</code>, <code>uptime</code>, <code>df</code>) การจัดการ process (<code>ps</code>, <code>kill</code>, <code>top</code>) การตรวจสอบ user (<code>who</code>, <code>id</code>, <code>last</code>) ไปจนถึงการตั้งค่า network (<code>ifconfig</code>) — ควรจดจำไว้เพราะใช้ประจำในงาน Cybersecurity</p>
</div>
</div>"""

# ─── Block 13: sep before Control-Keys — update with description ───
blocks[13]['value'] = "---"

# ─── Block 14: Control-Keys — update intro color/style ───
old14 = blocks[14]['value']
# The block already has a .ctrl-intro box. Update it to be more descriptive.
blocks[14]['value'] = old14.replace(
    '<div class="ctrl-intro">\n<strong style="color:#00f0ff;">Control-key</strong> คือแป้นพิมพ์ลัด (Keyboard Shortcut) ที่ใช้ร่วมกับปุ่ม <code>Ctrl</code> เพื่อควบคุมการทำงานของ Terminal และ Shell โดยไม่ต้องใช้เมาส์ มีความสำคัญมากสำหรับ Text-based Interface\n</div>',
    '<div class="ctrl-intro">\n<strong style="color:#00f0ff;">Control-key</strong> คือ <strong>แป้นพิมพ์ลัด (Keyboard Shortcut)</strong> ที่ใช้ร่วมกับปุ่ม <code>Ctrl</code> เพื่อควบคุมการทำงานของ Terminal และ Shell โดยไม่ต้องใช้เมาส์ มีความสำคัญมากสำหรับ <strong>Text-based User Interface (TUI)</strong> เพราะ Linux Terminal ไม่มี GUI ปุ่มเหล่านี้ใช้ควบคุมการ หยุด / รีเซ็ต / ลบ input และจัดการ process ที่รันอยู่\n</div>'
)

# ─── Block 15: Redirections + Env Vars — add section intro ───
old15 = blocks[15]['value']
intro15 = INTRO_CSS + """
<div class="s-intro purple">
<span class="s-intro-icon">🔀</span>
<div class="s-intro-body">
<strong>Redirections & Environment Variables</strong>
<p><strong>Redirection</strong> คือการเปลี่ยนทิศทาง Input/Output ของคำสั่ง แทนที่จะแสดงผลบนหน้าจอสามารถส่งไปยังไฟล์หรือโปรแกรมอื่นได้ด้วย <code>&gt;</code>, <code>&gt;&gt;</code>, <code>|</code> ซึ่งมีประโยชน์มากในการ script และ automation<br>
<strong>Environment Variables</strong> คือตัวแปรที่ระบบจัดเก็บค่าสำคัญไว้ให้ Shell และโปรแกรมต่างๆ ใช้งาน เช่น <code>$PATH</code> บอก Shell ว่าจะหาคำสั่งได้จาก directory ไหน</p>
</div>
</div>

"""
blocks[15]['value'] = intro15 + old15

# ─── Block 16: Regex + Wildcards — add section intro ───
old16 = blocks[16]['value']
intro16 = INTRO_CSS + """
<div class="s-intro pink">
<span class="s-intro-icon">🔎</span>
<div class="s-intro-body">
<strong>Regular Expressions & Wildcards</strong>
<p><strong>Regular Expression (Regex)</strong> คือลำดับตัวอักษรที่ใช้ระบุ pattern ในการค้นหาข้อความ ใช้กับ <code>grep</code> และ <code>find</code> — มีความสามารถสูง แต่ต้องเรียนรู้ syntax เพิ่มเติม<br>
<strong>Wildcard</strong> คือตัวแทนอักขระที่ง่ายกว่า ใช้กับคำสั่ง Shell เช่น <code>ls *.txt</code> หรือ <code>find /home -name "flag?"</code> — ความแตกต่างหลักคือ Wildcard ทำงานกับ <strong>ชื่อไฟล์</strong> ส่วน Regex ทำงานกับ <strong>เนื้อหาข้อความ</strong></p>
</div>
</div>

"""
blocks[16]['value'] = intro16 + old16

lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=166).update({"content": lesson.content})
db.session.commit()

print("Section intro boxes added to all topics!")
for i, b in enumerate(blocks):
    print(f"  Block {i}: {len(b['value'])} chars")
