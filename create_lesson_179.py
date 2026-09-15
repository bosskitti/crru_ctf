import json
import os
import sys

def clean_html(raw_html: str) -> str:
    """Ensure no blank lines exist inside HTML block so markdown parser doesn't inject <p> tags."""
    return '\n'.join([line.strip() for line in raw_html.split('\n') if line.strip()])

# =========================================================================
# 1. HERO BANNER & INTRODUCTION
# =========================================================================
hero_banner_html = """<!-- ========================================== -->
<!-- HERO BANNER: CHAPTER 5 PART 3 -->
<!-- ========================================== -->
<div style="margin-bottom: 2rem; padding: 26px 30px; background: linear-gradient(135deg, rgba(8, 14, 30, 0.95) 0%, rgba(10, 30, 25, 0.95) 100%); border: 1px solid rgba(16, 185, 129, 0.35); border-left: 5px solid #10b981; border-radius: 16px; box-shadow: 0 16px 45px rgba(0, 0, 0, 0.6), 0 0 30px rgba(16, 185, 129, 0.15);">
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px;">
<div style="display: flex; align-items: center; gap: 16px;">
<div style="width: 54px; height: 54px; border-radius: 14px; background: rgba(16, 185, 129, 0.15); color: #10b981; border: 1px solid rgba(16, 185, 129, 0.4); display: flex; align-items: center; justify-content: center; font-size: 1.6rem; box-shadow: 0 0 25px rgba(16, 185, 129, 0.35); flex-shrink: 0;">
<i class="fas fa-layer-group"></i>
</div>
<div>
<div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
<span style="background: rgba(16, 185, 129, 0.15); color: #6ee7b7; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 3px 10px; border-radius: 20px; border: 1px solid rgba(16, 185, 129, 0.35);">CHAPTER 05 &bull; PART 03</span>
<span style="background: rgba(0, 240, 255, 0.15); color: #7dd3fc; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 3px 10px; border-radius: 20px; border: 1px solid rgba(0, 240, 255, 0.35);">CLIENT-SIDE &amp; CMS SECURITY</span>
</div>
<h2 style="margin: 0; color: #ffffff; font-size: 1.5rem; font-weight: 800; letter-spacing: -0.01em;">
03. การโจมตีระบบ CMS, กลโกง CSRF และ Clickjacking
</h2>
<span style="color: #94a3b8; font-size: 0.84rem;">ถอดรหัสกลไกการโจมตีเว็บสำเร็จรูป ช่องโหว่แอบอ้างสิทธิ์ (CSRF) และกลลวงแผ่นใสครอบคลิก (Clickjacking) สู่แนวทางตั้งรับ</span>
</div>
</div>
<div style="display: flex; gap: 8px; flex-wrap: wrap;">
<span style="background: rgba(245, 158, 11, 0.15); color: #fde047; font-family: monospace; font-size: 0.75rem; font-weight: 700; padding: 4px 12px; border-radius: 8px; border: 1px solid rgba(245, 158, 11, 0.3);">
<i class="fas fa-flask mr-1"></i> 2 ปฏิบัติการจริง (Labs)
</span>
<span style="background: rgba(56, 189, 248, 0.15); color: #7dd3fc; font-family: monospace; font-size: 0.75rem; font-weight: 700; padding: 4px 12px; border-radius: 8px; border: 1px solid rgba(56, 189, 248, 0.3);">
<i class="fas fa-puzzle-piece mr-1"></i> 4 ข้อสอบประเมิน
</span>
</div>
</div>
</div>"""

