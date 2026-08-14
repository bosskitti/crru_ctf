import json
import re
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

# Open the file and parse val177_0, val177_1, val177_2
with open("/opt/CTFd/term_w36_web_app_complete_v5.py", "r", encoding="utf-8") as f:
    content = f.read()

def extract_val(var_name):
    # Regex to find var_name = \"\"\" ... \"\"\"
    pattern = rf'{var_name}\s*=\s*\"\"\"(.*?)\"\"\"'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

val177_0 = extract_val("val177_0")
val177_1 = extract_val("val177_1")
val177_2 = extract_val("val177_2")

if val177_0 and val177_1 and val177_2:
    app = create_app()
    with app.app_context():
        l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
        if l:
            l.content = json.dumps([
                {"type": "markdown", "value": val177_0},
                {"type": "markdown", "value": val177_1},
                {"type": "markdown", "value": val177_2}
            ], ensure_ascii=False)
            app.db.session.commit()
            print("Successfully restored Lesson 177 to its exact original state!")
        else:
            print("Error: Lesson 177 not found in DB.")
else:
    print("Error: Could not extract val177_0, val177_1, or val177_2 from the script.")
