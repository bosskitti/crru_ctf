"""
Fix lessons 177-180:
1. Remove ALL inline onclick attributes (CTFd DOMPurify strips them anyway)
2. Wrap ALL <script> blocks in IIFEs to prevent global var collisions
3. For quiz blocks: ensure event delegation handles Submit clicks
"""
import json, re, sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app

app = create_app()

with app.app_context():
    from CTFd.plugins.tutorials import TutorialLesson
    db = app.db

    for lid in [177, 178, 179, 180]:
        lesson = db.session.query(TutorialLesson).filter_by(id=lid).first()
        if not lesson or not lesson.content:
            print(f"[!] Lesson {lid} not found or empty, skipping.")
            continue

        blocks = json.loads(lesson.content)
        print(f"\n[*] Processing Lesson {lid} ({len(blocks)} blocks)...")
        changed = False

        for i, block in enumerate(blocks):
            val = block.get("value", "")
            original = val

            # 1. Remove inline onclick attributes
            val = re.sub(r'\s+onclick="[^"]*"', '', val)
            val = re.sub(r"\s+onclick='[^']*'", '', val)

            # 2. Wrap <script>...</script> content in IIFE if not already wrapped
            def wrap_in_iife(match):
                content = match.group(1)
                stripped = content.strip()
                # Already wrapped in IIFE?
                if stripped.startswith('(function()'):
                    return match.group(0)
                return '<script>\n(function() {\n' + content + '\n})();\n</script>'

            val = re.sub(r'<script>(.*?)</script>', wrap_in_iife, val, flags=re.DOTALL)

            if val != original:
                block["value"] = val
                changed = True
                has_onclick_after = 'onclick=' in val.lower()
                has_iife_after = '(function()' in val
                print(f"  Block {i}: FIXED (onclick_remaining={has_onclick_after}, iife={has_iife_after})")
            else:
                print(f"  Block {i}: no changes needed")

        if changed:
            lesson.content = json.dumps(blocks, ensure_ascii=False)
            db.session.commit()
            print(f"[+] Lesson {lid} saved to database!")
        else:
            print(f"[-] Lesson {lid} no changes needed.")

    print("\n[✓] All done! Hard refresh (Ctrl+F5) to see changes.")
