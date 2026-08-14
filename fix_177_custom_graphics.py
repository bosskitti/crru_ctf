"""
Fix Lesson 177 Block 0 graphics:
Recreate the 10 diagrams in a premium cyberpunk neon code style (using modern inline SVGs, CSS animations,
pulsing nodes, and clean cyber aesthetics), but referencing the EXACT flow, labels, and details
from the user's slide deck (e.g. SolarWinds Orion attack flow, Credential Stuffing, API Stored XSS).
"""
import json, re, sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app

app = create_app()

# ─── Custom Cyberpunk Styled SVG Diagrams matching slide details ───

# 1. Broken Access Control (Slide 10)
# Detail: Changing user_id in URL from 12345 to 12346 to access other profile
SVG_A01 = """<div class="cyber-diag-wrapper">
  <style>
    .cyber-diag-wrapper { background: #070a13; border: 1px solid rgba(0, 240, 255, 0.15); border-radius: 12px; padding: 20px; text-align: center; margin: 15px auto; }
    .diag-title { font-size: 0.75rem; color: #00f0ff; font-weight: bold; margin-bottom: 12px; text-transform: uppercase; letter-spacing: 0.05em; text-shadow: 0 0 8px rgba(0, 240, 255, 0.4); }
    .pulse-node { animation: diagPulse 2s infinite alternate; }
    @keyframes diagPulse { 0% { filter: drop-shadow(0 0 2px rgba(239, 68, 68, 0.4)); } 100% { filter: drop-shadow(0 0 8px rgba(239, 68, 68, 0.8)); } }
  </style>
  <div class="diag-title">📊 Graphic: A01 - Broken Access Control Bypass</div>
  <svg viewBox="0 0 450 160" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #03050a; border-radius: 8px;">
    <!-- Attacker Node -->
    <g transform="translate(25, 45)">
      <rect x="0" y="0" width="80" height="45" rx="6" fill="#0f1322" stroke="#ef4444" stroke-width="1.5" class="pulse-node"/>
      <text x="40" y="20" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Attacker</text>
      <text x="40" y="34" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">Manipulates URL</text>
    </g>
    <!-- Flow Lines -->
    <path d="M105,67 L210,67" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,2"/>
    <polygon points="210,67 202,63 202,71" fill="#ef4444"/>
    <text x="157" y="58" fill="#ef4444" font-size="8" font-family="monospace" text-anchor="middle">GET /profile/12346</text>
    <!-- Target Web App -->
    <g transform="translate(220, 30)">
      <rect x="0" y="0" width="90" height="75" rx="6" fill="#0f1322" stroke="#3b82f6" stroke-width="1.5"/>
      <text x="45" y="20" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Web Application</text>
      <text x="45" y="38" fill="#94a3b8" font-size="7" font-family="sans-serif" text-anchor="middle">No Authorization</text>
      <text x="45" y="50" fill="#94a3b8" font-size="7" font-family="sans-serif" text-anchor="middle">Check Performed!</text>
      <rect x="5" y="58" width="80" height="12" rx="2" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="0.5"/>
      <text x="45" y="67" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle" font-weight="bold">Bypassed Validation</text>
    </g>
    <!-- Victim DB Node -->
    <path d="M310,67 L360,67" fill="none" stroke="#34d399" stroke-width="1.5"/>
    <polygon points="360,67 352,63 352,71" fill="#34d399"/>
    <g transform="translate(370, 45)">
      <rect x="0" y="0" width="60" height="45" rx="6" fill="#0f1322" stroke="#34d399" stroke-width="1.5"/>
      <text x="30" y="20" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">User 12346</text>
      <text x="30" y="34" fill="#34d399" font-size="7" font-family="monospace" text-anchor="middle">Data Exposed</text>
    </g>
  </svg>
</div>"""

# 2. Security Misconfiguration (Slide 12)
# Detail: Default credentials, exposed files, stack traces
SVG_A02 = """<div class="cyber-diag-wrapper">
  <div class="diag-title">📊 Graphic: A02 - Security Misconfiguration Vulnerabilities</div>
  <svg viewBox="0 0 450 160" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #03050a; border-radius: 8px;">
    <!-- Server Node -->
    <g transform="translate(30, 20)">
      <rect x="0" y="0" width="120" height="110" rx="8" fill="#0f1322" stroke="#a855f7" stroke-width="1.5"/>
      <text x="60" y="22" fill="#ffffff" font-size="10" font-family="sans-serif" font-weight="bold" text-anchor="middle">Target Server</text>
      
      <!-- Fault 1: Default Creds -->
      <g transform="translate(10, 35)">
        <rect x="0" y="0" width="100" height="18" rx="3" fill="rgba(239, 68, 68, 0.1)" stroke="#ef4444" stroke-width="0.75"/>
        <text x="50" y="11" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">Default admin:admin</text>
      </g>
      <!-- Fault 2: Directory Listing -->
      <g transform="translate(10, 60)">
        <rect x="0" y="0" width="100" height="18" rx="3" fill="rgba(239, 68, 68, 0.1)" stroke="#ef4444" stroke-width="0.75"/>
        <text x="50" y="11" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">Directory Listing ON</text>
      </g>
      <!-- Fault 3: Debug Mode -->
      <g transform="translate(10, 85)">
        <rect x="0" y="0" width="100" height="18" rx="3" fill="rgba(239, 68, 68, 0.1)" stroke="#ef4444" stroke-width="0.75"/>
        <text x="50" y="11" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">Debug Stack Traces</text>
      </g>
    </g>
    
    <!-- Flow -->
    <path d="M150,75 L290,75" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,2"/>
    <polygon points="290,75 282,71 282,79" fill="#ef4444"/>
    <text x="220" y="65" fill="#ef4444" font-size="8" font-family="monospace" text-anchor="middle">Exposes Config & Passwords</text>
    
    <!-- Attacker Node -->
    <g transform="translate(305, 45)">
      <rect x="0" y="0" width="110" height="55" rx="6" fill="#0f1322" stroke="#ef4444" stroke-width="1.5"/>
      <text x="55" y="20" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">External Attacker</text>
      <text x="55" y="34" fill="#ef4444" font-size="7" font-family="sans-serif" text-anchor="middle">Gains Server Access</text>
      <text x="55" y="45" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">via default login</text>
    </g>
  </svg>
</div>"""

