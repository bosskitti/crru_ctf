import json

# =========================================================================
# 5. CSRF MASTERCLASS + ANIMATED SVG 2 + LAB 33 WALKTHROUGH (BLOCK 3)
# =========================================================================
csrf_masterclass_html = """<!-- ========================================== -->
<!-- SECTION 2: CROSS-SITE REQUEST FORGERY (CSRF) MASTERCLASS -->
<!-- ========================================== -->
<div style="margin: 2.5rem auto 1.5rem; max-width: 1050px; background: linear-gradient(135deg, rgba(8, 14, 30, 0.98) 0%, rgba(20, 10, 30, 0.98) 100%); border: 1px solid rgba(168, 85, 247, 0.3); border-left: 4px solid #a855f7; border-radius: 16px; padding: 24px 28px; box-shadow: 0 16px 45px rgba(0, 0, 0, 0.6), 0 0 25px rgba(168, 85, 247, 0.1);">

<!-- Header -->
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; margin-bottom: 20px; padding-bottom: 14px; border-bottom: 1px solid rgba(255, 255, 255, 0.08);">
<div style="display: flex; align-items: center; gap: 12px;">
<span style="font-size: 1.5rem;">🏦</span>
<div>
<h3 style="margin: 0; color: #ffffff; font-size: 1.25rem; font-weight: 800;">
2. ช่องโหว่แอบอ้างสิทธิ์คำสั่งข้ามไซต์ (Cross-Site Request Forgery - CSRF)
</h3>
<span style="color: #94a3b8; font-size: 0.82rem;">ถอดรหัสกลลวงที่หลอกให้เบราว์เซอร์ของเหยื่อส่งคำสั่งโอนเงินหรือเปลี่ยนรหัสผ่านแทนคนร้าย</span>
</div>
</div>
<div style="display: flex; gap: 8px; flex-wrap: wrap;">
<span style="background: rgba(168, 85, 247, 0.15); color: #d8b4fe; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(168, 85, 247, 0.35);">
OWASP A01: BROKEN ACCESS CONTROL
</span>
<span style="background: rgba(244, 63, 94, 0.15); color: #fca5a5; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(244, 63, 94, 0.35);">
CWE-352: CSRF
</span>
</div>
</div>

<!-- Intuitive Metaphor for Students -->
<div style="background: rgba(168, 85, 247, 0.06); border: 1px dashed rgba(168, 85, 247, 0.3); border-radius: 12px; padding: 18px 20px; margin-bottom: 22px;">
<div style="color: #c084fc; font-weight: 800; font-size: 0.92rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-lightbulb"></i> อุปมาอุปไมยให้เข้าใจง่าย: CSRF เปรียบเสมือน "จดหมายปลอมลายเซ็น &amp; บุรุษไปรษณีย์ที่ถูกหลอก"
</div>
<p style="margin: 0 0 10px; color: #cbd5e1; font-size: 0.84rem; line-height: 1.65;">
สมมุติว่าน้องๆ เดินทางไปแสดงตัวที่ธนาคารจนได้รับ <strong>"บัตร VIP (Session Cookie)"</strong> มาแขวนไว้ที่คอ ขณะที่กำลังเปิดหน้าธนาคารค้างไว้ใน Tab 1... บังเอิญมีเพื่อนส่งลิงก์ชวนคลิกใน Tab 2 ว่า: <em>"คลิกตรงนี้เพื่อรับเพชรฟรีในเกม 10,000 เม็ด!"</em>
</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 12px; margin-top: 12px;">
<div style="background: rgba(0,0,0,0.3); border-radius: 8px; padding: 12px; border-left: 3px solid #fbbf24;">
<strong style="color: #fde047; font-size: 0.8rem; display: block; margin-bottom: 4px;">✉️ แฮกเกอร์แอบเขียนจดหมายโอนเงิน:</strong>
<span style="color: #94a3b8; font-size: 0.78rem; line-height: 1.5;">ทันทีที่น้องๆ เปิดหน้าเว็บแจกเพชรปลอม เว็บนั้นจะแอบสั่งให้เบราว์เซอร์ของน้องๆ ส่งจดหมายว่า: <em>"โอนเงิน 1,000 บาท ไปให้แฮกเกอร์เดี๋ยวนี้!"</em></span>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 8px; padding: 12px; border-left: 3px solid #ef4444;">
<strong style="color: #fca5a5; font-size: 0.8rem; display: block; margin-bottom: 4px;">🏃‍♂️ เบราว์เซอร์หยิบบัตร VIP แนบไปด้วยเสมอ:</strong>
<span style="color: #94a3b8; font-size: 0.78rem; line-height: 1.5;">เบราว์เซอร์เปรียบเหมือนบุรุษไปรษณีย์ผู้ซื่อสัตย์ เมื่อส่งคำขอไปยังธนาคาร มันจะหยิบบัตร VIP (Cookie) แนบไปด้วย ธนาคารเห็นบัตร VIP ก็นึกว่าน้องๆ สั่งโอนเงินด้วยตัวเอง จึงอนุมัติเงินออกไปทันที!</span>
</div>
</div>
</div>

<!-- Animated Vector Graphic 2: CSRF 3-Layer Flow -->
<div style="background: #040711; border: 1px solid rgba(168, 85, 247, 0.25); border-radius: 14px; padding: 16px; margin-bottom: 22px; box-shadow: inset 0 0 30px rgba(0,0,0,0.8);">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; padding: 0 4px;">
<span style="color: #c084fc; font-size: 0.78rem; font-weight: 800; font-family: monospace; letter-spacing: 0.08em; text-transform: uppercase;">
<i class="fas fa-network-wired mr-2"></i> แผนภาพเคลื่อนไหว: ลำดับขั้นตอนการโจมตีข้ามไซต์ (CSRF Attack Mechanism)
</span>
<span style="font-size: 0.7rem; color: #64748b; font-family: monospace;">LIVE SVG INTERACTIVE</span>
</div>

<svg viewBox="0 0 900 370" width="100%" height="100%" style="display: block; border-radius: 10px; background: #070a14;" xmlns="http://www.w3.org/2000/svg">
<defs>
<linearGradient id="csrf-bg" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#080718" />
<stop offset="100%" stop-color="#140822" />
</linearGradient>
<linearGradient id="victim-tab-grad" x1="0%" y1="0%" x2="100%" y2="0%">
<stop offset="0%" stop-color="#3b82f6" />
<stop offset="100%" stop-color="#8b5cf6" />
</linearGradient>
<linearGradient id="evil-tab-grad" x1="0%" y1="0%" x2="100%" y2="0%">
<stop offset="0%" stop-color="#ec4899" />
<stop offset="100%" stop-color="#f43f5e" />
</linearGradient>
<style>
@keyframes cookiePulse {
  0%, 100% { transform: scale(1); filter: drop-shadow(0 0 4px #10b981); }
  50% { transform: scale(1.08); filter: drop-shadow(0 0 12px #34d399); }
}
@keyframes forgedPacket {
  0% { stroke-dashoffset: 280; opacity: 0.2; }
  50% { opacity: 1; }
  100% { stroke-dashoffset: 0; opacity: 0.2; }
}
@keyframes warningBlink {
  0%, 100% { opacity: 0.4; }
  50% { opacity: 1; filter: drop-shadow(0 0 8px #ef4444); }
}
.cookie-badge { animation: cookiePulse 2.5s infinite ease-in-out; transform-origin: center; }
.forged-stream { stroke-dasharray: 10 6; animation: forgedPacket 2s linear infinite; }
.warning-pulse { animation: warningBlink 1.5s infinite ease-in-out; }
</style>
</defs>

<rect width="900" height="370" rx="12" fill="url(#csrf-bg)" stroke="rgba(255,255,255,0.06)" />

<!-- ==================== LEFT: VICTIM BROWSER ==================== -->
<rect x="30" y="35" width="250" height="300" rx="14" fill="rgba(15, 23, 42, 0.9)" stroke="rgba(168, 85, 247, 0.4)" stroke-width="1.5" />
<rect x="30" y="35" width="250" height="36" rx="14" fill="rgba(168, 85, 247, 0.15)" />
<circle cx="50" cy="53" r="5" fill="#ef4444" />
<circle cx="65" cy="53" r="5" fill="#f59e0b" />
<circle cx="80" cy="53" r="5" fill="#10b981" />
<text x="160" y="57" fill="#d8b4fe" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">เหยื่อ &amp; เบราว์เซอร์ (VICTIM BROWSER)</text>

<!-- Tab 1: Bank Session (Active) -->
<rect x="44" y="85" width="222" height="70" rx="8" fill="#030712" stroke="rgba(59, 130, 246, 0.3)" />
<text x="56" y="105" fill="#60a5fa" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold">🌐 Tab 1: bank.local/dashboard</text>
<text x="56" y="122" fill="#94a3b8" font-family="sans-serif" font-size="8.5">สถานะ: ล็อกอินค้างอยู่ (Logged in as admin)</text>
<g class="cookie-badge">
<rect x="56" y="132" width="190" height="18" rx="4" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" />
<text x="151" y="145" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="bold" text-anchor="middle">🍪 Cookie: PHPSESSID=admin_vip_99</text>
</g>

<!-- Tab 2: Evil Giveaway Page -->
<rect x="44" y="165" width="222" height="75" rx="8" fill="#030712" stroke="rgba(244, 63, 94, 0.4)" />
<text x="56" y="185" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold">🎁 Tab 2: evil-giveaway.local</text>
<text x="56" y="202" fill="#cbd5e1" font-family="sans-serif" font-size="8.5">เปิดหน้าเว็บหลอกลวง "แจกเครดิต $1,000"</text>
<text x="56" y="218" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="8">&gt; Auto-submitting hidden form...</text>
<text x="56" y="232" fill="#f87171" font-family="'JetBrains Mono', monospace" font-size="8">&gt; POST /transfer.php (Silent)</text>

<!-- Browser Action Bar -->
<rect x="44" y="252" width="222" height="65" rx="8" fill="rgba(30, 41, 59, 0.5)" stroke="rgba(255,255,255,0.06)" />
<text x="56" y="272" fill="#ffffff" font-family="sans-serif" font-size="9.5" font-weight="bold">เบราว์เซอร์ทำงานอัตโนมัติ:</text>
<text x="56" y="290" fill="#94a3b8" font-family="sans-serif" font-size="8.5">เมื่อส่งคำขอข้ามไปหา bank.local</text>
<text x="56" y="306" fill="#34d399" font-family="sans-serif" font-size="8.5" font-weight="bold">เบราว์เซอร์จะแนบ Cookie ให้ทันที!</text>

<!-- ==================== MIDDLE: ATTACK FLOW & FORGED REQUEST ==================== -->
<!-- Malicious Form Code Box -->
<rect x="320" y="55" width="260" height="150" rx="10" fill="#030712" stroke="rgba(244, 63, 94, 0.4)" stroke-width="1.5" />
<rect x="320" y="55" width="260" height="28" rx="10" fill="rgba(244, 63, 94, 0.15)" />
<text x="450" y="73" fill="#fca5a5" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="bold" text-anchor="middle">โค้ดที่ซ่อนในเว็บคนร้าย (attacker.php)</text>
<text x="332" y="96" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="8.5">&lt;form id="f" method="POST"</text>
<text x="344" y="112" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="8.5">action="http://bank.local/transfer"&gt;</text>
<text x="344" y="128" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="8.5">&lt;input name="to" value="attacker"&gt;</text>
<text x="344" y="144" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="8.5">&lt;input name="amount" value="1000"&gt;</text>
<text x="332" y="160" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="8.5">&lt;/form&gt;</text>
<text x="332" y="178" fill="#4ade80" font-family="'JetBrains Mono', monospace" font-size="8.5">&lt;script&gt;f.submit();&lt;/script&gt;</text>
<text x="332" y="196" fill="#64748b" font-family="sans-serif" font-size="8">※ ยิงคำขอทันทีที่เปิดหน้าเว็บโดยไม่ต้องคลิก</text>

<!-- Forged Stream Arrow -->
<path d="M 280 205 L 320 205" fill="none" stroke="#f43f5e" stroke-width="2" class="forged-stream" />
<path d="M 580 130 L 620 130" fill="none" stroke="#ef4444" stroke-width="2.5" class="forged-stream" />

<!-- Status Badge in Middle -->
<g class="warning-pulse">
<rect x="345" y="235" width="210" height="50" rx="8" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="1.5" />
<text x="450" y="255" fill="#fca5a5" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">⚠️ คำขอปลอมแปลง (Cross-Site)</text>
<text x="450" y="272" fill="#ffffff" font-family="'JetBrains Mono', monospace" font-size="8.5" text-anchor="middle">POST + Victim's Cookie Attached</text>
</g>

<!-- ==================== RIGHT: TARGET BANK SERVER ==================== -->
<rect x="620" y="35" width="250" height="300" rx="14" fill="rgba(15, 23, 42, 0.9)" stroke="rgba(16, 185, 129, 0.4)" stroke-width="1.5" />
<rect x="620" y="35" width="250" height="36" rx="14" fill="rgba(16, 185, 129, 0.15)" />
<text x="745" y="58" fill="#6ee7b7" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">เซิร์ฟเวอร์ธนาคาร (BANK SERVER)</text>

<!-- Bank Checks Box -->
<rect x="635" y="85" width="220" height="140" rx="8" fill="#030712" stroke="rgba(255,255,255,0.06)" />
<text x="648" y="108" fill="#60a5fa" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold">📥 Endpoint: /transfer.php</text>

<!-- Check 1 -->
<rect x="648" y="118" width="194" height="28" rx="4" fill="rgba(16,185,129,0.1)" stroke="rgba(16,185,129,0.3)" />
<text x="656" y="136" fill="#34d399" font-family="sans-serif" font-size="9">1. ตรวจสอบ Cookie: <tspan font-weight="bold">ถูกต้อง! (admin)</tspan></text>

<!-- Check 2 -->
<rect x="648" y="152" width="194" height="28" rx="4" fill="rgba(239,68,68,0.15)" stroke="#ef4444" />
<text x="656" y="170" fill="#fca5a5" font-family="sans-serif" font-size="9">2. ตรวจสอบ CSRF Token: <tspan font-weight="bold">ไม่มี! (None)</tspan></text>

<!-- Result Badge -->
<rect x="648" y="186" width="194" height="28" rx="4" fill="rgba(244,63,94,0.2)" stroke="#f43f5e" />
<text x="745" y="204" fill="#f43f5e" font-family="sans-serif" font-size="9.5" font-weight="bold" text-anchor="middle">🚨 อนุมัติการโอนเงินสำเร็จ!</text>

<!-- Financial Deduction Result -->
<rect x="635" y="235" width="220" height="85" rx="8" fill="#030712" stroke="rgba(245,158,11,0.3)" />
<text x="648" y="256" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="bold">💰 ผลลัพธ์ในระบบบัญชี:</text>
<text x="648" y="274" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="8.5">ยอดเงินเดิม admin: $1,000</text>
<text x="648" y="290" fill="#f87171" font-family="'JetBrains Mono', monospace" font-size="8.5">โอนออก: -$1,000 ➔ attacker</text>
<text x="648" y="306" fill="#4ade80" font-family="'JetBrains Mono', monospace" font-size="8.5">ยอดคงเหลือ: $0 ➔ FLAG REVEALED!</text>
</svg>
</div>

<!-- Attack Vectors: GET vs POST CSRF -->
<div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 18px; margin-bottom: 20px;">
<div style="font-size: 0.85rem; font-weight: 700; color: #c084fc; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-bolt"></i> 2 รูปแบบการส่งเพย์โหลด CSRF ที่พบบ่อยในชีวิตจริง
</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 12px;">
<div style="background: rgba(0,0,0,0.3); border-radius: 8px; padding: 12px; border-left: 3px solid #38bdf8;">
<strong style="color: #7dd3fc; font-size: 0.82rem; display: block; margin-bottom: 4px;">1. GET-Based CSRF (ผ่านแท็กรูปภาพ &lt;img&gt;):</strong>
<span style="color: #94a3b8; font-size: 0.78rem; line-height: 1.5;">หากเว็บธนาคารยอมรับคำสั่งโอนเงินผ่านพารามิเตอร์ URL เช่น <code>/transfer?to=hacker&amp;amt=1000</code> แฮกเกอร์เพียงแค่โพสต์แท็กรูปภาพ <code>&lt;img src="http://bank.com/transfer?..."&gt;</code> บนเว็บบอร์ด ใครเปิดกระทู้จะโดนโอนเงินทันที!</span>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 8px; padding: 12px; border-left: 3px solid #ec4899;">
<strong style="color: #f472b6; font-size: 0.82rem; display: block; margin-bottom: 4px;">2. POST-Based CSRF (ผ่านฟอร์มซ่อนตัว):</strong>
<span style="color: #94a3b8; font-size: 0.78rem; line-height: 1.5;">หากเว็บรับเฉพาะ HTTP POST แฮกเกอร์จะสร้างฟอร์มซ่อน <code>&lt;form method="POST"&gt;</code> ในหน้าเว็บของตนเอง และใช้ JavaScript สั่ง <code>submit()</code> ทันทีที่ผู้ใช้โหลดหน้าเว็บเสร็จ</span>
</div>
</div>
</div>

<!-- Walkthrough Card for Challenge 33 -->
<div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 12px; padding: 18px; margin-bottom: 16px;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
<div style="color: #34d399; font-weight: 800; font-size: 0.95rem; display: flex; align-items: center; gap: 8px;">
<span>🎯</span> ปฏิบัติการ Lab CSRF: ขั้นตอนการเจาะระบบ (Challenge 33 Walkthrough Guide)
</div>
<span style="background: rgba(16, 185, 129, 0.2); color: #6ee7b7; font-size: 0.72rem; font-family: monospace; font-weight: 700; padding: 3px 8px; border-radius: 6px;">PRACTITIONER LAB</span>
</div>
<ol style="margin: 0; padding-left: 20px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.75;">
<li>คลิกเปิดระบบปฏิบัติการจำลอง SecureBank ในกล่อง Challenge ด้านล่าง</li>
<li>ล็อกอินด้วยบัญชีแอดมิน: Username: <code style="color: #34d399;">admin</code> / Password: <code style="color: #34d399;">password123</code> (สังเกตว่ามียอดเงินเริ่มต้น $1,000)</li>
<li>เมื่อล็อกอินค้างไว้แล้ว ให้เปิดหน้าเว็บจำลองของคนร้ายที่ URL: <code style="color: #fbbf24;">/attacker.php</code> บนแท็บใหม่</li>
<li>สังเกตว่าหน้าเว็บคนร้ายจะแอบยิงแบบฟอร์มโอนเงินไปยัง <code style="color: #38bdf8;">/dashboard.php</code> อัตโนมัติ โดยที่ผู้ใช้ไม่ต้องกดยืนยันอะไรเลย</li>
<li>ระบบจะเด้งกลับมาที่หน้าแดชบอร์ดธนาคาร ยอดเงินจะลดลงเหลือ $0 และธง Flag ประจำด่านจะปรากฏขึ้นมาทันที!</li>
</ol>
</div>

</div>"""

