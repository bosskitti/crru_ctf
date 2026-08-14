import os
import re

txt_path = "/opt/CTFd/lesson_165_temp.txt"

watermarks = [
    r"^Chapter\s*\d+$",
    r"Introduction to Cybersecurity",
    r"Copyright\s*©.*",
    r"^Copyright$",
    r"^202$",
    r"^6$",
    r"^By$",
    r"^Wongyos$",
    r"^Keardsri$",
    r"By\s*Wongyos\s*Keardsri",
    r"Faculty\s*of\s*Forensic\s*Science",
    r"Royal\s*Police\s*Cadet\s*Academy",
    r"Thailand",
    r"Email:.*",
    r"Line\s*ID:.*",
    r"Phone/WhatsApp:.*",
    r"Facebook:.*",
    r"RPCA\s*Cyber\s*Club",
    r"Asst\.Prof\..*",
    r"Pol\..*",
    r"Keardsri\s*\(Bank\)"
]

def clean_page_text(page_text):
    lines = page_text.split("\n")
    cleaned_lines = []
    for line in lines:
        line_strip = line.strip()
        if not line_strip:
            cleaned_lines.append("")
            continue
        is_watermark = False
        for wm in watermarks:
            if re.search(wm, line_strip, re.IGNORECASE):
                is_watermark = True
                break
        if not is_watermark:
            cleaned_lines.append(line.replace("\x0c", ""))
    return "\n".join(cleaned_lines).strip("\n")

def main():
    with open(txt_path, "r", encoding="utf-8") as f:
        full_text = f.read()
        
    pages_raw = full_text.split("\x0c")
    for p_num in range(16, 39):
        print(f"================ PAGE {p_num} ================")
        print(clean_page_text(pages_raw[p_num - 1]))

if __name__ == "__main__":
    main()
