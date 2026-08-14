import json
import os
import subprocess
import sys

transcript_path = "/home/kali/.gemini/antigravity/brain/c824c6d8-15e7-4399-b27b-1656c82fe65a/.system_generated/logs/transcript_full.jsonl"
scratch_dir = "/home/kali/.gemini/antigravity/brain/c824c6d8-15e7-4399-b27b-1656c82fe65a/scratch"

# Complete chronological list of steps that wrote the update scripts (23 steps)
steps_to_extract = [
    (2643, "update_lesson_177_ultimate.py"),
    (2691, "expand_lesson_177_source_inspections.py"),
    (2706, "replace_diagram_with_svg.py"),
    (2725, "fix_svg_no_indent.py"),
    (2741, "clean_expand_lesson_177.py"),
    (2749, "expand_robots_txt_dirb.py"),
    (2765, "add_unix_structure_card.py"),
    (2775, "deep_expand_lesson_177.py"),
    (2783, "fix_dirbuster_leaks.py"),
    (2807, "fix_all_quiz_newlines.py"),
    (2815, "add_ffuf_gobuster.py"),
    (2847, "fix_ffuf_ascii_final.py"),
    (2857, "add_comparison_table.py"),
    (2881, "add_http_understanding.py"),
    (2901, "fix_status_codes_table_link.py"),
    (2909, "add_curl_wireshark.py"),
    (2917, "add_malicious_http.py"),
    (2937, "replace_f12_dev_tools.py"),
    (2945, "fix_post_request_style.py"),
    (2956, "fix_response_line.py"),
    (2964, "color_code_anatomy.py"),
    (2972, "add_dom_explanation.py"),
    (2980, "add_burp_column.py")
]

# Read transcript
steps_data = {}
with open(transcript_path, "r", encoding="utf-8") as f:
    for line in f:
        try:
            step = json.loads(line)
            step_idx = step.get("step_index")
            steps_data[step_idx] = step
        except:
            pass

# 1. Reconstruct term_w36_web_app_complete_v5.py locally first
print("[*] Extracting clean baseline term_w36_web_app_complete_v5.py from Step 1569...")
step_1569 = steps_data.get(1569)
tool_calls = step_1569.get("tool_calls", [])
v5_code = None
for call in tool_calls:
    if call.get("name") == "write_to_file":
        v5_code = call.get("args", {}).get("CodeContent")
        break

if not v5_code:
    print("ERROR: Could not find baseline v5 code in Step 1569!")
    sys.exit(1)

# Read v4 to get Lesson 178 full block
with open("/home/kali/crru_ctf/CTFd/term_w36_web_app_complete_v4.py", "r", encoding="utf-8") as f:
    v4_content = f.read()

start_178 = v4_content.find('# ─── Lesson 178 ───')
end_178 = v4_content.find('# ─── Lesson 179 ───', start_178)
val178_full_block = v4_content[start_178:end_178]

# Patch v5 code with the Lesson 178 block
v5_start_178 = v5_code.find('# ─── Lesson 178 ───')
v5_end_178 = v5_code.find('# ─── Lesson 179 ───', v5_start_178)
v5_patched = v5_code[:v5_start_178] + val178_full_block + v5_code[v5_end_178:]

# Write patched v5 to local host path
local_v5_path = "/home/kali/crru_ctf/CTFd/term_w36_web_app_complete_v5.py"
with open(local_v5_path, "w", encoding="utf-8") as f:
    f.write(v5_patched)
print("[+] Wrote patched term_w36_web_app_complete_v5.py locally.")

# Copy patched v5 and baseline 177 text to container
print("[*] Copying patched complete_v5 and restore scripts to container...")
subprocess.run(["docker", "cp", local_v5_path, "ctfd-ctfd-1:/opt/CTFd/term_w36_web_app_complete_v5.py"], check=True)
subprocess.run(["docker", "cp", "/home/kali/crru_ctf/CTFd/lesson_177_block_0.txt", "ctfd-ctfd-1:/opt/CTFd/lesson_177_block_0.txt"], check=True)
subprocess.run(["docker", "cp", "/home/kali/crru_ctf/CTFd/restore_baseline_177.py", "ctfd-ctfd-1:/opt/CTFd/restore_baseline_177.py"], check=True)
subprocess.run(["docker", "cp", "/home/kali/crru_ctf/CTFd/restore_and_fix_177.py", "ctfd-ctfd-1:/opt/CTFd/restore_and_fix_177.py"], check=True)

# Run complete_v5 and restore baselines
print("[*] Populating baseline lesson tables inside container...")
subprocess.run(["docker", "exec", "ctfd-ctfd-1", "python3", "/opt/CTFd/term_w36_web_app_complete_v5.py"], check=True)
subprocess.run(["docker", "exec", "ctfd-ctfd-1", "python3", "/opt/CTFd/restore_baseline_177.py"], check=True)
subprocess.run(["docker", "exec", "ctfd-ctfd-1", "python3", "/opt/CTFd/restore_and_fix_177.py"], check=True)

# 2. Extract and run each incremental script in sequence
for step_idx, filename in steps_to_extract:
    print(f"\n[*] Extracting Step {step_idx}: {filename}...")
    step = steps_data.get(step_idx)
    if not step:
        print(f"ERROR: Step {step_idx} not found in transcript!")
        sys.exit(1)
        
    tool_calls = step.get("tool_calls", [])
    code = None
    for call in tool_calls:
        if call.get("name") == "write_to_file":
            code = call.get("args", {}).get("CodeContent")
            break
            
    if not code:
        print(f"ERROR: No write_to_file found in Step {step_idx}!")
        sys.exit(1)
        
    # Write to local scratch path
    local_path = os.path.join(scratch_dir, filename)
    with open(local_path, "w", encoding="utf-8") as f:
        f.write(code)
    print(f"  [+] Wrote to {local_path}")
    
    # Copy to docker container
    container_path = f"/opt/CTFd/{filename}"
    print(f"  [+] Copying to container: {container_path}...")
    subprocess.run(["docker", "cp", local_path, f"ctfd-ctfd-1:{container_path}"], check=True)
    
    # Execute inside container
    print(f"  [+] Executing inside container...")
    result = subprocess.run(["docker", "exec", "ctfd-ctfd-1", "python3", container_path], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR executing {filename}:")
        print(result.stderr)
        sys.exit(1)
    else:
        print(result.stdout.strip())

# 3. Apply final layout fixes
print("\n[*] Applying final fixes (fix_final_v7.py and fix_all_lessons_v6.py)...")
subprocess.run(["docker", "exec", "ctfd-ctfd-1", "python3", "/opt/CTFd/fix_final_v7.py"], check=True)
subprocess.run(["docker", "exec", "ctfd-ctfd-1", "python3", "/opt/CTFd/fix_all_lessons_v6.py"], check=True)

print("\n[✓] RECONSTRUCTION COMPLETE! All premium slide contents successfully restored to database.")
