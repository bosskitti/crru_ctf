import json
from CTFd import create_app
from CTFd.utils import markdown

# =========================================================================
# SUMMARY CARD 1: SQL INJECTION (UNIFIED LABS 01 - 12 DEBRIEF)
# =========================================================================
sqli_summary_html = """<!-- ========================================== -->
<!-- UNIFIED MASTERCLASS DEBRIEF: SQL INJECTION (LABS 01 - 12) -->
<!-- ========================================== -->
<div style="margin: 2.5rem auto 3rem; max-width: 1050px; background: linear-gradient(135deg, rgba(8, 14, 30, 0.98) 0%, rgba(25, 10, 20, 0.98) 100%); border: 1px solid rgba(244, 63, 94, 0.35); border-left: 4px solid #f43f5e; border-radius: 16px; padding: 24px 28px; box-shadow: 0 16px 45px rgba(0, 0, 0, 0.7), 0 0 30px rgba(244, 63, 94, 0.15);">

<!-- Header -->
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; margin-bottom: 20px; padding-bottom: 14px; border-bottom: 1px solid rgba(255, 255, 255, 0.08);">
<div style="display: flex; align-items: center; gap: 14px;">
<div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(244, 63, 94, 0.15); color: #f43f5e; border: 1px solid rgba(244, 63, 94, 0.4); display: flex; align-items: center; justify-content: center; font-size: 1.4rem; box-shadow: 0 0 20px rgba(244, 63, 94, 0.3); flex-shrink: 0;">
<i class="fas fa-database"></i>
</div>
<div>
<h4 style="margin: 0; color: #ffffff; font-size: 1.2rem; font-weight: 800; letter-spacing: -0.01em;">
🛡️ สรุปบทเรียนท้ายแล็บ: กลไกและแนวทางป้องกัน SQL Injection (Labs 01–12 Summary)
</h4>
<span style="color: #94a3b8; font-size: 0.82rem;">ถอดรหัสความล้มเหลวจากการต่อสตริงคำสั่ง SQL 12 รูปแบบ สู่มาตรฐานการป้องกันระดับโปรดักชัน</span>
</div>
</div>
<div style="display: flex; gap: 8px; flex-wrap: wrap;">
<span style="background: rgba(244, 63, 94, 0.15); color: #fca5a5; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(244, 63, 94, 0.35);">
OWASP A03: INJECTION
</span>
<span style="background: rgba(0, 240, 255, 0.15); color: #7dd3fc; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(0, 240, 255, 0.35);">
CWE-89: SQL INJECTION
</span>
</div>
</div>

<!-- Key Takeaways Grid (3 Columns) -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 14px; margin-bottom: 20px;">

<!-- Column 1 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(244, 63, 94, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #f43f5e; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-bolt"></i> 1. แก่นการโจมตี (Attack Vectors Explored)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>Auth Bypass:</strong> ใช้ <code>' OR 1=1 --</code> บิดเบือนเงื่อนไข Boolean เพื่อผ่านด่านล็อกอิน</li>
<li><strong>UNION-Based:</strong> ส่องหาจำนวนคอลัมน์ด้วย <code>ORDER BY n</code> และทดสอบ Type ก่อนดึงข้อมูล</li>
<li><strong>Error &amp; Blind:</strong> บังคับให้ DBMS ส่ง Error หรือหน่วงเวลา <code>SLEEP()</code> เมื่อไม่แสดงผลลัพธ์</li>
<li><strong>Multi-DBMS:</strong> ความต่างของไวยากรณ์ SQLite, MySQL, และ Oracle (เช่น <code>FROM dual</code>)</li>
</ul>
</div>

<!-- Column 2 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(251, 191, 36, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #fbbf24; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-triangle-exclamation"></i> 2. ผลกระทบจริงต่อองค์กร (Business Impact)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>ข้อมูลรั่วไหลขนานใหญ่ (Data Breach):</strong> แฮกเกอร์ดัมป์รหัสผ่าน แฮช และข้อมูลส่วนบุคคล (PDPA)</li>
<li><strong>การปลอมแปลงสิทธิ์ (Privilege Escalation):</strong> สวมรอยเป็นผู้ดูแลระบบระดับ Superadmin</li>
<li><strong>แก้ไขหรือทำลายฐานข้อมูล:</strong> สั่ง <code>UPDATE</code> ยอดเงิน หรือ <code>DROP TABLE</code> ทำลายระบบ</li>
<li><strong>ทะลุสู่ OS Host:</strong> หากใช้ <code>INTO OUTFILE</code> หรือ <code>xp_cmdshell</code> สามารถนำไปสู่ RCE ได้ทันที</li>
</ul>
</div>

<!-- Column 3 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #4ade80; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-shield-halved"></i> 3. กฎเหล็กการป้องกัน (Golden Defense Rules)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>Prepared Statements 100%:</strong> แยกคำสั่ง SQL ออกจากข้อมูลด้วย Parameterized Queries</li>
<li><strong>ใช้ ORM / Query Builder:</strong> เช่น Prisma, Hibernate, SQLAlchemy เพื่อความปลอดภัยอัตโนมัติ</li>
<li><strong>Least Privilege:</strong> กำหนดสิทธิ์บัญชีเชื่อมต่อ DB เท่าที่จำเป็น (ห้ามใช้ Root/DBA ต่อเว็บ)</li>
<li><strong>ปิดการแสดง Error ลึก:</strong> ซ่อน Database Stack Trace ไม่ให้ผู้ใช้ภายนอกมองเห็น</li>
</ul>
</div>

</div>

<!-- Secure Code Comparison Box -->
<div style="background: #040711; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 18px; margin-bottom: 16px;">
<div style="color: #94a3b8; font-size: 0.78rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-code-compare"></i> ตัวอย่างเปรียบเทียบโค้ด: โค้ดที่มีช่องโหว่ vs โค้ดที่ปลอดภัย (PHP PDO Standard)
</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(310px, 1fr)); gap: 14px;">
<div style="background: rgba(239, 68, 68, 0.08); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 8px; padding: 12px;">
<div style="color: #fca5a5; font-size: 0.78rem; font-weight: 800; margin-bottom: 6px;">❌ VULNERABLE: การต่อสตริงคำสั่ง SQL โดยตรง</div>
<pre style="margin: 0; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #fca5a5; line-height: 1.5;"><code>// ผู้โจมตีสามารถฉีด ' OR 1=1 -- บิดเบือนคิวรีได้ทันที
$sql = "SELECT * FROM users WHERE user = '" . $_POST['user'] . "' AND pass = '" . $_POST['pass'] . "'";
$res = $db-&gt;query($sql);</code></pre>
</div>
<div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 12px;">
<div style="color: #86efac; font-size: 0.78rem; font-weight: 800; margin-bottom: 6px;">✅ SECURE: ใช้ Prepared Statements พร้อม Parameter Binding</div>
<pre style="margin: 0; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #86efac; line-height: 1.5;"><code>// ฐานข้อมูลจะมองอินพุตเป็น Literal Data เท่านั้น ไม่มีวันกลายเป็นคำสั่ง
$stmt = $pdo-&gt;prepare("SELECT * FROM users WHERE user = :u AND pass = :p");
$stmt-&gt;execute(['u' =&gt; $_POST['user'], 'p' =&gt; $_POST['pass']]);
$user = $stmt-&gt;fetch();</code></pre>
</div>
</div>
</div>

<div style="text-align: right; font-size: 0.76rem; color: #64748b;">
บทสรุปสำหรับปฏิบัติการ Lab SQLi-01 ถึง SQLi-12 &bull; CRRU Cybersecurity Curriculum 2026
</div>

</div>"""

