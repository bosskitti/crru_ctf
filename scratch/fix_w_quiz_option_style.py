import json
import re
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

def fix_lesson_style(lid, val, color, hover_color, shadow_color):
    if '.w-quiz-option {' in val or '.w-quiz-option{' in val:
        print(f"Lesson {lid} style already contains .w-quiz-option rule. Skipping.")
        return val, False

    print(f"Adding w-quiz-option style to Lesson {lid}")
    
    quiz_option_css = f"""
.w-quiz-option {{
  display: block;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 8px;
  padding: 12px 16px;
  margin-bottom: 10px;
  color: #cbd5e1;
  font-size: 0.84rem;
  cursor: pointer;
  transition: all 0.2s ease;
  position: relative;
}}
.w-quiz-option:hover {{
  background: {hover_color};
  border-color: rgba({shadow_color}, 0.25);
  color: #ffffff;
}}
.w-quiz-option.selected {{
  background: {hover_color};
  border-color: {color};
  color: #ffffff;
  box-shadow: 0 0 10px rgba({shadow_color}, 0.2);
  font-weight: 700;
}}
.w-quiz-option input[type="radio"] {{
  display: none;
}}
"""
    # Insert right before </style>
    idx = val.find('</style>')
    if idx == -1:
        print(f"Error: </style> not found in Lesson {lid}")
        return val, False
    
    val = val[:idx] + quiz_option_css + val[idx:]
    return val, True

# Colors for each lesson
colors = {
    177: ("#00f0ff", "rgba(0, 240, 255, 0.04)", "0, 240, 255"),
    178: ("#a855f7", "rgba(168, 85, 247, 0.04)", "168, 85, 247"),
    179: ("#3b82f6", "rgba(59, 130, 246, 0.04)", "59, 130, 246"),
    180: ("#10b981", "rgba(16, 185, 129, 0.04)", "16, 185, 129"),
}

with app.app_context():
    for lid, (color, hover_color, shadow_color) in colors.items():
        lesson = app.db.session.query(TutorialLesson).filter_by(id=lid).first()
        if not lesson:
            print(f"Lesson {lid} not found in DB")
            continue
        try:
            blocks = json.loads(lesson.content)
            modified = False
            for idx, b in enumerate(blocks):
                val = b.get('value', '')
                if 'w-quiz-option' in val and '<style>' in val:
                    new_val, success = fix_lesson_style(lid, val, color, hover_color, shadow_color)
                    if success:
                        b['value'] = new_val
                        modified = True
            
            if modified:
                lesson.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print(f"Successfully patched CSS styling for Lesson ID {lid}!")
        except Exception as e:
            print(f"Error patching lesson {lid}: {e}")
