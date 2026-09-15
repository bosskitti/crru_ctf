import re

new_case_study_html = """<!-- ========================================================================= -->
<!-- CASE STUDY & REPORT DECODING: REAL RECON ON CRRU.AC.TH                  -->
<!-- ========================================================================= -->
<div style="background: #030712; border: 1px solid rgba(245, 158, 11, 0.35); border-radius: 14px; padding: 22px; margin-top: 24px; box-shadow: 0 12px 35px rgba(0,0,0,0.7);">

<!-- Header of Case Study -->
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; margin-bottom: 20px; padding-bottom: 14px; border-bottom: 1px solid rgba(255,255,255,0.08);">
<div style="display: flex; align-items: center; gap: 12px;">
<span style="font-size: 1.5rem;">🎯</span>
<div>
<h4 style="margin: 0; color: #fbbf24; font-size: 1.15rem; font-weight: 800;">
ถอดรหัสผลการสแกนระบบจริง: กรณีศึกษาประเมินความปลอดภัย CMS จากปฏิบัติการจริง (เป้าหมาย: crru.ac.th)
</h4>
<span style="color: #94a3b8; font-size: 0.8rem;">
วิเคราะห์ผลลัพธ์เชิงเทคนิคจากภาพการสแกนจริงบน Kali Linux ผ่าน 3 เครื่องมือมาตรฐาน (CMSeek, OWASP JoomScan และ WPScan) สู่แนวทางตั้งรับ
</span>
</div>
</div>
<span style="background: rgba(245, 158, 11, 0.15); color: #fde047; font-family: monospace; font-size: 0.75rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(245, 158, 11, 0.35);">
CASE STUDY &bull; REAL RECONNAISSANCE
</span>
</div>

<!-- ==================== SECTION 1: CMSEEK SCAN ==================== -->
<div style="margin-bottom: 24px; background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(0, 240, 255, 0.3); border-radius: 12px; padding: 18px;">
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 14px;">
<div style="color: #00f0ff; font-size: 0.95rem; font-weight: 800; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-cube"></i> ส่วนที่ 1: การตรวจจับเชิงลึกด้วย CMSeek (CMSeek Deepscan บน crru.ac.th)
</div>
<span style="background: rgba(0, 240, 255, 0.15); color: #7dd3fc; font-size: 0.7rem; font-family: monospace; padding: 2px 8px; border-radius: 4px; border: 1px solid rgba(0, 240, 255, 0.3);">
TOOL: CMSEEK (PYTHON3)
</span>
</div>

<div style="text-align: center; margin-bottom: 14px;">
<img src="/tutorials/static/uploads/cmseek_crru_annotated.png" alt="CMSeek Scan crru.ac.th Annotated" style="max-width: 100%; border-radius: 8px; border: 1px solid rgba(0, 240, 255, 0.3); box-shadow: 0 6px 25px rgba(0,0,0,0.7);" />
<div style="color: #94a3b8; font-size: 0.73rem; margin-top: 6px; font-style: italic;">
ภาพที่ 1.1: CMSeek ระบุ WordPress 7.1, ตรวจพบไฟล์ตกค้าง readme.html / license.txt และแจกแจงปลั๊กอิน 12 ตัว
</div>
</div>

<!-- 3 Callouts for CMSeek -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 10px;">
<div style="background: rgba(0,0,0,0.4); border-left: 3px solid #00f0ff; padding: 10px; border-radius: 6px;">
<strong style="color: #38bdf8; font-size: 0.78rem; display: block; margin-bottom: 4px;">🔴 จุดที่วง 1: CMS Detection &amp; Version</strong>
<span style="color: #cbd5e1; font-size: 0.74rem; line-height: 1.5; display: block;">
ตรวจจับได้ว่าเป้าหมายใช้ <code>WordPress</code> พร้อมระบุเลขเวอร์ชัน ช่วยให้แฮกเกอร์จำกัดขอบเขตชุดเครื่องมือโจมตีได้อย่างแม่นยำ
</span>
</div>
<div style="background: rgba(0,0,0,0.4); border-left: 3px solid #f59e0b; padding: 10px; border-radius: 6px;">
<strong style="color: #fbbf24; font-size: 0.78rem; display: block; margin-bottom: 4px;">🔴 จุดที่วง 2: Sensitive Information Leaks</strong>
<span style="color: #cbd5e1; font-size: 0.74rem; line-height: 1.5; display: block;">
พบไฟล์ <code>readme.html</code> และ <code>license.txt</code> ซึ่งมักถูกปล่อยทิ้งไว้ ช่วยยืนยันข้อมูลเวอร์ชันโดยไม่ต้องเดา
</span>
</div>
<div style="background: rgba(0,0,0,0.4); border-left: 3px solid #ef4444; padding: 10px; border-radius: 6px;">
<strong style="color: #f87171; font-size: 0.78rem; display: block; margin-bottom: 4px;">🔴 จุดที่วง 3: 12 Plugins Enumerated (จุดตาย!)</strong>
<span style="color: #cbd5e1; font-size: 0.74rem; line-height: 1.5; display: block;">
ตรวจพบปลั๊กอิน 12 ตัว เช่น <code>embedpress</code>, <code>jet-popup (v2.2.2)</code>, และ <code>elementor-pro</code> แฮกเกอร์จะนำเวอร์ชันปลั๊กอินไปเสิร์ชหาช่องโหว่ RCE / File Upload ทันที!
</span>
</div>
</div>
</div>

<!-- ==================== SECTION 2: OWASP JOOMSCAN ==================== -->
<div style="margin-bottom: 24px; background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 12px; padding: 18px;">
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 14px;">
<div style="color: #f87171; font-size: 0.95rem; font-weight: 800; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-crosshairs"></i> ส่วนที่ 2: การตรวจสอบช่องโหว่ด้วย OWASP JoomScan (เป้าหมายจริง: crru.ac.th)
</div>
<span style="background: rgba(239, 68, 68, 0.15); color: #fca5a5; font-size: 0.7rem; font-family: monospace; padding: 2px 8px; border-radius: 4px; border: 1px solid rgba(239, 68, 68, 0.3);">
TOOL: OWASP JOOMSCAN (PERL)
</span>
</div>

<!-- JoomScan Part 1 (FPD) -->
<div style="background: #020617; border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 10px; padding: 16px; margin-bottom: 18px;">
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 12px;">
<div style="color: #f87171; font-weight: 800; font-size: 0.88rem; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-radiation"></i> ภาพที่ 2.1: การตรวจจับ Version และช่องโหว่เผยพาธระบบจริง (Full Path Disclosure - FPD)
</div>
<span style="color: #fca5a5; font-size: 0.72rem; font-family: monospace; background: rgba(239, 68, 68, 0.15); padding: 2px 8px; border-radius: 4px;">HIGH RISK</span>
</div>

<div style="text-align: center; margin-bottom: 14px;">
<img src="/tutorials/static/uploads/joomscan_fpd_crru_annotated.png" alt="JoomScan FPD crru.ac.th Annotated" style="max-width: 100%; border-radius: 8px; border: 1px solid rgba(239, 68, 68, 0.4); box-shadow: 0 6px 25px rgba(0,0,0,0.7);" />
<div style="color: #94a3b8; font-size: 0.73rem; margin-top: 6px; font-style: italic;">
ภาพที่ 2.1: JoomScan ระบุ Version 7.1 และตรวจพบช่องโหว่ Full Path Disclosure ใน PSpellShell.php
</div>
</div>

<!-- Deep Dive into FPD & Version -->
<div style="background: rgba(239, 68, 68, 0.06); border: 1px solid rgba(239, 68, 68, 0.25); border-radius: 8px; padding: 12px;">
<div style="color: #f87171; font-size: 0.82rem; font-weight: 800; margin-bottom: 6px;">
⚡ ถอดรหัส 2 จุดสำคัญในภาพที่ 2.1 (ทำไมถึงอันตราย และแฮกเกอร์มองหาอะไร?):
</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 10px; margin-top: 8px;">
<div style="background: rgba(0,0,0,0.35); padding: 10px; border-radius: 6px; border-left: 3px solid #ef4444;">
<strong style="color: #f87171; font-size: 0.76rem; display: block; margin-bottom: 4px;">🔴 จุดที่วง 1: Detecting Version (7.1):</strong>
<span style="color: #94a3b8; font-size: 0.72rem; line-height: 1.45;">
<strong>คืออะไร:</strong> การทำ Version Fingerprinting ระบุเลขเวอร์ชันของระบบ<br/>
<strong>อันตรายอย่างไร:</strong> การรู้เลขเวอร์ชันเปรียบเสมือน <em>"การรู้รุ่นของแม่กุญแจ"</em> แฮกเกอร์จะนำเลขนี้ไปค้นหาในฐานข้อมูล <strong>CVE Details / Exploit-DB</strong> ทันที หากเป็นรุ่นที่มีประวัติช่องโหว่ RCE หรือ SQL Injection แฮกเกอร์จะยิงโค้ดเจาะสำเร็จรูปมายึดเซิร์ฟเวอร์ได้ทันทีโดยไม่ต้องเดา!
</span>
</div>
<div style="background: rgba(0,0,0,0.35); padding: 10px; border-radius: 6px; border-left: 3px solid #f59e0b;">
<strong style="color: #fbbf24; font-size: 0.76rem; display: block; margin-bottom: 4px;">🔴 จุดที่วง 2: Full Path Disclosure (FPD ใน PSpellShell.php):</strong>
<span style="color: #94a3b8; font-size: 0.72rem; line-height: 1.45;">
<strong>คืออะไร:</strong> สคริปต์แสดง Error Message คาย <strong>"Absolute Path (เส้นทางโฟลเดอร์จริงบนฮาร์ดดิสก์)"</strong> ออกมา<br/>
<strong>อันตรายอย่างไร:</strong> เป็นจิ๊กซอว์ชิ้นสำคัญที่สุดในการทำ <strong>SQL Injection (INTO OUTFILE)</strong> เพื่อเขียนไฟล์ Web Shell ลงดิสก์ และช่วยให้เจาะไฟล์ระบบผ่าน <strong>LFI (Local File Inclusion)</strong> ได้แม่นยำ 100% โดยไม่ต้องเดาจำนวน <code>../../</code>
</span>
</div>
</div>
</div>
</div>

<!-- JoomScan Part 2 (Admin & robots.txt) -->
<div style="background: #020617; border: 1px solid rgba(245, 158, 11, 0.25); border-radius: 10px; padding: 16px;">
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 12px;">
<div style="color: #fbbf24; font-weight: 800; font-size: 0.88rem; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-sitemap"></i> ภาพที่ 2.2: การตรวจพบ Admin Finder และข้อมูลรั่วไหลใน robots.txt
</div>
<span style="color: #94a3b8; font-size: 0.72rem; font-family: monospace;">ARTIFACT: REAL SCAN</span>
</div>

<div style="text-align: center; margin-bottom: 14px;">
<img src="/tutorials/static/uploads/joomscan_admin_robots_crru_annotated.png" alt="JoomScan Admin and robots.txt crru.ac.th Annotated" style="max-width: 100%; border-radius: 8px; border: 1px solid rgba(245, 158, 11, 0.3); box-shadow: 0 6px 25px rgba(0,0,0,0.7);" />
<div style="color: #94a3b8; font-size: 0.73rem; margin-top: 6px; font-style: italic;">
ภาพที่ 2.2: JoomScan ตรวจพบ Admin page (/administrator/) และพบไฟล์ robots.txt ที่เผยพาธ /wp-admin/ และ admin-ajax.php
</div>
</div>

<!-- 2 Callouts for JoomScan Part 2 -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 10px;">
<div style="background: rgba(0,0,0,0.4); border-left: 3px solid #fbbf24; padding: 10px; border-radius: 6px;">
<strong style="color: #fde047; font-size: 0.78rem; display: block; margin-bottom: 4px;">🔴 จุดที่วง 1: admin finder (/administrator/)</strong>
<span style="color: #cbd5e1; font-size: 0.74rem; line-height: 1.5; display: block;">
<strong>คืออะไร:</strong> ทางเข้าสู่ระบบของผู้ดูแล (Administrative Portal)<br/>
<strong>อันตรายอย่างไร:</strong> ประตูบานใหญ่ที่สุดของหลังบ้าน แฮกเกอร์จะเริ่มทำ <strong>Brute-force / Dictionary Attack</strong> หรือ <strong>Credential Stuffing</strong> ยิงใส่บัญชี <code>admin</code> ทันทีด้วย Hydra หากไม่ได้ตั้งรหัสผ่านซับซ้อนและไม่มี 2FA เว็บไซต์จะถูกยึดแบบเบ็ดเสร็จ
</span>
</div>
<div style="background: rgba(0,0,0,0.4); border-left: 3px solid #38bdf8; padding: 10px; border-radius: 6px;">
<strong style="color: #7dd3fc; font-size: 0.78rem; display: block; margin-bottom: 4px;">🔴 จุดที่วง 2: robots.txt found เผยพาธ /wp-admin/ &amp; admin-ajax.php</strong>
<span style="color: #cbd5e1; font-size: 0.74rem; line-height: 1.5; display: block;">
<strong>คืออะไร:</strong> ไฟล์นโยบาย Web Crawler ที่เปิดให้ทุกคนอ่านได้แบบสาธารณะ<br/>
<strong>อันตรายอย่างไร:</strong> เจ้าของเว็บมักเขียนบอกเองว่ามีโฟลเดอร์ลับอะไรซ่อนอยู่ กลายเป็น <em>"แผนที่ลายแทงสมบัติ" (Treasure Map)</em> สำหรับแฮกเกอร์ และเผย endpoint สำคัญอย่าง <code>admin-ajax.php</code> ที่มักมีช่องโหว่ปลั๊กอิน
</span>
</div>
</div>
</div>

</div>

<!-- ==================== SECTION 3: WPSCAN AUDIT ==================== -->
<div style="margin-bottom: 24px; background: rgba(15, 23, 42, 0.65); border: 1px solid rgba(59, 130, 246, 0.35); border-radius: 12px; padding: 18px;">
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 14px;">
<div style="color: #60a5fa; font-size: 0.95rem; font-weight: 800; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-shield-halved"></i> ส่วนที่ 3: การประเมินความปลอดภัย WordPress ด้วย WPScan (เป้าหมายจริง: crru.ac.th)
</div>
<span style="background: rgba(59, 130, 246, 0.15); color: #93c5fd; font-size: 0.7rem; font-family: monospace; padding: 2px 8px; border-radius: 4px; border: 1px solid rgba(59, 130, 246, 0.3);">
TOOL: WPSCAN (RUBY)
</span>
</div>

<!-- Intro note for WPScan audit -->
<div style="background: rgba(59, 130, 246, 0.08); border-left: 3px solid #3b82f6; border-radius: 6px; padding: 10px 14px; margin-bottom: 16px; font-size: 0.78rem; color: #cbd5e1; line-height: 1.55;">
<strong>💡 ภาพรวมการสแกนด้วย WPScan:</strong> คำสั่ง <code>wpscan --url https://crru.ac.th/</code> เป็นการส่งคำขอทดสอบ (Probe Requests) เพียง 32 ครั้ง ใช้เวลาสแกนสั้นเพียง 7 วินาที แต่สามารถดึงข้อมูลเบื้องลึกเกี่ยวกับสถาปัตยกรรมเซิร์ฟเวอร์ ช่องทาง API ที่เสี่ยงต่อการถูกเจาะรหัสผ่าน และช่องโหว่ประเภท DoS ออกมาได้อย่างแม่นยำ
</div>

<!-- WPScan Screenshot 1: Headers & Robots.txt -->
<div style="background: #020617; border: 1px solid rgba(59, 130, 246, 0.25); border-radius: 10px; padding: 16px; margin-bottom: 20px;">
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 12px;">
<div style="color: #93c5fd; font-weight: 800; font-size: 0.88rem; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-network-wired"></i> ภาพที่ 3.1: ข้อมูล HTTP Headers ของเซิร์ฟเวอร์ และพาธใน robots.txt
</div>
<span style="color: #94a3b8; font-size: 0.72rem; font-family: monospace;">ARTIFACT: SCREENSHOT 175755</span>
</div>

<div style="text-align: center; margin-bottom: 14px;">
<img src="/tutorials/static/uploads/wpscan_headers_robots_crru_annotated.png" alt="WPScan Headers & robots.txt Annotated" style="max-width: 100%; border-radius: 8px; border: 1px solid rgba(59, 130, 246, 0.3); box-shadow: 0 6px 25px rgba(0,0,0,0.7);" />
<div style="color: #94a3b8; font-size: 0.73rem; margin-top: 6px; font-style: italic;">
ภาพที่ 3.1: WPScan ตรวจจับเป้าหมาย IP 203.172.117.183, ระบุ LiteSpeed Web Server และดึงค่า robots.txt
</div>
</div>

<!-- 3 Callouts for Screenshot 1 -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 10px;">
<div style="background: rgba(0,0,0,0.4); border-left: 3px solid #3b82f6; padding: 10px; border-radius: 6px;">
<strong style="color: #60a5fa; font-size: 0.78rem; display: block; margin-bottom: 4px;">🔴 จุดที่วง 1: Target IP &amp; Command Line</strong>
<span style="color: #cbd5e1; font-size: 0.74rem; line-height: 1.5; display: block;">
สแกนเนอร์ระบุไอพีปลายทาง <code>[203.172.117.183]</code> ยืนยันว่าการสแกนเชื่อมต่อไปยังเซิร์ฟเวอร์จริงของมหาวิทยาลัย
</span>
</div>
<div style="background: rgba(0,0,0,0.4); border-left: 3px solid #f59e0b; padding: 10px; border-radius: 6px;">
<strong style="color: #fbbf24; font-size: 0.78rem; display: block; margin-bottom: 4px;">🔴 จุดที่วง 2: Server Fingerprint (LiteSpeed)</strong>
<span style="color: #cbd5e1; font-size: 0.74rem; line-height: 1.5; display: block;">
พบ <code>server: LiteSpeed</code> และ <code>x-litespeed-cache: hit</code> ชี้ชัดว่าใช้ LiteSpeed Web Server และเปิดแคชระดับเซิร์ฟเวอร์ พร้อมรองรับ HTTP/3 QUIC
</span>
</div>
<div style="background: rgba(0,0,0,0.4); border-left: 3px solid #ef4444; padding: 10px; border-radius: 6px;">
<strong style="color: #f87171; font-size: 0.78rem; display: block; margin-bottom: 4px;">🔴 จุดที่วง 3: robots.txt Leakage</strong>
<span style="color: #cbd5e1; font-size: 0.74rem; line-height: 1.5; display: block;">
เปิดเผยไดเรกทอรี <code>/wp-admin/</code> และสคริปต์ <code>admin-ajax.php</code> ซึ่งเป็นช่องทางรับคำขอ AJAX ที่แฮกเกอร์มักใช้ทดสอบช่องโหว่ปลั๊กอิน
</span>
</div>
</div>
</div>

<!-- WPScan Screenshot 2: XML-RPC, WP-Cron & Version -->
<div style="background: #020617; border: 1px solid rgba(239, 68, 68, 0.35); border-radius: 10px; padding: 16px; margin-bottom: 20px;">
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 12px;">
<div style="color: #f87171; font-weight: 800; font-size: 0.88rem; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-triangle-exclamation"></i> ภาพที่ 3.2: การเปิดใช้งาน XML-RPC, External WP-Cron และการตรวจจับเวอร์ชันผ่าน RSS
</div>
<span style="color: #fca5a5; font-size: 0.72rem; font-family: monospace; background: rgba(239, 68, 68, 0.15); padding: 2px 8px; border-radius: 4px;">HIGH SEVERITY</span>
</div>

<div style="text-align: center; margin-bottom: 14px;">
<img src="/tutorials/static/uploads/wpscan_xmlrpc_cron_version_crru_annotated.png" alt="WPScan XML-RPC, Cron & Version Annotated" style="max-width: 100%; border-radius: 8px; border: 1px solid rgba(239, 68, 68, 0.4); box-shadow: 0 6px 25px rgba(0,0,0,0.7);" />
<div style="color: #94a3b8; font-size: 0.73rem; margin-top: 6px; font-style: italic;">
ภาพที่ 3.2: WPScan ตรวจพบช่องโหว่ XML-RPC เปิดใช้งาน, WP-Cron ทำงานภายนอกได้ และพบ Version 7.1 ผ่าน RSS
</div>
</div>

<!-- 3 Detailed Callouts for Screenshot 2 -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 12px;">

<div style="background: rgba(239, 68, 68, 0.08); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 8px; padding: 12px;">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
<strong style="color: #f87171; font-size: 0.8rem;\">🔴 จุดที่ 1: XML-RPC Enabled (จุดตายวิกฤต!)</strong>
<span style="background: rgba(239,68,68,0.2); color:#fca5a5; font-size:0.65rem; font-family:monospace; padding:1px 5px; border-radius:3px;">CRITICAL</span>
</div>
<p style="margin: 0 0 8px; color: #cbd5e1; font-size: 0.74rem; line-height: 1.5;">
<strong>คืออะไร:</strong> ไฟล์ <code>xmlrpc.php</code> เป็นโพรโทคอลสื่อสารระยะไกลของ WordPress ที่ยังคงเปิดให้เข้าถึงได้โดยตรง
</p>
<div style="background: rgba(0,0,0,0.4); border-left: 3px solid #ef4444; padding: 8px; border-radius: 4px; font-size: 0.72rem; color: #fca5a5; line-height: 1.45;">
<strong>⚡ อันตรายอย่างไร:</strong><br/>
1. <strong>Brute-Force Amplification:</strong> ผ่านฟังก์ชัน <code>system.multicall</code> แฮกเกอร์สามารถส่งคำสั่งเดารหัสผ่าน 500-1,000 คู่ใน 1 HTTP Request ทำให้ทะลวงระบบ Rate Limiting ทั่วไปได้ง่ายดาย<br/>
2. <strong>Pingback DDoS:</strong> แฮกเกอร์ใช้สั่งให้เซิร์ฟเวอร์ยิง request ไปถล่มเหยื่ออื่น กลายเป็นตัวกระจาย DDoS!
</div>
</div>

<div style="background: rgba(245, 158, 11, 0.08); border: 1px solid rgba(245, 158, 11, 0.3); border-radius: 8px; padding: 12px;">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
<strong style="color: #fbbf24; font-size: 0.8rem;">🔴 จุดที่ 2: External WP-Cron Enabled</strong>
<span style="background: rgba(245,158,11,0.2); color:#fde047; font-size:0.65rem; font-family:monospace; padding:1px 5px; border-radius:3px;">MEDIUM RISK</span>
</div>
<p style="margin: 0 0 8px; color: #cbd5e1; font-size: 0.74rem; line-height: 1.5;">
<strong>คืออะไร:</strong> สคริปต์ตั้งเวลางานเบื้องหลัง <code>wp-cron.php</code> สามารถถูกทริกเกอร์เรียกทำงานได้จากคนภายนอก
</p>
<div style="background: rgba(0,0,0,0.4); border-left: 3px solid #f59e0b; padding: 8px; border-radius: 4px; font-size: 0.72rem; color: #fde047; line-height: 1.45;">
<strong>⚡ อันตรายอย่างไร:</strong><br/>
หากแฮกเกอร์ยิง Request ซ้ำๆ เข้าใส่ <code>wp-cron.php</code> ด้วยความเร็วสูง จะบังคับให้เซิร์ฟเวอร์รัน Background Tasks ตลอดเวลาจน CPU ทำงาน 100% ก่อให้เกิดภาวะ <strong>Resource Exhaustion Denial of Service (DoS)</strong> เว็บช้าหรือล่มในที่สุด
</div>
</div>

<div style="background: rgba(56, 189, 248, 0.08); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 8px; padding: 12px;">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
<strong style="color: #38bdf8; font-size: 0.8rem;">🔴 จุดที่ 3: WordPress 7.1 via RSS Feeds</strong>
<span style="background: rgba(56,189,248,0.2); color:#7dd3fc; font-size:0.65rem; font-family:monospace; padding:1px 5px; border-radius:3px;">INFO LEAK</span>
</div>
<p style="margin: 0 0 8px; color: #cbd5e1; font-size: 0.74rem; line-height: 1.5;">
<strong>คืออะไร:</strong> สแกนเนอร์สกัดเลขเวอร์ชันออกมาได้จากแท็ก <code>&lt;generator&gt;https://wordpress.org/?v=7.1&lt;/generator&gt;</code> ใน RSS Feed
</p>
<div style="background: rgba(0,0,0,0.4); border-left: 3px solid #38bdf8; padding: 8px; border-radius: 4px; font-size: 0.72rem; color: #7dd3fc; line-height: 1.45;">
<strong>⚡ บทเรียนสำคัญ:</strong><br/>
ผู้ดูแลเว็บมักลบเวอร์ชันในหน้า HTML หลัก แต่ลืมซ่อนในหน้า RSS Feed (เช่น <code>/feed/</code> และ <code>/comments/feed/</code>) ทำให้สแกนเนอร์อย่าง WPScan ดึงเวอร์ชันออกมาได้ทันที
</div>
</div>

</div>
</div>

<!-- WPScan Screenshot 3: Theme & Execution Metrics -->
<div style="background: #020617; border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 10px; padding: 16px;">
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; margin-bottom: 12px;">
<div style="color: #34d399; font-weight: 800; font-size: 0.88rem; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-palette"></i> ภาพที่ 3.3: การแจกแจงธีม (Theme Enumeration) และสถิติการสแกน (Execution Metrics)
</div>
<span style="color: #94a3b8; font-size: 0.72rem; font-family: monospace;">ARTIFACT: SCREENSHOT 175908</span>
</div>

<div style="text-align: center; margin-bottom: 14px;">
<img src="/tutorials/static/uploads/wpscan_theme_summary_crru_annotated.png" alt="WPScan Theme & Execution Metrics Annotated" style="max-width: 100%; border-radius: 8px; border: 1px solid rgba(16, 185, 129, 0.3); box-shadow: 0 6px 25px rgba(0,0,0,0.7);" />
<div style="color: #94a3b8; font-size: 0.73rem; margin-top: 6px; font-style: italic;">
ภาพที่ 3.3: WPScan แจกแจงธีม hello-elementor (v3.4.9) และสรุปการยิง 32 Requests เสร็จสิ้นในเวลาเพียง 7 วินาที
</div>
</div>

<!-- 2 Callouts for Screenshot 3 -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 10px;">
<div style="background: rgba(0,0,0,0.4); border-left: 3px solid #10b981; padding: 10px; border-radius: 6px;">
<strong style="color: #34d399; font-size: 0.78rem; display: block; margin-bottom: 4px;">🔴 จุดที่วง 1: Theme Enumeration (hello-elementor v3.4.9)</strong>
<span style="color: #cbd5e1; font-size: 0.74rem; line-height: 1.5; display: block;">
ตรวจพบธีม <code>hello-elementor</code> เวอร์ชัน 3.4.9 จากการอ่านไฟล์ <code>style.css</code> ซึ่งเป็นเวอร์ชันใหม่ที่มีผู้ใช้งานกว่า 1,000,000 เว็บไซต์ แสดงให้เห็นว่าระบบใช้ Elementor Page Builder ในการพัฒนาหน้าเว็บ
</span>
</div>
<div style="background: rgba(0,0,0,0.4); border-left: 3px solid #f59e0b; padding: 10px; border-radius: 6px;">
<strong style="color: #fde047; font-size: 0.78rem; display: block; margin-bottom: 4px;">🔴 จุดที่วง 2: Fast Execution Metrics (32 Requests / 7 วินาที)</strong>
<span style="color: #cbd5e1; font-size: 0.74rem; line-height: 1.5; display: block;">
WPScan ใช้เวลาเพียง 7 วินาทีในการส่ง 32 Requests เพื่อตรวจสอบความปลอดภัย ความรวดเร็วและจำนวนแพ็กเก็ตที่ต่ำนี้ทำให้การสแกนมักไม่ถูกตรวจจับโดยระบบ IDS/IPS ทั่วไป เว้นแต่จะมีการตั้งค่า Signature ตรวจจับบล็อก User-Agent ของ WPScan โดยเฉพาะ
</span>
</div>
</div>
</div>

</div>

<!-- ==================== HARDENING & DEFENSE MATRIX ==================== -->
<div style="margin-top: 20px; overflow-x: auto; border: 1px solid rgba(16,185,129,0.25); border-radius: 10px; background: #05070f;">
<div style="padding: 12px 16px; background: rgba(16,185,129,0.08); border-bottom: 1px solid rgba(16,185,129,0.15); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.82rem; font-weight: 700; color: #10b981; text-transform: uppercase;">
<i class="fas fa-shield-virus mr-2"></i> สรุปแนวทางแก้ไขและเสริมความปลอดภัย (CMS Hardening &amp; Remediation Matrix)
</span>
<span style="font-size: 0.7rem; color: #94a3b8;">BEST PRACTICES FOR SYSTEM ADMINS</span>
</div>
<table style="width: 100%; border-collapse: collapse; font-size: 0.78rem;">
<thead>
<tr style="background: rgba(255,255,255,0.03); border-bottom: 1px solid rgba(255,255,255,0.08);">
<th style="padding: 10px 12px; color: #10b981; text-align: left;">ประเด็นที่ตรวจพบ (Finding)</th>
<th style="padding: 10px 12px; color: #10b981; text-align: center; width: 110px;">ระดับความเสี่ยง</th>
<th style="padding: 10px 12px; color: #10b981; text-align: left;">แนวทางแก้ไขและป้องกัน (Remediation Actions)</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(239,68,68,0.03);">
<td style="padding: 10px 12px; font-weight: 700; color: #f87171;">XML-RPC เปิดใช้งาน (xmlrpc.php)</td>
<td style="padding: 10px 12px; text-align: center;"><span style="background: rgba(239,68,68,0.2); color: #fca5a5; padding: 2px 8px; border-radius: 4px; font-size: 0.7rem; font-weight: 800;">CRITICAL</span></td>
<td style="padding: 10px 12px; color: #cbd5e1; line-height: 1.5;">บล็อกการเข้าถึง <code>xmlrpc.php</code> ผ่าน Web Server เช่น ใน <code>.htaccess</code>: <code>RedirectMatch 403 (?i)/xmlrpc.php$</code> หรือติดตั้งปลั๊กอิน Disable XML-RPC เพื่อป้องกัน Brute-force และ Pingback DDoS</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 10px 12px; font-weight: 700; color: #fbbf24;">External WP-Cron เปิดให้เรียกตรง (wp-cron.php)</td>
<td style="padding: 10px 12px; text-align: center;"><span style="background: rgba(245,158,11,0.2); color: #fde047; padding: 2px 8px; border-radius: 4px; font-size: 0.7rem; font-weight: 800;">MEDIUM</span></td>
<td style="padding: 10px 12px; color: #cbd5e1; line-height: 1.5;">ปิด WP-Cron ภายนอกด้วย <code>define('DISABLE_WP_CRON', true);</code> ใน <code>wp-config.php</code> แล้วตั้งค่า Linux System Crontab ให้รัน <code>php wp-cron.php</code> ทุก 15 นาทีแทน เพื่อป้องกัน DoS Attack</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04); background: rgba(56,189,248,0.03);">
<td style="padding: 10px 12px; font-weight: 700; color: #38bdf8;">เวอร์ชันรั่วไหลทาง RSS Feeds &amp; Meta Generator</td>
<td style="padding: 10px 12px; text-align: center;"><span style="background: rgba(56,189,248,0.2); color: #7dd3fc; padding: 2px 8px; border-radius: 4px; font-size: 0.7rem; font-weight: 800;">LOW</span></td>
<td style="padding: 10px 12px; color: #cbd5e1; line-height: 1.5;">ซ่อนเลขเวอร์ชันในโค้ดธีมโดยใส่ <code>remove_action('wp_head', 'wp_generator');</code> และ <code>add_filter('the_generator', '__return_empty_string');</code> ใน <code>functions.php</code></td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 10px 12px; font-weight: 700; color: #f87171;">Full Path Disclosure (FPD) ในสคริปต์เก่า</td>
<td style="padding: 10px 12px; text-align: center;"><span style="background: rgba(239,68,68,0.2); color: #fca5a5; padding: 2px 8px; border-radius: 4px; font-size: 0.7rem; font-weight: 800;">HIGH</span></td>
<td style="padding: 10px 12px; color: #cbd5e1; line-height: 1.5;">ปิดการแสดง Error สู่หน้าบ้านใน Production (ตั้งค่า <code>display_errors = Off</code> ใน <code>php.ini</code>) และลบโมดูลที่ไม่ได้ใช้งานทิ้งเพื่อไม่ให้ Absolute Path หลุดไปช่วยแฮกเกอร์ทำ LFI หรือ SQLi INTO OUTFILE</td>
</tr>
<tr>
<td style="padding: 10px 12px; font-weight: 700; color: #a855f7;">หน้าล็อกอินผู้ดูแล (/administrator/ หรือ /wp-admin/)</td>
<td style="padding: 10px 12px; text-align: center;"><span style="background: rgba(168,85,247,0.2); color: #d8b4fe; padding: 2px 8px; border-radius: 4px; font-size: 0.7rem; font-weight: 800;">MEDIUM</span></td>
<td style="padding: 10px 12px; color: #cbd5e1; line-height: 1.5;">เปลี่ยนชื่อ URL หน้าล็อกอิน (URL Masking), เปิดระบบ 2FA (Two-Factor Authentication), และจำกัดการเข้าถึงหลังบ้านเฉพาะไอพีของแอดมิน (IP Whitelisting)</td>
</tr>
</tbody>
</table>
</div>

</div>
</div>"""

target_file = '/home/kali/crru_ctf/CTFd/create_lesson_179.py'
with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

pattern_start = r'<!-- ========================================================================= -->\s*<!-- CASE STUDY & REPORT DECODING:.*'
match_start = re.search(pattern_start, content)
if not match_start:
    print('[!] Could not find start of Case study!')
    exit(1)

start_pos = match_start.start()

pattern_end = r'"""\s*print\("Writing create_lesson_179\.py part 1\.\.\."\)'
match_end = re.search(pattern_end, content)
if not match_end:
    print('[!] Could not find end of cms_masterclass_html!')
    exit(1)

end_pos = match_end.start()

new_content = content[:start_pos] + new_case_study_html + content[end_pos:]

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('[+] Successfully updated create_lesson_179.py: Removed slide, using 100% real scans!')
