import json
import re
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

# Query lesson 164
lesson = db.session.query(TutorialLesson).filter_by(id=164).first()
if not lesson:
    print("Lesson not found!")
    exit(1)

blocks = json.loads(lesson.content)
block_9 = blocks[9]
val_9 = block_9['value']

# The HTML replacement code for the donut chart (completely flat, 0-indentation)
html_chart = """<style>
.chart-wrapper{margin:2.5rem 0;display:flex;flex-direction:column;align-items:center;width:100%;}
.chart-container{width:100%;max-width:820px;background:rgba(15,17,26,0.4);border:1px solid rgba(255,255,255,0.05);border-radius:12px;padding:28px;box-shadow:inset 0 0 20px rgba(0,0,0,0.4);display:flex;justify-content:space-around;align-items:center;gap:30px;}
@media (max-width:650px){.chart-container{flex-direction:column;padding:20px;}}
.donut-chart-box{position:relative;width:220px;height:220px;border-radius:50%;background:conic-gradient(#fbbf24 0% 72.1%, #00f0ff 72.1% 85.7%, #ab20fd 85.7% 92.2%, #f472b6 92.2% 97.8%, #e2e8f0 97.8% 100%);display:flex;align-items:center;justify-content:center;box-shadow:0 0 25px rgba(0, 0, 0, 0.5), 0 0 15px rgba(255, 255, 255, 0.02);transition:all 0.5s ease;}
.donut-chart-box::before{content:'';position:absolute;width:140px;height:140px;border-radius:50%;background:#141729;box-shadow:inset 0 0 12px rgba(0, 0, 0, 0.6);}
.donut-center-info{position:relative;z-index:10;text-align:center;display:flex;flex-direction:column;align-items:center;}
.donut-center-val{font-size:1.6rem;font-weight:800;color:#ffffff;line-height:1.1;text-shadow:0 0 10px rgba(255, 255, 255, 0.2);transition:color 0.3s ease, text-shadow 0.3s ease;}
.donut-center-lbl{font-size:0.75rem;color:#8a94a6;text-transform:uppercase;letter-spacing:0.1em;margin-top:4px;}
.chart-legend{display:flex;flex-direction:column;gap:12px;flex-grow:1;max-width:400px;width:100%;}
.legend-item{display:flex;align-items:center;justify-content:space-between;padding:10px 16px;background:rgba(255, 255, 255, 0.02);border:1px solid rgba(255, 255, 255, 0.05);border-radius:8px;cursor:pointer;transition:all 0.3s ease;user-select:none;}
.legend-left{display:flex;align-items:center;gap:12px;}
.legend-color-dot{width:12px;height:12px;border-radius:50%;box-shadow:0 0 8px currentColor;}
.legend-name{font-weight:600;font-size:0.95rem;color:#cbd5e1;}
.legend-pct{font-weight:700;font-size:1rem;color:#ffffff;transition:color 0.3s ease;}
.legend-item:hover{transform:translateX(4px);background:rgba(255, 255, 255, 0.05);}
.legend-item.type-win:hover{border-color:#fbbf24;}
.legend-item.type-win:hover .legend-pct{color:#fbbf24;text-shadow:0 0 8px rgba(251, 191, 36, 0.4);}
.legend-item.type-lin:hover{border-color:#00f0ff;}
.legend-item.type-lin:hover .legend-pct{color:#00f0ff;text-shadow:0 0 8px rgba(0, 240, 255, 0.4);}
.legend-item.type-oth:hover{border-color:#ab20fd;}
.legend-item.type-oth:hover .legend-pct{color:#ab20fd;text-shadow:0 0 8px rgba(171, 32, 253, 0.4);}
.legend-item.type-uni:hover{border-color:#f472b6;}
.legend-item.type-uni:hover .legend-pct{color:#f472b6;text-shadow:0 0 8px rgba(244, 114, 182, 0.4);}
.legend-item.type-390:hover{border-color:#e2e8f0;}
.legend-item.type-390:hover .legend-pct{color:#ffffff;text-shadow:0 0 8px rgba(255, 255, 255, 0.4);}
</style>
<div class="chart-wrapper">
<div class="chart-container">
<div class="donut-chart-box" id="donut-chart-el">
<div class="donut-center-info">
<span class="donut-center-val" id="donut-val-el">72.1%</span>
<span class="donut-center-lbl" id="donut-lbl-el">Windows</span>
</div>
</div>
<div class="chart-legend">
<div class="legend-item type-win" onmouseover="updateDonutInfo('72.1%', 'Windows', '#fbbf24', 'conic-gradient(#fbbf24 0% 72.1%, rgba(255,255,255,0.05) 72.1% 100%)')" onmouseout="resetDonutInfo()">
<div class="legend-left">
<div class="legend-color-dot" style="color: #fbbf24; background: #fbbf24;"></div>
<span class="legend-name">Windows</span>
</div>
<span class="legend-pct">72.1%</span>
</div>
<div class="legend-item type-lin" onmouseover="updateDonutInfo('13.6%', 'Linux', '#00f0ff', 'conic-gradient(rgba(255,255,255,0.05) 0% 72.1%, #00f0ff 72.1% 85.7%, rgba(255,255,255,0.05) 85.7% 100%)')" onmouseout="resetDonutInfo()">
<div class="legend-left">
<div class="legend-color-dot" style="color: #00f0ff; background: #00f0ff;"></div>
<span class="legend-name">Linux</span>
</div>
<span class="legend-pct">13.6%</span>
</div>
<div class="legend-item type-oth" onmouseover="updateDonutInfo('6.5%', 'Other', '#ab20fd', 'conic-gradient(rgba(255,255,255,0.05) 0% 85.7%, #ab20fd 85.7% 92.2%, rgba(255,255,255,0.05) 92.2% 100%)')" onmouseout="resetDonutInfo()">
<div class="legend-left">
<div class="legend-color-dot" style="color: #ab20fd; background: #ab20fd;"></div>
<span class="legend-name">Other</span>
</div>
<span class="legend-pct">6.5%</span>
</div>
<div class="legend-item type-uni" onmouseover="updateDonutInfo('5.6%', 'Unix', '#f472b6', 'conic-gradient(rgba(255,255,255,0.05) 0% 92.2%, #f472b6 92.2% 97.8%, rgba(255,255,255,0.05) 97.8% 100%)')" onmouseout="resetDonutInfo()">
<div class="legend-left">
<div class="legend-color-dot" style="color: #f472b6; background: #f472b6;"></div>
<span class="legend-name">Unix</span>
</div>
<span class="legend-pct">5.6%</span>
</div>
<div class="legend-item type-390" onmouseover="updateDonutInfo('2.1%', 'OS/390', '#e2e8f0', 'conic-gradient(rgba(255,255,255,0.05) 0% 97.8%, #e2e8f0 97.8% 100%)')" onmouseout="resetDonutInfo()">
<div class="legend-left">
<div class="legend-color-dot" style="color: #e2e8f0; background: #e2e8f0;"></div>
<span class="legend-name">OS/390</span>
</div>
<span class="legend-pct">2.1%</span>
</div>
</div>
</div>
</div>
<script>
const originalGradient = 'conic-gradient(#fbbf24 0% 72.1%, #00f0ff 72.1% 85.7%, #ab20fd 85.7% 92.2%, #f472b6 92.2% 97.8%, #e2e8f0 97.8% 100%)';
function updateDonutInfo(val, label, color, gradient) {
  const valEl = document.getElementById('donut-val-el');
  const lblEl = document.getElementById('donut-lbl-el');
  const chartEl = document.getElementById('donut-chart-el');
  if (valEl && lblEl && chartEl) {
    valEl.textContent = val;
    valEl.style.color = color;
    valEl.style.textShadow = '0 0 10px ' + color;
    lblEl.textContent = label;
    lblEl.style.color = color;
    chartEl.style.background = gradient;
  }
}
function resetDonutInfo() {
  const valEl = document.getElementById('donut-val-el');
  const lblEl = document.getElementById('donut-lbl-el');
  const chartEl = document.getElementById('donut-chart-el');
  if (valEl && lblEl && chartEl) {
    valEl.textContent = '72.1%';
    valEl.style.color = '#ffffff';
    valEl.style.textShadow = '0 0 10px rgba(255, 255, 255, 0.2)';
    lblEl.textContent = 'Windows';
    lblEl.style.color = '#8a94a6';
    chartEl.style.background = originalGradient;
  }
}
</script>"""

# Replace the table structure with our new flat HTML chart
pattern = r"\| OS \| Market Share \|.*\| \*\*OS/390\*\* \| 2\.1% \|"
modified_val_9 = re.sub(pattern, html_chart, val_9, flags=re.DOTALL)

if modified_val_9 == val_9:
    print("Warning: Table regex pattern did not match. Trying fallback string replacement...")
    # Reconstruct from scratch
    header = "### 💻 Server OS Market Share Worldwide\n\nhttps://www.enterpriseappstoday.com/stats/linux-statistics.html\n\n"
    footer = "\n\n> 💡 **หมายเหตุ:** ในกลุ่ม Top 500 Supercomputers ทั่วโลก ใช้ Linux 100%"
    modified_val_9 = header + html_chart + footer

block_9['value'] = modified_val_9
blocks[9] = block_9

# Save and Commit database
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=164).update({"content": lesson.content})
db.session.commit()
print("Server OS Market Share Donut Chart added successfully!")
