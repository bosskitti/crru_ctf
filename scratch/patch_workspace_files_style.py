import os

def patch_lesson(content, filepath, prefix, num, color, hover_color, shadow_color):
    var_name = f"{prefix}_{num}" if prefix == "QUIZ" else f"val{num}_2"
    idx = content.find(var_name)
    if idx == -1:
        return content, False
    
    # Find the start of the string (either """ or ''')
    q3_idx = content.find('"""', idx)
    q3_single_idx = content.find("'''", idx)
    
    quote = '"""'
    start_pos = q3_idx
    if q3_single_idx != -1 and (q3_idx == -1 or q3_single_idx < q3_idx):
        quote = "'''"
        start_pos = q3_single_idx
        
    if start_pos == -1:
        return content, False
        
    end_pos = content.find(quote, start_pos + 3)
    if end_pos == -1:
        return content, False
        
    quiz_content = content[start_pos + 3 : end_pos]
    if '.w-quiz-option {' in quiz_content or '.w-quiz-option{' in quiz_content:
        return content, False # Already patched
        
    style_start = quiz_content.find('<style>')
    style_end = quiz_content.find('</style>')
    if style_start == -1 or style_end == -1:
        return content, False
        
    style_str = quiz_content[style_start:style_end+8]
    # Check for escaping
    if "\\'" in style_str or "\\\"" in style_str or "term_w36" in filepath:
        # Escaped CSS style block
        option_css = f"""
.w-quiz-option \\{{
  display: block;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 8px;
  padding: 12px 16px;
  margin-bottom: 10px;
  color: #cbd5e1;
  font-size: 0.84rem;
  cursor: pointer;
  transition: all 0.2s ease;
  position: relative;
\\}}
.w-quiz-option:hover \\{{
  background: {hover_color};
  border-color: rgba({shadow_color}, 0.25);
  color: #ffffff;
\\}}
.w-quiz-option.selected \\{{
  background: {hover_color};
  border-color: {color};
  color: #ffffff;
  box-shadow: 0 0 10px rgba({shadow_color}, 0.2);
  font-weight: 700;
\\}}
.w-quiz-option input[type=\\"radio\\"] \\{{
  display: none;
\\}}
"""
    else:
        option_css = f"""
.w-quiz-option {{
  display: block;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 8px;
  padding: 12px 16px;
  margin-bottom: 10px;
  color: #cbd5e1;
  font-size: 0.84rem;
  cursor: pointer;
  transition: all 0.2s ease;
  position: relative;
}}
.w-quiz-option:hover {{
  background: {hover_color};
  border-color: rgba({shadow_color}, 0.25);
  color: #ffffff;
}}
.w-quiz-option.selected {{
  background: {hover_color};
  border-color: {color};
  color: #ffffff;
  box-shadow: 0 0 10px rgba({shadow_color}, 0.2);
  font-weight: 700;
}}
.w-quiz-option input[type="radio"] {{
  display: none;
}}
"""
    new_style = style_str.replace('</style>', option_css + '</style>')
    new_quiz_content = quiz_content.replace(style_str, new_style)
    
    # Replace in content
    new_full_string = content[:start_pos + 3] + new_quiz_content + content[end_pos:]
    return new_full_string, True


def patch_file(filepath):
    print(f"Patching file: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lessons = {
        '177': ("#00f0ff", "rgba(0, 240, 255, 0.04)", "0, 240, 255"),
        '178': ("#a855f7", "rgba(168, 85, 247, 0.04)", "168, 85, 247"),
        '179': ("#3b82f6", "rgba(59, 130, 246, 0.04)", "59, 130, 246"),
        '180': ("#10b981", "rgba(16, 185, 129, 0.04)", "16, 185, 129"),
    }

    modified = False
    prefix = "QUIZ" if "fix_final" in filepath else "val"
    
    for num, (color, hover_color, shadow_color) in lessons.items():
        content, success = patch_lesson(content, filepath, prefix, num, color, hover_color, shadow_color)
        if success:
            modified = True
            print(f"Patched Lesson {num} style block in content.")

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully saved patches to {filepath}")

patch_file('/home/kali/crru_ctf/CTFd/fix_final_v7.py')
patch_file('/home/kali/crru_ctf/CTFd/term_w36_web_app_complete_v5.py')
