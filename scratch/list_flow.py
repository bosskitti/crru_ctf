import json

transcript_path = "/home/kali/.gemini/antigravity/brain/c824c6d8-15e7-4399-b27b-1656c82fe65a/.system_generated/logs/transcript_full.jsonl"

with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            step = json.loads(line)
            step_index = step.get("step_index")
            if 2900 <= step_index <= 3120:
                print(f"Step {step_index}: source={step.get('source')} type={step.get('type')} tools={[c.get('name') for c in step.get('tool_calls', [])]}")
        except Exception as e:
            pass
