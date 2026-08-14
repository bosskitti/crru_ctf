import os

txt_path = "/opt/CTFd/lesson_165_temp.txt"

def main():
    with open(txt_path, "r", encoding="utf-8") as f:
        full_text = f.read()
        
    pages_raw = full_text.split("\x0c")
    for p_num in range(16, 26):
        print(f"================ PAGE {p_num} ================")
        print(pages_raw[p_num - 1])

if __name__ == "__main__":
    main()
