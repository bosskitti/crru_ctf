import json
import re
import os
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

def add_api_call(val, lid):
    # Check if already contains fetch call
    if "fetch('/api/v1/tutorials/progress'" in val:
        return val, False
        
    target = f"localStorage.setItem('solved_lesson_{lid}', 'solved');"
    
    # We want to replace it with:
    # localStorage.setItem('solved_lesson_{lid}', 'solved');
    # fetch('/api/v1/tutorials/progress', {
    #   method: 'POST',
    #   headers: {
    #     'Content-Type': 'application/json',
    #     'CSRF-Token': window.init.csrfNonce
    #   },
    #   body: JSON.stringify({
    #     lesson_id: {lid},
    #     type: 'quiz',
    #     item_key: 'quick_quiz',
    #     solved: true
    #   })
    # }).catch(e => console.error("Error syncing progress:", e));
    
    # Handle javascript backslashes escaping if the file uses double backslashes in multi-line python string
    # We will detect the escaping of braces: if "\\{" in val or "\\}" in val:
    is_escaped = "\\{" in val or "\\}" in val
    
    if is_escaped:
        fetch_call = f"""localStorage.setItem('solved_lesson_{lid}', 'solved');
    fetch('/api/v1/tutorials/progress', \\{{
      method: 'POST',
      headers: \\{{
        'Content-Type': 'application/json',
        'CSRF-Token': window.init.csrfNonce
      \\}},
      body: JSON.stringify(\\{{
        lesson_id: {lid},
        type: 'quiz',
        item_key: 'quick_quiz',
        solved: true
      \\}})
    \\}}).catch(e => console.error("Error syncing progress:", e));"""
    else:
        fetch_call = f"""localStorage.setItem('solved_lesson_{lid}', 'solved');
    fetch('/api/v1/tutorials/progress', {{
      method: 'POST',
      headers: {{
        'Content-Type': 'application/json',
        'CSRF-Token': window.init.csrfNonce
      }},
      body: JSON.stringify({{
        lesson_id: {lid},
        type: 'quiz',
        item_key: 'quick_quiz',
        solved: true
      }})
    }}).catch(e => console.error("Error syncing progress:", e));"""

    if target in val:
        val = val.replace(target, fetch_call)
        return val, True
        
    return val, False

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
                    new_val, success = add_api_call(val, lid)
                    if success:
                        b['value'] = new_val
                        modified = True
            
            if modified:
                lesson.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print(f"Successfully added API sync call to DB Lesson {lid}")
        except Exception as e:
            print(f"Error patching DB Lesson {lid}: {e}")

# Update workspace files (done on host later)
