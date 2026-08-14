import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    l = app.db.session.query(TutorialLesson).filter_by(id=177).first()
    if l:
        try:
            blocks = json.loads(l.content)
            val = blocks[0]["value"]
            
            # Find the path with the glow filter that is causing it to fail to render
            target_path = '<path d="M455,120 L175,120" fill="none" stroke="#3ddc84" stroke-width="2" filter="url(#glow-b)"/>'
            fixed_path = '<path d="M455,120 L175,120" fill="none" stroke="#3ddc84" stroke-width="2"/>'
            
            if target_path in val:
                val = val.replace(target_path, fixed_path)
                blocks[0]["value"] = val
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print("Successfully repaired the HTTP response line in the SVG diagram!")
            else:
                # Let's search for a generic match if the spacing is slightly different
                import re
                val_new, count = re.subn(r'stroke="#3ddc84"\s+stroke-width="2"\s+filter="url\(#glow-b\)"', 'stroke="#3ddc84" stroke-width="2"', val)
                if count > 0:
                    blocks[0]["value"] = val_new
                    l.content = json.dumps(blocks, ensure_ascii=False)
                    app.db.session.commit()
                    print(f"Repaired the response line in the SVG diagram using regex replacement! ({count} matches)")
                else:
                    print("Error: Could not locate the target response path inside Lesson 177 Block 0.")
        except Exception as e:
            print(f"Error: {e}")
