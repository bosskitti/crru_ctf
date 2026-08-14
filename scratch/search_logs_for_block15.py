import json
import os

log_dir = "/home/kali/.gemini/antigravity/brain/c824c6d8-15e7-4399-b27b-1656c82fe65a/.system_generated/logs/"
transcript_path = os.path.join(log_dir, "transcript.jsonl")

found = False
if os.path.exists(transcript_path):
    with open(transcript_path, "r", encoding="utf-8") as f:
        for line in f:
            if "Regular User" in line and "STANDARD USER" in line and "Service User" in line:
                # Let's print matching snippets
                idx = line.find("Regular User")
                print("Found match in transcript:")
                print(line[max(0, idx-500):idx+1500])
                found = True
                break

if not found:
    print("Not found in transcript, trying transcript_full...")
    transcript_full = os.path.join(log_dir, "transcript_full.jsonl")
    if os.path.exists(transcript_full):
        with open(transcript_full, "r", encoding="utf-8") as f:
            for line in f:
                if "Regular User" in line and "STANDARD USER" in line and "Service User" in line:
                    idx = line.find("Regular User")
                    print("Found match in transcript_full:")
                    print(line[max(0, idx-500):idx+1500])
                    break
