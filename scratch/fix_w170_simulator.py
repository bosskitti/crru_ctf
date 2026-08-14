import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l170 = db.session.query(TutorialLesson).filter_by(id=170).first()
blocks = json.loads(l170.content)

# ─── Replace Block 2 with fixed Javascript string concatenation ───
blocks[2]['value'] = """### 🛡️ Brute-forcing & Automation Skills

**การรันระบบอัตโนมัติ (Automation)** นิยมใช้สำหรับการประมวลผลงานซ้ำๆ และกู้คืนรหัสผ่านด้วยกระบวนการ **Brute-forcing** ซึ่งจำลองการโจมตีพจนานุกรม (Dictionary Attack) โดยทดสอบคู่คำรหัสผ่านทั้งหมดจาก Wordlist จนกว่าจะเข้าระบบได้สำเร็จ:

<style>
.bf-console{background:#070910;border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:20px;max-width:1050px;margin:2rem auto;box-shadow:0 8px 24px rgba(0,0,0,0.5);box-sizing:border-box;}
.bf-header{display:flex;justify-content:between;align-items:center;border-bottom:1px solid rgba(255,255,255,0.08);padding-bottom:10px;margin-bottom:14px;}
.bf-title{font-family:'JetBrains Mono',monospace;font-size:0.82rem;color:#e2e8f0;font-weight:bold;}
.bf-title span{color:#00f0ff;}
.bf-btn{padding:6px 14px;background:#00f0ff;border:none;border-radius:4px;font-family:'JetBrains Mono',monospace;font-size:0.75rem;font-weight:800;color:#070910;cursor:pointer;}
.bf-btn:hover{background:#ffffff;}

.bf-table{width:100%;border-collapse:collapse;font-family:'JetBrains Mono',monospace;font-size:0.78rem;}
.bf-table th{text-align:left;color:#8a94a6;padding:8px;border-bottom:1px solid rgba(255,255,255,0.06);}
.bf-table td{padding:8px;color:#cbd5e1;}
.bf-status{font-weight:bold;}
.bf-status.trying{color:#fbbf24;}
.bf-status.failed{color:#ff007f;}
.bf-status.success{color:#3ddc84;text-shadow:0 0 8px rgba(61,220,132,0.45);}
</style>

<div class="bf-console">
<div class="bf-header">
<div class="bf-title">⚡ <span>Brute-force Live Attack Simulator</span></div>
<button id="run-bf-btn" class="bf-btn" onclick="startBruteForceSimulation()">Start Attack Simulation</button>
</div>
<table class="bf-table">
<thead>
<tr>
<th>Username</th>
<th>Password Attempt</th>
<th>Status</th>
</tr>
</thead>
<tbody id="bf-tbody">
<tr>
<td colspan="3" style="color:#64748b; text-align:center; padding:20px;">กดปุ่มเพื่อจำลองลำดับกระบวนการรันเจาะระบบแบบเรียลไทม์</td>
</tr>
</tbody>
</table>
</div>

<script>
let bfInterval = null;
window.startBruteForceSimulation = function() {
  const btn = document.getElementById('run-bf-btn');
  btn.disabled = true;
  btn.textContent = "Attacking...";

  const tbody = document.getElementById('bf-tbody');
  tbody.innerHTML = '';

  const wordlist = [
    { u: 'admin', p: 'a1234567', s: 'FAILED' },
    { u: 'admin', p: 'aa123456', s: 'FAILED' },
    { u: 'admin', p: 'aaa12345', s: 'FAILED' },
    { u: 'admin', p: 'aaaa1234', s: 'FAILED' },
    { u: 'admin', p: 'aaaaa123', s: 'SUCCESS' }
  ];

  let step = 0;
  
  if (bfInterval) clearInterval(bfInterval);

  bfInterval = setInterval(function() {
    if (step < wordlist.length) {
      const current = wordlist[step];
      
      // Update previous attempts to FAILED instantly
      const rows = tbody.querySelectorAll('tr');
      if (rows.length > 0) {
        const lastRow = rows[rows.length - 1];
        const statusTd = lastRow.querySelector('.bf-status');
        if (statusTd && statusTd.textContent === 'TRYING...') {
          statusTd.textContent = 'FAILED';
          statusTd.className = 'bf-status failed';
        }
      }

      // Add new row using stable string concatenation instead of template literals
      const tr = document.createElement('tr');
      tr.innerHTML = '<td>' + current.u + '</td><td>' + current.p + '</td><td class="bf-status trying">TRYING...</td>';
      tbody.appendChild(tr);
      
      if (current.s === 'SUCCESS') {
        setTimeout(function() {
          const statusTd = tr.querySelector('.bf-status');
          statusTd.textContent = 'SUCCESS';
          statusTd.className = 'bf-status success';
          btn.disabled = false;
          btn.textContent = "Attack Done!";
          clearInterval(bfInterval);
        }, 600);
      }
      
      step++;
    }
  }, 900);
}
</script>"""

l170.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=170).update({"content": l170.content})
db.session.commit()
print("Brute-force simulator fixed with stable JS string concatenation!")
ctx.pop()
