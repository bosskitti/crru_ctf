import json
import sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

# SVG without any HTML comments and with minimal indentation (to avoid markdown treating as code block)
new_svg_html = """<div style="background:#070a13; border:1px solid rgba(0,240,255,0.15); border-radius:12px; padding:24px; text-align:center; margin:2rem auto; max-width:900px; box-shadow: 0 8px 32px rgba(0,0,0,0.4);">
<div style="font-size:0.85rem; color:#00f0ff; font-weight:bold; margin-bottom:16px; text-transform:uppercase; letter-spacing:0.08em; text-shadow:0 0 8px rgba(0,240,255,0.4);"><i class="fas fa-network-wired mr-2"></i> แผนภาพแสดงช่องโหว่และการโจมตี Path Traversal (Directory Traversal Attack)</div>
<svg viewBox="0 0 820 340" style="width:100%; height:auto; display:block; margin:0 auto; background:#03050a; border-radius:8px;">
<defs>
<linearGradient id="neon-cyan-pt" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#00f0ff" /><stop offset="100%" stop-color="#3b82f6" /></linearGradient>
<linearGradient id="neon-red-pt" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#ff007f" /><stop offset="100%" stop-color="#ef4444" /></linearGradient>
<linearGradient id="neon-green-pt" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#3ddc84" /><stop offset="100%" stop-color="#10b981" /></linearGradient>
<filter id="glow-cyan-pt" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="4" result="blur" /><feComposite in="SourceGraphic" in2="blur" operator="over" /></filter>
<filter id="glow-red-pt" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="4" result="blur" /><feComposite in="SourceGraphic" in2="blur" operator="over" /></filter>
<filter id="glow-green-pt" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="4" result="blur" /><feComposite in="SourceGraphic" in2="blur" operator="over" /></filter>
</defs>
<path d="M 50,0 L 50,340 M 150,0 L 150,340 M 250,0 L 250,340 M 350,0 L 350,340 M 450,0 L 450,340 M 550,0 L 550,340 M 650,0 L 650,340 M 750,0 L 750,340" stroke="rgba(255,255,255,0.015)" stroke-width="1" />
<path d="M 0,50 L 820,50 M 0,150 L 820,150 M 0,250 L 820,250" stroke="rgba(255,255,255,0.015)" stroke-width="1" />
<g transform="translate(60, 90)">
<circle cx="60" cy="60" r="55" fill="none" stroke="#ff007f" stroke-width="1" stroke-dasharray="3,3" opacity="0.3" />
<path d="M 60,15 L 95,25 L 90,75 C 90,95 60,110 60,110 C 60,110 30,95 30,75 L 25,25 Z" fill="#0f111a" stroke="#ff007f" stroke-width="2" filter="url(#glow-red-pt)" />
<path d="M 60,35 C 50,35 45,43 45,55 C 45,67 52,70 60,70 C 68,70 75,67 75,55 C 75,43 70,35 60,35 Z" fill="none" stroke="#ffffff" stroke-width="1.5" />
<polygon points="50,52 56,54 53,50" fill="#ff007f" filter="url(#glow-red-pt)" />
<polygon points="70,52 64,54 67,50" fill="#ff007f" filter="url(#glow-red-pt)" />
<path d="M 35,95 C 35,80 50,78 60,78 C 70,78 85,80 85,95" fill="none" stroke="#ffffff" stroke-width="1.5" />
<rect x="42" y="85" width="36" height="15" rx="2" fill="#000000" stroke="#ff007f" stroke-width="1" />
<text x="60" y="93" fill="#ff007f" font-size="7" font-family="monospace" font-weight="bold" text-anchor="middle">A</text>
<text x="60" y="135" fill="#ff007f" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">Attacker</text>
</g>
<g transform="translate(200, 140)">
<path d="M 0,25 L 140,25" fill="none" stroke="#ff007f" stroke-width="3" filter="url(#glow-red-pt)" />
<polygon points="140,25 130,19 130,31" fill="#ff007f" filter="url(#glow-red-pt)" />
<text x="70" y="12" fill="#ff007f" font-size="10.5" font-family="monospace" font-weight="bold" text-anchor="middle" filter="url(#glow-red-pt)">../../etc/passwd</text>
</g>
<g transform="translate(370, 70)">
<ellipse cx="60" cy="180" rx="45" ry="12" fill="rgba(0,240,255,0.1)" filter="url(#glow-cyan-pt)" />
<polygon points="60,0 110,20 60,40 10,20" fill="#0f172a" stroke="#00f0ff" stroke-width="1.5" filter="url(#glow-cyan-pt)" />
<polygon points="10,20 60,40 60,170 10,150" fill="#090d16" stroke="#00f0ff" stroke-width="1.5" filter="url(#glow-cyan-pt)" />
<polygon points="60,40 110,20 110,150 60,170" fill="#05070a" stroke="#00f0ff" stroke-width="1.5" filter="url(#glow-cyan-pt)" />
<line x1="20" y1="45" x2="50" y2="57" stroke="#3b82f6" stroke-width="2" />
<line x1="20" y1="65" x2="50" y2="77" stroke="#3b82f6" stroke-width="2" />
<line x1="20" y1="85" x2="50" y2="97" stroke="#3b82f6" stroke-width="2" />
<line x1="20" y1="105" x2="50" y2="117" stroke="#3b82f6" stroke-width="2" />
<line x1="20" y1="125" x2="50" y2="137" stroke="#3b82f6" stroke-width="2" />
<circle cx="25" cy="50" r="1.5" fill="#3ddc84" filter="url(#glow-green-pt)" />
<circle cx="25" cy="70" r="1.5" fill="#3ddc84" filter="url(#glow-green-pt)" />
<circle cx="25" cy="90" r="1.5" fill="#ef4444" filter="url(#glow-red-pt)" />
<circle cx="25" cy="110" r="1.5" fill="#3ddc84" filter="url(#glow-green-pt)" />
<circle cx="25" cy="130" r="1.5" fill="#3ddc84" filter="url(#glow-green-pt)" />
<path d="M 70,55 L 95,45 L 95,85 L 80,95 L 80,125" fill="none" stroke="rgba(0,240,255,0.4)" stroke-width="1.2" />
<circle cx="95" cy="85" r="2.5" fill="#00f0ff" filter="url(#glow-cyan-pt)" />
<circle cx="80" cy="125" r="2.5" fill="#00f0ff" filter="url(#glow-cyan-pt)" />
<text x="60" y="200" fill="#00f0ff" font-size="12" font-family="sans-serif" font-weight="bold" text-anchor="middle">Web Server</text>
</g>
<g transform="translate(520, 30)">
<line x1="0" y1="0" x2="0" y2="240" stroke="#475569" stroke-dasharray="6,4" stroke-width="2" />
<text x="0" y="-8" fill="#cbd5e1" font-size="10.5" font-family="monospace" text-anchor="middle" font-weight="bold">Web Root</text>
</g>
<path d="M 430,90 C 430,20 520,20 560,50 L 590,72" fill="none" stroke="#ff007f" stroke-width="2" stroke-dasharray="5,2" filter="url(#glow-red-pt)" />
<path d="M 480,150 L 540,150" fill="none" stroke="#3ddc84" stroke-width="2.5" filter="url(#glow-green-pt)" />
<polygon points="540,150 532,146 532,154" fill="#3ddc84" />
<path d="M 480,175 L 540,175" fill="none" stroke="#3ddc84" stroke-width="2.5" filter="url(#glow-green-pt)" />
<polygon points="540,175 532,171 532,179" fill="#3ddc84" />
<path d="M 480,200 L 540,200" fill="none" stroke="#3ddc84" stroke-width="2.5" filter="url(#glow-green-pt)" />
<polygon points="540,200 532,196 532,204" fill="#3ddc84" />
<g transform="translate(600, 100)">
<path d="M -10,-28 L 50,0 L 50,30" fill="none" stroke="#ff007f" stroke-width="2.5" filter="url(#glow-red-pt)" />
<polygon points="50,30 46,22 54,22" fill="#ff007f" filter="url(#glow-red-pt)" />
<g transform="translate(0, 30)">
<rect x="0" y="0" width="120" height="90" rx="8" fill="#0f111a" stroke="#00f0ff" stroke-width="2" filter="url(#glow-cyan-pt)" />
<path d="M 0,15 L 0,8 C 0,5 5,0 10,0 L 45,0 C 50,0 55,5 60,10 L 110,10 C 115,10 120,15 120,20 L 120,25 Z" fill="#0f111a" stroke="#00f0ff" stroke-width="2" filter="url(#glow-cyan-pt)" />
<rect x="25" y="25" width="70" height="48" rx="2" fill="#1e293b" opacity="0.6" />
<line x1="35" y1="37" x2="85" y2="37" stroke="#ffffff" stroke-width="1.5" opacity="0.8" />
<line x1="35" y1="49" x2="70" y2="49" stroke="#ffffff" stroke-width="1.5" opacity="0.8" />
<line x1="35" y1="61" x2="60" y2="61" stroke="#00f0ff" stroke-width="1.5" filter="url(#glow-cyan-pt)" />
<text x="60" y="115" fill="#ffffff" font-size="11.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">System Files</text>
<text x="60" y="132" fill="#00f0ff" font-size="10.5" font-family="monospace" font-weight="bold" text-anchor="middle">/etc/passwd</text>
</g>
</g>
</svg>
</div>"""