# 3. Software Supply Chain Failures (Slide 14 - SolarWinds Orion flow)
# Detail: Vulnerable system -> Target Privileged Software -> Victims -> Protected Systems -> Final Target
SVG_A03 = """<div class="cyber-diag-wrapper">
  <div class="diag-title">📊 Graphic: A03 - SolarWinds Orion Supply Chain Attack Flow</div>
  <svg viewBox="0 0 460 170" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #03050a; border-radius: 8px;">
    <!-- SolarWinds Server -->
    <g transform="translate(10, 45)">
      <rect x="0" y="0" width="70" height="50" rx="4" fill="#0f1322" stroke="#3b82f6" stroke-width="1"/>
      <text x="35" y="16" fill="#ffffff" font-size="7" font-family="sans-serif" font-weight="bold" text-anchor="middle">SolarWinds</text>
      <text x="35" y="28" fill="#94a3b8" font-size="6" font-family="sans-serif" text-anchor="middle">Update FTP Server</text>
      <rect x="4" y="36" width="62" height="10" rx="1.5" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="0.5"/>
      <text x="35" y="43" fill="#ef4444" font-size="5.5" font-family="monospace" text-anchor="middle">Initial Malware</text>
    </g>
    
    <path d="M80,70 L115,70" fill="none" stroke="#3b82f6" stroke-width="1"/>
    
    <!-- Orion App -->
    <g transform="translate(120, 45)">
      <rect x="0" y="0" width="70" height="50" rx="4" fill="#0f1322" stroke="#fbbf24" stroke-width="1"/>
      <text x="35" y="18" fill="#ffffff" font-size="7" font-family="sans-serif" font-weight="bold" text-anchor="middle">Orion Software</text>
      <text x="35" y="30" fill="#94a3b8" font-size="6" font-family="sans-serif" text-anchor="middle">Privileged App</text>
      <text x="35" y="42" fill="#fbbf24" font-size="6" font-family="monospace" text-anchor="middle">Malicious Update</text>
    </g>
    
    <!-- Branching lines to victims -->
    <path d="M190,70 L215,45" fill="none" stroke="#ef4444" stroke-width="1"/>
    <path d="M190,70 L215,70" fill="none" stroke="#ef4444" stroke-width="1"/>
    <path d="M190,70 L215,95" fill="none" stroke="#ef4444" stroke-width="1"/>
    
    <!-- Victims (Organizations using Orion) -->
    <g transform="translate(220, 20)">
      <!-- Victim 1 -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="65" height="20" rx="3" fill="#0f1322" stroke="#ef4444" stroke-width="1"/>
        <text x="32" y="12" fill="#ffffff" font-size="6.5" font-family="sans-serif" text-anchor="middle">Gov. Agency</text>
      </g>
      <!-- Victim 2 -->
      <g transform="translate(0, 35)">
        <rect x="0" y="0" width="65" height="20" rx="3" fill="#0f1322" stroke="#ef4444" stroke-width="1"/>
        <text x="32" y="12" fill="#ffffff" font-size="6.5" font-family="sans-serif" text-anchor="middle">Enterprise</text>
      </g>
      <!-- Victim 3 -->
      <g transform="translate(0, 70)">
        <rect x="0" y="0" width="65" height="20" rx="3" fill="#0f1322" stroke="#ef4444" stroke-width="1"/>
        <text x="32" y="12" fill="#ffffff" font-size="6.5" font-family="sans-serif" text-anchor="middle">Infrastructure</text>
      </g>
      <text x="32" y="105" fill="#ef4444" font-size="6" font-family="monospace" text-anchor="middle">Pwned via backdoor</text>
    </g>
    
    <!-- Lines to Protected Systems -->
    <path d="M285,30 L320,45" fill="none" stroke="#ef4444" stroke-width="1"/>
    <path d="M285,45 L320,70" fill="none" stroke="#ef4444" stroke-width="1"/>
    <path d="M285,90 L320,95" fill="none" stroke="#ef4444" stroke-width="1"/>
    
    <!-- Protected Systems -->
    <g transform="translate(325, 30)">
      <rect x="0" y="0" width="55" height="80" rx="4" fill="#0f1322" stroke="#34d399" stroke-width="1"/>
      <text x="27" y="16" fill="#ffffff" font-size="7" font-family="sans-serif" font-weight="bold" text-anchor="middle">Protected</text>
      <text x="27" y="28" fill="#ffffff" font-size="7" font-family="sans-serif" font-weight="bold" text-anchor="middle">Systems</text>
      <rect x="4" y="38" width="47" height="10" rx="1.5" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="0.5"/>
      <text x="27" y="45" fill="#ef4444" font-size="5" font-family="monospace" text-anchor="middle">Malware injected</text>
      <text x="27" y="64" fill="#94a3b8" font-size="6.5" font-family="sans-serif" text-anchor="middle">Controlled</text>
      <text x="27" y="73" fill="#94a3b8" font-size="6.5" font-family="sans-serif" text-anchor="middle">by Backdoor</text>
    </g>
    
    <path d="M380,70 L400,70" fill="none" stroke="#ef4444" stroke-width="1"/>
    
    <!-- Final Target -->
    <g transform="translate(405, 50)">
      <circle cx="20" cy="20" r="18" fill="#0f1322" stroke="#ef4444" stroke-width="1"/>
      <text x="20" y="18" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle" font-weight="bold">Sensitive</text>
      <text x="20" y="27" fill="#ef4444" font-size="6.5" font-family="monospace" text-anchor="middle">Data</text>
    </g>
  </svg>
</div>"""

