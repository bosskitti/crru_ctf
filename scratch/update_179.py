import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

def save_lesson(lid, val0, val1, val2):
    l = db.session.query(TutorialLesson).filter_by(id=lid).first()
    blocks = [
        {"type": "markdown", "value": val0},
        {"type": "markdown", "value": val1},
        {"type": "markdown", "value": val2}
    ]
    l.content = json.dumps(blocks, ensure_ascii=False)
    db.session.query(TutorialLesson).filter_by(id=lid).update({"content": l.content})
    db.session.commit()
    print(f"Lesson {lid} successfully upgraded!")

val179_0 = """<div style="text-align: center; margin-bottom: 2rem; padding: 20px; background: linear-gradient(135deg, rgba(59,130,246,0.1) 0%, rgba(168,85,247,0.1) 100%); border: 1px solid rgba(255,255,255,0.06); border-radius: 16px;">
<h2 style="margin: 0; font-size: 1.8rem; font-weight: 800; color: #ffffff; text-shadow: 0 0 10px rgba(59,130,246,0.5);">🎭 SQL Injection, Command Injection & Broken Auth</h2>
<p style="margin: 8px 0 0 0; font-size: 0.9rem; color: #94a3b8;">เจาะลึกเทคนิคการดึงข้อมูลระดับสูง การฝังแทรกคำสั่งควบคุมเซิร์ฟเวอร์ และการวิเคราะห์เซสชันความปลอดภัย</p>
</div>

### 💉 ประเภทและเทคนิคการโจมตี SQL Injection (SQLi)
เทคนิคการยิงคำสั่ง SQL มีหลายวิธีเพื่อบังคับให้ฐานข้อมูลแสดงผลลัพธ์ที่เป็นความลับ:

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1-fraction)); gap: 16px; margin: 1.5rem auto;">
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 18px;">
<strong style="color: #3b82f6; font-size: 0.95rem; display: block; margin-bottom: 8px;">🔑 Bypass Authentication</strong>
ใช้ประพจน์ตรรกศาสตร์ที่เป็นจริงเสมอ เช่น <code style="color: #3b82f6;">' OR 1=1 --</code> เพื่อหักล้างเงื่อนไขความถูกต้องของรหัสผ่านในตารางล็อกอิน
</div>
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 18px;">
<strong style="color: #3b82f6; font-size: 0.95rem; display: block; margin-bottom: 8px;">🔗 UNION-Based SQLi</strong>
การใช้คำสั่ง <code style="color: #3b82f6;">UNION SELECT</code> ผสานผลลัพธ์ของคิวรีหลัก เพื่อดึงข้อมูลข้ามตาราง เช่นการดึงชื่อผู้ใช้และรหัสผ่านจากตารางสมาชิก
</div>
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 18px;">
<strong style="color: #3b82f6; font-size: 0.95rem; display: block; margin-bottom: 8px;">⏱️ Blind SQL Injection</strong>
ใช้สืบค้นข้อมูลในกรณีเซิร์ฟเวอร์ไม่แสดงเอเรอร์ใดๆ โดยจับสังเกตตรรกะหน้าเว็บที่เปลี่ยนไป (Boolean) หรือการหน่วงเวลาคำสั่ง (Time-based เช่น <code style="color: #3b82f6;">sleep(5)</code>)
</div>
</div>

---

### ⚙️ คู่มือสืบค้นหาช่องโหว่ฐานข้อมูลอัตโนมัติด้วย SQLMap
SQLMap เป็นโปรแกรม CLI ยอดนิยมในการแกะโครงสร้างและดึงฐานข้อมูลแบบอัตโนมัติ:

<div style="overflow-x: auto; margin: 1.5rem auto; max-width: 1000px; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; background: #05070f;">
<table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.85rem;">
<thead>
<tr style="background: rgba(255,255,255,0.03); border-bottom: 1px solid rgba(255,255,255,0.08);">
<th style="padding: 12px 16px; color: #00f0ff; width: 35%;">คำสั่งสั่งการ (Command Example)</th>
<th style="padding: 12px 16px; color: #00f0ff; width: 65%;">คำอธิบายเป้าหมายการทดสอบ</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 12px 16px; font-family: monospace; color: #a7f3d0; vertical-align: top;">sqlmap -u "URL" --dbs</td>
<td style="padding: 12px 16px; color: #cbd5e1; vertical-align: top;">สืบค้นและแสดงรายชื่อฐานข้อมูล (Databases) ทั้งหมดบนระบบหลังบ้าน</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 12px 16px; font-family: monospace; color: #a7f3d0; vertical-align: top;">sqlmap -u "URL" -D db --tables</td>
<td style="padding: 12px 16px; color: #cbd5e1; vertical-align: top;">ดึงรายชื่อตาราง (Tables) ทั้งหมดที่อยู่ในฐานข้อมูลชื่อ <code style="color: #3b82f6;">db</code></td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 12px 16px; font-family: monospace; color: #a7f3d0; vertical-align: top;">sqlmap -u "URL" -D db -T users --columns</td>
<td style="padding: 12px 16px; color: #cbd5e1; vertical-align: top;">เรียกดูรายชื่อคอลัมน์ฟิลด์ (Columns) ทั้งหมดในตาราง <code style="color: #3b82f6;">users</code></td>
</tr>
<tr>
<td style="padding: 12px 16px; font-family: monospace; color: #a7f3d0; vertical-align: top;">sqlmap -u "URL" --os-shell</td>
<td style="padding: 12px 16px; color: #cbd5e1; vertical-align: top;">กรณีสิทธิ์ฐานข้อมูลสูง ยอมให้เขียนเว็บเชลล์อัปโหลดเพื่อเปิดหน้ารันคำสั่งระบบปฏิบัติการ</td>
</tr>
</tbody>
</table>
</div>

---

### 🐚 OS Command Injection & Broken Authentication
<div style="background: rgba(239,68,68,0.04); border: 1px solid rgba(239,68,68,0.25); border-radius: 12px; padding: 20px; margin: 1.5rem auto; box-shadow: 0 4px 15px rgba(239,68,68,0.05);">
<h4 style="margin: 0 0 10px 0; font-size: 1rem; color: #f87171; font-weight: bold;">⚠️ การแฝงคำสั่งและจุดเปราะบางความปลอดภัยเซสชัน</h4>
<p style="margin: 0; font-size: 0.84rem; color: #cbd5e1; line-height: 1.6;">
- <strong>OS Command Injection</strong>: ช่องโหว่จากการที่หลังบ้านนำตัวแปรป้อนเข้าของผู้ใช้ ไปรวมเข้าเป็นส่วนหนึ่งของสตริงประมวลผลคำสั่งระบบปฏิบัติการโดยตรง ทำให้ผู้โจมตีสามารถสั่งพิมพ์อ่านไฟล์ในระบบได้ตามต้องการ<br>
- <strong>Filter Evasion (Space Bypass)</strong>: หากระบบห้ามพิมพ์ช่องว่าง แฮกเกอร์จะใช้ตัวแปรสภาพแวดล้อมระบบ <code style="color: #f87171;">${IFS}</code> ทำงานคั่นแทน เช่น <code style="color: #f87171;">cat${IFS}/etc/passwd</code> เพื่อข้ามผ่านตัวกรอง<br>
- <strong>Broken Authentication</strong>: ความล้มเหลวในการบริหารจัดการรหัสผ่านและเซสชัน เช่น การไม่ตั้ง Rate Limiting บล็อกบอต Brute Force หรือยอมให้ตั้งรหัสผ่านง่ายเกินไป
</p>
</div>"""

