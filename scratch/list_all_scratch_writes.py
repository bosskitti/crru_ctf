import json

transcript_path = "/home/kali/.gemini/antigravity/brain/c824c6d8-15e7-4399-b27b-1656c82fe65a/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            step = json.loads(line)
            step_index = step.get("step_index")
            tool_calls = step.get("tool_calls", [])
            for call in tool_calls:
                name = call.get("name")
                args = call.get("args", {})
                if name == "write_to_file":
                    target_file = args.get("TargetFile", "")
                    if "scratch" in target_file and target_file.endswith(".py"):
                        # print filename only
                        filename = target_file.split("/")[-1]
                        print(f"Step {step_index}: {filename}")
        except Exception as e:
            pass