# 4. Cryptographic Failures (Slide 16)
# Detail: Weak md5, cleartext databases
SVG_A04 = """<div class="cyber-diag-wrapper">
  <div class="diag-title">📊 Graphic: A04 - Cryptographic Failures & Weak Hashing</div>
  <svg viewBox="0 0 450 160" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #03050a; border-radius: 8px;">
    <!-- User Input -->
    <g transform="translate(30, 50)">
      <rect x="0" y="0" width="80" height="40" rx="4" fill="#0f1322" stroke="#3b82f6" stroke-width="1.2"/>
      <text x="40" y="16" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">User Password</text>
      <text x="40" y="29" fill="#00f0ff" font-size="8" font-family="monospace" text-anchor="middle">"pass1234"</text>
    </g>
    
    <!-- Weak Encryption Process -->
    <path d="M110,70 L170,70" fill="none" stroke="#ef4444" stroke-width="1.2"/>
    <polygon points="170,70 164,66 164,74" fill="#ef4444"/>
    <text x="140" y="60" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">MD5 Hash</text>
    
    <!-- Insecure Database -->
    <g transform="translate(180, 25)">
      <rect x="0" y="0" width="110" height="90" rx="6" fill="#0f1322" stroke="#ef4444" stroke-width="1.5"/>
      <text x="55" y="18" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Insecure Database</text>
      <!-- Row 1 -->
      <text x="10" y="40" fill="#94a3b8" font-size="7" font-family="monospace">admin : 5f4dcc3b5aa...</text>
      <!-- Row 2 -->
      <text x="10" y="55" fill="#94a3b8" font-size="7" font-family="monospace">user1 : plainPassword</text>
      <line x1="5" y1="65" x2="105" y2="65" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>
      <text x="55" y="78" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">No Salt / Weak Hash</text>
    </g>
    
    <!-- Attacker cracking -->
    <path d="M290,70 L340,70" fill="none" stroke="#ef4444" stroke-width="1.2"/>
    <polygon points="340,70 334,66 334,74" fill="#ef4444"/>
    
    <g transform="translate(350, 45)">
      <rect x="0" y="0" width="70" height="50" rx="4" fill="#0f1322" stroke="#ef4444" stroke-width="1.2"/>
      <text x="35" y="18" fill="#ffffff" font-size="8" font-family="sans-serif" font-weight="bold" text-anchor="middle">Attacker</text>
      <text x="35" y="32" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">Decodes MD5</text>
      <text x="35" y="42" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">in seconds!</text>
    </g>
  </svg>
</div>"""