val179_1 = """### 💻 SQLi & Command Injection Lab Simulator (จำลองการแทรกคำสั่งประมวลผล)

คลิกหัวข้อด้านซ้ายมือเพื่อศึกษาช่องโหว่ และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลการแทรกคำสั่ง:

<style type="text/css">
.w-sandbox-main { display: flex !important; gap: 20px !important; margin: 1.5rem auto !important; max-width: 1000px !important; }
.w-sandbox-nav { width: 220px !important; display: flex !important; flex-direction: column !important; gap: 8px !important; flex-shrink: 0 !important; }
.w-nav-item { background: rgba(255, 255, 255, 0.02) !important; border: 1px solid rgba(255, 255, 255, 0.06) !important; border-radius: 6px !important; padding: 10px 14px !important; color: #cbd5e1 !important; text-align: left !important; cursor: pointer !important; font-size: 0.78rem !important; transition: all 0.2s !important; }
.w-nav-item:hover, .w-nav-item.active { border-color: #3b82f6 !important; color: #ffffff !important; background: rgba(59, 130, 246, 0.05) !important; }
.w-nav-item.active { font-weight: 700 !important; box-shadow: 0 0 8px rgba(59, 130, 246, 0.15) !important; }
.w-sandbox-panels { flex-grow: 1 !important; display: flex !important; flex-direction: column !important; gap: 14px !important; }
.w-sand-panel { display: none; background: #05070f !important; border: 1px solid rgba(255, 255, 255, 0.08) !important; border-radius: 10px !important; padding: 20px !important; box-shadow: 0 8px 24px rgba(0,0,0,0.45) !important; }
.w-sand-panel.active { display: block !important; }
</style>
<div class="w-sandbox-main" style="display: flex; gap: 20px; margin: 1.5rem auto; max-width: 1000px;">
<div class="w-sandbox-nav" style="width: 220px; display: flex; flex-direction: column; gap: 8px; flex-shrink: 0;">
<button id="nav-item-sqlitest" class="w-nav-item active" style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 6px; padding: 10px 14px; color: #cbd5e1; text-align: left; cursor: pointer; font-size: 0.78rem; transition: all 0.2s;" onclick="showSandboxItem('sqlitest', this)">1. UNION SQLi Test</button>
<button id="nav-item-cmdtest" class="w-nav-item" style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 6px; padding: 10px 14px; color: #cbd5e1; text-align: left; cursor: pointer; font-size: 0.78rem; transition: all 0.2s;" onclick="showSandboxItem('cmdtest', this)">2. OS Command Injection</button>
</div>
<div class="w-sandbox-panels" style="flex-grow: 1; display: flex; flex-direction: column; gap: 14px;">
<div id="panel-sqlitest" class="w-sand-panel active" style="background: #05070f; border: 1px solid rgba(255, 255, 255, 0.08) !important; border-radius: 10px !important; padding: 20px !important; box-shadow: 0 8px 24px rgba(0,0,0,0.45) !important;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>1. UNION-Based SQL Injection Simulation</span>
<span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(59,130,246,0.08); border: 1px solid rgba(59,130,246,0.2); color: #3b82f6; font-family: monospace;">UNION SQLi</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #3b82f6; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">' UNION SELECT null, username, password FROM users --</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button style="background: rgba(59,130,246,0.1); border: 1px solid rgba(59,130,246,0.3); border-radius: 4px; color: #3b82f6; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700; transition: all 0.15s;" onclick="startWebSim('sqlitest')">▶ Run Simulation</button>
</div>
<div id="term-sqlitest" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 90px;">
<span style="color: #3ddc84;">db-cli$</span> [กดปุ่ม Run Simulation เพื่อส่ง UNION payload]
</div>
</div>
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 16px; font-size: 0.83rem; color: #cbd5e1; line-height: 1.65;">
<h5 style="margin: 0 0 8px; font-size: 0.85rem; color: #fbbf24; font-weight: bold;">⚙️ Command Description</h5>
<p style="margin: 0;">คิวรีผสาน UNION SELECT ช่วยให้เราแอบไปดึงข้อมูลผู้ใช้งานและรหัสผ่านจากตารางอื่นออกมาทางเว็บบอร์ดแสดงผล</p>
</div>
</div>
<div id="panel-cmdtest" class="w-sand-panel" style="background: #05070f; border: 1px solid rgba(255, 255, 255, 0.08) !important; border-radius: 10px !important; padding: 20px !important; box-shadow: 0 8px 24px rgba(0,0,0,0.45) !important; display: none;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>2. OS Command Injection Bypass Space</span>
<span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(59,130,246,0.08); border: 1px solid rgba(59,130,246,0.2); color: #3b82f6; font-family: monospace;">OS Command</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #3b82f6; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">cat${IFS}/etc/passwd</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button style="background: rgba(59,130,246,0.1); border: 1px solid rgba(59,130,246,0.3); border-radius: 4px; color: #3b82f6; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700; transition: all 0.15s;" onclick="startWebSim('cmdtest')">▶ Run Simulation</button>
</div>
<div id="term-cmdtest" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 90px;">
<span style="color: #3ddc84;">kali$</span> [กดปุ่ม Run Simulation เพื่อส่งคำสั่ง]
</div>
</div>
<div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 8px; padding: 16px; font-size: 0.83rem; color: #cbd5e1; line-height: 1.65;">
<h5 style="margin: 0 0 8px; font-size: 0.85rem; color: #fbbf24; font-weight: bold;">⚙️ Command Description</h5>
<p style="margin: 0;">การเขียนตัวแปร IFS ช่วยเลี่ยงการกรองช่องว่าง ทำให้คำสั่งสามารถรันเพื่อเรียกดูไฟล์ระบบปฏิบัติการได้เหมือนเดิม</p>
</div>
</div>
</div>
</div>
<script>
window.showSandboxItem = function(itemKey, element) {
  const navButtons = document.querySelectorAll('.w-sandbox-nav button');
  navButtons.forEach(btn => {
    btn.style.borderColor = 'rgba(255, 255, 255, 0.06)';
    btn.style.color = '#cbd5e1';
    btn.style.background = 'rgba(255, 255, 255, 0.02)';
  });
  element.style.borderColor = '#3b82f6';
  element.style.color = '#ffffff';
  element.style.background = 'rgba(59, 130, 246, 0.05)';
  const panels = document.querySelectorAll('.w-sand-panel');
  panels.forEach(p => { p.style.display = 'none'; });
  const target = document.getElementById('panel-' + itemKey);
  if (target) { target.style.display = 'block'; }
}
window.startWebSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#ffffff; font-weight:bold;">Executing commands...</span>\\n[.] Verifying backend sanitization checks...';
  setTimeout(() => {
    if (itemKey === 'sqlitest') {
      term.innerHTML = '<span style="color:#64748b;">db-cli$</span> <span style="color:#3ddc84; font-weight:bold;">UNION select output:</span>\\nID: null | User: admin | Pass: <span style="color:#ef4444;">$2y$10$xyzPasswordHash...</span>\\nID: null | User: user1 | Pass: <span style="color:#ef4444;">$2y$10$abcHashUser1...</span>\\n\\n[+] Data exfiltration successful!';
    } else if (itemKey === 'cmdtest') {
      term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#3ddc84; font-weight:bold;">cat /etc/passwd:</span>\\nroot:x:0:0:root:/root:/bin/bash\\nbin:x:1:1:bin:/bin:/sbin/nologin\\n\\n[+] Command completed without spaces.';
    }
  }, 1000);
}
</script>"""

