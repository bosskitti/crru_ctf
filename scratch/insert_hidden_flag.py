import json
import sys
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

hidden_flag_html = """

<!-- [SECURITY DEBUG ALERT] - DEPRECATED ENVIRONMENT DETECTED -->
<!-- SYSTEM ADMINISTRATOR LOG: Decrypt the base64 string to verify DOM flag integrity -->
<!-- Secret Payload: ZmxhZ3tmMTJfdmlld19zb3VyY2VfcGFnZV9vYmZ1c2NhdGlvbl9zdWNjZXNzZnVsXzk4YTRjM2FkMmU5fQ== -->
<script>
  /*
   TODO: DEPRECATED IN PRODUCTION - REMOVE THIS BLOCK BEFORE SHIPMENT
   System integrity check:
   window.db_debug_check = atob("ZmxhZ3tmMTJfdmlld19zb3VyY2VfcGFnZV9vYmZ1c2NhdGlvbl9zdWNjZXNzZnVsXzk4YTRjM2FkMmU5fQ==");
  */
</script>
"""

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if not l:
        print("ERROR: Lesson 177 not found.")
        sys.exit(1)
        
    try:
        blocks = json.loads(l.content)
        val = blocks[2]["value"]
        
        # Target header to insert after
        target_header = "### 🛠️ เครื่องมือแกะรหัสหน้าเว็บ (Web Page Source Inspections)"
        idx = val.find(target_header)
        if idx == -1:
            # Try a slightly different variation in case header styling is different
            target_header = "### 📄 SLIDE 29-41: Web Page Source Inspections (F12 Developer Tools)"
            idx = val.find(target_header)
        if idx == -1:
            target_header = "Web Page Source Inspections (F12 Developer Tools)"
            idx = val.find(target_header)
            
        if idx == -1:
            print("ERROR: F12 header marker not found in Block 2.")
            sys.exit(1)
            
        insert_pos = idx + len(target_header)
        
        # Check if already inserted to prevent duplicates
        if "Secret Payload: ZmxhZ3tmMTJfdmlld19z" in val:
            print("Hidden flag is already injected in Block 2.")
            sys.exit(0)
            
        new_val = val[:insert_pos] + hidden_flag_html + val[insert_pos:]
        blocks[2]["value"] = new_val
        l.content = json.dumps(blocks, ensure_ascii=False)
        app.db.session.commit()
        print("SUCCESS: Injected hidden base64 flag inside Lesson 177 Block 2!")
    except Exception as e:
        print("ERROR:", e)
        sys.exit(1)
