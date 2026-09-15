import json
import os
import sys
from CTFd import create_app
from CTFd.models import db
from CTFd.plugins.tutorials import TutorialLesson
from CTFd.utils import markdown

from create_lesson_179 import hero_banner_html, cms_masterclass_html
from create_lesson_179_part2 import cms_sandbox_html, cms_summary_html
from create_lesson_179_part3 import csrf_masterclass_html, csrf_summary_html
from create_lesson_179_part4 import clickjacking_masterclass_html, clickjacking_summary_html

def clean_html(text: str) -> str:
    """Ensure no blank lines exist inside HTML block so markdown parser doesn't inject <p> tags."""
    return '\n'.join([line.strip() for line in text.split('\n') if line.strip()])

def main():
    print("=== ASSEMBLING COMPREHENSIVE LESSON 179 ===")

    # Load quiz
    quiz_path = os.path.join(os.path.dirname(__file__), "b6_quiz.txt")
    with open(quiz_path, "r", encoding="utf-8") as f:
        quiz_raw = f.read()

    # Clean each component
    block0_html = clean_html(hero_banner_html + "\n" + cms_masterclass_html)
    block1_html = clean_html(cms_sandbox_html)
    block2_html = clean_html(cms_summary_html)
    block3_html = clean_html(csrf_masterclass_html)
    block5_html = clean_html(csrf_summary_html)
    block6_html = clean_html(clickjacking_masterclass_html)
    block8_html = clean_html(clickjacking_summary_html)
    block9_html = clean_html(quiz_raw)

    test_cards = [
        ("Block 0: Hero & CMS Masterclass", block0_html),
        ("Block 1: CMS Sandbox", block1_html),
        ("Block 2: CMS Hardening Debrief", block2_html),
        ("Block 3: CSRF Masterclass & Guide", block3_html),
        ("Block 5: CSRF Defense Debrief", block5_html),
        ("Block 6: Clickjacking Masterclass & Guide", block6_html),
        ("Block 8: Clickjacking Defense Debrief", block8_html),
        ("Block 9: Interactive Quick Quiz", block9_html),
    ]

    print("\n--- Testing Markdown Purity ---")
    all_clean = True
    for name, content in test_cards:
        rendered = markdown(content)
        # Note: Quiz might have <p> inside markdown questions or style tags, but debriefs & masterclasses should be pure HTML
        has_p = "<p>" in rendered
        has_escaped_div = "&lt;div" in rendered
        print(f"{name:42}: len={len(rendered):6}, has_<p>={has_p!s:5}, has_&lt;div={has_escaped_div!s:5}")
        if has_escaped_div:
            all_clean = False
            print(f"[!] Warning: &lt;div found in {name}!")

    # Compose 10 blocks:
    # 0: Hero & CMS Masterclass
    # 1: CMS Sandbox
    # 2: CMS Hardening Debrief
    # 3: CSRF Masterclass & Walkthrough
    # 4: Challenge 33
    # 5: CSRF Defense Debrief
    # 6: Clickjacking Masterclass & Walkthrough
    # 7: Challenge 34
    # 8: Clickjacking Defense Debrief
    # 9: Interactive Quick Quiz
    new_blocks = [
        {"type": "markdown", "value": block0_html},
        {"type": "markdown", "value": block1_html},
        {"type": "markdown", "value": block2_html},
        {"type": "markdown", "value": block3_html},
        {"type": "challenge", "value": "", "challenge_id": 33},
        {"type": "markdown", "value": block5_html},
        {"type": "markdown", "value": block6_html},
        {"type": "challenge", "value": "", "challenge_id": 34},
        {"type": "markdown", "value": block8_html},
        {"type": "markdown", "value": block9_html},
    ]

    print(f"\n[*] Total assembled blocks: {len(new_blocks)}")

    app = create_app()
    with app.app_context():
        lesson = TutorialLesson.query.get(179)
        if not lesson:
            print("[!] Error: Lesson 179 not found in DB!")
            sys.exit(1)

        print(f"[*] Found Lesson 179: '{lesson.title}'")

        # Save backup
        backup_path = os.path.join(os.path.dirname(__file__), "lesson_179_backup.json")
        with open(backup_path, "w", encoding="utf-8") as f:
            f.write(lesson.content)
        print(f"[*] Saved backup to {backup_path}")

        # Update lesson title to be comprehensive & clear
        lesson.title = "03. การโจมตีระบบจัดการเนื้อหาเว็บ (CMS Exploitation, CSRF & Clickjacking)"
        lesson.content = json.dumps(new_blocks, ensure_ascii=False)
        db.session.commit()
        print("\n[+] Successfully updated Lesson 179 in database!")

        # Verify blocks in DB
        updated_lesson = TutorialLesson.query.get(179)
        verified_blocks = json.loads(updated_lesson.content)
        print("\n=== Verified Blocks in Database ===")
        for idx, b in enumerate(verified_blocks):
            b_type = b.get("type")
            cid = b.get("challenge_id")
            val = b.get("value", "")
            first_line = val.strip().split("\n")[0] if val else ""
            print(f"[{idx:02d}] type={b_type:10} chall={str(cid):4} | {first_line[:65]}")

if __name__ == "__main__":
    main()