val179_2 = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการบันทึกความสำเร็จและปลดล็อกปุ่มบทเรียนถัดไป:

<div class="row align-items-center" style="margin:1.5rem auto; max-width:980px;"><div class="col-md-8"><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. ช่องโหว่ Cross-Site Scripting (XSS) เกิดจากการลอบฝังแทรกสคริปต์โค้ดประเภทใดเข้ามาทำงานฝั่ง Client Browser?</p><div class="options-container" data-q="q1"><label class="w-quiz-option"><input type="radio" name="xss_lang" value="SQL" data-hash="false">SQL Query code</label><label class="w-quiz-option"><input type="radio" name="xss_lang" value="JavaScript" data-hash="78ec09be8733f52e505820464fdbb19d45388047970d47d457cb146ef279ec3d">JavaScript</label><label class="w-quiz-option"><input type="radio" name="xss_lang" value="Bash" data-hash="false">Bash Shell command</label><label class="w-quiz-option"><input type="radio" name="xss_lang" value="PHP" data-hash="false">PHP Server Script</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. คีย์เวิร์ดมาตรฐาน HTML tag ใดที่นักโจมตีใช้ส่ง XSS Payload เพื่อเปิดจำลองกล่องป๊อปอัพ?</p><div class="options-container" data-q="q2"><label class="w-quiz-option"><input type="radio" name="xss_tag" value="script" data-hash="3a95aa975765796245d8b8ff716d0046522bb33f749eb721867c4e515d18d451"><span>&lt;script&gt;</span></label><label class="w-quiz-option"><input type="radio" name="xss_tag" value="iframe" data-hash="false"><span>&lt;iframe&gt;</span></label><label class="w-quiz-option"><input type="radio" name="xss_tag" value="div" data-hash="false"><span>&lt;div&gt;</span></label><label class="w-quiz-option"><input type="radio" name="xss_tag" value="img" data-hash="false"><span>&lt;img&gt;</span></label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div></div><div class="col-md-4 text-center"><div class="p-4" style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); border-radius:12px; min-height:220px; display:flex; flex-direction:column; justify-content:center; align-items:center;"><span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;">Lesson Progress</span><div class="neon-gauge-container"><svg class="neon-gauge" viewBox="0 0 36 36"><path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><path class="neon-gauge-fill" id="lesson-gauge-fill" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text">0%</text></svg></div><span id="lesson-status-txt" class="mt-3 d-block text-muted" style="font-size:0.78rem;">โปรดตอบคำถามให้ครบ 2 ข้อ</span></div></div></div>
<style>
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:#3b82f6; stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease, stroke 0.5s ease; filter:drop-shadow(0 0 5px rgba(59,130,246,0.5));}
.neon-gauge-text {fill:#ffffff; font-family:\'JetBrains Mono\',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}
</style>
<script>
const lessonKey = 'solved_lesson_179';
function getSavedSolves() { try { return JSON.parse(localStorage.getItem(lessonKey) || '[]'); } catch(e) { return []; } }
function updateLocalProgress() {
  const solved = getSavedSolves();
  const total = 2;
  const percent = Math.round((solved.length / total) * 100);
  const fill = document.getElementById('lesson-gauge-fill');
  const text = document.getElementById('lesson-gauge-text');
  const status = document.getElementById('lesson-status-txt');
  if (fill) fill.setAttribute('stroke-dasharray', `${percent}, 100`);
  if (text) text.textContent = `${percent}%`;
  if (solved.length === total) {
    if (fill) fill.style.stroke = '#3ddc84';
    if (status) status.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
  } else {
    if (fill) fill.style.stroke = '#3b82f6';
    if (status) status.textContent = `ทำเสร็จแล้ว ${solved.length}/${total} ข้อ`;
  }
}
document.addEventListener('click', function(e) {
  const label = e.target.closest('.w-quiz-option');
  if (label) {
    const container = label.closest('.options-container');
    if (container) {
      container.querySelectorAll('.w-quiz-option').forEach(opt => opt.classList.remove('selected'));
      label.classList.add('selected');
      const radio = label.querySelector('input[type="radio"]');
      if (radio) radio.checked = true;
    }
  }
});
window.verifyMultipleChoice = function(button) {
  const cell = button.closest('.question-cell');
  const selectedRadio = cell.querySelector('input[type="radio"]:checked');
  const feedback = cell.querySelector('.feedback-msg');
  if (!selectedRadio) {
    feedback.className = "feedback-msg mt-2 alert-warning py-1.5 px-3 text-dark";
    feedback.innerHTML = '<i class="fas fa-exclamation-triangle mr-1"></i> กรุณาเลือกคำตอบ';
    feedback.style.setProperty('display', 'block', 'important');
    return;
  }
  const hashVal = selectedRadio.getAttribute('data-hash');
  if (hashVal !== 'false') {
    feedback.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
    feedback.innerHTML = '<i class="fas fa-check-circle mr-1"></i> คำตอบถูกต้อง!';
    feedback.style.setProperty('display', 'block', 'important');
    cell.querySelectorAll('input[type="radio"]').forEach(r => r.disabled = true);
    cell.querySelectorAll('.w-quiz-option').forEach(opt => opt.style.pointerEvents = 'none');
    button.disabled = true;
    const solved = getSavedSolves();
    if (!solved.includes(hashVal)) {
      solved.push(hashVal);
      localStorage.setItem(lessonKey, JSON.stringify(solved));
    }
    updateLocalProgress();
  } else {
    feedback.className = "feedback-msg mt-2 alert-danger py-1.5 px-3 text-white bg-danger border-0";
    feedback.innerHTML = '<i class="fas fa-times-circle mr-1"></i> คำตอบไม่ถูกต้อง ลองใหม่!';
    feedback.style.setProperty('display', 'block', 'important');
  }
}
setTimeout(() => {
  const solved = getSavedSolves();
  document.querySelectorAll('.options-container').forEach(container => {
    container.querySelectorAll('input[type="radio"]').forEach(radio => {
      const hash = radio.getAttribute('data-hash');
      if (solved.includes(hash)) {
        radio.checked = true;
        const label = radio.closest('.w-quiz-option');
        if (label) label.classList.add('selected');
        container.querySelectorAll('input[type="radio"]').forEach(r => r.disabled = true);
        container.querySelectorAll('.w-quiz-option').forEach(opt => opt.style.pointerEvents = 'none');
        const cell = container.closest('.question-cell');
        if (cell) {
          const btn = cell.querySelector('button');
          if (btn) btn.disabled = true;
          const fb = cell.querySelector('.feedback-msg');
          if (fb) {
            fb.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
            fb.innerHTML = '<i class="fas fa-check-circle mr-1"></i> เรียบร้อยแล้ว';
            fb.style.setProperty('display', 'block', 'important');
          }
        }
      }
    });
  });
  updateLocalProgress();
}, 200);
</script>"""

save_lesson(179, val179_0, val179_1, val179_2)
ctx.pop()
