import os

scratch_dir = "/home/kali/.gemini/antigravity/brain/c824c6d8-15e7-4399-b27b-1656c82fe65a/scratch"
for fname in os.listdir(scratch_dir):
    if fname.endswith(".py") or fname.endswith(".txt") or fname.endswith(".json"):
        fpath = os.path.join(scratch_dir, fname)
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
                if "SUPER USER" in content or "Standard User" in content or "Service User" in content:
                    print(f"Match found in file: {fname}")
                    # Print lines containing standard user
                    for i, line in enumerate(content.splitlines()):
                        if "SUPER USER" in line or "Standard User" in line or "Regular User" in line:
                            print(f"  Line {i+1}: {line[:120]}")
        except Exception as e:
            pass
