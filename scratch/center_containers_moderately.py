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

# 1. Update Block 5 (Architecture Blueprint)
# Change max-width:100% to max-width:1050px and center with margin: 2.5rem auto
blocks[5]['value'] = blocks[5]['value'].replace(
    ".arch-grid-v3{margin:2.5rem 0;display:flex;flex-direction:column;align-items:center;width:100%;max-width:100%;",
    ".arch-grid-v3{margin:2.5rem auto;display:flex;flex-direction:column;align-items:center;width:100%;max-width:1050px;"
).replace(
    ".arch-grid-v3{margin:2.5rem auto;display:flex;flex-direction:column;align-items:center;width:100%;max-width:100%;",
    ".arch-grid-v3{margin:2.5rem auto;display:flex;flex-direction:column;align-items:center;width:100%;max-width:1050px;"
)

# 2. Update Block 11 (Directory Tree)
# Center the tree components (max-width: 1050px)
blocks[11]['value'] = blocks[11]['value'].replace(
    ".tree-wrapper-v6{margin:2.5rem 0;display:flex;flex-direction:column;align-items:center;width:100%;}",
    ".tree-wrapper-v6{margin:2.5rem auto;display:flex;flex-direction:column;align-items:center;width:100%;}"
).replace(
    ".tree-side-text-card{background:linear-gradient(135deg,rgba(15,17,26,0.6) 0%,rgba(30,20,45,0.4) 100%);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:20px;width:100%;max-width:100%;margin-top:20px;",
    ".tree-side-text-card{background:linear-gradient(135deg,rgba(15,17,26,0.6) 0%,rgba(30,20,45,0.4) 100%);border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:20px;width:100%;max-width:1050px;margin:20px auto 0 auto;"
).replace(
    ".tree-hover-info{margin-top:24px;background:rgba(15, 17, 26, 0.75);border:1px solid rgba(255, 255, 255, 0.08);border-radius:12px;padding:20px 28px;width:100%;max-width:100%;",
    ".tree-hover-info{margin:24px auto 0 auto;background:rgba(15, 17, 26, 0.75);border:1px solid rgba(255, 255, 255, 0.08);border-radius:12px;padding:20px 28px;width:100%;max-width:1050px;"
)

# 3. Update Block 13 (5 Flat-Tree Sub-trees)
# Center sub-trees (max-width: 1050px)
blocks[13]['value'] = blocks[13]['value'].replace(
    ".mini-tree-wrapper{margin:2.5rem 0;width:100%;max-width:100%;",
    ".mini-tree-wrapper{margin:2.5rem auto;width:100%;max-width:1050px;"
).replace(
    ".mini-tree-wrapper{margin:2.5rem auto;width:100%;max-width:100%;",
    ".mini-tree-wrapper{margin:2.5rem auto;width:100%;max-width:1050px;"
)

# 4. Update Block 15 (User Accounts Cards)
# Center user account cards (max-width: 1050px)
blocks[15]['value'] = blocks[15]['value'].replace(
    ".user-grid{display:flex;gap:20px;width:100%;max-width:100%;margin:2rem 0;}",
    ".user-grid{display:flex;gap:20px;width:100%;max-width:1050px;margin:2rem auto;}"
).replace(
    ".user-grid{display:flex;gap:20px;width:100%;max-width:100%;margin:2rem auto;}",
    ".user-grid{display:flex;gap:20px;width:100%;max-width:1050px;margin:2rem auto;}"
)

# Save and Commit
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
db.session.commit()

print("All container widths centered and constrained to 1050px successfully!")
