import json
import sys
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if not l:
        print("ERROR: Lesson 177 not found.")
        sys.exit(1)
        
    try:
        blocks = json.loads(l.content)
        print(f"Current number of blocks: {len(blocks)}")
        
        # We want to find the split position in Block 0
        val = blocks[0]["value"]
        
        # Target marker representing the end of status codes section
        target_str = "[🔗 คู่มือวิเคราะห์ HTTP Status Codes และการตรวจสอบสิทธิ์ความปลอดภัย](#http-status-codes-details)"
        idx = val.find(target_str)
        if idx == -1:
            print("ERROR: Target marker not found in Block 0.")
            sys.exit(1)
            
        # The split point should be right after the target string and subsequent newlines
        split_idx = idx + len(target_str)
        
        # We need to skip any trailing newlines/whitespace
        while split_idx < len(val) and val[split_idx].isspace():
            split_idx += 1
            
        part1 = val[:split_idx].strip()
        part2 = val[split_idx:].strip()
        
        print(f"Part 1 length: {len(part1)} characters")
        print(f"Part 2 length: {len(part2)} characters")
        
        # Check if the challenge block is already embedded to avoid duplicates
        # If there are already 5 blocks and block[1]["type"] is challenge, it's already done
        if len(blocks) == 5 and blocks[1]["type"] == "challenge":
            print("Challenge block is already embedded.")
            sys.exit(0)
            
        # Construct new blocks list
        new_blocks = [
            {
                "type": "markdown",
                "value": part1 + "\n\n"
            },
            {
                "type": "challenge",
                "challenge_id": 19
            },
            {
                "type": "markdown",
                "value": "\n\n" + part2
            },
            blocks[1],  # The sandbox (Block 1)
            blocks[2]   # The quiz (Block 2)
        ]
        
        l.content = json.dumps(new_blocks, ensure_ascii=False)
        app.db.session.commit()
        print("SUCCESS: Challenge 19 embedded as a native block inside Lesson 177!")
    except Exception as e:
        print("ERROR:", e)
        sys.exit(1)