with app.app_context():
    l = TutorialLesson.query.get(177)
    if l:
        blocks = json.loads(l.content)
        val4 = blocks[4]["value"]
        
        # Find the old SVG wrapper div and replace it
        # The wrapper starts with: <div style="background:#070a13; border:1px solid rgba(0,240,255,0.15)
        old_div_start = val4.find('<div style="background:#070a13; border:1px solid rgba(0,240,255,0.15)')
        if old_div_start != -1:
            # Find the closing </div> that closes the SVG wrapper
            old_svg_end = val4.find('</svg>', old_div_start) + 6   # after </svg>
            old_div_end = val4.find('</div>', old_svg_end) + 6     # after the outer </div>
            new_val = val4[:old_div_start] + new_svg_html + val4[old_div_end:]
            blocks[4]["value"] = new_val
            l.content = json.dumps(blocks, ensure_ascii=False)
            app.db.session.commit()
            print("Successfully replaced SVG diagram with comment-free version in Lesson 177 Block 4!")
        else:
            print("Could not find SVG wrapper div. Checking alternatives...")
            # Try the image-based old div
            old_div_start2 = val4.find('<div style="text-align: center; margin: 2rem auto; padding: 15px;')
            if old_div_start2 != -1:
                old_div_end2 = val4.find('</div>', old_div_start2) + 6
                new_val = val4[:old_div_start2] + new_svg_html + val4[old_div_end2:]
                blocks[4]["value"] = new_val
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print("Replaced old image div with SVG in Lesson 177 Block 4!")
            else:
                print("ERROR: Cannot find the target div to replace!")
