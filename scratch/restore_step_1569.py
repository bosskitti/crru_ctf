import json

transcript_path = "/home/kali/.gemini/antigravity/brain/c824c6d8-15e7-4399-b27b-1656c82fe65a/.system_generated/logs/transcript_full.jsonl"
output_path = "/home/kali/crru_ctf/CTFd/term_w36_web_app_complete_v5.py"

with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            step = json.loads(line)
            if step.get("step_index") == 1569:
                tool_calls = step.get("tool_calls", [])
                for call in tool_calls:
                    if call.get("name") == "write_to_file":
                        code = call.get("args", {}).get("CodeContent")
                        if code:
                            # Strip any escaping if it's there, but json.loads does it already
                            with open(output_path, "w", encoding="utf-8") as out:
                                out.write(code)
                            print("SUCCESS: Extracted and wrote term_w36_web_app_complete_v5.py from Step 1569!")
                            exit(0)
        except Exception as e:
            print("Error parsing line:", e)
            
print("ERROR: Step 1569 or write_to_file code not found.")
