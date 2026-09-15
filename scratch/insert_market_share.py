import re

market_share_html = """<!-- ========================================================================= -->
<!-- CMS DEFINITION & MARKET SHARE METRICS                                     -->
<!-- ========================================================================= -->
<div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(16, 185, 129, 0.35); border-radius: 14px; padding: 20px; margin-bottom: 22px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 10px; margin-bottom: 14px; padding-bottom: 10px; border-bottom: 1px solid rgba(255,255,255,0.08);">
<div style="display: flex; align-items: center; gap: 10px;">
<span style="font-size: 1.4rem;">📊</span>
<div>
<h4 style="margin: 0; color: #34d399; font-size: 1.05rem; font-weight: 800;">
ภาพรวมและส่วนแบ่งการตลาดของระบบ CMS (CMS Market Share &amp; Attack Surface)
</h4>
<span style="color: #94a3b8; font-size: 0.78rem;">ทำไมแฮกเกอร์ถึงเล็งเป้าหมายระบบเว็บสำเร็จรูปเป็นอันดับหนึ่ง?</span>
</div>
</div>
<span style="background: rgba(16, 185, 129, 0.15); color: #6ee7b7; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 6px; border: 1px solid rgba(16, 185, 129, 0.3);">
GLOBAL MARKET METRICS
</span>
</div>

<p style="margin: 0 0 14px; color: #cbd5e1; font-size: 0.82rem; line-height: 1.65;">
<strong>Content Management System (CMS):</strong> ระบบจัดการสารสนเทศและเนื้อหาเว็บสำเร็จรูปยอดฮิต เช่น <strong>WordPress, Joomla, Drupal และ Magento</strong> ซึ่งมักตกเป็นเป้าหมายหลักของการเจาะระบบเพื่อดึงข้อมูลลับ ขโมยสิทธิ์ผู้ดูแล (Privilege Escalation) หรือลอบฝังคำสั่งประหารยึดเซิร์ฟเวอร์ (Remote Code Execution - RCE)
</p>

<!-- Market Share Progress Bars Grid -->
<div style="background: #030712; border: 1px solid rgba(255,255,255,0.06); border-radius: 10px; padding: 16px; margin-bottom: 14px;">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
<span style="color: #fde047; font-size: 0.82rem; font-weight: 800; display: flex; align-items: center; gap: 6px;">
<i class="fas fa-chart-pie"></i> อัตราครองส่วนแบ่งตลาดของระบบ CMS (สถิติล่าสุดทั่วโลก):
</span>
<span style="font-size: 0.7rem; color: #64748b; font-family: monospace;">W3Techs Market Share Benchmark</span>
</div>

<!-- WordPress Bar (62.7%) -->
<div style="margin-bottom: 12px;">
<div style="display: flex; justify-content: space-between; font-size: 0.78rem; margin-bottom: 5px;">
<span style="color: #38bdf8; font-weight: 700;">
<i class="fab fa-wordpress mr-1"></i> WordPress (เป้าโจมตีอันดับหนึ่งของโลก 🔥)
</span>
<span style="color: #38bdf8; font-family: monospace; font-weight: 800;">62.7%</span>
</div>
<div style="height: 10px; background: rgba(255,255,255,0.06); border-radius: 6px; overflow: hidden;">
<div style="width: 62.7%; height: 100%; background: linear-gradient(90deg, #0284c7, #38bdf8); border-radius: 6px; box-shadow: 0 0 10px rgba(56,189,248,0.5);"></div>
</div>
</div>

<!-- 5 Other CMS Grid -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 10px; margin-top: 14px;">

<!-- Shopify -->
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 6px; padding: 8px 10px;">
<div style="display: flex; justify-content: space-between; font-size: 0.74rem; margin-bottom: 4px;">
<span style="color: #94a3b8; font-weight: 600;"><i class="fab fa-shopify mr-1 text-success"></i> Shopify</span>
<span style="color: #6ee7b7; font-family: monospace; font-weight: 700;">6.4%</span>
</div>
<div style="height: 5px; background: rgba(255,255,255,0.06); border-radius: 4px; overflow: hidden;">
<div style="width: 6.4%; min-width: 14px; height: 100%; background: #10b981; border-radius: 4px;"></div>
</div>
</div>

<!-- Wix -->
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 6px; padding: 8px 10px;">
<div style="display: flex; justify-content: space-between; font-size: 0.74rem; margin-bottom: 4px;">
<span style="color: #94a3b8; font-weight: 600;"><i class="fab fa-wix mr-1 text-warning"></i> Wix</span>
<span style="color: #fde047; font-family: monospace; font-weight: 700;">3.9%</span>
</div>
<div style="height: 5px; background: rgba(255,255,255,0.06); border-radius: 4px; overflow: hidden;">
<div style="width: 3.9%; min-width: 10px; height: 100%; background: #f59e0b; border-radius: 4px;"></div>
</div>
</div>

<!-- Squarespace -->
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 6px; padding: 8px 10px;">
<div style="display: flex; justify-content: space-between; font-size: 0.74rem; margin-bottom: 4px;">
<span style="color: #94a3b8; font-weight: 600;"><i class="fas fa-shapes mr-1 text-info"></i> Squarespace</span>
<span style="color: #93c5fd; font-family: monospace; font-weight: 700;">3.0%</span>
</div>
<div style="height: 5px; background: rgba(255,255,255,0.06); border-radius: 4px; overflow: hidden;">
<div style="width: 3.0%; min-width: 8px; height: 100%; background: #60a5fa; border-radius: 4px;"></div>
</div>
</div>

<!-- Joomla -->
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 6px; padding: 8px 10px;">
<div style="display: flex; justify-content: space-between; font-size: 0.74rem; margin-bottom: 4px;">
<span style="color: #94a3b8; font-weight: 600;"><i class="fab fa-joomla mr-1 text-danger"></i> Joomla</span>
<span style="color: #fca5a5; font-family: monospace; font-weight: 700;">2.4%</span>
</div>
<div style="height: 5px; background: rgba(255,255,255,0.06); border-radius: 4px; overflow: hidden;">
<div style="width: 2.4%; min-width: 6px; height: 100%; background: #ef4444; border-radius: 4px;"></div>
</div>
</div>

<!-- Drupal -->
<div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 6px; padding: 8px 10px;">
<div style="display: flex; justify-content: space-between; font-size: 0.74rem; margin-bottom: 4px;">
<span style="color: #94a3b8; font-weight: 600;"><i class="fab fa-drupal mr-1 text-primary"></i> Drupal</span>
<span style="color: #c4b5fd; font-family: monospace; font-weight: 700;">1.3%</span>
</div>
<div style="height: 5px; background: rgba(255,255,255,0.06); border-radius: 4px; overflow: hidden;">
<div style="width: 1.3%; min-width: 4px; height: 100%; background: #8b5cf6; border-radius: 4px;"></div>
</div>
</div>

</div>
</div>

<!-- Security Insight -->
<div style="background: rgba(245, 158, 11, 0.08); border-left: 3px solid #f59e0b; border-radius: 6px; padding: 10px 14px; font-size: 0.76rem; color: #fde047; line-height: 1.55;">
<strong>⚡ ความสำคัญเชิงความมั่นคงปลอดภัย (Security Insight):</strong><br/>
เหตุผลที่บอทและแฮกเกอร์ทั่วโลกพุ่งเป้าไปที่ <strong>WordPress (62.7%)</strong> มากที่สุด เป็นเพราะ <em>"ความคุ้มค่าของการลงทุน (ROI)"</em> — เมื่อแฮกเกอร์ค้นพบช่องโหว่ของปลั๊กอิน WordPress แม้เพียงตัวเดียว พวกเขาสามารถใช้สคริปต์สแกนอัตโนมัติยิงโจมตีเว็บไซต์ได้นับล้านเว็บไซต์ทั่วโลกในคราวเดียวกัน!
</div>
</div>"""

target_file = "/home/kali/crru_ctf/CTFd/create_lesson_179.py"
with open(target_file, "r", encoding="utf-8") as f:
    content = f.read()

# Locate insertion point: before <!-- Intuitive Metaphor for Students -->
marker = "<!-- Intuitive Metaphor for Students -->"
idx = content.find(marker)
if idx == -1:
    print("[!] Marker not found!")
    exit(1)

new_content = content[:idx] + market_share_html + "\n\n" + content[idx:]
with open(target_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print("[+] Successfully inserted Market Share metrics into front of Section 1 in create_lesson_179.py!")
