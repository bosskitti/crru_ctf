"""
Fix Lesson 177 Block 1 sidebar to match Chapter 4 pattern:
- Use CSS classes (.w-sand-hdr, .w-sand-code, .w-sand-term-container, etc.)
- Use .w-sand-panel (no inline display) with class-based active
- Consistent hover/active styling with cyan (#00f0ff) theme
"""
import json, sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app

app = create_app()

NEW_SANDBOX_177 = r"""### 💻 HTTP Headers Diagnostic Sandbox (จำลองวิเคราะห์โครงสร้างข้อมูลเว็บ)

คลิกหัวข้อด้านซ้ายมือเพื่อจำลองวิเคราะห์โครงสร้าง และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อตรวจสอบทราฟฟิกข้อมูล:

<style>
.w-sandbox-main{display:flex;gap:20px;margin:2rem auto;max-width:1050px;}
@media(max-width:820px){.w-sandbox-main{flex-direction:column;}}
.w-sandbox-nav{width:220px;display:flex;flex-direction:column;gap:6px;flex-shrink:0;}
@media(max-width:820px){.w-sandbox-nav{width:100%;flex-direction:row;flex-wrap:wrap;}}
.w-nav-item{padding:8px 12px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.04);border-radius:6px;font-size:0.75rem;color:#cbd5e1;cursor:pointer;text-align:left;transition:all 0.15s ease;}
.w-nav-item:hover, .w-nav-item.active{border-color:#00f0ff;color:#ffffff;background:rgba(0,240,255,0.04);}
.w-nav-item.active{font-weight:bold;box-shadow:0 0 8px rgba(0,240,255,0.15);}
.w-sandbox-panels{flex:1;display:flex;flex-direction:column;gap:14px;}
.w-sand-panel{display:none;background:#05070f;border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:20px;box-shadow:0 8px 24px rgba(0,0,0,0.45);box-sizing:border-box;}
.w-sand-panel.active{display:block !important;}
.w-sand-hdr{font-size:0.95rem;font-weight:800;color:#ffffff;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:10px;margin-bottom:14px;display:flex;justify-content:space-between;align-items:center;}
.w-sand-hdr span.tag{font-size:0.65rem;padding:2px 8px;border-radius:4px;background:rgba(0,240,255,0.08);border:1px solid rgba(0,240,255,0.2);color:#00f0ff;font-family:'JetBrains Mono',monospace;}
.w-sand-code{font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#00f0ff;white-space:pre-wrap;margin:0 0 12px;background:rgba(0,0,0,0.2);padding:14px;border-radius:8px;border:1px solid rgba(255,255,255,0.02);}
.w-sand-term-container{position:relative;background:#02040a;border:1px solid rgba(255,255,255,0.06);border-radius:8px;margin-bottom:16px;box-shadow:inset 0 2px 8px rgba(0,0,0,0.9);overflow:hidden;}
.w-sand-term-bar{background:rgba(255,255,255,0.03);padding:6px 12px;border-bottom:1px solid rgba(255,255,255,0.05);display:flex;justify-content:space-between;align-items:center;}
.w-sand-term-title{font-size:0.65rem;color:#64748b;font-weight:800;letter-spacing:0.06em;font-family:'JetBrains Mono',monospace;}
.w-sand-term-btn{background:rgba(0,240,255,0.1);border:1px solid rgba(0,240,255,0.3);border-radius:4px;color:#00f0ff;font-size:0.68rem;padding:3px 8px;cursor:pointer;font-family:'JetBrains Mono',monospace;font-weight:700;transition:all 0.15s ease;display:flex;align-items:center;gap:4px;}
.w-sand-term-btn:hover{background:#00f0ff;color:#02040a;box-shadow:0 0 8px rgba(0,240,255,0.4);}
.w-sand-term{font-family:'JetBrains Mono',monospace;font-size:0.76rem;color:#a7f3d0;padding:12px 16px;white-space:pre-wrap;min-height:90px;}
.w-sand-term span.prompt{color:#3ddc84;}
.w-sand-term span.cmd{color:#ffffff;font-weight:bold;}
.w-sand-expl{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:16px;font-size:0.83rem;color:#cbd5e1;line-height:1.65;}
.w-sand-expl h5{margin:0 0 8px;font-size:0.85rem;color:#fbbf24;font-weight:bold;}
.w-sand-expl p{margin:0 0 10px;}
.w-sand-expl p:last-child{margin-bottom:0;}
</style>
<div class="w-sandbox-main"><div class="w-sandbox-nav"><button id="nav-item-httpget" class="w-nav-item active" onclick="showSandboxItem('httpget', this)">1. Send HTTP GET</button><button id="nav-item-httppost" class="w-nav-item" onclick="showSandboxItem('httppost', this)">2. Send HTTP POST</button></div><div class="w-sandbox-panels"><div id="panel-httpget" class="w-sand-panel active"><div class="w-sand-hdr"><span>1. HTTP GET Request Method</span> <span class="tag">HTTP Client</span></div><pre class="w-sand-code">GET /index.php HTTP/1.1
Host: ctf.rpca.ac.th
User-Agent: Mozilla/5.0
Accept: text/html
Cookie: session_id=abc123xyz</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startPostSim('httpget')">▶ Run Simulation</button></div><div id="term-httpget" class="w-sand-term"><span class="prompt">client$</span> [กดปุ่ม Run Simulation เพื่อส่ง Request]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>เมธอด GET ใช้เพื่อดึงหน้าเพจขึ้นมาแสดงผล โดยบราวเซอร์ส่ง Cookie ยืนยันสิทธิ์เซสชันแอดมิน</p></div></div><div id="panel-httppost" class="w-sand-panel"><div class="w-sand-hdr"><span>2. HTTP POST Request Method</span> <span class="tag">HTTP Client</span></div><pre class="w-sand-code">POST /login.php HTTP/1.1
Host: ctf.rpca.ac.th
Content-Type: application/x-www-form-urlencoded
Content-Length: 29

username=admin&password=secret</pre><div class="w-sand-term-container"><div class="w-sand-term-bar"><span class="w-sand-term-title">🐚 Terminal Console</span><button class="w-sand-term-btn" onclick="startPostSim('httppost')">▶ Run Simulation</button></div><div id="term-httppost" class="w-sand-term"><span class="prompt">client$</span> [กดปุ่ม Run Simulation เพื่อส่ง Request]</div></div><div class="w-sand-expl"><h5>⚙️ Command Description</h5><p>เมธอด POST ใช้เพื่อส่งข้อมูลชุดใหญ่ที่เป็นความลับ (เช่น รหัสผ่าน) ไปประมวลผลบนเซิร์ฟเวอร์โดยไม่โชว์บน URL</p></div></div></div></div>
<script>
window.showSandboxItem = function(itemKey, element) {
  var items = document.querySelectorAll('.w-sandbox-nav .w-nav-item');
  items.forEach(function(i) { i.classList.remove('active'); });
  element.classList.add('active');
  var panels = document.querySelectorAll('.w-sand-panel');
  panels.forEach(function(p) { p.classList.remove('active'); });
  var targetPanel = document.getElementById('panel-' + itemKey);
  if (targetPanel) { targetPanel.classList.add('active'); }
}
window.startPostSim = function(itemKey) {
  var term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span class="prompt">client$</span> <span class="cmd">Sending HTTP Request...</span>\n[.] Accessing remote port 80/443\n[.] Reading Response Headers...';
  setTimeout(function() {
    if (itemKey === 'httpget') {
      term.innerHTML = '<span class="prompt">client$</span> <span style="color:#3ddc84; font-weight:bold;">HTTP/1.1 200 OK</span>\nServer: Apache/2.4.41 (Ubuntu)\nContent-Type: text/html\nContent-Length: 1042\n\n&lt;html&gt;&lt;body&gt;&lt;h1&gt;Welcome to RPCA Cyber Club&lt;/h1&gt;&lt;/body&gt;&lt;/html&gt;';
    } else if (itemKey === 'httppost') {
      term.innerHTML = '<span class="prompt">client$</span> <span style="color:#fbbf24; font-weight:bold;">HTTP/1.1 302 Found</span>\nServer: Apache/2.4.41 (Ubuntu)\nLocation: /dashboard.php\nSet-Cookie: session_id=abc123xyz; Path=/; HttpOnly\n\n[+] Redirecting to dashboard...';
    }
  }, 1000);
}
setTimeout(function() {
  var activeBtn = document.querySelector('.w-sandbox-nav .w-nav-item.active');
  if (activeBtn) { activeBtn.click(); }
}, 100);
</script>"""

with app.app_context():
    from CTFd.plugins.tutorials import TutorialLesson
    db = app.db
    lesson = db.session.query(TutorialLesson).filter_by(id=177).first()
    if lesson:
        blocks = json.loads(lesson.content)
        blocks[1]["value"] = NEW_SANDBOX_177
        lesson.content = json.dumps(blocks, ensure_ascii=False)
        db.session.commit()
        print("[OK] Lesson 177 Block 1 updated with Chapter-4 style sidebar!")
    else:
        print("[!] Lesson 177 not found")