# =========================================================================
# 6. SUMMARY CARD 2: CSRF DEFENSE DEBRIEF (BLOCK 5)
# =========================================================================
csrf_summary_html = """<!-- ========================================== -->
<!-- UNIFIED MASTERCLASS DEBRIEF: CSRF DEFENSE -->
<!-- ========================================== -->
<div style="margin: 2.5rem auto 3rem; max-width: 1050px; background: linear-gradient(135deg, rgba(8, 14, 30, 0.98) 0%, rgba(25, 10, 30, 0.98) 100%); border: 1px solid rgba(168, 85, 247, 0.35); border-left: 4px solid #a855f7; border-radius: 16px; padding: 24px 28px; box-shadow: 0 16px 45px rgba(0, 0, 0, 0.7), 0 0 30px rgba(168, 85, 247, 0.15);">

<!-- Header -->
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; margin-bottom: 20px; padding-bottom: 14px; border-bottom: 1px solid rgba(255, 255, 255, 0.08);">
<div style="display: flex; align-items: center; gap: 14px;">
<div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(168, 85, 247, 0.15); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.4); display: flex; align-items: center; justify-content: center; font-size: 1.4rem; box-shadow: 0 0 20px rgba(168, 85, 247, 0.3); flex-shrink: 0;">
<i class="fas fa-shield-virus"></i>
</div>
<div>
<h4 style="margin: 0; color: #ffffff; font-size: 1.2rem; font-weight: 800; letter-spacing: -0.01em;">
🛡️ สรุปบทเรียนท้ายแล็บ: กลไกและแนวทางป้องกัน CSRF (CSRF Defense Summary)
</h4>
<span style="color: #94a3b8; font-size: 0.82rem;">ถอดรหัสความล้มเหลวจากการไม่มี Anti-CSRF Token สู่มาตรฐาน SameSite Cookie และ Re-Authentication</span>
</div>
</div>
<div style="display: flex; gap: 8px; flex-wrap: wrap;">
<span style="background: rgba(168, 85, 247, 0.15); color: #d8b4fe; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(168, 85, 247, 0.35);">
OWASP A01: BROKEN ACCESS CONTROL
</span>
<span style="background: rgba(244, 63, 94, 0.15); color: #fca5a5; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(244, 63, 94, 0.35);">
CWE-352: CSRF
</span>
</div>
</div>

<!-- 3 Columns Takeaways -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 14px; margin-bottom: 20px;">

<!-- Column 1 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(168, 85, 247, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #c084fc; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-key"></i> 1. แก่นการโจมตี (Attack Mechanics Explored)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>Ambient Authority:</strong> เบราว์เซอร์หยิบคุกกี้เซสชันส่งไปด้วยทุกครั้งที่มีคำขอไปยังโดเมนเป้าหมาย แม้คำขอนั้นจะเริ่มจากเว็บภายนอก</li>
<li><strong>Silent Execution:</strong> ผู้ใช้ไม่รู้ตัวว่ากำลังส่งคำสั่งร้ายแรง เพราะฟอร์มถูกซ่อนและรันผ่าน JavaScript หลังบ้าน</li>
<li><strong>No Re-confirmation:</strong> ระบบปลายทางไม่มีการขอรหัสผ่านซ้ำ หรือขอ OTP ก่อนอนุมัติการทำธุรกรรมสำคัญ</li>
</ul>
</div>

<!-- Column 2 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(239, 68, 68, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #f87171; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-triangle-exclamation"></i> 2. ผลกระทบจริงต่อองค์กร (Business Impact)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>สูญเสียทรัพย์สินทางการเงิน:</strong> ถูกสั่งโอนเงิน ย้ายแต้มสะสม หรือซื้อสินค้าแทนเหยื่อ</li>
<li><strong>การยึดครองบัญชี (Account Takeover):</strong> ถูกสั่งเปลี่ยนอีเมลกู้คืนรหัสผ่านเป็นของแฮกเกอร์</li>
<li><strong>แอบแก้ไขการตั้งค่าเร้าเตอร์ (Router DNS Hijack):</strong> แฮกเกอร์สั่งเปลี่ยน DNS เซิร์ฟเวอร์ของเร้าเตอร์ในบ้านผ่านเว็บเบราว์เซอร์</li>
</ul>
</div>

<!-- Column 3 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #4ade80; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-shield-halved"></i> 3. กฎเหล็กการป้องกัน (Golden Defense Rules)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>Anti-CSRF Tokens:</strong> สร้าง Unique, Cryptographically Secure Token แนบไปกับทุกแบบฟอร์ม POST และตรวจทานก่อนประมวลผล</li>
<li><strong>SameSite Cookie Attribute:</strong> กำหนดค่า <code>SameSite=Strict</code> หรือ <code>SameSite=Lax</code> ป้องกันเบราว์เซอร์ส่งคุกกี้เมื่อข้ามมาจากไซต์อื่น</li>
<li><strong>Re-Authentication:</strong> สำหรับการโอนเงินหรือเปลี่ยนรหัสผ่าน ต้องบังคับให้ผู้ใช้กรอกรหัสผ่านปัจจุบันหรือ OTP ซ้ำเสมอ</li>
<li><strong>Custom Request Headers:</strong> บังคับให้ส่งคำขอแบบ API ผ่าน <code>X-Requested-With</code> ซึ่งเว็บข้ามไซต์สร้างไม่ได้หากไม่มี CORS อนุญาต</li>
</ul>
</div>

</div>

<!-- Secure Code Comparison Box -->
<div style="background: #040711; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 18px; margin-bottom: 16px;">
<div style="color: #94a3b8; font-size: 0.78rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-code-compare"></i> ตัวอย่างเปรียบเทียบโค้ด: แบบฟอร์มที่มีช่องโหว่ CSRF vs แบบฟอร์มที่ป้องกันด้วย CSRF Token (PHP)
</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(310px, 1fr)); gap: 14px;">
<div style="background: rgba(239, 68, 68, 0.08); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 8px; padding: 12px;">
<div style="color: #fca5a5; font-size: 0.78rem; font-weight: 800; margin-bottom: 6px;">❌ VULNERABLE: ตรวจสอบเพียงว่าล็อกอินอยู่หรือไม่</div>
<pre style="margin: 0; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #fca5a5; line-height: 1.5;"><code>// ตรวจสอบแค่เซสชัน ใครส่ง POST มาก็ประมวลผลทันที
if ($_SESSION['logged_in']) {
    $amount = $_POST['amount'];
    transfer_money($amount, $_POST['recipient']);
}</code></pre>
</div>
<div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 12px;">
<div style="color: #86efac; font-size: 0.78rem; font-weight: 800; margin-bottom: 6px;">✅ SECURE: ตรวจสอบ Anti-CSRF Token ที่สุ่มขึ้นมาเฉพาะตัว</div>
<pre style="margin: 0; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #86efac; line-height: 1.5;"><code>// ตรวจทาน Token ที่ส่งมาว่าตรงกับ Token ที่เก็บในเซสชันหรือไม่
if (!hash_equals($_SESSION['csrf_token'], $_POST['csrf_token'] ?? '')) {
    die("CSRF Attack Blocked: Invalid Token");
}
transfer_money($_POST['amount'], $_POST['recipient']);</code></pre>
</div>
</div>
</div>

<div style="text-align: right; font-size: 0.76rem; color: #64748b;">
บทสรุปสำหรับปฏิบัติการ Lab CSRF (Challenge 33) &bull; CRRU Cybersecurity Curriculum 2026
</div>

</div>"""

print("Writing create_lesson_179.py part 3...")
