import json
import os
import sys
from CTFd import create_app
from CTFd.models import db
from CTFd.plugins.tutorials import TutorialLesson
from CTFd.utils import markdown

from create_lab_summaries import (
    sqli_summary_html,
    cmdi_summary_html,
    lfi_summary_html,
    xss_summary_html,
    brute_summary_html,
)

def clean_html_block(html_text: str) -> str:
    """Ensure no blank lines exist inside HTML block so markdown parser doesn't inject <p> tags."""
    return '\n'.join([line.strip() for line in html_text.split('\n') if line.strip()])

def main():
    app = create_app()
    with app.app_context():
        lesson = TutorialLesson.query.get(178)
        if not lesson:
            print("[!] Lesson 178 not found!")
            sys.exit(1)

        print(f"[*] Found Lesson 178: '{lesson.title}'")
        blocks = json.loads(lesson.content)
        print(f"[*] Current total blocks: {len(blocks)}")

        # Check if already injected
        for i, b in enumerate(blocks):
            val = b.get("value", "")
            if "UNIFIED MASTERCLASS DEBRIEF: SQL INJECTION" in val:
                print(f"[!] Warning: SQL Injection summary already present at block {i}!")
                print("[!] Aborting to prevent duplicate insertion.")
                return

        # Backup current content
        backup_path = os.path.join(os.path.dirname(__file__), "lesson_178_backup.json")
        with open(backup_path, "w", encoding="utf-8") as f:
            f.write(lesson.content)
        print(f"[*] Saved backup to {backup_path}")

        # Clean all summary HTML cards
        cards = {
            "sqli": clean_html_block(sqli_summary_html),
            "cmdi": clean_html_block(cmdi_summary_html),
            "lfi": clean_html_block(lfi_summary_html),
            "xss": clean_html_block(xss_summary_html),
            "brute": clean_html_block(brute_summary_html),
        }

        # Verify markdown rendering
        for name, html in cards.items():
            rendered = markdown(html)
            if "<p>" in rendered:
                print(f"[!] Warning: <p> tag detected in {name} card rendering!")
            if "&lt;div" in rendered:
                print(f"[!] Warning: &lt;div detected in {name} card rendering!")

        # Prepare summary blocks
        sqli_block = {"type": "markdown", "value": cards["sqli"]}
        cmdi_block = {"type": "markdown", "value": cards["cmdi"]}
        lfi_block = {"type": "markdown", "value": cards["lfi"]}
        xss_block = {"type": "markdown", "value": cards["xss"]}
        brute_block = {"type": "markdown", "value": cards["brute"]}

        # Construct new blocks list:
        # Original:
        # 0..27: SQLi Intro & Labs 01-12 (ends at Chall 18)
        # 28..32: CMD Injection Intro & Labs CMD-1, 2 (ends at Chall 32)
        # 33..37: File Inclusion Intro & Labs LFI-1, 2 (ends at Chall 31)
        # 38..44: XSS Intro & Labs XSS-1, 2, 3 (ends at Chall 27)
        # 45..49: Brute Force Intro & Labs BRUTE-1, 2 (ends at Chall 29)
        # 50: Quick Quiz

        assert blocks[27].get("challenge_id") == 18, f"Block 27 expected chall 18, got {blocks[27]}"
        assert blocks[32].get("challenge_id") == 32, f"Block 32 expected chall 32, got {blocks[32]}"
        assert blocks[37].get("challenge_id") == 31, f"Block 37 expected chall 31, got {blocks[37]}"
        assert blocks[44].get("challenge_id") == 27, f"Block 44 expected chall 27, got {blocks[44]}"
        assert blocks[49].get("challenge_id") == 29, f"Block 49 expected chall 29, got {blocks[49]}"
        assert "Lesson Quick Quiz" in blocks[50].get("value", ""), f"Block 50 expected Quiz, got {blocks[50]}"

        new_blocks = (
            blocks[0:28]              # 0..27 (SQLi Labs 01-12)
            + [sqli_block]            # New Block 28
            + blocks[28:33]           # 28..32 -> Now 29..33 (CMD Injection Masterclass + Labs CMD-1, 2)
            + [cmdi_block]            # New Block 34
            + blocks[33:38]           # 33..37 -> Now 35..39 (File Inclusion Masterclass + Labs LFI-1, 2)
            + [lfi_block]             # New Block 40
            + blocks[38:45]           # 38..44 -> Now 41..47 (XSS Masterclass + Labs XSS-1, 2, 3)
            + [xss_block]             # New Block 48
            + blocks[45:50]           # 45..49 -> Now 49..53 (Brute Force Masterclass + Labs BRUTE-1, 2)
            + [brute_block]           # New Block 54
            + blocks[50:51]           # 50 -> Now 55 (Interactive Quick Quiz)
        )

        print(f"[*] Constructed new_blocks list: total {len(new_blocks)} blocks (expected 56)")
        assert len(new_blocks) == 56

        # Print block structure verification
        print("\n=== Block Sequence Verification ===")
        for idx, b in enumerate(new_blocks):
            b_type = b.get("type")
            cid = b.get("challenge_id")
            preview = (b.get("value") or "")[:45].replace("\n", " ")
            if "UNIFIED MASTERCLASS DEBRIEF" in preview:
                print(f" --> [{idx:02d}] *** SUMMARY DEBRIEF CARD ***: {preview}")
            elif b_type == "challenge":
                print(f"     [{idx:02d}] Challenge ID: {cid}")
            elif "Lesson Quick Quiz" in preview:
                print(f" --> [{idx:02d}] *** INTERACTIVE QUIZ ***")
            elif "<!-- ========================================== -->" in preview:
                print(f" --- [{idx:02d}] Category Header/Masterclass")

        lesson.content = json.dumps(new_blocks, ensure_ascii=False)
        db.session.commit()
        print("\n[+] Successfully updated TutorialLesson 178 content in database!")

if __name__ == "__main__":
    main()
