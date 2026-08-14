import json
import re
import os
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

def add_call_to_content(content):
    target_str = "localStorage.setItem('solved_lesson_"
    pattern = re.compile(r"localStorage\.setItem\('solved_lesson_(\d+)',\s*'solved'\);")
    
    modified = False
    matches = list(pattern.finditer(content))
    for m in reversed(matches):
        full_match = m.group(0)
        lid = m.group(1)
        
        start_pos = m.start()
        end_pos = m.end()
        surround = content[end_pos : end_pos + 100]
        if "updateProgressUI" in surround:
            continue
            
        replacement = f"{full_match}\n    if (typeof updateProgressUI === 'function') updateProgressUI();"
        content = content[:start_pos] + replacement + content[end_pos:]
        modified = True
        
    return content, modified

# Update DB for Lessons 177-180
with app.app_context():
    for lid in [177, 178, 179, 180]:
        lesson = app.db.session.query(TutorialLesson).filter_by(id=lid).first()
        if not lesson:
            continue
        try:
            blocks = json.loads(lesson.content)
            modified = False
            for idx, b in enumerate(blocks):
                val = b.get('value', '')
                if 'checkMiniQuiz' in val:
                    new_val, success = add_call_to_content(val)
                    if success:
                        b['value'] = new_val
                        modified = True
            
            if modified:
                lesson.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print(f"Successfully added updateProgressUI() call to DB Lesson {lid}")
        except Exception as e:
            print(f"Error patching DB Lesson {lid}: {e}")

# Update workspace files
files_to_patch = [
    '/home/kali/crru_ctf/CTFd/fix_final_v7.py',
    '/home/kali/crru_ctf/CTFd/term_w36_web_app_complete_v5.py'
]

for filepath in files_to_patch:
    if os.path.exists(filepath):
        print(f"Patching workspace file: {filepath}")
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content, success = add_call_to_content(content)
        if success:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Successfully saved patches to {filepath}")
