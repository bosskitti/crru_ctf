import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

new_svg_html = """<div style="background:#070a13; border:1px solid rgba(0,240,255,0.15); border-radius:12px; padding:24px; text-align:center; margin:2rem auto; max-width:850px; box-shadow: 0 8px 32px rgba(0,0,0,0.4);">
  <div style="font-size:0.85rem; color:#00f0ff; font-weight:bold; margin-bottom:16px; text-transform:uppercase; letter-spacing:0.08em; text-shadow:0 0 8px rgba(0,240,255,0.4);"><i class="fas fa-project-diagram mr-2"></i> แผนภาพจำลองกระบวนการโจมตี Path Traversal (3-Step Attack Flow)</div>
  
  <svg viewBox="0 0 720 280" style="width:100%; height:auto; display:block; margin:0 auto; background:#03050a; border-radius:8px;">
    <defs>
      <linearGradient id="neon-blue" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#00f0ff" />
        <stop offset="100%" stop-color="#3b82f6" />
      </linearGradient>
      <linearGradient id="neon-red" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#ff007f" />
        <stop offset="100%" stop-color="#ef4444" />
      </linearGradient>
      <filter id="glow-blue" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="3" result="blur" />
        <feComposite in="SourceGraphic" in2="blur" operator="over" />
      </filter>
      <filter id="glow-red" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="3" result="blur" />
        <feComposite in="SourceGraphic" in2="blur" operator="over" />
      </filter>
    </defs>

    <!-- STEP 1 & 3: Hacker Panel -->
    <g transform="translate(20, 80)">
      <rect x="0" y="0" width="110" height="110" rx="8" fill="#0f1322" stroke="#ff007f" stroke-width="1.5" filter="url(#glow-red)"/>
      <circle cx="55" cy="40" r="18" fill="none" stroke="#ff007f" stroke-width="1.5"/>
      <path d="M42,40 C42,32 68,32 68,40" fill="none" stroke="#ff007f" stroke-width="1.5"/>
      <path d="M37,70 C37,55 73,55 73,70 L73,80 L37,80 Z" fill="#ff007f" opacity="0.2"/>
      <path d="M37,70 C37,55 73,55 73,70 L73,80 L37,80 Z" fill="none" stroke="#ff007f" stroke-width="1.5"/>
      <text x="55" y="100" fill="#ffffff" font-size="10" font-family="sans-serif" font-weight="bold" text-anchor="middle">Hacker</text>
    </g>

    <!-- STEP 1: Sending Malicious Path Request -->
    <path d="M140,110 L220,110" fill="none" stroke="#ff007f" stroke-width="2" stroke-dasharray="4,2" filter="url(#glow-red)"/>
    <polygon points="220,110 212,106 212,114" fill="#ff007f"/>
    <text x="180" y="100" fill="#ff007f" font-size="8.5" font-family="monospace" text-anchor="middle" font-weight="bold">1. Send Path Request</text>
    <text x="180" y="122" fill="#cbd5e1" font-size="7.5" font-family="monospace" text-anchor="middle">?page=../../etc/passwd</text>

    <!-- STEP 3: Return File Contents -->
    <path d="M220,160 L140,160" fill="none" stroke="#3b82f6" stroke-width="2" filter="url(#glow-blue)"/>
    <polygon points="140,160 148,156 148,164" fill="#3b82f6"/>
    <text x="180" y="152" fill="#3b82f6" font-size="8.5" font-family="monospace" text-anchor="middle" font-weight="bold">3. Return Private File</text>
    <text x="180" y="174" fill="#34d399" font-size="7.5" font-family="monospace" text-anchor="middle">Content of passwd file...</text>

    <!-- Web Server Panel -->
    <g transform="translate(240, 80)">
      <rect x="0" y="0" width="100" height="110" rx="8" fill="#0f1322" stroke="#3b82f6" stroke-width="1.5" filter="url(#glow-blue)"/>
      <rect x="10" y="15" width="80" height="18" rx="3" fill="#1e293b" stroke="#3b82f6" stroke-width="0.75"/>
      <circle cx="20" cy="24" r="3" fill="#34d399" filter="url(#glow-blue)"/>
      <text x="50" y="26" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Server OS</text>
      
      <rect x="10" y="45" width="80" height="18" rx="3" fill="#1e293b" stroke="#3b82f6" stroke-width="0.75"/>
      <circle cx="20" cy="54" r="3" fill="#3b82f6"/>
      <text x="50" y="56" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Web Service</text>

      <rect x="10" y="75" width="80" height="18" rx="3" fill="#1e293b" stroke="#3b82f6" stroke-width="0.75"/>
      <circle cx="20" cy="84" r="3" fill="#ff007f" filter="url(#glow-red)"/>
      <text x="50" y="86" fill="#ff007f" font-size="8" font-family="sans-serif" font-weight="bold" text-anchor="middle">Vulnerable API</text>
    </g>

    <!-- STEP 2: Path Resolution (Red Cross blocking normal path) -->
    <!-- Line to Normal File -->
    <path d="M350,115 L430,75" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,2"/>
    <!-- Red Cross blocking normal file access -->
    <circle cx="390" cy="95" r="9" fill="#03050a" stroke="#ef4444" stroke-width="1.5"/>
    <path d="M386,91 L394,99 M394,91 L386,99" fill="none" stroke="#ef4444" stroke-width="1.5"/>

    <!-- Line to Private Directory -->
    <path d="M350,150 L430,195" fill="none" stroke="#ff007f" stroke-width="2" filter="url(#glow-red)"/>
    <polygon points="430,195 422,190 424,199" fill="#ff007f"/>
    <text x="395" y="215" fill="#ff007f" font-size="8" font-family="monospace" text-anchor="middle" font-weight="bold">2. Include Hacker Path</text>

    <!-- WEBSITE (Web Root) Container -->
    <g transform="translate(450, 20)">
      <rect x="0" y="0" width="130" height="210" rx="8" fill="#05070f" stroke="#3b82f6" stroke-width="1" stroke-dasharray="2,2"/>
      <text x="65" y="16" fill="#3b82f6" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Website (Web Root)</text>

      <!-- Normal File/Directory -->
      <g transform="translate(15, 30)">
        <rect x="0" y="0" width="100" height="50" rx="5" fill="#0f1322" stroke="#3b82f6" stroke-width="1"/>
        <path d="M15,15 L25,15 L25,35 L15,35 Z" fill="none" stroke="#3b82f6" stroke-width="1"/>
        <text x="60" y="25" fill="#ffffff" font-size="8.5" font-family="sans-serif" text-anchor="middle">Normal File</text>
        <text x="60" y="38" fill="#94a3b8" font-size="7" font-family="monospace" text-anchor="middle">index.html</text>
      </g>

      <!-- Private Directory -->
      <g transform="translate(15, 140)">
        <rect x="0" y="0" width="100" height="55" rx="5" fill="#0f1322" stroke="#ff007f" stroke-width="1" filter="url(#glow-red)"/>
        <!-- Folder Icon -->
        <path d="M12,18 L12,42 L38,42 L38,24 L24,24 L20,18 Z" fill="rgba(255, 0, 127, 0.1)" stroke="#ff007f" stroke-width="1"/>
        <text x="62" y="28" fill="#ffffff" font-size="8" font-family="sans-serif" font-weight="bold" text-anchor="middle">Private Dir</text>
        <text x="62" y="42" fill="#ff007f" font-size="7" font-family="monospace" text-anchor="middle">/../../</text>
      </g>
    </g>

    <!-- Connection from Private Directory to System (Climbing out of web root) -->
    <path d="M570,170 L600,170" fill="none" stroke="#ff007f" stroke-width="2" filter="url(#glow-red)"/>
    <polygon points="600,170 592,166 592,174" fill="#ff007f"/>

    <!-- SYSTEM Container -->
    <g transform="translate(605, 95)">
      <rect x="0" y="0" width="100" height="100" rx="8" fill="#05070f" stroke="#ef4444" stroke-width="1"/>
      <text x="50" y="16" fill="#ef4444" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">System (OS)</text>

      <!-- Private File -->
      <g transform="translate(10, 30)">
        <rect x="0" y="0" width="80" height="50" rx="4" fill="#0f1322" stroke="#ef4444" stroke-width="1" filter="url(#glow-red)"/>
        <text x="40" y="24" fill="#ffffff" font-size="8" font-family="sans-serif" font-weight="bold" text-anchor="middle">Private File</text>
        <text x="40" y="38" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">/etc/passwd</text>
      </g>
    </g>
  </svg>
</div>"""

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        try:
            blocks = json.loads(l.content)
            val = blocks[0]["value"]
            
            # Find the enclosing container of path_traversal_custom_diagram_1783910274465.png
            target_start = val.find('<div style="text-align: center; margin: 2rem auto; padding: 15px;')
            target_end = val.find('</div>', target_start) + 6
            
            if target_start != -1 and target_end != -1:
                # Replace with the new SVG HTML block
                new_val = val[:target_start] + new_svg_html + val[target_end:]
                blocks[0]["value"] = new_val
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print("Successfully replaced static image with custom SVG 3-step Traversal diagram!")
            else:
                print("Error: Could not find target image container in Lesson 177 Block 0.")
        except Exception as e:
            print(f"Error: {e}")
