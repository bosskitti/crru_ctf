# Craft the ultimate SQL Injection SVG icon
sqli_svg_icon = """<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:100%; display:block; filter:drop-shadow(0 0 12px rgba(244, 63, 94, 0.6));">
<defs>
<linearGradient id="sqli-db-grad" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="#1e293b"/>
  <stop offset="50%" stop-color="#0f172a"/>
  <stop offset="100%" stop-color="#020617"/>
</linearGradient>
<linearGradient id="sqli-db-rim" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" stop-color="#38bdf8"/>
  <stop offset="100%" stop-color="#0284c7"/>
</linearGradient>
<linearGradient id="sqli-needle-grad" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="#ff007f"/>
  <stop offset="50%" stop-color="#f43f5e"/>
  <stop offset="100%" stop-color="#e11d48"/>
</linearGradient>
<linearGradient id="sqli-laser-core" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="#ffffff"/>
  <stop offset="100%" stop-color="#fb7185"/>
</linearGradient>
<filter id="neon-glow" x="-30%" y="-30%" width="160%" height="160%">
  <feGaussianBlur stdDeviation="3" result="blur"/>
  <feComposite in="SourceGraphic" in2="blur" operator="over"/>
</filter>
</defs>

<!-- Background Tech Hex/Circle Accent -->
<circle cx="60" cy="60" r="54" fill="none" stroke="rgba(244,63,94,0.2)" stroke-width="1.5" stroke-dasharray="6,4"/>
<circle cx="60" cy="60" r="48" fill="rgba(15,23,42,0.6)"/>

<!-- 1. Database Cylinders (Base & Middle Layers) -->
<!-- Bottom Disk -->
<ellipse cx="50" cy="85" rx="32" ry="11" fill="url(#sqli-db-grad)" stroke="#38bdf8" stroke-width="1.5"/>
<path d="M 18,85 L 18,97 C 18,104 82,104 82,97 L 82,85" fill="url(#sqli-db-grad)" stroke="#38bdf8" stroke-width="1.5"/>

<!-- Middle Disk (Breached / Glowing Red) -->
<ellipse cx="50" cy="66" rx="32" ry="11" fill="url(#sqli-db-grad)" stroke="#f43f5e" stroke-width="1.8"/>
<path d="M 18,66 L 18,78 C 18,85 82,85 82,78 L 82,66" fill="url(#sqli-db-grad)" stroke="#f43f5e" stroke-width="1.8"/>

<!-- Top Disk -->
<ellipse cx="50" cy="47" rx="32" ry="11" fill="url(#sqli-db-grad)" stroke="#38bdf8" stroke-width="1.5"/>
<path d="M 18,47 L 18,59 C 18,66 82,66 82,59 L 82,47" fill="url(#sqli-db-grad)" stroke="#38bdf8" stroke-width="1.5"/>

<!-- Database Status LEDs -->
<circle cx="28" cy="53" r="2" fill="#00f0ff"/>
<circle cx="28" cy="72" r="2" fill="#f43f5e"/>
<circle cx="28" cy="91" r="2" fill="#00f0ff"/>

<!-- 2. Breach Crack & SQL Injection Payload (';--) on Database -->
<path d="M 52,66 L 46,72 L 54,75 L 49,82" fill="none" stroke="#f43f5e" stroke-width="2" stroke-linecap="round" filter="url(#neon-glow)"/>
<!-- Shockwave Rings at injection point -->
<circle cx="50" cy="66" r="6" fill="none" stroke="#f43f5e" stroke-width="1.5" opacity="0.8"/>
<circle cx="50" cy="66" r="11" fill="none" stroke="#f43f5e" stroke-width="1" stroke-dasharray="3,3" opacity="0.6"/>

<!-- 3. The Malicious Cyber Syringe / Injector (Diagonal from Top-Right ➔ Into Core) -->
<!-- Plunger Top & Rod -->
<rect x="94" y="8" width="14" height="4" rx="2" transform="rotate(45, 94, 8)" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
<path d="M 88,18 L 74,32" stroke="#e2e8f0" stroke-width="2.5" stroke-linecap="round"/>

<!-- Syringe Glass Barrel (Glowing Neon Red Injection) -->
<rect x="58" y="26" width="30" height="15" rx="3" transform="rotate(45, 58, 26)" fill="url(#sqli-needle-grad)" stroke="#ffffff" stroke-width="1.5" filter="url(#neon-glow)"/>

<!-- Measurement Lines on Syringe Barrel -->
<line x1="68" y1="31" x2="71" y2="28" stroke="#ffffff" stroke-width="1" opacity="0.8"/>
<line x1="74" y1="37" x2="77" y2="34" stroke="#ffffff" stroke-width="1" opacity="0.8"/>
<line x1="80" y1="43" x2="83" y2="40" stroke="#ffffff" stroke-width="1" opacity="0.8"/>

<!-- Syringe Fluid Core Highlight -->
<path d="M 64,36 L 82,54" stroke="url(#sqli-laser-core)" stroke-width="2" stroke-linecap="round"/>

<!-- Needle Hub -->
<polygon points="56,48 61,43 57,39 52,44" fill="#94a3b8" stroke="#ffffff" stroke-width="1"/>

<!-- Ultra-sharp Needle penetrating DB Center (50, 66) -->
<line x1="54" y1="46" x2="48" y2="52" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" filter="url(#neon-glow)"/>

<!-- 4. Leaking SQL Exploit Glyphs Floating Out -->
<text x="76" y="92" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="900" filter="url(#neon-glow)">';--</text>
<text x="82" y="74" fill="#00f0ff" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold">1=1</text>
<circle cx="50" cy="66" r="3" fill="#ffffff" filter="url(#neon-glow)"/>
</svg>"""

with open('/tmp/sqli_icon.svg', 'w') as f:
    f.write(sqli_svg_icon)
print("Created /tmp/sqli_icon.svg!")
