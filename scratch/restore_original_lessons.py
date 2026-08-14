import re
import subprocess

# 1. Read v3 to extract val179_0 and val179_1
with open("term_w36_web_app_complete_v3.py", "r", encoding="utf-8") as f:
    v3_content = f.read()

# Extract val179_0
start_0 = v3_content.find('val179_0 = """')
if start_0 == -1:
    print("ERROR: val179_0 not found in v3")
    exit(1)
end_0 = v3_content.find('"""', start_0 + len('val179_0 = """')) + 3
val179_0_block = v3_content[start_0:end_0]

# Extract val179_1
start_1 = v3_content.find('val179_1 = """')
if start_1 == -1:
    print("ERROR: val179_1 not found in v3")
    exit(1)
end_1 = v3_content.find('"""', start_1 + len('val179_1 = """')) + 3
val179_1_block = v3_content[start_1:end_1]

# 2. Read v4 to extract val179_2
with open("term_w36_web_app_complete_v4.py", "r", encoding="utf-8") as f:
    v4_content = f.read()

# Extract val179_2
start_2 = v4_content.find('val179_2 = """')
if start_2 == -1:
    print("ERROR: val179_2 not found in v4")
    exit(1)
end_2 = v4_content.find('"""', start_2 + len('val179_2 = """')) + 3
val179_2_block = v4_content[start_2:end_2]

# 3. Read the current term_w36_web_app_complete_v5.py
with open("term_w36_web_app_complete_v5.py", "r", encoding="utf-8") as f:
    v5_content = f.read()

# Find the start and end of val179_0 in v5
v5_start_0 = v5_content.find('val179_0 = """')
v5_end_0 = v5_content.find('"""', v5_start_0 + len('val179_0 = """')) + 3

# Replace val179_0 in v5
v5_updated = v5_content[:v5_start_0] + val179_0_block + v5_content[v5_end_0:]

# Find the start and end of val179_1 in updated v5
v5_start_1 = v5_updated.find('val179_1 = """')
v5_end_1 = v5_updated.find('"""', v5_start_1 + len('val179_1 = """')) + 3

# Replace val179_1 in updated v5
v5_updated = v5_updated[:v5_start_1] + val179_1_block + v5_updated[v5_end_1:]

# Find the start and end of val179_2 in updated v5
v5_start_2 = v5_updated.find('val179_2 = """')
v5_end_2 = v5_updated.find('"""', v5_start_2 + len('val179_2 = """')) + 3

# Replace val179_2 in updated v5
v5_updated = v5_updated[:v5_start_2] + val179_2_block + v5_updated[v5_end_2:]

# Write the updated v5 content back
with open("term_w36_web_app_complete_v5.py", "w", encoding="utf-8") as f:
    f.write(v5_updated)

print("SUCCESS: Original SQLi/XSS/Broken Auth variables restored in term_w36_web_app_complete_v5.py.")
