import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

new_ascii_html = """<pre style="color:#fbbf24;font-family:monospace;font-size:0.72rem;line-height:1.25;border:none;background:transparent;padding:0;margin:10px 0;">
      /'___&#92;  /'___&#92;           /&#92;_ &#92;
     /&#92; &#92;__/ /&#92; &#92;__/  __  __   &#92;//&#92; &#92;
     &#92; &#92;  __&#92;&#92; &#92;  __&#92;/&#92; &#92;/&#92; &#92;    &#92; &#92; &#92;
      &#92; &#92; &#92;_&#92;/&#92; &#92; &#92;_&#92;/&#92; &#92; &#92;_&#92; &#92;    &#92;_&#92; &#92;_
       &#92; &#92;_&#92;  &#92; &#92;_&#92;  &#92; &#92;____/    /&#92;____&#92;
        &#92;/_/   &#92;/_/   &#92;/___/     &#92;/____/

       v2.1.0-dev
</pre>"""

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        try:
            blocks = json.loads(l.content)
            val = blocks[0]["value"]
            
            # Find the pre block with the ASCII art
            start_tag = '<pre style="color:#fbbf24;font-family:monospace;font-size:0.72rem;line-height:1.25;border:none;background:transparent;padding:0;margin:10px 0;">'
            idx = val.find(start_tag)
            end_idx = val.find('</pre>', idx) + 6 if idx != -1 else -1
            
            if idx != -1 and end_idx != -1:
                # Replace with the new precise version
                new_val = val[:idx] + new_ascii_html + val[end_idx:]
                blocks[0]["value"] = new_val
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print("Successfully updated FFUF ASCII logo to match precise character layout!")
            else:
                print("Error: Could not find target FFUF pre block in Lesson 177 Block 0.")
        except Exception as e:
            print(f"Error: {e}")
