import json

transcript_path = "/home/kali/.gemini/antigravity/brain/c824c6d8-15e7-4399-b27b-1656c82fe65a/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            step = json.loads(line)
            if step.get("step_index") == 2986:
                print("CONTENT:")
                print(step.get("content"))
                print("TOOL CALLS:")
                print(step.get("tool_calls"))
        except Exception as e:
            pass
