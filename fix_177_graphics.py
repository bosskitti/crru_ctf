"""
Fix Lesson 177 Block 0 graphics:
- Replace the manually drawn inline SVGs (which are incorrect/mismatched with slides)
  with the actual slide page images from /themes/core/static/lessons/Chapter05/page-010.png to page-028.png.
"""
import json, re, sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app

app = create_app()

GRAPHICS_MAPPING = {
    "Access Control vs Broken Access Control": "page-010.png",
    "Security Misconfiguration": "page-012.png",
    "Software Supply Chain": "page-014.png",
    "Cryptographic Failures": "page-016.png",
    "SQL Injection": "page-018.png",
    "Insecure Design (No Rate Limit)": "page-020.png",
    "Authentication Failure": "page-022.png",
    "Integrity Failure": "page-024.png",
    "Logging Failure": "page-026.png",
    "Exception Bypass": "page-028.png",
}

with app.app_context():
    from CTFd.plugins.tutorials import TutorialLesson
    db = app.db
    lesson = db.session.query(TutorialLesson).filter_by(id=177).first()
    if not lesson:
        print("[!] Lesson 177 not found")
        sys.exit(1)

    blocks = json.loads(lesson.content)
    val = blocks[0].get('value', '')

    # We will find every block matching:
    # <div style="background: rgba(255,255,255,0.01); border: 1px solid rgba(255,255,255,0.04); border-radius: 8px; padding: 14px; text-align: center;">
    # <div style="font-size: 0.72rem; color: #94a3b8; margin-bottom: 12px; font-weight: bold; text-transform: uppercase;">📊 Graphic: [Name]</div>
    # <svg ... > ... </svg>
    # </div>
    
    # We can write a regex to find each graphic card container
    pattern = r'(<div style="background: rgba\(255,255,255,0\.01\); border: 1px solid rgba\(255,255,255,0\.04\); border-radius: 8px; padding: 14px; text-align: center;">\s*<div style="font-size: 0\.72rem; color: #94a3b8; margin-bottom: 12px; font-weight: bold; text-transform: uppercase;">📊 Graphic: ([^<]+)</div>\s*)(<svg.*?</svg>)(\s*</div>)'
    
    def replacer(match):
        prefix = match.group(1)
        name = match.group(2).strip()
        svg_content = match.group(3)
        suffix = match.group(4)
        
        if name in GRAPHICS_MAPPING:
            img_file = GRAPHICS_MAPPING[name]
            img_url = f"/themes/core/static/lessons/Chapter05/{img_file}"
            print(f"[+] Replacing graphic '{name}' with image {img_file}")
            return f'{prefix}<img src="{img_url}" alt="{name}" style="max-width: 100%; height: auto; border-radius: 8px; border: 1px solid rgba(255,255,255,0.08); box-shadow: 0 8px 24px rgba(0,0,0,0.35); display: block; margin: 0 auto;" />{suffix}'
        else:
            print(f"[-] No mapping found for graphic '{name}', leaving unchanged")
            return match.group(0)

    new_val = re.sub(pattern, replacer, val, flags=re.DOTALL)
    
    if new_val != val:
        blocks[0]['value'] = new_val
        lesson.content = json.dumps(blocks, ensure_ascii=False)
        db.session.commit()
        print("[OK] Lesson 177 Block 0 slide graphics successfully replaced with actual slide images!")
    else:
        print("[!] No matches found for graphic replacement patterns. Please check regex.")

    # Quick Verification
    lesson = db.session.query(TutorialLesson).filter_by(id=177).first()
    blocks = json.loads(lesson.content)
    val = blocks[0].get('value', '')
    svgs = re.findall(r'<svg[^>]*>', val)
    imgs = re.findall(r'<img[^>]*src=\"/themes/core/static/[^\"]+\"[^>]*>', val)
    print(f"Verification: remaining SVGs={len(svgs)}, loaded slide images={len(imgs)}")