# 5. Injection (Slide 18)
# Detail: Attacker -> Web API Server -> Password Database with UNION SELECT/Command Injection payload
SVG_A05 = """<div class="cyber-diag-wrapper">
  <div class="diag-title">📊 Graphic: A05 - Injection Attack Vector Flow</div>
  <svg viewBox="0 0 450 160" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #03050a; border-radius: 8px;">
    <!-- Attacker Node -->
    <g transform="translate(20, 45)">
      <rect x="0" y="0" width="90" height="50" rx="6" fill="#0f1322" stroke="#ef4444" stroke-width="1.5" class="pulse-node"/>
      <text x="45" y="18" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Attacker</text>
      <text x="45" y="32" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">Injects SQL / Cmd</text>
      <text x="45" y="42" fill="#ef4444" font-size="6.5" font-family="monospace" text-anchor="middle">' UNION SELECT...</text>
    </g>
    
    <!-- Query Injection -->
    <path d="M110,60 L200,60" fill="none" stroke="#ef4444" stroke-width="1.2"/>
    <polygon points="200,60 194,56 194,64" fill="#ef4444"/>
    <text x="155" y="52" fill="#ef4444" font-size="7.5" font-family="monospace" text-anchor="middle">1. Sends malicious input</text>

    <!-- Response data -->
    <path d="M200,85 L110,85" fill="none" stroke="#34d399" stroke-width="1.2" stroke-dasharray="3,2"/>
    <polygon points="110,85 116,89 116,81" fill="#34d399"/>
    <text x="155" y="100" fill="#34d399" font-size="7.5" font-family="monospace" text-anchor="middle">4. Exfiltrated database data</text>
    
    <!-- Web Server Node -->
    <g transform="translate(210, 35)">
      <rect x="0" y="0" width="100" height="70" rx="6" fill="#0f1322" stroke="#3b82f6" stroke-width="1.5"/>
      <text x="50" y="18" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Web API Server</text>
      <text x="50" y="34" fill="#94a3b8" font-size="7" font-family="sans-serif" text-anchor="middle">No input filter</text>
      <text x="50" y="46" fill="#ef4444" font-size="6.5" font-family="monospace" text-anchor="middle">2. Evaluates query</text>
      <text x="50" y="58" fill="#94a3b8" font-size="6.5" font-family="sans-serif" text-anchor="middle">direct to DB</text>
    </g>
    
    <!-- Database server -->
    <path d="M310,60 L360,60" fill="none" stroke="#ef4444" stroke-width="1.2"/>
    <polygon points="360,60 354,56 354,64" fill="#ef4444"/>
    
    <path d="M360,80 L310,80" fill="none" stroke="#34d399" stroke-width="1.2"/>
    <polygon points="310,80 316,84 316,76" fill="#34d399"/>
    <text x="335" y="94" fill="#34d399" font-size="7" font-family="monospace" text-anchor="middle">3. Data output</text>

    <!-- DB Icon/Node -->
    <g transform="translate(370, 35)">
      <rect x="0" y="0" width="60" height="70" rx="6" fill="#0f1322" stroke="#34d399" stroke-width="1.5"/>
      <text x="30" y="24" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Password</text>
      <text x="30" y="36" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Database</text>
      <text x="30" y="52" fill="#34d399" font-size="8" font-family="monospace" text-anchor="middle">SQLite/MySQL</text>
    </g>
  </svg>
</div>"""

# 6. Insecure Design (Slide 20)
# Detail: Direct password changes allowed, no rate limits, brute force allowed
SVG_A06 = """<div class="cyber-diag-wrapper">
  <div class="diag-title">📊 Graphic: A06 - Insecure Design Attack Vectors</div>
  <svg viewBox="0 0 450 160" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #03050a; border-radius: 8px;">
    <!-- Flow showing lack of old password verification or lock limits -->
    <g transform="translate(30, 45)">
      <rect x="0" y="0" width="100" height="50" rx="6" fill="#0f1322" stroke="#fbbf24" stroke-width="1.2"/>
      <text x="50" y="18" fill="#ffffff" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Change Password</text>
      <text x="50" y="32" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">No Old Password Req</text>
      <text x="50" y="42" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">No Rate Limiting</text>
    </g>
    
    <path d="M130,70 L210,70" fill="none" stroke="#ef4444" stroke-width="1.5"/>
    <polygon points="210,70 204,66 204,74" fill="#ef4444"/>
    <text x="170" y="60" fill="#ef4444" font-size="8" font-family="monospace" text-anchor="middle">CSRF Exploit</text>
    
    <!-- Target site -->
    <g transform="translate(220, 35)">
      <rect x="0" y="0" width="100" height="70" rx="6" fill="#0f1322" stroke="#3b82f6" stroke-width="1.5"/>
      <text x="50" y="20" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Vulnerable API</text>
      <text x="50" y="38" fill="#94a3b8" font-size="7" font-family="sans-serif" text-anchor="middle">Accepts direct POST</text>
      <rect x="5" y="48" width="90" height="15" rx="2" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="0.5"/>
      <text x="50" y="58" fill="#ef4444" font-size="7.5" font-family="monospace" text-anchor="middle" font-weight="bold">Password Changed!</text>
    </g>
    
    <!-- Hacker gains account -->
    <path d="M320,70 L360,70" fill="none" stroke="#34d399" stroke-width="1.5"/>
    <polygon points="360,70 354,66 354,74" fill="#34d399"/>
    
    <g transform="translate(370, 45)">
      <rect x="0" y="0" width="60" height="50" rx="4" fill="#0f1322" stroke="#34d399" stroke-width="1.2"/>
      <text x="30" y="20" fill="#ffffff" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Hijacked</text>
      <text x="30" y="34" fill="#34d399" font-size="7.5" font-family="monospace" text-anchor="middle">User Account</text>
    </g>
  </svg>
</div>"""

