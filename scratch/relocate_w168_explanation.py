import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l168 = db.session.query(TutorialLesson).filter_by(id=168).first()
blocks = json.loads(l168.content)

# ─── Replace Block 7 with Layout: Map on top, Explanation at the bottom (100% wide) ───
blocks[7]['value'] = """### ⚙️ Windows System Architecture Layers

คลิกหรือเลื่อนเมาส์ชี้ไปที่แต่ละกล่ององค์ประกอบในผังโครงสร้างสถาปัตยกรรม Windows เพื่อดูคำอธิบายและหน้าที่การทำงานของส่วนประกอบนั้นๆ ด้านล่าง:

<style>
.w-full-arch{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:20px;background:#0d0e15;border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:24px;box-shadow:0 8px 32px rgba(0,0,0,0.4);box-sizing:border-box;}
.w-arch-map{width:100%;display:flex;flex-direction:column;gap:8px;font-family:'JetBrains Mono',monospace;}
.w-mode-sec{border:1px solid;border-radius:8px;padding:14px;position:relative;display:flex;flex-direction:column;gap:8px;}
.w-mode-sec.user-mode{border-color:rgba(0,240,255,0.2);background:rgba(0,240,255,0.01);}
.w-mode-sec.kernel-mode{border-color:rgba(255,0,127,0.2);background:rgba(255,0,127,0.01);}
.w-mode-title-tag{font-size:0.7rem;font-weight:800;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:4px;}
.user-mode .w-mode-title-tag{color:#00f0ff;}
.kernel-mode .w-mode-title-tag{color:#ff007f;}
.w-row{display:flex;gap:8px;width:100%;}
.w-col{display:flex;flex-direction:column;gap:8px;}
.wnode{padding:10px 4px;border-radius:5px;border:1px solid rgba(255,255,255,0.08);background:rgba(255,255,255,0.03);text-align:center;font-size:0.75rem;font-weight:700;color:#94a3b8;cursor:pointer;transition:all 0.18s ease;user-select:none;display:flex;align-items:center;justify-content:center;min-height:36px;box-sizing:border-box;}
.wnode:hover, .wnode.active{color:#ffffff;transform:scale(1.015);box-shadow:0 0 12px rgba(255,255,255,0.1);background:rgba(255,255,255,0.08);}
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

/* Bottom Explanation Panel (100% wide) */
.w-arch-info{background:rgba(15,17,26,0.6);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:20px;display:flex;flex-direction:column;width:100%;box-sizing:border-box;}
.w-info-header{display:flex;align-items:center;gap:12px;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:10px;margin-bottom:12px;}
.w-info-badge{font-size:0.68rem;font-weight:800;padding:2px 8px;border-radius:4px;text-transform:uppercase;letter-spacing:0.05em;}
.w-info-badge.user{background:rgba(0,240,255,0.08);border:1px solid rgba(0,240,255,0.25);color:#00f0ff;}
.w-info-badge.kernel{background:rgba(255,0,127,0.08);border:1px solid rgba(255,0,127,0.25);color:#ff007f;}
.w-info-title{font-size:1.05rem;font-weight:700;color:#ffffff;margin:0;}
.w-info-body{font-size:0.88rem;color:#94a3b8;line-height:1.75;}
.w-info-body p{margin:0 0 8px;}
.w-info-body p:last-child{margin-bottom:0;}
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
<div class="wnode clr-subsys" style="width:110px;" onclick="showWInfo('subsys-srv', this)" onmouseover="showWInfo('subsys-srv', this)">Subsystem<br>servers</div>
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
<div class="w-col" style="flex:1.2;gap:6px;">
<div class="w-row" style="gap:6px;">
<div class="wnode clr-exec" style="flex:1;font-size:0.65rem;min-height:28px;padding:2px;" onclick="showWInfo('net-dev', this)" onmouseover="showWInfo('net-dev', this)">Net devices</div>
<div class="wnode clr-exec" style="flex:1;font-size:0.65rem;min-height:28px;padding:2px;" onclick="showWInfo('file-filt', this)" onmouseover="showWInfo('file-filt', this)">File filters</div>
</div>
<div class="w-row" style="gap:6px;">
<div class="wnode clr-exec" style="flex:1;font-size:0.65rem;min-height:28px;padding:2px;" onclick="showWInfo('net-prot', this)" onmouseover="showWInfo('net-prot', this)">Net protocols</div>
<div class="wnode clr-exec" style="flex:1;font-size:0.65rem;min-height:28px;padding:2px;" onclick="showWInfo('file-sys', this)" onmouseover="showWInfo('file-sys', this)">File systems</div>
</div>
<div class="w-row" style="gap:6px;">
<div class="wnode clr-exec" style="flex:1;font-size:0.65rem;min-height:28px;padding:2px;" onclick="showWInfo('net-intf', this)" onmouseover="showWInfo('net-intf', this)">Net interfaces</div>
<div class="wnode clr-exec" style="flex:1;font-size:0.65rem;min-height:28px;padding:2px;" onclick="showWInfo('vol-mgr', this)" onmouseover="showWInfo('vol-mgr', this)">Volume mgrs</div>
</div>
<div class="w-row">
<div class="wnode clr-exec" style="flex:1;font-size:0.68rem;min-height:28px;" onclick="showWInfo('dev-stack', this)" onmouseover="showWInfo('dev-stack', this)">Device stacks</div>
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
<h4 id="win-title" class="w-info-title">Applications (โปรแกรมประยุกต์)</h4>
</div>
<div id="win-desc" class="w-info-body">
<p>โปรแกรมประยุกต์ที่ผู้ใช้งานเรียกเปิดใช้ เช่น <strong>Chrome, Word, Discord</strong> หรือเครื่องมือรักษาความปลอดภัยต่างๆ</p>
<p>โปรแกรมในชั้นนี้ทำงานอยู่บนระดับวงแหวนสิทธิ์ Ring 3 เพื่อป้องกันไม่ให้ข้อผิดพลาดของโปรแกรมใดๆ ส่งผลกระทบต่อระบบปฏิบัติการหลัก หากแอปพลิเคชันปิดตัวหรือแครช จะไม่ทำให้ Windows ล่มตามไปด้วย</p>
</div>
</div>
</div>

<script>
const winArchData = {
  'apps': {
    title: 'Applications (โปรแกรมประยุกต์)',
    badge: 'User Mode',
    badgeClass: 'user',
    desc: '<p>โปรแกรมประยุกต์ที่ผู้ใช้งานเรียกเปิดใช้ เช่น <strong>Chrome, Word, Discord</strong> หรือเครื่องมือรักษาความปลอดภัยต่างๆ</p><p>โปรแกรมในชั้นนี้ทำงานอยู่บนระดับวงแหวนสิทธิ์ Ring 3 เพื่อป้องกันไม่ให้ข้อผิดพลาดของโปรแกรมใดๆ ส่งผลกระทบต่อระบบปฏิบัติการหลัก หากแอปพลิเคชันปิดตัวหรือแครช จะไม่ทำให้ Windows ล่มตามไปด้วย</p>'
  },
  'subsys-srv': {
    title: 'Subsystem Servers (เซิร์ฟเวอร์ระบบย่อย)',
    badge: 'User Mode',
    badgeClass: 'user',
    desc: '<p>กระบวนการทำงานเบื้องหลังระบบย่อย เช่น <strong>Win32 Subsystem (csrss.exe)</strong></p><p>ทำหน้าที่ควบคุมสภาพแวดล้อมเฉพาะตัวของ Windows เพื่อประสานงานการเปิดใช้งานหน้าต่าง UI การป้อนข้อมูลผ่านเมาส์/คีย์บอร์ด และจัดการควบคุมโปรแกรมให้ตอบสนองได้ตามมาตรฐาน API ของ Windows</p>'
  },
  'dlls': {
    title: 'DLLs (Dynamic Link Libraries)',
    badge: 'User Mode',
    badgeClass: 'user',
    desc: '<p>ไลบรารีแชร์ลิงก์ข้อมูล เช่น DLL ทั่วไปของโปรแกรมต่างๆ</p><p>เก็บชุดคำสั่งกลางที่เปิดให้โปรแกรมประยุกต์หลายๆ ตัวสามารถเรียกใช้งานร่วมกันได้ทันที ช่วยลดการซ้ำซ้อนของไฟล์และประหยัดพื้นที่หน่วยความจำหลัก (RAM)</p>'
  },
  'sys-srv': {
    title: 'System Services (บริการระบบส่วนหลัง)',
    badge: 'User Mode',
    badgeClass: 'user',
    desc: '<p>บริการระบบปฏิบัติการที่ทำงานอยู่ส่วนหลัง (Background Services)</p><p>ทำหน้าที่จัดการคิวงานทั่วไปในระบบ เช่น ระบบจัดการคิวเครื่องพิมพ์ (Print Spooler) บริการลงทะเบียนงาน และคอยสนับสนุนฟังก์ชันเสริมด้านความปลอดภัยของ Windows</p>'
  },
  'login-gina': {
    title: 'Login / GINA',
    badge: 'User Mode',
    badgeClass: 'user',
    desc: '<p>ส่วนประสานและจัดการล็อกอินเข้าสู่ระบบ (Graphical Identification and Authentication)</p><p>ทำหน้าที่ตรวจสอบความปลอดภัยตอนเริ่มต้นการบูตระบบและแสดงหน้าล็อกอิน รับรหัสผ่านหรือลายนิ้วมือเพื่อยืนยันสิทธิ์ของผู้ใช้ก่อนปล่อยสิทธิ์ให้เข้าถึงหน้า Desktop</p>'
  },
  'kernel32': {
    title: 'Kernel32.dll (Windows API Core)',
    badge: 'User Mode',
    badgeClass: 'user',
    desc: '<p>ไฟล์ไลบรารีระบบย่อยหลัก <code>kernel32.dll</code></p><p>ทำหน้าที่รับข้อกำหนด API จากโปรแกรมฝั่งผู้ใช้งานเพื่อนำไปควบคุมกระบวนการสร้าง Process, จัดการหน่วยความจำกายภาพเบื้องต้น และปูทางคำสั่งส่งต่อไปยัง <code>ntdll.dll</code></p>'
  },
  'crit-srv': {
    title: 'Critical Services (บริการระบบที่สำคัญมาก)',
    badge: 'User Mode',
    badgeClass: 'user',
    desc: '<p>บริการพื้นฐานของระบบที่จำเป็นต่อการรัน Windows เช่น <strong>lsass.exe (ตรวจความปลอดภัยบัญชี)</strong></p><p>หากบริการกลุ่มนี้หยุดทำงานลง ระบบปฏิบัติการ Windows จะไม่สามารถทำงานต่อไปได้และจะทำการปิดระบบปฏิบัติการทันทีเพื่อป้องกันความปลอดภัยของข้อมูล</p>'
  },
  'user32-gdi': {
    title: 'User32.dll / GDI32.dll',
    badge: 'User Mode',
    badgeClass: 'user',
    desc: '<p>ไลบรารี UI และงานกราฟิก <code>user32.dll</code> & <code>gdi32.dll</code></p><p>ทำหน้าที่แปลและส่งคำสั่งควบคุมการวาดหน้าต่าง ปุ่มกด เมนูคำสั่ง และฟังก์ชันกราฟิกรูปภาพเบื้องต้น ก่อนส่งต่อไปประมวลผลการแสดงผลบนจอภาพ</p>'
  },
  'ntdll': {
    title: 'ntdll.dll (ตัวเชื่อมระดับต่ำสุดของ User Mode)',
    badge: 'User Mode',
    badgeClass: 'user',
    desc: '<p>ไลบรารีรันไทม์ <code>ntdll.dll</code></p><p>เป็นด่านสุดท้ายก่อนคำสั่งจะออกจาก User Mode ทำหน้าที่รับ API มาแปลงเป็นรหัสคำสั่งภายในระบบย่อย <strong>(Native System Calls)</strong> เพื่อยิงข้ามกำแพงความปลอดภัยผ่าน Trap Interface เข้าไปที่ฝั่ง Kernel Mode</p>'
  },
  'trap': {
    title: 'Trap Interface / LPC (สวิตช์ส่งสายสิทธิ์การรัน)',
    badge: 'Kernel Mode',
    badgeClass: 'kernel',
    desc: '<p>ช่องทางประตูกั้นสิทธิ์ระหว่าง User และ Kernel (Trap / Local Procedure Call)</p><p>ทำหน้าที่รับสัญญาณขอเข้าถึงฮาร์ดแวร์เพื่อสลับระดับสิทธิ์การทำงานของ CPU จาก Ring 3 (User) ไปเป็น Ring 0 (Kernel) อย่างปลอดภัย พร้อมรองรับการประมวลผลคำสั่งข้าม Process ระหว่างกัน</p>'
  },
  'sec-ref': {
    title: 'Security Reference Monitor (SRM)',
    badge: 'Kernel Mode',
    badgeClass: 'kernel',
    desc: '<p>ระบบตรวจสอบและยืนยันสิทธิ์ความปลอดภัยสูงสุดของระบบไฟล์</p><p>คอยบังคับใช้นโยบายความปลอดภัยและสิทธิ์การเข้าถึง (Access Control Lists - ACLs) ตรวจสอบว่าผู้ใช้คนนี้มีสิทธิ์เปิด อ่าน หรือแก้ไขไฟล์นี้จริงๆ หรือไม่</p>'
  },
  'io-mgr': {
    title: 'I/O Manager (ผู้จัดการ Input/Output)',
    badge: 'Kernel Mode',
    badgeClass: 'kernel',
    desc: '<p>ระบบจัดการคำสั่งรับส่งข้อมูลกับอุปกรณ์ภายนอกทั้งหมด</p><p>ทำหน้าที่แปลคำสั่งอ่าน/เขียนทั่วไปให้กลายเป็นชุดคำสั่งไดรเวอร์ (I/O Request Packets) เพื่อนำไปสั่งงานฮาร์ดแวร์โดยตรงแบบเป็นลำดับคิว</p>'
  },
  'mem-mgr': {
    title: 'Memory Manager (ผู้จัดการหน่วยความจำ)',
    badge: 'Kernel Mode',
    badgeClass: 'kernel',
    desc: '<p>ระบบควบคุมการจัดสรรแรมและหน่วยความจำเสมือน (Virtual Memory)</p><p>คอยจัดการพื้นที่หน่วยความจำของทุกแอปพลิเคชันอย่างเข้มงวด ป้องกันไม่ให้แอปพลิเคชันใดรันเขียนทับพื้นที่ของผู้อื่น และสลับข้อมูลที่ไม่ได้ใช้ไปพักในฮาร์ดดิสก์ (Paging)</p>'
  },
  'proc-thread': {
    title: 'Process & Thread Manager',
    badge: 'Kernel Mode',
    badgeClass: 'kernel',
    desc: '<p>ตัวควบคุมโครงสร้าง Process และการกระจายงาน CPU</p><p>ทำหน้าที่สร้างและยกเลิก Process คอยตรวจจับการประมวลผลระดับย่อย (Threads) เพื่อนำไปส่งคิวให้แก่ CPU เพื่อให้คอมพิวเตอร์ทำงานแบบ Multi-tasking ได้เสถียร</p>'
  },
  'win32-gui': {
    title: 'Win32 GUI Driver (win32k.sys)',
    badge: 'Kernel Mode',
    badgeClass: 'kernel',
    desc: '<p>ไดรเวอร์ประมวลผลกราฟิกและหน้าต่างฝั่งเคอร์เนล</p><p>ย้ายโค้ดบางส่วนของการประมวลผลกราฟิกและ UI จากฝั่ง User Mode เข้ามาทำใน Kernel Mode เพื่อประหยัดเวลารับส่งสัญญาณ ทำให้วาดหน้าต่างและแสดงผลบนจอภาพได้เร็วขึ้นมาก</p>'
  },
  'net-dev': {
    title: 'Network Devices (อุปกรณ์เครือข่าย)',
    badge: 'Kernel Mode',
    badgeClass: 'kernel',
    desc: '<p>ไดรเวอร์ระดับล่างสำหรับสั่งงานการ์ดแลน (NIC) หรือชิป Wi-Fi โดยตรง</p>'
  },
  'file-filt': {
    title: 'File Filters (ตัวกรองไฟล์ระบบ)',
    badge: 'Kernel Mode',
    badgeClass: 'kernel',
    desc: '<p>โปรแกรมฟิลเตอร์ความปลอดภัย เช่น แอนตี้ไวรัส คอยดักจับและแสกนไฟล์ก่อนที่ I/O Manager จะส่งสิทธิ์ให้อ่านเขียนไฟล์จริง</p>'
  },
  'net-prot': {
    title: 'Network Protocols',
    badge: 'Kernel Mode',
    badgeClass: 'kernel',
    desc: '<p>โปรโตคอลระบบการสื่อสารเครือข่าย (เช่น TCP/IP, UDP) ระดับเคอร์เนล เพื่อให้รับส่งข้อมูลทางเครือข่ายได้อย่างรวดเร็วและไม่มีข้อมูลตกหล่น</p>'
  },
  'file-sys': {
    title: 'File Systems (ระบบไฟล์)',
    badge: 'Kernel Mode',
    badgeClass: 'kernel',
    desc: '<p>ไดรเวอร์ระบบไฟล์ เช่น NTFS, FAT32 เพื่อแปลตำแหน่งที่อยู่ข้อมูลทางดิจิทัลให้สัมพันธ์กับเนื้อที่จริงของจานหมุนดิสก์หรือ SSD</p>'
  },
  'net-intf': {
    title: 'Network Interfaces',
    badge: 'Kernel Mode',
    badgeClass: 'kernel',
    desc: '<p>อินเตอร์เฟซสื่อกลางรับข้อมูลจากเครือข่ายเข้ามาสั่งงานบริการรับส่งข้อมูลในเคอร์เนล</p>'
  },
  'vol-mgr': {
    title: 'Volume Managers',
    badge: 'Kernel Mode',
    badgeClass: 'kernel',
    desc: '<p>ตัวควบคุมพาธและพาร์ติชันไดรฟ์ (เช่น แบ่งเนื้อที่เป็น C:, D: หรือผูกฮาร์ดดิสก์สองลูกเข้าด้วยกัน)</p>'
  },
  'dev-stack': {
    title: 'Device Stacks',
    badge: 'Kernel Mode',
    badgeClass: 'kernel',
    desc: '<p>สแต็กอุปกรณ์ที่ผูกความเกี่ยวโยงของไดรเวอร์ระดับบนลงสู่ไดรเวอร์ควบคุมพอร์ตและฮาร์ดแวร์ตัวล่างสุด</p>'
  },
  'filesys-rt': {
    title: 'File System Run-time',
    badge: 'Kernel Mode',
    badgeClass: 'kernel',
    desc: '<p>ตัวควบคุมสภาพแวดล้อมการทำงานของระบบไฟล์แบบเรียลไทม์ คอยประสานความปลอดภัยและตรวจสอบความสมบูรณ์ของพอยน์เตอร์ข้อมูล</p>'
  },
  'cache-mgr': {
    title: 'Cache Manager',
    badge: 'Kernel Mode',
    badgeClass: 'kernel',
    desc: '<p>ผู้จัดการพื้นที่แคชความเร็วสูง คอยดึงไฟล์ที่ใช้งานบ่อยเก็บไว้ในแรมล่วงหน้า เพื่อให้โปรแกรมเรียกใช้ซ้ำได้ทันทีโดยไม่ต้องรออ่านดิสก์ใหม่</p>'
  },
  'scheduler': {
    title: 'Scheduler (ตัวจัดคิวงานระบบ)',
    badge: 'Kernel Mode',
    badgeClass: 'kernel',
    desc: '<p>คอยพิจารณาจัดลำดับความสำคัญของแต่ละ Thread ในการเข้าใช้งาน CPU เพื่อไม่ให้เกิดภาวะระบบชะงัก (Deadlock) และทำให้งานเร่งด่วนประมวลผลก่อน</p>'
  },
  'sync': {
    title: 'Synchronization',
    badge: 'Kernel Mode',
    badgeClass: 'kernel',
    desc: '<p>ระบบการประสานเวลา ป้องกันปัญหากรณี Threads 2 ตัวพยายามเขียนทับหน่วยความจำตำแหน่งเดียวกันในเวลาเดียวกัน (Race Condition)</p>'
  },
  'obj-mgr': {
    title: 'Object Manager / Registry (ผู้ดูแลอ็อบเจกต์และเรจิสทรี)',
    badge: 'Kernel Mode',
    badgeClass: 'kernel',
    desc: '<p>ทำหน้าที่สร้าง ตรวจจับ และทำลายอ็อบเจกต์ทรัพยากรหลักของระบบปฏิบัติการ เช่น Process handles และจัดการดึงค่า/จัดเก็บค่าสำคัญในไฟล์ <strong>Windows Registry</strong> ที่รันบริการกลางของเครื่อง</p>'
  },
  'hal': {
    title: 'Hardware Abstraction Layer (HAL)',
    badge: 'Kernel Mode',
    badgeClass: 'kernel',
    desc: '<p>ชั้นอินเตอร์เฟซพิเศษที่คอยสั่งการฮาร์ดแวร์และแผงชิปเซ็ตประมวลผลหลักโดยตรง</p><p>ทำหน้าที่แปลและตัดปัญหาความต่างในสถาปัตยกรรมชิปเซ็ตของยี่ห้อบอร์ดแต่ละค่ายออกไป เพื่อให้ตัวเคอร์เนลหลักเขียนชุดคำสั่งควบคุมที่เป็นแบบเดียวกันรันได้ทุกบอร์ด</p>'
  }
};

function showWInfo(key, element) {
const nodes = document.querySelectorAll('.wnode');
nodes.forEach(n => n.classList.remove('active'));
element.classList.add('active');
const data = winArchData[key];
if (!data) return;
const badge = document.getElementById('win-badge');
const title = document.getElementById('win-title');
const desc = document.getElementById('win-desc');
badge.textContent = data.badge;
badge.className = 'w-info-badge ' + data.badgeClass;
title.textContent = data.title;
desc.innerHTML = data.desc;
}
</script>"""

l168.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=168).update({"content": l168.content})
db.session.commit()
print("Block 7 updated: Map on top, Explanation card full width at the bottom!")
