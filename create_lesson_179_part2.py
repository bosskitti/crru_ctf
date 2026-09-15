import json
import os
import sys

def clean_html(raw_html: str) -> str:
    """Ensure no blank lines exist inside HTML block so markdown parser doesn't inject <p> tags."""
    return '\n'.join([line.strip() for line in raw_html.split('\n') if line.strip()])

# Read the first part (Hero banner + CMS Masterclass)
from create_lesson_179 import hero_banner_html, cms_masterclass_html

# =========================================================================
# 3. ENHANCED CMS SECURITY AUDIT SANDBOX (BLOCK 1)
# =========================================================================
cms_sandbox_html = """### 💻 CMS Security Audit Sandbox (จำลองเรียกสแกนความปลอดภัย CMS)

คลิกเลือกเครื่องมือด้านซ้ายมือเพื่อศึกษาขั้นตอน และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลการสแกนความเปราะบาง:

<style type="text/css">
.w-sandbox-main { display: flex !important; gap: 20px !important; margin: 1.5rem auto !important; max-width: 1000px !important; }
.w-sandbox-nav { width: 230px !important; display: flex !important; flex-direction: column !important; gap: 8px !important; flex-shrink: 0 !important; }
.w-nav-item { background: rgba(255, 255, 255, 0.02) !important; border: 1px solid rgba(255, 255, 255, 0.06) !important; border-radius: 8px !important; padding: 11px 14px !important; color: #cbd5e1 !important; text-align: left !important; cursor: pointer !important; font-size: 0.8rem !important; transition: all 0.2s !important; display: flex !important; align-items: center !important; gap: 8px !important; }
.w-nav-item:hover, .w-nav-item.active { border-color: #10b981 !important; color: #ffffff !important; background: rgba(16, 185, 129, 0.08) !important; }
.w-nav-item.active { font-weight: 700 !important; box-shadow: 0 0 12px rgba(16, 185, 129, 0.2) !important; }
.w-sandbox-panels { flex-grow: 1 !important; }
.w-sand-panel { background: #05070f !important; border: 1px solid rgba(255, 255, 255, 0.08) !important; border-radius: 12px !important; padding: 22px !important; box-shadow: 0 8px 28px rgba(0,0,0,0.5) !important; }
</style>
<div class="w-sandbox-main">
<div class="w-sandbox-nav">
<button id="nav-item-wpscan" class="w-nav-item active" onclick="showSandboxItem('wpscan', this)">
<span>🔵</span> 1. WPScan (WordPress)
</button>
<button id="nav-item-joomscan" class="w-nav-item" onclick="showSandboxItem('joomscan', this)">
<span>🟠</span> 2. JoomScan (Joomla)
</button>
<button id="nav-item-droopescan" class="w-nav-item" onclick="showSandboxItem('droopescan', this)">
<span>🟣</span> 3. Droopescan (Drupal)
</button>
<button id="nav-item-cmseek" class="w-nav-item" onclick="showSandboxItem('cmseek', this)">
<span>🟢</span> 4. CMSeek (Fingerprint)
</button>
</div>
<div class="w-sandbox-panels">

<!-- Panel 1: WPScan -->
<div id="panel-wpscan" class="w-sand-panel" style="display: block;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>1. สแกน WordPress ด้วย WPScan</span>
<span style="font-size: 0.68rem; padding: 2px 8px; border-radius: 4px; background: rgba(59,130,246,0.1); border: 1px solid rgba(59,130,246,0.3); color: #60a5fa; font-family: monospace;">WordPress Scanner</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #38bdf8; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.25); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.04);">wpscan --url http://target-wp.local/ --enumerate vp,u</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startPostSim('wpscan')" style="background: rgba(16,185,129,0.12); border: 1px solid rgba(16,185,129,0.35); border-radius: 4px; color: #34d399; font-size: 0.7rem; padding: 4px 10px; cursor: pointer; font-family: monospace; font-weight: 700;">▶ Run Simulation</button>
</div>
<div id="term-wpscan" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 95px;">
<span style="color: #3ddc84;">kali$</span> [กดปุ่ม Run Simulation เพื่อยิงสแกน WPScan]
</div>
</div>
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 14px; font-size: 0.82rem; color: #cbd5e1; line-height: 1.6;">
<strong style="color: #fbbf24;">💡 สิ่งที่ได้เรียนรู้:</strong> คำสั่งนี้ใช้แฟล็ก <code>--enumerate vp,u</code> เพื่อสแกนหาเฉพาะปลั๊กอินที่มีช่องโหว่ความปลอดภัย (vp) และแจกแจงรายชื่อ Username ผู้ใช้งาน (u)
</div>
</div>

<!-- Panel 2: JoomScan -->
<div id="panel-joomscan" class="w-sand-panel" style="display: none;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>2. ตรวจสอบ Joomla ด้วย JoomScan</span>
<span style="font-size: 0.68rem; padding: 2px 8px; border-radius: 4px; background: rgba(251,146,60,0.1); border: 1px solid rgba(251,146,60,0.3); color: #fb923c; font-family: monospace;">OWASP JoomScan</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #fb923c; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.25); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.04);">joomscan -u http://target-joomla.local/ --components</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startPostSim('joomscan')" style="background: rgba(16,185,129,0.12); border: 1px solid rgba(16,185,129,0.35); border-radius: 4px; color: #34d399; font-size: 0.7rem; padding: 4px 10px; cursor: pointer; font-family: monospace; font-weight: 700;">▶ Run Simulation</button>
</div>
<div id="term-joomscan" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 95px;">
<span style="color: #3ddc84;">kali$</span> [กดปุ่ม Run Simulation เพื่อเริ่มทำ JoomScan]
</div>
</div>
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 14px; font-size: 0.82rem; color: #cbd5e1; line-height: 1.6;">
<strong style="color: #fbbf24;">💡 สิ่งที่ได้เรียนรู้:</strong> JoomScan เจาะจงหาไฟล์คอนฟิกหลุด (เช่น <code>configuration.php.bak</code>) และส่วนประกอบเสริม (Components) ที่เปิดเผยข้อมูลสำคัญ
</div>
</div>

<!-- Panel 3: Droopescan -->
<div id="panel-droopescan" class="w-sand-panel" style="display: none;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>3. สแกน Drupal ด้วย Droopescan</span>
<span style="font-size: 0.68rem; padding: 2px 8px; border-radius: 4px; background: rgba(99,102,241,0.1); border: 1px solid rgba(99,102,241,0.3); color: #818cf8; font-family: monospace;">Droopescan Tool</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #818cf8; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.25); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.04);">droopescan scan drupal -u http://target-drupal.local/ -t 10</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startPostSim('droopescan')" style="background: rgba(16,185,129,0.12); border: 1px solid rgba(16,185,129,0.35); border-radius: 4px; color: #34d399; font-size: 0.7rem; padding: 4px 10px; cursor: pointer; font-family: monospace; font-weight: 700;">▶ Run Simulation</button>
</div>
<div id="term-droopescan" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 95px;">
<span style="color: #3ddc84;">kali$</span> [กดปุ่ม Run Simulation เพื่อเริ่มสแกน Droopescan]
</div>
</div>
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 14px; font-size: 0.82rem; color: #cbd5e1; line-height: 1.6;">
<strong style="color: #fbbf24;">💡 สิ่งที่ได้เรียนรู้:</strong> แฟล็ก <code>-t 10</code> สั่งเปิด 10 Threads พร้อมกัน สแกนทั้ง Modules, Themes และระบุเวอร์ชัน Drupal ได้อย่างแม่นยำ
</div>
</div>

<!-- Panel 4: CMSeek -->
<div id="panel-cmseek" class="w-sand-panel" style="display: none;">
<div style="font-size: 0.95rem; font-weight: 800; color: #ffffff; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 10px; margin-bottom: 14px; display: flex; justify-content: space-between; align-items: center;">
<span>4. สแกน Fingerprint ด้วย CMSeek</span>
<span style="font-size: 0.68rem; padding: 2px 8px; border-radius: 4px; background: rgba(0,240,255,0.1); border: 1px solid rgba(0,240,255,0.3); color: #00f0ff; font-family: monospace;">Multi-CMS Recon</span>
</div>
<pre style="font-family: monospace; font-size: 0.8rem; color: #00f0ff; white-space: pre-wrap; margin: 0 0 12px; background: rgba(0,0,0,0.25); padding: 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.04);">python3 cmseek.py -u http://target.local/ --cms</pre>
<div style="background: #02040a; border: 1px solid rgba(255,255,255,0.06); border-radius: 8px; margin-bottom: 16px; overflow: hidden;">
<div style="background: rgba(255,255,255,0.03); padding: 6px 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.65rem; color: #64748b; font-weight: 800; letter-spacing: 0.06em; font-family: monospace;">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startPostSim('cmseek')" style="background: rgba(16,185,129,0.12); border: 1px solid rgba(16,185,129,0.35); border-radius: 4px; color: #34d399; font-size: 0.7rem; padding: 4px 10px; cursor: pointer; font-family: monospace; font-weight: 700;">▶ Run Simulation</button>
</div>
<div id="term-cmseek" style="font-family: monospace; font-size: 0.76rem; color: #a7f3d0; padding: 12px 16px; white-space: pre-wrap; min-height: 95px;">
<span style="color: #3ddc84;">kali$</span> [กดปุ่ม Run Simulation เพื่อระบุชนิด CMS ด้วย CMSeek]
</div>
</div>
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; padding: 14px; font-size: 0.82rem; color: #cbd5e1; line-height: 1.6;">
<strong style="color: #fbbf24;">💡 สิ่งที่ได้เรียนรู้:</strong> CMSeek มีฐานข้อมูลมากกว่า 160 แพลตฟอร์ม สามารถระบุได้ทันทีว่าเว็บเป้าหมายใช้ CMS อะไรโดยไม่กระตุ้นสัญญาณเตือน WAF
</div>
</div>

</div>
</div>

<script>
window.showSandboxItem = function(itemKey, element) {
  var items = document.querySelectorAll('.w-sandbox-nav .w-nav-item');
  items.forEach(function(i) { i.classList.remove('active'); });
  element.classList.add('active');
  var panels = document.querySelectorAll('.w-sand-panel');
  panels.forEach(function(p) { p.style.setProperty('display', 'none', 'important'); });
  var targetPanel = document.getElementById('panel-' + itemKey);
  if (targetPanel) { targetPanel.style.setProperty('display', 'block', 'important'); }
}
window.startPostSim = function(itemKey) {
  var term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#ffffff; font-weight:bold;">Running audit engine...</span>\\n[.] Connecting to target and analyzing signatures...';
  setTimeout(function() {
    if (itemKey === 'wpscan') {
      term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#3ddc84; font-weight:bold;">WPScan Output:</span>\\nWordPress version: 6.2.2 (Outdated)\\nFOUND User: admin (ID: 1)\\nFOUND Vulnerable Plugin: contact-form-7 v5.7.1 (CVE-2023-XXXX)\\n\\n[+] WPScan Completed!';
    } else if (itemKey === 'joomscan') {
      term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#fb923c; font-weight:bold;">OWASP Joomla! Vulnerability Scanner:</span>\\nJoomla! version: 3.9.22 (Outdated)\\nFOUND: http://target-joomla.local/configuration.php.bak (HTTP 200)\\n\\n[+] JoomScan completed successfully.';
    } else if (itemKey === 'droopescan') {
      term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#818cf8; font-weight:bold;">Droopescan 1.4.0 Engine:</span>\\nTarget: Drupal 7.54\\n[!] Critical Vulnerability Found: Drupalgeddon2 (CVE-2018-7600)\\n[+] Modules identified: 12 active components\\n\\n[+] Droopescan finished.';
    } else if (itemKey === 'cmseek') {
      term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#00f0ff; font-weight:bold;">CMSeek Detection:</span>\\nCMS Detected: WordPress (Certainty: 100%)\\nServer Header: Apache/2.4.52 (Ubuntu)\\nAdmin Login: http://target.local/wp-login.php\\n\\n[+] CMSeek finished reconnaissance.';
    }
  }, 1000);
}
setTimeout(function() {
  var activeBtn = document.querySelector('.w-sandbox-nav .w-nav-item.active');
  if (activeBtn) { activeBtn.click(); }
}, 100);
</script>"""

