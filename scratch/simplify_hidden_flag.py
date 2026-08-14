import json
import sys
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

old_injected_str = """
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

simple_comment = "\n\n<!-- FLAG_B64: ZmxhZ3tmMTJfdmlld19zb3VyY2VfcGFnZV9vYmZ1c2NhdGlvbl9zdWNjZXNzZnVsXzk4YTRjM2FkMmU5fQ== -->\n"

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if not l:
        print("ERROR: Lesson 177 not found.")
        sys.exit(1)
        
    try:
        blocks = json.loads(l.content)
        val = blocks[2]["value"]
        
        # Replace the old complex block with the simple comment
        if old_injected_str in val:
            new_val = val.replace(old_injected_str, simple_comment)
            blocks[2]["value"] = new_val
            l.content = json.dumps(blocks, ensure_ascii=False)
            app.db.session.commit()
            print("SUCCESS: Simplified the hidden flag to a simple HTML comment!")
        else:
            # If the complex block is not there (perhaps because it wasn't matches exactly), let's search for the signature
            sig = "Secret Payload: ZmxhZ3tmMTJfdmlld19z"
            if sig in val:
                # Find index of target header and reconstruct
                target_header = "### 🛠️ เครื่องมือแกะรหัสหน้าเว็บ (Web Page Source Inspections)"
                idx = val.find(target_header)
                if idx != -1:
                    # Let's clean it up by replacing it
                    # We can find the end of the script block
                    script_end = "</script>"
                    script_end_idx = val.find(script_end, idx)
                    if script_end_idx != -1:
                        insert_pos = idx + len(target_header)
                        new_val = val[:insert_pos] + simple_comment + val[script_end_idx + len(script_end):]
                        blocks[2]["value"] = new_val
                        l.content = json.dumps(blocks, ensure_ascii=False)
                        app.db.session.commit()
                        print("SUCCESS: Simplified the hidden flag using fallback search!")
                        sys.exit(0)
            print("ERROR: Injected script block not found in Block 2.")
            sys.exit(1)
    except Exception as e:
        print("ERROR:", e)
        sys.exit(1)