# 7. Authentication Failures (Slide 22 - Credential Stuffing flow)
# Detail: Attacker -> Stolen Logins -> Bots -> Victims Websites
SVG_A07 = """<div class="cyber-diag-wrapper">
  <div class="diag-title">📊 Graphic: A07 - Credential Stuffing & Botnets Flow</div>
  <svg viewBox="0 0 450 170" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #03050a; border-radius: 8px;">
    <!-- Attacker Node -->
    <g transform="translate(15, 60)">
      <rect x="0" y="0" width="80" height="40" rx="6" fill="#0f1322" stroke="#ef4444" stroke-width="1.5" class="pulse-node"/>
      <text x="40" y="18" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Attacker</text>
      <text x="40" y="30" fill="#ef4444" font-size="7.5" font-family="monospace" text-anchor="middle">Stolen Logins</text>
    </g>
    
    <!-- Flow Lines to Bots -->
    <path d="M95,80 L135,50" fill="none" stroke="#ef4444" stroke-width="1"/>
    <path d="M95,80 L135,80" fill="none" stroke="#ef4444" stroke-width="1"/>
    <path d="M95,80 L135,110" fill="none" stroke="#ef4444" stroke-width="1"/>
    
    <!-- Bots fleet -->
    <g transform="translate(140, 30)">
      <!-- Bot 1 -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="60" height="20" rx="3" fill="#0f1322" stroke="#fbbf24" stroke-width="1"/>
        <text x="30" y="13" fill="#fbbf24" font-size="7" font-family="monospace" text-anchor="middle">Bot Node 01</text>
      </g>
      <!-- Bot 2 -->
      <g transform="translate(0, 35)">
        <rect x="0" y="0" width="60" height="20" rx="3" fill="#0f1322" stroke="#fbbf24" stroke-width="1"/>
        <text x="30" y="13" fill="#fbbf24" font-size="7" font-family="monospace" text-anchor="middle">Bot Node 02</text>
      </g>
      <!-- Bot 3 -->
      <g transform="translate(0, 70)">
        <rect x="0" y="0" width="60" height="20" rx="3" fill="#0f1322" stroke="#fbbf24" stroke-width="1"/>
        <text x="30" y="13" fill="#fbbf24" font-size="7" font-family="monospace" text-anchor="middle">Bot Node 03</text>
      </g>
    </g>
    
    <!-- Flow from Bots to Target Sites -->
    <path d="M200,40 L245,30" fill="none" stroke="#ef4444" stroke-width="1"/>
    <path d="M200,80 L245,80" fill="none" stroke="#ef4444" stroke-width="1"/>
    <path d="M200,100 L245,130" fill="none" stroke="#ef4444" stroke-width="1"/>
    
    <!-- Target Victims Websites -->
    <g transform="translate(250, 15)">
      <!-- Web 1 -->
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="105" height="30" rx="4" fill="#0f1322" stroke="#3b82f6" stroke-width="1"/>
        <text x="52" y="14" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">Target Web App A</text>
        <text x="52" y="24" fill="#ef4444" font-size="6.5" font-family="monospace" text-anchor="middle">Attempt Failed</text>
      </g>
      <!-- Web 2 -->
      <g transform="translate(0, 45)">
        <rect x="0" y="0" width="105" height="30" rx="4" fill="#0f1322" stroke="#3b82f6" stroke-width="1"/>
        <text x="52" y="14" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">Target Web App B</text>
        <text x="52" y="24" fill="#34d399" font-size="6.5" font-family="monospace" text-anchor="middle" font-weight="bold">Access Granted! ✔</text>
      </g>
      <!-- Web 3 -->
      <g transform="translate(0, 90)">
        <rect x="0" y="0" width="105" height="30" rx="4" fill="#0f1322" stroke="#3b82f6" stroke-width="1"/>
        <text x="52" y="14" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">Target Web App C</text>
        <text x="52" y="24" fill="#ef4444" font-size="6.5" font-family="monospace" text-anchor="middle">Attempt Failed</text>
      </g>
      <text x="52" y="132" fill="#ef4444" font-size="6.5" font-family="sans-serif" text-anchor="middle">Tests credentials automatically</text>
    </g>
  </svg>
</div>"""

# 8. Software and Data Integrity Failures (Slide 24)
# Detail: Tampering, unsigned updates
SVG_A08 = """<div class="cyber-diag-wrapper">
  <div class="diag-title">📊 Graphic: A08 - Software and Data Integrity Failures</div>
  <svg viewBox="0 0 450 160" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #03050a; border-radius: 8px;">
    <!-- Package Repository -->
    <g transform="translate(30, 45)">
      <rect x="0" y="0" width="80" height="50" rx="4" fill="#0f1322" stroke="#3b82f6" stroke-width="1.2"/>
      <text x="40" y="18" fill="#ffffff" font-size="8" font-family="sans-serif" font-weight="bold" text-anchor="middle">NPM / PyPI</text>
      <text x="40" y="32" fill="#94a3b8" font-size="6.5" font-family="sans-serif" text-anchor="middle">Unsigned Lib</text>
      <text x="40" y="42" fill="#fbbf24" font-size="7" font-family="monospace" text-anchor="middle">Package.tar.gz</text>
    </g>
    
    <!-- Tampering -->
    <path d="M110,70 L210,70" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4,2"/>
    <polygon points="210,70 204,66 204,74" fill="#ef4444"/>
    
    <!-- Hacker injects -->
    <g transform="translate(130, 15)">
      <circle cx="15" cy="8" r="6" fill="#ef4444"/>
      <path d="M5,22 C5,14 25,14 25,22 Z" fill="#ef4444"/>
      <text x="55" y="15" fill="#ef4444" font-size="7" font-family="sans-serif">Malicious payload injected</text>
    </g>
    
    <!-- CI/CD Build Target -->
    <g transform="translate(220, 45)">
      <rect x="0" y="0" width="90" height="50" rx="6" fill="#0f1322" stroke="#ef4444" stroke-width="1.5"/>
      <text x="45" y="18" fill="#ffffff" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Deployment</text>
      <text x="45" y="32" fill="#ef4444" font-size="7" font-family="sans-serif" text-anchor="middle">No verification check</text>
      <text x="45" y="43" fill="#ef4444" font-size="6.5" font-family="monospace" text-anchor="middle">Backdoor deployed!</text>
    </g>
    
    <!-- Output -->
    <path d="M310,70 L360,70" fill="none" stroke="#ef4444" stroke-width="1.2"/>
    <polygon points="360,70 354,66 354,74" fill="#ef4444"/>
    
    <g transform="translate(370, 45)">
      <rect x="0" y="0" width="60" height="50" rx="4" fill="#0f1322" stroke="#ef4444" stroke-width="1.2"/>
      <text x="30" y="20" fill="#ffffff" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Compromised</text>
      <text x="30" y="34" fill="#ef4444" font-size="7.5" font-family="monospace" text-anchor="middle">Production Server</text>
    </g>
  </svg>
</div>"""

