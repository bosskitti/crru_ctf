from CTFd import create_app
from CTFd.utils import markdown

# Design the ultimate conceptual animated SVG and visual explainer
svg_code = """<svg viewBox="0 0 980 380" style="width:100%; height:auto; display:block; margin:0 auto; background:#070b16; border-radius:14px; border:1px solid rgba(244, 63, 94, 0.3); box-shadow:0 14px 45px rgba(0,0,0,0.7), 0 0 25px rgba(244, 63, 94, 0.1);">
<defs>
<linearGradient id="grad-user" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#ff007f"/><stop offset="100%" stop-color="#e11d48"/></linearGradient>
<linearGradient id="grad-server" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#0284c7"/><stop offset="100%" stop-color="#0369a1"/></linearGradient>
<linearGradient id="grad-db" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#10b981"/><stop offset="100%" stop-color="#047857"/></linearGradient>
<linearGradient id="grad-cut" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#ef4444"/><stop offset="100%" stop-color="#f59e0b"/></linearGradient>
<filter id="glow-pink" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3" result="blur"/><feComposite in="SourceGraphic" in2="blur" operator="over"/></filter>
<filter id="glow-cyan" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3" result="blur"/><feComposite in="SourceGraphic" in2="blur" operator="over"/></filter>
<style>
@keyframes flowStream { from { stroke-dashoffset: 32; } to { stroke-dashoffset: 0; } }
@keyframes pulseSparks { 0%, 100% { transform: scale(1); opacity: 0.8; } 50% { transform: scale(1.15); opacity: 1; filter: drop-shadow(0 0 10px #f43f5e); } }
@keyframes blinkBypass { 0%, 100% { fill: #ef4444; filter: drop-shadow(0 0 8px #ef4444); } 50% { fill: #22c55e; filter: drop-shadow(0 0 12px #22c55e); } }
@keyframes laserCut { 0% { opacity: 0.3; } 50% { opacity: 1; stroke-width: 3.5; } 100% { opacity: 0.3; } }
.dash-stream { stroke-dasharray: 8, 4; animation: flowStream 1.2s linear infinite; }
.pulse-spark { transform-origin: center; animation: pulseSparks 1.8s ease-in-out infinite; }
.laser-guillotine { animation: laserCut 1.5s ease-in-out infinite; }
.lock-pulse { animation: blinkBypass 2.5s infinite; }
</style>
</defs>

<!-- Subtle Grid Background -->
<path d="M 0,60 L 980,60 M 0,160 L 980,160 M 0,260 L 980,260 M 0,340 L 980,340" stroke="rgba(255,255,255,0.02)" stroke-width="1"/>
<path d="M 160,0 L 160,380 M 390,0 L 390,380 M 690,0 L 690,380 M 860,0 L 860,380" stroke="rgba(255,255,255,0.02)" stroke-width="1"/>

<!-- 1. Left Node: Attacker / Input Form -->
<g transform="translate(30, 95)">
<rect x="0" y="0" width="140" height="175" rx="14" fill="#0b1224" stroke="#f43f5e" stroke-width="2" filter="url(#glow-pink)"/>
<circle cx="70" cy="42" r="26" fill="#1e293b" stroke="#f43f5e" stroke-width="1.5"/>
<circle cx="70" cy="35" r="11" fill="#f43f5e"/>
<path d="M 52,53 C 52,44 88,44 88,53" fill="#f43f5e"/>
<rect x="14" y="78" width="112" height="24" rx="12" fill="rgba(244, 63, 94, 0.15)" stroke="#f43f5e" stroke-width="1"/>
<text x="70" y="94" fill="#ffffff" font-family="sans-serif" font-size="10.5" font-weight="bold" text-anchor="middle">Attacker Input</text>
<rect x="12" y="112" width="116" height="46" rx="6" fill="#040711" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
<text x="18" y="127" fill="#94a3b8" font-family="monospace" font-size="8.5">Username:</text>
<text x="18" y="146" fill="#f43f5e" font-family="monospace" font-size="9" font-weight="bold">admin' --</text>
</g>

<!-- Stream 1: Attacker to Web Server -->
<g transform="translate(170, 160)">
<path d="M 0,20 L 75,20" fill="none" stroke="#f43f5e" stroke-width="3" filter="url(#glow-pink)" class="dash-stream"/>
<polygon points="78,20 66,14 66,26" fill="#f43f5e"/>
<rect x="5" y="-3" width="70" height="18" rx="5" fill="#0f172a" stroke="#f43f5e" stroke-width="0.8"/>
<text x="40" y="10" fill="#fca5a5" font-family="monospace" font-size="8" font-weight="bold" text-anchor="middle">HTTP POST</text>
</g>

<!-- 2. Middle Node: Web Application (String Concatenation Trap) -->
<g transform="translate(250, 80)">
<rect x="0" y="0" width="155" height="205" rx="14" fill="#0b1329" stroke="#00f0ff" stroke-width="2" filter="url(#glow-cyan)"/>
<rect x="12" y="14" width="131" height="34" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
<text x="77" y="35" fill="#00f0ff" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Web Application</text>
<rect x="12" y="58" width="131" height="90" rx="6" fill="#040711" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
<text x="20" y="74" fill="#94a3b8" font-family="monospace" font-size="8">// Insecure Code:</text>
<text x="20" y="90" fill="#cbd5e1" font-family="monospace" font-size="8">$sql = "SELECT *</text>
<text x="20" y="104" fill="#cbd5e1" font-family="monospace" font-size="8">FROM users</text>
<text x="20" y="118" fill="#cbd5e1" font-family="monospace" font-size="8">WHERE user='</text>
<text x="20" y="132" fill="#f43f5e" font-family="monospace" font-size="8.5" font-weight="bold">.$_POST['u']."'";</text>
<rect x="12" y="158" width="131" height="34" rx="6" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="1"/>
<text x="77" y="174" fill="#fca5a5" font-family="sans-serif" font-size="8.5" font-weight="bold" text-anchor="middle">⚠️ No Sanitization!</text>
<text x="77" y="186" fill="#fde047" font-family="sans-serif" font-size="8" text-anchor="middle">นำข้อมูลต่อสตริงตรงๆ</text>
</g>

<!-- Stream 2: Web Server to SQL Query Pipeline -->
<g transform="translate(405, 160)">
<path d="M 0,20 L 50,20" fill="none" stroke="#00f0ff" stroke-width="2.5" class="dash-stream"/>
<polygon points="53,20 43,15 43,25" fill="#00f0ff"/>
</g>

<!-- 3. The Query Breakthrough & Guillotine (Center-Right Engine) -->
<g transform="translate(460, 65)">
<rect x="0" y="0" width="280" height="235" rx="14" fill="#060a16" stroke="rgba(255,255,255,0.15)" stroke-width="1.5"/>
<rect x="0" y="0" width="280" height="32" rx="14" fill="rgba(255,255,255,0.04)"/>
<text x="140" y="21" fill="#cbd5e1" font-family="sans-serif" font-size="10.5" font-weight="bold" text-anchor="middle">SQL Parser: คำสั่งถูกเปลี่ยนแปลงโครงสร้าง</text>

<!-- Assembled SQL Box -->
<g transform="translate(15, 48)">
<rect x="0" y="0" width="250" height="75" rx="8" fill="#02040a" stroke="#38bdf8" stroke-width="1"/>
<text x="12" y="22" fill="#38bdf8" font-family="monospace" font-size="9.5" font-weight="bold">SELECT * FROM users</text>
<text x="12" y="40" fill="#38bdf8" font-family="monospace" font-size="9.5" font-weight="bold">WHERE username = '</text>
<text x="155" y="40" fill="#f43f5e" font-family="monospace" font-size="10.5" font-weight="bold">admin'</text>
<text x="202" y="40" fill="#fbbf24" font-family="monospace" font-size="11" font-weight="bold">--</text>
<text x="12" y="60" fill="#64748b" font-family="monospace" font-size="9" text-decoration="line-through">' AND password = 'xxx';</text>
</g>

<!-- Explanatory Visual Badges inside parser -->
<!-- Spark 1: Single Quote Breakout -->
<g transform="translate(25, 138)">
<circle cx="12" cy="12" r="14" fill="rgba(244, 63, 94, 0.2)" stroke="#f43f5e" stroke-width="1.5" class="pulse-spark"/>
<text x="12" y="17" fill="#f43f5e" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">'</text>
<text x="36" y="12" fill="#fff" font-family="sans-serif" font-size="9.5" font-weight="bold">1. Single Quote Breakout</text>
<text x="36" y="25" fill="#94a3b8" font-family="sans-serif" font-size="8.5">ปิดสตริงก่อนเวลาเพื่อแหกออกเป็นคำสั่ง</text>
</g>

<!-- Spark 2: Comment Guillotine -->
<g transform="translate(25, 180)">
<circle cx="12" cy="12" r="14" fill="rgba(251, 191, 36, 0.2)" stroke="#fbbf24" stroke-width="1.5" class="pulse-spark"/>
<text x="12" y="16" fill="#fbbf24" font-family="monospace" font-size="11" font-weight="bold" text-anchor="middle">--</text>
<text x="36" y="12" fill="#fff" font-family="sans-serif" font-size="9.5" font-weight="bold">2. Comment Laser Guillotine</text>
<text x="36" y="25" fill="#fca5a5" font-family="sans-serif" font-size="8.5">สัญลักษณ์ -- ลบการตรวจรหัสผ่านทิ้ง 100%!</text>
</g>
</g>

<!-- Stream 3: Parser to Database -->
<g transform="translate(740, 160)">
<path d="M 0,20 L 45,20" fill="none" stroke="#22c55e" stroke-width="3" class="dash-stream"/>
<polygon points="48,20 36,14 36,26" fill="#22c55e"/>
</g>

<!-- 4. Right Node: Database Cylinder & Vault -->
<g transform="translate(790, 75)">
<rect x="0" y="0" width="160" height="215" rx="14" fill="#08141d" stroke="#22c55e" stroke-width="2" filter="url(#glow-cyan)"/>
<!-- 3D Database Cylinders -->
<ellipse cx="80" cy="38" rx="55" ry="16" fill="#0f2b26" stroke="#22c55e" stroke-width="1.5"/>
<path d="M 25,38 L 25,65 C 25,76 135,76 135,65 L 135,38" fill="#0b1f1b" stroke="#22c55e" stroke-width="1.5"/>
<path d="M 25,65 L 25,92 C 25,103 135,103 135,92 L 135,65" fill="#0b1f1b" stroke="#22c55e" stroke-width="1.5"/>
<text x="80" y="42" fill="#4ade80" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">MySQL Vault</text>

<!-- Access Granted Badge -->
<rect x="15" y="112" width="130" height="38" rx="8" fill="rgba(34, 197, 94, 0.15)" stroke="#22c55e" stroke-width="1.5"/>
<circle cx="32" cy="131" r="7" class="lock-pulse"/>
<text x="48" y="128" fill="#86efac" font-family="sans-serif" font-size="9" font-weight="bold">AUTH BYPASS!</text>
<text x="48" y="140" fill="#cbd5e1" font-family="sans-serif" font-size="8">LoggedIn as "admin"</text>

<!-- Leaked Table rows -->
<rect x="15" y="160" width="130" height="42" rx="6" fill="#03060c" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
<text x="22" y="174" fill="#fbbf24" font-family="monospace" font-size="7.5">id: 1 &bull; user: admin</text>
<text x="22" y="186" fill="#94a3b8" font-family="monospace" font-size="7.5">hash: $2y$10$vK3... [OK]</text>
<text x="22" y="196" fill="#4ade80" font-family="sans-serif" font-size="7.5" font-weight="bold">🔓 ฐานข้อมูลยอมส่งข้อมูลออก</text>
</g>

<!-- Bottom Explanatory Banner inside SVG -->
<g transform="translate(30, 310)">
<rect x="0" y="0" width="920" height="50" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
<text x="20" y="24" fill="#00f0ff" font-family="sans-serif" font-size="11" font-weight="bold">💡 หัวใจสำคัญ (Core Concept):</text>
<text x="20" y="40" fill="#cbd5e1" font-family="sans-serif" font-size="10">SQL Injection เกิดจากความสับสนระหว่าง "ข้อมูล (Data)" กับ "คำสั่ง (Command)" เมื่อใส่ Single Quote (') ระบบคิดว่าข้อมูลจบแล้ว ข้อความถัดมาจึงกลายเป็นคำสั่ง SQL ใหม่ทันที!</text>
</g>
</svg>"""

rendered = markdown(svg_code)
print("Rendered length:", len(rendered))
print("Any <p>:", "<p>" in rendered)
print("Any &lt;div:", "&lt;div" in rendered)
print("Contains <svg>:", "<svg" in rendered)
