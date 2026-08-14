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

# ─── Block 13: separator ───
b_sep4 = "---"

# ─────────────────────────────────────────────────────────────────────────────
# BLOCK 14 — Control-Keys
# ─────────────────────────────────────────────────────────────────────────────
b_ctrl = """### ⌨️ Control-Keys

<style>
.ctrl-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.ctrl-intro{font-size:0.92rem;color:#94a3b8;line-height:1.7;margin-bottom:20px;padding:14px 18px;background:rgba(0,240,255,0.04);border:1px solid rgba(0,240,255,0.1);border-radius:10px;}
.ctrl-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;}
@media(max-width:680px){.ctrl-grid{grid-template-columns:repeat(2,1fr);}}
.ctrl-card{background:rgba(15,17,26,0.5);border:1px solid rgba(255,255,255,0.05);border-radius:10px;padding:16px;transition:all 0.2s;cursor:default;}
.ctrl-card:hover{border-color:rgba(0,240,255,0.2);transform:translateY(-2px);box-shadow:0 6px 20px rgba(0,0,0,0.3);}
.ctrl-keys{display:flex;align-items:center;gap:6px;margin-bottom:10px;}
.ctrl-key{font-family:'JetBrains Mono',monospace;font-size:0.82rem;font-weight:700;padding:4px 10px;border-radius:6px;background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.15);color:#e2e8f0;box-shadow:0 2px 0 rgba(0,0,0,0.4);}
.ctrl-key.ctrl{color:#00f0ff;border-color:rgba(0,240,255,0.3);background:rgba(0,240,255,0.07);}
.ctrl-plus{color:#475569;font-size:0.8rem;}
.ctrl-desc{font-size:0.82rem;color:#94a3b8;line-height:1.5;}
.ctrl-card:hover .ctrl-desc{color:#cbd5e1;}
</style>

<div class="ctrl-wrap">
<div class="ctrl-intro">
<strong style="color:#00f0ff;">Control-key</strong> คือแป้นพิมพ์ลัด (Keyboard Shortcut) ที่ใช้ร่วมกับปุ่ม <code>Ctrl</code> เพื่อควบคุมการทำงานของ Terminal และ Shell โดยไม่ต้องใช้เมาส์ มีความสำคัญมากสำหรับ Text-based Interface
</div>
<div class="ctrl-grid">
<div class="ctrl-card">
<div class="ctrl-keys"><span class="ctrl-key ctrl">Ctrl</span><span class="ctrl-plus">+</span><span class="ctrl-key">S</span></div>
<div class="ctrl-desc">หยุดการแสดงผลบนหน้าจอชั่วคราว (Freeze / Pause screen output)</div>
</div>
<div class="ctrl-card">
<div class="ctrl-keys"><span class="ctrl-key ctrl">Ctrl</span><span class="ctrl-plus">+</span><span class="ctrl-key">Q</span></div>
<div class="ctrl-desc">เปิดการแสดงผลอีกครั้งหลังจาก Ctrl-S (Unfreeze screen)</div>
</div>
<div class="ctrl-card">
<div class="ctrl-keys"><span class="ctrl-key ctrl">Ctrl</span><span class="ctrl-plus">+</span><span class="ctrl-key">C</span></div>
<div class="ctrl-desc">หยุดโปรแกรมที่กำลังทำงานอยู่ทันที (Interrupt / Kill running program)</div>
</div>
<div class="ctrl-card">
<div class="ctrl-keys"><span class="ctrl-key ctrl">Ctrl</span><span class="ctrl-plus">+</span><span class="ctrl-key">Z</span></div>
<div class="ctrl-desc">หยุดโปรแกรมพักไว้ชั่วคราว (Suspend) เพื่อกลับมาทำงานทีหลัง</div>
</div>
<div class="ctrl-card">
<div class="ctrl-keys"><span class="ctrl-key ctrl">Ctrl</span><span class="ctrl-plus">+</span><span class="ctrl-key">H</span></div>
<div class="ctrl-desc">ลบตัวอักษรสุดท้ายที่พิมพ์ไป (Delete last character typed)</div>
</div>
<div class="ctrl-card">
<div class="ctrl-keys"><span class="ctrl-key ctrl">Ctrl</span><span class="ctrl-plus">+</span><span class="ctrl-key">W</span></div>
<div class="ctrl-desc">ลบคำสุดท้ายที่พิมพ์ไปทั้งคำ (Delete last word typed)</div>
</div>
<div class="ctrl-card">
<div class="ctrl-keys"><span class="ctrl-key ctrl">Ctrl</span><span class="ctrl-plus">+</span><span class="ctrl-key">U</span></div>
<div class="ctrl-desc">ลบทั้งบรรทัดที่กำลังพิมพ์อยู่ (Delete entire current line)</div>
</div>
<div class="ctrl-card">
<div class="ctrl-keys"><span class="ctrl-key ctrl">Ctrl</span><span class="ctrl-plus">+</span><span class="ctrl-key">D</span></div>
<div class="ctrl-desc">สิ้นสุดการรับข้อความ / ส่งสัญญาณ End-of-File (EOF) ให้กับโปรแกรม</div>
</div>
</div>
</div>"""

