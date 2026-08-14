import json

transcript_path = "/home/kali/.gemini/antigravity/brain/c824c6d8-15e7-4399-b27b-1656c82fe65a/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            step = json.loads(line)
            step_index = step.get("step_index")
            content = step.get("content", "")
            if "path_traversal_custom_diagram" in content:
                print(f"Step {step_index}: source={step.get('source')} type={step.get('type')}")
                # print a snippet around it
                idx = content.find("path_traversal_custom_diagram")
                print("Snippet:", content[max(0, idx-100):idx+100])
        except Exception as e:
            pass