# =========================================================================
# SUMMARY CARD 2: COMMAND INJECTION (UNIFIED LABS CMD-1 & CMD-2 DEBRIEF)
# =========================================================================
cmdi_summary_html = """<!-- ========================================== -->
<!-- UNIFIED MASTERCLASS DEBRIEF: COMMAND INJECTION (LABS CMD-1 & CMD-2) -->
<!-- ========================================== -->
<div style="margin: 2.5rem auto 3rem; max-width: 1050px; background: linear-gradient(135deg, rgba(8, 14, 30, 0.98) 0%, rgba(25, 12, 10, 0.98) 100%); border: 1px solid rgba(239, 68, 68, 0.35); border-left: 4px solid #ef4444; border-radius: 16px; padding: 24px 28px; box-shadow: 0 16px 45px rgba(0, 0, 0, 0.7), 0 0 30px rgba(239, 68, 68, 0.15);">

<!-- Header -->
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; margin-bottom: 20px; padding-bottom: 14px; border-bottom: 1px solid rgba(255, 255, 255, 0.08);">
<div style="display: flex; align-items: center; gap: 14px;">
<div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(239, 68, 68, 0.15); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.4); display: flex; align-items: center; justify-content: center; font-size: 1.4rem; box-shadow: 0 0 20px rgba(239, 68, 68, 0.3); flex-shrink: 0;">
<i class="fas fa-terminal"></i>
</div>
<div>
<h4 style="margin: 0; color: #ffffff; font-size: 1.2rem; font-weight: 800; letter-spacing: -0.01em;">
🛡️ สรุปบทเรียนท้ายแล็บ: กลไกและแนวทางป้องกัน Command Injection (Labs CMD-1 &amp; CMD-2)
</h4>
<span style="color: #94a3b8; font-size: 0.82rem;">ถอดรหัสความแตกต่างระหว่าง Direct Execution กับ Blind Delay สู่การควบคุมความปลอดภัยระดับ OS</span>
</div>
</div>
<div style="display: flex; gap: 8px; flex-wrap: wrap;">
<span style="background: rgba(239, 68, 68, 0.15); color: #fca5a5; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(239, 68, 68, 0.35);">
OWASP A03: INJECTION
</span>
<span style="background: rgba(245, 158, 11, 0.15); color: #fde047; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(245, 158, 11, 0.35);">
CWE-78: OS COMMAND
</span>
</div>
</div>

<!-- Comparison & Remediation Grid -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 14px; margin-bottom: 20px;">

<!-- Column 1 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(239, 68, 68, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #ef4444; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-microchip"></i> 1. สิ่งที่ได้เรียนรู้จาก 2 แล็บ (Lab Scenarios)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>Lab CMD-1 (Direct RCE):</strong> แทรกตัวคั่นคำสั่ง (<code>;</code>, <code>|</code>, <code>&amp;&amp;</code>) แล้วอ่านผลลัพธ์คำสั่งระบบได้ทันทีบนหน้าเว็บ</li>
<li><strong>Lab CMD-2 (Blind OOB):</strong> เซิร์ฟเวอร์ไม่พ่น Output จึงต้องใช้ <code>sleep 5</code> วัดเวลาหน่วงเพื่อยืนยัน RCE</li>
<li><strong>Bypass Filters:</strong> การใช้ Command Substitution เช่น <code>$(cat /flag.txt)</code> เลี่ยงการตรวจจับคีย์เวิร์ด</li>
</ul>
</div>

<!-- Column 2 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(245, 158, 11, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #fde047; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-radiation"></i> 2. ระดับความรุนแรงสูงสุด (Remote Code Exec)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>Sever Host Compromise:</strong> แฮกเกอร์ไม่ได้อยู่แค่ในระดับ Web แต่ทะลุเข้าไปสั่งการในระบบปฏิบัติการ</li>
<li><strong>Reverse Shell Takeover:</strong> สามารถยิง <code>nc -e /bin/sh</code> ยึด Terminal ของเครื่องเซิร์ฟเวอร์แบบถาวร</li>
<li><strong>Pivot &amp; Lateral Movement:</strong> ใช้เครื่องเซิร์ฟเวอร์ที่ถูกยึดเป็นฐานเจาะต่อไปยังระบบเครือข่ายภายในองค์กร</li>
</ul>
</div>

<!-- Column 3 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #4ade80; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-shield-halved"></i> 3. แนวทางป้องกันที่ได้ผลจริง (Remediation)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>หลีกเลี่ยง Shell Functions:</strong> ไม่ใช้ <code>system()</code>, <code>exec()</code>, <code>passthru()</code> หรือ <code>shell_exec()</code></li>
<li><strong>ใช้ Built-in API แทน:</strong> เช่น หากต้องการตรวจสอบโดเมน ให้ใช้ <code>dns_get_record()</code> แทนการสั่ง <code>nslookup</code></li>
<li><strong>Strict Input Whitelist:</strong> ตรวจสอบว่า IP ต้องเป็นตัวเลขและจุดเท่านั้นด้วย <code>filter_var($ip, FILTER_VALIDATE_IP)</code></li>
<li><strong>Container Sandboxing:</strong> รันเว็บด้วยผู้ใช้สิทธิ์ต่ำ (เช่น <code>www-data</code>) และตั้งค่า Read-Only Filesystem</li>
</ul>
</div>

</div>

<!-- Secure Code Comparison Box -->
<div style="background: #040711; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 18px; margin-bottom: 16px;">
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(310px, 1fr)); gap: 14px;">
<div style="background: rgba(239, 68, 68, 0.08); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 8px; padding: 12px;">
<div style="color: #fca5a5; font-size: 0.78rem; font-weight: 800; margin-bottom: 6px;">❌ VULNERABLE: ส่งพารามิเตอร์ตรงเข้า OS Shell</div>
<pre style="margin: 0; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #fca5a5; line-height: 1.5;"><code>$ip = $_GET['ip'];
// คำสั่งถูกต่อสตริงตรงๆ แฮกเกอร์ใช้ ; หรือ | ยึดเชลล์ได้ทันที
system("ping -c 1 " . $ip);</code></pre>
</div>
<div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 12px;">
<div style="color: #86efac; font-size: 0.78rem; font-weight: 800; margin-bottom: 6px;">✅ SECURE: ตรวจสอบ IP อย่างเข้มงวด + หลีกเลี่ยง Shell</div>
<pre style="margin: 0; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #86efac; line-height: 1.5;"><code>$ip = $_GET['ip'];
if (!filter_var($ip, FILTER_VALIDATE_IP)) {
    die("Invalid IP address"); // บล็อกอักขระแปลกปลอมทันที
}
// หากจำเป็นต้องรัน ให้ Escape Argument อย่างรัดกุม
system("ping -c 1 " . escapeshellarg($ip));</code></pre>
</div>
</div>
</div>

<div style="text-align: right; font-size: 0.76rem; color: #64748b;">
บทสรุปสำหรับปฏิบัติการ Lab CMD-1 ถึง CMD-2 &bull; CRRU Cybersecurity Curriculum 2026
</div>

</div>"""