# ─────────────────────────────────────────────────────────────────────────────
# BLOCK 15 — Redirections + Environment Variables (combined)
# ─────────────────────────────────────────────────────────────────────────────
b_redir_env = """### 🔀 Redirections & 🌐 Environment Variables

<style>
.re-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:24px;}
.re-card{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,0.2);}
.re-card-header{padding:14px 20px;border-bottom:1px solid rgba(255,255,255,0.05);}
.re-card-header h4{margin:0 0 4px;font-size:0.95rem;font-weight:700;color:#ffffff;}
.re-card-header p{margin:0;font-size:0.82rem;color:#64748b;line-height:1.5;}
.re-table{width:100%;border-collapse:collapse;}
.re-table th{padding:10px 16px;text-align:left;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.08em;font-weight:700;color:#8a94a6;background:rgba(255,255,255,0.01);border-bottom:1px solid rgba(255,255,255,0.05);}
.re-table td{padding:12px 16px;border-bottom:1px solid rgba(255,255,255,0.04);font-size:0.9rem;vertical-align:top;line-height:1.6;}
.re-table tr:last-child td{border-bottom:none;}
.re-table tr:hover td{background:rgba(255,255,255,0.02);}
.re-table td:first-child{font-family:'JetBrains Mono',monospace;font-size:1rem;font-weight:800;text-align:center;width:60px;}
.re-table td:last-child{color:#94a3b8;}
.sym-out{color:#fbbf24;}.sym-app{color:#fb923c;}.sym-in{color:#3ddc84;}.sym-pipe{color:#ab20fd;}.sym-bg{color:#f472b6;}.sym-eq{color:#00f0ff;}
.ex-inline{display:inline-block;font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#fbbf24;background:rgba(251,191,36,0.07);border:1px solid rgba(251,191,36,0.2);padding:1px 6px;border-radius:4px;margin-top:4px;}
.env-var{font-family:'JetBrains Mono',monospace;font-size:0.88rem;color:#3ddc84;font-weight:700;}
.env-val{font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#64748b;}
</style>

<div class="re-wrap">

<div class="re-card">
<div class="re-card-header">
<h4>🔀 Redirection Characters</h4>
<p>เปลี่ยนทิศทาง Input/Output ของคำสั่ง — จากไฟล์ไปยังโปรแกรม หรือระหว่างโปรแกรม</p>
</div>
<table class="re-table">
<tr><th>Symbol</th><th>Description</th></tr>
<tr><td class="sym-out">&gt;</td><td>ส่ง output ของคำสั่งซ้ายไปเขียนทับลงในไฟล์ทางขวา (overwrite)<div class="ex-inline">ls -l &gt; output.txt</div></td></tr>
<tr><td class="sym-app">&gt;&gt;</td><td>ส่ง output ของคำสั่งซ้ายไปต่อท้ายไฟล์ทางขวา (append ไม่ลบข้อมูลเดิม)<div class="ex-inline">echo "hello" &gt;&gt; log.txt</div></td></tr>
<tr><td class="sym-in">&lt;</td><td>ส่งเนื้อหาของไฟล์ทางขวาเป็น input ให้คำสั่งทางซ้าย<div class="ex-inline">sort &lt; names.txt</div></td></tr>
<tr><td class="sym-pipe">|</td><td>ส่ง output ของคำสั่งซ้ายเป็น input ให้คำสั่งขวา (Pipe) ทำงานเป็นลำดับ<div class="ex-inline">cat file.txt | grep "flag"</div></td></tr>
<tr><td class="sym-bg">&amp;</td><td>รันคำสั่งซ้ายและขวาพร้อมกันในเวลาเดียวกัน (Background + Concurrent)<div class="ex-inline">ping 8.8.8.8 &amp; nmap 192.168.1.1</div></td></tr>
</table>
</div>

<div class="re-card">
<div class="re-card-header">
<h4>🌐 Environment Variables</h4>
<p>ตัวแปรสภาพแวดล้อมที่ระบบจัดเก็บไว้สำหรับใช้โดย Shell และโปรแกรมต่างๆ — ดูค่าได้ด้วย <code style="color:#00f0ff;">echo $VAR</code></p>
</div>
<table class="re-table">
<tr><th>Variable</th><th>Description & Example</th></tr>
<tr><td class="env-var">$HOME</td><td>เส้นทาง home directory ของผู้ใช้ปัจจุบัน<div class="env-val">e.g. /root</div></td></tr>
<tr><td class="env-var">$LOGNAME</td><td>ชื่อ username ที่ใช้ login เข้าระบบ<div class="env-val">e.g. root</div></td></tr>
<tr><td class="env-var">$SHELL</td><td>เส้นทาง Shell ที่กำลังใช้งานอยู่ในระบบ<div class="env-val">e.g. /bin/bash</div></td></tr>
<tr><td class="env-var">$USER</td><td>ชื่อ username ของผู้ใช้ปัจจุบัน<div class="env-val">e.g. root</div></td></tr>
<tr><td class="env-var">$PATH</td><td>รายการเส้นทางที่ Shell ค้นหาคำสั่งตามลำดับ คั่นด้วย <code>:</code><div class="env-val">e.g. /usr/bin:/usr/local/bin:/usr/sbin</div></td></tr>
<tr><td class="env-var">$TERM</td><td>ประเภทของ Terminal ที่กำลังใช้งาน<div class="env-val">e.g. xterm-256color</div></td></tr>
<tr><td class="env-var">$LANG</td><td>การเข้ารหัสภาษาปัจจุบันของระบบ (Language Encoding)<div class="env-val">e.g. en_US.UTF-8</div></td></tr>
<tr><td class="env-var">$EDITOR</td><td>โปรแกรม text editor เริ่มต้นของระบบ<div class="env-val">e.g. nano, vim</div></td></tr>
<tr><td class="env-var">$MAIL</td><td>เส้นทางที่จัดเก็บ mail ของผู้ใช้ปัจจุบัน<div class="env-val">e.g. /var/mail/root</div></td></tr>
</table>
</div>

</div>"""

