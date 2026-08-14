file_path = "/home/kali/crru_ctf/CTFd/term_w36_web_app_complete_v5.py"

with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

start_marker = 'val178_0 = """## 💉 Path Traversal'
start_idx = code.find(start_marker)
print(f"Start index: {start_idx}")

if start_idx != -1:
    # Find the next triple quotes """
    triple_quote_idx = code.find('"""', start_idx + len(start_marker))
    print(f"Next triple quote index: {triple_quote_idx}")
    print("Surrounding text of next triple quotes:")
    print(code[max(0, triple_quote_idx - 150):triple_quote_idx + 20])