# =========================================================================
# 4. SUMMARY CARD 1: CMS HARDENING DEBRIEF (BLOCK 2)
# =========================================================================
cms_summary_html = """<!-- ========================================== -->
<!-- UNIFIED MASTERCLASS DEBRIEF: CMS SECURITY & HARDENING -->
<!-- ========================================== -->
<div style="margin: 2.5rem auto 3rem; max-width: 1050px; background: linear-gradient(135deg, rgba(8, 14, 30, 0.98) 0%, rgba(10, 30, 25, 0.98) 100%); border: 1px solid rgba(16, 185, 129, 0.35); border-left: 4px solid #10b981; border-radius: 16px; padding: 24px 28px; box-shadow: 0 16px 45px rgba(0, 0, 0, 0.7), 0 0 30px rgba(16, 185, 129, 0.15);">

<!-- Header -->
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 14px; margin-bottom: 20px; padding-bottom: 14px; border-bottom: 1px solid rgba(255, 255, 255, 0.08);">
<div style="display: flex; align-items: center; gap: 14px;">
<div style="width: 48px; height: 48px; border-radius: 12px; background: rgba(16, 185, 129, 0.15); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.4); display: flex; align-items: center; justify-content: center; font-size: 1.4rem; box-shadow: 0 0 20px rgba(16, 185, 129, 0.3); flex-shrink: 0;">
<i class="fas fa-cubes"></i>
</div>
<div>
<h4 style="margin: 0; color: #ffffff; font-size: 1.2rem; font-weight: 800; letter-spacing: -0.01em;">
🛡️ สรุปบทเรียน: กลไกและแนวทางป้องกันระบบ CMS (CMS Hardening &amp; Defense)
</h4>
<span style="color: #94a3b8; font-size: 0.82rem;">ถอดรหัสความเสี่ยงจากปลั๊กอินและสแกนเนอร์ สู่มาตรการตั้งรับระดับโปรดักชัน</span>
</div>
</div>
<div style="display: flex; gap: 8px; flex-wrap: wrap;">
<span style="background: rgba(16, 185, 129, 0.15); color: #6ee7b7; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(16, 185, 129, 0.35);">
OWASP A06: VULNERABLE COMPONENTS
</span>
<span style="background: rgba(56, 189, 248, 0.15); color: #7dd3fc; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(56, 189, 248, 0.35);">
CWE-1104: THIRD-PARTY CODE
</span>
</div>
</div>

<!-- 3 Columns Takeaways -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 14px; margin-bottom: 20px;">

<!-- Column 1 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #34d399; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-radar"></i> 1. แก่นการโจมตี (Reconnaissance &amp; Exploits)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>CMS Fingerprinting:</strong> สแกนหาเวอร์ชัน CMS และรายชื่อปลั๊กอินที่ติดตั้งผ่าน API และ Signature</li>
<li><strong>Outdated Addons:</strong> โจมตีปลั๊กอินที่ไม่อัปเดต ซึ่งมักมีช่องโหว่ Arbitrary File Upload นำไปสู่ Web Shell</li>
<li><strong>Admin Brute Force:</strong> สุ่มยิงรหัสผ่านหน้า <code>/wp-login.php</code> หรือ <code>/administrator</code> ด้วยบัญชี default เช่น admin</li>
</ul>
</div>

<!-- Column 2 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(251, 191, 36, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #fbbf24; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-radiation"></i> 2. ผลกระทบจริงต่อองค์กร (Business Impact)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>Web Defacement:</strong> หน้าเว็บถูกเปลี่ยนข้อความ สร้างความเสียหายต่อภาพลักษณ์องค์กร</li>
<li><strong>SEO Spam &amp; Malware Drop:</strong> เว็บถูกฝังลิงก์การพนัน หรือเป็นฐานกระจายมัลแวร์สู่ผู้เข้าชม</li>
<li><strong>Database Exfiltration:</strong> รหัสผ่านแฮช ข้อมูลลูกค้า และอีเมลถูกดัมป์ออกไปขายใน Dark Web</li>
</ul>
</div>

<!-- Column 3 -->
<div style="background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 12px; padding: 16px; display: flex; flex-direction: column;">
<div style="color: #38bdf8; font-weight: 800; font-size: 0.9rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-shield-halved"></i> 3. กฎเหล็กการป้องกัน (Golden Hardening Rules)
</div>
<ul style="margin: 0; padding-left: 18px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<li><strong>Auto-Updates 100%:</strong> เปิดระบบอัปเดตอัตโนมัติสำหรับ Security Patches และลบปลั๊กอินที่ไม่ได้ใช้ออก</li>
<li><strong>เปลี่ยน URL Admin &amp; 2FA:</strong> เปลี่ยนจาก <code>/wp-admin</code> เป็น URL ลับ พร้อมบังคับใช้ Two-Factor Auth</li>
<li><strong>ปิดการแก้ไขไฟล์ในแดชบอร์ด:</strong> ตั้งค่า <code>DISALLOW_FILE_EDIT</code> ใน <code>wp-config.php</code> ป้องกันการแก้ไขโค้ด</li>
<li><strong>บล็อกการรัน PHP ในโฟลเดอร์ Uploads:</strong> ห้ามไม่ให้ Web Server ประมวลผลไฟล์ .php ในโฟลเดอร์รูปภาพ</li>
</ul>
</div>

</div>

<!-- Secure Code Comparison Box -->
<div style="background: #040711; border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 18px; margin-bottom: 16px;">
<div style="color: #94a3b8; font-size: 0.78rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-code-compare"></i> ตัวอย่างการตั้งค่าความปลอดภัย WordPress (wp-config.php &amp; Nginx Hardening)
</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(310px, 1fr)); gap: 14px;">
<div style="background: rgba(239, 68, 68, 0.08); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 8px; padding: 12px;">
<div style="color: #fca5a5; font-size: 0.78rem; font-weight: 800; margin-bottom: 6px;">❌ VULNERABLE: การตั้งค่าเริ่มต้นที่ไม่ได้ล็อกความปลอดภัย</div>
<pre style="margin: 0; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #fca5a5; line-height: 1.5;"><code>// ปล่อยให้แก้ไขธีม/ปลั๊กอินผ่านแดชบอร์ดได้ (เสี่ยงโดนใส่ Web Shell)
// ไม่มีคำสั่งล็อกโฟลเดอร์ uploads ทำให้รัน PHP แปลกปลอมได้ทันที
define('DISALLOW_FILE_EDIT', false);</code></pre>
</div>
<div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 12px;">
<div style="color: #86efac; font-size: 0.78rem; font-weight: 800; margin-bottom: 6px;">✅ SECURE: ล็อกไฟล์ระบบ + บล็อกการรันโค้ดใน Uploads</div>
<pre style="margin: 0; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #86efac; line-height: 1.5;"><code>// wp-config.php: ปิด Theme/Plugin Editor หลังบ้านถาวร
define('DISALLOW_FILE_EDIT', true);
define('DISALLOW_FILE_MODS', true);
// Nginx: บล็อกการรัน PHP ใน /wp-content/uploads/
location ~* /wp-content/uploads/.*\\.php$ { deny all; }</code></pre>
</div>
</div>
</div>

<div style="text-align: right; font-size: 0.76rem; color: #64748b;">
บทสรุปสำหรับระบบจัดการเนื้อหาเว็บ (CMS Security) &bull; CRRU Cybersecurity Curriculum 2026
</div>

</div>"""

print("Writing create_lesson_179.py part 2...")