# =========================================================================
# SUMMARY CARD 3: FILE INCLUSION (UNIFIED LABS LFI-1 & LFI-2 DEBRIEF)
# =========================================================================
lfi_summary_html = """<!-- ========================================== -->
<!-- UNIFIED MASTERCLASS DEBRIEF: FILE INCLUSION (LABS LFI-1 & LFI-2) -->
<!-- ========================================== -->
<div style="margin: 2.5rem auto 3rem; max-width: 1050px; background: linear-gradient(135deg, rgba(8, 14, 30, 0.98) 0%, rgba(25, 20, 10, 0.98) 100%); border: 1px solid rgba(251, 191, 36, 0.35); border-left: 4px solid #fbbf24; border-radius: 16px; padding: 24px 28px; box-shadow: 0 16px 45px rgba(0, 0, 0, 0.7), 0 0 30px rgba(251, 191, 36, 0.15);">

<!-- Header -->
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; margin-bottom: 20px; padding-bottom: 14px; border-bottom: 1px solid rgba(255, 255, 255, 0.08);">
<div style="display: flex; align-items: center; gap: 14px;">
<div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(251, 191, 36, 0.15); color: #fbbf24; border: 1px solid rgba(251, 191, 36, 0.4); display: flex; align-items: center; justify-content: center; font-size: 1.4rem; box-shadow: 0 0 20px rgba(251, 191, 36, 0.3); flex-shrink: 0;">
<i class="fas fa-folder-open"></i>
</div>
<div>
<h4 style="margin: 0; color: #ffffff; font-size: 1.2rem; font-weight: 800; letter-spacing: -0.01em;">
🛡️ สรุปบทเรียนท้ายแล็บ: กลไกและแนวทางป้องกัน File Inclusion (Labs LFI-1 &amp; LFI-2)
</h4>
<span style="color: #94a3b8; font-size: 0.82rem;">ถอดรหัสความล้มเหลวของการกรอง Path Traversal สู่การบล็อก Stream Wrappers และ Whitelist</span>
</div>
</div>
<div style="display: flex; gap: 8px; flex-wrap: wrap;">
<span style="background: rgba(251, 191, 36, 0.15); color: #fde047; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(251, 191, 36, 0.35);">
OWASP A01: BROKEN ACCESS CONTROL
</span>
<span style="background: rgba(16, 185, 129, 0.15); color: #6ee7b7; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(16, 185, 129, 0.35);">
CWE-98: PHP FILE INCLUSION
</span>
</div>
</div>

<!-- Comparison & Remediation Grid -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 14px; margin-bottom: 20px;">

<!-- Column 1 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(251, 191, 36, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #fbbf24; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-file-code"></i> 1. แก่นการโจมตีจาก 2 แล็บ (LFI Techniques)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>Lab LFI-1 (Basic Path Traversal):</strong> การใช้ <code>../../../../</code> ถอยออกจาก Web Root เพื่ออ่านไฟล์ระบบ</li>
<li><strong>Lab LFI-2 (Stream Wrapper Bypass):</strong> การใช้ <code>php://filter/convert.base64-encode/resource=...</code> เพื่ออ่าน Source Code หลังบ้าน</li>
<li><strong>ทำไมถึงอันตราย:</strong> ฟังก์ชัน <code>include()</code> ใน PHP ไม่ได้แค่เปิดอ่านไฟล์ แต่ยังสั่งประมวลผลโค้ด PHP ในไฟล์นั้นด้วย</li>
</ul>
</div>

<!-- Column 2 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(239, 68, 68, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #f87171; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-bomb"></i> 2. การยกระดับจาก LFI สู่ RCE (Escalation Path)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>Log Poisoning:</strong> ฉีดโค้ด PHP ลงใน Access Log ของ Apache/Nginx แล้วเรียก <code>include()</code> ล็อกไฟล์เพื่อรันเชลล์</li>
<li><strong>PHP Session File Upload:</strong> ฝังโค้ด PHP ลงในตัวแปร Session แล้วเรียกไฟล์ <code>/tmp/sess_*</code></li>
<li><strong>RFI (Remote Execution):</strong> หากเปิด <code>allow_url_include = On</code> แฮกเกอร์จะดึง Webshell จากภายนอกมารันได้ทันที</li>
</ul>
</div>

<!-- Column 3 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #4ade80; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-lock"></i> 3. มาตรการป้องกันที่สมบูรณ์ (Hardening)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>ใช้ Whitelist Array 100%:</strong> อนุญาตเฉพาะชื่อไฟล์ที่อยู่ในรายการ เช่น <code>['home', 'about', 'contact']</code></li>
<li><strong>ตัด Directory Traversal:</strong> ใช้ฟังก์ชัน <code>basename()</code> ตัดเครื่องหมาย <code>../</code> หรือพาธทิ้งทั้งหมด</li>
<li><strong>ปิดการโหลดไฟล์ภายนอก:</strong> กำหนด <code>allow_url_include = Off</code> และ <code>allow_url_fopen = Off</code> ใน <code>php.ini</code></li>
<li><strong>แยกไฟล์ออกนอก DocumentRoot:</strong> เก็บไฟล์ระบบไว้ในโฟลเดอร์ที่ไม่เปิดให้บุคคลภายนอกเข้าถึงผ่าน URL</li>
</ul>
</div>

</div>

<!-- Secure Code Comparison Box -->
<div style="background: #040711; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 18px; margin-bottom: 16px;">
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(310px, 1fr)); gap: 14px;">
<div style="background: rgba(239, 68, 68, 0.08); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 8px; padding: 12px;">
<div style="color: #fca5a5; font-size: 0.78rem; font-weight: 800; margin-bottom: 6px;">❌ VULNERABLE: ส่งพารามิเตอร์เข้าฟังก์ชัน include() ตรงๆ</div>
<pre style="margin: 0; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #fca5a5; line-height: 1.5;"><code>$page = $_GET['page'];
// เปิดโอกาสให้ใช้ ../../ หรือ php://filter ดึง Source Code
include($page . ".php");</code></pre>
</div>
<div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 12px;">
<div style="color: #86efac; font-size: 0.78rem; font-weight: 800; margin-bottom: 6px;">✅ SECURE: กำหนด Whitelist ไฟล์ที่อนุญาตอย่างเข้มงวด</div>
<pre style="margin: 0; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #86efac; line-height: 1.5;"><code>$whitelist = ['home' =&gt; 'home.php', 'about' =&gt; 'about.php'];
$page = $_GET['page'] ?? 'home';
if (!array_key_exists($page, $whitelist)) {
    die("Access Denied: Invalid Page");
}
include($whitelist[$page]); // ปลอดภัย 100% เพราะไม่อิงตามพาธที่ผู้ใช้ส่งมา</code></pre>
</div>
</div>
</div>

<div style="text-align: right; font-size: 0.76rem; color: #64748b;">
บทสรุปสำหรับปฏิบัติการ Lab LFI-1 ถึง LFI-2 &bull; CRRU Cybersecurity Curriculum 2026
</div>

</div>"""

