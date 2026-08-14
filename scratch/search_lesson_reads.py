import json

transcript_path = "/home/kali/.gemini/antigravity/brain/c824c6d8-15e7-4399-b27b-1656c82fe65a/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            step = json.loads(line)
            step_index = step.get("step_index")
            content = step.get("content", "")
            if "Lesson 177" in content and "value" in content and len(content) > 10000:
                print(f"Step {step_index}: length of content={len(content)}")
        except Exception as e:
            pass