# ─────────────────────────────────────────────────────────────────────────────
# BLOCK 16 — Regular Expressions + Wildcards
# ─────────────────────────────────────────────────────────────────────────────
b_regex = """### 🔎 Regular Expressions & Wildcards

<style>
.rx-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:24px;}
.rx-card{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,0.2);}
.rx-card-header{padding:14px 20px;border-bottom:1px solid rgba(255,255,255,0.05);}
.rx-card-header h4{margin:0 0 4px;font-size:0.95rem;font-weight:700;color:#ffffff;}
.rx-card-header p{margin:0;font-size:0.82rem;color:#64748b;line-height:1.5;}
.rx-table{width:100%;border-collapse:collapse;}
.rx-table th{padding:10px 16px;text-align:left;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.08em;font-weight:700;color:#8a94a6;background:rgba(255,255,255,0.01);border-bottom:1px solid rgba(255,255,255,0.05);}
.rx-table td{padding:11px 16px;border-bottom:1px solid rgba(255,255,255,0.04);font-size:0.9rem;vertical-align:top;line-height:1.6;}
.rx-table tr:last-child td{border-bottom:none;}
.rx-table tr:hover td{background:rgba(255,255,255,0.02);}
.rx-table td:first-child{font-family:'JetBrains Mono',monospace;font-size:0.92rem;font-weight:700;color:#fbbf24;white-space:nowrap;}
.rx-table td:last-child{color:#94a3b8;}
/* Example table */
.rx-ex-table{width:100%;border-collapse:collapse;}
.rx-ex-table th{padding:10px 16px;text-align:left;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.08em;font-weight:700;color:#8a94a6;background:rgba(255,255,255,0.01);border-bottom:1px solid rgba(255,255,255,0.05);}
.rx-ex-table td{padding:10px 16px;border-bottom:1px solid rgba(255,255,255,0.04);font-size:0.88rem;vertical-align:middle;font-family:'JetBrains Mono',monospace;}
.rx-ex-table tr:last-child td{border-bottom:none;}
.rx-ex-table tr:hover td{background:rgba(255,255,255,0.02);}
.rx-pat{color:#fbbf24;font-weight:700;}
.str-wrap{display:flex;flex-wrap:wrap;gap:6px;}
.str-item{padding:3px 8px;border-radius:5px;font-size:0.8rem;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);color:#475569;}
.str-item.match{background:rgba(255,0,127,0.12);border-color:rgba(255,0,127,0.3);color:#ff007f;font-weight:700;}
/* Wildcard card */
.wc-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;padding:16px;}
@media(max-width:680px){.wc-grid{grid-template-columns:1fr;}}
.wc-card{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:16px;}
.wc-sym{font-family:'JetBrains Mono',monospace;font-size:1.8rem;font-weight:900;margin-bottom:8px;}
.wc-name{font-size:0.75rem;text-transform:uppercase;letter-spacing:0.1em;font-weight:700;margin-bottom:6px;opacity:0.7;}
.wc-desc{font-size:0.82rem;color:#94a3b8;line-height:1.5;margin-bottom:10px;}
.wc-eg-label{font-size:0.72rem;color:#475569;margin-bottom:4px;}
.wc-eg{font-family:'JetBrains Mono',monospace;font-size:0.8rem;line-height:1.7;}
.wc-cmd{color:#00f0ff;}.wc-out{color:#3ddc84;}.wc-dim{color:#334155;}
.wc-star .wc-sym,.wc-star .wc-name{color:#fbbf24;}
.wc-star{border-color:rgba(251,191,36,0.15);}
.wc-q .wc-sym,.wc-q .wc-name{color:#ab20fd;}
.wc-q{border-color:rgba(171,32,253,0.15);}
.wc-br .wc-sym,.wc-br .wc-name{color:#00f0ff;}
.wc-br{border-color:rgba(0,240,255,0.15);}
</style>

<div class="rx-wrap">

<!-- Regex Reference -->
<div class="rx-card">
<div class="rx-card-header">
<h4>🔎 Regular Expression (Regex) — ตารางอ้างอิง</h4>
<p>ลำดับตัวอักษรที่ระบุ pattern สำหรับค้นหาข้อความ ใช้กับคำสั่ง <code style="color:#fbbf24;">grep</code> และ <code style="color:#fbbf24;">find</code></p>
</div>
<table class="rx-table">
<tr><th>Regex</th><th>Description</th></tr>
<tr><td>.</td><td>จับคู่กับอักขระ <strong>ตัวใดก็ได้ 1 ตัว</strong> ยกเว้น newline<br><span style="color:#64748b;font-size:0.8rem;">เช่น <code>.at</code> → hat, cat, bat, 4at ...</span></td></tr>
<tr><td>?</td><td>จับคู่กับอักขระก่อนหน้า <strong>0 หรือ 1 ครั้ง</strong></td></tr>
<tr><td>*</td><td>จับคู่กับอักขระก่อนหน้า <strong>0 ครั้งขึ้นไป</strong> (zero or more)</td></tr>
<tr><td>+</td><td>จับคู่กับอักขระก่อนหน้า <strong>1 ครั้งขึ้นไป</strong> (one or more)</td></tr>
<tr><td>[abc]</td><td>จับคู่กับอักขระ <strong>ตัวใดตัวหนึ่งในวงเล็บ</strong> (Set)<br><span style="color:#64748b;font-size:0.8rem;">เช่น <code>[hc]at</code> → hat, cat</span></td></tr>
<tr><td>[a-d]</td><td>จับคู่กับอักขระ <strong>ในช่วงที่กำหนด</strong> (Range)<br><span style="color:#64748b;font-size:0.8rem;">เช่น <code>[a-d]</code> → a, b, c, d</span></td></tr>
<tr><td>[^abc]</td><td>จับคู่กับอักขระ <strong>ที่ไม่อยู่ในวงเล็บ</strong> (Negation)<br><span style="color:#64748b;font-size:0.8rem;">เช่น <code>[^b]at</code> → hat, cat, 4at ...</span></td></tr>
<tr><td>^abc</td><td>จับคู่เฉพาะบรรทัดที่ <strong>ขึ้นต้นด้วย</strong> pattern ที่ระบุ</td></tr>
<tr><td>abc$</td><td>จับคู่เฉพาะบรรทัดที่ <strong>ลงท้ายด้วย</strong> pattern ที่ระบุ</td></tr>
<tr><td>abc|def</td><td>จับคู่กับ pattern <strong>ใดก็ได้ในสองฝั่ง</strong> (OR)<br><span style="color:#64748b;font-size:0.8rem;">เช่น <code>cat|alt</code> → cat หรือ alt</span></td></tr>
<tr><td>{m,n}</td><td>จับคู่กับอักขระก่อนหน้า <strong>อย่างน้อย m ครั้ง และไม่เกิน n ครั้ง</strong></td></tr>
</table>
</div>

<!-- Regex Examples -->
<div class="rx-card">
<div class="rx-card-header">
<h4>📋 Regex Examples — สตริงที่ตรงกัน (highlighted)</h4>
<p>ตัวอย่างชุด: <code style="color:#94a3b8;">"hat", "cat", "bat", "4at", "#at", " at", "a t", "alt"</code> — <span style="color:#ff007f;">สีแดง</span> = ตรงกับ pattern</p>
</div>
<table class="rx-ex-table">
<tr><th>Regex</th><th>Matching Strings</th></tr>
<tr>
<td class="rx-pat">.at</td>
<td><div class="str-wrap">
<span class="str-item match">hat</span><span class="str-item match">cat</span><span class="str-item match">bat</span><span class="str-item match">4at</span><span class="str-item match">#at</span><span class="str-item match">&nbsp;at</span><span class="str-item">a t</span><span class="str-item">alt</span>
</div></td>
</tr>
<tr>
<td class="rx-pat">[hc]at</td>
<td><div class="str-wrap">
<span class="str-item match">hat</span><span class="str-item match">cat</span><span class="str-item">bat</span><span class="str-item">4at</span><span class="str-item">#at</span><span class="str-item">&nbsp;at</span><span class="str-item">a t</span><span class="str-item">alt</span>
</div></td>
</tr>
<tr>
<td class="rx-pat">[^b]at</td>
<td><div class="str-wrap">
<span class="str-item match">hat</span><span class="str-item match">cat</span><span class="str-item">bat</span><span class="str-item match">4at</span><span class="str-item match">#at</span><span class="str-item match">&nbsp;at</span><span class="str-item">a t</span><span class="str-item">alt</span>
</div></td>
</tr>
<tr>
<td class="rx-pat">[^hc]at</td>
<td><div class="str-wrap">
<span class="str-item">hat</span><span class="str-item">cat</span><span class="str-item match">bat</span><span class="str-item match">4at</span><span class="str-item match">#at</span><span class="str-item match">&nbsp;at</span><span class="str-item">a t</span><span class="str-item">alt</span>
</div></td>
</tr>
<tr>
<td class="rx-pat">cat|alt</td>
<td><div class="str-wrap">
<span class="str-item">hat</span><span class="str-item match">cat</span><span class="str-item">bat</span><span class="str-item">4at</span><span class="str-item">#at</span><span class="str-item">&nbsp;at</span><span class="str-item">a t</span><span class="str-item match">alt</span>
</div></td>
</tr>
<tr>
<td class="rx-pat">[a&nbsp;t]{3}</td>
<td><div class="str-wrap">
<span class="str-item">hat</span><span class="str-item">cat</span><span class="str-item">bat</span><span class="str-item">4at</span><span class="str-item">#at</span><span class="str-item match">&nbsp;at</span><span class="str-item match">a t</span><span class="str-item">alt</span>
</div></td>
</tr>
<tr>
<td class="rx-pat">[a-t]{3}</td>
<td><div class="str-wrap">
<span class="str-item match">hat</span><span class="str-item match">cat</span><span class="str-item match">bat</span><span class="str-item">4at</span><span class="str-item">#at</span><span class="str-item">&nbsp;at</span><span class="str-item">a t</span><span class="str-item match">alt</span>
</div></td>
</tr>
<tr>
<td class="rx-pat">[a-ct]{3,}</td>
<td><div class="str-wrap">
<span class="str-item">hat</span><span class="str-item match">cat</span><span class="str-item match">bat</span><span class="str-item">4at</span><span class="str-item">#at</span><span class="str-item">&nbsp;at</span><span class="str-item">a t</span><span class="str-item">alt</span>
</div></td>
</tr>
</table>
</div>

<!-- Wildcards -->
<div class="rx-card">
<div class="rx-card-header">
<h4>🃏 Wildcard Characters — ตัวแทนอักขระใน Shell Commands</h4>
<p>Wildcard คือตัวอักษรพิเศษที่ใช้แทนตัวอักษรอื่นๆ ใน Shell commands เช่น <code>ls</code>, <code>find</code>, <code>cp</code> ต่างจาก Regex ตรงที่ Wildcard ใช้กับ <strong>ชื่อไฟล์และ path</strong> โดยตรง</p>
</div>
<div class="wc-grid">
<div class="wc-card wc-star">
<div class="wc-sym">*</div>
<div class="wc-name">Asterisk — Zero or More</div>
<div class="wc-desc">แทนอักขระ <strong>ตัวใดก็ได้จำนวนเท่าใดก็ได้</strong> รวมถึงไม่มีอักขระเลย</div>
<div class="wc-eg-label">ตัวอย่าง:</div>
<div class="wc-eg">
<div><span class="wc-cmd">ls *.txt</span></div>
<div><span class="wc-out">→ file.txt, notes.txt, log.txt</span></div>
<div style="margin-top:4px;"><span class="wc-cmd">ls report_*</span></div>
<div><span class="wc-out">→ report_2023, report_final</span></div>
</div>
</div>
<div class="wc-card wc-q">
<div class="wc-sym">?</div>
<div class="wc-name">Question Mark — Exactly One</div>
<div class="wc-desc">แทนอักขระ <strong>ตัวใดก็ได้ 1 ตัวเท่านั้น</strong> (ไม่สามารถเป็นศูนย์ได้)</div>
<div class="wc-eg-label">ตัวอย่าง:</div>
<div class="wc-eg">
<div><span class="wc-cmd">ls file?.txt</span></div>
<div><span class="wc-out">→ file1.txt, fileA.txt</span></div>
<div><span class="wc-dim">✗ file10.txt (2 chars)</span></div>
<div style="margin-top:4px;"><span class="wc-cmd">ls log_??_2023</span></div>
<div><span class="wc-out">→ log_01_2023, log_AB_2023</span></div>
</div>
</div>
<div class="wc-card wc-br">
<div class="wc-sym">[]</div>
<div class="wc-name">Brackets — Character Set</div>
<div class="wc-desc">แทนอักขระ <strong>ตัวใดตัวหนึ่งในวงเล็บ</strong> ใช้ range หรือ negation ได้</div>
<div class="wc-eg-label">ตัวอย่าง:</div>
<div class="wc-eg">
<div><span class="wc-cmd">ls [abc]*.sh</span></div>
<div><span class="wc-out">→ attack.sh, backup.sh, crack.sh</span></div>
<div style="margin-top:4px;"><span class="wc-cmd">ls [0-9]*.txt</span></div>
<div><span class="wc-out">→ 1_log.txt, 9_data.txt</span></div>
<div><span class="wc-dim">✗ abc.txt (starts with letter)</span></div>
</div>
</div>
</div>
</div>

</div>"""

# Append new blocks
new_blocks = [
    {"type": "markdown", "value": b_sep4},
    {"type": "markdown", "value": b_ctrl},
    {"type": "markdown", "value": b_redir_env},
    {"type": "markdown", "value": b_regex},
]
blocks.extend(new_blocks)

lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=166).update({"content": lesson.content})
db.session.commit()

print(f"Control-Keys, Redirections, Env Vars, Regex & Wildcards appended! Total blocks: {len(blocks)}")
for i, b in enumerate(blocks[-5:], start=len(blocks)-5):
    print(f"  Block {i}: {len(b['value'])} chars")
