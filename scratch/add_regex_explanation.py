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

# Re-build block 16 with explanation column added to regex examples table
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
.rx-ex-table{width:100%;border-collapse:collapse;}
.rx-ex-table th{padding:10px 16px;text-align:left;font-size:0.78rem;text-transform:uppercase;letter-spacing:0.08em;font-weight:700;color:#8a94a6;background:rgba(255,255,255,0.01);border-bottom:1px solid rgba(255,255,255,0.05);}
.rx-ex-table td{padding:10px 16px;border-bottom:1px solid rgba(255,255,255,0.04);font-size:0.88rem;vertical-align:middle;}
.rx-ex-table tr:last-child td{border-bottom:none;}
.rx-ex-table tr:hover td{background:rgba(255,255,255,0.02);}
.rx-ex-table td:first-child{font-family:'JetBrains Mono',monospace;font-weight:700;color:#fbbf24;white-space:nowrap;width:130px;}
.rx-ex-table td:nth-child(2){width:280px;}
.rx-ex-table td:nth-child(3){color:#94a3b8;font-size:0.83rem;line-height:1.55;}
.str-wrap{display:flex;flex-wrap:wrap;gap:5px;}
.str-item{padding:3px 8px;border-radius:5px;font-size:0.78rem;font-family:'JetBrains Mono',monospace;background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);color:#475569;}
.str-item.match{background:rgba(255,0,127,0.12);border-color:rgba(255,0,127,0.35);color:#ff007f;font-weight:700;}
.rx-hl{color:#fbbf24;font-weight:700;font-family:'JetBrains Mono',monospace;}
.rx-no{color:#ff007f;font-family:'JetBrains Mono',monospace;}
.rx-yes{color:#3ddc84;font-family:'JetBrains Mono',monospace;}
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
<tr><td>[abc]</td><td>จับคู่กับอักขระ <strong>ตัวใดตัวหนึ่งในวงเล็บ</strong> (Set)<br><span style="color:#64748b;font-size:0.8rem;">เช่น <code>[hc]at</code> → hat, cat เท่านั้น</span></td></tr>
<tr><td>[a-d]</td><td>จับคู่กับอักขระ <strong>ในช่วงที่กำหนด</strong> (Range a ถึง d)<br><span style="color:#64748b;font-size:0.8rem;">เช่น <code>[a-d]</code> → a, b, c, d</span></td></tr>
<tr><td>[^abc]</td><td>จับคู่กับอักขระ <strong>ที่ไม่อยู่ในวงเล็บ</strong> (Negation)<br><span style="color:#64748b;font-size:0.8rem;">เช่น <code>[^b]at</code> → hat, cat, 4at ... (ไม่รวม bat)</span></td></tr>
<tr><td>^abc</td><td>จับคู่เฉพาะบรรทัดที่ <strong>ขึ้นต้นด้วย</strong> pattern ที่ระบุ</td></tr>
<tr><td>abc$</td><td>จับคู่เฉพาะบรรทัดที่ <strong>ลงท้ายด้วย</strong> pattern ที่ระบุ</td></tr>
<tr><td>abc|def</td><td>จับคู่กับ pattern <strong>ใดก็ได้ในสองฝั่ง</strong> (OR)<br><span style="color:#64748b;font-size:0.8rem;">เช่น <code>cat|alt</code> → cat หรือ alt</span></td></tr>
<tr><td>{m,n}</td><td>จับคู่กับอักขระก่อนหน้า <strong>อย่างน้อย m ครั้ง และไม่เกิน n ครั้ง</strong></td></tr>
</table>
</div>

<div class="rx-card">
<div class="rx-card-header">
<h4>📋 Regex Examples — สตริงที่ตรงกัน พร้อมคำอธิบาย</h4>
<p>ชุดทดสอบ: <code style="color:#94a3b8;">"hat"&nbsp;&nbsp;"cat"&nbsp;&nbsp;"bat"&nbsp;&nbsp;"4at"&nbsp;&nbsp;"#at"&nbsp;&nbsp;" at"&nbsp;&nbsp;"a t"&nbsp;&nbsp;"alt"</code> — <span style="color:#ff007f;font-weight:700;">สีแดง</span> = ตรงกับ pattern</p>
</div>
<table class="rx-ex-table">
<tr><th>Regex</th><th>Matching Strings</th><th>คำอธิบาย</th></tr>
<tr>
<td>.at</td>
<td><div class="str-wrap"><span class="str-item match">hat</span><span class="str-item match">cat</span><span class="str-item match">bat</span><span class="str-item match">4at</span><span class="str-item match">#at</span><span class="str-item match">&nbsp;at</span><span class="str-item">a t</span><span class="str-item">alt</span></div></td>
<td><span class="rx-hl">.</span> = ตัวใดก็ได้ 1 ตัว ตามด้วย <span class="rx-hl">at</span><br><span class="rx-no">✗ "a t"</span> — ตรงกลางเป็น space แต่ลงท้ายด้วย t ไม่ใช่ at<br><span class="rx-no">✗ "alt"</span> — ลงท้ายด้วย lt ไม่ใช่ at</td>
</tr>
<tr>
<td>[hc]at</td>
<td><div class="str-wrap"><span class="str-item match">hat</span><span class="str-item match">cat</span><span class="str-item">bat</span><span class="str-item">4at</span><span class="str-item">#at</span><span class="str-item">&nbsp;at</span><span class="str-item">a t</span><span class="str-item">alt</span></div></td>
<td>ตัวแรกต้องเป็น <span class="rx-hl">h</span> หรือ <span class="rx-hl">c</span> เท่านั้น ตามด้วย <span class="rx-hl">at</span><br><span class="rx-yes">✓ hat</span> (h ∈ {h,c}), <span class="rx-yes">✓ cat</span> (c ∈ {h,c})<br><span class="rx-no">✗ bat</span> (b ∉ {h,c})</td>
</tr>
<tr>
<td>[^b]at</td>
<td><div class="str-wrap"><span class="str-item match">hat</span><span class="str-item match">cat</span><span class="str-item">bat</span><span class="str-item match">4at</span><span class="str-item match">#at</span><span class="str-item match">&nbsp;at</span><span class="str-item">a t</span><span class="str-item">alt</span></div></td>
<td>ตัวแรก <strong>ต้องไม่ใช่</strong> <span class="rx-hl">b</span> ตามด้วย <span class="rx-hl">at</span><br><span class="rx-no">✗ bat</span> — b ถูกยกเว้นด้วย [^b]<br><span class="rx-no">✗ "a t", "alt"</span> — ไม่ลงท้ายด้วย at</td>
</tr>
<tr>
<td>[^hc]at</td>
<td><div class="str-wrap"><span class="str-item">hat</span><span class="str-item">cat</span><span class="str-item match">bat</span><span class="str-item match">4at</span><span class="str-item match">#at</span><span class="str-item match">&nbsp;at</span><span class="str-item">a t</span><span class="str-item">alt</span></div></td>
<td>ตัวแรก <strong>ต้องไม่ใช่</strong> <span class="rx-hl">h</span> หรือ <span class="rx-hl">c</span> ตามด้วย <span class="rx-hl">at</span><br><span class="rx-no">✗ hat</span> (h ถูกยกเว้น), <span class="rx-no">✗ cat</span> (c ถูกยกเว้น)<br><span class="rx-yes">✓ bat, 4at, #at, &nbsp;at</span></td>
</tr>
<tr>
<td>cat|alt</td>
<td><div class="str-wrap"><span class="str-item">hat</span><span class="str-item match">cat</span><span class="str-item">bat</span><span class="str-item">4at</span><span class="str-item">#at</span><span class="str-item">&nbsp;at</span><span class="str-item">a t</span><span class="str-item match">alt</span></div></td>
<td>ต้องเป็น <span class="rx-hl">cat</span> หรือ <span class="rx-hl">alt</span> ทั้งคำเท่านั้น (OR)<br><span class="rx-yes">✓ cat</span> — ตรงทั้งคำ<br><span class="rx-yes">✓ alt</span> — ตรงทั้งคำ<br><span class="rx-no">✗ ที่เหลือ</span> — ไม่ตรงกับ pattern ใดเลย</td>
</tr>
<tr>
<td>[a&nbsp;t]{3}</td>
<td><div class="str-wrap"><span class="str-item">hat</span><span class="str-item">cat</span><span class="str-item">bat</span><span class="str-item">4at</span><span class="str-item">#at</span><span class="str-item match">&nbsp;at</span><span class="str-item match">a t</span><span class="str-item">alt</span></div></td>
<td>ชุดอักขระที่ยอมรับคือ <span class="rx-hl">{a, space, t}</span> เท่านั้น ต้องมีพอดี 3 ตัว<br><span class="rx-yes">✓ " at"</span> — space, a, t ∈ {a,sp,t}<br><span class="rx-yes">✓ "a t"</span> — a, space, t ∈ {a,sp,t}<br><span class="rx-no">✗ alt</span> — l ∉ {a,sp,t}</td>
</tr>
<tr>
<td>[a-t]{3}</td>
<td><div class="str-wrap"><span class="str-item match">hat</span><span class="str-item match">cat</span><span class="str-item match">bat</span><span class="str-item">4at</span><span class="str-item">#at</span><span class="str-item">&nbsp;at</span><span class="str-item">a t</span><span class="str-item match">alt</span></div></td>
<td>ทุกตัวต้องอยู่ในช่วง <span class="rx-hl">a–t</span> (ASCII) พอดี 3 ตัว<br><span class="rx-yes">✓ hat, cat, bat, alt</span> — h,c,b,l ∈ [a-t]<br><span class="rx-no">✗ 4at</span> (4 ∉ a-t), <span class="rx-no">✗ #at</span> (# ∉ a-t)<br><span class="rx-no">✗ " at"</span> (space ∉ a-t), <span class="rx-no">✗ "a t"</span> (space ∉ a-t)</td>
</tr>
<tr>
<td>[a-ct]{3,}</td>
<td><div class="str-wrap"><span class="str-item">hat</span><span class="str-item match">cat</span><span class="str-item match">bat</span><span class="str-item">4at</span><span class="str-item">#at</span><span class="str-item">&nbsp;at</span><span class="str-item">a t</span><span class="str-item">alt</span></div></td>
<td>ชุด <span class="rx-hl">{a,b,c,t}</span> เท่านั้น อย่างน้อย 3 ตัวขึ้นไป<br><span class="rx-yes">✓ cat</span> — c,a,t ∈ {a,b,c,t}<br><span class="rx-yes">✓ bat</span> — b,a,t ∈ {a,b,c,t}<br><span class="rx-no">✗ hat</span> (h ∉ set), <span class="rx-no">✗ alt</span> (l ∉ set)</td>
</tr>
</table>
</div>

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

blocks[16]['value'] = b_regex
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=166).update({"content": lesson.content})
db.session.commit()
print("Block 16 updated: explanation column added to regex examples table!")