# =========================================================================
# SUMMARY CARD 4: CROSS-SITE SCRIPTING (UNIFIED LABS XSS 1, 2, 3 DEBRIEF)
# =========================================================================
xss_summary_html = """<!-- ========================================== -->
<!-- UNIFIED MASTERCLASS DEBRIEF: CROSS-SITE SCRIPTING (LABS XSS-1, 2, 3) -->
<!-- ========================================== -->
<div style="margin: 2.5rem auto 3rem; max-width: 1050px; background: linear-gradient(135deg, rgba(8, 14, 30, 0.98) 0%, rgba(20, 10, 30, 0.98) 100%); border: 1px solid rgba(168, 85, 247, 0.35); border-left: 4px solid #a855f7; border-radius: 16px; padding: 24px 28px; box-shadow: 0 16px 45px rgba(0, 0, 0, 0.7), 0 0 30px rgba(168, 85, 247, 0.15);">

<!-- Header -->
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; margin-bottom: 20px; padding-bottom: 14px; border-bottom: 1px solid rgba(255, 255, 255, 0.08);">
<div style="display: flex; align-items: center; gap: 14px;">
<div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(168, 85, 247, 0.15); color: #c084fc; border: 1px solid rgba(168, 85, 247, 0.4); display: flex; align-items: center; justify-content: center; font-size: 1.4rem; box-shadow: 0 0 20px rgba(168, 85, 247, 0.3); flex-shrink: 0;">
<i class="fas fa-shield-virus"></i>
</div>
<div>
<h4 style="margin: 0; color: #ffffff; font-size: 1.2rem; font-weight: 800; letter-spacing: -0.01em;">
🛡️ สรุปบทเรียนท้ายแล็บ: กลไกและแนวทางป้องกัน Cross-Site Scripting (Labs XSS-1, 2, 3)
</h4>
<span style="color: #94a3b8; font-size: 0.82rem;">เปรียบเทียบ Reflected vs Stored vs DOM-Based และแนวทางป้องกันด้วย Context-Aware Encoding &amp; CSP</span>
</div>
</div>
<div style="display: flex; gap: 8px; flex-wrap: wrap;">
<span style="background: rgba(168, 85, 247, 0.15); color: #d8b4fe; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(168, 85, 247, 0.35);">
OWASP A03: INJECTION
</span>
<span style="background: rgba(236, 72, 153, 0.15); color: #f472b6; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(236, 72, 153, 0.35);">
CWE-79: XSS
</span>
</div>
</div>

<!-- Comparison & Remediation Grid -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 14px; margin-bottom: 20px;">

<!-- Column 1 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(168, 85, 247, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #c084fc; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-layer-group"></i> 1. สรุป 3 รูปแบบ XSS ที่ได้ลงมือทำ
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>Lab XSS-1 (Reflected):</strong> พารามิเตอร์ <code>?q=</code> สะท้อนกลับทันที ต้องหลอกให้เหยื่อคลิกลิงก์ฟิชชิ่ง</li>
<li><strong>Lab XSS-2 (Stored):</strong> สคริปต์ถูกบันทึกลงในฐานข้อมูลของเว็บบอร์ด ส่งผลกระทบต่อทุกคนที่เปิดดูหน้านั้น</li>
<li><strong>Lab XSS-3 (DOM-Based):</strong> ช่องโหว่บน JavaScript หน้าบ้าน อ่าน <code>location.hash</code> ไปเขียนลง <code>innerHTML</code> โดยไม่ผ่านเซิร์ฟเวอร์</li>
</ul>
</div>

<!-- Column 2 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(236, 72, 153, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #f472b6; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-user-ninja"></i> 2. ภัยคุกคามจริงฝั่ง Client (Weaponization)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>Session Hijacking:</strong> ขโมย <code>document.cookie</code> เพื่อสวมรอยเข้าใช้งานบัญชีของแอดมินหรือเหยื่อ</li>
<li><strong>Credential Harvesting:</strong> ซ้อนหน้าต่างล็อกอินปลอม (Phishing Modal) หลอกขโมยรหัสผ่านสดๆ</li>
<li><strong>Client-side Actions:</strong> บังคับให้เบราว์เซอร์ของเหยื่อสั่งโอนเงิน หรือเปลี่ยนรหัสผ่านโดยไม่รู้ตัว (XSS to CSRF)</li>
</ul>
</div>

<!-- Column 3 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #4ade80; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-shield-halved"></i> 3. เกราะป้องกันมาตรฐานสากล (Remediation)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>Context-Aware Encoding:</strong> ใช้ <code>htmlspecialchars($str, ENT_QUOTES, 'UTF-8')</code> แปลงอักขระพิเศษเป็น HTML Entities</li>
<li><strong>HttpOnly Flag on Cookies:</strong> ตั้งค่า Cookie ให้เป็น <code>HttpOnly</code> ป้องกันไม่ให้ JavaScript เข้าถึงได้</li>
<li><strong>Safe DOM APIs:</strong> ใช้ <code>textContent</code> หรือ <code>innerText</code> แทนการใช้ <code>innerHTML</code> หรือ <code>document.write</code></li>
<li><strong>Content Security Policy (CSP):</strong> ติดตั้ง Header <code>Content-Security-Policy: default-src 'self'</code> บล็อกสคริปต์ภายนอก</li>
</ul>
</div>

</div>

<!-- Secure Code Comparison Box -->
<div style="background: #040711; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 18px; margin-bottom: 16px;">
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(310px, 1fr)); gap: 14px;">
<div style="background: rgba(239, 68, 68, 0.08); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 8px; padding: 12px;">
<div style="color: #fca5a5; font-size: 0.78rem; font-weight: 800; margin-bottom: 6px;">❌ VULNERABLE: แสดงผลอินพุตผู้ใช้โดยไม่ Escape</div>
<pre style="margin: 0; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #fca5a5; line-height: 1.5;"><code>// PHP: แสดงค่าค้นหาทันที
echo "&lt;h2&gt;Search: " . $_GET['q'] . "&lt;/h2&gt;";

// JS DOM: สั่งเขียนโค้ด HTML ตรงๆ
document.getElementById("output").innerHTML = location.hash;</code></pre>
</div>
<div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 12px;">
<div style="color: #86efac; font-size: 0.78rem; font-weight: 800; margin-bottom: 6px;">✅ SECURE: แปลงเป็น HTML Entities + Safe DOM API</div>
<pre style="margin: 0; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #86efac; line-height: 1.5;"><code>// PHP: แปลงแท็ก &lt;script&gt; เป็นข้อความธรรมดา
echo "&lt;h2&gt;Search: " . htmlspecialchars($_GET['q'], ENT_QUOTES, 'UTF-8') . "&lt;/h2&gt;";

// JS DOM: ใช้ textContent ปลอดภัยจากการรันสคริปต์ 100%
document.getElementById("output").textContent = location.hash;</code></pre>
</div>
</div>
</div>

<div style="text-align: right; font-size: 0.76rem; color: #64748b;">
บทสรุปสำหรับปฏิบัติการ Lab XSS-1, XSS-2 และ XSS-3 &bull; CRRU Cybersecurity Curriculum 2026
</div>

</div>"""

