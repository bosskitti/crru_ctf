import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

# Query lesson 165
lesson = db.session.query(TutorialLesson).filter_by(id=165).first()
if not lesson:
    print("Lesson not found!")
    exit(1)

blocks = json.loads(lesson.content)
block_7 = blocks[7]

# Replace the css definition in block 7 with larger, more proportionate font sizes
old_css = """.tree-hover-info{margin-top:20px;background:rgba(15, 17, 26, 0.7);border:1px solid rgba(255, 255, 255, 0.05);border-radius:10px;padding:14px 20px;width:100%;max-width:820px;min-height:75px;display:flex;align-items:center;gap:16px;box-shadow:0 6px 20px rgba(0, 0, 0, 0.4);transition:all 0.3s ease;}
.tree-hover-badge{font-weight:800;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.12em;color:#8a94a6;border-right:2px solid rgba(255, 255, 255, 0.1);padding-right:16px;height:100%;display:flex;align-items:center;white-space:nowrap;transition:color 0.3s ease;}
.tree-hover-desc{font-size:0.95rem;color:#94a3b8;line-height:1.6;transition:color 0.3s ease;}"""

new_css = """.tree-hover-info{margin-top:24px;background:rgba(15, 17, 26, 0.75);border:1px solid rgba(255, 255, 255, 0.08);border-radius:12px;padding:20px 28px;width:100%;max-width:820px;min-height:100px;display:flex;align-items:center;gap:24px;box-shadow:0 8px 32px rgba(0, 0, 0, 0.4);transition:all 0.3s ease;}
.tree-hover-badge{font-weight:800;font-size:1.25rem;text-transform:none;letter-spacing:0.02em;color:#8a94a6;border-right:2px solid rgba(255, 255, 255, 0.15);padding-right:24px;display:flex;align-items:center;white-space:nowrap;transition:color 0.3s ease;font-family:'Fira Code', monospace;}
.tree-hover-desc{font-size:1.1rem;color:#cbd5e1;line-height:1.7;transition:color 0.3s ease;font-weight:600;}"""

if old_css in block_7['value']:
    block_7['value'] = block_7['value'].replace(old_css, new_css)
else:
    # Fallback replace if whitespace was different
    block_7['value'] = block_7['value'].replace(".tree-hover-badge{font-weight:800;font-size:0.75rem", ".tree-hover-badge{font-weight:800;font-size:1.25rem")
    block_7['value'] = block_7['value'].replace(".tree-hover-desc{font-size:0.95rem", ".tree-hover-desc{font-size:1.1rem")
    block_7['value'] = block_7['value'].replace(".tree-hover-info{margin-top:20px;", ".tree-hover-info{margin-top:24px;")

blocks[7] = block_7

# Save and Commit
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
db.session.commit()
print("Hover description text size in Block 7 adjusted successfully!")