# =========================================================================
# 2. CMS EXPLOITATION MASTERCLASS + ANIMATED SVG 1
# =========================================================================
cms_masterclass_html = """<!-- ========================================== -->
<!-- SECTION 1: CMS EXPLOITATION & SCANNING TOOLS MASTERCLASS -->
<!-- ========================================== -->
<div style="margin: 2.5rem auto 1.5rem; max-width: 1050px; background: linear-gradient(135deg, rgba(8, 14, 30, 0.98) 0%, rgba(10, 30, 25, 0.98) 100%); border: 1px solid rgba(16, 185, 129, 0.3); border-left: 4px solid #10b981; border-radius: 16px; padding: 24px 28px; box-shadow: 0 16px 45px rgba(0, 0, 0, 0.6), 0 0 25px rgba(16, 185, 129, 0.1);">

<!-- Header -->
<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 12px; margin-bottom: 20px; padding-bottom: 14px; border-bottom: 1px solid rgba(255, 255, 255, 0.08);">
<div style="display: flex; align-items: center; gap: 12px;">
<span style="font-size: 1.5rem;">🧩</span>
<div>
<h3 style="margin: 0; color: #ffffff; font-size: 1.25rem; font-weight: 800;">
1. ระบบจัดการเนื้อหาเว็บ (CMS) และเครื่องมือสแกนความปลอดภัย (Scanning Tools)
</h3>
<span style="color: #94a3b8; font-size: 0.82rem;">เจาะลึกสถาปัตยกรรม WordPress, Joomla, Drupal และจุดตายสำคัญจากห่วงโซ่อุปทาน (Supply Chain Plugins)</span>
</div>
</div>
<div style="display: flex; gap: 8px; flex-wrap: wrap;">
<span style="background: rgba(16, 185, 129, 0.15); color: #6ee7b7; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(16, 185, 129, 0.35);">
OWASP A06: VULNERABLE COMPONENTS
</span>
<span style="background: rgba(0, 240, 255, 0.15); color: #7dd3fc; font-family: monospace; font-size: 0.72rem; font-weight: 800; padding: 4px 12px; border-radius: 20px; border: 1px solid rgba(0, 240, 255, 0.35);">
CWE-1104: THIRD-PARTY COMPONENTS
</span>
</div>
</div>

<!-- ========================================================================= -->
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
</div>

<!-- Intuitive Metaphor for Students -->
<div style="background: rgba(16, 185, 129, 0.06); border: 1px dashed rgba(16, 185, 129, 0.3); border-radius: 12px; padding: 18px 20px; margin-bottom: 22px;">
<div style="color: #34d399; font-weight: 800; font-size: 0.92rem; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-lightbulb"></i> อุปมาอุปไมยให้เข้าใจง่าย: CMS เปรียบเสมือน "บ้านสำเร็จรูป" และ "ของแต่งบ้าน"
</div>
<p style="margin: 0 0 10px; color: #cbd5e1; font-size: 0.84rem; line-height: 1.65;">
ลองจินตนาการว่าการสร้างเว็บไซต์ขึ้นมาเองตั้งแต่ศูนย์ เปรียบเหมือนการสร้างบ้านด้วยการก่ออิฐทีละก้อน ต้องผสมปูนเอง ต่อท่อน้ำเอง ซึ่งใช้เวลานานมาก แต่ <strong>CMS (Content Management System)</strong> อย่าง <strong>WordPress, Joomla หรือ Drupal</strong> เปรียบเหมือน <strong>"บ้านสำเร็จรูป"</strong> ที่โครงสร้างหลักสร้างเสร็จสมบูรณ์ มีประตู หน้าต่าง และห้องต่างๆ พร้อมเข้าอยู่ได้ทันทีในเวลาไม่กี่นาที
</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 12px; margin-top: 12px;">
<div style="background: rgba(0,0,0,0.3); border-radius: 8px; padding: 12px; border-left: 3px solid #3b82f6;">
<strong style="color: #60a5fa; font-size: 0.8rem; display: block; margin-bottom: 4px;">🏠 โครงสร้างหลัก (CMS Core):</strong>
<span style="color: #94a3b8; font-size: 0.78rem; line-height: 1.5;">ทีมงานผู้พัฒนาระดับโลกดูแลความปลอดภัยอย่างแน่นหนา มีอัปเดตสม่ำเสมอ โอกาสโดนเจาะตรงๆ มีน้อยมาก</span>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 8px; padding: 12px; border-left: 3px solid #f43f5e;">
<strong style="color: #fca5a5; font-size: 0.8rem; display: block; margin-bottom: 4px;">🚪 จุดตาย: ของแต่งบ้านและกลอนเสริม (Plugins &amp; Themes):</strong>
<span style="color: #94a3b8; font-size: 0.78rem; line-height: 1.5;">ผู้ใช้มักดาวน์โหลดปลั๊กอินนับสิบตัวจากนักพัฒนาภายนอก หากปลั๊กอินตัวใดตัวหนึ่งเขียนโค้ดหละหลวม หรือเจ้าของเลิกอัปเดต โจรก็จะใช้กลอนพังๆ นี้ปีนเข้าบ้านได้ทันที!</span>
</div>
</div>
</div>

<!-- Animated Vector Graphic 1: CMS Security & Supply Chain Flow -->
<div style="background: #040711; border: 1px solid rgba(16, 185, 129, 0.25); border-radius: 14px; padding: 16px; margin-bottom: 22px; box-shadow: inset 0 0 30px rgba(0,0,0,0.8);">
<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; padding: 0 4px;">
<span style="color: #10b981; font-size: 0.78rem; font-weight: 800; font-family: monospace; letter-spacing: 0.08em; text-transform: uppercase;">
<i class="fas fa-project-diagram mr-2"></i> แผนภาพเคลื่อนไหว: กลไกการตรวจจับและโจมตีช่องโหว่บน CMS (Recon to Shell Upload)
</span>
<span style="font-size: 0.7rem; color: #64748b; font-family: monospace;">LIVE SVG INTERACTIVE</span>
</div>

<svg viewBox="0 0 900 370" width="100%" height="100%" style="display: block; border-radius: 10px; background: #070a14;" xmlns="http://www.w3.org/2000/svg">
<defs>
<linearGradient id="cms-bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
<stop offset="0%" stop-color="#070b18" />
<stop offset="100%" stop-color="#0a1520" />
</linearGradient>
<linearGradient id="attacker-grad" x1="0%" y1="0%" x2="100%" y2="0%">
<stop offset="0%" stop-color="#ef4444" />
<stop offset="100%" stop-color="#f97316" />
</linearGradient>
<linearGradient id="cms-core-grad" x1="0%" y1="0%" x2="100%" y2="0%">
<stop offset="0%" stop-color="#3b82f6" />
<stop offset="100%" stop-color="#00f0ff" />
</linearGradient>
<linearGradient id="plugin-grad" x1="0%" y1="0%" x2="100%" y2="0%">
<stop offset="0%" stop-color="#f43f5e" />
<stop offset="100%" stop-color="#fb7185" />
</linearGradient>
<linearGradient id="server-grad" x1="0%" y1="0%" x2="100%" y2="0%">
<stop offset="0%" stop-color="#10b981" />
<stop offset="100%" stop-color="#059669" />
</linearGradient>
<filter id="cms-glow" x="-20%" y="-20%" width="140%" height="140%">
<feGaussianBlur stdDeviation="5" result="blur" />
<feComposite in="SourceGraphic" in2="blur" operator="over" />
</filter>
<style>
@keyframes scanBeam {
  0% { stroke-dashoffset: 240; opacity: 0.3; }
  50% { opacity: 1; }
  100% { stroke-dashoffset: 0; opacity: 0.3; }
}
@keyframes exploitPulse {
  0% { transform: scale(1); opacity: 0.8; }
  50% { transform: scale(1.05); opacity: 1; filter: drop-shadow(0 0 10px #f43f5e); }
  100% { transform: scale(1); opacity: 0.8; }
}
@keyframes dataPacketMove {
  0% { stroke-dashoffset: 300; }
  100% { stroke-dashoffset: 0; }
}
@keyframes radarSweep {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
.scan-line { stroke-dasharray: 8 6; animation: scanBeam 2.5s linear infinite; }
.exploit-card { animation: exploitPulse 3s ease-in-out infinite; transform-origin: center; }
.data-flow { stroke-dasharray: 12 8; animation: dataPacketMove 2s linear infinite; }
</style>
</defs>

<!-- Background & Grid -->
<rect width="900" height="370" rx="12" fill="url(#cms-bg-grad)" stroke="rgba(255,255,255,0.06)" />
<line x1="0" y1="90" x2="900" y2="90" stroke="rgba(255,255,255,0.03)" stroke-dasharray="4 4" />
<line x1="0" y1="180" x2="900" y2="180" stroke="rgba(255,255,255,0.03)" stroke-dasharray="4 4" />
<line x1="0" y1="270" x2="900" y2="270" stroke="rgba(255,255,255,0.03)" stroke-dasharray="4 4" />

<!-- ==================== LEFT: ATTACKER RECON STATION ==================== -->
<rect x="30" y="45" width="220" height="280" rx="12" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(239, 68, 68, 0.4)" stroke-width="1.5" />
<rect x="30" y="45" width="220" height="36" rx="12" fill="rgba(239, 68, 68, 0.15)" />
<circle cx="50" cy="63" r="5" fill="#ef4444" />
<circle cx="65" cy="63" r="5" fill="#f59e0b" />
<circle cx="80" cy="63" r="5" fill="#10b981" />
<text x="140" y="67" fill="#fca5a5" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="bold" text-anchor="middle">KALI RECON DRONE</text>

<!-- Terminal Output Inside Attacker -->
<rect x="42" y="95" width="196" height="150" rx="8" fill="#030712" stroke="rgba(255,255,255,0.06)" />
<text x="52" y="115" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="9.5">$ wpscan --url target.com</text>
<text x="52" y="132" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="9">[+] CMS: WordPress 6.2</text>
<text x="52" y="149" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9">[+] User found: admin (id:1)</text>
<text x="52" y="166" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold">[!] Vuln Plugin: evil-form</text>
<text x="52" y="183" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="9">[!] CVE-2023-XXXX (RCE)</text>
<text x="52" y="202" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="9">[&gt;] Uploading shell.php...</text>
<text x="52" y="222" fill="#4ade80" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="bold">[+] SHELL ACTIVE: 200 OK</text>

<rect x="42" y="258" width="196" height="52" rx="6" fill="rgba(239, 68, 68, 0.08)" stroke="rgba(239, 68, 68, 0.25)" />
<text x="140" y="278" fill="#fca5a5" font-family="sans-serif" font-size="10.5" font-weight="bold" text-anchor="middle">Automated Scanning Engines</text>
<text x="140" y="296" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">WPScan &bull; CMSeek &bull; Droopescan</text>

<!-- Connecting Scanning Beam from Attacker to Server -->
<path d="M 250 150 L 320 120" fill="none" stroke="#38bdf8" stroke-width="2.5" class="scan-line" />
<path d="M 250 190 L 320 220" fill="none" stroke="#f43f5e" stroke-width="2.5" class="scan-line" />

<!-- ==================== MIDDLE: CMS WEB ARCHITECTURE ==================== -->
<rect x="320" y="35" width="280" height="300" rx="14" fill="rgba(15, 23, 42, 0.9)" stroke="rgba(56, 189, 248, 0.4)" stroke-width="1.5" />
<rect x="320" y="35" width="280" height="36" rx="14" fill="rgba(56, 189, 248, 0.12)" />
<text x="460" y="58" fill="#7dd3fc" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">TARGET CMS SERVER (WordPress)</text>

<!-- Core Box (Upper Middle) -->
<rect x="338" y="85" width="244" height="65" rx="8" fill="rgba(30, 41, 59, 0.6)" stroke="rgba(56, 189, 248, 0.3)" />
<circle cx="356" cy="117" r="10" fill="rgba(56, 189, 248, 0.15)" stroke="#38bdf8" stroke-width="1.5" />
<text x="356" y="121" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">W</text>
<text x="375" y="112" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">WordPress Core 6.2</text>
<text x="375" y="128" fill="#94a3b8" font-family="sans-serif" font-size="9.5">Hardened Core APIs (SQLi/XSS Filtered)</text>
<rect x="525" y="102" width="48" height="18" rx="4" fill="rgba(16,185,129,0.15)" stroke="rgba(16,185,129,0.4)" />
<text x="549" y="115" fill="#4ade80" font-family="sans-serif" font-size="8.5" font-weight="bold" text-anchor="middle">SECURE</text>

<!-- Outdated Plugin Box (Lower Middle - High Risk) -->
<g class="exploit-card">
<rect x="338" y="165" width="244" height="85" rx="8" fill="rgba(244, 63, 94, 0.08)" stroke="#f43f5e" stroke-width="1.5" />
<circle cx="356" cy="195" r="10" fill="rgba(244, 63, 94, 0.2)" stroke="#f43f5e" stroke-width="1.5" />
<text x="356" y="199" fill="#f43f5e" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">!</text>
<text x="375" y="190" fill="#fca5a5" font-family="sans-serif" font-size="11" font-weight="bold">Outdated Form Plugin v1.2</text>
<text x="375" y="206" fill="#f87171" font-family="'JetBrains Mono', monospace" font-size="9">Arbitrary File Upload Bug (CVE)</text>
<text x="375" y="222" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="8.5">Path: /wp-content/plugins/form/</text>
<rect x="515" y="177" width="58" height="18" rx="4" fill="rgba(244,63,94,0.2)" stroke="#f43f5e" />
<text x="544" y="190" fill="#fca5a5" font-family="sans-serif" font-size="8.5" font-weight="bold" text-anchor="middle">CRITICAL</text>
</g>

<!-- Web Uploads Directory Target -->
<rect x="338" y="262" width="244" height="60" rx="8" fill="#030712" stroke="rgba(255,255,255,0.1)" />
<text x="352" y="282" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="9.5">📂 /wp-content/uploads/</text>
<text x="368" y="302" fill="#4ade80" font-family="'JetBrains Mono', monospace" font-size="9">└── ⚠️ shell.php (Web Shell Injected)</text>

<!-- Flow line from Plugin to Server Host -->
<path d="M 582 205 L 670 170" fill="none" stroke="#f43f5e" stroke-width="2.5" class="data-flow" />
<path d="M 582 290 L 670 270" fill="none" stroke="#38bdf8" stroke-width="2" class="data-flow" />

<!-- ==================== RIGHT: DATABASE & HOST SYSTEM ==================== -->
<rect x="670" y="45" width="200" height="280" rx="12" fill="rgba(15, 23, 42, 0.85)" stroke="rgba(16, 185, 129, 0.4)" stroke-width="1.5" />
<rect x="670" y="45" width="200" height="36" rx="12" fill="rgba(16, 185, 129, 0.15)" />
<text x="770" y="67" fill="#6ee7b7" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">BACKEND HOST &amp; DB</text>

<!-- Database Box -->
<rect x="682" y="95" width="176" height="95" rx="8" fill="#030712" stroke="rgba(16, 185, 129, 0.25)" />
<text x="694" y="118" fill="#34d399" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold">🗄️ MySQL Database</text>
<text x="694" y="136" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="8.5">Table: wp_users</text>
<text x="694" y="152" fill="#fca5a5" font-family="'JetBrains Mono', monospace" font-size="8.5">admin: $P$B9z... (Hash)</text>
<text x="694" y="168" fill="#94a3b8" font-family="'JetBrains Mono', monospace" font-size="8.5">Table: wp_options (Secret)</text>

<!-- OS Host Box -->
<rect x="682" y="205" width="176" height="105" rx="8" fill="#030712" stroke="rgba(239, 68, 68, 0.3)" />
<text x="694" y="228" fill="#f87171" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="bold">🖥️ Linux OS Shell</text>
<text x="694" y="246" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="8.5">www-data execution:</text>
<text x="694" y="264" fill="#fbbf24" font-family="'JetBrains Mono', monospace" font-size="8.5">&gt; id: uid=33(www-data)</text>
<text x="694" y="282" fill="#4ade80" font-family="'JetBrains Mono', monospace" font-size="8.5">&gt; cat /var/www/flag.txt</text>
<text x="694" y="298" fill="#f43f5e" font-family="'JetBrains Mono', monospace" font-size="8.5">Privilege Escalation 🔥</text>
</svg>
</div>

<!-- Key Takeaways & Tools Summary -->
<div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 18px; margin-bottom: 20px;">
<div style="font-size: 0.85rem; font-weight: 700; color: #10b981; margin-bottom: 12px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-search-dollar"></i> 3 ขั้นตอนที่บอทสแกนอัตโนมัติ (Automated Scanners) ใช้เจาะระบบ CMS
</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 12px;">
<div style="background: rgba(0,0,0,0.25); border-radius: 8px; padding: 12px; border-top: 2px solid #38bdf8;">
<strong style="color: #7dd3fc; font-size: 0.82rem; display: block; margin-bottom: 4px;">1. CMS Fingerprinting &amp; Reconnaissance:</strong>
<span style="color: #94a3b8; font-size: 0.78rem; line-height: 1.5;">อ่านค่า HTTP Header, ไฟล์ <code>readme.html</code>, หรือ meta tag <code>&lt;meta name="generator" content="WordPress"&gt;</code> เพื่อระบุชนิดและเวอร์ชัน</span>
</div>
<div style="background: rgba(0,0,0,0.25); border-radius: 8px; padding: 12px; border-top: 2px solid #f59e0b;">
<strong style="color: #fde047; font-size: 0.82rem; display: block; margin-bottom: 4px;">2. Plugin &amp; User Enumeration:</strong>
<span style="color: #94a3b8; font-size: 0.78rem; line-height: 1.5;">ใช้คำสั่งสแกนหารายชื่อปลั๊กอินนับพันตัว พร้อมดึงบัญชีผู้ใช้ผ่าน REST API <code>/wp-json/wp/v2/users</code> หรือ Author ID</span>
</div>
<div style="background: rgba(0,0,0,0.25); border-radius: 8px; padding: 12px; border-top: 2px solid #ef4444;">
<strong style="color: #fca5a5; font-size: 0.82rem; display: block; margin-bottom: 4px;">3. Automated Exploit &amp; Brute Force:</strong>
<span style="color: #94a3b8; font-size: 0.78rem; line-height: 1.5;">ยิง Exploit สำเร็จรูปเข้าใส่ปลั๊กอินที่มีช่องโหว่ หรือรัน Brute-force รหัสผ่านหน้า <code>/wp-login.php</code> ด้วย Wordlist</span>
</div>
</div>
</div>

<!-- Tools Comparison Table -->
<div style="overflow-x: auto; margin-bottom: 20px; border: 1px solid rgba(16,185,129,0.2); border-radius: 12px; background: #05070f; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
<div style="padding: 12px 18px; background: rgba(16,185,129,0.07); border-bottom: 1px solid rgba(16,185,129,0.15); display: flex; justify-content: space-between; align-items: center;">
<span style="font-size: 0.82rem; font-weight: 700; color: #10b981; text-transform: uppercase; letter-spacing: 0.06em;">
<i class="fas fa-tools mr-2"></i> ตารางเปรียบเทียบเครื่องมือสแกนความปลอดภัย CMS (Tools Comparison)
</span>
<span style="font-size: 0.74rem; color: #64748b;">OWASP &amp; Kali Linux Standards</span>
</div>
<table style="width: 100%; border-collapse: collapse; font-size: 0.8rem;">
<thead>
<tr style="border-bottom: 1px solid rgba(255,255,255,0.06); background: rgba(255,255,255,0.02);">
<th style="padding: 10px 14px; color: #10b981; font-weight: 700; text-align: left;">ชื่อเครื่องมือ (Tool)</th>
<th style="padding: 10px 14px; color: #10b981; font-weight: 700; text-align: left;">เป้าหมายที่รองรับ</th>
<th style="padding: 10px 14px; color: #10b981; font-weight: 700; text-align: left;">ความสามารถหลัก (Capabilities)</th>
<th style="padding: 10px 14px; color: #10b981; font-weight: 700; text-align: left;">ความยากง่าย</th>
<th style="padding: 10px 14px; color: #10b981; font-weight: 700; text-align: left;">จุดเด่นสำคัญ</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(59,130,246,0.04);">
<td style="padding:10px 14px;"><span style="color:#3b82f6; font-weight:700; font-family:monospace;">WPScan</span></td>
<td style="padding:10px 14px; color:#cbd5e1;">WordPress (อันดับ 1 ของโลก)</td>
<td style="padding:10px 14px; color:#94a3b8; font-size:0.77rem;">สแกนเวอร์ชัน, ธีม, ปลั๊กอิน, ผู้ใช้ และรัน Brute Force</td>
<td style="padding:10px 14px;"><span style="background:rgba(61,220,132,0.12); color:#3ddc84; padding:2px 8px; border-radius:10px; font-size:0.72rem; font-weight:700;">ง่ายมาก</span></td>
<td style="padding:10px 14px; color:#94a3b8; font-size:0.77rem;">เชื่อมต่อฐานข้อมูล WPScan Vulnerability Database แบบเรียลไทม์</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td style="padding:10px 14px;"><span style="color:#fb923c; font-weight:700; font-family:monospace;">JoomScan</span></td>
<td style="padding:10px 14px; color:#cbd5e1;">Joomla</td>
<td style="padding:10px 14px; color:#94a3b8; font-size:0.77rem;">สแกนหา Components, ไฟล์แบ็กอัป, และการตั้งค่าผิดพลาด</td>
<td style="padding:10px 14px;"><span style="background:rgba(251,191,36,0.12); color:#fbbf24; padding:2px 8px; border-radius:10px; font-size:0.72rem; font-weight:700;">ปานกลาง</span></td>
<td style="padding:10px 14px; color:#94a3b8; font-size:0.77rem;">พัฒนาโดยทีมงาน OWASP ตรวจสอบไฟล์ตกค้างเช่น configuration.php.bak</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04); background:rgba(99,102,241,0.04);">
<td style="padding:10px 14px;"><span style="color:#6366f1; font-weight:700; font-family:monospace;">Droopescan</span></td>
<td style="padding:10px 14px; color:#cbd5e1;">Drupal, SilverStripe, Moodle</td>
<td style="padding:10px 14px; color:#94a3b8; font-size:0.77rem;">สแกนหา Modules, Themes, Default Files และ Versions</td>
<td style="padding:10px 14px;"><span style="background:rgba(251,191,36,0.12); color:#fbbf24; padding:2px 8px; border-radius:10px; font-size:0.72rem; font-weight:700;">ปานกลาง</span></td>
<td style="padding:10px 14px; color:#94a3b8; font-size:0.77rem;">สแกนหลายเธรด (Multi-threaded) รวดเร็วมาก</td>
</tr>
<tr style="border-bottom:1px solid rgba(255,255,255,0.04);">
<td style="padding:10px 14px;"><span style="color:#10b981; font-weight:700; font-family:monospace;">CMSmap</span></td>
<td style="padding:10px 14px; color:#cbd5e1;">WordPress, Joomla, Drupal</td>
<td style="padding:10px 14px; color:#94a3b8; font-size:0.77rem;">สแกนตรวจจับชนิด CMS อัตโนมัติ พร้อมฟังก์ชัน Dictionary Attack</td>
<td style="padding:10px 14px;"><span style="background:rgba(251,191,36,0.12); color:#fbbf24; padding:2px 8px; border-radius:10px; font-size:0.72rem; font-weight:700;">ปานกลาง</span></td>
<td style="padding:10px 14px; color:#94a3b8; font-size:0.77rem;">เครื่องมือ All-in-One ในภาษา Python สำหรับ Multi-CMS</td>
</tr>
<tr>
<td style="padding:10px 14px;"><span style="color:#00f0ff; font-weight:700; font-family:monospace;">CMSeek</span></td>
<td style="padding:10px 14px; color:#cbd5e1;">160+ CMS แพลตฟอร์ม</td>
<td style="padding:10px 14px; color:#94a3b8; font-size:0.77rem;">ตรวจจับ Fingerprint ชนิดของ CMS และประเมินช่องโหว่เบื้องต้น</td>
<td style="padding:10px 14px;"><span style="background:rgba(61,220,132,0.12); color:#3ddc84; padding:2px 8px; border-radius:10px; font-size:0.72rem; font-weight:700;">ง่ายมาก</span></td>
<td style="padding:10px 14px; color:#94a3b8; font-size:0.77rem;">ฐานข้อมูล Signature กว้างขวางที่สุด ตรวจจับได้แม้กระทั่ง Shopify หรือ Wix</td>
</tr>
</tbody>
</table>
</div>

<!-- WPScan Quick Cheatsheet for Students -->
<div style="background: #05070f; border: 1px solid rgba(59,130,246,0.2); border-left: 4px solid #3b82f6; border-radius: 10px; padding: 16px; margin-bottom: 20px;">
<div style="font-size: 0.85rem; font-weight: 800; color: #60a5fa; margin-bottom: 10px; display: flex; align-items: center; gap: 8px;">
<i class="fas fa-terminal"></i> ชุดคำสั่ง WPScan ยอดนิยมที่ต้องรู้ (Command Quick Reference)
</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 10px;">
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 10px;">
<div style="font-size: 0.72rem; color: #94a3b8; font-weight: 700; margin-bottom: 4px;">1. สแกนหาปลั๊กอินที่มีช่องโหว่ (Vulnerable Plugins)</div>
<pre style="margin: 0; font-family: monospace; font-size: 0.74rem; color: #38bdf8;"><code>wpscan --url http://target.com --enumerate vp</code></pre>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 10px;">
<div style="font-size: 0.72rem; color: #94a3b8; font-weight: 700; margin-bottom: 4px;">2. ดึงรายชื่อผู้ใช้งานทั้งหมด (Enumerate Users)</div>
<pre style="margin: 0; font-family: monospace; font-size: 0.74rem; color: #38bdf8;"><code>wpscan --url http://target.com --enumerate u</code></pre>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 10px;">
<div style="font-size: 0.72rem; color: #94a3b8; font-weight: 700; margin-bottom: 4px;">3. สุ่มโจมตีรหัสผ่านผู้ดูแลระบบ (Brute Force Password)</div>
<pre style="margin: 0; font-family: monospace; font-size: 0.74rem; color: #38bdf8;"><code>wpscan --url http://target.com -U admin -P rockyou.txt</code></pre>
</div>
<div style="background: rgba(0,0,0,0.3); border-radius: 6px; padding: 10px;">
<div style="font-size: 0.72rem; color: #94a3b8; font-weight: 700; margin-bottom: 4px;">4. สแกนครบวงจรพร้อมเชื่อมต่อฐานข้อมูล CVE API</div>
<pre style="margin: 0; font-family: monospace; font-size: 0.74rem; color: #38bdf8;"><code>wpscan --url http://target.com --api-token YOUR_KEY -e vp,vt,u</code></pre>
</div>
</div>
</div>

<!-- ========================================================================= -->
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
<strong style="color: #f87171; font-size: 0.8rem;">🔴 จุดที่ 1: XML-RPC Enabled (จุดตายวิกฤต!)</strong>
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

print("Writing create_lesson_179.py part 1...")
