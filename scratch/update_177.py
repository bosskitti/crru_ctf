import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

def save_lesson(lid, val0, val1, val2):
    l = db.session.query(TutorialLesson).filter_by(id=lid).first()
    blocks = [
        {"type": "markdown", "value": val0},
        {"type": "markdown", "value": val1},
        {"type": "markdown", "value": val2}
    ]
    l.content = json.dumps(blocks, ensure_ascii=False)
    db.session.query(TutorialLesson).filter_by(id=lid).update({"content": l.content})
    db.session.commit()
    print(f"Lesson {lid} successfully upgraded!")

val177_0 = """<div style="text-align: center; margin-bottom: 2rem; padding: 24px; background: linear-gradient(135deg, rgba(6,182,212,0.15) 0%, rgba(59,130,246,0.15) 100%); border: 1px solid rgba(6,182,212,0.3); border-radius: 16px; box-shadow: 0 0 20px rgba(6,182,212,0.15);">
<h2 style="margin: 0; font-size: 1.9rem; font-weight: 800; color: #ffffff; text-shadow: 0 0 12px rgba(6,182,212,0.6); letter-spacing: 0.03em;">🌐 Web Application Security & OWASP</h2>
<p style="margin: 8px 0 0 0; font-size: 0.92rem; color: #94a3b8; font-weight: 500;">ทำความเข้าใจเชิงความมั่นคงปลอดภัยบนเว็บแอปพลิเคชันและมาตรฐานความเสี่ยงระดับสากล</p>
</div>

### 🔍 ภาพรวมวิทยาการการโจมตีเว็บ (Web Exploitation Overviews)
การโจมตีแอปพลิเคชันเว็บมีเป้าหมายเพื่อแทรกแซง หาจุดอ่อนในระบบปฏิบัติการ ซอฟต์แวร์ หรือการคอนฟิกเพื่อเข้ายึดครองสิทธิ์:

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 1.5rem auto;">
<div style="background: linear-gradient(to bottom right, rgba(255,255,255,0.03), rgba(255,255,255,0.01)); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 18px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
<strong style="color: #00f0ff; font-size: 0.98rem; display: flex; align-items: center; gap: 8px; margin-bottom: 10px; text-shadow: 0 0 8px rgba(0,240,255,0.3);">🔓 Access Control</strong>
<span style="color: #cbd5e1; font-size: 0.82rem; line-height: 1.6;">การลอบเข้าสู่แผงควบคุมระบบโดยข้ามขั้นตอนการตรวจสิทธิ์ ทำให้แฮกเกอร์จัดการข้อมูลและระบบแทนแอดมินได้</span>
</div>
<div style="background: linear-gradient(to bottom right, rgba(255,255,255,0.03), rgba(255,255,255,0.01)); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 18px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
<strong style="color: #3b82f6; font-size: 0.98rem; display: flex; align-items: center; gap: 8px; margin-bottom: 10px; text-shadow: 0 0 8px rgba(59,130,246,0.3);">💾 Data Exfiltration</strong>
<span style="color: #cbd5e1; font-size: 0.82rem; line-height: 1.6;">การดึงพารามิเตอร์ลับ รหัสผ่านแฮช หรือข้อมูลส่วนบุคคลของเหยื่อออกจากตารางฐานข้อมูลลับของเซิร์ฟเวอร์</span>
</div>
<div style="background: linear-gradient(to bottom right, rgba(255,255,255,0.03), rgba(255,255,255,0.01)); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 18px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
<strong style="color: #a855f7; font-size: 0.98rem; display: flex; align-items: center; gap: 8px; margin-bottom: 10px; text-shadow: 0 0 8px rgba(168,85,247,0.3);">🐚 Remote Code Execution</strong>
<span style="color: #cbd5e1; font-size: 0.82rem; line-height: 1.6;">การฝังโค้ดเชลล์ประสงค์ร้ายลงในระบบเพื่อเรียกใช้คำสั่งควบคุมสั่งการหน้าต่าง Terminal ของเว็บโฮสต์จากระยะไกล</span>
</div>
</div>

---

### 🛡️ ความเปรียบต่างวิวัฒนาการ OWASP Top 10 (2021 vs 2025/2026)
กรอบมาตรฐานความเสี่ยงระดับสากลได้รับการอัปเดตเพื่อสะท้อนวิวัฒนาการของการโจมตีในเทคโนโลยีคลาวด์ยุคใหม่:

<div style="overflow-x: auto; margin: 1.5rem auto; max-width: 1000px; border: 1px solid rgba(6,182,212,0.25); border-radius: 12px; background: #05070f; box-shadow: 0 10px 30px rgba(0,0,0,0.6);">
<table style="width: 100%; border-collapse: collapse; text-align: left; font-family: sans-serif; font-size: 0.85rem;">
<thead>
<tr style="background: rgba(6,182,212,0.08); border-bottom: 1px solid rgba(6,182,212,0.2);">
<th style="padding: 14px 18px; font-weight: bold; color: #a855f7; width: 42%; text-shadow: 0 0 6px rgba(168,85,247,0.3);">อันดับเดิมในปี 2021 (OWASP 2021)</th>
<th style="padding: 14px 18px; font-weight: bold; color: #00f0ff; width: 16%; text-align: center; text-shadow: 0 0 6px rgba(0,240,255,0.3);">แนวโน้ม</th>
<th style="padding: 14px 18px; font-weight: bold; color: #10b981; width: 42%; text-shadow: 0 0 6px rgba(16,185,129,0.3);">อันดับล่าสุดในการประกาศใช้ (2025 - Present)</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(255,255,255,0.005);">
<td style="padding: 14px 18px; color: #cbd5e1; vertical-align: middle;"><strong style="color: #ffffff;">A01:2021</strong> - Broken Access Control</td>
<td style="padding: 14px 18px; text-align: center; vertical-align: middle;">
  <span style="color: #94a3b8; font-weight: 900; font-size: 1.1rem; text-shadow: 0 0 4px rgba(148,163,184,0.4); letter-spacing: -2px;">➔</span>
</td>
<td style="padding: 14px 18px; color: #cbd5e1; vertical-align: middle;"><strong style="color: #ffffff;">A01:2025</strong> - Broken Access Control <span style="font-size:0.75rem; color:#10b981; font-weight:bold; margin-left:6px; background:rgba(16,185,129,0.1); padding:2px 6px; border-radius:4px; border:1px solid rgba(16,185,129,0.2);">(คงที่อันดับ 1)</span></td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(255,255,255,0.015);">
<td style="padding: 14px 18px; color: #cbd5e1; vertical-align: middle;"><strong style="color: #ffffff;">A02:2021</strong> - Cryptographic Failures</td>
<td style="padding: 14px 18px; text-align: center; vertical-align: middle;">
  <span style="color: #10b981; font-weight: 900; font-size: 1.1rem; text-shadow: 0 0 8px rgba(16,185,129,0.6);">↗</span>
</td>
<td style="padding: 14px 18px; color: #cbd5e1; vertical-align: middle;"><strong style="color: #ffffff;">A02:2025</strong> - Security Misconfiguration <span style="font-size:0.75rem; color:#f97316; font-weight:bold; margin-left:6px; background:rgba(249,115,22,0.1); padding:2px 6px; border-radius:4px; border:1px solid rgba(249,115,22,0.2);">(ขึ้นจากอันดับ 5)</span></td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(255,255,255,0.005);">
<td style="padding: 14px 18px; color: #cbd5e1; vertical-align: middle;"><strong style="color: #ffffff;">A05:2021</strong> - Security Misconfiguration</td>
<td style="padding: 14px 18px; text-align: center; vertical-align: middle;">
  <span style="color: #ef4444; font-weight: 900; font-size: 1.1rem; text-shadow: 0 0 8px rgba(239,68,68,0.6);">↘</span>
</td>
<td style="padding: 14px 18px; color: #cbd5e1; vertical-align: middle;"><strong style="color: #ffffff;">A04:2025</strong> - Cryptographic Failures <span style="font-size:0.75rem; color:#a855f7; font-weight:bold; margin-left:6px; background:rgba(168,85,247,0.1); padding:2px 6px; border-radius:4px; border:1px solid rgba(168,85,247,0.2);">(ลดลงจากอันดับ 2)</span></td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(255,255,255,0.015);">
<td style="padding: 14px 18px; color: #cbd5e1; vertical-align: middle;"><strong style="color: #ffffff;">A03:2021</strong> - Injection</td>
<td style="padding: 14px 18px; text-align: center; vertical-align: middle;">
  <span style="color: #94a3b8; font-weight: 900; font-size: 1.1rem; text-shadow: 0 0 4px rgba(148,163,184,0.4); letter-spacing: -2px;">➔</span>
</td>
<td style="padding: 14px 18px; color: #cbd5e1; vertical-align: middle;"><strong style="color: #ffffff;">A05:2025</strong> - Injection <span style="font-size:0.75rem; color:#10b981; font-weight:bold; margin-left:6px; background:rgba(16,185,129,0.1); padding:2px 6px; border-radius:4px; border:1px solid rgba(16,185,129,0.2);">(คงที่อันดับ 5)</span></td>
</tr>
<tr style="background: rgba(255,255,255,0.005);">
<td style="padding: 14px 18px; color: #94a3b8; vertical-align: middle; font-style: italic;">(พิกัดความเสี่ยงใหม่)</td>
<td style="padding: 14px 18px; text-align: center; vertical-align: middle;">
  <span style="background: rgba(168,85,247,0.2); border: 1px solid #a855f7; color: #d8b4fe; padding: 3px 8px; border-radius: 6px; font-size: 0.68rem; font-weight: bold; text-shadow: 0 0 8px rgba(168,85,247,0.5); letter-spacing: 0.05em;">NEW</span>
</td>
<td style="padding: 14px 18px; color: #cbd5e1; vertical-align: middle;"><strong style="color: #34d399;">A03:2025</strong> - Software Supply Chain Failures <span style="font-size:0.75rem; color:#34d399; font-weight:bold; margin-left:6px; background:rgba(52,211,153,0.1); padding:2px 6px; border-radius:4px; border:1px solid rgba(52,211,153,0.2);">(ความปลอดภัยซัพพลายเชน)</span></td>
</tr>
</tbody>
</table>
</div>

---

### 🛡️ คลังความรู้เจาะลึก 10 อันดับความเสี่ยงความเปราะบาง (OWASP Top 10 Complete Suite)
คำอธิบายเชิงสถาปัตยกรรม แผนภาพกราฟิกจำลองเวกเตอร์ (Vector Graphic Diagram) และระดับความรุนแรงของภัยคุกคาม:

<style>
.owasp-card {
  background: #05070f;
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.45);
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 20px;
  align-items: start;
}
@media (max-width: 900px) {
  .owasp-card {
    grid-template-columns: 1fr;
  }
}
</style>

<div style="display: flex; flex-direction: column; gap: 24px; margin: 1.5rem auto;">

<!-- A01 -->
<div class="owasp-card">
<div>
<div style="font-size: 1.05rem; font-weight: bold; color: #00f0ff; margin-bottom: 2px;">A01:2025 - Broken Access Control (การควบคุมสิทธิ์บกพร่อง)</div>
<div style="margin: 4px 0 10px 0; display: flex; align-items: center; gap: 8px;">
  <span style="font-size: 0.72rem; color: #94a3b8; font-weight: bold;">ระดับความรุนแรง:</span>
  <div style="flex-grow: 1; height: 6px; background: rgba(255,255,255,0.05); border-radius: 3px; overflow: hidden; max-width: 120px;">
    <div style="width: 95%; height: 100%; background: linear-gradient(90deg, #ef4444, #f43f5e); box-shadow: 0 0 6px #f43f5e;"></div>
  </div>
  <span style="font-size: 0.7rem; color: #f43f5e; font-weight: 800; text-shadow: 0 0 4px rgba(244,63,94,0.4);">CRITICAL (9.5/10)</span>
</div>
<div style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.6;">
<strong style="color: #ffffff;">🔴 ปัญหาที่เกิดขึ้น (Occurs when):</strong>
ผู้ใช้ธรรมดาสามารถเข้าถึงและดัดแปลงทรัพยากรส่วนตัว หรือฟังก์ชันการทำงานที่พวกเขาไม่ควรได้รับสิทธิ์เข้าใช้งาน<br>
<strong style="color: #ffffff;">💀 ผลกระทบระดับอันตราย (Can lead to):</strong>
การรั่วไหลของข้อมูลสมาชิก (Data leakage), การเข้าสิทธิ์หลังบ้านโดยข้ามการตรวจสิทธิ์ (Bypassing authentication)<br>
<strong style="color: #ffffff;">📝 ตัวอย่างเคสที่พบ (Examples):</strong>
- <strong>URL Bypass:</strong> เดาพาธแอดมินตรงๆ เช่น การพิมพ์ <code style="color:#00f0ff;">/admin</code> บน URL ลิงก์ตรงๆ<br>
- <strong>Tampering parameters:</strong> การแก้ไขตัวแปร ID ใน URL หรือเปลี่ยนค่า JWT cookie เพื่อเลื่อนสิทธิ์แอดมิน<br>
<strong style="color: #ffffff;">🔍 สถานการณ์จำลอง (Scenario):</strong>
เว็บแอปพลิเคชันมี URL โปรไฟล์ผู้ใช้ระบุค่าตัวเลขดิบ เช่น <code style="color:#00f0ff;">/profile/view/12345</code> แฮกเกอร์แอบเปลี่ยนเลขตัวหลังเป็น <code style="color:#00f0ff;">12346</code> และระบบยอมให้เปิดอ่านโปรไฟล์ผู้อื่นได้โดยไม่มีการรันคำสั่งเช็คยืนยันตัวตน
</div>
</div>
<div style="background: rgba(255,255,255,0.01); border: 1px solid rgba(255,255,255,0.04); border-radius: 8px; padding: 14px; text-align: center;">
<div style="font-size: 0.72rem; color: #94a3b8; margin-bottom: 12px; font-weight: bold; text-transform: uppercase;">📊 Graphic: Access Control vs Broken Access Control</div>
<svg viewBox="0 0 420 180" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #030408; border-radius: 8px;">
<rect x="10" y="10" width="190" height="160" rx="8" fill="none" stroke="rgba(255,255,255,0.05)"/>
<text x="105" y="30" fill="#a7f3d0" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Access Control (ปกติ)</text>
<g transform="translate(20, 65)">
<rect x="0" y="10" width="26" height="16" rx="2" fill="#1e293b" stroke="#00f0ff" stroke-width="1.5"/>
<line x1="5" y1="13" x2="21" y2="13" stroke="#00f0ff" stroke-width="1"/>
<polygon points="-4,28 30,28 26,26 0,26" fill="#334155" stroke="#00f0ff" stroke-width="1"/>
<circle cx="13" cy="4" r="5" fill="#475569"/>
<path d="M5,12 C5,8 21,8 21,12 Z" fill="#475569"/>
<text x="13" y="38" fill="#8892b0" font-size="8" font-family="sans-serif" text-anchor="middle">User</text>
</g>
<g transform="translate(90, 55)">
<rect x="0" y="0" width="28" height="42" rx="4" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
<line x1="4" y1="8" x2="24" y2="8" stroke="#10b981" stroke-width="1.5"/>
<line x1="4" y1="16" x2="24" y2="16" stroke="#10b981" stroke-width="1.5"/>
<rect x="9" y="26" width="10" height="8" rx="1" fill="#10b981"/>
<path d="M11,26 L11,22 A3,3 0 0,1 17,22 L17,26" fill="none" stroke="#10b981" stroke-width="1.5"/>
<text x="14" y="52" fill="#8892b0" font-size="8" font-family="sans-serif" text-anchor="middle">Server</text>
</g>
<g transform="translate(155, 65)">
<circle cx="13" cy="5" r="6" fill="#ef4444"/>
<path d="M3,18 C3,10 23,10 23,18 Z" fill="#ef4444"/>
<path d="M3,15 L23,15" stroke="#ef4444" stroke-width="1.5"/>
<text x="13" y="38" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle">Hacker</text>
</g>
<line x1="50" y1="82" x2="86" y2="82" stroke="#10b981" stroke-width="1.5"/>
<polygon points="86,79 92,82 86,85" fill="#10b981"/>
<text x="68" y="76" fill="#10b981" font-size="7" font-family="sans-serif" text-anchor="middle">Granted</text>
<path d="M152,82 L122,82" stroke="#ef4444" stroke-width="1.5"/>
<line x1="132" y1="77" x2="142" y2="87" stroke="#ef4444" stroke-width="2"/>
<line x1="142" y1="77" x2="132" y2="87" stroke="#ef4444" stroke-width="2"/>
<text x="140" y="73" fill="#ef4444" font-size="7" font-family="sans-serif" text-anchor="middle">Blocked</text>

<rect x="220" y="10" width="190" height="160" rx="8" fill="none" stroke="rgba(255,255,255,0.05)"/>
<text x="315" y="30" fill="#fca5a5" font-size="11" font-family="sans-serif" text-anchor="middle" font-weight="bold">Broken Access Control</text>
<g transform="translate(230, 65)">
<rect x="0" y="10" width="26" height="16" rx="2" fill="#1e293b" stroke="#00f0ff" stroke-width="1.5"/>
<line x1="5" y1="13" x2="21" y2="13" stroke="#00f0ff" stroke-width="1"/>
<polygon points="-4,28 30,28 26,26 0,26" fill="#334155" stroke="#00f0ff" stroke-width="1"/>
<circle cx="13" cy="4" r="5" fill="#475569"/>
<path d="M5,12 C5,8 21,8 21,12 Z" fill="#475569"/>
<text x="13" y="38" fill="#8892b0" font-size="8" font-family="sans-serif" text-anchor="middle">User</text>
</g>
<g transform="translate(300, 55)">
<rect x="0" y="0" width="28" height="42" rx="4" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
<line x1="4" y1="8" x2="24" y2="8" stroke="#ef4444" stroke-width="1.5"/>
<line x1="4" y1="16" x2="24" y2="16" stroke="#ef4444" stroke-width="1.5"/>
<rect x="9" y="26" width="10" height="8" rx="1" fill="#ef4444"/>
<path d="M15,26 L15,19 A3,3 0 0,1 21,21" fill="none" stroke="#ef4444" stroke-width="1.5"/>
<text x="14" y="52" fill="#8892b0" font-size="8" font-family="sans-serif" text-anchor="middle">Server</text>
</g>
<g transform="translate(365, 65)">
<circle cx="13" cy="5" r="6" fill="#ef4444"/>
<path d="M3,18 C3,10 23,10 23,18 Z" fill="#ef4444"/>
<path d="M3,15 L23,15" stroke="#ef4444" stroke-width="1.5"/>
<text x="13" y="38" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle">Hacker</text>
</g>
<line x1="260" y1="82" x2="296" y2="82" stroke="#10b981" stroke-width="1.5"/>
<path d="M362,82 L332,82" stroke="#10b981" stroke-width="1.5"/>
<text x="347" y="76" fill="#10b981" font-size="7" font-family="sans-serif" text-anchor="middle">Bypass!</text>
</svg>
</div>
</div>
</div>

<!-- A02 -->
<div class="owasp-card">
<div>
<div style="font-size: 1.05rem; font-weight: bold; color: #00f0ff; margin-bottom: 2px;">A02:2025 - Security Misconfiguration (การตั้งค่าสิทธิ์ความปลอดภัยผิดพลาด)</div>
<div style="margin: 4px 0 10px 0; display: flex; align-items: center; gap: 8px;">
  <span style="font-size: 0.72rem; color: #94a3b8; font-weight: bold;">ระดับความรุนแรง:</span>
  <div style="flex-grow: 1; height: 6px; background: rgba(255,255,255,0.05); border-radius: 3px; overflow: hidden; max-width: 120px;">
    <div style="width: 85%; height: 100%; background: linear-gradient(90deg, #f97316, #eab308); box-shadow: 0 0 6px #f97316;"></div>
  </div>
  <span style="font-size: 0.7rem; color: #f97316; font-weight: 800; text-shadow: 0 0 4px rgba(249,115,22,0.4);">HIGH (8.5/10)</span>
</div>
<div style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.6;">
<strong style="color: #ffffff;">🔴 ปัญหาที่เกิดขึ้น (Occurs when):</strong>
ระบบแอปพลิเคชัน, ฐานข้อมูลหลังบ้าน หรือเว็บเซิร์ฟเวอร์ไม่ได้ตั้งค่าความมั่นคงปลอดภัยอย่างรัดกุม ปล่อยให้ใช้งานคอนฟิกเริ่มต้นดีฟอลต์<br>
<strong style="color: #ffffff;">💀 ผลกระทบระดับอันตราย (Can lead to):</strong>
ข้อมูลความลับถูกขโมย หรือแฮกเกอร์มองเห็นโครงสร้างโฟลเดอร์ของระบบทั้งหมดได้ทันที<br>
<strong style="color: #ffffff;">📝 ตัวอย่างเคสที่พบ (Examples):</strong>
- ลืมเปลี่ยนรหัสผ่านเริ่มต้นของระบบ (เช่น ชื่อผู้ใช้ <code style="color:#00f0ff;">admin</code> และรหัสผ่าน <code style="color:#00f0ff;">admin</code>)<br>
- ปล่อย Directory listing ทำงาน ทำให้เปิดอ่านโครงสร้างไฟล์ย่อยบนหน้าเว็บได้<br>
- เปิดโหมด Debug ค้างไว้ในระบบจริง เผยแพร่โค้ดและข้อมูลส่วนเชื่อมต่อฐานข้อมูลดิบ<br>
<strong style="color: #ffffff;">🔍 สถานการณ์จำลอง (Scenario):</strong>
เว็บเซิร์ฟเวอร์เปิดโหมด Debug ทิ้งไว้ เมื่อแฮกเกอร์จงใจสร้างข้อผิดพลาดให้ระบบพัง ตัวเว็บหลังบ้านจะพ่น Stack trace และ Database Password ออกมาทางบราวเซอร์ ทำให้แฮกเกอร์ลอบนำไปเจาะฐานข้อมูลได้สำเร็จ
</div>
</div>
<div style="background: rgba(255,255,255,0.01); border: 1px solid rgba(255,255,255,0.04); border-radius: 8px; padding: 14px; text-align: center;">
<div style="font-size: 0.72rem; color: #94a3b8; margin-bottom: 12px; font-weight: bold; text-transform: uppercase;">📊 Graphic: Security Misconfiguration</div>
<svg viewBox="0 0 400 150" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #030408; border-radius: 8px;">
<g transform="translate(30, 50)">
<circle cx="15" cy="10" r="8" fill="#ef4444"/>
<path d="M3,28 C3,18 27,18 27,28 Z" fill="#ef4444"/>
<text x="15" y="44" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle">Attacker</text>
</g>
<line x1="70" y1="75" x2="155" y2="75" stroke="#f97316" stroke-width="1.5" stroke-dasharray="4,2"/>
<text x="112" y="66" fill="#f97316" font-size="8" font-family="monospace" text-anchor="middle">Access via Default</text>
<rect x="170" y="35" width="16" height="80" rx="3" fill="#334155" stroke="#94a3b8"/>
<line x1="170" y1="55" x2="186" y2="55" stroke="#ef4444" stroke-width="2"/>
<line x1="170" y1="75" x2="186" y2="75" stroke="#ef4444" stroke-width="2"/>
<line x1="170" y1="95" x2="186" y2="95" stroke="#ef4444" stroke-width="2"/>
<g transform="translate(210, 25)">
<rect x="0" y="0" width="65" height="40" rx="4" fill="#0f172a" stroke="#00f0ff" stroke-width="1.5"/>
<text x="32" y="15" fill="#00f0ff" font-size="7" font-family="sans-serif" text-anchor="middle">Server (Active)</text>
<text x="32" y="30" fill="#ef4444" font-size="6" font-family="monospace" text-anchor="middle">Admin:Admin</text>
<line x1="-15" y1="20" x2="0" y2="20" stroke="#f43f5e" stroke-width="1.5"/>
</g>
<g transform="translate(210, 85)">
<rect x="0" y="0" width="65" height="40" rx="4" fill="#0f172a" stroke="#00f0ff" stroke-width="1.5"/>
<text x="32" y="15" fill="#00f0ff" font-size="7" font-family="sans-serif" text-anchor="middle">Database Server</text>
<text x="32" y="30" fill="#ef4444" font-size="6" font-family="monospace" text-anchor="middle">Debug: Active</text>
<line x1="-15" y1="20" x2="0" y2="20" stroke="#f43f5e" stroke-width="1.5"/>
</g>
<g transform="translate(315, 55)">
<rect x="0" y="0" width="40" height="40" rx="2" fill="#1e293b" stroke="#a855f7" stroke-width="1.5"/>
<ellipse cx="20" cy="10" rx="15" ry="5" fill="#a855f7"/>
<ellipse cx="20" cy="20" rx="15" ry="5" fill="#a855f7"/>
<ellipse cx="20" cy="30" rx="15" ry="5" fill="#a855f7"/>
<text x="20" y="48" fill="#cbd5e1" font-size="6" font-family="sans-serif" text-anchor="middle">Leak!</text>
</g>
<line x1="275" y1="45" x2="315" y2="70" stroke="#f43f5e" stroke-width="1.5"/>
<line x1="275" y1="105" x2="315" y2="75" stroke="#f43f5e" stroke-width="1.5"/>
</svg>
</div>
</div>
</div>

<!-- A03 -->
<div class="owasp-card">
<div>
<div style="font-size: 1.05rem; font-weight: bold; color: #00f0ff; margin-bottom: 2px;">A03:2025 - Software Supply Chain Failures (ความล้มเหลวด้านซอฟต์แวร์และข้อมูล)</div>
<div style="margin: 4px 0 10px 0; display: flex; align-items: center; gap: 8px;">
  <span style="font-size: 0.72rem; color: #94a3b8; font-weight: bold;">ระดับความรุนแรง:</span>
  <div style="flex-grow: 1; height: 6px; background: rgba(255,255,255,0.05); border-radius: 3px; overflow: hidden; max-width: 120px;">
    <div style="width: 90%; height: 100%; background: linear-gradient(90deg, #ef4444, #f97316); box-shadow: 0 0 6px #ef4444;"></div>
  </div>
  <span style="font-size: 0.7rem; color: #f43f5e; font-weight: 800; text-shadow: 0 0 4px rgba(244,63,94,0.4);">CRITICAL (9.0/10)</span>
</div>
<div style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.6;">
<strong style="color: #ffffff;">🔴 ปัญหาที่เกิดขึ้น (Occurs when):</strong>
การเรียกใช้ปลั๊กอิน ไลบรารีซอร์สโค้ด หรืออัปเดตระบบจากภายนอกโดยไม่มีการตรวจเช็คลายมือชื่อดิจิทัลรับรอง (Integrity Verification)<br>
<strong style="color: #ffffff;">💀 ผลกระทบระดับอันตราย (Can lead to):</strong>
การถูกโจมตีแบบซัพพลายเชน (Supply Chain Attack) โดยแฮกเกอร์ลอบนำส่งมัลแวร์มาติดตั้งแฝงผ่านกระบวนการบิวด์อัตโนมัติ<br>
<strong style="color: #ffffff;">📝 ตัวอย่างเคสที่พบ (Examples):</strong>
- การติดตั้งปลั๊กอินดัดแปลงหลังบ้านที่อ้างว่าปล่อยให้ใช้งานฟรี<br>
- การเรียกใช้ไฟล์ JavaScript หรือคอมโพเนนต์คลาวด์จากผู้พัฒนาที่ไม่น่าเชื่อถือ<br>
<strong style="color: #ffffff;">🔍 สถานการณ์จำลอง (Scenario):</strong>
ช่องทาง CI/CD pipeline ถูกผู้ไม่ประสงค์ดีเจาะระบบลักลอบฝังมัลแวร์ลงในแพ็กเกจอัปเดต เมื่อเครื่องเซิร์ฟเวอร์หลักทำการอัปเกรดแอปพลิเคชันระบบอัตโนมัติ จะส่งผลให้มัลแวร์ทำงานส่งข้อมูลความลับออกไปทันที
</div>
</div>
<div style="background: rgba(255,255,255,0.01); border: 1px solid rgba(255,255,255,0.04); border-radius: 8px; padding: 14px; text-align: center;">
<div style="font-size: 0.72rem; color: #94a3b8; margin-bottom: 12px; font-weight: bold; text-transform: uppercase;">📊 Graphic: Software Supply Chain</div>
<svg viewBox="0 0 400 150" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #030408; border-radius: 8px;">
<g transform="translate(15, 55)">
<rect x="0" y="0" width="70" height="35" rx="4" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5"/>
<text x="35" y="21" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Source Repo</text>
</g>
<g transform="translate(100, 10)">
<circle cx="15" cy="8" r="6" fill="#ef4444"/>
<path d="M5,22 C5,14 25,14 25,22 Z" fill="#ef4444"/>
<text x="15" y="32" fill="#ef4444" font-size="7" font-family="sans-serif" text-anchor="middle">Malicious User</text>
</g>
<path d="M115,45 Q135,70 160,70" fill="none" stroke="#ef4444" stroke-dasharray="3,1" stroke-width="1.5"/>
<line x1="85" y1="72" x2="145" y2="72" stroke="#3b82f6" stroke-width="1.5"/>
<g transform="translate(150, 55)">
<rect x="0" y="0" width="75" height="35" rx="4" fill="#0f172a" stroke="#fbbf24" stroke-width="1.5"/>
<text x="37" y="21" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">CI/CD Pipeline</text>
</g>
<line x1="225" y1="72" x2="280" y2="72" stroke="#ef4444" stroke-width="1.5"/>
<g transform="translate(285, 55)">
<rect x="0" y="0" width="70" height="35" rx="4" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
<text x="35" y="21" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle">Prod Server</text>
</g>
</svg>
</div>
</div>
</div>

<!-- A04 -->
<div class="owasp-card">
<div>
<div style="font-size: 1.05rem; font-weight: bold; color: #00f0ff; margin-bottom: 2px;">A04:2025 - Cryptographic Failures (ความล้มเหลวในการเข้ารหัสข้อมูล)</div>
<div style="margin: 4px 0 10px 0; display: flex; align-items: center; gap: 8px;">
  <span style="font-size: 0.72rem; color: #94a3b8; font-weight: bold;">ระดับความรุนแรง:</span>
  <div style="flex-grow: 1; height: 6px; background: rgba(255,255,255,0.05); border-radius: 3px; overflow: hidden; max-width: 120px;">
    <div style="width: 92%; height: 100%; background: linear-gradient(90deg, #ef4444, #f43f5e); box-shadow: 0 0 6px #f43f5e;"></div>
  </div>
  <span style="font-size: 0.7rem; color: #f43f5e; font-weight: 800; text-shadow: 0 0 4px rgba(244,63,94,0.4);">CRITICAL (9.2/10)</span>
</div>
<div style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.6;">
<strong style="color: #ffffff;">🔴 ปัญหาที่เกิดขึ้น (Occurs when):</strong>
การเข้ารหัสข้อมูลไม่แน่นหนาพอ หรือการรับส่งข้อมูลที่เป็นความลับผ่านช่องทางปกติที่ไม่มีการเข้ารหัสความปลอดภัย<br>
<strong style="color: #ffffff;">💀 ผลกระทบระดับอันตราย (Can lead to):</strong>
ข้อมูลรั่วไหลระหว่างทาง (Data leak), รหัสผ่านหลุดร่วงเผยแพร่สู่ภายนอก (Password exposure)<br>
<strong style="color: #ffffff;">📝 ตัวอย่างเคสที่พบ (Examples):</strong>
- Storing passwords in plaintext: บันทึกรหัสผ่านสมาชิกไว้ในฐานข้อมูลเป็นข้อความธรรมดา หรือใช้แฮชที่แคร็กได้ง่าย เช่น MD5<br>
- การรับส่งข้อมูลความลับผ่านช่องทางโปรโตคอลที่ไม่เข้ารหัส เช่น HTTP (Port 80)<br>
<strong style="color: #ffffff;">🔍 สถานการณ์จำลอง (Scenario):</strong>
เว็บแอปจัดเก็บรหัสผ่านผู้เรียนไว้เป็นข้อความธรรมดา หรือนำไปแฮชด้วย MD5 แฮกเกอร์ที่เจาะฐานข้อมูลได้จะขโมยรายชื่อรหัสผ่านนี้ไปแคร็กเปรียบเทียบใน Wordlist ยอดฮิตได้อย่างรวดเร็ว ทำให้เข้าถึงรหัสผ่านจริงของสมาชิกทั้งหมดบนระบบได้ทันที
</div>
</div>
<div style="background: rgba(255,255,255,0.01); border: 1px solid rgba(255,255,255,0.04); border-radius: 8px; padding: 14px; text-align: center;">
<div style="font-size: 0.72rem; color: #94a3b8; margin-bottom: 12px; font-weight: bold; text-transform: uppercase;">📊 Graphic: Cryptographic Failures</div>
<svg viewBox="0 0 400 150" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #030408; border-radius: 8px;">
<g transform="translate(20, 30)">
<rect x="0" y="0" width="110" height="90" rx="4" fill="#0f172a" stroke="#00f0ff" stroke-width="1.5"/>
<text x="55" y="18" fill="#00f0ff" font-size="8" font-family="sans-serif" text-anchor="middle" font-weight="bold">Database (MD5 Hash)</text>
<text x="10" y="40" fill="#a855f7" font-size="7" font-family="monospace">admin: 21232f297a...</text>
<text x="10" y="60" fill="#a855f7" font-size="7" font-family="monospace">user1: 5f4dcc3b5a...</text>
<text x="10" y="80" fill="#a855f7" font-size="7" font-family="monospace">pass2: 7815696ecb...</text>
</g>
<line x1="140" y1="75" x2="220" y2="75" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,1"/>
<g transform="translate(230, 50)">
<circle cx="15" cy="10" r="8" fill="#ef4444"/>
<path d="M3,28 C3,18 27,18 27,28 Z" fill="#ef4444"/>
<text x="15" y="44" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle">Hacker</text>
</g>
<line x1="270" y1="75" x2="310" y2="75" stroke="#34d399" stroke-width="1.5"/>
<g transform="translate(320, 50)">
<rect x="0" y="0" width="60" height="50" rx="3" fill="#1e293b" stroke="#34d399" stroke-width="1.5"/>
<text x="30" y="16" fill="#34d399" font-size="7" font-family="monospace" text-anchor="middle">Cracked!</text>
<text x="30" y="32" fill="#ffffff" font-size="6" font-family="monospace" text-anchor="middle">"admin"</text>
<text x="30" y="42" fill="#ffffff" font-size="6" font-family="monospace" text-anchor="middle">"password"</text>
</g>
</svg>
</div>
</div>
</div>

<!-- A05 -->
<div class="owasp-card">
<div>
<div style="font-size: 1.05rem; font-weight: bold; color: #00f0ff; margin-bottom: 2px;">A05:2025 - Injection (การยิงแทรกคำสั่งประมวลผล)</div>
<div style="margin: 4px 0 10px 0; display: flex; align-items: center; gap: 8px;">
  <span style="font-size: 0.72rem; color: #94a3b8; font-weight: bold;">ระดับความรุนแรง:</span>
  <div style="flex-grow: 1; height: 6px; background: rgba(255,255,255,0.05); border-radius: 3px; overflow: hidden; max-width: 120px;">
    <div style="width: 94%; height: 100%; background: linear-gradient(90deg, #ef4444, #f43f5e); box-shadow: 0 0 6px #f43f5e;"></div>
  </div>
  <span style="font-size: 0.7rem; color: #f43f5e; font-weight: 800; text-shadow: 0 0 4px rgba(244,63,94,0.4);">CRITICAL (9.4/10)</span>
</div>
<div style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.6;">
<strong style="color: #ffffff;">🔴 ปัญหาที่เกิดขึ้น (Occurs when):</strong>
แอปพลิเคชันเว็บรับอินพุตข้อมูลโดยไม่มีคำสั่งสกัดลบ (Sanitization) อักขระพิเศษ แล้วนำไปป้อนเป็นตัวแปรคำสั่งประมวลผลระบบตรงๆ<br>
<strong style="color: #ffffff;">💀 ผลกระทบระดับอันตราย (Can lead to):</strong>
ข้อมูลสูญหาย ดึงประวัติไฟล์สำคัญภายนอก หรือถูกยึดระบบหลังบ้านได้ทันที<br>
<strong style="color: #ffffff;">📝 ตัวอย่างประเภทสำคัญ (Key Categories):</strong>
- <strong>SQL Injection (SQLi):</strong> การแทรกสตริง SQL คิวรีเพื่อหลบเงื่อนไขและดึงตารางข้อมูลลับ<br>
- <strong>OS Command Injection:</strong> การฝังเซมิโคลอนและคำสั่งระบบปฏิบัติการ Linux ในช่องฟอร์มปิง IP<br>
- <strong>Cross-Site Scripting (XSS):</strong> การฝังสคริปต์ JavaScript เพื่อไปรันประมวลผลบน Client ของเหยื่อ<br>
<strong style="color: #ffffff;">🔍 สถานการณ์จำลอง (Scenario):</strong>
ในแบบฟอร์มเข้าสู่ระบบ ตรรกะตรวจเช็คความถูกต้องของชื่อผู้ใช้และรหัสผ่านนำอินพุตผู้ใช้ไปเขียนคิวรีดิบ แฮกเกอร์แอบใส่ข้อความสัญลักษณ์ <code style="color:#00f0ff;">' OR '1'='1</code> เข้าที่ฟิลด์ชื่อผู้ใช้ ทำให้คำสั่ง SQL เปลี่ยนรูปแบบการคำนวณและประมวลผลสิทธิ์เป็นจริงเสมอ นำไปสู่การ Bypass เข้าแผงแอดมินทันทีโดยไม่ต้องรหัสผ่านจริง
</div>
</div>
<div style="background: rgba(255,255,255,0.01); border: 1px solid rgba(255,255,255,0.04); border-radius: 8px; padding: 14px; text-align: center;">
<div style="font-size: 0.72rem; color: #94a3b8; margin-bottom: 12px; font-weight: bold; text-transform: uppercase;">📊 Graphic: SQL Injection</div>
<svg viewBox="0 0 400 150" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #030408; border-radius: 8px;">
<g transform="translate(15, 45)">
<rect x="0" y="0" width="100" height="60" rx="3" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
<text x="50" y="16" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Login Username Input</text>
<rect x="10" y="28" width="80" height="20" rx="2" fill="#1e293b" stroke="#ef4444"/>
<text x="50" y="41" fill="#fca5a5" font-size="6" font-family="monospace" text-anchor="middle">' OR '1'='1' --</text>
</g>
<line x1="125" y1="75" x2="195" y2="75" stroke="#ef4444" stroke-width="1.5"/>
<text x="160" y="67" fill="#ef4444" font-size="6" font-family="monospace" text-anchor="middle">Bypass Query</text>
<g transform="translate(205, 35)">
<rect x="0" y="0" width="115" height="80" rx="3" fill="#0f172a" stroke="#00f0ff" stroke-width="1.5"/>
<text x="57" y="18" fill="#00f0ff" font-size="7" font-family="monospace" text-anchor="middle">SELECT * FROM users</text>
<text x="57" y="38" fill="#fca5a5" font-size="6" font-family="monospace" text-anchor="middle">WHERE user='' OR '1'='1'</text>
<text x="57" y="58" fill="#34d399" font-size="6" font-family="monospace" text-anchor="middle">[Result: True ALWAYS]</text>
</g>
<line x1="330" y1="75" x2="360" y2="75" stroke="#34d399" stroke-width="1.5"/>
<circle cx="375" cy="75" r="10" fill="#34d399"/>
<text x="375" y="78" fill="#ffffff" font-size="7" font-family="sans-serif" text-anchor="middle">✔️</text>
</svg>
</div>
</div>
</div>

<!-- A06 -->
<div class="owasp-card">
<div>
<div style="font-size: 1.05rem; font-weight: bold; color: #00f0ff; margin-bottom: 2px;">A06:2025 - Insecure Design (การออกแบบระบบที่ไม่ปลอดภัย)</div>
<div style="margin: 4px 0 10px 0; display: flex; align-items: center; gap: 8px;">
  <span style="font-size: 0.72rem; color: #94a3b8; font-weight: bold;">ระดับความรุนแรง:</span>
  <div style="flex-grow: 1; height: 6px; background: rgba(255,255,255,0.05); border-radius: 3px; overflow: hidden; max-width: 120px;">
    <div style="width: 82%; height: 100%; background: linear-gradient(90deg, #f97316, #eab308); box-shadow: 0 0 6px #f97316;"></div>
  </div>
  <span style="font-size: 0.7rem; color: #f97316; font-weight: 800; text-shadow: 0 0 4px rgba(249,115,22,0.4);">HIGH (8.2/10)</span>
</div>
<div style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.6;">
<strong style="color: #ffffff;">🔴 ปัญหาที่เกิดขึ้น (Occurs when):</strong>
ความบกพร่องของตรรกะระบบตั้งแต่ขั้นตอนการออกแบบโครงสร้างสถาปัตยกรรม (Architecture) หรือการขาดการทำ Threat Modeling<br>
<strong style="color: #ffffff;">💀 ผลกระทบระดับอันตราย (Can lead to):</strong>
การถูกเจาะระบบโดยที่ไม่มีส่วนใดในบรรทัดโค้ดหลักเกิดข้อผิดพลาดทางไวยากรณ์ (Syntax)<br>
<strong style="color: #ffffff;">📝 ตัวอย่างเคสที่พบ (Examples):</strong>
- แอปพลิเคชันธุรกรรมการเงินยอมให้ตั้งค่าขอเปลี่ยนรหัสผ่านใหม่ได้ทันทีโดยไม่ต้องส่งอีเมลยืนยันตัวตนหรือกรอกรหัสผ่านเก่า<br>
- การขาด Rate Limiting เปิดโอกาสให้แฮกเกอร์ใช้โปรแกรมยิงเพื่อเดารหัสหรือส่งทราฟฟิกป่วนระบบอย่างเสรี<br>
<strong style="color: #ffffff;">🔍 สถานการณ์จำลอง (Scenario):</strong>
เว็บระบบสมัครสมาชิกระบุพารามิเตอร์ตรวจสอบไม่มีการจำกัดจำนวนครั้งการล็อกอิน แฮกเกอร์เขียนสคริปต์สั้นๆ รันคำสั่งเดารหัสผ่านซ้ำเป็นล้านรอบอย่างรวดเร็วเพื่อ Brute Force โดยที่ระบบตรวจเฝ้าระวังไม่รับรู้ นำไปสู่การเข้ายึดระบบได้สำเร็จในที่สุด
</div>
</div>
<div style="background: rgba(255,255,255,0.01); border: 1px solid rgba(255,255,255,0.04); border-radius: 8px; padding: 14px; text-align: center;">
<div style="font-size: 0.72rem; color: #94a3b8; margin-bottom: 12px; font-weight: bold; text-transform: uppercase;">📊 Graphic: Insecure Design (No Rate Limit)</div>
<svg viewBox="0 0 400 150" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #030408; border-radius: 8px;">
<g transform="translate(20, 50)">
<circle cx="15" cy="10" r="8" fill="#ef4444"/>
<path d="M3,28 C3,18 27,18 27,28 Z" fill="#ef4444"/>
<text x="15" y="44" fill="#fca5a5" font-size="7" font-family="sans-serif" text-anchor="middle">Brute Force Bot</text>
</g>
<path d="M60,60 L140,40" stroke="#ef4444" stroke-width="1"/>
<path d="M60,70 L140,65" stroke="#ef4444" stroke-width="1"/>
<path d="M60,80 L140,85" stroke="#ef4444" stroke-width="1"/>
<path d="M60,90 L140,110" stroke="#ef4444" stroke-width="1"/>
<g transform="translate(150, 35)">
<rect x="0" y="0" width="105" height="80" rx="3" fill="#0f172a" stroke="#00f0ff" stroke-width="1.5"/>
<text x="52" y="20" fill="#00f0ff" font-size="8" font-family="sans-serif" text-anchor="middle">Web Server</text>
<text x="52" y="45" fill="#ef4444" font-size="6" font-family="monospace" text-anchor="middle">Requests: Endless</text>
<text x="52" y="65" fill="#cbd5e1" font-size="6" font-family="monospace" text-anchor="middle">No Lock Policy</text>
</g>
<line x1="260" y1="75" x2="310" y2="75" stroke="#ef4444" stroke-width="1.5"/>
<g transform="translate(320, 50)">
<rect x="0" y="0" width="60" height="50" rx="3" fill="#1e293b" stroke="#ef4444" stroke-width="1.5"/>
<text x="30" y="20" fill="#ef4444" font-size="7" font-family="monospace" text-anchor="middle">CRACKED!</text>
<text x="30" y="38" fill="#ffffff" font-size="6" font-family="monospace" text-anchor="middle">Pass: 123456</text>
</g>
</svg>
</div>
</div>
</div>

<!-- A07 -->
<div class="owasp-card">
<div>
<div style="font-size: 1.05rem; font-weight: bold; color: #00f0ff; margin-bottom: 2px;">A07:2025 - Authentication Failures (ความล้มเหลวในการระบุตัวตน)</div>
<div style="margin: 4px 0 10px 0; display: flex; align-items: center; gap: 8px;">
  <span style="font-size: 0.72rem; color: #94a3b8; font-weight: bold;">ระดับความรุนแรง:</span>
  <div style="flex-grow: 1; height: 6px; background: rgba(255,255,255,0.05); border-radius: 3px; overflow: hidden; max-width: 120px;">
    <div style="width: 88%; height: 100%; background: linear-gradient(90deg, #ef4444, #f97316); box-shadow: 0 0 6px #f97316;"></div>
  </div>
  <span style="font-size: 0.7rem; color: #f97316; font-weight: 800; text-shadow: 0 0 4px rgba(249,115,22,0.4);">HIGH (8.8/10)</span>
</div>
<div style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.6;">
<strong style="color: #ffffff;">🔴 ปัญหาที่เกิดขึ้น (Occurs when):</strong>
ระบบแอปพลิเคชันไม่ป้องกันความแข็งแกร่งของรหัสผ่าน หรือไม่มีระบบล็อกบัญชีเมื่อมีความพยายามเข้าสู่ระบบที่ล้มเหลวหลายครั้ง<br>
<strong style="color: #ffffff;">💀 ผลกระทบระดับอันตราย (Can lead to):</strong>
ผู้ใช้ทั่วไปถูกแฮกเกอร์โจรกรรมบัญชี หรือสวมสิทธิ์แทนเจ้าของที่แท้จริงได้โดยง่าย<br>
<strong style="color: #ffffff;">📝 ตัวอย่างเคสที่พบ (Examples):</strong>
- ยินยอมให้ตั้งค่ารหัสผ่านที่เดาง่ายมาก เช่น <code style="color:#00f0ff;">123456</code> หรือ <code style="color:#00f0ff;">password123</code><br>
- ไม่ล็อกหรือระงับไอดี (Account lockout) ชั่วคราวเมื่อกรอกรหัสผ่านผิดซ้ำๆ หลายครั้ง<br>
<strong style="color: #ffffff;">🔍 สถานการณ์จำลอง (Scenario):</strong>
หน้าต่างลงทะเบียนผู้ใช้บริการไม่ได้คัดกรองหรือแจ้งเตือนความปลอดภัยของรหัสผ่าน แฮกเกอร์จึงนำบอทและไฟล์ลิสต์รหัสผ่านยอดฮิตมาสแกนเทียบหาบัญชีสมาชิกที่มีรหัสเดาง่ายๆ และสามารถเข้าควบคุมสิทธิ์ผู้เรียนได้ทันที
</div>
</div>
<div style="background: rgba(255,255,255,0.01); border: 1px solid rgba(255,255,255,0.04); border-radius: 8px; padding: 14px; text-align: center;">
<div style="font-size: 0.72rem; color: #94a3b8; margin-bottom: 12px; font-weight: bold; text-transform: uppercase;">📊 Graphic: Authentication Failure</div>
<svg viewBox="0 0 400 150" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #030408; border-radius: 8px;">
<g transform="translate(30, 50)">
<circle cx="15" cy="8" r="6" fill="#ef4444"/>
<path d="M5,22 C5,14 25,14 25,22 Z" fill="#ef4444"/>
<text x="15" y="34" fill="#fca5a5" font-size="7" font-family="sans-serif" text-anchor="middle">Attacker</text>
</g>
<line x1="70" y1="75" x2="160" y2="75" stroke="#ef4444" stroke-width="1.5"/>
<text x="115" y="66" fill="#fca5a5" font-size="7" font-family="monospace" text-anchor="middle">Try "123456"</text>
<g transform="translate(170, 35)">
<rect x="0" y="0" width="90" height="80" rx="3" fill="#0f172a" stroke="#00f0ff" stroke-width="1.5"/>
<text x="45" y="20" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Logins</text>
<text x="45" y="45" fill="#ef4444" font-size="6" font-family="sans-serif" text-anchor="middle">No Lock limit</text>
<text x="45" y="65" fill="#f97316" font-size="6" font-family="sans-serif" text-anchor="middle">Weak pass ok</text>
</g>
<line x1="265" y1="75" x2="315" y2="75" stroke="#34d399" stroke-width="1.5"/>
<g transform="translate(330, 55)">
<circle cx="15" cy="15" r="12" fill="#34d399"/>
<text x="15" y="19" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle">🔓</text>
<text x="15" y="38" fill="#34d399" font-size="7" font-family="sans-serif" text-anchor="middle">Hijacked</text>
</g>
</svg>
</div>
</div>
</div>

<!-- A08 -->
<div class="owasp-card">
<div>
<div style="font-size: 1.05rem; font-weight: bold; color: #00f0ff; margin-bottom: 2px;">A08:2025 - Software and Data Integrity Failures (ความล้มเหลวด้านความสมบูรณ์ของซอฟต์แวร์)</div>
<div style="margin: 4px 0 10px 0; display: flex; align-items: center; gap: 8px;">
  <span style="font-size: 0.72rem; color: #94a3b8; font-weight: bold;">ระดับความรุนแรง:</span>
  <div style="flex-grow: 1; height: 6px; background: rgba(255,255,255,0.05); border-radius: 3px; overflow: hidden; max-width: 120px;">
    <div style="width: 80%; height: 100%; background: linear-gradient(90deg, #f97316, #eab308); box-shadow: 0 0 6px #f97316;"></div>
  </div>
  <span style="font-size: 0.7rem; color: #f97316; font-weight: 800; text-shadow: 0 0 4px rgba(249,115,22,0.4);">HIGH (8.0/10)</span>
</div>
<div style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.6;">
<strong style="color: #ffffff;">🔴 ปัญหาที่เกิดขึ้น (Occurs when):</strong>
การขาดการตรวจสอบความถูกต้อง (Verification) ของข้อมูลผู้ใช้งานหรือส่วนต่อขยายอัปเดตระบบก่อนที่จะทำการประมวลผลจริง<br>
<strong style="color: #ffffff;">💀 ผลกระทบระดับอันตราย (Can lead to):</strong>
ถูกลักลอบโจรกรรมส่งมัลแวร์ไปติดตั้งแฝงผ่านระบบอัตโนมัติของตัวเว็บบิวด์<br>
<strong style="color: #ffffff;">📝 ตัวอย่างเคสที่พบ (Examples):</strong>
- นำเข้าไลบรารีหรือโมดูลเสริมของบุคคลภายนอก (Third-party) ที่ไม่ได้ลงลายมือชื่อดิจิทัลรับรอง<br>
- การปลดปล่อยระบบส่งต่อวัตถุข้อมูลโดยไม่ลงนามรับรองความปลอดภัย (Insecure Deserialization)<br>
<strong style="color: #ffffff;">🔍 สถานการณ์จำลอง (Scenario):</strong>
ช่องทางอัปเกรดอัตโนมัติ (Update server) ขององค์กรไม่ได้ลงลายมือชื่อยืนยัน แฮกเกอร์แอบปลอมไฟล์อัปเกรดและส่งต่อมัลแวร์ขึ้นเซิร์ฟเวอร์หลักของแอปพลิเคชัน ทำให้หน้าหลักทำงานผิดเพี้ยนและเผยแพร่ข้อมูลผู้ใช้ออกไป
</div>
</div>
<div style="background: rgba(255,255,255,0.01); border: 1px solid rgba(255,255,255,0.04); border-radius: 8px; padding: 14px; text-align: center;">
<div style="font-size: 0.72rem; color: #94a3b8; margin-bottom: 12px; font-weight: bold; text-transform: uppercase;">📊 Graphic: Integrity Failure</div>
<svg viewBox="0 0 400 150" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #030408; border-radius: 8px;">
<g transform="translate(20, 50)">
<rect x="0" y="0" width="85" height="40" rx="3" fill="#0f172a" stroke="#3b82f6" stroke-width="1.5"/>
<text x="42" y="24" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">Firmware package</text>
</g>
<line x1="110" y1="70" x2="200" y2="70" stroke="#ef4444" stroke-width="1.5"/>
<text x="155" y="62" fill="#ef4444" font-size="6" font-family="monospace" text-anchor="middle">No signature check</text>
<g transform="translate(210, 50)">
<rect x="0" y="0" width="85" height="40" rx="3" fill="#0f172a" stroke="#ef4444" stroke-width="1.5"/>
<text x="42" y="24" fill="#fca5a5" font-size="8" font-family="sans-serif" text-anchor="middle">Run Firmware</text>
</g>
<line x1="300" y1="70" x2="330" y2="70" stroke="#ef4444" stroke-width="1.5"/>
<circle cx="345" cy="70" r="10" fill="#ef4444"/>
<text x="345" y="73" fill="#ffffff" font-size="8" font-family="sans-serif" text-anchor="middle">☠️</text>
</svg>
</div>
</div>
</div>

<!-- A09 -->
<div class="owasp-card">
<div>
<div style="font-size: 1.05rem; font-weight: bold; color: #00f0ff; margin-bottom: 2px;">A09:2025 - Security Logging and Monitoring Failures (ความล้มเหลวในการบันทึกและเฝ้าระวัง)</div>
<div style="margin: 4px 0 10px 0; display: flex; align-items: center; gap: 8px;">
  <span style="font-size: 0.72rem; color: #94a3b8; font-weight: bold;">ระดับความรุนแรง:</span>
  <div style="flex-grow: 1; height: 6px; background: rgba(255,255,255,0.05); border-radius: 3px; overflow: hidden; max-width: 120px;">
    <div style="width: 75%; height: 100%; background: linear-gradient(90deg, #3b82f6, #f97316); box-shadow: 0 0 6px #3b82f6;"></div>
  </div>
  <span style="font-size: 0.7rem; color: #3b82f6; font-weight: 800; text-shadow: 0 0 4px rgba(59,130,246,0.4);">MEDIUM / HIGH (7.5/10)</span>
</div>
<div style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.6;">
<strong style="color: #ffffff;">🔴 ปัญหาที่เกิดขึ้น (Occurs when):</strong>
เซิร์ฟเวอร์และแอปพลิเคชันไม่ได้จัดเก็บบันทึก (Logs) เหตุการณ์สำคัญ หรือไม่มีการแจ้งเตือนทันเวลาเมื่อระบบเกิดพฤติกรรมผิดสังเกต<br>
<strong style="color: #ffffff;">💀 ผลกระทบระดับอันตราย (Can lead to):</strong>
นักโจมตีแฝงตัวอยู่ในเครือข่ายภายในได้นานหลายสัปดาห์หรือหลายเดือนโดยที่แอดมินไม่รู้ตัว<br>
<strong style="color: #ffffff;">📝 ตัวอย่างเคสที่พบ (Examples):</strong>
- ไม่มีบันทึกเมื่อรหัสผ่านล็อกอินแอดมินผิดพลาด (Failed login attempts)<br>
- ไม่มีการเก็บล็อกการเข้าใช้งานฟังก์ชันจัดการข้อมูลส่วนบุคคลของระบบหลังบ้าน<br>
<strong style="color: #ffffff;">🔍 สถานการณ์จำลอง (Scenario):</strong>
แฮกเกอร์ใช้เวลา 3 สัปดาห์ในการรันบอทสแกนและลองเดารหัสผ่านเพื่อเข้าใช้งาน API หลังบ้าน เนื่องจากไม่มีระบบบันทึกความล้มเหลวในการเชื่อมต่อ ทำให้ผู้โจมตีทำงานได้อย่างอิสระโดยไม่สะดุดการตรวจเช็คของเซิร์ฟเวอร์
</div>
</div>
<div style="background: rgba(255,255,255,0.01); border: 1px solid rgba(255,255,255,0.04); border-radius: 8px; padding: 14px; text-align: center;">
<div style="font-size: 0.72rem; color: #94a3b8; margin-bottom: 12px; font-weight: bold; text-transform: uppercase;">📊 Graphic: Logging Failure</div>
<svg viewBox="0 0 400 150" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #030408; border-radius: 8px;">
<g transform="translate(30, 50)">
<circle cx="15" cy="8" r="6" fill="#ef4444"/>
<path d="M5,22 C5,14 25,14 25,22 Z" fill="#ef4444"/>
<text x="15" y="34" fill="#fca5a5" font-size="7" font-family="sans-serif" text-anchor="middle">Attacker</text>
</g>
<line x1="70" y1="75" x2="160" y2="75" stroke="#ef4444" stroke-width="1.5"/>
<text x="115" y="66" fill="#fca5a5" font-size="7" font-family="monospace" text-anchor="middle">Slow scans (3 weeks)</text>
<g transform="translate(170, 45)">
<rect x="0" y="0" width="110" height="60" rx="3" fill="#0f172a" stroke="#00f0ff" stroke-width="1.5"/>
<text x="55" y="20" fill="#cbd5e1" font-size="8" font-family="sans-serif" text-anchor="middle">API Server</text>
<rect x="15" y="30" width="80" height="20" rx="2" fill="#1e293b" stroke="#475569"/>
<text x="55" y="42" fill="#475569" font-size="6" font-family="monospace" text-anchor="middle">Logs: disabled</text>
</g>
<line x1="285" y1="75" x2="330" y2="75" stroke="#34d399" stroke-width="1.5"/>
<text x="350" y="80" fill="#34d399" font-size="14" font-family="sans-serif" text-anchor="middle">👻</text>
<text x="350" y="98" fill="#94a3b8" font-size="7" font-family="sans-serif" text-anchor="middle">Undetected</text>
</svg>
</div>
</div>
</div>

<!-- A10 -->
<div class="owasp-card">
<div>
<div style="font-size: 1.05rem; font-weight: bold; color: #00f0ff; margin-bottom: 2px;">A10:2025 - Mishandling of Exceptional Conditions (การจัดการข้อยกเว้นไม่ปลอดภัย)</div>
<div style="margin: 4px 0 10px 0; display: flex; align-items: center; gap: 8px;">
  <span style="font-size: 0.72rem; color: #94a3b8; font-weight: bold;">ระดับความรุนแรง:</span>
  <div style="flex-grow: 1; height: 6px; background: rgba(255,255,255,0.05); border-radius: 3px; overflow: hidden; max-width: 120px;">
    <div style="width: 78%; height: 100%; background: linear-gradient(90deg, #3b82f6, #f97316); box-shadow: 0 0 6px #3b82f6;"></div>
  </div>
  <span style="font-size: 0.7rem; color: #3b82f6; font-weight: 800; text-shadow: 0 0 4px rgba(59,130,246,0.4);">MEDIUM / HIGH (7.8/10)</span>
</div>
<div style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.6;">
<strong style="color: #ffffff;">🔴 ปัญหาที่เกิดขึ้น (Occurs when):</strong>
แอปพลิเคชันหลังบ้านตอบรับหรือดักพารามิเตอร์ผิดสังเกต (Exceptions) ในทิศทางที่ไม่ถูกต้อง ส่งผลให้กระบวนการเช็คความมั่นคงปลอดภัยหยุดชะงัก<br>
<strong style="color: #ffffff;">💀 ผลกระทบระดับอันตราย (Can lead to):</strong>
การถูกข้ามสิทธิ์การยืนยันตัวตน (Authentication Bypass), หรือทำให้ระบบเข้าสู่สถานะไม่เสถียรที่เอื้อต่อการโจรกรรม<br>
<strong style="color: #ffffff;">📝 ตัวอย่างเคสที่พบ (Examples):</strong>
- ระบบตรวจพบข้อผิดพลาดไฟล์ขาดหาย แต่กลับรันคำสั่งดำเนินการต่อโดยข้ามขั้นตอนยื่นคำร้องตรวจสอบสิทธิ์ (CWE-288)<br>
- การล้มเหลวในการจัดกลุ่ม NullPointerException นำไปสู่การ Bypass เงื่อนไขหลัก<br>
<strong style="color: #ffffff;">🔍 สถานการณ์จำลอง (Scenario):</strong>
แฮกเกอร์ส่งอินพุตที่เป็นค่าว่างหรือ Null ในฟิลด์ข้อมูลสิทธิ์ความปลอดภัย ตรรกะของโปรแกรมตรวจสอบขัดข้องและสร้าง Exception แต่เนื่องจากโค้กดักบกพร่อง มันแทนที่จะหยุดกระบวนการ กลับสั่งการข้ามสิทธิ์และพาเหยื่อเข้าใช้งานแดชบอร์ดแอดมินทันที
</div>
</div>
<div style="background: rgba(255,255,255,0.01); border: 1px solid rgba(255,255,255,0.04); border-radius: 8px; padding: 14px; text-align: center;">
<div style="font-size: 0.72rem; color: #94a3b8; margin-bottom: 12px; font-weight: bold; text-transform: uppercase;">📊 Graphic: Exception Bypass</div>
<svg viewBox="0 0 400 150" style="width: 100%; height: auto; display: block; margin: 0 auto; background: #030408; border-radius: 8px;">
<g transform="translate(30, 50)">
<circle cx="15" cy="8" r="6" fill="#ef4444"/>
<path d="M5,22 C5,14 25,14 25,22 Z" fill="#ef4444"/>
<text x="15" y="34" fill="#fca5a5" font-size="7" font-family="sans-serif" text-anchor="middle">Attacker</text>
</g>
<line x1="70" y1="75" x2="150" y2="75" stroke="#ef4444" stroke-width="1.5"/>
<text x="110" y="66" fill="#fca5a5" font-size="6" font-family="monospace" text-anchor="middle">Send Null input</text>
<g transform="translate(160, 45)">
<rect x="0" y="0" width="110" height="60" rx="3" fill="#0f172a" stroke="#00f0ff" stroke-width="1.5"/>
<text x="55" y="20" fill="#cbd5e1" font-size="7" font-family="sans-serif" text-anchor="middle">Auth Process</text>
<text x="55" y="45" fill="#ef4444" font-size="6" font-family="monospace" text-anchor="middle">[Internal Exception]</text>
</g>
<line x1="275" y1="75" x2="315" y2="75" stroke="#34d399" stroke-width="1.5"/>
<g transform="translate(325, 55)">
<circle cx="15" cy="15" r="12" fill="#34d399"/>
<text x="15" y="19" fill="#ffffff" font-size="10" font-family="sans-serif" text-anchor="middle">✔️</text>
<text x="15" y="38" fill="#34d399" font-size="7" font-family="sans-serif" text-anchor="middle">Bypassed</text>
</g>
</svg>
</div>
</div>
</div>

</div>

---

### 🛠️ เครื่องมือแกะรหัสหน้าเว็บ (Web Page Source Inspections)
นักทดสอบระบบมักกดใช้ปุ่ม F12 เพื่อเรียกใช้เครื่องมือช่วยเหลือในการวิเคราะห์คุณลักษณะภายใน:

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin: 1.5rem auto;">
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.25);">
<strong style="color: #00f0ff; display: block; margin-bottom: 6px; font-size: 0.95rem;">📄 Elements</strong>
<span style="color: #cbd5e1; font-size: 0.8rem; line-height: 1.5;">ตรวจสอบโครงสร้าง HTML เพื่อดัดแปลงพารามิเตอร์ลับที่นักพัฒนาซ่อนไว้ เช่น ปุ่มแก้ไขราคา หรือปุ่มสิทธิ์</span>
</div>
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.25);">
<strong style="color: #00f0ff; display: block; margin-bottom: 6px; font-size: 0.95rem;">💻 Console</strong>
<span style="color: #cbd5e1; font-size: 0.8rem; line-height: 1.5;">หน้ารันคำสั่งสคริปต์สด ช่วยทดสอบคำสั่งการทำงานหรือพิมพ์ข้อความดักจับตัวแปรเซสชันปัจจุบัน</span>
</div>
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 10px; padding: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.25);">
<strong style="color: #00f0ff; display: block; margin-bottom: 6px; font-size: 0.95rem;">💾 Application</strong>
<span style="color: #cbd5e1; font-size: 0.8rem; line-height: 1.5;">ใช้ตรวจสอบและดึงรายละเอียดที่เครื่อง Client เก็บสะสมไว้ เช่น คุกกี้เซสชัน บันทึก local storage</span>
</div>
</div>

---

### 🍪 วิเคราะห์คุณลักษณะ HTTP Cookies & Directory Traversal
<div style="background: rgba(6,182,212,0.04); border: 1px solid rgba(6,182,212,0.25); border-radius: 12px; padding: 20px; margin: 1.5rem auto; box-shadow: 0 4px 15px rgba(6,182,212,0.05);">
<h4 style="margin: 0 0 10px 0; font-size: 1rem; color: #06b6d4; font-weight: bold;">🔑 คุณสมบัติและจุดระวังความมั่นคงปลอดภัยบนบราวเซอร์</h4>
<p style="margin: 0; font-size: 0.84rem; color: #cbd5e1; line-height: 1.6;">
- <strong>HttpOnly Cookie Attribute</strong>: ช่วยปิดช่องโหว่ความมั่นคงปลอดภัย โดยบังคับไม่ให้สคริปต์ JavaScript โคลนหรือขโมยคุกกี้สำคัญผ่านการยิง XSS<br>
- <strong>Secure Attribute</strong>: บังคับการส่งต่อคุกกี้ผ่านเฉพาะช่องทางเข้ารหัส HTTPS เท่านั้น<br>
- <strong>Directory Traversal</strong>: ช่องโหว่แฝงคำสั่งถอยหลังพาธระบบปฏิบัติการโฮสต์หลังบ้าน (<code style="color: #00f0ff;">../../etc/passwd</code>) เพื่อลักลอบอ่านไฟล์เป้าหมาย<br>
- <strong>Robots.txt</strong>: ไฟล์แนะนำบอตดัชนี แต่สัญลักษณ์และรายชื่อไดเรกทอรีมักระบุพิกัดโฟลเดอร์ส่วนตัว แฮกเกอร์จึงนิยมเปิดสืบข้อมูลเป็นที่แรก
</p>
</div>"""

