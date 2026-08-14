import re

# Read restore_and_fix_177.py to extract HTML definitions and replacement logic
with open("/home/kali/crru_ctf/CTFd/restore_and_fix_177.py", "r", encoding="utf-8") as f:
    restore_code = f.read()

# Extract definitions from HTML_A01 to end of replacing
# We want to grab from HTML_A01 = """ up to just before 'with app.app_context():'
start_marker = 'HTML_A01 = """'
end_marker = 'with app.app_context():'

start_idx = restore_code.find(start_marker)
end_idx = restore_code.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Error: Could not locate markers in restore_and_fix_177.py")
    exit(1)

extracted_logic = restore_code[start_idx:end_idx].strip()

# Adjust variable names in the extracted logic to work on val177_0
extracted_logic = extracted_logic.replace("baseline_val177_0", "val177_0_rich")

# Load term_w36_web_app_complete_v6.py
with open("/home/kali/crru_ctf/CTFd/term_w36_web_app_complete_v6.py", "r", encoding="utf-8") as f:
    v6_code = f.read()

# Locate 'save_lesson(177, val177_0, val177_1, val177_2)'
target_str = "save_lesson(177, val177_0, val177_1, val177_2)"

replacement_block = f"""
# --- Begin Lesson 177 Rich Graphics Integration ---
val177_0_rich = val177_0
{extracted_logic}
save_lesson(177, val177_0_rich, val177_1, val177_2)
# --- End Lesson 177 Rich Graphics Integration ---
"""

if target_str not in v6_code:
    print("Error: Could not locate save_lesson(177) target in term_w36_web_app_complete_v6.py")
    exit(1)

v6_code = v6_code.replace(target_str, replacement_block)

# Save updated term_w36_web_app_complete_v6.py
with open("/home/kali/crru_ctf/CTFd/term_w36_web_app_complete_v6.py", "w", encoding="utf-8") as f:
    f.write(v6_code)

print("Successfully integrated Lesson 177 rich graphics into term_w36_web_app_complete_v6.py!")
