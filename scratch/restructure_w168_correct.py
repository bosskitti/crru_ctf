import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l168 = db.session.query(TutorialLesson).filter_by(id=168).first()
b168 = json.loads(l168.content)

# ─── Find specific blocks from Lesson 168 ───
b_header = b168[0]
b_intro_w = b168[3] # Overviews of Windows
b_rings = b168[5] # Rings
b_layers = b168[7] # Interactive layers
b_tree = b168[9] # Tree
b_drives = b168[11] # Drives
b_paths = b168[13] # Path rules
b_folders = b168[15] # Folders table

# ─── New Visual Block for Windows User Accounts ───
b_accounts = {
    "type": "markdown",
    "value": """### 👥 Windows User Accounts

ระบบปฏิบัติการ Windows สนับสนุนการจัดการบัญชีผู้ใช้งานหลักทั้งหมด 5 ประเภท เพื่อจัดสรรสิทธิ์และควบคุมระดับความปลอดภัยในลักษณะที่แตกต่างกัน:

<style>
.w-acc-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.w-acc-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;}
@media(max-width:960px){.w-acc-grid{grid-template-columns:repeat(3,1fr);}}
@media(max-width:680px){.w-acc-grid{grid-template-columns:repeat(2,1fr);}}
@media(max-width:440px){.w-acc-grid{grid-template-columns:1fr;}}
.w-acc-card{background:rgba(15,17,26,0.5);border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:16px;transition:all 0.2s ease;display:flex;flex-direction:column;gap:8px;box-sizing:border-box;}
.w-acc-card:hover{border-color:rgba(0,240,255,0.25);transform:translateY(-2px);box-shadow:0 6px 20px rgba(0,0,0,0.3);}
.w-acc-hdr{display:flex;align-items:center;gap:8px;}
.w-acc-icon{font-size:1.4rem;}
.w-acc-title{font-size:0.85rem;font-weight:800;font-family:'JetBrains Mono',monospace;}
.w-acc-desc{font-size:0.8rem;color:#94a3b8;line-height:1.5;margin:0;}
.clr-admin{color:#ff007f;}.clr-std{color:#00f0ff;}.clr-work{color:#ab20fd;}.clr-child{color:#fbbf24;}.clr-guest{color:#94a3b8;}
.w-acc-card.admin{border-color:rgba(255,0,127,0.15);background:rgba(255,0,127,0.015);}
.w-acc-card.admin:hover{border-color:#ff007f;}
</style>

<div class="w-acc-wrap">
<div class="w-acc-grid">
<!-- Admin -->
<div class="w-acc-card admin">
<div class="w-acc-hdr">
<span class="w-acc-icon">👑</span>
<span class="w-acc-title clr-admin">Admin</span>
</div>
<p class="w-acc-desc">บัญชีผู้ดูแลระบบสูงสุด มีสิทธิ์สร้าง/ลบ บัญชีอื่น และแก้ไขทุกอย่างในเครื่องได้โดยไม่มีข้อจำกัด</p>
</div>
<!-- Standard -->
<div class="w-acc-card">
<div class="w-acc-hdr">
<span class="w-acc-icon">👤</span>
<span class="w-acc-title clr-std">Standard</span>
</div>
<p class="w-acc-desc">บัญชีผู้ใช้ทั่วไป ทำงานทั่วไปได้ แต่ไม่สามารถเปลี่ยนค่าระบบหลักหรือติดตั้งซอฟต์แวร์ที่กระทบเครื่องได้</p>
</div>
<!-- Work or School -->
<div class="w-acc-card">
<div class="w-acc-hdr">
<span class="w-acc-icon">🏫</span>
<span class="w-acc-title clr-work">Work/School</span>
</div>
<p class="w-acc-desc">บัญชีที่สร้างและควบคุมโดยองค์กรหรือสถานศึกษา เพื่อควบคุมนโยบายความปลอดภัยและทรัพยากรส่วนกลาง</p>
</div>
<!-- Child -->
<div class="w-acc-card">
<div class="w-acc-hdr">
<span class="w-acc-icon">🧸</span>
<span class="w-acc-title clr-child">Child</span>
</div>
<p class="w-acc-desc">บัญชีประเภท Standard พิเศษที่มีระบบควบคุมโดยผู้ปกครอง (Parental Controls) ดักกรองเนื้อหาไม่ปลอดภัย</p>
</div>
<!-- Guest -->
<div class="w-acc-card">
<div class="w-acc-hdr">
<span class="w-acc-icon">👥</span>
<span class="w-acc-title clr-guest">Guest</span>
</div>
<p class="w-acc-desc">บัญชีสำหรับผู้ใช้ชั่วคราว มีสิทธิ์การใช้งานต่ำสุด ไม่มีรหัสผ่าน และไม่สามารถเซฟค่าการตั้งค่าใดๆ ได้ถาวร</p>
</div>
</div>
</div>"""
}

# ─── Permissions & Comparison blocks ───
b_permissions = b168[25]
b_compare = b168[30]

