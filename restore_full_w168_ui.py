import json
from CTFd import create_app
from CTFd.models import db
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
with app.app_context():
    l168 = TutorialLesson.query.get(168)
    # Load b_layers from interactive_w168_full_map.py logic
    b_layers_val = """### ⚙️ Windows System Architecture Layers

คลิกหรือเลื่อนเมาส์ชี้ไปที่แต่ละกล่ององค์ประกอบในผังโครงสร้างสถาปัตยกรรม Windows ด้านซ้าย เพื่อดูคำอธิบายและหน้าที่การทำงานของส่วนประกอบนั้นๆ ทางด้านขวา:

<style>
.w-full-arch{width:100%;max-width:1050px;margin:2rem auto;display:flex;gap:24px;background:#0d0e15;border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:24px;box-shadow:0 8px 32px rgba(0,0,0,0.4);box-sizing:border-box;}
@media(max-width:960px){.w-full-arch{flex-direction:column;}}

.w-arch-map{width:55%;flex-shrink:0;display:flex;flex-direction:column;gap:8px;font-family:'JetBrains Mono',monospace;}
@media(max-width:960px){.w-arch-map{width:100%;}}

.w-mode-sec{border:1px solid;border-radius:8px;padding:12px;position:relative;display:flex;flex-direction:column;gap:8px;}
.w-mode-sec.user-mode{border-color:rgba(0,240,255,0.2);background:rgba(0,240,255,0.01);}
.w-mode-sec.kernel-mode{border-color:rgba(255,0,127,0.2);background:rgba(255,0,127,0.01);}
.w-mode-title-tag{font-size:0.68rem;font-weight:800;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:4px;}
.user-mode .w-mode-title-tag{color:#00f0ff;}
.kernel-mode .w-mode-title-tag{color:#ff007f;}

.w-row{display:flex;gap:6px;width:100%;}
.w-col{display:flex;flex-direction:column;gap:6px;}

.wnode{padding:8px 4px;border-radius:5px;border:1px solid rgba(255,255,255,0.08);background:rgba(255,255,255,0.03);text-align:center;font-size:0.72rem;font-weight:700;color:#94a3b8;cursor:pointer;transition:all 0.18s ease;user-select:none;display:flex;align-items:center;justify-content:center;min-height:32px;box-sizing:border-box;}
.wnode:hover, .wnode.active{color:#ffffff;transform:scale(1.02);box-shadow:0 0 10px rgba(255,255,255,0.1);background:rgba(255,255,255,0.08);}

.wnode.clr-app{border-color:rgba(61,220,132,0.25);background:rgba(61,220,132,0.03);color:#3ddc84;}
.wnode.clr-app:hover, .wnode.clr-app.active{border-color:#3ddc84;background:rgba(61,220,132,0.15);box-shadow:0 0 12px rgba(61,220,132,0.35);color:#ffffff;}

.wnode.clr-subsys{border-color:rgba(0,240,255,0.25);background:rgba(0,240,255,0.03);color:#00f0ff;}
.wnode.clr-subsys:hover, .wnode.clr-subsys.active{border-color:#00f0ff;background:rgba(0,240,255,0.15);box-shadow:0 0 12px rgba(0,240,255,0.35);color:#ffffff;}

.wnode.clr-ntdll{border-color:rgba(251,191,36,0.25);background:rgba(251,191,36,0.03);color:#fbbf24;}
.wnode.clr-ntdll:hover, .wnode.clr-ntdll.active{border-color:#fbbf24;background:rgba(251,191,36,0.15);box-shadow:0 0 12px rgba(251,191,36,0.35);color:#ffffff;}

.wnode.clr-trap{border-color:rgba(244,114,182,0.25);background:rgba(244,114,182,0.03);color:#f472b6;}
.wnode.clr-trap:hover, .wnode.clr-trap.active{border-color:#f472b6;background:rgba(244,114,182,0.15);box-shadow:0 0 12px rgba(244,114,182,0.35);color:#ffffff;}

.wnode.clr-exec{border-color:rgba(171,32,253,0.25);background:rgba(171,32,253,0.03);color:#ab20fd;}
.wnode.clr-exec:hover, .wnode.clr-exec.active{border-color:#ab20fd;background:rgba(171,32,253,0.15);box-shadow:0 0 12px rgba(171,32,253,0.35);color:#ffffff;}

.wnode.clr-hal{border-color:rgba(255,0,127,0.25);background:rgba(255,0,127,0.03);color:#ff007f;}
.wnode.clr-hal:hover, .wnode.clr-hal.active{border-color:#ff007f;background:rgba(255,0,127,0.15);box-shadow:0 0 12px rgba(255,0,127,0.35);color:#ffffff;}

.w-arch-info{flex:1;background:rgba(15,17,26,0.5);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:20px;display:flex;flex-direction:column;}
.w-info-header{display:flex;align-items:center;gap:10px;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:10px;margin-bottom:12px;}
.w-info-badge{font-size:0.68rem;font-weight:800;padding:2px 8px;border-radius:4px;text-transform:uppercase;letter-spacing:0.05em;}
.w-info-badge.user{background:rgba(0,240,255,0.08);border:1px solid rgba(0,240,255,0.25);color:#00f0ff;}
.w-info-badge.kernel{background:rgba(255,0,127,0.08);border:1px solid rgba(255,0,127,0.25);color:#ff007f;}
.w-info-title{font-size:1rem;font-weight:700;color:#ffffff;margin:0;}
.w-info-body{font-size:0.86rem;color:#94a3b8;line-height:1.7;}
.w-info-body p{margin:0 0 10px;}
.w-info-body strong{color:#fbbf24;}
</style>

<div class="w-full-arch">
  <div class="w-arch-map">
    <div class="w-mode-sec user-mode">
      <div class="w-mode-title-tag">User Mode (Ring 3)</div>
      <div class="w-row">
        <div class="wnode clr-app active" style="flex:1;" onclick="showWInfo('apps', this)" onmouseover="showWInfo('apps', this)">Applications</div>
      </div>
      <div class="w-row">
        <div class="wnode clr-subsys" style="width:100px;" onclick="showWInfo('subsys-srv', this)" onmouseover="showWInfo('subsys-srv', this)">Subsystem<br>servers</div>
        <div class="w-col" style="flex:1;">
          <div class="w-row">
            <div class="wnode clr-subsys" style="flex:1;" onclick="showWInfo('dlls', this)" onmouseover="showWInfo('dlls', this)">DLLs</div>
            <div class="wnode clr-subsys" style="flex:1;" onclick="showWInfo('sys-srv', this)" onmouseover="showWInfo('sys-srv', this)">System Services</div>
            <div class="wnode clr-subsys" style="flex:1;" onclick="showWInfo('login-gina', this)" onmouseover="showWInfo('login-gina', this)">Login/GINA</div>
          </div>
          <div class="w-row">
            <div class="wnode clr-subsys" style="flex:1;" onclick="showWInfo('kernel32', this)" onmouseover="showWInfo('kernel32', this)">Kernel32</div>
            <div class="wnode clr-subsys" style="flex:1;" onclick="showWInfo('crit-srv', this)" onmouseover="showWInfo('crit-srv', this)">Critical services</div>
            <div class="wnode clr-subsys" style="flex:1;" onclick="showWInfo('user32-gdi', this)" onmouseover="showWInfo('user32-gdi', this)">User32 / GDI</div>
          </div>
        </div>
      </div>
      <div class="w-row">
        <div class="wnode clr-ntdll" style="flex:1;" onclick="showWInfo('ntdll', this)" onmouseover="showWInfo('ntdll', this)">ntdll / run-time library</div>
      </div>
    </div>
    
    <div class="w-mode-sec kernel-mode">
      <div class="w-mode-title-tag">Kernel Mode (Ring 0)</div>
      <div class="w-row">
        <div class="wnode clr-trap" style="flex:1;" onclick="showWInfo('trap', this)" onmouseover="showWInfo('trap', this)">Trap interface / LPC</div>
      </div>
      <div class="w-row">
        <div class="wnode clr-exec" style="flex:1;" onclick="showWInfo('sec-ref', this)" onmouseover="showWInfo('sec-ref', this)">Security refmon</div>
        <div class="wnode clr-exec" style="flex:1.2;" onclick="showWInfo('io-mgr', this)" onmouseover="showWInfo('io-mgr', this)">I/O Manager</div>
        <div class="wnode clr-exec" style="flex:1;" onclick="showWInfo('mem-mgr', this)" onmouseover="showWInfo('mem-mgr', this)">Memory Manger</div>
        <div class="wnode clr-exec" style="flex:1;" onclick="showWInfo('proc-thread', this)" onmouseover="showWInfo('proc-thread', this)">Procs & threads</div>
        <div class="wnode clr-exec" style="flex:1;" onclick="showWInfo('win32-gui', this)" onmouseover="showWInfo('win32-gui', this)">Win32 GUI</div>
      </div>
      <div class="w-row">
        <div class="w-col" style="flex:1.2;gap:4px;">
          <div class="w-row" style="gap:4px;">
            <div class="wnode clr-exec" style="flex:1;font-size:0.62rem;min-height:26px;padding:2px;" onclick="showWInfo('net-dev', this)" onmouseover="showWInfo('net-dev', this)">Net devices</div>
            <div class="wnode clr-exec" style="flex:1;font-size:0.62rem;min-height:26px;padding:2px;" onclick="showWInfo('file-filt', this)" onmouseover="showWInfo('file-filt', this)">File filters</div>
          </div>
          <div class="w-row" style="gap:4px;">
            <div class="wnode clr-exec" style="flex:1;font-size:0.62rem;min-height:26px;padding:2px;" onclick="showWInfo('net-prot', this)" onmouseover="showWInfo('net-prot', this)">Net protocols</div>
            <div class="wnode clr-exec" style="flex:1;font-size:0.62rem;min-height:26px;padding:2px;" onclick="showWInfo('file-sys', this)" onmouseover="showWInfo('file-sys', this)">File systems</div>
          </div>
          <div class="w-row" style="gap:4px;">
            <div class="wnode clr-exec" style="flex:1;font-size:0.62rem;min-height:26px;padding:2px;" onclick="showWInfo('net-intf', this)" onmouseover="showWInfo('net-intf', this)">Net interfaces</div>
            <div class="wnode clr-exec" style="flex:1;font-size:0.62rem;min-height:26px;padding:2px;" onclick="showWInfo('vol-mgr', this)" onmouseover="showWInfo('vol-mgr', this)">Volume mgrs</div>
          </div>
          <div class="w-row">
            <div class="wnode clr-exec" style="flex:1;font-size:0.65rem;min-height:26px;" onclick="showWInfo('dev-stack', this)" onmouseover="showWInfo('dev-stack', this)">Device stacks</div>
          </div>
        </div>
        <div class="w-col" style="flex:1;justify-content:center;gap:6px;">
          <div class="wnode clr-exec" style="flex:1;" onclick="showWInfo('filesys-rt', this)" onmouseover="showWInfo('filesys-rt', this)">Filesys run-time</div>
          <div class="wnode clr-exec" style="flex:1;" onclick="showWInfo('cache-mgr', this)" onmouseover="showWInfo('cache-mgr', this)">Cache mgr</div>
        </div>
        <div class="w-col" style="flex:1;justify-content:center;gap:6px;">
          <div class="wnode clr-exec" style="flex:1;" onclick="showWInfo('scheduler', this)" onmouseover="showWInfo('scheduler', this)">Scheduler</div>
          <div class="wnode clr-exec" style="flex:1;" onclick="showWInfo('sync', this)" onmouseover="showWInfo('sync', this)">Synchronization</div>
        </div>
      </div>
      <div class="w-row">
        <div class="wnode clr-exec" style="flex:1;" onclick="showWInfo('obj-mgr', this)" onmouseover="showWInfo('obj-mgr', this)">Object Manager / Configuration Management (registry)</div>
      </div>
      <div class="w-row">
        <div class="wnode clr-hal" style="flex:1;" onclick="showWInfo('hal', this)" onmouseover="showWInfo('hal', this)">Kernel run-time / Hardware Abstraction Layer</div>
      </div>
    </div>
  </div>
  
  <div class="w-arch-info">
    <div class="w-info-header">
      <span id="win-badge" class="w-info-badge user">User Mode</span>
      <h4 id="win-title" class="w-info-title">Applications</h4>
    </div>
    <div id="win-desc" class="w-info-body">
      <p>โปรแกรมระดับบนสุดที่ผู้ใช้งานเรียกใช้งานโดยตรง เช่น <strong>Web Browser (Chrome, Edge), Text Editors, Microsoft Office</strong> รวมถึงซอฟต์แวร์ประยุกต์อื่นๆ</p>
      <p>แอปพลิเคชันเหล่านี้จะทำงานภายใต้กรอบการควบคุมของ User Mode (Ring 3) อย่างเข้มงวด โดยมีพื้นที่หน่วยความจำจำลองของตัวเอง (Virtual Address Space) และไม่สามารถติดต่อสั่งงานฮาร์ดแวร์โดยตรงได้เพื่อความปลอดภัยของระบบ</p>
    </div>
  </div>
</div>

<script>
const winArchData = {
  'apps': { title: 'Applications (โปรแกรมประยุกต์)', badge: 'User Mode', badgeClass: 'user', desc: '<p>โปรแกรมประยุกต์ที่ผู้ใช้งานเรียกเปิดใช้ เช่น <strong>Chrome, Word, Discord</strong></p>' },
  'subsys-srv': { title: 'Subsystem Servers (เซิร์ฟเวอร์ระบบย่อย)', badge: 'User Mode', badgeClass: 'user', desc: '<p>ควบคุมสภาพแวดล้อมเฉพาะตัวของ Windows เช่น <code>csrss.exe</code></p>' },
  'dlls': { title: 'DLLs (Dynamic Link Libraries)', badge: 'User Mode', badgeClass: 'user', desc: '<p>เก็บชุดคำสั่งกลางที่เปิดให้โปรแกรมประยุกต์หลายตัวเรียกใช้งานร่วมกัน</p>' },
  'sys-srv': { title: 'System Services', badge: 'User Mode', badgeClass: 'user', desc: '<p>บริการระบบปฏิบัติการที่ทำงานอยู่ส่วนหลัง (Background Services)</p>' },
  'login-gina': { title: 'Login / GINA', badge: 'User Mode', badgeClass: 'user', desc: '<p>ส่วนยืนยันตัวตนก่อนปล่อยสิทธิ์เข้าสู่หน้า Desktop</p>' },
  'kernel32': { title: 'Kernel32.dll', badge: 'User Mode', badgeClass: 'user', desc: '<p>รับข้อกำหนด API จากโปรแกรมเพื่อควบคุม Process และ Memory</p>' },
  'crit-srv': { title: 'Critical Services', badge: 'User Mode', badgeClass: 'user', desc: '<p>บริการสำคัญเช่น <code>lsass.exe</code> ตรวจความปลอดภัยบัญชี</p>' },
  'user32-gdi': { title: 'User32 / GDI', badge: 'User Mode', badgeClass: 'user', desc: '<p>ควบคุมการวาดหน้าต่าง UI กราฟิก เมาส์ และตัวอักษร</p>' },
  'ntdll': { title: 'ntdll.dll (Native API)', badge: 'User Mode', badgeClass: 'user', desc: '<p>สะพานด่านสุดท้ายก่อนข้ามจาก User Mode ไป Kernel Mode</p>' },
  'trap': { title: 'Trap Interface / LPC', badge: 'Kernel Mode', badgeClass: 'kernel', desc: '<p>ประตูด่านตรวจรับ System Calls สลับสิทธิ์เข้าสู่โหมดเคอร์เนล</p>' },
  'sec-ref': { title: 'Security Reference Monitor (SRM)', badge: 'Kernel Mode', badgeClass: 'kernel', desc: '<p>ตรวจสอบ Token สิทธิ์ความปลอดภัยและการเข้าถึงไฟล์ตามกฎ NTFS</p>' },
  'io-mgr': { title: 'I/O Manager', badge: 'Kernel Mode', badgeClass: 'kernel', desc: '<p>จัดการการรับส่งข้อมูลระหว่างฮาร์ดแวร์ อุปกรณ์จัดเก็บ และไฟล์ระบบ</p>' },
  'mem-mgr': { title: 'Memory Manager', badge: 'Kernel Mode', badgeClass: 'kernel', desc: '<p>จัดสรรพื้นที่ RAM กายภาพและ Virtual Memory</p>' },
  'proc-thread': { title: 'Process & Thread Manager', badge: 'Kernel Mode', badgeClass: 'kernel', desc: '<p>สร้าง ระงับ และควบคุมวงจรชีวิตของ Process ทั้งหมดในเครื่อง</p>' },
  'win32-gui': { title: 'Win32k.sys (Kernel GUI)', badge: 'Kernel Mode', badgeClass: 'kernel', desc: '<p>ส่วนเคอร์เนลสำหรับประมวลผลกราฟิกและ Driver จอภาพ</p>' },
  'net-dev': { title: 'Net Devices / Protocols', badge: 'Kernel Mode', badgeClass: 'kernel', desc: '<p>ไดรเวอร์การ์ดจอ ไดรเวอร์แลน และโพรโทคอลเครือข่าย TCP/IP</p>' },
  'file-filt': { title: 'File Filters / File Systems', badge: 'Kernel Mode', badgeClass: 'kernel', desc: '<p>ระบบไฟล์ NTFS, FAT32 และฟิลเตอร์สแกนไวรัส</p>' },
  'dev-stack': { title: 'Device Stacks', badge: 'Kernel Mode', badgeClass: 'kernel', desc: '<p>ซ้อนชั้นไดรเวอร์อุปกรณ์เพื่อควบคุมคีย์บอร์ด เมาส์ และ USB</p>' },
  'filesys-rt': { title: 'Filesys Run-time', badge: 'Kernel Mode', badgeClass: 'kernel', desc: '<p>ส่วนประมวลผลชุดคำสั่งการอ่านเขียนไฟล์ความเร็วสูง</p>' },
  'cache-mgr': { title: 'Cache Manager', badge: 'Kernel Mode', badgeClass: 'kernel', desc: '<p>ทำแคชข้อมูลดิสก์บน RAM เพื่อเร่งความเร็วระบบ</p>' },
  'scheduler': { title: 'Thread Scheduler', badge: 'Kernel Mode', badgeClass: 'kernel', desc: '<p>จัดคิวการทำงานของ CPU Cores ให้กับงานแต่ละ Thread</p>' },
  'sync': { title: 'Synchronization Primitives', badge: 'Kernel Mode', badgeClass: 'kernel', desc: '<p>กลไก Mutex / Spinlock ป้องกันการชนกันของข้อมูลใน RAM</p>' },
  'obj-mgr': { title: 'Object Manager & Registry', badge: 'Kernel Mode', badgeClass: 'kernel', desc: '<p>จัดการออบเจกต์ทรัพยากรระบบและฐานข้อมูล Registry</p>' },
  'hal': { title: 'HAL (Hardware Abstraction Layer)', badge: 'Kernel Mode', badgeClass: 'kernel', desc: '<p>ชั้นล่างสุดที่คุยกับ CPU, Motherboard และ Hardware โดยตรง</p>' }
};

function showWInfo(key, el) {
  document.querySelectorAll('.wnode').forEach(n => n.classList.remove('active'));
  if(el) el.classList.add('active');
  const d = winArchData[key];
  if(!d) return;
  const b = document.getElementById('win-badge');
  b.innerText = d.badge;
  b.className = 'w-info-badge ' + d.badgeClass;
  document.getElementById('win-title').innerText = d.title;
  document.getElementById('win-desc').innerHTML = d.desc;
}
</script>"""

    # Load b_tree from expand_wsa_tree.py logic
    b_tree_val = """### 📁 Windows File System & Directory Structure

ต่างจาก Linux ที่รวมทุกอย่างเข้ากับ Root Directory (/) เพียงอันเดียว ระบบปฏิบัติการ Windows ใช้สถาปัตยกรรมแบบ **หลายพาร์ติชัน (Multi-Partitions)** โดยแบ่งข้อมูลจัดเก็บออกเป็นไดรฟ์ต่างๆ เช่น **C:, D:, E:**

<style>
.wfs-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:24px;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:28px;box-shadow:0 8px 32px rgba(0,0,0,0.4);box-sizing:border-box;}

.tree-container{width:100%;display:flex;flex-direction:column;align-items:center;padding:20px 0;overflow-x:auto;scrollbar-width:thin;}
.tree-branch{display:flex;justify-content:center;gap:12px;position:relative;}

.tnode{display:flex;flex-direction:column;align-items:center;padding:8px 12px;background:rgba(7,9,16,0.88);border:1px solid rgba(255,255,255,0.08);border-radius:8px;font-family:'JetBrains Mono',monospace;font-size:0.75rem;font-weight:700;color:#e2e8f0;transition:all 0.2s ease;z-index:2;position:relative;min-width:70px;text-align:center;}
.tnode:hover{border-color:#00f0ff;box-shadow:0 0 12px rgba(0,240,255,0.3);transform:translateY(-2px);color:#ffffff;}
.tnode-icon{font-size:1.3rem;margin-bottom:3px;}
.tnode.root{border-color:#00f0ff;background:rgba(0,240,255,0.04);color:#00f0ff;min-width:110px;}
.tnode.sub{border-color:#fbbf24;background:rgba(251,191,36,0.04);color:#fbbf24;min-width:90px;}
.tnode.file{border-color:rgba(255,255,255,0.12);background:rgba(255,255,255,0.02);color:#94a3b8;font-size:0.68rem;padding:5px 8px;min-width:65px;}
.tnode.file .tnode-icon{font-size:1rem;color:#94a3b8;}

.file-grp{display:flex;gap:4px;margin-top:10px;}
.t-spine-v{width:2px;height:24px;background:rgba(255,255,255,0.12);margin:0 auto;position:relative;}
.t-spine-h{height:2px;background:rgba(255,255,255,0.12);position:absolute;top:-12px;left:0;right:0;width:calc(100% - 140px);margin:0 auto;}
.t-connector-down{width:2px;height:12px;background:rgba(255,255,255,0.12);position:absolute;top:-12px;left:50%;transform:translateX(-50%);}
.t-col{display:flex;flex-direction:column;align-items:center;position:relative;}

.wfs-exp-panel{background:rgba(15,17,26,0.6);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:20px;margin-top:12px;}
.wfs-exp-hdr{font-size:0.95rem;font-weight:700;color:#ffffff;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:8px;margin-bottom:12px;display:flex;align-items:center;gap:8px;}
.wfs-exp-hdr span{color:#00f0ff;}
.wfs-exp-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;}
@media(max-width:768px){.wfs-exp-grid{grid-template-columns:1fr;}}
.wfs-exp-card{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:12px 14px;}
.wfs-exp-title{font-size:0.83rem;font-weight:700;margin-bottom:6px;}
.wfs-exp-title.t-root{color:#00f0ff;}
.wfs-exp-title.t-sub{color:#fbbf24;}
.wfs-exp-title.t-file{color:#94a3b8;}
.wfs-exp-desc{font-size:0.8rem;color:#94a3b8;line-height:1.6;margin:0;}
</style>

<div class="wfs-wrap">
<div class="tree-container">
<div class="tree-branch">
<div class="tnode root">
<span class="tnode-icon">💽</span>
<span>C:\\ (Root)</span>
</div>
</div>
<div class="t-spine-v"></div>
<div class="tree-branch" style="width:100%;max-width:980px;">
<div class="t-spine-h" style="width:75%;"></div>
<div class="w-row" style="justify-content:center;gap:40px;width:100%;">
<div class="t-col" style="flex:1;">
<div class="t-connector-down"></div>
<div class="tnode sub">
<span class="tnode-icon">📁</span>
<span>DOS</span>
</div>
<div class="t-spine-v"></div>
<div class="file-grp">
<div class="tnode file"><span class="tnode-icon">📄</span><span>file1.txt</span></div>
<div class="tnode file"><span class="tnode-icon">📄</span><span>file2.txt</span></div>
<div class="tnode file"><span class="tnode-icon">📄</span><span>file3.txt</span></div>
</div>
</div>
<div class="t-col" style="flex:1;">
<div class="t-connector-down"></div>
<div class="tnode sub">
<span class="tnode-icon">📁</span>
<span>XLS</span>
</div>
<div class="t-spine-v"></div>
<div class="file-grp">
<div class="tnode file"><span class="tnode-icon">📊</span><span>budget.xls</span></div>
<div class="tnode file"><span class="tnode-icon">📊</span><span>sales.xls</span></div>
</div>
</div>
<div class="t-col" style="flex:1;">
<div class="t-connector-down"></div>
<div class="tnode sub">
<span class="tnode-icon">📁</span>
<span>DOC</span>
</div>
<div class="t-spine-v"></div>
<div class="file-grp">
<div class="tnode file"><span class="tnode-icon">📝</span><span>doc1.doc</span></div>
</div>
</div>
</div>
</div>
</div>

<div class="wfs-exp-panel">
<div class="wfs-exp-hdr"><span>📌</span> คำอธิบายองค์ประกอบโครงสร้างระบบไฟล์ Windows</div>
<div class="wfs-exp-grid">
<div class="wfs-exp-card">
<div class="wfs-exp-title t-root">1. Root Directory (ไดเรกทอรีราก)</div>
<p class="wfs-exp-desc">จุดเริ่มต้นของแต่ละไดร์ฟ (เช่น <code>C:\\</code>) ใช้เก็บระบบปฏิบัติการและไฟล์ระบบระดับบนสุด</p>
</div>
<div class="wfs-exp-card">
<div class="wfs-exp-title t-sub">2. Subdirectories (โฟลเดอร์ย่อย)</div>
<p class="wfs-exp-desc">โฟลเดอร์สำหรับแบ่งหมวดหมู่ข้อมูล เช่น <code>DOS</code>, <code>Program Files</code>, <code>Users</code></p>
</div>
<div class="wfs-exp-card">
<div class="wfs-exp-title t-file">3. Files (ไฟล์ข้อมูล)</div>
<p class="wfs-exp-desc">เอกสารหรือโปรแกรมที่จัดเก็บอยู่ภายใน เช่น <code>.txt</code>, <code>.doc</code>, <code>.exe</code></p>
</div>
</div>
</div>
</div>"""

    b0_header = {'type': 'markdown', 'value': '## 🛡️ โครงสร้างระบบและการจัดการสิทธิ์ใน WINDOWS (WINDOWS ARCHITECTURE & PERMISSIONS)'}

    b1_intro = {'type': 'markdown', 'value': '''<div class="s-intro cyan" style="margin-top: 1rem; margin-bottom: 2rem;">
  <div class="s-intro-icon">💻</div>
  <div class="s-intro-body">
    <strong style="font-size: 1.1rem; color: #ffffff; margin-bottom: 8px; display: block;">ภาพรวมโครงสร้างระบบและการจัดการสิทธิ์ใน Windows (Windows Architecture & Permissions)</strong>
    <p style="margin-bottom: 8px; color: #cbd5e1; font-size: 0.9rem;">ยินดีต้อนรับสู่บทเรียนระบบปฏิบัติการ <strong>Microsoft Windows</strong> ซึ่งเป็นระบบปฏิบัติการฝั่ง Desktop ที่มีผู้ใช้งานมากที่สุดในโลก (กว่า 75% ของตลาด) 💻</p>
    <p style="margin-bottom: 0; color: #cbd5e1; font-size: 0.9rem;">ในบทเรียนนี้เราจะได้เรียนรู้สถาปัตยกรรมภายในแบบ <strong>Hybrid Kernel (User Mode vs Kernel Mode)</strong>, ระบบจัดเก็บข้อมูลแบบหลายไดรฟ์ (<code>C:\\</code>, <code>D:\\</code>), โครงสร้างโฟลเดอร์สำคัญ ตลอดจนการบริหารจัดการสิทธิ์ความปลอดภัยในระบบครับ 🛡️</p>
  </div>
</div>'''}

    b2_overview = {'type': 'markdown', 'value': '''### 📌 Overviews of Windows (ภาพรวมระบบปฏิบัติการ Windows)

น้องๆ น่าจะคุ้นเคยกับ **Microsoft Windows** กันดีอยู่แล้วใช่มั้ยครับ? 😊 Windows ถือเป็น OS สำหรับคอมพิวเตอร์ตั้งโต๊ะที่มีผู้ใช้งานมากที่สุดในโลก (มากกว่า 75% ของตลาด Desktop) พัฒนาโดยบริษัท Microsoft ตั้งแต่ปี 1985 บนฐานของ MS-DOS จนวิวัฒนาการมาเป็น Windows 10 และ Windows 11 ที่เราใช้กันในปัจจุบันครับ! 🚀'''}

    b3_rings = {'type': 'markdown', 'value': '''### 🏛️ Windows System Architecture (สถาปัตยกรรมภายในของระบบปฏิบัติการ Windows)

สถาปัตยกรรมของ Windows ถูกออกแบบในลักษณะ **Hybrid Kernel** ที่แบ่งพื้นที่ทำงานออกเป็น 2 ระดับหลักคือ **User Mode** (สำหรับแอปพลิเคชันของผู้ใช้ทั่วไป) และ **Kernel Mode** (สำหรับระบบแกนกลางและไดรเวอร์อุปกรณ์) ซึ่งเป็นกลไกสำคัญในการรักษาความเสถียรและความปลอดภัยของระบบครับ! 🛡️

<style>
.wsa-wrap{width:100%;margin:2rem auto;display:flex;gap:36px;align-items:center;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:32px;box-shadow:0 4px 20px rgba(0,0,0,0.25);box-sizing:border-box;}
@media(max-width:820px){.wsa-wrap{flex-direction:column;}}
.wsa-diagram-wrap{flex-shrink:0;position:relative;width:340px;height:340px;display:flex;align-items:center;justify-content:center;}
.wsa-r-user{width:320px;height:320px;border:1.2px solid #00f0ff;border-radius:50%;background:transparent;box-shadow:0 0 12px rgba(0,240,255,0.12), inset 0 0 10px rgba(0,240,255,0.04);position:relative;display:flex;align-items:center;justify-content:center;}
.wsa-r-kernel{width:220px;height:220px;border:1.2px solid #ff007f;border-radius:50%;background:transparent;box-shadow:0 0 12px rgba(255,0,127,0.12), inset 0 0 10px rgba(255,0,127,0.04);position:relative;display:flex;align-items:center;justify-content:center;}
.wsa-r-hardware{width:120px;height:120px;border:1.2px solid #fbbf24;border-radius:50%;background:rgba(251,191,36,0.12);box-shadow:0 0 18px rgba(251,191,36,0.2), inset 0 0 10px rgba(251,191,36,0.08);display:flex;align-items:center;justify-content:center;position:relative;}
.wsa-lbl{position:absolute;font-family:'JetBrains Mono',monospace;font-size:0.75rem;font-weight:800;letter-spacing:0.04em;text-shadow:0 0 8px currentColor;white-space:nowrap;pointer-events:none;}
.wsa-lbl-user{color:#00f0ff;top:14px;left:50%;transform:translateX(-50%);}
.wsa-lbl-kernel{color:#ff007f;top:12px;left:50%;transform:translateX(-50%);}
.wsa-lbl-hw{color:#fbbf24;position:static;}
.wsa-content{display:flex;flex-direction:column;gap:16px;flex-grow:1;}
.wsa-mode-card{padding:16px 20px;border-radius:10px;background:rgba(15,17,26,0.6);border:1px solid rgba(255,255,255,0.06);}
.kernel-card{border-left:4px solid #ff007f;}
.user-card{border-left:4px solid #00f0ff;}
.wsa-mode-title{font-size:0.95rem;font-weight:800;margin-bottom:6px;}
.wsa-mode-desc{font-size:0.85rem;color:#94a3b8;line-height:1.6;margin:0;}
</style>

<div class="wsa-wrap">
<div class="wsa-diagram-wrap">
<div class="wsa-r-user">
<span class="wsa-lbl wsa-lbl-user">User Mode</span>
<div class="wsa-r-kernel">
<span class="wsa-lbl wsa-lbl-kernel">Kernel Mode</span>
<div class="wsa-r-hardware">
<span class="wsa-lbl wsa-lbl-hw">Hardware</span>
</div>
</div>
</div>
</div>
<div class="wsa-content">
<div class="wsa-mode-card kernel-card">
<div class="wsa-mode-title" style="color:#ff007f;">🔴 Kernel Mode (โหมดเคอร์เนล)</div>
<p class="wsa-mode-desc">เป็นส่วนสิทธิ์ระบบระดับสูงที่มี <strong>การเข้าถึงฮาร์ดแวร์โดยตรงและไม่มีข้อจำกัด</strong> การประมวลผลคำสั่งเคอร์เนลทั้งหมดแชร์หน่วยความจำเสมือนเพียงพื้นที่เดียว หากมีข้อผิดพลาดระบบ Windows จะล่มลงในลักษณะจอฟ้า (BSOD) ทันทีเพื่อความปลอดภัยของข้อมูล</p>
</div>
<div class="wsa-mode-card user-card">
<div class="wsa-mode-title" style="color:#00f0ff;">🔵 User Mode (โหมดผู้ใช้)</div>
<p class="wsa-mode-desc">เป็นระดับสิทธิ์ใช้งานทั่วไปสำหรับแอปพลิเคชันของผู้ใช้ ระบบ Windows จะแบ่งสัดส่วนเนื้อที่การทำงานแยกขาดจากกัน (Isolated Process Space) หากโปรแกรมใดทำงานล้มเหลวหรือปิดตัวลง จะไม่กระทบต่อระบบปฏิบัติการหลักให้เสียหายตาม</p>
</div>
</div>
</div>'''}

    b4_accounts = {'type': 'markdown', 'value': '''### 👥 Windows User Accounts (ประเภทบัญชีผู้ใช้ในระบบ Windows)

ระบบปฏิบัติการ Windows สนับสนุนการจัดการบัญชีผู้ใช้งานหลักทั้งหมด 5 ประเภท เพื่อจัดสรรสิทธิ์และควบคุมระดับความปลอดภัยในลักษณะที่แตกต่างกัน:

<style>
.w-acc-grid{display:grid;grid-template-columns:repeat(auto-fit, minmax(180px, 1fr));gap:12px;margin:1.5rem 0;}
.w-acc-card{background:rgba(15,17,26,0.5);border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:16px;display:flex;flex-direction:column;gap:8px;}
.w-acc-hdr{display:flex;align-items:center;gap:8px;}
.w-acc-icon{font-size:1.4rem;}
.w-acc-title{font-size:0.85rem;font-weight:800;font-family:'JetBrains Mono',monospace;}
.w-acc-desc{font-size:0.8rem;color:#94a3b8;line-height:1.5;margin:0;}
.clr-admin{color:#ff007f;}.clr-std{color:#00f0ff;}.clr-work{color:#a855f7;}.clr-child{color:#fbbf24;}.clr-guest{color:#94a3b8;}
</style>

<div class="w-acc-grid">
<div class="w-acc-card">
<div class="w-acc-hdr"><span class="w-acc-icon">👑</span><span class="w-acc-title clr-admin">Administrator</span></div>
<p class="w-acc-desc">บัญชีผู้ดูแลระบบสูงสุด มีสิทธิ์สร้าง/ลบ บัญชีอื่น และแก้ไขทุกอย่างในเครื่องได้โดยไม่มีข้อจำกัด</p>
</div>
<div class="w-acc-card">
<div class="w-acc-hdr"><span class="w-acc-icon">⚙️</span><span class="w-acc-title clr-admin">SYSTEM</span></div>
<p class="w-acc-desc">บัญชีบริการระบบระดับสูงสุด มีสิทธิ์เหนือ Administrator ในการจัดการเคอร์เนลและไฟล์ระบบป้องกัน</p>
</div>
<div class="w-acc-card">
<div class="w-acc-hdr"><span class="w-acc-icon">👤</span><span class="w-acc-title clr-std">Standard User</span></div>
<p class="w-acc-desc">บัญชีผู้ใช้ทั่วไป ทำงานทั่วไปได้ แต่ไม่สามารถเปลี่ยนค่าระบบหลักหรือติดตั้งซอฟต์แวร์ที่กระทบเครื่องได้</p>
</div>
<div class="w-acc-card">
<div class="w-acc-hdr"><span class="w-acc-icon">🧸</span><span class="w-acc-title clr-child">Child Account</span></div>
<p class="w-acc-desc">บัญชีประเภท Standard พิเศษที่มีระบบควบคุมโดยผู้ปกครอง (Parental Controls) ดักกรองเนื้อหาไม่ปลอดภัย</p>
</div>
<div class="w-acc-card">
<div class="w-acc-hdr"><span class="w-acc-icon">👥</span><span class="w-acc-title clr-guest">Guest Account</span></div>
<p class="w-acc-desc">บัญชีสำหรับผู้ใช้ชั่วคราว มีสิทธิ์การใช้งานต่ำสุด ไม่มีรหัสผ่าน และไม่สามารถเซฟค่าการตั้งค่าใดๆ ได้ถาวร</p>
</div>
</div>'''}

    quiz_html_168 = {'type': 'markdown', 'value': '''<style>
.mini-quiz-card { background: rgba(12, 15, 29, 0.85); border: 1px solid rgba(0, 240, 255, 0.3); border-radius: 14px; padding: 28px; margin: 2.5rem 0; box-shadow: 0 0 30px rgba(0, 240, 255, 0.12); }
.mq-hdr { display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px; padding-bottom: 14px; border-bottom: 1px solid rgba(255, 255, 255, 0.08); }
.mq-item { background: rgba(15, 17, 26, 0.6); border: 1px solid rgba(255, 255, 255, 0.06); border-radius: 10px; padding: 18px; margin-bottom: 16px; }
.mq-title { font-weight: 700; color: #ffffff; font-size: 0.92rem; margin-bottom: 12px; }
.mq-opt-btn { width: 100%; text-align: left; background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); color: #cbd5e1; padding: 10px 14px; border-radius: 8px; font-size: 0.85rem; margin-bottom: 8px; transition: all 0.2s ease; cursor: pointer; }
.mq-opt-btn:hover { background: rgba(0, 240, 255, 0.1); border-color: #00f0ff; color: #ffffff; }
.mq-opt-btn.correct { background: rgba(34, 197, 94, 0.2) !important; border-color: #22c55e !important; color: #4ade80 !important; font-weight: bold; }
.mq-opt-btn.wrong { background: rgba(239, 68, 68, 0.2) !important; border-color: #ef4444 !important; color: #fca5a5 !important; }
</style>

<div class="mini-quiz-card">
  <div class="mq-hdr">
    <div style="font-weight: 800; color: #00f0ff; font-size: 1.1rem;"><i class="fas fa-tasks mr-2"></i> Lesson Quiz (แบบทดสอบท้ายบทเรียน 05)</div>
    <span class="badge" style="background: rgba(0,240,255,0.15); color: #00f0ff; border: 1px solid #00f0ff; padding: 4px 10px; border-radius: 20px;">4 QUESTIONS</span>
  </div>

  <div class="mq-item" data-q="1">
    <div class="mq-title">Q1. ในระบบบัญชีความปลอดภัยของ Windows บัญชีข้อใดที่เป็นบัญชีสิทธิ์มาตรฐาน (Standard) แต่มีขอบเขตปกป้องความปลอดภัยพิเศษเพิ่มเติม?</div>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 0, 'A')">A. Administrator Account</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 0, 'B')">B. Guest Account</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 0, 'C')">C. Child Account</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 0, 'D')">D. SYSTEM Account</button>
  </div>

  <div class="mq-item" data-q="2">
    <div class="mq-title">Q2. ในสิทธิ์เข้าใช้ข้อมูล NTFS Permissions หากกลุ่ม User ได้รับสิทธิ์อนุญาตเข้าถึง แต่บัญชีส่วนบุคคลติดสิทธิ์ปฏิเสธเด่นชัด (Explicit Deny) ผลจะเป็นอย่างไร?</div>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 1, 'A')">A. โดนปฏิเสธการเข้าถึงทันที (Explicit Deny มีผลครอบสิทธิ์อนุญาตเสมอ)</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 1, 'B')">B. เข้าถึงได้ปกติเพราะสิทธิ์ของกลุ่มมีค่าสูงกว่า</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 1, 'C')">C. ระบบจะสุ่มขอรหัสผ่าน Administrator อีกครั้ง</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 1, 'D')">D. สามารถอ่านไฟล์ได้แต่อ่านโฟลเดอร์ไม่ได้</button>
  </div>

  <div class="mq-item" data-q="3">
    <div class="mq-title">Q3. โครงสร้างระบบปฏิบัติการ Windows ส่วนใดที่ทำหน้าที่เป็นชั้นล่างสุดในการเชื่อมต่อและควบคุมฮาร์ดแวร์โดยตรง เพื่อให้ระบบระดับบนทำงานข้ามฮาร์ดแวร์ต่างรุ่นกันได้?</div>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 2, 'A')">A. User Mode Subsystems</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 2, 'B')">B. Hardware Abstraction Layer (HAL)</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 2, 'C')">C. Windows Registry Hives</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 2, 'D')">D. Command Prompt (cmd.exe)</button>
  </div>

  <div class="mq-item" data-q="4">
    <div class="mq-title">Q4. โฟลเดอร์ระบบโฟลเดอร์ใดใน Windows ที่ใช้จัดเก็บไฟล์ระบบ 32-bit บนระบบปฏิบัติการสถาปัตยกรรมแบบ 64-bit เพื่อให้แอปย้อนหลังทำงานได้?</div>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 3, 'A')">A. C:\\Windows\\System32</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 3, 'B')">B. C:\\Windows\\SysWOW64</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 3, 'C')">C. C:\\ProgramData</button>
    <button class="mq-opt-btn" onclick="handleMiniQuizOpt(this, 168, 3, 'D')">D. C:\\Users\\Public</button>
  </div>
</div>'''}

    card_168_p1 = {'type': 'markdown', 'value': '''<div style="border: 1px solid #00f0ff; background: rgba(8, 12, 25, 0.85); border-radius: 12px; padding: 24px 28px; margin-top: 2rem; margin-bottom: 1.5rem; box-shadow: 0 0 25px rgba(0, 240, 255, 0.15);">
  <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 12px;">
    <div style="font-size: 1.1rem; font-weight: 800; color: #ffffff; display: flex; align-items: center;">
      <span style="font-size: 1.4rem; margin-right: 10px;">🎯</span> เป้าหมายการทำแล็บ PART 1 - WINDOWS SYSTEM32 SECURITY AUDIT
    </div>
    <span class="badge" style="background: rgba(0, 240, 255, 0.18); color: #00f0ff; border: 1px solid #00f0ff; padding: 5px 14px; border-radius: 20px; font-size: 0.75rem; font-family: monospace; font-weight: 700;">PRIMARY LAB</span>
  </div>
  <p style="color: #cbd5e1; font-size: 0.9rem; margin-bottom: 16px; line-height: 1.6;">
    กดเปิดเซสชันคอนเทนเนอร์ Docker Instance Lab ด้านล่างเพื่อเข้าสู่ Windows Command Prompt (CMD) และใช้เซสชันนี้ในการทำแล็บย่อยทุกข้อในบทนี้ครับ!
  </p>
  <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 8px; padding: 14px 18px;">
    <div style="font-weight: 700; color: #38bdf8; font-size: 0.88rem; margin-bottom: 8px;">📌 ภารกิจปฏิบัติการ (MISSION DETAILS)</div>
    <ul style="margin: 0; padding-left: 20px; color: #cbd5e1; font-size: 0.85rem; line-height: 1.7;">
      <li>กดปุ่ม "Launch Lab Instance" ด้านล่างเพื่อเปิดการใช้งานคอนเทนเนอร์เซิร์ฟเวอร์หลัก</li>
      <li>พิมพ์คำสั่ง <code>cd C:\\Windows\\System32\\config</code> แล้วใช้ <code>type sec_flag.txt</code> อ่านเนื้อหาไฟล์ลับเพื่อนำ Flag มาตอบส่งในช่องด้านล่าง</li>
    </ul>
  </div>
</div>'''}

    card_168_p2 = {'type': 'markdown', 'value': '''<div style="border: 1px solid #a855f7; background: rgba(15, 11, 28, 0.85); border-radius: 12px; padding: 24px 28px; margin-top: 2rem; margin-bottom: 1.5rem; box-shadow: 0 0 25px rgba(168, 85, 247, 0.15);">
  <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 12px;">
    <div style="font-size: 1.1rem; font-weight: 800; color: #ffffff; display: flex; align-items: center;">
      <span style="font-size: 1.4rem; margin-right: 10px;">🎯</span> เป้าหมายการทำแล็บ PART 2 - WINDOWS TEXT FILTERING (FINDSTR)
    </div>
    <span class="badge" style="background: rgba(168, 85, 247, 0.18); color: #c084fc; border: 1px solid #a855f7; padding: 5px 14px; border-radius: 20px; font-size: 0.75rem; font-family: monospace; font-weight: 700;">SUBMISSION ONLY</span>
  </div>
  <p style="color: #cbd5e1; font-size: 0.9rem; margin-bottom: 16px; line-height: 1.6;">
    ใช้เซิร์ฟเวอร์จำลองเครื่องเดียวกับ Part 1 ในการกรองค้นหาบรรทัดที่มีข้อความ Flag ในไฟล์ Log ระบบขนาดใหญ่
  </p>
  <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 8px; padding: 14px 18px;">
    <div style="font-weight: 700; color: #c084fc; font-size: 0.88rem; margin-bottom: 8px;">📌 ภารกิจปฏิบัติการ (MISSION DETAILS)</div>
    <ul style="margin: 0; padding-left: 20px; color: #cbd5e1; font-size: 0.85rem; line-height: 1.7;">
      <li>สลับไปยังหน้าต่าง Terminal ของ Part 1 แล้วพิมพ์คำสั่ง <code>findstr "FLAG" C:\\ProgramData\\Microsoft\\Logs\\system_env.log</code></li>
      <li>นำ Flag ที่ได้ส่งคำตอบในช่องด้านล่าง <em>(ไม่ต้องกดเปิดเครื่องใหม่)</em></li>
    </ul>
  </div>
</div>'''}

    card_168_p3 = {'type': 'markdown', 'value': '''<div style="border: 1px solid #22c55e; background: rgba(8, 24, 18, 0.85); border-radius: 12px; padding: 24px 28px; margin-top: 2rem; margin-bottom: 1.5rem; box-shadow: 0 0 25px rgba(34, 197, 94, 0.15);">
  <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 12px;">
    <div style="font-size: 1.1rem; font-weight: 800; color: #ffffff; display: flex; align-items: center;">
      <span style="font-size: 1.4rem; margin-right: 10px;">🎯</span> เป้าหมายการทำแล็บ PART 3 - SYSTEM RESOURCES SEARCH
    </div>
    <span class="badge" style="background: rgba(34, 197, 94, 0.18); color: #4ade80; border: 1px solid #22c55e; padding: 5px 14px; border-radius: 20px; font-size: 0.75rem; font-family: monospace; font-weight: 700;">SUBMISSION ONLY</span>
  </div>
  <p style="color: #cbd5e1; font-size: 0.9rem; margin-bottom: 16px; line-height: 1.6;">
    ใช้เซิร์ฟเวอร์จำลองเครื่องเดียวกับ Part 1 ในการสำรวจโฟลเดอร์ทรัพยากรสถาปัตยกรรมระบบ
  </p>
  <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 8px; padding: 14px 18px;">
    <div style="font-weight: 700; color: #4ade80; font-size: 0.88rem; margin-bottom: 8px;">📌 ภารกิจปฏิบัติการ (MISSION DETAILS)</div>
    <ul style="margin: 0; padding-left: 20px; color: #cbd5e1; font-size: 0.85rem; line-height: 1.7;">
      <li>สลับไปยังหน้าต่าง Terminal ของ Part 1 แล้วพิมพ์คำสั่ง <code>type C:\\Windows\\SystemResources\\arch_flag.txt</code></li>
      <li>นำ Flag ที่ได้ส่งคำตอบในช่องด้านล่าง <em>(ไม่ต้องกดเปิดเครื่องใหม่)</em></li>
    </ul>
  </div>
</div>'''}

    lab_header_168 = {'type': 'markdown', 'value': '## 🛠️ WINDOWS SECURITY & ARCHITECTURE PRACTICE LABS (ห้องปฏิบัติการจำลองการใช้คำสั่ง WINDOWS)'}

    final_168 = [
        b0_header,
        b1_intro,
        b2_overview,
        b3_rings,
        {'type': 'markdown', 'value': b_layers_val},
        {'type': 'markdown', 'value': b_tree_val},
        b4_accounts,
        lab_header_168,
        card_168_p1,
        {'type': 'challenge', 'challenge_id': 46},
        card_168_p2,
        {'type': 'challenge', 'challenge_id': 47},
        card_168_p3,
        {'type': 'challenge', 'challenge_id': 48},
        quiz_html_168
    ]

    l168.content = json.dumps(final_168, ensure_ascii=False)
    db.session.commit()
    print("SUCCESSFULLY RESTORED ALL LECTURE UI COMPONENTS (LAYERS & DIRECTORY TREE STACK) AND QUIZ FOR LESSON 168!")
