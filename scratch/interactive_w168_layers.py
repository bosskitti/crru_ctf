import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l168 = db.session.query(TutorialLesson).filter_by(id=168).first()
blocks = json.loads(l168.content)

# ─── Replace Block 7 (System Architecture Layers) with Interactive Hover Layout ───
blocks[7]['value'] = """### ⚙️ Windows System Architecture Layers

สถาปัตยกรรมของระบบปฏิบัติการ Windows แบ่งระดับสิทธิ์การทำงานอย่างเข้มงวดระหว่าง **User Mode (Ring 3)** และ **Kernel Mode (Ring 0)** เลื่อนเมาส์ชี้ไปที่แต่ละชั้นเพื่อดูหน้าที่การทำงานและคำอธิบายโดยละเอียด:

<style>
.w-arch-grid{margin:2.5rem auto;display:flex;flex-direction:column;align-items:center;width:100%;max-width:1050px;background:rgba(15,17,26,0.4);border:1px solid rgba(255,255,255,0.05);border-radius:12px;padding:24px;box-shadow:inset 0 0 20px rgba(0,0,0,0.3);}
.w-arch-container{display:flex;flex-direction:column;align-items:center;width:100%;}
.w-arch-row{display:flex;align-items:center;width:100%;position:relative;transition:all 0.2s ease;cursor:pointer;padding:4px 0;}
.w-arch-card-wrap{min-width:220px;display:flex;justify-content:center;}
.w-arch-card{width:200px;padding:12px 16px;border-radius:8px;text-align:center;font-weight:700;font-size:0.92rem;box-shadow:0 4px 15px rgba(0, 0, 0, 0.2);transition:all 0.25s ease;font-family:'JetBrains Mono',monospace;}

/* Custom Layer Colors */
.w-layer-apps{border:1px solid #3ddc84;background:rgba(61,220,132,0.05);color:#3ddc84;}
.w-layer-dlls{border:1px solid #00f0ff;background:rgba(0,240,255,0.05);color:#00f0ff;}
.w-layer-ntdll{border:1px solid #fbbf24;background:rgba(251,191,36,0.05);color:#fbbf24;}
.w-layer-exec{border:1px solid #ab20fd;background:rgba(171,32,253,0.05);color:#ab20fd;}
.w-layer-hal{border:1px solid #ff007f;background:rgba(255,0,127,0.05);color:#ff007f;}

.w-arch-leader{flex:1;height:1px;border-bottom:1px dashed rgba(255,255,255,0.12);margin:0 20px;min-width:20px;transition:border-color 0.2s ease;}
.w-arch-desc{width:55%;font-size:0.88rem;color:#94a3b8;line-height:1.6;transition:all 0.2s ease;text-align:left;}
.w-arch-desc span.highlight{font-weight:700;transition:all 0.2s ease;}

/* Hover Effects */
.w-arch-row:hover .w-arch-card{transform:scale(1.04);color:#ffffff;}
.w-arch-row:hover .w-arch-card.w-layer-apps{border-color:#3ddc84;box-shadow:0 0 15px rgba(61,220,132,0.35);background:rgba(61,220,132,0.15);}
.w-arch-row:hover .w-arch-card.w-layer-dlls{border-color:#00f0ff;box-shadow:0 0 15px rgba(0,240,255,0.35);background:rgba(0,240,255,0.15);}
.w-arch-row:hover .w-arch-card.w-layer-ntdll{border-color:#fbbf24;box-shadow:0 0 15px rgba(251,191,36,0.35);background:rgba(251,191,36,0.15);}
.w-arch-row:hover .w-arch-card.w-layer-exec{border-color:#ab20fd;box-shadow:0 0 15px rgba(171,32,253,0.35);background:rgba(171,32,253,0.15);}
.w-arch-row:hover .w-arch-card.w-layer-hal{border-color:#ff007f;box-shadow:0 0 15px rgba(255,0,127,0.35);background:rgba(255,0,127,0.15);}

.w-arch-row:hover .w-arch-leader{border-bottom-color:rgba(255,255,255,0.4);border-bottom-style:solid;}
.w-arch-row:hover .w-arch-desc{color:#ffffff;text-shadow:0 0 8px rgba(255,255,255,0.2);}

/* Custom Highlight colors based on layer */
.w-arch-row.r-apps:hover .w-arch-desc span.highlight{color:#3ddc84;text-shadow:0 0 10px rgba(61,220,132,0.5);}
.w-arch-row.r-dlls:hover .w-arch-desc span.highlight{color:#00f0ff;text-shadow:0 0 10px rgba(0,240,255,0.5);}
.w-arch-row.r-ntdll:hover .w-arch-desc span.highlight{color:#fbbf24;text-shadow:0 0 10px rgba(251,191,36,0.5);}
.w-arch-row.r-exec:hover .w-arch-desc span.highlight{color:#ab20fd;text-shadow:0 0 10px rgba(171,32,253,0.5);}
.w-arch-row.r-hal:hover .w-arch-desc span.highlight{color:#ff007f;text-shadow:0 0 10px rgba(255,0,127,0.5);}

.w-arch-spine{width:2px;height:12px;background:rgba(255,255,255,0.15);margin-right:auto;margin-left:119px;}
.w-mode-label{width:100%;max-width:1050px;font-size:0.72rem;font-weight:800;color:#64748b;text-transform:uppercase;letter-spacing:0.1em;padding:4px 0;margin-top:12px;border-bottom:1px solid rgba(255,255,255,0.05);text-align:left;}
</style>

<div class="w-arch-grid">
<div class="w-arch-container">

<div class="w-mode-label">User Mode (Ring 3) - สิทธิ์ผู้ใช้งานทั่วไป</div>

<!-- Row 1: Apps -->
<div class="w-arch-row r-apps">
<div class="w-arch-card-wrap"><div class="w-arch-card w-layer-apps">Applications</div></div>
<div class="w-arch-leader"></div>
<div class="w-arch-desc"><span class="highlight">User Applications</span> — โปรแกรมระดับบนสุดที่ผู้ใช้งานเรียกเปิดรัน เช่น Chrome, MS Word, หรือ Tools ต่างๆ โดยทำงานภายในพื้นที่หน่วยความจำจำลองของตัวเอง (Virtual Address Space) ไม่มีสิทธิ์แทรกแซงโค้ดอื่น</div>
</div>

<!-- Connector -->
<div class="w-arch-spine"></div>

<!-- Row 2: Subsystem DLLs -->
<div class="w-arch-row r-dlls">
<div class="w-arch-card-wrap"><div class="w-arch-card w-layer-dlls">Subsystem DLLs</div></div>
<div class="w-arch-leader"></div>
<div class="w-arch-desc"><span class="highlight">Subsystem API DLLs</span> — ไฟล์ไลบรารีส่วนเชื่อมต่อ เช่น <code>kernel32.dll</code>, <code>user32.dll</code>, <code>gdi32.dll</code> ที่ทำหน้าที่แปลคำสั่งจากโปรแกรมใช้งาน (เช่น ขอเปิดหน้าต่างหรือเขียนไฟล์) ให้อยู่ในรูปคำสั่ง API พื้นฐานของ Windows</div>
</div>

<!-- Connector -->
<div class="w-arch-spine"></div>

<!-- Row 3: ntdll.dll -->
<div class="w-arch-row r-ntdll">
<div class="w-arch-card-wrap"><div class="w-arch-card w-layer-ntdll">ntdll.dll</div></div>
<div class="w-arch-leader"></div>
<div class="w-arch-desc"><span class="highlight">Gateway to Kernel (ntdll)</span> — ไลบรารีตัวกลางระดับต่ำสุดของ User Mode ทำหน้าที่เป็นประตูผ่านคำสั่ง โดยแปลงระบบ API ให้เป็น <code>System Calls</code> แล้วส่งผ่านช่องทาง (Trap Interface) เพื่อข้ามเข้าไปประมวลผลต่อในฝั่ง Kernel Mode</div>
</div>

<div class="w-mode-label">Kernel Mode (Ring 0) - สิทธิ์ควบคุมสูงสุดระดับระบบ</div>

<!-- Connector -->
<div class="w-arch-spine"></div>

<!-- Row 4: Executive Services -->
<div class="w-arch-row r-exec">
<div class="w-arch-card-wrap"><div class="w-arch-card w-layer-exec">Executive Services</div></div>
<div class="w-arch-leader"></div>
<div class="w-arch-desc"><span class="highlight">Executive & Kernel Services</span> — กลุ่มบริการจัดสรรทรัพยากรหลักของระบบปฏิบัติการ เช่น <strong>I/O Manager</strong> (จัดการการอ่านเขียน), <strong>Memory Manager</strong> (ควบคุม RAM), <strong>Security Monitor</strong> (ตรวจสอบสิทธิ์ไฟล์) และ Scheduler</div>
</div>

<!-- Connector -->
<div class="w-arch-spine"></div>

<!-- Row 5: HAL -->
<div class="w-arch-row r-hal">
<div class="w-arch-card-wrap"><div class="w-arch-card w-layer-hal">HAL & Hardware</div></div>
<div class="w-arch-leader"></div>
<div class="w-arch-desc"><span class="highlight">Hardware Abstraction Layer (HAL)</span> — เลเยอร์ล่างสุดที่ทำหน้าที่แปลคำสั่งเคอร์เนลให้เข้ากับประเภทและชิปเซ็ตประมวลผลของเมนบอร์ดและ CPU โดยตรง ช่วยให้นักพัฒนาไม่ต้องกังวลเรื่องรุ่นของเมนบอร์ดแต่ละยี่ห้อ</div>
</div>

</div>
</div>"""

l168.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=168).update({"content": l168.content})
db.session.commit()
print("Interactive Windows Architecture Layers updated successfully!")
