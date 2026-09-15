from CTFd import create_app
from CTFd.utils import markdown

# 1. Command Injection SVG
cmdi_svg = """<svg viewBox="0 0 980 340" style="width:100%; height:auto; display:block; margin:0 auto; background:#070b16; border-radius:14px; border:1px solid rgba(239, 68, 68, 0.3); box-shadow:0 14px 45px rgba(0,0,0,0.7), 0 0 25px rgba(239, 68, 68, 0.1);">
<defs>
<linearGradient id="cmdi-grad-shell" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#1e293b"/><stop offset="100%" stop-color="#020617"/></linearGradient>
<filter id="cmdi-glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3" result="blur"/><feComposite in="SourceGraphic" in2="blur" operator="over"/></filter>
<style>
@keyframes cmdiPulse { 0%, 100% { opacity: 0.8; } 50% { opacity: 1; filter: drop-shadow(0 0 8px #ef4444); } }
@keyframes cmdiFlow { from { stroke-dashoffset: 24; } to { stroke-dashoffset: 0; } }
.cmdi-stream { stroke-dasharray: 6, 3; animation: cmdiFlow 1s linear infinite; }
.cmdi-cursor { animation: cmdiPulse 1s infinite; }
</style>
</defs>
<path d="M 0,60 L 980,60 M 0,160 L 980,160 M 0,260 L 980,260" stroke="rgba(255,255,255,0.02)" stroke-width="1"/>
<!-- Left: Input Form -->
<g transform="translate(30, 70)">
<rect x="0" y="0" width="170" height="190" rx="12" fill="#0b1224" stroke="#ef4444" stroke-width="1.5"/>
<rect x="15" y="15" width="140" height="30" rx="6" fill="#1e293b"/>
<text x="85" y="34" fill="#f87171" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">Vulnerable Web Form</text>
<text x="18" y="70" fill="#94a3b8" font-family="monospace" font-size="8.5">Ping Diagnostic:</text>
<rect x="15" y="80" width="140" height="40" rx="6" fill="#02040a" stroke="rgba(255,255,255,0.1)"/>
<text x="22" y="98" fill="#cbd5e1" font-family="monospace" font-size="9">127.0.0.1<tspan fill="#ef4444" font-weight="bold">;</tspan></text>
<text x="22" y="112" fill="#f59e0b" font-family="monospace" font-size="9" font-weight="bold">cat /etc/passwd</text>
<rect x="15" y="135" width="140" height="32" rx="6" fill="rgba(239, 68, 68, 0.2)" stroke="#ef4444" stroke-width="1"/>
<text x="85" y="155" fill="#ffffff" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">Submit Request</text>
</g>
<!-- Flow 1 -->
<g transform="translate(205, 150)">
<path d="M 0,15 L 65,15" fill="none" stroke="#ef4444" stroke-width="2.5" class="cmdi-stream"/>
<polygon points="68,15 58,10 58,20" fill="#ef4444"/>
<text x="35" y="5" fill="#fca5a5" font-family="monospace" font-size="8" text-anchor="middle">HTTP GET</text>
</g>
<!-- Middle: PHP system() Call Trap -->
<g transform="translate(280, 60)">
<rect x="0" y="0" width="280" height="210" rx="12" fill="#0c142b" stroke="#38bdf8" stroke-width="1.5"/>
<rect x="15" y="15" width="250" height="30" rx="6" fill="#1e293b"/>
<text x="140" y="34" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">PHP Backend: system() Execution</text>
<rect x="15" y="55" width="250" height="95" rx="6" fill="#02040a" stroke="rgba(255,255,255,0.08)"/>
<text x="25" y="76" fill="#94a3b8" font-family="monospace" font-size="8.5">&lt;?php</text>
<text x="25" y="94" fill="#cbd5e1" font-family="monospace" font-size="8.5">$ip = $_GET['ip'];</text>
<text x="25" y="112" fill="#f43f5e" font-family="monospace" font-size="8.5" font-weight="bold">system("ping -c 1 " . $ip);</text>
<text x="25" y="130" fill="#94a3b8" font-family="monospace" font-size="8.5">?&gt;</text>
<rect x="15" y="160" width="250" height="36" rx="6" fill="rgba(245, 158, 11, 0.15)" stroke="#f59e0b" stroke-width="1"/>
<text x="140" y="177" fill="#fde047" font-family="sans-serif" font-size="9" font-weight="bold" text-anchor="middle">⚠️ คำสั่ง ; ทำหน้าที่เป็น Command Separator</text>
<text x="140" y="189" fill="#cbd5e1" font-family="sans-serif" font-size="8" text-anchor="middle">ระบบปฏิบัติการจะรันคำสั่งที่สองต่อทันที!</text>
</g>
<!-- Flow 2 -->
<g transform="translate(565, 150)">
<path d="M 0,15 L 65,15" fill="none" stroke="#f59e0b" stroke-width="2.5" class="cmdi-stream"/>
<polygon points="68,15 58,10 58,20" fill="#f59e0b"/>
<text x="35" y="5" fill="#fde047" font-family="monospace" font-size="8" text-anchor="middle">OS Fork</text>
</g>
<!-- Right: Server OS Terminal Execution -->
<g transform="translate(640, 50)">
<rect x="0" y="0" width="310" height="230" rx="12" fill="#000000" stroke="#10b981" stroke-width="1.5"/>
<rect x="0" y="0" width="310" height="28" rx="12" fill="#1e293b"/>
<circle cx="15" cy="14" r="4.5" fill="#ef4444"/>
<circle cx="28" cy="14" r="4.5" fill="#f59e0b"/>
<circle cx="41" cy="14" r="4.5" fill="#10b981"/>
<text x="160" y="18" fill="#94a3b8" font-family="monospace" font-size="9" text-anchor="middle">Linux Server Host (OS Shell)</text>
<text x="15" y="52" fill="#94a3b8" font-family="monospace" font-size="8.5"># 1. First Command (Ping):</text>
<text x="15" y="68" fill="#38bdf8" font-family="monospace" font-size="8.5">64 bytes from 127.0.0.1: icmp_seq=1 ttl=64</text>
<text x="15" y="95" fill="#ef4444" font-family="monospace" font-size="8.5" font-weight="bold"># 2. Injected Command (Arbitrary Read):</text>
<rect x="12" y="105" width="286" height="85" rx="6" fill="#040711" stroke="rgba(255,255,255,0.06)"/>
<text x="20" y="123" fill="#fde047" font-family="monospace" font-size="8">root:x:0:0:root:/root:/bin/bash</text>
<text x="20" y="139" fill="#cbd5e1" font-family="monospace" font-size="8">daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin</text>
<text x="20" y="155" fill="#fca5a5" font-family="monospace" font-size="8">www-data:x:33:33:www-data:/var/www:/bin/bash</text>
<text x="20" y="171" fill="#4ade80" font-family="monospace" font-size="8" font-weight="bold">flag_user:x:1001:1001:FLAG{cmd_1nj_pwned}</text>
<text x="15" y="210" fill="#10b981" font-family="monospace" font-size="8.5">www-data@server:~$ <tspan class="cmdi-cursor">_</tspan></text>
</g>
<!-- Bottom Callout -->
<g transform="translate(30, 290)">
<rect x="0" y="0" width="920" height="38" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="rgba(255,255,255,0.08)"/>
<text x="18" y="23" fill="#fca5a5" font-family="sans-serif" font-size="9.5" font-weight="bold">💡 ข้อแตกต่างสำคัญ:</text>
<text x="140" y="23" fill="#cbd5e1" font-family="sans-serif" font-size="9">SQLi เจาะแค่ฐานข้อมูล แต่ Command Injection ทะลุเข้าสู่ระบบปฏิบัติการ (OS) โดยตรง ทำให้แฮกเกอร์ยึดเครื่องเซิร์ฟเวอร์ได้ทันที!</text>
</g>
</svg>"""

rendered = markdown(cmdi_svg)
print("CmdI SVG: any <p>:", "<p>" in rendered, "any &lt;div:", "&lt;div" in rendered)
