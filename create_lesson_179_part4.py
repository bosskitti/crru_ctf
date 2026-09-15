import json

# =========================================================================
# 7. CLICKJACKING MASTERCLASS + ANIMATED SVG 3 + LAB 34 WALKTHROUGH (BLOCK 6)
# =========================================================================
clickjacking_masterclass_html = """<!-- ========================================== -->
<!-- SECTION 3: CLICKJACKING (UI REDRESSING) MASTERCLASS -->
<!-- ========================================== -->
<div style="margin: 2.5rem auto 1.5rem; max-width: 1050px; background: linear-gradient(135deg, rgba(8, 14, 30, 0.98) 0%, rgba(30, 20, 10, 0.98) 100%); border: 1px solid rgba(245, 158, 11, 0.3); border-left: 4px solid #f59e0b; border-radius: 16px; padding: 24px 28px; box-shadow: 0 16px 45px rgba(0, 0, 0, 0.6), 0 0 25px rgba(245, 158, 11, 0.1);">

<!-- Header -->
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; margin-bottom: 20px; padding-bottom: 14px; border-bottom: 1px solid rgba(255, 255, 255, 0.08);">
<div style="display: flex; align-items: center; gap: 12px;">
<span style="font-size: 1.5rem;">🖱️</span>
<div>
<h3 style="margin: 0; color: #ffffff; font-size: 1.25rem; font-weight: 800;">
3. ช่องโหว่แผ่นใสล่องหนครอบคลิก (Clickjacking / UI Redressing Attacks)
</h3>
<span style="color: #94a3b8; font-size: 0.82rem;">ถอดรหัสกลลวงซ้อนทับหน้าเว็บที่มองไม่เห็น (Invisible Iframe) เพื่อขโมยการคลิกของผู้ใช้งาน</span>
</div>
</div>
<div style="display: flex; gap: 8px; flex-wrap: wrap;">
<span style="background: rgba(245, 158, 11, 0.15); color: #fde047; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(245, 158, 11, 0.35);">
OWASP A04: INSECURE DESIGN
</span>
<span style="background: rgba(239, 68, 68, 0.15); color: #fca5a5; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(239, 68, 68, 0.35);">
CWE-1021: IMPROPER FRAME RESTRICTION
</span>
</div>
</div>

<!-- Intuitive Metaphor for Students -->
<div style="background: rgba(245, 158, 11, 0.06); border: 1px dashed rgba(245, 158, 11, 0.3); border-radius: 12px; padding: 18px 20px; margin-bottom: 22px;">
<div style="color: #fbbf24; font-weight: 800; font-size: 0.92rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-lightbulb"></i> อุปมาอุปไมยให้เข้าใจง่าย: Clickjacking เปรียบเสมือน "แผ่นใสล่องหนวางทับปุ่ม"
</div>
<p style="margin: 0 0 10px; color: #cbd5e1; font-size: 0.84rem; line-height: 1.65;">
ลองนึกภาพเกมในงานวัดที่มีปุ่มไฟกะพริบสีเขียวเขียนว่า <strong>"กดตรงนี้เพื่อรับรางวัล 1,000,000 บาท!"</strong> ใครเห็นก็อยากจะเอานิ้วไปกด... แต่สิ่งที่น้องๆ มองไม่เห็นคือ มีคนเอา <strong>"แผ่นพลาสติกใสแจ๋ว (Invisible Iframe)"</strong> มาวางลอยอยู่เหนือปุ่มนั้นเพียง 1 มิลลิเมตร!
</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 12px; margin-top: 12px;">
<div style="background: rgba(0,0,0,0.3); border-radius: 8px; padding: 12px; border-left: 3px solid #10b981;">
<strong style="color: #34d399; font-size: 0.8rem; display: block; margin-bottom: 4px;">👁️ สิ่งที่สายตาเรามองเห็น (ชั้นล่าง):</strong>
<span style="color: #94a3b8; font-size: 0.78rem; line-height: 1.5;">เราเห็นปุ่มน่าดึงดูดใจ เช่น <em>"กดรับเงินรางวัล / ดูคลิปแมวน่ารัก / เล่นเกมฟรี"</em> จึงไม่ลังเลที่จะคลิก</span>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 8px; padding: 12px; border-left: 3px solid #ef4444;">
<strong style="color: #fca5a5; font-size: 0.8rem; display: block; margin-bottom: 4px;">🎯 สิ่งที่นิ้วเราสัมผัสจริง (ชั้นบนสุด):</strong>
<span style="color: #94a3b8; font-size: 0.78rem; line-height: 1.5;">บนแผ่นใสที่ลอยอยู่ มีหน้าต่างของธนาคารหรือบัญชีของเราเปิดอยู่แบบโปร่งใส 100% และมีปุ่ม <em>"ลบบัญชีถาวร"</em> หรือ <em>"โอนเงินทั้งหมด"</em> วางตรงกับตำแหน่งนิ้วของเราพอดีเป๊ะ!</span>
</div>
</div>
</div>

<!-- Animated Vector Graphic 3: Clickjacking 3D Layer Breakdown -->
<div style="background: #040711; border: 1px solid rgba(245, 158, 11, 0.25); border-radius: 14px; padding: 16px; margin-bottom: 22px; box-shadow: inset 0 0 30px rgba(0,0,0,0.8);">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; padding: 0 4px;">
<span style="color: #fbbf24; font-size: 0.78rem; font-weight: 800; font-family: monospace; letter-spacing: 0.08em; text-transform: uppercase;">
<i class="fas fa-layer-group mr-2"></i> แผนภาพเคลื่อนไหว: โครงสร้างซ้อนชั้น 3D ของการโจมตี Clickjacking (UI Redressing Layers)
</span>
<span style="font-size: 0.7rem; color: #64748b; font-family: monospace;">LIVE SVG INTERACTIVE</span>
</div>

<svg viewBox="0 0 900 380" width="100%" height="100%" style="display: block; border-radius: 10px; background: #070a14;" xmlns="http://www.w3.org/2000/svg">
<defs>
<linearGradient id="cj-bg" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#090a18" />
<stop offset="100%" stop-color="#161208" />
</linearGradient>
<filter id="cursor-glow" x="-20%" y="-20%" width="140%" height="140%">
<feGaussianBlur stdDeviation="3" result="blur" />
<feComposite in="SourceGraphic" in2="blur" operator="over" />
</filter>
<style>
@keyframes clickPulse {
  0% { transform: scale(1); opacity: 0.9; }
  50% { transform: scale(1.15); opacity: 1; filter: drop-shadow(0 0 10px #f59e0b); }
  100% { transform: scale(1); opacity: 0.9; }
}
@keyframes cursorClick {
  0%, 100% { transform: translate(0, 0); }
  50% { transform: translate(6px, 8px); }
}
@keyframes rippleWave {
  0% { r: 6; opacity: 1; }
  100% { r: 32; opacity: 0; }
}
.click-target { animation: clickPulse 2.5s infinite ease-in-out; transform-origin: center; }
.mouse-cursor { animation: cursorClick 2s infinite ease-in-out; }
.ripple { animation: rippleWave 2s infinite cubic-bezier(0, 0.2, 0.8, 1); }
</style>
</defs>

<rect width="900" height="380" rx="12" fill="url(#cj-bg)" stroke="rgba(255,255,255,0.06)" />

<!-- Left/Center Perspective: 2 Overlapping Layers -->

<!-- LAYER 1: DECOY WEBSITE (BOTTOM VISIBLE LAYER) -->
<g transform="translate(60, 40)">
<rect x="0" y="0" width="400" height="290" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="rgba(16, 185, 129, 0.4)" stroke-width="1.5" />
<rect x="0" y="0" width="400" height="32" rx="12" fill="rgba(16, 185, 129, 0.15)" />
<circle cx="20" cy="16" r="4" fill="#ef4444" />
<circle cx="34" cy="16" r="4" fill="#f59e0b" />
<circle cx="48" cy="16" r="4" fill="#10b981" />
<text x="200" y="21" fill="#6ee7b7" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" text-anchor="middle">ชั้นที่ 1: หน้าเว็บเหยื่อล่อ (DECOY BAIT - VISIBLE)</text>

<!-- Fake Content -->
<text x="200" y="65" fill="#fde047" font-family="sans-serif" font-size="14" font-weight="extrabold" text-anchor="middle">🎁 QUICKPAY REWARDS GIVEAWAY!</text>
<text x="200" y="88" fill="#94a3b8" font-family="sans-serif" font-size="9.5" text-anchor="middle">ยินดีด้วย! คุณได้รับสิทธิ์รับเงินรางวัล 1,000,000 บาท</text>
<text x="200" y="115" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="24" font-weight="bold" text-anchor="middle">$1,000,000</text>

<!-- Decoy Button -->
<rect x="100" y="145" width="200" height="48" rx="10" fill="linear-gradient(135deg, #10b981, #059669)" stroke="#34d399" stroke-width="1.5" />
<text x="200" y="174" fill="#ffffff" font-family="sans-serif" font-size="11.5" font-weight="bold" text-anchor="middle">👉 CLAIM YOUR CASHBACK</text>

<rect x="25" y="215" width="350" height="60" rx="8" fill="#030712" stroke="rgba(255,255,255,0.06)" />
<text x="40" y="238" fill="#94a3b8" font-family="sans-serif" font-size="9">สิ่งที่ผู้ใช้มองเห็น:</text>
<text x="40" y="256" fill="#38bdf8" font-family="sans-serif" font-size="9" font-weight="bold">มองเห็นปุ่มแจกเงินรางวัลสีเขียว จึงตัดสินใจคลิกทันที</text>
</g>

<!-- LAYER 2: INVISIBLE IFRAME (TOP TRANSPARENT LAYER) -->
<g transform="translate(110, 80)">
<!-- Dotted outline showing the transparent iframe -->
<rect x="0" y="0" width="370" height="270" rx="12" fill="rgba(239, 68, 68, 0.04)" stroke="#ef4444" stroke-width="2" stroke-dasharray="6 4" />
<rect x="0" y="0" width="370" height="30" rx="12" fill="rgba(239, 68, 68, 0.15)" />
<text x="185" y="20" fill="#fca5a5" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold" text-anchor="middle">ชั้นที่ 2: IFRAME โปร่งแสง (OPACITY: 0.001 &bull; Z-INDEX: 20)</text>

<!-- Real Victim Page Content inside invisible frame -->
<text x="20" y="55" fill="#f87171" font-family="'JetBrains Mono', monospace" font-size="9">Src: http://bank.local/victim.php</text>
<text x="20" y="75" fill="#94a3b8" font-family="sans-serif" font-size="8.5">ระบบจัดการบัญชีผู้ใช้: admin</text>

<!-- Hidden Real Danger Button aligned over Decoy Button -->
<g class="click-target">
<rect x="50" y="105" width="200" height="48" rx="10" fill="rgba(239, 68, 68, 0.25)" stroke="#ef4444" stroke-width="2" />
<text x="150" y="134" fill="#fca5a5" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">🗑️ DELETE ACCOUNT PERMANENTLY</text>
</g>

<!-- Click Ripple Animation -->
<circle cx="150" cy="129" r="10" fill="none" stroke="#ef4444" stroke-width="2" class="ripple" />
<circle cx="150" cy="129" r="18" fill="none" stroke="#f59e0b" stroke-width="1.5" class="ripple" style="animation-delay: 0.5s;" />

<rect x="15" y="185" width="340" height="70" rx="8" fill="#030712" stroke="rgba(239, 68, 68, 0.3)" />
<text x="28" y="208" fill="#fca5a5" font-family="sans-serif" font-size="9" font-weight="bold">สิ่งที่เกิดขึ้นจริงเมื่อคลิก:</text>
<text x="28" y="226" fill="#cbd5e1" font-family="sans-serif" font-size="8.5">อีเวนต์การคลิกทะลุเข้าสู่ iframe ที่อยู่ชั้นบนสุด</text>
<text x="28" y="244" fill="#ef4444" font-family="sans-serif" font-size="8.5" font-weight="bold">ทำให้ปุ่ม "ลบบัญชีถาวร" ถูกกดโดยไม่รู้ตัว!</text>
</g>

<!-- Cursor Hand Pointer -->
<g transform="translate(230, 200)" class="mouse-cursor">
<polygon points="0,0 0,22 6,17 12,28 17,25 11,14 19,14" fill="#ffffff" stroke="#000000" stroke-width="1.5" filter="url(#cursor-glow)" />
</g>

<!-- ==================== RIGHT: CSS ATTACK ATTRIBUTES ==================== -->
<g transform="translate(530, 40)">
<rect x="0" y="0" width="330" height="300" rx="14" fill="rgba(15, 23, 42, 0.95)" stroke="rgba(245, 158, 11, 0.35)" stroke-width="1.5" />
<rect x="0" y="0" width="330" height="34" rx="14" fill="rgba(245, 158, 11, 0.12)" />
<text x="165" y="22" fill="#fde047" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">⚙️ 4 คุณสมบัติ CSS ที่แฮกเกอร์ใช้</text>

<!-- CSS Item 1 -->
<rect x="16" y="48" width="298" height="52" rx="6" fill="#030712" stroke="rgba(255,255,255,0.06)" />
<text x="28" y="68" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="bold">opacity: 0.001; /* เกือบมองไม่เห็น */</text>
<text x="28" y="86" fill="#94a3b8" font-family="sans-serif" font-size="8">ทำให้เฟรมกลายเป็นแผ่นใสโปร่งแสง ผู้ใช้มองไม่เห็นหน้าจริง</text>

<!-- CSS Item 2 -->
<rect x="16" y="108" width="298" height="52" rx="6" fill="#030712" stroke="rgba(255,255,255,0.06)" />
<text x="28" y="128" fill="#f59e0b" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="bold">position: absolute; top: -260px;</text>
<text x="28" y="146" fill="#94a3b8" font-family="sans-serif" font-size="8">ขยับปรับพิกัดให้ปุ่มเป้าหมายมาทับตรงปุ่มล่อใจเป๊ะๆ</text>

<!-- CSS Item 3 -->
<rect x="16" y="168" width="298" height="52" rx="6" fill="#030712" stroke="rgba(255,255,255,0.06)" />
<text x="28" y="188" fill="#ec4899" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="bold">z-index: 999; /* ลอยอยู่ชั้นบนสุด */</text>
<text x="28" y="206" fill="#94a3b8" font-family="sans-serif" font-size="8">บังคับให้เบราว์เซอร์ส่งอีเวนต์คลิกไปให้ Iframe ก่อน</text>

<!-- CSS Item 4 -->
<rect x="16" y="228" width="298" height="58" rx="6" fill="rgba(16, 185, 129, 0.08)" stroke="rgba(16, 185, 129, 0.25)" />
<text x="28" y="248" fill="#34d399" font-family="sans-serif" font-size="9.5" font-weight="bold">🛡️ จุดตายของระบบ:</text>
<text x="28" y="266" fill="#cbd5e1" font-family="sans-serif" font-size="8.5">เว็บเหยื่อไม่ได้ตั้งค่า Header: <tspan fill="#fca5a5" font-family="monospace">X-Frame-Options</tspan></text>
</g>
</svg>
</div>

<!-- Walkthrough Card for Challenge 34 -->
<div style="background: rgba(245, 158, 11, 0.08); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 12px; padding: 18px; margin-bottom: 16px;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
<div style="color: #fbbf24; font-weight: 800; font-size: 0.95rem; display: flex; align-items: center; gap: 8px;">
<span>🎯</span> ปฏิบัติการ Lab Clickjacking: ขั้นตอนการเจาะระบบ (Challenge 34 Walkthrough Guide)
</div>
<span style="background: rgba(245, 158, 11, 0.2); color: #fde047; font-size: 0.72rem; font-family: monospace; font-weight: 700; padding: 3px 8px; border-radius: 6px;">APPRENTICE LAB</span>
</div>
<ol style="margin: 0; padding-left: 20px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.75;">
<li>คลิกเปิดระบบปฏิบัติการจำลอง QuickPay ในกล่อง Challenge ด้านล่าง</li>
<li>เปิดดูหน้าเป้าหมายของเหยื่อที่ URL: <code style="color: #fbbf24;">/victim.php</code> จะพบหน้าจัดการบัญชีที่มีปุ่มสีแดง <strong>"Remove Account"</strong> (สังเกตว่าหน้านี้ไม่มี Header ป้องกันการครอบเฟรม)</li>
<li>เปิดหน้าเว็บของคนร้ายที่ URL: <code style="color: #38bdf8;">/attacker.php</code> จะพบหน้าเว็บโปรโมชันล่อใจ "Claim Your Cashback 💰"</li>
<li>คลิกขวาที่ปุ่มสีเขียว "CLAIM YOUR CASHBACK" แล้วเลือก <strong>Inspect (ตรวจสอบองค์ประกอบ)</strong> จะสังเกตเห็นแท็ก <code style="color: #f43f5e;">&lt;iframe class="victim-iframe"&gt;</code> ที่มีค่า <code>opacity: 0.01</code> ลอยอยู่ข้างบน</li>
<li>เมื่อคลิกปุ่มสีเขียว 1 ครั้ง จะส่งผลให้ปุ่ม "Remove Account" ใน iframe ถูกกด บัญชีจะถูกลบและธง Flag จะปรากฏขึ้นในหน้า <code style="color: #34d399;">/victim.php</code> ทันที!</li>
</ol>
</div>

</div>"""

