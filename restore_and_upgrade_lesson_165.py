import os
import re
import html
import json

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
    print("Reading extracted text from Chapter 2...")
    with open(txt_path, "r", encoding="utf-8") as f:
        full_text = f.read()
        
    pages_raw = full_text.split("\x0c")
    print(f"Total pages extracted: {len(pages_raw)}")
    
    slides = []
    for p_num in range(16, 39): # Pages 16 to 38
        if p_num > len(pages_raw):
            break
        page_content = pages_raw[p_num - 1]
        cleaned_content = clean_page_text(page_content)
        escaped_content = html.escape(cleaned_content)
        
        slides.append({
            "page": p_num,
            "text": escaped_content
        })
        
    print(f"Total slides compiled: {len(slides)}")
    for s in slides:
        lines = s["text"].split("\n")
        title = lines[0].strip() if lines else "EMPTY"
        print(f"Page {s['page']} Title: {title}")

if __name__ == "__main__":
    main()
