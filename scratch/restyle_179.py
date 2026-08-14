import json
import sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

NEW_BLOCK_0 = """<div style="text-align: center; margin-bottom: 2rem; padding: 24px; background: linear-gradient(135deg, rgba(16,185,129,0.15) 0%, rgba(59,130,246,0.15) 100%); border: 1px solid rgba(16,185,129,0.3); border-radius: 16px; box-shadow: 0 0 20px rgba(16,185,129,0.15);">
<h2 style="margin: 0; font-size: 1.9rem; font-weight: 800; color: #ffffff; text-shadow: 0 0 12px rgba(16,185,129,0.6); letter-spacing: 0.03em;">🧩 CMS Exploitation & Scanning Tools</h2>
<p style="margin: 8px 0 0 0; font-size: 0.92rem; color: #94a3b8; font-weight: 500;">เจาะลึกการโจมตีระบบจัดการเนื้อหาเว็บ (CMS) และเครื่องมือสแกนช่องโหว่ระดับมืออาชีพ</p>
</div>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin: 1.5rem auto;">
<div style="background: linear-gradient(to bottom right, rgba(59,130,246,0.07), rgba(59,130,246,0.02)); border: 1px solid rgba(59,130,246,0.25); border-radius: 10px; padding: 14px; text-align: center;">
<div style="font-size: 1.4rem; margin-bottom: 6px;">🔵</div>
<strong style="color: #3b82f6; font-size: 0.85rem; display: block; margin-bottom: 4px;">WordPress</strong>
<span style="color: #64748b; font-size: 0.75rem;">62.7% market share → WPScan</span>
</div>
<div style="background: linear-gradient(to bottom right, rgba(251,146,60,0.07), rgba(251,146,60,0.02)); border: 1px solid rgba(251,146,60,0.25); border-radius: 10px; padding: 14px; text-align: center;">
<div style="font-size: 1.4rem; margin-bottom: 6px;">🟠</div>
<strong style="color: #fb923c; font-size: 0.85rem; display: block; margin-bottom: 4px;">Joomla</strong>
<span style="color: #64748b; font-size: 0.75rem;">2.4% market share → JoomScan</span>
</div>
<div style="background: linear-gradient(to bottom right, rgba(99,102,241,0.07), rgba(99,102,241,0.02)); border: 1px solid rgba(99,102,241,0.25); border-radius: 10px; padding: 14px; text-align: center;">
<div style="font-size: 1.4rem; margin-bottom: 6px;">🟣</div>
<strong style="color: #6366f1; font-size: 0.85rem; display: block; margin-bottom: 4px;">Drupal</strong>
<span style="color: #64748b; font-size: 0.75rem;">1.3% market share → Droopescan</span>
</div>
<div style="background: linear-gradient(to bottom right, rgba(16,185,129,0.07), rgba(16,185,129,0.02)); border: 1px solid rgba(16,185,129,0.25); border-radius: 10px; padding: 14px; text-align: center;">
<div style="font-size: 1.4rem; margin-bottom: 6px;">🟢</div>
<strong style="color: #10b981; font-size: 0.85rem; display: block; margin-bottom: 4px;">Multi-CMS</strong>
<span style="color: #64748b; font-size: 0.75rem;">CMSmap / CMSeek / Metasploit</span>
</div>
</div>

<div style="background: #05070f; border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 20px; margin-bottom: 2rem;">
<div style="font-size: 0.82rem; color: #00f0ff; font-weight: 700; margin-bottom: 14px; text-transform: uppercase; letter-spacing: 0.07em;"><i class="fas fa-crosshairs mr-2"></i>Common CMS Exploitation Techniques</div>
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">
<div style="display: flex; align-items: center; gap: 8px; padding: 8px 12px; background: rgba(255,0,127,0.05); border: 1px solid rgba(255,0,127,0.15); border-radius: 6px;"><span style="color:#ff007f; font-size:0.9rem;">💉</span><span style="color:#cbd5e1; font-size:0.8rem;">SQL Injection (SQLi)</span></div>
<div style="display: flex; align-items: center; gap: 8px; padding: 8px 12px; background: rgba(251,191,36,0.05); border: 1px solid rgba(251,191,36,0.15); border-radius: 6px;"><span style="color:#fbbf24; font-size:0.9rem;">📜</span><span style="color:#cbd5e1; font-size:0.8rem;">Cross-Site Scripting (XSS)</span></div>
<div style="display: flex; align-items: center; gap: 8px; padding: 8px 12px; background: rgba(239,68,68,0.05); border: 1px solid rgba(239,68,68,0.15); border-radius: 6px;"><span style="color:#ef4444; font-size:0.9rem;">💥</span><span style="color:#cbd5e1; font-size:0.8rem;">Remote Code Execution (RCE)</span></div>
<div style="display: flex; align-items: center; gap: 8px; padding: 8px 12px; background: rgba(0,240,255,0.05); border: 1px solid rgba(0,240,255,0.15); border-radius: 6px;"><span style="color:#00f0ff; font-size:0.9rem;">📁</span><span style="color:#cbd5e1; font-size:0.8rem;">File Inclusion (LFI &amp; RFI)</span></div>
<div style="display: flex; align-items: center; gap: 8px; padding: 8px 12px; background: rgba(168,85,247,0.05); border: 1px solid rgba(168,85,247,0.15); border-radius: 6px;"><span style="color:#a855f7; font-size:0.9rem;">⬆️</span><span style="color:#cbd5e1; font-size:0.8rem;">Privilege Escalation</span></div>
<div style="display: flex; align-items: center; gap: 8px; padding: 8px 12px; background: rgba(16,185,129,0.05); border: 1px solid rgba(16,185,129,0.15); border-radius: 6px;"><span style="color:#3ddc84; font-size:0.9rem;">🔑</span><span style="color:#cbd5e1; font-size:0.8rem;">Brute Force + Supply Chain</span></div>
</div>
</div>

<div style="overflow-x: auto; margin: 0 0 2rem 0; border: 1px solid rgba(16,185,129,0.2); border-radius: 12px; background: #05070f; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
<div style="padding: 14px 18px; background: rgba(16,185,129,0.07); border-bottom: 1px solid rgba(16,185,129,0.15);">
<span style="font-size: 0.82rem; font-weight: 700; color: #10b981; text-transform: uppercase; letter-spacing: 0.06em;"><i class="fas fa-tools mr-2"></i>CMS Exploitation Tools Comparison</span>
<a href="https://www.mobiloud.com/blog/cms-market-share" target="_blank" style="float:right; font-size:0.72rem; color:#64748b; text-decoration:none;">CMS Market Share Reference ↗</a>
</div>
<table style="width: 100%; border-collapse: collapse; font-size: 0.8rem;">
<thead>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06);">
<th style="padding: 10px 14px; color: #10b981; font-weight: 700; text-align: left;">Tool</th>
<th style="padding: 10px 14px; color: #10b981; font-weight: 700; text-align: left;">Targeted CMS</th>
<th style="padding: 10px 14px; color: #10b981; font-weight: 700; text-align: left;">Capabilities</th>
<th style="padding: 10px 14px; color: #10b981; font-weight: 700; text-align: left;">Ease</th>
<th style="padding: 10px 14px; color: #10b981; font-weight: 700; text-align: left;">Notable Features</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(59,130,246,0.04);">
<td style="padding:10px 14px;"><span style="color:#3b82f6; font-weight:700; font-family:monospace;">WPScan</span></td>
<td style="padding:10px 14px; color:#cbd5e1;">WordPress</td>
<td style="padding:10px 14px; color:#94a3b8; font-size:0.77rem;">Scanning, vuln detection, brute force</td>
<td style="padding:10px 14px;"><span style="background:rgba(61,220,132,0.12); color:#3ddc84; padding:2px 8px; border-radius:10px; font-size:0.72rem; font-weight:700;">Easy</span></td>
<td style="padding:10px 14px; color:#94a3b8; font-size:0.77rem;">Large vuln DB, API integration</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td style="padding:10px 14px;"><span style="color:#fb923c; font-weight:700; font-family:monospace;">JoomScan</span></td>
<td style="padding:10px 14px; color:#cbd5e1;">Joomla</td>
<td style="padding:10px 14px; color:#94a3b8; font-size:0.77rem;">Scanning, vuln detection, component analysis</td>
<td style="padding:10px 14px;"><span style="background:rgba(251,191,36,0.12); color:#fbbf24; padding:2px 8px; border-radius:10px; font-size:0.72rem; font-weight:700;">Medium</span></td>
<td style="padding:10px 14px; color:#94a3b8; font-size:0.77rem;">Detects misconfigs &amp; outdated plugins</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(99,102,241,0.04);">
<td style="padding:10px 14px;"><span style="color:#6366f1; font-weight:700; font-family:monospace;">Droopescan</span></td>
<td style="padding:10px 14px; color:#cbd5e1;">Drupal, SilverStripe, WordPress, Joomla, Moodle</td>
<td style="padding:10px 14px; color:#94a3b8; font-size:0.77rem;">Enumeration, vulnerability scanning</td>
<td style="padding:10px 14px;"><span style="background:rgba(251,191,36,0.12); color:#fbbf24; padding:2px 8px; border-radius:10px; font-size:0.72rem; font-weight:700;">Medium</span></td>
<td style="padding:10px 14px; color:#94a3b8; font-size:0.77rem;">Supports multiple CMS platforms</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td style="padding:10px 14px;"><span style="color:#10b981; font-weight:700; font-family:monospace;">CMSmap</span></td>
<td style="padding:10px 14px; color:#cbd5e1;">WordPress, Joomla, Drupal</td>
<td style="padding:10px 14px; color:#94a3b8; font-size:0.77rem;">Scanning, brute-force, enumeration</td>
<td style="padding:10px 14px;"><span style="background:rgba(251,191,36,0.12); color:#fbbf24; padding:2px 8px; border-radius:10px; font-size:0.72rem; font-weight:700;">Medium</span></td>
<td style="padding:10px 14px; color:#94a3b8; font-size:0.77rem;">Plugin &amp; theme vulnerability detection</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(0,240,255,0.04);">
<td style="padding:10px 14px;"><span style="color:#00f0ff; font-weight:700; font-family:monospace;">CMSeek</span></td>
<td style="padding:10px 14px; color:#cbd5e1;">160+ CMS (WordPress, Joomla, Drupal, etc.)</td>
<td style="padding:10px 14px; color:#94a3b8; font-size:0.77rem;">CMS detection, vuln scanning, brute-force</td>
<td style="padding:10px 14px;"><span style="background:rgba(61,220,132,0.12); color:#3ddc84; padding:2px 8px; border-radius:10px; font-size:0.72rem; font-weight:700;">Easy</span></td>
<td style="padding:10px 14px; color:#94a3b8; font-size:0.77rem;">Identifies CMS type &amp; potential vulns</td>
</tr>
<tr>
<td style="padding:10px 14px;"><span style="color:#ef4444; font-weight:700; font-family:monospace;">Metasploit</span></td>
<td style="padding:10px 14px; color:#cbd5e1;">Multiple CMS</td>
<td style="padding:10px 14px; color:#94a3b8; font-size:0.77rem;">Exploit execution, payload delivery, privilege escalation</td>
<td style="padding:10px 14px;"><span style="background:rgba(239,68,68,0.12); color:#ef4444; padding:2px 8px; border-radius:10px; font-size:0.72rem; font-weight:700;">Hard</span></td>
<td style="padding:10px 14px; color:#94a3b8; font-size:0.77rem;">Contains CMS-specific exploits in DB</td>
</tr>
</tbody>
</table>
</div>

---

<div style="margin: 2rem 0;">
<div style="font-size: 1.1rem; font-weight: 800; color: #3b82f6; margin-bottom: 6px; text-shadow: 0 0 8px rgba(59,130,246,0.4);">🔵 WPScan — WordPress Security Scanner</div>
<div style="height: 2px; background: linear-gradient(90deg, #3b82f6, transparent); margin-bottom: 18px; border-radius: 1px;"></div>

<div style="background: #05070f; border: 1px solid rgba(59,130,246,0.15); border-radius: 12px; padding: 20px; margin-bottom: 16px; box-shadow: 0 8px 24px rgba(0,0,0,0.4);">
<p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.75; margin: 0 0 12px 0;"><strong style="color: #ffffff;">WPScan</strong> (WordPress Security Scanner) คือ open-source security scanner ที่ออกแบบมาเฉพาะสำหรับ <strong style="color: #3b82f6;">WordPress</strong> ใช้อย่างแพร่หลายโดย security professionals, ethical hackers และผู้ดูแลระบบเพื่อค้นหาช่องโหว่ใน WordPress websites รองรับทั้ง Linux, macOS และ Windows (via WSL)</p>
<div style="font-family: monospace; font-size: 0.82rem; color: #00f0ff; background: rgba(0,0,0,0.3); padding: 10px 14px; border-radius: 6px; border-left: 3px solid #3b82f6;">wpscan --url &lt;target_url&gt;</div>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 16px;">
<div style="background: #05070f; border: 1px solid rgba(59,130,246,0.12); border-radius: 10px; overflow: hidden;">
<div style="padding: 10px 14px; background: rgba(59,130,246,0.07); border-bottom: 1px solid rgba(59,130,246,0.12);">
<span style="font-size: 0.78rem; font-weight: 700; color: #3b82f6; text-transform: uppercase; letter-spacing: 0.05em;"><i class="fas fa-list mr-2"></i>Enumeration Options (--enumerate)</span>
</div>
<table style="width: 100%; border-collapse: collapse; font-size: 0.78rem;">
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-weight:600;">v</td><td style="padding:7px 12px; color:#94a3b8;">Enumerate WordPress version</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-weight:600;">p</td><td style="padding:7px 12px; color:#94a3b8;">Enumerate plugins</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-weight:600;">vp</td><td style="padding:7px 12px; color:#94a3b8;">Enumerate <strong style="color:#ef4444;">vulnerable</strong> plugins</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-weight:600;">t</td><td style="padding:7px 12px; color:#94a3b8;">Enumerate themes</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-weight:600;">vt</td><td style="padding:7px 12px; color:#94a3b8;">Enumerate <strong style="color:#ef4444;">vulnerable</strong> themes</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-weight:600;">u</td><td style="padding:7px 12px; color:#94a3b8;">Enumerate WordPress users</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-weight:600;">cb</td><td style="padding:7px 12px; color:#94a3b8;">Enumerate config backups</td></tr>
<tr><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-weight:600;">m</td><td style="padding:7px 12px; color:#94a3b8;">Enumerate media (attachments)</td></tr>
</tbody>
</table>
</div>
<div style="background: #05070f; border: 1px solid rgba(59,130,246,0.12); border-radius: 10px; overflow: hidden;">
<div style="padding: 10px 14px; background: rgba(59,130,246,0.07); border-bottom: 1px solid rgba(59,130,246,0.12);">
<span style="font-size: 0.78rem; font-weight: 700; color: #3b82f6; text-transform: uppercase; letter-spacing: 0.05em;"><i class="fas fa-cog mr-2"></i>Additional Options</span>
</div>
<table style="width: 100%; border-collapse: collapse; font-size: 0.78rem;">
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem; white-space:nowrap;">--random-user-agent</td><td style="padding:7px 12px; color:#94a3b8;">Random User-Agent เพื่อหลบการตรวจจับ</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem; white-space:nowrap;">--proxy &lt;ip:port&gt;</td><td style="padding:7px 12px; color:#94a3b8;">ใช้ proxy เพื่อซ่อน IP</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem; white-space:nowrap;">--disable-tls-checks</td><td style="padding:7px 12px; color:#94a3b8;">ปิดการตรวจ SSL/TLS certificate</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem; white-space:nowrap;">--timeout &lt;seconds&gt;</td><td style="padding:7px 12px; color:#94a3b8;">กำหนด request timeout</td></tr>
<tr><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem; white-space:nowrap;">--threads &lt;num&gt;</td><td style="padding:7px 12px; color:#94a3b8;">จำนวน concurrent threads เพื่อเร่งความเร็ว</td></tr>
</tbody>
</table>
</div>
</div>

<div style="background: #05070f; border: 1px solid rgba(59,130,246,0.1); border-left: 3px solid #3b82f6; border-radius: 8px; padding: 16px; margin-bottom: 1.5rem;">
<div style="font-size: 0.8rem; font-weight: 700; color: #3b82f6; margin-bottom: 12px;"><i class="fas fa-terminal mr-2"></i>WPScan — ตัวอย่างการใช้งานจริงพร้อมคำอธิบาย</div>
<div style="display: flex; flex-direction: column; gap: 10px;">
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 12px;">
<div style="font-size: 0.72rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">1. สแกนหาช่องโหว่ปลั๊กอินที่ล้าสมัย (Enumerate Vulnerable Plugins)</div>
<div style="font-family: monospace; font-size: 0.78rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#3b82f6;">wpscan</span> --url <span style="color:#fbbf24;">https://example.com</span> --enumerate <span style="color:#ff007f;">vp</span></div>
<div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">→ ค้นหา plugin ที่มีช่องโหว่ที่ทราบและรายงาน CVE ที่เกี่ยวข้อง</div>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 12px;">
<div style="font-size: 0.72rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">2. Brute Force Login พร้อม Password List</div>
<div style="font-family: monospace; font-size: 0.78rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#3b82f6;">wpscan</span> --url <span style="color:#fbbf24;">https://example.com</span> --passwords <span style="color:#ff007f;">rockyou.txt</span> --usernames <span style="color:#ff007f;">admin</span></div>
<div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">→ ลองรหัสผ่านทุกอันจาก wordlist กับ username "admin" จนกว่าจะสำเร็จ</div>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 12px;">
<div style="font-size: 0.72rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">3. ค้นหา Users และ Plugins พร้อมกัน</div>
<div style="font-family: monospace; font-size: 0.78rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#3b82f6;">wpscan</span> --url <span style="color:#fbbf24;">https://example.com</span> --enumerate <span style="color:#ff007f;">u,p</span></div>
<div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">→ ดึงรายชื่อ user accounts และ plugins ที่ติดตั้งออกมาพร้อมกัน</div>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 12px;">
<div style="font-size: 0.72rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">4. Full Advanced Scan พร้อม API Key + บันทึกผลเป็น JSON</div>
<div style="font-family: monospace; font-size: 0.78rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#3b82f6;">wpscan</span> --url <span style="color:#fbbf24;">https://example.com</span> \
  --enumerate <span style="color:#ff007f;">vp,vt,u</span> \
  --random-user-agent \
  --api-token <span style="color:#ff007f;">YOUR_API_KEY</span> \
  --output report.json --format json</div>
<div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">→ สแกนครบทั้ง vulnerable plugins, vulnerable themes, users + หลบ WAF + บันทึกผลลัพธ์เป็น JSON</div>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 12px;">
<div style="font-size: 0.72rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">5. ใช้ Proxy เพื่อซ่อน IP (Route ผ่าน Burp Suite)</div>
<div style="font-family: monospace; font-size: 0.78rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#3b82f6;">wpscan</span> --url <span style="color:#fbbf24;">https://example.com</span> --proxy <span style="color:#ff007f;">127.0.0.1:8080</span></div>
<div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">→ ส่งทราฟฟิกทั้งหมดผ่าน proxy เช่น Burp Suite เพื่อ intercept/analyze request</div>
</div>
</div>
</div>
</div>

---

<div style="margin: 2rem 0;">
<div style="font-size: 1.1rem; font-weight: 800; color: #fb923c; margin-bottom: 6px; text-shadow: 0 0 8px rgba(251,146,60,0.4);">🟠 JoomScan — Joomla Security Scanner</div>
<div style="height: 2px; background: linear-gradient(90deg, #fb923c, transparent); margin-bottom: 18px; border-radius: 1px;"></div>

<div style="background: #05070f; border: 1px solid rgba(251,146,60,0.15); border-radius: 12px; padding: 20px; margin-bottom: 16px;">
<p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.75; margin: 0 0 10px 0;"><strong style="color: #ffffff;">JoomScan</strong> (Joomla Security Scanner) คือ open-source security tool ที่พัฒนาโดย <strong style="color: #fb923c;">OWASP</strong> ออกแบบมาเฉพาะสำหรับสแกน Joomla websites ต้องใช้ <code style="color:#fbbf24; background:rgba(255,255,255,0.05); padding:1px 5px; border-radius:3px;">Perl</code> และรองรับ Linux, macOS, Windows (via WSL)</p>
<a href="https://www.geeksforgeeks.org/joomscan-vulnerability-scanner-tool-in-kali-linux/" target="_blank" style="font-size: 0.75rem; color: #fb923c; background: rgba(251,146,60,0.08); border: 1px solid rgba(251,146,60,0.25); padding: 4px 10px; border-radius: 20px; text-decoration: none; display: inline-block;"><i class="fas fa-external-link-alt mr-1"></i>JoomScan on Kali Linux Guide</a>
</div>

<div style="overflow-x: auto; margin: 0 0 16px 0; border: 1px solid rgba(251,146,60,0.15); border-radius: 10px; background: #05070f;">
<div style="padding: 10px 14px; background: rgba(251,146,60,0.06); border-bottom: 1px solid rgba(251,146,60,0.12);">
<span style="font-size: 0.78rem; font-weight: 700; color: #fb923c; text-transform: uppercase; letter-spacing: 0.05em;"><i class="fas fa-cog mr-2"></i>JoomScan Command Options</span>
</div>
<table style="width: 100%; border-collapse: collapse; font-size: 0.8rem;">
<thead><tr style="border-bottom:1px solid rgba(255,255,255,0.06);"><th style="padding:8px 14px; color:#fb923c; font-weight:700; text-align:left;">Command Option</th><th style="padding:8px 14px; color:#fb923c; font-weight:700; text-align:left;">Description</th></tr></thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem; white-space:nowrap;">-u &lt;target_url&gt;</td><td style="padding:8px 14px; color:#94a3b8;">สแกน Joomla website ที่ระบุ</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem; white-space:nowrap;">--joomla-version</td><td style="padding:8px 14px; color:#94a3b8;">ตรวจสอบ Joomla version ที่รันอยู่บน target</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem; white-space:nowrap;">--components</td><td style="padding:8px 14px; color:#94a3b8;">สแกนหา Joomla components, extensions และ plugins ที่มีช่องโหว่</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem; white-space:nowrap;">--enumerate-users</td><td style="padding:8px 14px; color:#94a3b8;">ดึงรายชื่อ Joomla user accounts</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem; white-space:nowrap;">--backup-files</td><td style="padding:8px 14px; color:#94a3b8;">ค้นหาไฟล์ backup, config และ sensitive files ที่เปิดเผย</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem; white-space:nowrap;">--xss</td><td style="padding:8px 14px; color:#94a3b8;">ตรวจสอบช่องโหว่ Cross-Site Scripting (XSS)</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem; white-space:nowrap;">--sql-injection</td><td style="padding:8px 14px; color:#94a3b8;">ทดสอบช่องโหว่ SQL Injection</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem; white-space:nowrap;">-o &lt;output-file&gt;</td><td style="padding:8px 14px; color:#94a3b8;">บันทึกผลการสแกนลงไฟล์</td></tr>
<tr><td style="padding:8px 14px; color:#ff007f; font-family:monospace; font-size:0.76rem; white-space:nowrap;">--verbose</td><td style="padding:8px 14px; color:#94a3b8;">แสดงผลลัพธ์แบบละเอียด</td></tr>
</tbody>
</table>
</div>

<div style="background: #05070f; border: 1px solid rgba(251,146,60,0.1); border-left: 3px solid #fb923c; border-radius: 8px; padding: 16px; margin-bottom: 1.5rem;">
<div style="font-size: 0.8rem; font-weight: 700; color: #fb923c; margin-bottom: 12px;"><i class="fas fa-terminal mr-2"></i>JoomScan — ตัวอย่างการใช้งานจริงพร้อมคำอธิบาย</div>
<div style="display: flex; flex-direction: column; gap: 10px;">
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 12px;">
<div style="font-size: 0.72rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">1. สแกนหาช่องโหว่ทั่วไปของ Joomla</div>
<div style="font-family: monospace; font-size: 0.78rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#fb923c;">joomscan</span> -u <span style="color:#fbbf24;">https://example.com</span></div>
<div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">→ Full vulnerability scan ตรวจหาช่องโหว่ที่รู้จักใน Joomla core, config และ components</div>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 12px;">
<div style="font-size: 0.72rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">2. ตรวจสอบ Joomla Version เพื่อหา CVE</div>
<div style="font-family: monospace; font-size: 0.78rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#fb923c;">joomscan</span> -u <span style="color:#fbbf24;">https://example.com</span> --joomla-version</div>
<div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">→ ระบุ version ที่ใช้งาน เพื่อค้นหา CVE ที่ตรงกับเวอร์ชั่นนั้นๆ</div>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 12px;">
<div style="font-size: 0.72rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">3. สแกน Components และ Plugins ที่มีช่องโหว่</div>
<div style="font-family: monospace; font-size: 0.78rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#fb923c;">joomscan</span> -u <span style="color:#fbbf24;">https://example.com</span> --components</div>
<div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">→ แสดงรายการ Joomla components และ extensions ทั้งหมด พร้อมแจ้งเตือนว่าอันไหนมีช่องโหว่</div>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 12px;">
<div style="font-size: 0.72rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">4. ดึงรายชื่อ User Accounts ของ Joomla</div>
<div style="font-family: monospace; font-size: 0.78rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#fb923c;">joomscan</span> -u <span style="color:#fbbf24;">https://example.com</span> --enumerate-users</div>
<div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">→ ดึง username list ออกมา จากนั้นนำไปใช้ใน Brute Force attack ต่อได้</div>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 12px;">
<div style="font-size: 0.72rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">5. บันทึกผลการสแกนลงไฟล์</div>
<div style="font-family: monospace; font-size: 0.78rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#fb923c;">joomscan</span> -u <span style="color:#fbbf24;">https://example.com</span> -o <span style="color:#ff007f;">report.txt</span></div>
<div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">→ บันทึกผลลัพธ์ทั้งหมดลงไฟล์ text เพื่อนำไปวิเคราะห์ต่อหรือทำ pentest report</div>
</div>
</div>
</div>
</div>

---

<div style="margin: 2rem 0;">
<div style="font-size: 1.1rem; font-weight: 800; color: #6366f1; margin-bottom: 6px; text-shadow: 0 0 8px rgba(99,102,241,0.4);">🟣 Droopescan — Multi-CMS Vulnerability Scanner</div>
<div style="height: 2px; background: linear-gradient(90deg, #6366f1, transparent); margin-bottom: 18px; border-radius: 1px;"></div>

<div style="background: #05070f; border: 1px solid rgba(99,102,241,0.15); border-radius: 12px; padding: 20px; margin-bottom: 16px;">
<p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.75; margin: 0 0 10px 0;"><strong style="color: #ffffff;">Droopescan</strong> คือ open-source scanner ที่ค้นหาช่องโหว่ใน CMS หลายระบบ ได้แก่ <strong style="color: #6366f1;">Drupal, WordPress, SilverStripe, Joomla, Moodle</strong> โดยทำ enumeration และ fingerprinting เพื่อตรวจจับ outdated versions, plugins, themes และ misconfigurations</p>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 10px 14px; font-family: monospace; font-size: 0.8rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#64748b;"># ติดตั้ง Droopescan</span>
git clone https://github.com/droope/droopescan.git
cd droopescan
pip install -r requirements.txt</div>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 16px;">
<div style="background: #05070f; border: 1px solid rgba(99,102,241,0.12); border-radius: 10px; overflow: hidden;">
<div style="padding: 10px 14px; background: rgba(99,102,241,0.07); border-bottom: 1px solid rgba(99,102,241,0.12);">
<span style="font-size: 0.78rem; font-weight: 700; color: #6366f1; text-transform: uppercase; letter-spacing: 0.05em;"><i class="fas fa-sitemap mr-2"></i>Supported CMS Scan Commands</span>
</div>
<table style="width: 100%; border-collapse: collapse; font-size: 0.78rem;">
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:7px 12px; color:#6366f1; font-weight:600; white-space:nowrap;">Drupal</td><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem;">droopescan scan drupal -u &lt;url&gt;</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:7px 12px; color:#6366f1; font-weight:600;">Joomla</td><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem;">droopescan scan joomla -u &lt;url&gt;</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:7px 12px; color:#6366f1; font-weight:600;">WordPress</td><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem;">droopescan scan wordpress -u &lt;url&gt;</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:7px 12px; color:#6366f1; font-weight:600;">SilverStripe</td><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem;">droopescan scan silverstripe -u &lt;url&gt;</td></tr>
<tr><td style="padding:7px 12px; color:#6366f1; font-weight:600;">Moodle</td><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem;">droopescan scan moodle -u &lt;url&gt;</td></tr>
</tbody>
</table>
</div>
<div style="background: #05070f; border: 1px solid rgba(99,102,241,0.12); border-radius: 10px; overflow: hidden;">
<div style="padding: 10px 14px; background: rgba(99,102,241,0.07); border-bottom: 1px solid rgba(99,102,241,0.12);">
<span style="font-size: 0.78rem; font-weight: 700; color: #6366f1; text-transform: uppercase; letter-spacing: 0.05em;"><i class="fas fa-list-ul mr-2"></i>Enumeration Options (-e)</span>
</div>
<table style="width: 100%; border-collapse: collapse; font-size: 0.78rem;">
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.76rem;">themes</td><td style="padding:7px 12px; color:#94a3b8;">Detects installed themes</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.76rem;">plugins</td><td style="padding:7px 12px; color:#94a3b8;">Lists installed plugins/modules</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.76rem;">versions</td><td style="padding:7px 12px; color:#94a3b8;">Identifies CMS version</td></tr>
<tr><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.76rem;">default-files</td><td style="padding:7px 12px; color:#94a3b8;">Finds exposed default CMS files</td></tr>
</tbody>
</table>
</div>
</div>

<div style="background: #05070f; border: 1px solid rgba(99,102,241,0.1); border-left: 3px solid #6366f1; border-radius: 8px; padding: 16px; margin-bottom: 1.5rem;">
<div style="font-size: 0.8rem; font-weight: 700; color: #6366f1; margin-bottom: 12px;"><i class="fas fa-terminal mr-2"></i>Droopescan — ตัวอย่างการใช้งานจริงพร้อมคำอธิบาย</div>
<div style="display: flex; flex-direction: column; gap: 10px;">
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 12px;">
<div style="font-size: 0.72rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">1. เพิ่มความเร็วสแกนด้วย Multi-threading</div>
<div style="font-family: monospace; font-size: 0.78rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#6366f1;">droopescan</span> scan joomla -u <span style="color:#fbbf24;">https://example.com</span> -t <span style="color:#ff007f;">10</span></div>
<div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">→ รัน 10 threads พร้อมกัน ทำให้สแกนเสร็จเร็วขึ้น 10 เท่าบนเครือข่ายที่เร็ว</div>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 12px;">
<div style="font-size: 0.72rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">2. สแกน Plugins ที่ติดตั้งบน Drupal</div>
<div style="font-family: monospace; font-size: 0.78rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#6366f1;">droopescan</span> scan drupal -u <span style="color:#fbbf24;">https://example.com</span> -e <span style="color:#ff007f;">plugins</span></div>
<div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">→ ระบุรายชื่อ Drupal modules/plugins ที่ติดตั้งอยู่ทั้งหมด</div>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 12px;">
<div style="font-size: 0.72rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">3. Full Scan ทุกประเภทพร้อมบันทึกผล</div>
<div style="font-family: monospace; font-size: 0.78rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#6366f1;">droopescan</span> scan drupal -u <span style="color:#fbbf24;">https://example.com</span> \
  -e <span style="color:#ff007f;">plugins,themes,versions,default-files</span> \
  -t <span style="color:#ff007f;">10</span> -o <span style="color:#ff007f;">drupal_scan.txt</span></div>
<div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">→ สแกน plugins, themes, version และ default files พร้อมกัน ด้วย 10 threads แล้วบันทึกผล</div>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 12px;">
<div style="font-size: 0.72rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">4. สแกนผ่าน Proxy</div>
<div style="font-family: monospace; font-size: 0.78rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#6366f1;">droopescan</span> scan moodle -u <span style="color:#fbbf24;">https://example.com</span> --proxy <span style="color:#ff007f;">127.0.0.1:8080</span></div>
<div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">→ Route traffic ผ่าน proxy (เช่น Burp Suite) เพื่อ intercept และวิเคราะห์ request ที่ส่งออกไป</div>
</div>
</div>
</div>
</div>

---

<div style="margin: 2rem 0;">
<div style="font-size: 1.1rem; font-weight: 800; color: #10b981; margin-bottom: 6px; text-shadow: 0 0 8px rgba(16,185,129,0.4);">🟢 CMSmap — Automated CMS Penetration Testing</div>
<div style="height: 2px; background: linear-gradient(90deg, #10b981, transparent); margin-bottom: 18px; border-radius: 1px;"></div>

<div style="background: #05070f; border: 1px solid rgba(16,185,129,0.15); border-radius: 12px; padding: 20px; margin-bottom: 16px;">
<p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.75; margin: 0 0 10px 0;"><strong style="color: #ffffff;">CMSmap</strong> คือ automated security scanner สำหรับ <strong style="color: #10b981;">WordPress, Joomla, Drupal</strong> ทำงานอัตโนมัติในการสแกน enumeration, plugin scanning และ brute-force attacks ต้องใช้ Python 3</p>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 10px 14px; font-family: monospace; font-size: 0.8rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#64748b;"># ติดตั้ง CMSmap</span>
git clone https://github.com/Dionach/CMSmap.git
cd CMSmap && pip install -r requirements.txt</div>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 16px;">
<div style="background: #05070f; border: 1px solid rgba(16,185,129,0.12); border-radius: 10px; overflow: hidden;">
<div style="padding: 10px 14px; background: rgba(16,185,129,0.07); border-bottom: 1px solid rgba(16,185,129,0.12);">
<span style="font-size: 0.78rem; font-weight: 700; color: #10b981; text-transform: uppercase; letter-spacing: 0.05em;"><i class="fas fa-flag mr-2"></i>Scan per CMS (-f flag)</span>
</div>
<table style="width: 100%; border-collapse: collapse; font-size: 0.78rem;">
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:7px 12px; color:#3b82f6; font-weight:600;">WordPress</td><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem;">python3 cmsmap.py -t &lt;url&gt; -f W</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:7px 12px; color:#fb923c; font-weight:600;">Joomla</td><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem;">python3 cmsmap.py -t &lt;url&gt; -f J</td></tr>
<tr><td style="padding:7px 12px; color:#6366f1; font-weight:600;">Drupal</td><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem;">python3 cmsmap.py -t &lt;url&gt; -f D</td></tr>
</tbody>
</table>
</div>
<div style="background: #05070f; border: 1px solid rgba(16,185,129,0.12); border-radius: 10px; overflow: hidden;">
<div style="padding: 10px 14px; background: rgba(16,185,129,0.07); border-bottom: 1px solid rgba(16,185,129,0.12);">
<span style="font-size: 0.78rem; font-weight: 700; color: #10b981; text-transform: uppercase; letter-spacing: 0.05em;"><i class="fas fa-cog mr-2"></i>Command Options</span>
</div>
<table style="width: 100%; border-collapse: collapse; font-size: 0.78rem;">
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace;">-u</td><td style="padding:7px 12px; color:#94a3b8; font-size:0.76rem;">Enumerate CMS users</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace;">-e</td><td style="padding:7px 12px; color:#94a3b8; font-size:0.76rem;">Detect plugins, themes, versions</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace;">-d</td><td style="padding:7px 12px; color:#94a3b8; font-size:0.76rem;">Dictionary attack for credentials</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace;">-w &lt;wordlist&gt;</td><td style="padding:7px 12px; color:#94a3b8; font-size:0.76rem;">Custom wordlist for brute-force</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace;">-o &lt;file&gt;</td><td style="padding:7px 12px; color:#94a3b8; font-size:0.76rem;">Save results to file</td></tr>
<tr><td style="padding:7px 12px; color:#ff007f; font-family:monospace;">-v</td><td style="padding:7px 12px; color:#94a3b8; font-size:0.76rem;">Verbose mode</td></tr>
</tbody>
</table>
</div>
</div>

<div style="background: #05070f; border: 1px solid rgba(16,185,129,0.1); border-left: 3px solid #10b981; border-radius: 8px; padding: 16px; margin-bottom: 1.5rem;">
<div style="font-size: 0.8rem; font-weight: 700; color: #10b981; margin-bottom: 12px;"><i class="fas fa-terminal mr-2"></i>CMSmap — ตัวอย่างการใช้งานจริงพร้อมคำอธิบาย</div>
<div style="display: flex; flex-direction: column; gap: 10px;">
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 12px;">
<div style="font-size: 0.72rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">1. ดึงรายชื่อ Users ของ CMS</div>
<div style="font-family: monospace; font-size: 0.78rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#10b981;">python3 cmsmap.py</span> -t <span style="color:#fbbf24;">https://example.com</span> -u</div>
<div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">→ enumerate user accounts ทั้งหมด เพื่อนำ username list ไปใช้ใน Brute Force ต่อ</div>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 12px;">
<div style="font-size: 0.72rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">2. Brute Force ด้วย Custom Wordlist บน Joomla</div>
<div style="font-family: monospace; font-size: 0.78rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#10b981;">python3 cmsmap.py</span> -t <span style="color:#fbbf24;">https://example.com</span> -f J -d -w <span style="color:#ff007f;">joomla_wordlist.txt</span></div>
<div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">→ โจมตีระบบ login ของ Joomla ด้วยรหัสผ่านจาก wordlist แบบ automated</div>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 12px;">
<div style="font-size: 0.72rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">3. Full WordPress Scan พร้อมบันทึกผลและ Verbose Mode</div>
<div style="font-family: monospace; font-size: 0.78rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#10b981;">python3 cmsmap.py</span> -t <span style="color:#fbbf24;">https://example.com</span> \
  -f <span style="color:#ff007f;">W</span> -e -u -v -o <span style="color:#ff007f;">wp_scan.txt</span></div>
<div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">→ สแกน WordPress แบบสมบูรณ์: enumerate plugins, themes, users + verbose mode + บันทึกผล</div>
</div>
</div>
</div>
</div>

---

<div style="margin: 2rem 0;">
<div style="font-size: 1.1rem; font-weight: 800; color: #00f0ff; margin-bottom: 6px; text-shadow: 0 0 8px rgba(0,240,255,0.4);">🔵 CMSeek — Universal CMS Detection & Exploitation</div>
<div style="height: 2px; background: linear-gradient(90deg, #00f0ff, transparent); margin-bottom: 18px; border-radius: 1px;"></div>

<div style="background: #05070f; border: 1px solid rgba(0,240,255,0.15); border-radius: 12px; padding: 20px; margin-bottom: 16px;">
<p style="color: #cbd5e1; font-size: 0.88rem; line-height: 1.75; margin: 0 0 10px 0;"><strong style="color: #ffffff;">CMSeek</strong> คือ powerful CMS detection และ vulnerability scanning tool ที่รองรับ <strong style="color: #00f0ff;">กว่า 160 CMS</strong> ตรวจจับ CMS type, enumerate themes/plugins และค้นหาช่องโหว่ใน WordPress, Joomla, Drupal, Magento</p>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 10px 14px; font-family: monospace; font-size: 0.8rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#64748b;"># ติดตั้ง CMSeek</span>
sudo apt-get install cmseek</div>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 16px;">
<div style="background: #05070f; border: 1px solid rgba(0,240,255,0.12); border-radius: 10px; overflow: hidden;">
<div style="padding: 10px 14px; background: rgba(0,240,255,0.06); border-bottom: 1px solid rgba(0,240,255,0.12);">
<span style="font-size: 0.78rem; font-weight: 700; color: #00f0ff; text-transform: uppercase; letter-spacing: 0.05em;"><i class="fas fa-cog mr-2"></i>General Options</span>
</div>
<table style="width: 100%; border-collapse: collapse; font-size: 0.78rem;">
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem; white-space:nowrap;">-u &lt;target-url&gt;</td><td style="padding:7px 12px; color:#94a3b8; font-size:0.76rem;">Target URL for scanning</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem; white-space:nowrap;">-l &lt;list&gt;</td><td style="padding:7px 12px; color:#94a3b8; font-size:0.76rem;">Scan multiple targets from file</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem; white-space:nowrap;">-o &lt;output-dir&gt;</td><td style="padding:7px 12px; color:#94a3b8; font-size:0.76rem;">Save results to directory</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem; white-space:nowrap;">--headers</td><td style="padding:7px 12px; color:#94a3b8; font-size:0.76rem;">Display HTTP headers</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem; white-space:nowrap;">--cms</td><td style="padding:7px 12px; color:#94a3b8; font-size:0.76rem;">Detect CMS without full scan</td></tr>
<tr><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem; white-space:nowrap;">--follow-redirect</td><td style="padding:7px 12px; color:#94a3b8; font-size:0.76rem;">Follow redirects during scan</td></tr>
</tbody>
</table>
</div>
<div style="background: #05070f; border: 1px solid rgba(0,240,255,0.12); border-radius: 10px; overflow: hidden;">
<div style="padding: 10px 14px; background: rgba(0,240,255,0.06); border-bottom: 1px solid rgba(0,240,255,0.12);">
<span style="font-size: 0.78rem; font-weight: 700; color: #00f0ff; text-transform: uppercase; letter-spacing: 0.05em;"><i class="fas fa-search mr-2"></i>CMS-Specific Enumeration</span>
</div>
<table style="width: 100%; border-collapse: collapse; font-size: 0.78rem;">
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem; white-space:nowrap;">--wp</td><td style="padding:7px 12px; color:#94a3b8; font-size:0.76rem;">WordPress vulns, themes &amp; plugins</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem; white-space:nowrap;">--joomla</td><td style="padding:7px 12px; color:#94a3b8; font-size:0.76rem;">Joomla vulns, extensions, components</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem; white-space:nowrap;">--drupal</td><td style="padding:7px 12px; color:#94a3b8; font-size:0.76rem;">Drupal vulns, modules &amp; themes</td></tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(255,255,255,0.005);"><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem; white-space:nowrap;">--magento</td><td style="padding:7px 12px; color:#94a3b8; font-size:0.76rem;">Magento security issues</td></tr>
<tr><td style="padding:7px 12px; color:#ff007f; font-family:monospace; font-size:0.73rem; white-space:nowrap;">--brute</td><td style="padding:7px 12px; color:#94a3b8; font-size:0.76rem;">Brute-force with default wordlist</td></tr>
</tbody>
</table>
</div>
</div>

<div style="background: #05070f; border: 1px solid rgba(0,240,255,0.1); border-left: 3px solid #00f0ff; border-radius: 8px; padding: 16px; margin-bottom: 1.5rem;">
<div style="font-size: 0.8rem; font-weight: 700; color: #00f0ff; margin-bottom: 12px;"><i class="fas fa-terminal mr-2"></i>CMSeek — ตัวอย่างการใช้งานจริงพร้อมคำอธิบาย</div>
<div style="display: flex; flex-direction: column; gap: 10px;">
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 12px;">
<div style="font-size: 0.72rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">1. ตรวจจับ HTTP Headers เพื่อดู Server Info รั่วไหล</div>
<div style="font-family: monospace; font-size: 0.78rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#00f0ff;">cmseek</span> -u <span style="color:#fbbf24;">https://example.com</span> --headers</div>
<div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">→ แสดง HTTP headers เช่น Server, X-Powered-By ที่อาจเปิดเผยชนิด web server, PHP version หรือ CMS ที่ใช้งาน</div>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 12px;">
<div style="font-size: 0.72rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">2. ตรวจจับชนิด CMS โดยไม่สแกนช่องโหว่</div>
<div style="font-family: monospace; font-size: 0.78rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#00f0ff;">cmseek</span> -u <span style="color:#fbbf24;">https://example.com</span> --cms</div>
<div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">→ ระบุว่า website ใช้ CMS อะไร (WordPress, Joomla, Drupal, ฯลฯ) โดยใช้ fingerprinting จาก HTTP response และ file signatures</div>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 12px;">
<div style="font-size: 0.72rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">3. Full WordPress Scan — ช่องโหว่ + Plugins + Themes + Verbose + บันทึกผล</div>
<div style="font-family: monospace; font-size: 0.78rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#00f0ff;">cmseek</span> -u <span style="color:#fbbf24;">https://example.com</span> --wp -v -o <span style="color:#ff007f;">wp_scan_report/</span></div>
<div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">→ สแกน WordPress เต็มรูปแบบ: ค้นหา vulnerable plugins, themes, misconfigs + verbose mode + บันทึกเป็นไฟล์ JSON ใน folder ที่กำหนด</div>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 12px;">
<div style="font-size: 0.72rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">4. Joomla Scan พร้อม CMS Detection และ Component Enumeration</div>
<div style="font-family: monospace; font-size: 0.78rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#00f0ff;">cmseek</span> -u <span style="color:#fbbf24;">https://example.com</span> --joomla --cms -o <span style="color:#ff007f;">joomla_report/</span></div>
<div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">→ ตรวจ CMS type ก่อน แล้วสแกน Joomla vulns + components + extensions ทั้งหมด และบันทึกผลลัพธ์</div>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 12px;">
<div style="font-size: 0.72rem; color: #64748b; margin-bottom: 6px; font-weight: 600;">5. Scan หลาย Target พร้อมกันจากไฟล์</div>
<div style="font-family: monospace; font-size: 0.78rem; color: #94a3b8; white-space: pre-wrap;"><span style="color:#00f0ff;">cmseek</span> -l <span style="color:#ff007f;">targets.txt</span> --cms -o <span style="color:#ff007f;">bulk_scan_results/</span></div>
<div style="font-size: 0.72rem; color: #64748b; margin-top: 4px;">→ รับ URL list จากไฟล์ text แล้วตรวจจับ CMS ทุก target พร้อมกัน เหมาะสำหรับ bulk reconnaissance</div>
</div>
</div>
</div>
</div>
"""

with app.app_context():
    l = TutorialLesson.query.get(179)
    if l:
        blocks = json.loads(l.content)
        blocks[0]['value'] = NEW_BLOCK_0
        l.content = json.dumps(blocks, ensure_ascii=False)
        app.db.session.commit()
        print(f"Successfully rewrote Lesson 179 Block 0!")
        print(f"New Block 0 length: {len(NEW_BLOCK_0)} characters")
    else:
        print("ERROR: Lesson 179 not found!")