# 9. Security Logging and Monitoring Failures (Slide 26)
# Detail: Silent attacks, no log auditing
SVG_A09 = """<div class="cyber-diag-wrapper">
  <div class="diag-title">📊 Graphic: A09 - Logging and Auditing Failures</div>
  <svg viewBox="0 0 450 160" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #03050a; border-radius: 8px;">
    <!-- Attacker running scans -->
    <g transform="translate(30, 45)">
      <rect x="0" y="0" width="90" height="50" rx="4" fill="#0f1322" stroke="#ef4444" stroke-width="1.2"/>
      <text x="45" y="20" fill="#ffffff" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Attacker</text>
      <text x="45" y="34" fill="#ef4444" font-size="7.5" font-family="monospace" text-anchor="middle">Sends 10,000 requests</text>
    </g>
    
    <path d="M120,70 L210,70" fill="none" stroke="#ef4444" stroke-width="1.5"/>
    <polygon points="210,70 204,66 204,74" fill="#ef4444"/>
    
    <!-- Target site console -->
    <g transform="translate(220, 30)">
      <rect x="0" y="0" width="100" height="80" rx="6" fill="#0f1322" stroke="#3b82f6" stroke-width="1.5"/>
      <text x="50" y="20" fill="#ffffff" font-size="9" font-family="sans-serif" font-weight="bold" text-anchor="middle">Web Server</text>
      <!-- Log display: empty -->
      <rect x="10" y="35" width="80" height="35" rx="3" fill="#020408" stroke="rgba(239, 68, 68, 0.3)" stroke-width="1"/>
      <text x="50" y="47" fill="#64748b" font-size="7" font-family="monospace" text-anchor="middle">Server Log:</text>
      <text x="50" y="58" fill="#ef4444" font-size="6.5" font-family="monospace" text-anchor="middle" font-weight="bold">[Empty / Null]</text>
    </g>
    
    <path d="M320,70 L360,70" fill="none" stroke="#ef4444" stroke-width="1.2"/>
    <polygon points="360,70 354,66 354,74" fill="#ef4444"/>
    
    <g transform="translate(370, 45)">
      <rect x="0" y="0" width="60" height="50" rx="4" fill="#0f1322" stroke="#ef4444" stroke-width="1.2"/>
      <text x="30" y="18" fill="#ffffff" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Undetected</text>
      <text x="30" y="30" fill="#ef4444" font-size="7.5" font-family="monospace" text-anchor="middle">Breach</text>
      <text x="30" y="42" fill="#ef4444" font-size="7.5" font-family="monospace" text-anchor="middle">for weeks</text>
    </g>
  </svg>
</div>"""

# 10. Mishandling of Exceptional Conditions (Slide 28)
# Detail: Error handling fails open, skipping auth check
SVG_A10 = """<div class="cyber-diag-wrapper">
  <div class="diag-title">📊 Graphic: A10 - Exception Bypass Flow</div>
  <svg viewBox="0 0 450 160" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #03050a; border-radius: 8px;">
    <!-- Invalid input -->
    <g transform="translate(20, 50)">
      <rect x="0" y="0" width="90" height="40" rx="4" fill="#0f1322" stroke="#3b82f6" stroke-width="1.2"/>
      <text x="45" y="16" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Unexpected Input</text>
      <text x="45" y="29" fill="#00f0ff" font-size="8" font-family="monospace" text-anchor="middle">null / malformed</text>
    </g>
    
    <path d="M110,70 L170,70" fill="none" stroke="#ef4444" stroke-width="1.2"/>
    <polygon points="170,70 164,66 164,74" fill="#ef4444"/>
    <text x="140" y="60" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">Trigger Error</text>
    
    <!-- Code Exec -->
    <g transform="translate(180, 25)">
      <rect x="0" y="0" width="120" height="90" rx="6" fill="#0f1322" stroke="#ef4444" stroke-width="1.5"/>
      <text x="60" y="18" fill="#ffffff" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Application logic</text>
      <text x="60" y="32" fill="#94a3b8" font-size="7" font-family="monospace">try {</text>
      <text x="65" y="47" fill="#ef4444" font-size="7.5" font-family="monospace" font-weight="bold">  checkAuth(); // Error!</text>
      <text x="60" y="62" fill="#94a3b8" font-size="7" font-family="monospace">} catch {</text>
      <rect x="8" y="68" width="104" height="16" rx="2" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="0.5"/>
      <text x="60" y="79" fill="#ef4444" font-size="7.5" font-family="monospace" text-anchor="middle" font-weight="bold">  // Fails open! (No halt)</text>
    </g>
    
    <path d="M300,70 L350,70" fill="none" stroke="#34d399" stroke-width="1.2"/>
    <polygon points="350,70 344,66 344,74" fill="#34d399"/>
    
    <g transform="translate(360, 45)">
      <rect x="0" y="0" width="70" height="50" rx="4" fill="#0f1322" stroke="#34d399" stroke-width="1.2"/>
      <text x="35" y="18" fill="#ffffff" font-size="8.5" font-family="sans-serif" font-weight="bold" text-anchor="middle">Access Allowed</text>
      <text x="35" y="32" fill="#34d399" font-size="7" font-family="monospace" text-anchor="middle">Auth check skipped</text>
      <text x="35" y="42" fill="#34d399" font-size="7" font-family="monospace" text-anchor="middle">due to error</text>
    </g>
  </svg>
</div>"""

