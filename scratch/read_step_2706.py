import json

transcript_path = "/home/kali/.gemini/antigravity/brain/c824c6d8-15e7-4399-b27b-1656c82fe65a/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            step = json.loads(line)
            if step.get("step_index") == 2706:
                tool_calls = step.get("tool_calls", [])
                for call in tool_calls:
                    if call.get("name") == "write_to_file":
                        print(call.get("args", {}).get("CodeContent"))
        except Exception as e:
            pass
