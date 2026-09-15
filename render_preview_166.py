import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson, markdown

app = create_app()
with app.app_context():
    l = TutorialLesson.query.get(166)
    blocks = json.loads(l.content)
    rendered_parts = []
    for b in blocks:
        if b.get('type') == 'markdown':
            rendered_parts.append(markdown(b.get('value', '')))
        elif b.get('type') == 'challenge':
            cid = b.get('challenge_id')
            rendered_parts.append(f"""
            <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(0, 240, 255, 0.2); border-radius: 12px; padding: 18px 24px; margin: 1.5rem 0; text-align: center;">
                <span style="color: #38bdf8; font-weight: 700; font-family: monospace;">[CTFd Whale Interactive Challenge Box • ID: {cid}]</span>
                <div style="margin-top: 8px; color: #94a3b8; font-size: 0.85rem;">ปุ่มเปิด Docker Container & ช่องส่งคำตอบ Flag</div>
            </div>
            """)
    
    html_content = "\n".join(rendered_parts)
    with open('/opt/CTFd/rendered_166.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Rendered 166 HTML saved!")
