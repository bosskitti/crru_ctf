import json
import re
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

def heal_style1(lid, val):
    # Extract lnum
    lnum_match = re.search(r'id="mq-box-(\d+)"', val)
    if not lnum_match:
        print(f"Skipping heal for Lesson {lid} - no mq-box-ID found")
        return val, False
    
    lnum = lnum_match.group(1)
    
    # Check if mq-gauge-col is already present in HTML
    if 'class="mq-gauge-col"' in val:
        print(f"Lesson {lid} is already healed and complete!")
        return val, False

    print(f"Healing quiz layout for Lesson {lid} with lnum={lnum}")

    # The missing HTML block:
    missing_html = f"""
<button class="mq-btn-check" onclick="checkMiniQuiz({lnum})">Check Answers / ตรวจคำตอบ</button>
<div id="mq-status-{lnum}" class="mq-status-bar"></div>
</div>
<div class="mq-gauge-col">
  <span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em; text-align:center;">Lesson Progress</span>
  <div class="neon-gauge-container">
    <svg class="neon-gauge" viewBox="0 0 36 36">
      <defs>
        <linearGradient id="gauge-grad-{lnum}" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="#ff007f" />
          <stop offset="50%" stop-color="#fbbf24" />
          <stop offset="100%" stop-color="#00f0ff" />
        </linearGradient>
      </defs>
      <path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
      <path class="neon-gauge-fill" id="lesson-gauge-fill-{lnum}" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" />
      <text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text-{lnum}">0%</text>
    </svg>
  </div>
  <span id="lesson-status-txt-{lnum}" class="mt-3 d-block text-muted" style="font-size:0.78rem; text-align:center;">โปรดตอบคำถามให้ครบ 2 ข้อ</span>
</div>
</div>
</div>
"""
    # Insert right before <script>
    idx = val.find('<script>')
    if idx == -1:
        print(f"Error: <script> not found in Lesson {lid}")
        return val, False
    
    val = val[:idx] + missing_html + val[idx:]
    return val, True


with app.app_context():
    lessons = app.db.session.query(TutorialLesson).all()
    for l in lessons:
        try:
            blocks = json.loads(l.content)
            modified = False
            for idx, b in enumerate(blocks):
                val = b.get('value', '')
                if 'Lesson Quick Quiz' in val:
                    if 'mq-layout-container' in val:
                        new_val, success = heal_style1(l.id, val)
                        if success:
                            b['value'] = new_val
                            modified = True
            
            if modified:
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print(f"Successfully healed quiz for Lesson ID {l.id}!")
        except Exception as e:
            print(f"Error healing lesson {l.id}: {e}")
