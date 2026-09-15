from CTFd import create_app
from CTFd.utils import markdown

# Load SVG
with open('/home/kali/crru_ctf/CTFd/test_sqli_animated_explainer.py', 'r') as f:
    text = f.read()
    s = text.find('svg_code = """') + len('svg_code = """')
    e = text.find('"""\n\nrendered')
    svg_raw = text[s:e].strip()

# Load Payloads & SQLMap from previous test
with open('/home/kali/crru_ctf/CTFd/test_sqli_lesson_content.py', 'r') as f:
    text = f.read()
    p2_s = text.find('<!-- ========================================== -->\n<!-- 2. SQL INJECTION PAYLOAD ARSENAL TABLE -->')
    p2_e = text.find('combined_html =')
    payloads_and_sqlmap_raw = text[p2_s:p2_e].replace('"""', '').strip()

full_content = [
'<!-- ========================================== -->',
'<!-- 1. SQL INJECTION CONCEPTUAL HERO & ANIMATED VECTOR -->',
'<!-- ========================================== -->',
'<div style="margin: 2rem auto 2.5rem; max-width: 1050px; background: linear-gradient(135deg, rgba(8, 14, 30, 0.98) 0%, rgba(15, 23, 42, 0.98) 100%); border: 1px solid rgba(244, 63, 94, 0.3); border-radius: 18px; box-shadow: 0 16px 45px rgba(0, 0, 0, 0.7), 0 0 30px rgba(244, 63, 94, 0.12); overflow: hidden;">',
'<div style="height: 4px; background: linear-gradient(90deg, #f43f5e, #ec4899, #8b5cf6, #00f0ff);"></div>',

'<div style="padding: 24px 28px 18px; border-bottom: 1px solid rgba(255, 255, 255, 0.08);">',
'<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; margin-bottom: 14px;">',
'<div style="display: flex; align-items: center; gap: 12px;">',
'<div style="width: 46px; height: 46px; border-radius: 12px; background: rgba(244, 63, 94, 0.15); color: #f43f5e; border: 1px solid rgba(244, 63, 94, 0.4); display: flex; align-items: center; justify-content: center; font-size: 1.4rem; box-shadow: 0 0 20px rgba(244, 63, 94, 0.25); flex-shrink: 0;">',
'<i class="fas fa-database"></i>',
'</div>',
'<div>',
'<h3 style="margin: 0; color: #ffffff; font-size: 1.35rem; font-weight: 800; letter-spacing: -0.02em;">',
'🗄️ SQL Injections (SQLi) — ทฤษฎี กลไก และการเจาะระบบฐานข้อมูลเชิงความเข้าใจ',
'</h3>',
'<span style="color: #94a3b8; font-size: 0.82rem;">Chapter 5: Web Exploitations &bull; เอกสารประกอบการสอนวิชาความมั่นคงปลอดภัยเว็บ (Copyright &copy; 2026 By Wongyos Keardsri)</span>',
'</div>',
'</div>',
'<div style="display: flex; gap: 8px; flex-wrap: wrap;">',
'<span style="background: rgba(239, 68, 68, 0.15); color: #fca5a5; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 14px; border-radius: 20px; border: 1px solid rgba(239, 68, 68, 0.35);">',
'OWASP A03: INJECTION',
'</span>',
'<span style="background: rgba(0, 240, 255, 0.15); color: #7dd3fc; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 14px; border-radius: 20px; border: 1px solid rgba(0, 240, 255, 0.35);">',
'CWE-89: SQL INJECTION',
'</span>',
'</div>',
'</div>',

'<div style="background: rgba(15, 23, 42, 0.8); border: 1px solid rgba(0, 240, 255, 0.25); border-left: 4px solid #00f0ff; border-radius: 12px; padding: 14px 18px; margin-bottom: 18px;">',
'<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px;">',
'<span style="font-size: 1.3rem;">🍕</span>',
'<strong style="color: #00f0ff; font-size: 0.95rem;">',
'อุปมาอุปไมยให้เห็นภาพใน 30 วินาที: "เมื่อข้อความธรรมดากลายร่างเป็นระเบิดคำสั่ง" (Data vs Code Confusion)',
'</strong>',
'</div>',
'<p style="color: #cbd5e1; font-size: 0.86rem; line-height: 1.7; margin: 0;">',
'จินตนาการว่าคุณสั่งอาหารผ่านแอป แล้วในช่อง <strong>"ชื่อผู้รับ"</strong> คุณแกล้งพิมพ์ว่า: <code style="color: #f43f5e; background: #040711; padding: 2px 6px; border-radius: 4px;">สมชาย\' และไม่ต้องคิดเงิน ส่งอาหารมาฟรีทันที --</code><br>',
'หากพนักงานส่งของอ่านแล้วเข้าใจว่านี่คือชื่อคนตามปกติ ระบบก็ปลอดภัย... แต่หากพนักงานส่งของแยกไม่ออก แล้วทำตามข้อความข้างหลังโดย <em>"ส่งอาหารให้ฟรีจริงๆ"</em> นั่นคืออาการของ <strong>SQL Injection!</strong> เกิดจากการที่ระบบแยกไม่ออกว่าส่วนไหนคือ <strong>"ข้อมูลของผู้ใช้ (Data)"</strong> และส่วนไหนคือ <strong>"คำสั่งของโปรแกรม (Command)"</strong>',
'</p>',
'</div>',
'</div>',

'<!-- Animated Vector SVG Section -->',
'<div style="padding: 22px 28px 16px;">',
'<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">',
'<span style="color: #f43f5e; font-family: monospace; font-size: 0.84rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; display: flex; align-items: center; gap: 8px;">',
'<i class="fas fa-project-diagram"></i> แผนภาพจำลองกลไกการแหกคุกคำสั่ง SQL (SQL INJECTION BREAKOUT &amp; GUILLOTINE ANIMATION)',
'</span>',
'<span style="background: rgba(239, 68, 68, 0.15); color: #f87171; font-family: monospace; font-size: 0.7rem; font-weight: 800; padding: 2px 8px; border-radius: 4px; display: inline-flex; align-items: center; gap: 6px;">',
'<span style="width: 6px; height: 6px; border-radius: 50%; background: #ef4444; display: inline-block;"></span> ANIMATED PIPELINE',
'</span>',
'</div>',
svg_raw,
'</div>',

'<!-- The 3 Deadly Symbols Breakdown -->',
'<div style="padding: 0 28px 24px; background: rgba(5, 8, 18, 0.85);">',
'<h4 style="margin: 16px 0 14px; color: #fbbf24; font-size: 0.95rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.06em; display: flex; align-items: center; gap: 8px;">',
'<i class="fas fa-key"></i> ถอดรหัส 3 สัญลักษณ์มหาภัยของ SQL Injection (The 3 Deadly Symbols)',
'</h4>',

'<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; margin-bottom: 20px;">',

'<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(244, 63, 94, 0.35); border-radius: 12px; padding: 16px;">',
'<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">',
'<strong style="color: #fb7185; font-size: 0.9rem; display: flex; align-items: center; gap: 8px;">',
'<span style="font-size: 1.2rem;">💥</span> 1. เครื่องหมาย \' (Single Quote)',
'</strong>',
'<span style="background: rgba(244, 63, 94, 0.15); color: #fca5a5; font-size: 0.65rem; font-family: monospace; font-weight: bold; padding: 2px 6px; border-radius: 4px;">กุญแจแหกคุก</span>',
'</div>',
'<p style="color: #cbd5e1; font-size: 0.8rem; line-height: 1.6; margin: 0 0 8px;">',
'ในไวยากรณ์ SQL ข้อความต้องถูกครอบด้วยเครื่องหมายคำพูด <code>\'...\'</code> เมื่อผู้โจมตีใส่ <code>\'</code> เข้าไป มันจะไป <strong>ปิดสตริงก่อนเวลาอันควร</strong> ทำให้ข้อความถัดจากนั้นหลุดออกจากการเป็นข้อมูล กลายร่างเป็นคำสั่ง SQL นอกกรงขังทันที',
'</p>',
'<div style="background: #040711; border: 1px dashed rgba(244, 63, 94, 0.3); border-radius: 6px; padding: 6px 10px; font-family: monospace; font-size: 0.72rem; color: #fca5a5;">',
'WHERE user = \'admin<strong>\'</strong> &larr; สตริงปิดตรงนี้!',
'</div>',
'</div>',

'<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(251, 191, 36, 0.35); border-radius: 12px; padding: 16px;">',
'<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">',
'<strong style="color: #fde047; font-size: 0.9rem; display: flex; align-items: center; gap: 8px;">',
'<span style="font-size: 1.2rem;">🪄</span> 2. ประพจน์ OR 1=1 (Tautology)',
'</strong>',
'<span style="background: rgba(251, 191, 36, 0.15); color: #fde047; font-size: 0.65rem; font-family: monospace; font-weight: bold; padding: 2px 6px; border-radius: 4px;">คาถาสัจนิรันดร์</span>',
'</div>',
'<p style="color: #cbd5e1; font-size: 0.8rem; line-height: 1.6; margin: 0 0 8px;">',
'ตามกฎตรรกศาสตร์ <code>เท็จ OR จริง = จริง (F &or; T = True)</code> แม้รหัสผ่านหรือชื่อผู้ใช้จะไม่ถูกต้อง แต่เมื่อถูกเชื่อมด้วย <code>OR 1=1</code> ทั้งประโยคจะถูกประเมินผลเป็น **จริงเสมอ** ทำให้ฐานข้อมูลยอมคายข้อมูลทุกแถวออกมา',
'</p>',
'<div style="background: #040711; border: 1px dashed rgba(251, 191, 36, 0.3); border-radius: 6px; padding: 6px 10px; font-family: monospace; font-size: 0.72rem; color: #fde047;">',
'WHERE id = \'\' <strong>OR \'1\'=\'1\'</strong> &larr; เป็นจริงทุกกรณี!',
'</div>',
'</div>',

'<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(56, 189, 248, 0.35); border-radius: 12px; padding: 16px;">',
'<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">',
'<strong style="color: #38bdf8; font-size: 0.9rem; display: flex; align-items: center; gap: 8px;">',
'<span style="font-size: 1.2rem;">✂️</span> 3. เครื่องหมาย -- หรือ # (Comment)',
'</strong>',
'<span style="background: rgba(56, 189, 248, 0.15); color: #7dd3fc; font-size: 0.65rem; font-family: monospace; font-weight: bold; padding: 2px 6px; border-radius: 4px;">มีดเลเซอร์ตัดตอน</span>',
'</div>',
'<p style="color: #cbd5e1; font-size: 0.8rem; line-height: 1.6; margin: 0 0 8px;">',
'ในภาษา SQL สัญลักษณ์ <code>--</code> หรือ <code>#</code> หมายถึง <em>"ข้อความหลังจากนี้คือหมายเหตุ (Comment) ห้ามนำไปประมวลผล"</em> ผู้โจมตีจึงใช้สัญลักษณ์นี้เพื่อ **ตัดคำสั่งตรวจรหัสผ่านทิ้งไปทั้งยวง** อย่างง่ายดาย',
'</p>',
'<div style="background: #040711; border: 1px dashed rgba(56, 189, 248, 0.3); border-radius: 6px; padding: 6px 10px; font-family: monospace; font-size: 0.72rem; color: #7dd3fc;">',
'WHERE user=\'admin\' <strong>--</strong> <span style="text-decoration:line-through; color:#64748b;">AND pass=\'...\'</span>',
'</div>',
'</div>',

'</div>',

'<!-- 4 Core Attack Mechanics Cards (Normal vs Exploit) -->',
'<h4 style="margin: 16px 0 14px; color: #00f0ff; font-size: 0.95rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.06em; display: flex; align-items: center; gap: 8px;">',
'<i class="fas fa-microchip"></i> 4 รูปแบบการโจมตีหลักในบทเรียนสไลด์ (Lecture Attack Scenarios)',
'</h4>',

'<div style="display: flex; flex-direction: column; gap: 14px;">',

'<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(34, 197, 94, 0.3); border-left: 4px solid #22c55e; border-radius: 10px; padding: 14px 18px;">',
'<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">',
'<strong style="color: #4ade80; font-size: 0.88rem;">1. Normal SQL Query (การตรวจสอบปกติ)</strong>',
'<span style="background: rgba(34, 197, 94, 0.15); color: #86efac; font-size: 0.65rem; font-family: monospace; padding: 2px 6px; border-radius: 4px;">LEGITIMATE</span>',
'</div>',
'<div style="font-size: 0.78rem; color: #cbd5e1; margin-bottom: 6px;">อินพุต: <code>admin</code> / <code>p@ssW0rd</code> &bull; ระบบตรวจเช็คว่ามี username และ password ตรงกับในตาราง users หรือไม่</div>',
'<code style="background: #040711; padding: 6px 10px; border-radius: 6px; font-size: 0.76rem; color: #86efac; display: block;">SELECT * FROM users WHERE username = \'admin\' AND password = \'p@ssW0rd\';</code>',
'</div>',

'<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(244, 63, 94, 0.3); border-left: 4px solid #f43f5e; border-radius: 10px; padding: 14px 18px;">',
'<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">',
'<strong style="color: #fb7185; font-size: 0.88rem;">2. Authentication Bypass via Commenting Out (admin\' --)</strong>',
'<span style="background: rgba(244, 63, 94, 0.15); color: #fca5a5; font-size: 0.65rem; font-family: monospace; padding: 2px 6px; border-radius: 4px;">AUTH BYPASS</span>',
'</div>',
'<div style="font-size: 0.78rem; color: #cbd5e1; margin-bottom: 6px;">อินพุต: <code>admin\' --</code> &bull; สัญลักษณ์ <code>--</code> ตัดทิ้งเงื่อนไข password ทำให้ล็อกอินเข้าเป็น admin สำเร็จทันที</div>',
'<code style="background: #040711; padding: 6px 10px; border-radius: 6px; font-size: 0.76rem; color: #fca5a5; display: block;">SELECT * FROM users WHERE username = \'admin\' <span style="color:#f59e0b;">--\' AND password = \'xxx\';</span></code>',
'</div>',

'<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(251, 191, 36, 0.3); border-left: 4px solid #fbbf24; border-radius: 10px; padding: 14px 18px;">',
'<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">',
'<strong style="color: #fde047; font-size: 0.88rem;">3. Error-Based / Tautology Stealing Data (\' OR \'1\'=\'1)</strong>',
'<span style="background: rgba(251, 191, 36, 0.15); color: #fde047; font-size: 0.65rem; font-family: monospace; padding: 2px 6px; border-radius: 4px;">DATA THEFT</span>',
'</div>',
'<div style="font-size: 0.78rem; color: #cbd5e1; margin-bottom: 6px;">อินพุต: <code>\' OR \'1\'=\'1</code> &bull; สัจนิรันดร์ F &or; T = True ทำให้ฐานข้อมูลพ่นรายชื่อบัญชีผู้ใช้ทุกคนออกมาทั้งหมด</div>',
'<code style="background: #040711; padding: 6px 10px; border-radius: 6px; font-size: 0.76rem; color: #fde047; display: block;">SELECT id, name FROM users WHERE id = \'\' <span style="color:#00f0ff;">OR \'1\'=\'1\';</span></code>',
'</div>',

'<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(168, 85, 247, 0.3); border-left: 4px solid #a855f7; border-radius: 10px; padding: 14px 18px;">',
'<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px;">',
'<strong style="color: #c084fc; font-size: 0.88rem;">4. UNION-Based &amp; Blind Boolean Injection</strong>',
'<span style="background: rgba(168, 85, 247, 0.15); color: #d8b4fe; font-size: 0.65rem; font-family: monospace; padding: 2px 6px; border-radius: 4px;">ADVANCED</span>',
'</div>',
'<div style="font-size: 0.78rem; color: #cbd5e1; margin-bottom: 6px;">ใช้ <code>UNION SELECT</code> สูบข้อมูลข้ามตาราง หรือใช้ <code>SUBSTRING(database(),1,1)=\'m\'</code> สืบหาตัวอักษรแบบตาบอด</div>',
'<code style="background: #040711; padding: 6px 10px; border-radius: 6px; font-size: 0.76rem; color: #d8b4fe; display: block;">SELECT id, name FROM users WHERE id = \'\' UNION SELECT username, password FROM users --\';</code>',
'</div>',

'</div>',

'</div>',
'</div>',
'',
payloads_and_sqlmap_raw
]

clean_html = '\n'.join([p.lstrip() for p in full_content])
rendered = markdown(clean_html)
print("Rendered length:", len(rendered))
print("Any <p>:", "<p>" in rendered)
print("Any &lt;div:", "&lt;div" in rendered)
print("Contains <svg>:", "<svg" in rendered)