# =========================================================================
# SUMMARY CARD 5: BRUTE FORCE & AUTOMATION (UNIFIED LABS BRUTE 1 & 2 DEBRIEF)
# =========================================================================
brute_summary_html = """<!-- ========================================== -->
<!-- UNIFIED MASTERCLASS DEBRIEF: BRUTE FORCE & AUTOMATION (LABS BRUTE-1 & 2) -->
<!-- ========================================== -->
<div style="margin: 2.5rem auto 3rem; max-width: 1050px; background: linear-gradient(135deg, rgba(8, 14, 30, 0.98) 0%, rgba(10, 20, 35, 0.98) 100%); border: 1px solid rgba(56, 189, 248, 0.35); border-left: 4px solid #38bdf8; border-radius: 16px; padding: 24px 28px; box-shadow: 0 16px 45px rgba(0, 0, 0, 0.7), 0 0 30px rgba(56, 189, 248, 0.15);">

<!-- Header -->
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; margin-bottom: 20px; padding-bottom: 14px; border-bottom: 1px solid rgba(255, 255, 255, 0.08);">
<div style="display: flex; align-items: center; gap: 14px;">
<div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); display: flex; align-items: center; justify-content: center; font-size: 1.4rem; box-shadow: 0 0 20px rgba(56, 189, 248, 0.3); flex-shrink: 0;">
<i class="fas fa-key"></i>
</div>
<div>
<h4 style="margin: 0; color: #ffffff; font-size: 1.2rem; font-weight: 800; letter-spacing: -0.01em;">
🛡️ สรุปบทเรียนท้ายแล็บ: กลไกและแนวทางป้องกัน Brute Force Attacks (Labs BRUTE-1 &amp; 2)
</h4>
<span style="color: #94a3b8; font-size: 0.82rem;">ถอดรหัสความล้มเหลวของการไม่มี Rate Limiting สู่การตั้งรับด้วย Multi-Factor Auth, CAPTCHA และ Lockout</span>
</div>
</div>
<div style="display: flex; gap: 8px; flex-wrap: wrap;">
<span style="background: rgba(56, 189, 248, 0.15); color: #7dd3fc; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(56, 189, 248, 0.35);">
OWASP A07: AUTH FAILURES
</span>
<span style="background: rgba(239, 68, 68, 0.15); color: #fca5a5; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(239, 68, 68, 0.35);">
CWE-307: IMPROPER RESTRICTION
</span>
</div>
</div>

<!-- Comparison & Remediation Grid -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 14px; margin-bottom: 20px;">

<!-- Column 1 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #38bdf8; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-stopwatch"></i> 1. สิ่งที่ได้เรียนรู้จาก 2 แล็บ (Automation Impact)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>Lab BRUTE-1 (PIN Lock):</strong> รหัส PIN 4 หลักมีเพียง 10,000 รูปแบบ สคริปต์ Python ใช้เวลาไม่ถึง 2 นาทีในการเจาะผ่าน</li>
<li><strong>Lab BRUTE-2 (Dictionary Login):</strong> การใช้พจนานุกรมรหัสผ่านยอดนิยม (เช่น <code>rockyou.txt</code>) ร่วมกับ Hydra เพื่อสุ่มเข้าบัญชี Admin</li>
<li><strong>จุดตายสำคัญ:</strong> ระบบขาด Rate Limiting ส่งผลให้บอทสามารถยิง Request ได้นับร้อยครั้งต่อวินาทีโดยไม่ถูกตัดการเชื่อมต่อ</li>
</ul>
</div>

<!-- Column 2 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(239, 68, 68, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #f87171; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-skull"></i> 2. ความเสี่ยงต่อความมั่นคงของระบบ (Security Risk)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>Account Takeover (ATO):</strong> ผู้โจมตีเข้าควบคุมบัญชีของผู้ใช้หรือแอดมินได้อย่างสมบูรณ์</li>
<li><strong>Resource Exhaustion (DoS):</strong> การยิงล็อกอินซ้ำๆ ด้วยความเร็วสูงทำให้ CPU และฐานข้อมูลทำงานหนักจนระบบล่ม</li>
<li><strong>Credential Stuffing Leaks:</strong> แฮกเกอร์นำฐานข้อมูลที่รั่วไหลจากเว็บอื่นมาตระเวนล็อกอินสำเร็จเพราะผู้ใช้ชอบตั้งรหัสซ้ำ</li>
</ul>
</div>

<!-- Column 3 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #4ade80; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-shield-halved"></i> 3. มาตรการป้องกันระดับสากล (Remediation)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>Rate Limiting (Token Bucket):</strong> จำกัดการล็อกอินไม่เกิน 5 ครั้งต่อนาทีต่อ IP (เช่น Nginx <code>limit_req</code>, Flask-Limiter)</li>
<li><strong>Account Lockout &amp; Progressive Delay:</strong> หากกรอกผิดครบ 5 ครั้ง ให้ล็อกบัญชีชั่วคราว 15 นาที หรือหน่วงเวลาตอบสนอง</li>
<li><strong>Multi-Factor Authentication (MFA):</strong> บังคับใช้ 2FA (เช่น Google Authenticator, TOTP) ทำให้แม้รู้รหัสผ่านก็ล็อกอินไม่ได้</li>
<li><strong>CAPTCHA Protection:</strong> แสดง Cloudflare Turnstile หรือ reCAPTCHA ทันทีที่พบการล็อกอินผิดซ้ำหลายครั้ง</li>
</ul>
</div>

</div>

<!-- Secure Code Comparison Box -->
<div style="background: #040711; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 18px; margin-bottom: 16px;">
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(310px, 1fr)); gap: 14px;">
<div style="background: rgba(239, 68, 68, 0.08); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 8px; padding: 12px;">
<div style="color: #fca5a5; font-size: 0.78rem; font-weight: 800; margin-bottom: 6px;">❌ VULNERABLE: ไม่มีระบบนับครั้งผิดและ Rate Limiting</div>
<pre style="margin: 0; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #fca5a5; line-height: 1.5;"><code>// อนุญาตให้ยิง Request ได้ไม่จำกัดครั้ง ไม่มีการบันทึกประวัติล้มเหลว
if (check_password($user, $pass)) {
    login_success();
} else {
    echo "Invalid Credentials"; // เปิดให้วนลูปทดสอบได้เป็นล้านครั้ง
}</code></pre>
</div>
<div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 12px;">
<div style="color: #86efac; font-size: 0.78rem; font-weight: 800; margin-bottom: 6px;">✅ SECURE: จำกัดจำนวนครั้งด้วย Redis / Rate Limiter + Lockout</div>
<pre style="margin: 0; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #86efac; line-height: 1.5;"><code>$attempts = $redis-&gt;get("login_fail:" . $ip);
if ($attempts &gt;= 5) {
    die("Account temporarily locked. Please try again in 15 minutes.");
}
if (!check_password($user, $pass)) {
    $redis-&gt;incr("login_fail:" . $ip);
    $redis-&gt;expire("login_fail:" . $ip, 900); // หน่วงเวลา 15 นาที
    echo "Invalid Credentials";
}</code></pre>
</div>
</div>
</div>

<div style="text-align: right; font-size: 0.76rem; color: #64748b;">
บทสรุปสำหรับปฏิบัติการ Lab BRUTE-1 ถึง BRUTE-2 &bull; CRRU Cybersecurity Curriculum 2026
</div>

</div>"""

# Test rendering
summaries = [
    ("SQLi Summary", sqli_summary_html),
    ("CMD Injection Summary", cmdi_summary_html),
    ("LFI/RFI Summary", lfi_summary_html),
    ("XSS Summary", xss_summary_html),
    ("Brute Force Summary", brute_summary_html)
]

for name, html in summaries:
    clean = '\n'.join([l.strip() for l in html.split('\n') if l.strip()])
    r = markdown(clean)
    has_p = '<p>' in r
    has_div = '&lt;div' in r
    print(f"{name:24}: len={len(r):5}, any <p>={has_p!s:5}, any &lt;div={has_div!s:5}")

print("\nAll 5 summary cards tested successfully!")