# =========================================================================
# 8. SUMMARY CARD 3: CLICKJACKING DEFENSE DEBRIEF (BLOCK 8)
# =========================================================================
clickjacking_summary_html = """<!-- ========================================== -->
<!-- UNIFIED MASTERCLASS DEBRIEF: CLICKJACKING DEFENSE -->
<!-- ========================================== -->
<div style="margin: 2.5rem auto 3rem; max-width: 1050px; background: linear-gradient(135deg, rgba(8, 14, 30, 0.98) 0%, rgba(30, 20, 10, 0.98) 100%); border: 1px solid rgba(245, 158, 11, 0.35); border-left: 4px solid #f59e0b; border-radius: 16px; padding: 24px 28px; box-shadow: 0 16px 45px rgba(0, 0, 0, 0.7), 0 0 30px rgba(245, 158, 11, 0.15);">

<!-- Header -->
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; margin-bottom: 20px; padding-bottom: 14px; border-bottom: 1px solid rgba(255, 255, 255, 0.08);">
<div style="display: flex; align-items: center; gap: 14px;">
<div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.4); display: flex; align-items: center; justify-content: center; font-size: 1.4rem; box-shadow: 0 0 20px rgba(245, 158, 11, 0.3); flex-shrink: 0;">
<i class="fas fa-hand-pointer"></i>
</div>
<div>
<h4 style="margin: 0; color: #ffffff; font-size: 1.2rem; font-weight: 800; letter-spacing: -0.01em;">
🛡️ สรุปบทเรียนท้ายแล็บ: กลไกและแนวทางป้องกัน Clickjacking (UI Redressing Defense)
</h4>
<span style="color: #94a3b8; font-size: 0.82rem;">ถอดรหัสความล้มเหลวจากการไร้ Frame Control สู่เกราะป้องกัน X-Frame-Options และ CSP frame-ancestors</span>
</div>
</div>
<div style="display: flex; gap: 8px; flex-wrap: wrap;">
<span style="background: rgba(245, 158, 11, 0.15); color: #fde047; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(245, 158, 11, 0.35);">
OWASP A04: INSECURE DESIGN
</span>
<span style="background: rgba(239, 68, 68, 0.15); color: #fca5a5; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(239, 68, 68, 0.35);">
CWE-1021: UI REDRESSING
</span>
</div>
</div>

<!-- 3 Columns Takeaways -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 14px; margin-bottom: 20px;">

<!-- Column 1 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(245, 158, 11, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #fbbf24; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-bullseye"></i> 1. แก่นการโจมตี (UI Redressing Explored)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>Invisible Framing:</strong> หน้าเว็บที่ไม่มี Header ห้ามครอบเฟรม สามารถถูกฝังลงในแท็ก <code>&lt;iframe&gt;</code> ของเว็บอื่นได้ทุกที่</li>
<li><strong>Pixel-Perfect Alignment:</strong> ใช้คำสั่ง CSS ปรับพิกัด <code>top/left</code> ดึงปุ่มสำคัญของเหยื่อมาทับตรงกับปุ่มล่อใจของแฮกเกอร์</li>
<li><strong>Opacity Camouflage:</strong> ตั้งค่า <code>opacity: 0.0001</code> เพื่อให้มองทะลุเห็นปุ่มปลอมด้านล่าง แต่ยังรับแรงกดของเมาส์ได้สมบูรณ์</li>
</ul>
</div>

<!-- Column 2 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(239, 68, 68, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #f87171; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-skull"></i> 2. ผลกระทบจริงต่อผู้ใช้ (Weaponization)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>ลบบัญชีหรือข้อมูลถาวร:</strong> เหยื่อกดลบบัญชีตนเองโดยไม่ตั้งใจ เหมือนในปฏิบัติการ Lab 34</li>
<li><strong>Likejacking / Social Fraud:</strong> บังคับให้บัญชีของเหยื่อกดถูกใจ (Like) โพสต์การเมือง หรือแชร์สแกมหลอกลวง</li>
<li><strong>เปิดสิทธิ์ฮาร์ดแวร์ (Camera/Mic):</strong> หลอกคลิกอนุญาตให้เว็บเข้าถึงกล้องเว็บแคมหรือไมโครโฟน</li>
</ul>
</div>

<!-- Column 3 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #4ade80; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-shield-halved"></i> 3. กฎเหล็กการป้องกัน (Golden Defense Rules)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>X-Frame-Options: DENY:</strong> สั่งเบราว์เซอร์ห้ามนำหน้าเว็บนี้ไปใส่ใน <code>&lt;iframe&gt;</code> เด็ดขาด ไม่ว่าใครจะขอเปิดก็ตาม</li>
<li><strong>X-Frame-Options: SAMEORIGIN:</strong> อนุญาตให้เปิดในเฟรมได้เฉพาะหน้าเว็บที่มาจากโดเมนเดียวกันเท่านั้น</li>
<li><strong>CSP frame-ancestors 'none':</strong> มาตรฐานใหม่ที่แนะนำใน Content Security Policy รองรับการควบคุมที่ยืดหยุ่น</li>
<li><strong>SameSite Cookies:</strong> ช่วยบรรเทาปัญหา เพราะหากข้ามโดเมน คุกกี้จะไม่ถูกส่ง ทำให้หน้าใน iframe เป็นสถานะยังไม่ได้ล็อกอิน</li>
</ul>
</div>

</div>

<!-- Secure Code Comparison Box -->
<div style="background: #040711; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 18px; margin-bottom: 16px;">
<div style="color: #94a3b8; font-size: 0.78rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-code-compare"></i> ตัวอย่างการติดตั้ง Header ป้องกัน Clickjacking บนเว็บเซิร์ฟเวอร์ (Nginx &amp; PHP)
</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(310px, 1fr)); gap: 14px;">
<div style="background: rgba(239, 68, 68, 0.08); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 8px; padding: 12px;">
<div style="color: #fca5a5; font-size: 0.78rem; font-weight: 800; margin-bottom: 6px;">❌ VULNERABLE: ไม่มี Header ควบคุมการครอบเฟรม</div>
<pre style="margin: 0; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #fca5a5; line-height: 1.5;"><code>// เว็บไซต์ตอบสนองกลับโดยไม่มี Header ป้องกัน
// ส่งผลให้เว็บอื่นสามารถเขียน &lt;iframe src="our-site.com"&gt; ครอบได้ทันที
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8</code></pre>
</div>
<div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 12px;">
<div style="color: #86efac; font-size: 0.78rem; font-weight: 800; margin-bottom: 6px;">✅ SECURE: ติดตั้ง X-Frame-Options และ CSP ปลอดภัย 100%</div>
<pre style="margin: 0; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #86efac; line-height: 1.5;"><code>// PHP: สั่งส่ง Header ทันทีที่ส่วนหัวของสคริปต์
header("X-Frame-Options: DENY");
header("Content-Security-Policy: frame-ancestors 'none';");

// Nginx Config: บล็อกการครอบเฟรมทั้งเว็บไซต์
add_header X-Frame-Options "DENY" always;
add_header Content-Security-Policy "frame-ancestors 'none';" always;</code></pre>
</div>
</div>
</div>

<div style="text-align: right; font-size: 0.76rem; color: #64748b;">
บทสรุปสำหรับปฏิบัติการ Lab Clickjacking (Challenge 34) &bull; CRRU Cybersecurity Curriculum 2026
</div>

</div>"""

print("Writing create_lesson_179.py part 4...")
