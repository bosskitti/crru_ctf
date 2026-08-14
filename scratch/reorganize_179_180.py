import json
import sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    l179 = TutorialLesson.query.get(179)
    l180 = TutorialLesson.query.get(180)

    b179 = json.loads(l179.content)
    b180 = json.loads(l180.content)

    # --- PLAN ---
    # Lesson 179 (CMS Exploitation):
    #   Block 0: new styled CMS content (already good) — keep
    #   Block 1: sandbox from 180 (CMS Security Audit Sandbox)
    #   Block 2: quiz from 180 (CMS quiz)
    #
    # Lesson 180 (placeholder/empty content):
    #   Block 0: short placeholder with title
    #   Block 1: old sandbox from 179 (SQLi & Command Injection Lab)
    #   Block 2: old quiz from 179 (old quiz)
    #
    # This way: 179 has proper CMS sandbox+quiz, 180 has old sandbox+quiz
    # and nothing is deleted

    # Save everything first
    cms_content_179 = b179[0]['value']    # new styled CMS content (keep)
    old_sandbox_179 = b179[1]['value']    # SQLi sandbox
    old_quiz_179    = b179[2]['value']    # old quiz

    cms_content_180 = b180[0]['value']    # old CMS markdown text (short)
    cms_sandbox_180 = b180[1]['value']    # CMS Security Audit Sandbox
    cms_quiz_180    = b180[2]['value']    # CMS quiz

    # === LESSON 179: CMS Exploitation ===
    # Block 0: keep new styled CMS content
    # Block 1: CMS Security Audit Sandbox (from 180)
    # Block 2: CMS quiz (from 180)
    new_b179 = [
        {'type': 'markdown', 'value': cms_content_179},
        {'type': 'markdown', 'value': cms_sandbox_180},
        {'type': 'markdown', 'value': cms_quiz_180},
    ]

    # === LESSON 180: จอง / ว่างไว้ ===
    # Move old content here so nothing is lost
    # Block 0: placeholder header + old CMS markdown text
    placeholder_180 = """<div style="text-align: center; margin-bottom: 2rem; padding: 24px; background: linear-gradient(135deg, rgba(100,116,139,0.12) 0%, rgba(51,65,85,0.12) 100%); border: 1px solid rgba(100,116,139,0.25); border-radius: 16px; box-shadow: 0 0 20px rgba(100,116,139,0.1);">
<h2 style="margin: 0; font-size: 1.9rem; font-weight: 800; color: #ffffff; letter-spacing: 0.03em;">📦 เนื้อหาสำรอง (Reserved Lesson)</h2>
<p style="margin: 8px 0 0 0; font-size: 0.92rem; color: #94a3b8; font-weight: 500;">บทเรียนนี้สำรองไว้สำหรับเนื้อหาในอนาคต หรือเนื้อหาที่ย้ายมาเก็บไว้ชั่วคราว</p>
</div>

""" + cms_content_180

    new_b180 = [
        {'type': 'markdown', 'value': placeholder_180},
        {'type': 'markdown', 'value': old_sandbox_179},
        {'type': 'markdown', 'value': old_quiz_179},
    ]

    # === Update titles ===
    l179.title = '03. การโจมตีระบบจัดการเนื้อหาเว็บ (CMS Exploitation & Scanning Tools)'
    l180.title = '04. เนื้อหาสำรองและแบบฝึกหัดเพิ่มเติม (Reserved & Extra Practice)'

    # === Save ===
    l179.content = json.dumps(new_b179, ensure_ascii=False)
    l180.content = json.dumps(new_b180, ensure_ascii=False)
    app.db.session.commit()

    print('=== Done! ===')
    print(f'Lesson 179 title: {l179.title}')
    print(f'  Block 0 len: {len(new_b179[0]["value"])}  (CMS styled content)')
    print(f'  Block 1 len: {len(new_b179[1]["value"])}  (CMS Sandbox)')
    print(f'  Block 2 len: {len(new_b179[2]["value"])}  (CMS Quiz)')
    print()
    print(f'Lesson 180 title: {l180.title}')
    print(f'  Block 0 len: {len(new_b180[0]["value"])}  (placeholder + old CMS text)')
    print(f'  Block 1 len: {len(new_b180[1]["value"])}  (old SQLi sandbox)')
    print(f'  Block 2 len: {len(new_b180[2]["value"])}  (old quiz)')
