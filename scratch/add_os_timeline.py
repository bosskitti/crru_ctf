import json
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
block_13 = blocks[13]

# The HTML replacement code for the OS timelines (completely flat, 0-indentation)
html_timeline = """<style>
.tl-wrapper{margin:2.5rem 0;display:flex;flex-direction:column;align-items:center;width:100%;}
.tl-tabs-container{display:flex;justify-content:center;flex-wrap:wrap;gap:10px;margin-bottom:20px;width:100%;max-width:820px;}
.tl-tab-btn{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.08);border-radius:8px;padding:10px 16px;color:#8a94a6;font-weight:600;font-size:0.9rem;cursor:pointer;display:flex;align-items:center;gap:8px;transition:all 0.3s ease;}
.tl-tab-btn:hover{background:rgba(255,255,255,0.06);color:#ffffff;}
.tl-tab-btn.active.type-win{border-color:#00c0ff;background:rgba(0,192,255,0.08);color:#00c0ff;box-shadow:0 0 10px rgba(0,192,255,0.15);}
.tl-tab-btn.active.type-lin{border-color:#f5a623;background:rgba(245,166,35,0.08);color:#f5a623;box-shadow:0 0 10px rgba(245,166,35,0.15);}
.tl-tab-btn.active.type-and{border-color:#3ddc84;background:rgba(61,220,132,0.08);color:#3ddc84;box-shadow:0 0 10px rgba(61,220,132,0.15);}
.tl-tab-btn.active.type-mac{border-color:#ff007f;background:rgba(255,0,127,0.08);color:#ff007f;box-shadow:0 0 10px rgba(255,0,127,0.15);}
.tl-tab-btn.active.type-ios{border-color:#00f0ff;background:rgba(0,240,255,0.08);color:#00f0ff;box-shadow:0 0 10px rgba(0,240,255,0.15);}
.tl-panel{display:none;width:100%;max-width:820px;background:rgba(15,17,26,0.4);border:1px solid rgba(255,255,255,0.05);border-radius:12px;padding:24px;box-shadow:inset 0 0 20px rgba(0,0,0,0.4);}
.tl-panel.active{display:block;}
.tl-panel-title{font-size:1.1rem;font-weight:700;color:#ffffff;margin-bottom:20px;display:flex;align-items:center;gap:10px;}
.tl-panel-title i{font-size:1.25rem;}
.tl-scroll-track{width:100%;overflow-x:auto;padding:40px 10px;position:relative;scrollbar-width:thin;scrollbar-color:rgba(255,255,255,0.1) rgba(0,0,0,0.2);}
.tl-scroll-track::-webkit-scrollbar{height:6px;}
.tl-scroll-track::-webkit-scrollbar-track{background:rgba(0,0,0,0.2);border-radius:3px;}
.tl-scroll-track::-webkit-scrollbar-thumb{background:rgba(255,255,255,0.1);border-radius:3px;}
.tl-scroll-track::-webkit-scrollbar-thumb:hover{background:rgba(255,255,255,0.25);}
.tl-axis-container{display:flex;position:relative;padding-left:20px;padding-right:20px;align-items:center;min-width:max-content;}
.tl-axis-line{position:absolute;top:50%;left:0;right:0;height:4px;background:rgba(255,255,255,0.1);transform:translateY(-50%);z-index:1;}
.tl-node{position:relative;z-index:2;margin-right:70px;display:flex;flex-direction:column;align-items:center;cursor:pointer;}
.tl-node:last-child{margin-right:0;}
.tl-node-dot{width:16px;height:16px;border-radius:50%;background:#0f111a;border:3px solid rgba(255,255,255,0.3);transition:all 0.3s cubic-bezier(0.4, 0, 0.2, 1);box-shadow:0 0 10px rgba(0, 0, 0, 0.5);}
.tl-node-label{position:absolute;font-weight:700;font-size:0.9rem;color:#94a3b8;white-space:nowrap;transition:all 0.3s ease;}
.tl-node:nth-child(odd) .tl-node-label{bottom:24px;}
.tl-node:nth-child(even) .tl-node-label{top:24px;}
.type-win .tl-node:hover .tl-node-dot{border-color:#00c0ff;background:#00c0ff;box-shadow:0 0 12px #00c0ff;transform:scale(1.25);}
.type-win .tl-node:hover .tl-node-label{color:#00c0ff;text-shadow:0 0 8px rgba(0,192,255,0.3);}
.type-and .tl-node:hover .tl-node-dot{border-color:#3ddc84;background:#3ddc84;box-shadow:0 0 12px #3ddc84;transform:scale(1.25);}
.type-and .tl-node:hover .tl-node-label{color:#3ddc84;text-shadow:0 0 8px rgba(61, 220, 132, 0.3);}
.type-mac .tl-node:hover .tl-node-dot{border-color:#ff007f;background:#ff007f;box-shadow:0 0 12px #ff007f;transform:scale(1.25);}
.type-mac .tl-node:hover .tl-node-label{color:#ff007f;text-shadow:0 0 8px rgba(255, 0, 127, 0.3);}
.type-ios .tl-node:hover .tl-node-dot{border-color:#00f0ff;background:#00f0ff;box-shadow:0 0 12px #00f0ff;transform:scale(1.25);}
.type-ios .tl-node:hover .tl-node-label{color:#00f0ff;text-shadow:0 0 8px rgba(0, 240, 255, 0.3);}
.linux-families-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:16px;width:100%;}
.linux-family-card{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:16px;transition:all 0.3s ease;box-shadow:0 4px 12px rgba(0,0,0,0.2);}
.linux-family-card:hover{transform:translateY(-3px);border-color:#f5a623;box-shadow:0 6px 15px rgba(245,166,35,0.1);}
.linux-family-name{font-weight:700;font-size:1rem;color:#f5a623;margin-bottom:12px;border-bottom:1px solid rgba(245,166,35,0.2);padding-bottom:6px;}
.linux-family-badges{display:flex;flex-direction:column;gap:8px;}
.linux-badge{background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-radius:6px;padding:6px 10px;font-size:0.8rem;color:#cbd5e1;text-align:center;font-weight:600;transition:all 0.2s ease;}
.linux-badge:hover{background:rgba(255,255,255,0.08);color:#ffffff;}
.tl-scroll-hint{display:flex;font-size:0.75rem;color:#8a94a6;margin-bottom:12px;align-items:center;gap:6px;justify-content:center;}
</style>
<div class="tl-wrapper">
<div class="tl-tabs-container">
<button class="tl-tab-btn active type-win" id="tl-btn-win" onclick="switchTLTab('win')"><i class="fab fa-windows"></i> Windows</button>
<button class="tl-tab-btn type-lin" id="tl-btn-lin" onclick="switchTLTab('lin')"><i class="fab fa-linux"></i> Linux</button>
<button class="tl-tab-btn type-and" id="tl-btn-and" onclick="switchTLTab('and')"><i class="fab fa-android"></i> Android</button>
<button class="tl-tab-btn type-mac" id="tl-btn-mac" onclick="switchTLTab('mac')"><i class="fab fa-apple"></i> macOS</button>
<button class="tl-tab-btn type-ios" id="tl-btn-ios" onclick="switchTLTab('ios')"><i class="fas fa-mobile-alt"></i> iOS</button>
</div>
<div class="tl-panel active type-win" id="tl-panel-win">
<div class="tl-panel-title"><i class="fab fa-windows" style="color: #00c0ff;"></i> Windows Distribution Timeline</div>
<div class="tl-scroll-hint"><i class="fas fa-arrows-alt-h"></i> <span>เลื่อนในแนวนอนเพื่อดูไทม์ไลน์ทั้งหมด</span></div>
<div class="tl-scroll-track">
<div class="tl-axis-container">
<div class="tl-axis-line" style="background: rgba(0, 192, 255, 0.25);"></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Windows 1.0</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Windows 2.0</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Windows 3.0</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Windows 95</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Windows 98</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Windows ME</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Windows 2000</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Windows XP</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Windows Vista</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Windows 7</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Windows 8</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Windows 8.1</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Windows 10</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Windows 11</div></div>
</div>
</div>
</div>
<div class="tl-panel type-lin" id="tl-panel-lin">
<div class="tl-panel-title"><i class="fab fa-linux" style="color: #f5a623;"></i> Linux Families & Derived Distributions</div>
<div class="linux-families-grid">
<div class="linux-family-card">
<div class="linux-family-name">Debian Family</div>
<div class="linux-family-badges">
<div class="linux-badge">Ubuntu</div>
<div class="linux-badge">Kali Linux</div>
<div class="linux-badge">Linux Mint</div>
</div>
</div>
<div class="linux-family-card">
<div class="linux-family-name">Red Hat Family</div>
<div class="linux-family-badges">
<div class="linux-badge">Fedora</div>
<div class="linux-badge">CentOS</div>
</div>
</div>
<div class="linux-family-card">
<div class="linux-family-name">Slackware Family</div>
<div class="linux-family-badges">
<div class="linux-badge">openSUSE</div>
</div>
</div>
<div class="linux-family-card">
<div class="linux-family-name">Arch Family</div>
<div class="linux-family-badges">
<div class="linux-badge">Manjaro</div>
</div>
</div>
</div>
</div>
<div class="tl-panel type-and" id="tl-panel-and">
<div class="tl-panel-title"><i class="fab fa-android" style="color: #3ddc84;"></i> Android Version Code Names</div>
<div class="tl-scroll-hint"><i class="fas fa-arrows-alt-h"></i> <span>เลื่อนในแนวนอนเพื่อดูไทม์ไลน์ทั้งหมด</span></div>
<div class="tl-scroll-track">
<div class="tl-axis-container">
<div class="tl-axis-line" style="background: rgba(61, 220, 132, 0.25);"></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Cupcake</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Donut</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Eclair</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Froyo</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Gingerbread</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Honeycomb</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Ice Cream Sandwich</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Jelly Bean</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">KitKat</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Lollipop</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Marshmallow</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Nougat</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Oreo</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Pie</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Android 10</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Android 11</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Android 12</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Android 12L</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Android 13</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Android 14</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Android 15</div></div>
</div>
</div>
</div>
<div class="tl-panel type-mac" id="tl-panel-mac">
<div class="tl-panel-title"><i class="fab fa-apple" style="color: #ff007f;"></i> macOS Code Names</div>
<div class="tl-scroll-hint"><i class="fas fa-arrows-alt-h"></i> <span>เลื่อนในแนวนอนเพื่อดูไทม์ไลน์ทั้งหมด</span></div>
<div class="tl-scroll-track">
<div class="tl-axis-container">
<div class="tl-axis-line" style="background: rgba(255, 0, 127, 0.25);"></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Cheetah</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Puma</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Jaguar</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Panther</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Tiger</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Leopard</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Snow Leopard</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Lion</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Mountain Lion</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Mavericks</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Yosemite</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">El Capitan</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Sierra</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">High Sierra</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Mojave</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Catalina</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Big Sur</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Monterey</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Ventura</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Sonoma</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">Sequoia</div></div>
</div>
</div>
</div>
<div class="tl-panel type-ios" id="tl-panel-ios">
<div class="tl-panel-title"><i class="fas fa-mobile-alt" style="color: #00f0ff;"></i> iOS Major Version Timeline</div>
<div class="tl-scroll-hint"><i class="fas fa-arrows-alt-h"></i> <span>เลื่อนในแนวนอนเพื่อดูไทม์ไลน์ทั้งหมด</span></div>
<div class="tl-scroll-track">
<div class="tl-axis-container">
<div class="tl-axis-line" style="background: rgba(0, 240, 255, 0.25);"></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">iPhone OS 1</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">iPhone OS 2</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">iPhone OS 3</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">iOS 4</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">iOS 5</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">iOS 6</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">iOS 7</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">iOS 8</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">iOS 9</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">iOS 10</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">iOS 11</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">iOS 12</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">iOS 13</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">iOS 14</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">iOS 15</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">iOS 16</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">iOS 17</div></div>
<div class="tl-node"><div class="tl-node-dot"></div><div class="tl-node-label">iOS 18</div></div>
</div>
</div>
</div>
</div>
<script>
function switchTLTab(tabType){
const panels=document.querySelectorAll('.tl-panel');
panels.forEach(p=>p.classList.remove('active'));
const buttons=document.querySelectorAll('.tl-tab-btn');
buttons.forEach(b=>b.classList.remove('active'));
const targetPanel=document.getElementById('tl-panel-'+tabType);
if(targetPanel){targetPanel.classList.add('active');}
const targetBtn=document.getElementById('tl-btn-'+tabType);
if(targetBtn){targetBtn.classList.add('active');}
}
</script>"""

# Replace the timelines text block completely
block_13['value'] = "### 📅 Distribution Timelines (ไทม์ไลน์เวอร์ชัน OS)\n\n" + html_timeline
blocks[13] = block_13

# Save and Commit database
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=164).update({"content": lesson.content})
db.session.commit()
print("OS Distribution Timelines converted to Interactive CSS tabbed timelines successfully!")