# ─── Q&A Accordion of Lesson 168 ───
b_qa_168 = {
    "type": "markdown",
    "value": """### ❓ Questions & Answers (Q&A)

ไขข้อสงสัยเบื้องต้นเกี่ยวกับการเรียนรู้โครงสร้างระบบสิทธิ์และความปลอดภัยของ Windows:

<style>
.qa-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:12px;}
.qa-item{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:10px;overflow:hidden;transition:all 0.25s ease;}
.qa-item:hover{border-color:rgba(0,240,255,0.25);background:rgba(0,240,255,0.01);box-shadow:0 4px 15px rgba(0,0,0,0.3);}
.qa-q{padding:16px 20px;font-size:0.92rem;font-weight:700;color:#e2e8f0;cursor:pointer;display:flex;justify-content:between;align-items:center;user-select:none;}
.qa-q::after{content:"▼";font-size:0.65rem;color:#64748b;margin-left:auto;transition:transform 0.2s ease;}
.qa-item.active .qa-q::after{transform:rotate(180deg);color:#00f0ff;}
.qa-a{max-height:0;overflow:hidden;padding:0 20px;font-size:0.86rem;color:#94a3b8;line-height:1.7;transition:all 0.25s ease-out;background:rgba(0,0,0,0.15);}
.qa-item.active .qa-a{max-height:300px;padding:16px 20px;border-top:1px solid rgba(255,255,255,0.03);}
.qa-item.active .qa-q{color:#00f0ff;}
</style>

<div class="qa-wrap">

<div class="qa-item active">
<div class="qa-q" onclick="toggleQA(this)">1. โครงสร้าง System Directories ใน Windows มีผลต่อความปลอดภัยข้อมูลอย่างไร?</div>
<div class="qa-a">
การจัดโครงสร้างแบบมีสัญญลักษณ์จำเพาะ (เช่น <code>\\Windows\\System32</code> หรือ <code>\\ProgramData</code>) ช่วยให้ระบบความปลอดภัย NTFS กำหนดนโยบายและกรองสิทธิ์ผู้ใช้งานแยกส่วนได้ชัดเจน ไฟล์ระบบที่สำคัญจะถูกคุ้มครองด้วยสิทธิ์ระดับ SYSTEM หรือ Administrator เพื่อไม่ให้มัลแวร์ทั่วไปเข้าถึงและสร้างความเสียหายแก่ระบบได้ง่าย
</div>
</div>

<div class="qa-item">
<div class="qa-q" onclick="toggleQA(this)">2. การปฏิเสธสิทธิ์ด้วย 'icacls /deny' มีผลต่างจากการยกเลิกการอนุญาตปกติอย่างไร?</div>
<div class="qa-a">
ในระบบความปลอดภัย Windows NTFS Permissions กฎการปฏิเสธสิทธิ์ (Explicit Deny) จะมีผล **สำคัญที่สุด (Override)** เสมอ หมายความว่า แม้กลุ่มผู้ใช้งานของ User นั้นจะได้รับสิทธิ์ <code>Full Control</code> ผ่านระบบ <code>/grant</code> แต่หากตัวบัญชีผู้ใช้งานส่วนตัวถูกระบุในรายการ <code>/deny</code> แม้เพียงสิทธิ์เดียว ระบบความปลอดภัยจะบล็อกและห้าม User คนนั้นเข้าถึงทรัพยากรทันที
</div>
</div>

<div class="qa-item">
<div class="qa-q" onclick="toggleQA(this)">3. โโฟลเดอร์ SysWOW64 มีหน้าที่อย่างไรบนระบบปฏิบัติการแบบ 64-bit?</div>
<div class="qa-a">
ชื่อของ SysWOW64 ย่อมาจาก "Windows 32-bit on Windows 64-bit" ทำหน้าที่เก็บไฟล์ไลบรารีระบบ (DLLs) ขนาด 32-bit เพื่อช่วยให้ระบบปฏิบัติการ Windows แบบ 64-bit สามารถเรียกเปิดรันแอปพลิเคชัน 32-bit ย้อนหลังได้โดยไม่เกิดข้อผิดพลาดในการประมวลผลคำสั่ง API
</div>
</div>

</div>

<script>
function toggleQA(element) {
    const item = element.parentElement;
    item.classList.toggle("active");
}
</script>"""
}

# ─── Assemble New Lesson 168 Content ───
new_b168 = [
    {
        "type": "markdown",
        "value": "## 🛡️ โครงสร้างระบบและการจัดการสิทธิ์ใน Windows (Windows Architecture & Permissions)"
    },
    b_intro_w,
    {"type": "markdown", "value": "---"},
    b_rings,
    {"type": "markdown", "value": "---"},
    b_layers,
    {"type": "markdown", "value": "---"},
    b_tree,
    {"type": "markdown", "value": "---"},
    b_drives,
    {"type": "markdown", "value": "---"},
    b_paths,
    {"type": "markdown", "value": "---"},
    b_folders,
    {"type": "markdown", "value": "---"},
    b_accounts,
    {"type": "markdown", "value": "---"},
    b_permissions,
    {"type": "markdown", "value": "---"},
    b_compare,
    {"type": "markdown", "value": "---"},
    b_qa_168
]

l168.title = "05. โครงสร้างระบบและการจัดการสิทธิ์ใน Windows (Windows Architecture & Permissions)"
l168.content = json.dumps(new_b168, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=168).update({
    "title": l168.title,
    "content": l168.content
})
db.session.commit()

print(f"Lesson 168 title updated and content blocks restructured to 23 blocks successfully!")