val177_1 = """### 💻 HTTP Headers Diagnostic Sandbox (จำลองวิเคราะห์โครงสร้างข้อมูลเว็บ)

คลิกหัวข้อด้านซ้ายมือเพื่อจำลองวิเคราะห์โครงสร้าง และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อตรวจสอบทราฟฟิกข้อมูล:

<style type="text/css">
.w-sandbox-main { display: flex !important; gap: 20px !important; margin: 1.5rem auto !important; max-width: 1000px !important; }
.w-sandbox-nav { width: 220px !important; display: flex !important; flex-direction: column !important; gap: 8px !important; flex-shrink: 0 !important; }
.w-nav-item { background: rgba(255, 255, 255, 0.02) !important; border: 1px solid rgba(255, 255, 255, 0.06) !important; border-radius: 6px !important; padding: 10px 14px !important; color: #cbd5e1 !important; text-align: left !important; cursor: pointer !important; font-size: 0.78rem !important; transition: all 0.2s !important; }
.w-sandbox-nav:hover, .w-nav-item.active { border-color: #00f0ff !important; color: #ffffff !important; background: rgba(0, 240, 255, 0.05) !important; }
.w-nav-item.active { font-weight: 700 !important; box-shadow: 0 0 8px rgba(0, 240, 255, 0.15) !important; }
.w-sandbox-panels { flex-grow: 1 !important; }
.w-sand-panel { background: #05070f !important; border: 1px solid rgba(255, 255, 255, 0.08) !important; border-radius: 10px !important; padding: 20px !important; box-shadow: 0 8px 24px rgba(0,0,0,0.45) !important; }
</style>
<div class="w-sandbox-main">
<div class="w-sandbox-nav">
<button id="nav-item-httpget" class="w-nav-item active">1. Send HTTP GET</button>
<button id="nav-item-httppost" class="w-nav-item">2. Send HTTP POST</button>
</div>
<div class="w-sandbox-panels">
<div id="panel-httpget" class="w-sand-panel" style="display: block;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>1. HTTP GET Request Method</span>
<span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(0,240,255,0.08); border: 1px solid rgba(0,240,255,0.2); color: #00f0ff; font-family: monospace;">HTTP Client</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #00f0ff; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">GET /index.php HTTP/1.1
Host: ctf.rpca.ac.th
User-Agent: Mozilla/5.0
Accept: text/html
Cookie: session_id=abc123xyz</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button id="btn-run-get" style="background: rgba(0,240,255,0.1); border: 1px solid rgba(0,240,255,0.3); border-radius: 4px; color: #00f0ff; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700; transition: all 0.15s;">▶ Run Simulation</button>
</div>
<div id="term-httpget" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 90px;">
<span style="color: #3ddc84;">client$</span> [กดปุ่ม Run Simulation เพื่อส่ง Request]
</div>
</div>
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 16px; font-size: 0.83rem; color: #cbd5e1; line-height: 1.65;">
<h5 style="margin: 0 0 8px; font-size: 0.85rem; color: #fbbf24; font-weight: bold;">⚙️ Command Description</h5>
<p style="margin: 0;">เมธอด GET ใช้เพื่อดึงหน้าเพจขึ้นมาแสดงผล โดยบราวเซอร์ส่ง Cookie ยืนยันสิทธิ์เซสชันแอดมิน</p>
</div>
</div>
<div id="panel-httppost" class="w-sand-panel" style="display: none;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>2. HTTP POST Request Method</span>
<span style="font-size: 0.65rem; padding: 2px 8px; border-radius: 4px; background: rgba(0,240,255,0.08); border: 1px solid rgba(0,240,255,0.2); color: #00f0ff; font-family: monospace;">HTTP Client</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #00f0ff; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.2); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.02);">POST /login.php HTTP/1.1
Host: ctf.rpca.ac.th
Content-Type: application/x-www-form-urlencoded
Content-Length: 29

username=admin&password=secret</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button id="btn-run-post" style="background: rgba(0,240,255,0.1); border: 1px solid rgba(0,240,255,0.3); border-radius: 4px; color: #00f0ff; font-size: 0.68rem; padding: 3px 8px; cursor: pointer; font-family: monospace; font-weight: 700; transition: all 0.15s;">▶ Run Simulation</button>
</div>
<div id="term-httppost" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 90px;">
<span style="color: #3ddc84;">client$</span> [กดปุ่ม Run Simulation เพื่อส่ง Request]
</div>
</div>
<div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 8px; padding: 16px; font-size: 0.83rem; color: #cbd5e1; line-height: 1.65;">
<h5 style="margin: 0 0 8px; font-size: 0.85rem; color: #fbbf24; font-weight: bold;">⚙️ Command Description</h5>
<p style="margin: 0;">เมธอด POST ใช้เพื่อส่งข้อมูลชุดใหญ่ที่เป็นความลับ (เช่น รหัสผ่าน) ไปประมวลผลบนเซิร์ฟเวอร์โดยไม่โชว์บน URL</p>
</div>
</div>
</div>
</div>
<script>
// Define simulation behavior globally
window.startWebSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span style="color:#64748b;">client$</span> <span style="color:#ffffff; font-weight:bold;">Sending HTTP Request...</span>\\n[.] Accessing remote port 80/443\\n[.] Reading Response Headers...';
  setTimeout(() => {
    if (itemKey === 'httpget') {
      term.innerHTML = '<span style="color:#64748b;">client$</span> <span style="color:#3ddc84; font-weight:bold;">HTTP/1.1 200 OK</span>\\nServer: Apache/2.4.41 (Ubuntu)\\nContent-Type: text/html\\nContent-Length: 1042\\n\\n&lt;html&gt;&lt;body&gt;&lt;h1&gt;Welcome to RPCA Cyber Club&lt;/h1&gt;&lt;/body&gt;&lt;/html&gt;';
    } else if (itemKey === 'httppost') {
      term.innerHTML = '<span style="color:#64748b;">client$</span> <span style="color:#fbbf24; font-weight:bold;">HTTP/1.1 302 Found</span>\\nServer: Apache/2.4.41 (Ubuntu)\\nLocation: /dashboard.php\\nSet-Cookie: session_id=abc123xyz; Path=/; HttpOnly\\n\\n[+] Redirecting to dashboard...';
    }
  }, 1000);
}

// Bind events globally using Event Delegation
document.addEventListener('click', function(e) {
  const tabGet = e.target.closest('#nav-item-httpget');
  if (tabGet) {
    const tabPost = document.getElementById('nav-item-httppost');
    const panelGet = document.getElementById('panel-httpget');
    const panelPost = document.getElementById('panel-httppost');
    if (panelGet && panelPost) {
      panelGet.style.display = 'block';
      panelPost.style.display = 'none';
      tabGet.classList.add('active');
      if (tabPost) tabPost.classList.remove('active');
    }
    return;
  }

  const tabPost = e.target.closest('#nav-item-httppost');
  if (tabPost) {
    const tabGet = document.getElementById('nav-item-httpget');
    const panelGet = document.getElementById('panel-httpget');
    const panelPost = document.getElementById('panel-httppost');
    if (panelGet && panelPost) {
      panelGet.style.display = 'none';
      panelPost.style.display = 'block';
      tabPost.classList.add('active');
      if (tabGet) tabGet.classList.remove('active');
    }
    return;
  }

  const runGet = e.target.closest('#btn-run-get');
  if (runGet) {
    window.startWebSim('httpget');
    return;
  }

  const runPost = e.target.closest('#btn-run-post');
  if (runPost) {
    window.startWebSim('httppost');
    return;
  }
});
</script>"""