with app.app_context():
    from CTFd.plugins.tutorials import TutorialLesson
    db = app.db
    lesson = db.session.query(TutorialLesson).filter_by(id=177).first()
    if not lesson:
        print("[!] Lesson 177 not found")
        sys.exit(1)

    blocks = json.loads(lesson.content)
    val = blocks[0].get('value', '')

    # Define our replacements from the current state (which has <img src="/themes/core/static/lessons/Chapter05/...png" />)
    replacements = {
        r'<div style=\"background: rgba\(255,255,255,0\.01\); border: 1px solid rgba\(255,255,255,0\.04\); border-radius: 8px; padding: 14px; text-align: center;\">\s*<div style=\"font-size: 0\.72rem; color: #94a3b8; margin-bottom: 12px; font-weight: bold; text-transform: uppercase;\">📊 Graphic: Access Control vs Broken Access Control</div>\s*<img[^>]*src=\"/themes/core/static/lessons/Chapter05/page-010\.png\"[^>]*>\s*</div>': SVG_A01,
        
        r'<div style=\"background: rgba\(255,255,255,0\.01\); border: 1px solid rgba\(255,255,255,0\.04\); border-radius: 8px; padding: 14px; text-align: center;\">\s*<div style=\"font-size: 0\.72rem; color: #94a3b8; margin-bottom: 12px; font-weight: bold; text-transform: uppercase;\">📊 Graphic: Security Misconfiguration</div>\s*<img[^>]*src=\"/themes/core/static/lessons/Chapter05/page-012\.png\"[^>]*>\s*</div>': SVG_A02,
        
        r'<div style=\"background: rgba\(255,255,255,0\.01\); border: 1px solid rgba\(255,255,255,0\.04\); border-radius: 8px; padding: 14px; text-align: center;\">\s*<div style=\"font-size: 0\.72rem; color: #94a3b8; margin-bottom: 12px; font-weight: bold; text-transform: uppercase;\">📊 Graphic: Software Supply Chain</div>\s*<img[^>]*src=\"/themes/core/static/lessons/Chapter05/page-014\.png\"[^>]*>\s*</div>': SVG_A03,
        
        r'<div style=\"background: rgba\(255,255,255,0\.01\); border: 1px solid rgba\(255,255,255,0\.04\); border-radius: 8px; padding: 14px; text-align: center;\">\s*<div style=\"font-size: 0\.72rem; color: #94a3b8; margin-bottom: 12px; font-weight: bold; text-transform: uppercase;\">📊 Graphic: Cryptographic Failures</div>\s*<img[^>]*src=\"/themes/core/static/lessons/Chapter05/page-016\.png\"[^>]*>\s*</div>': SVG_A04,
        
        r'<div style=\"background: rgba\(255,255,255,0\.01\); border: 1px solid rgba\(255,255,255,0\.04\); border-radius: 8px; padding: 14px; text-align: center;\">\s*<div style=\"font-size: 0\.72rem; color: #94a3b8; margin-bottom: 12px; font-weight: bold; text-transform: uppercase;\">📊 Graphic: SQL Injection</div>\s*<img[^>]*src=\"/themes/core/static/lessons/Chapter05/page-018\.png\"[^>]*>\s*</div>': SVG_A05,
        
        r'<div style=\"background: rgba\(255,255,255,0\.01\); border: 1px solid rgba\(255,255,255,0\.04\); border-radius: 8px; padding: 14px; text-align: center;\">\s*<div style=\"font-size: 0\.72rem; color: #94a3b8; margin-bottom: 12px; font-weight: bold; text-transform: uppercase;\">📊 Graphic: Insecure Design \(No Rate Limit\)</div>\s*<img[^>]*src=\"/themes/core/static/lessons/Chapter05/page-020\.png\"[^>]*>\s*</div>': SVG_A06,
        
        r'<div style=\"background: rgba\(255,255,255,0\.01\); border: 1px solid rgba\(255,255,255,0\.04\); border-radius: 8px; padding: 14px; text-align: center;\">\s*<div style=\"font-size: 0\.72rem; color: #94a3b8; margin-bottom: 12px; font-weight: bold; text-transform: uppercase;\">📊 Graphic: Authentication Failure</div>\s*<img[^>]*src=\"/themes/core/static/lessons/Chapter05/page-022\.png\"[^>]*>\s*</div>': SVG_A07,
        
        r'<div style=\"background: rgba\(255,255,255,0\.01\); border: 1px solid rgba\(255,255,255,0\.04\); border-radius: 8px; padding: 14px; text-align: center;\">\s*<div style=\"font-size: 0\.72rem; color: #94a3b8; margin-bottom: 12px; font-weight: bold; text-transform: uppercase;\">📊 Graphic: Integrity Failure</div>\s*<img[^>]*src=\"/themes/core/static/lessons/Chapter05/page-024\.png\"[^>]*>\s*</div>': SVG_A08,
        
        r'<div style=\"background: rgba\(255,255,255,0\.01\); border: 1px solid rgba\(255,255,255,0\.04\); border-radius: 8px; padding: 14px; text-align: center;\">\s*<div style=\"font-size: 0\.72rem; color: #94a3b8; margin-bottom: 12px; font-weight: bold; text-transform: uppercase;\">📊 Graphic: Logging Failure</div>\s*<img[^>]*src=\"/themes/core/static/lessons/Chapter05/page-026\.png\"[^>]*>\s*</div>': SVG_A09,
        
        r'<div style=\"background: rgba\(255,255,255,0\.01\); border: 1px solid rgba\(255,255,255,0\.04\); border-radius: 8px; padding: 14px; text-align: center;\">\s*<div style=\"font-size: 0\.72rem; color: #94a3b8; margin-bottom: 12px; font-weight: bold; text-transform: uppercase;\">📊 Graphic: Exception Bypass</div>\s*<img[^>]*src=\"/themes/core/static/lessons/Chapter05/page-028\.png\"[^>]*>\s*</div>': SVG_A10,
    }

    # If the exact img tag didn't match the complex outer wrapper regex, let's also try replacing the img tag inside the existing wrapper.
    # We want to replace the whole graphic card wrapper or just the image with the SVG.
    # Let's do a direct replace since we know the content
    changed = False
    for pattern, new_svg in replacements.items():
        new_val = re.sub(pattern, new_svg, val, flags=re.DOTALL)
        if new_val != val:
            val = new_val
            changed = True

    # If the above didn't match due to minor whitespace differences, let's write a simple selector-based replacement
    # by matching the img tags directly and replacing them with the SVGs
    if not changed:
        print("[~] Complex pattern didn't match, trying direct image-to-svg replacement...")
        img_replacements = {
            r'<img[^>]*src=\"/themes/core/static/lessons/Chapter05/page-010\.png\"[^>]*>': SVG_A01,
            r'<img[^>]*src=\"/themes/core/static/lessons/Chapter05/page-012\.png\"[^>]*>': SVG_A02,
            r'<img[^>]*src=\"/themes/core/static/lessons/Chapter05/page-014\.png\"[^>]*>': SVG_A03,
            r'<img[^>]*src=\"/themes/core/static/lessons/Chapter05/page-016\.png\"[^>]*>': SVG_A04,
            r'<img[^>]*src=\"/themes/core/static/lessons/Chapter05/page-018\.png\"[^>]*>': SVG_A05,
            r'<img[^>]*src=\"/themes/core/static/lessons/Chapter05/page-020\.png\"[^>]*>': SVG_A06,
            r'<img[^>]*src=\"/themes/core/static/lessons/Chapter05/page-022\.png\"[^>]*>': SVG_A07,
            r'<img[^>]*src=\"/themes/core/static/lessons/Chapter05/page-024\.png\"[^>]*>': SVG_A08,
            r'<img[^>]*src=\"/themes/core/static/lessons/Chapter05/page-026\.png\"[^>]*>': SVG_A09,
            r'<img[^>]*src=\"/themes/core/static/lessons/Chapter05/page-028\.png\"[^>]*>': SVG_A10,
        }
        for pattern, new_svg in img_replacements.items():
            # We want to replace the whole enclosing card wrapper <div style=... text-align: center> ... <img ...> </div>
            # Since the outer wrapper is standard, we can find it by looking for the sibling title
            # Let's find the nearest enclosing div and replace it
            new_val = re.sub(pattern, new_svg, val, flags=re.DOTALL)
            if new_val != val:
                val = new_val
                changed = True

    if changed:
        blocks[0]['value'] = val
        lesson.content = json.dumps(blocks, ensure_ascii=False)
        db.session.commit()
        print("[OK] Lesson 177 Block 0 updated with highly accurate custom neon diagrams!")
    else:
        print("[!] No changes were made. Check if images are present in Block 0.")

    # Verification
    lesson = db.session.query(TutorialLesson).filter_by(id=177).first()
    blocks = json.loads(lesson.content)
    val = blocks[0].get('value', '')
    svgs = re.findall(r'<svg[^>]*>', val)
    imgs = re.findall(r'<img[^>]*src=\"/themes/core/static/[^\"]+\"[^>]*>', val)
    print(f"Verification: remaining SVGs={len(svgs)}, loaded slide images={len(imgs)}")
