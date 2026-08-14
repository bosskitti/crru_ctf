import re

# Read term_w36_web_app_complete_v4.py to extract val178_0, val178_1, val178_2
with open("term_w36_web_app_complete_v4.py", "r", encoding="utf-8") as f:
    v4_content = f.read()

# Extract from "# ─── Lesson 178 ───" up to "# ─── Lesson 179 ───" (exclusive)
pattern = r"(# ─── Lesson 178 ───.*?)(?=# ─── Lesson 179 ───)"
match = re.search(pattern, v4_content, re.DOTALL)
if not match:
    print("ERROR: Could not find Lesson 178 variables in v4 script.")
    exit(1)

val178_block = match.group(1)
print("SUCCESS: Extracted Lesson 178 block from v4.")

# Read term_w36_web_app_complete_v5.py
with open("term_w36_web_app_complete_v5.py", "r", encoding="utf-8") as f:
    v5_content = f.read()

# Replace the empty Lesson 178 section in v5 with the full block from v4
# The empty section is:
# # ─── Lesson 178 ───
# # ─── Lesson 179 ───
v5_updated = v5_content.replace(
    "# ─── Lesson 178 ───\n# ─── Lesson 179 ───",
    val178_block + "# ─── Lesson 179 ───"
)

# Write the updated v5 content back
with open("term_w36_web_app_complete_v5.py", "w", encoding="utf-8") as f:
    f.write(v5_updated)

print("SUCCESS: Patched term_w36_web_app_complete_v5.py successfully.")