val177_2 = """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการบันทึกความสำเร็จและปลดล็อกปุ่มบทเรียนถัดไป:

<div class="row align-items-center" style="margin:1.5rem auto; max-width:980px;"><div class="col-md-8"><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">1. พอร์ตบริการเครือข่ายมาตรฐานสำหรับการเข้าถึงหน้าเว็บเพจแบบเข้ารหัสปลอดภัย (HTTPS) คือพอร์ตใด?</p><div class="options-container" data-q="q1"><label class="w-quiz-option"><input type="radio" name="web_port" value="80" data-hash="false">Port 80</label><label class="w-quiz-option"><input type="radio" name="web_port" value="443" data-hash="868846c4f8d48e0259b38466e3fb0c4b26090cfa4b6f1f457788be4fbf0fa8fb">Port 443 (HTTPS)</label><label class="w-quiz-option"><input type="radio" name="web_port" value="22" data-hash="false">Port 22</label><label class="w-quiz-option"><input type="radio" name="web_port" value="8080" data-hash="false">Port 8080</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div><div class="question-cell p-4 mb-3" style="background:rgba(255,255,255,0.015); border:1px solid rgba(255,255,255,0.04); border-radius:8px;"><p class="text-white mb-3" style="font-size:0.88rem; font-weight:600;">2. โครงการมาตรฐานสากลด้านความปลอดภัยเว็บที่จัดอันดับ 10 ความเสี่ยงสูงสุดของเว็บแอปพลิเคชันคือองค์กรใด?</p><div class="options-container" data-q="q2"><label class="w-quiz-option"><input type="radio" name="owasp_q" value="W3C" data-hash="false">W3C</label><label class="w-quiz-option"><input type="radio" name="owasp_q" value="OWASP" data-hash="3367b846e49226cb100416972049d5bf59892cfa76e4a2cdbbf24c56e2978000">OWASP</label><label class="w-quiz-option"><input type="radio" name="owasp_q" value="SANS" data-hash="false">SANS Institute</label><label class="w-quiz-option"><input type="radio" name="owasp_q" value="MITRE" data-hash="false">MITRE Corporation</label></div><button class="btn btn-warning px-4 mt-2 text-dark font-weight-bold" type="button" onclick="verifyMultipleChoice(this)"><i class="fas fa-paper-plane mr-1"></i> Submit</button><div class="feedback-msg mt-2" style="display:none; font-size:0.8rem; border-radius:4px; padding:6px 12px;"></div></div></div><div class="col-md-4 text-center"><div class="p-4" style="background:rgba(255,255,255,0.01); border:1px solid rgba(255,255,255,0.03); border-radius:12px; min-height:220px; display:flex; flex-direction:column; justify-content:center; align-items:center;"><span class="text-muted d-block mb-3" style="font-size:0.75rem; text-transform:uppercase; letter-spacing:0.1em;">Lesson Progress</span><div class="neon-gauge-container"><svg class="neon-gauge" viewBox="0 0 36 36"><path class="neon-gauge-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><path class="neon-gauge-fill" id="lesson-gauge-fill" stroke-dasharray="0, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" /><text x="18" y="20.35" class="neon-gauge-text" id="lesson-gauge-text">0%</text></svg></div><span id="lesson-status-txt" class="mt-3 d-block text-muted" style="font-size:0.78rem;">โปรดตอบคำถามให้ครบ 2 ข้อ</span></div></div></div>
<style>
.neon-gauge-container {position:relative; width:120px; height:120px;}
.neon-gauge {width:100%; height:100%;}
.neon-gauge-bg {fill:none; stroke:rgba(255,255,255,0.05); stroke-width:2.8;}
.neon-gauge-fill {fill:none; stroke:#00f0ff; stroke-width:2.8; stroke-linecap:round; transition:stroke-dasharray 0.5s ease, stroke 0.5s ease; filter:drop-shadow(0 0 5px rgba(0,240,255,0.5));}
.neon-gauge-text {fill:#ffffff; font-family:\'JetBrains Mono\',monospace; font-size:9px; font-weight:800; text-anchor:middle; filter:drop-shadow(0 0 2px rgba(255,255,255,0.3));}
</style>
<script>
const lessonKey = 'solved_lesson_177';
function getSavedSolves() { try { return JSON.parse(localStorage.getItem(lessonKey) || '[]'); } catch(e) { return []; } }
function updateLocalProgress() {
  const solved = getSavedSolves();
  const total = 2;
  const percent = Math.round((solved.length / total) * 100);
  const fill = document.getElementById('lesson-gauge-fill');
  const text = document.getElementById('lesson-gauge-text');
  const status = document.getElementById('lesson-status-txt');
  if (fill) fill.setAttribute('stroke-dasharray', `${percent}, 100`);
  if (text) text.textContent = `${percent}%`;
  if (solved.length === total) {
    if (fill) fill.style.stroke = '#3ddc84';
    if (status) status.innerHTML = '<span style="color:#3ddc84; font-weight:bold;"><i class="fas fa-check-circle mr-1"></i> ปลดล็อกบทเรียนถัดไปแล้ว</span>';
  } else {
    if (fill) fill.style.stroke = '#00f0ff';
    if (status) status.textContent = `ทำเสร็จแล้ว ${solved.length}/${total} ข้อ`;
  }
}
document.addEventListener('click', function(e) {
  const label = e.target.closest('.w-quiz-option');
  if (label) {
    const container = label.closest('.options-container');
    if (container) {
      container.querySelectorAll('.w-quiz-option').forEach(opt => opt.classList.remove('selected'));
      label.classList.add('selected');
      const radio = label.querySelector('input[type="radio"]');
      if (radio) radio.checked = true;
    }
  }
});
window.verifyMultipleChoice = function(button) {
  const cell = button.closest('.question-cell');
  const selectedRadio = cell.querySelector('input[type="radio"]:checked');
  const feedback = cell.querySelector('.feedback-msg');
  if (!selectedRadio) {
    feedback.className = "feedback-msg mt-2 alert-warning py-1.5 px-3 text-dark";
    feedback.innerHTML = '<i class="fas fa-exclamation-triangle mr-1"></i> กรุณาเลือกคำตอบ';
    feedback.style.setProperty('display', 'block', 'important');
    return;
  }
  const hashVal = selectedRadio.getAttribute('data-hash');
  if (hashVal !== 'false') {
    feedback.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
    feedback.innerHTML = '<i class="fas fa-check-circle mr-1"></i> คำตอบถูกต้อง!';
    feedback.style.setProperty('display', 'block', 'important');
    cell.querySelectorAll('input[type="radio"]').forEach(r => r.disabled = true);
    cell.querySelectorAll('.w-quiz-option').forEach(opt => opt.style.pointerEvents = 'none');
    button.disabled = true;
    const solved = getSavedSolves();
    if (!solved.includes(hashVal)) {
      solved.push(hashVal);
      localStorage.setItem(lessonKey, JSON.stringify(solved));
    }
    updateLocalProgress();
  } else {
    feedback.className = "feedback-msg mt-2 alert-danger py-1.5 px-3 text-white bg-danger border-0";
    feedback.innerHTML = '<i class="fas fa-times-circle mr-1"></i> คำตอบไม่ถูกต้อง ลองใหม่!';
    feedback.style.setProperty('display', 'block', 'important');
  }
}
setTimeout(() => {
  const solved = getSavedSolves();
  document.querySelectorAll('.options-container').forEach(container => {
    container.querySelectorAll('input[type="radio"]').forEach(radio => {
      const hash = radio.getAttribute('data-hash');
      if (solved.includes(hash)) {
        radio.checked = true;
        const label = radio.closest('.w-quiz-option');
        if (label) label.classList.add('selected');
        container.querySelectorAll('input[type="radio"]').forEach(r => r.disabled = true);
        container.querySelectorAll('.w-quiz-option').forEach(opt => opt.style.pointerEvents = 'none');
        const cell = container.closest('.question-cell');
        if (cell) {
          const btn = cell.querySelector('button');
          if (btn) btn.disabled = true;
          const fb = cell.querySelector('.feedback-msg');
          if (fb) {
            fb.className = "feedback-msg mt-2 alert-success py-1.5 px-3 text-dark";
            fb.innerHTML = '<i class="fas fa-check-circle mr-1"></i> เรียบร้อยแล้ว';
            fb.style.setProperty('display', 'block', 'important');
          }
        }
      }
    });
  });
  updateLocalProgress();
}, 200);
</script>"""

save_lesson(177, val177_0, val177_1, val177_2)
ctx.pop()
