import json

# Let's search for step 3964
with open("/home/kali/.gemini/antigravity/brain/c824c6d8-15e7-4399-b27b-1656c82fe65a/.system_generated/logs/transcript_full.jsonl", "r") as f:
    for line in f:
        data = json.loads(line)
        if data.get("step_index") == 3964:
            print(data.get("content"))
            break
