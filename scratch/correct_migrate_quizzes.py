import json
import re
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

def migrate_style1_correct(lid, val):
    # Extract the lnum (which is the local quiz number like 1, 2, 3, or 343)
    lnum_match = re.search(r'id="mq-box-(\d+)"', val)
    if not lnum_match:
        print(f"Skipping lesson {lid} style 1 - no mq-box-ID found")
        return val, False
    
    lnum = lnum_match.group(1)
    print(f"Migrating Style 1 quiz for Lesson {lid} with lnum={lnum}")

    # 1. Update the CSS style tag
    css_pattern = re.compile(r'/\* Neon Gauge Progress Bar styling \*/.*?(?=\.mq-btn-check|\.mq-status-bar|</style>)', re.DOTALL)
    new_css = f""".mq-layout-container {{display:flex; gap:24px; align-items:stretch;}}
.mq-questions-col {{flex:1;}}
.mq-gauge-col {{width:160px; display:flex; flex-direction:column; align-items:center; justify-content:center; border-left:1px solid rgba(255,255,255,0.06); padding-left:24px;}}
@media (max-width: 768px) {{
  .mq-layout-container {{flex-direction:column;}}
  .mq-gauge-col {{width:100%; border-left:none; padding-left:0; border-top:1px solid rgba(255,255,255,0.06); padding-top:24px;}}
}}
.neon-gauge-container {{position:relative; width:120px; height:120px;}}
.neon-gauge {{width:100%; height:100%;}}
.neon-gauge-bg {{fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}}
.neon-gauge-fill {{fill:none; stroke:url(#gauge-grad-{lnum}); stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease; filter:drop-shadow(0 0 5px rgba(0,240,255,0.4));}}
.neon-gauge-text {{fill:#ffffff; font-family:'JetBrains Mono',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}}
"""
    if css_pattern.search(val):
        val = css_pattern.sub(new_css, val)
    else:
        # If CSS pattern doesn't match because we already replaced it partly, let's find the neon-gauge-fill stroke and make sure it has the correct lnum
        val = re.sub(r'stroke:url\(#gauge-grad-\d+\)', f'stroke:url(#gauge-grad-{lnum})', val)

    # 2. Update the HTML structure:
    # Wrap questions in mq-layout-container and mq-questions-col
    # First, undo any previous partial wraps to make it clean
    val = val.replace('<div class="mq-layout-container"><div class="mq-questions-col">', '')
    box_start_pattern = re.compile(rf'<div id="mq-box-{lnum}" class="mini-quiz-box">')
    val = box_start_pattern.sub(f'<div id="mq-box-{lnum}" class="mini-quiz-box"><div class="mq-layout-container"><div class="mq-questions-col">', val)
    
    # Remove old progress bar HTML
    progress_bar_pattern = re.compile(r'<!-- Neon Gauge Bar Progress -->.*?</div>\s*</div>', re.DOTALL)
    val = progress_bar_pattern.sub('', val)
    alt_progress_pattern = re.compile(r'<div class="mq-progress-container">.*?</div>\s*</div>', re.DOTALL)
    val = alt_progress_pattern.sub('', val)

    # Wrap up questions column and insert gauge column after status bar
    # Remove any existing gauge column if it was partially added
    gauge_col_pattern = re.compile(r'</div>\s*<div class="mq-gauge-col">.*?</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)
    val = gauge_col_pattern.sub('', val)
    
    status_bar_str = f'<div id="mq-status-{lnum}" class="mq-status-bar"></div>'
    new_gauge_html = f"""<div id="mq-status-{lnum}" class="mq-status-bar"></div>
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
</div>"""
    val = val.replace(status_bar_str, new_gauge_html)

    # 3. Update the Javascript progress updater functions
    js_update_progress_pattern = re.compile(rf'function updateMiniProgress\(lnum\) \{{.*?\}}', re.DOTALL)
    new_js_update = f"""function updateMiniProgress(lnum) {{
  var box = document.getElementById('mq-box-' + lnum);
  var qGroups = box.querySelectorAll('.mq-q');
  var answeredCount = 0;
  qGroups.forEach(function(g) {{
    if (g.querySelector('.mini-opt.selected')) {{
      answeredCount++;
    }}
  }});
  var pct = Math.round((answeredCount / qGroups.length) * 100);
  var fill = document.getElementById('lesson-gauge-fill-' + lnum);
  var text = document.getElementById('lesson-gauge-text-' + lnum);
  var status = document.getElementById('lesson-status-txt-' + lnum);
  if (fill) fill.setAttribute('stroke-dasharray', pct + ', 100');
  if (text) text.textContent = pct + '%';
  if (status) {{
    if (pct === 100) {{
      status.innerHTML = '<span style="color:#00f0ff; font-weight:bold;">กรุณากดตรวจคำตอบ</span>';
    }} else if (pct > 0) {{
      status.textContent = 'ตอบคำถามแล้ว ' + answeredCount + '/' + qGroups.length + ' ข้อ';
    }} else {{
      status.textContent = 'โปรดตอบคำถามให้ครบ 2 ข้อ';
    }}
  }}
}}"""
    val = js_update_progress_pattern.sub(new_js_update, val)

    # Replace pbar/ptext elements in checkMiniQuiz JS
    pbar_def_pattern = re.compile(r'const pbar = document\.getElementById\(\'mq-progress-bar-\' \+ lnum\);|var pbar = document\.getElementById\(\'mq-progress-bar-\' \+ lnum\);|var fill = document\.getElementById\(\'lesson-gauge-fill-\' \+ lnum\);')
    ptext_def_pattern = re.compile(r'const ptext = document\.getElementById\(\'mq-progress-text-\' \+ lnum\);|var ptext = document\.getElementById\(\'mq-progress-text-\' \+ lnum\);|var text = document\.getElementById\(\'lesson-gauge-text-\' \+ lnum\);')
    val = pbar_def_pattern.sub("var fill = document.getElementById('lesson-gauge-fill-' + lnum);", val)
    val = ptext_def_pattern.sub("var text = document.getElementById('lesson-gauge-text-' + lnum);\n  var status_txt = document.getElementById('lesson-status-txt-' + lnum);", val)

    val = val.replace("pbar.style.width = '100%';", "if (fill) { fill.setAttribute('stroke-dasharray', '100, 100'); fill.style.stroke = '#3ddc84'; }")
    val = val.replace("pbar.style.background = '#3ddc84';", "")
    val = val.replace("pbar.style.boxShadow = '0 0 15px rgba(61,220,132,0.6)';", "")
    val = val.replace("ptext.textContent = 'Lesson Progress: 100% (ผ่านเรียบร้อย)';", "if (text) text.textContent = '100%';\n    if (status_txt) status_txt.innerHTML = '<span style=\"color:#3ddc84; font-weight:bold;\"><i class=\"fas fa-check-circle mr-1\"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';")

    val = val.replace("pbar.style.width = errorPct + '%';", "if (fill) { fill.setAttribute('stroke-dasharray', errorPct + ', 100'); fill.style.stroke = '#ff007f'; }")
    val = val.replace("pbar.style.background = '#ff007f';", "")
    val = val.replace("pbar.style.boxShadow = '0 0 15px rgba(255,0,127,0.6)';", "")
    val = re.sub(r"ptext\.textContent = 'Lesson Progress: ' \+ errorPct \+ '% \(ไม่ผ่าน - ทำไม่จบ\)';", "if (text) text.textContent = errorPct + '%';\n    if (status_txt) status_txt.textContent = 'ตอบไม่ถูกต้อง ลองใหม่!';", val)

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
                    if 'mq-progress-bar' in val or 'mq-layout-container' in val:
                        # Style 1
                        new_val, success = migrate_style1_correct(l.id, val)
                        if success:
                            b['value'] = new_val
                            modified = True
            
            if modified:
                l.content = json.dumps(blocks, ensure_ascii=False)
                app.db.session.commit()
                print(f"Successfully re-migrated quiz for Lesson ID {l.id}!")
        except Exception as e:
            print(f"Error migrating lesson {l.id}: {e}")
