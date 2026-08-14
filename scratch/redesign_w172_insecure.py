import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l172 = db.session.query(TutorialLesson).filter_by(id=172).first()

# ─── 1. Construct Premium Blocks for Lesson 172 ───
blocks_172 = []

# Block 0: Title & Header
blocks_172.append({
    "type": "markdown",
    "value": "## 🛡️ การเขียนโค้ดที่ไม่มีความปลอดภัยและช่องโหว่ (Insecure Coding & Buffer Overflows)"
})

# Block 1: SSDLC & Secure Design Standards
blocks_172.append({
    "type": "markdown",
    "value": """### ⚙️ Secure SDLC & Standards

การพัฒนาซอฟต์แวร์ที่ปลอดภัย (Secure Application Development) มีบทบาทสำคัญในการจำกัดการเกิดช่องโหว่ในโปรแกรมจากการเขียนโค้ดที่บกพร่อง โดยทีมพัฒนาจะต้องนำเอาแนวคิด **Secure Software Development Life Cycle (SSDLC)** เข้ามารวมไว้ในขั้นตอนวงจรชีวิตการพัฒนาระบบเพื่อสร้างความมั่นคงปลอดภัยตั้งแต่ก้าวแรก:

<style>
.ssdlc-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin:2rem auto;max-width:1050px;}
@media(max-width:768px){.ssdlc-grid{grid-template-columns:1fr;}}
.ssdlc-card{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:20px;box-sizing:border-box;}
.ssdlc-title{font-size:0.92rem;font-weight:800;color:#00f0ff;margin-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.05);padding-bottom:6px;}
.ssdlc-desc{font-size:0.8rem;color:#94a3b8;line-height:1.65;margin:0;}
.ssdlc-desc strong{color:#fbbf24;}
</style>

<div class="ssdlc-grid">
<div class="ssdlc-card">
<div class="ssdlc-title">🛡️ Secure SDLC Goals</div>
<p class="ssdlc-desc">เน้นยัดมาตรการความปลอดภัยเข้าสู่ทุกเฟสของการพัฒนา เพื่อระบุและแก้ไขบั๊กตั้งแต่เนิ่นๆ ช่วยลดต้นทุนความปลอดภัย และจำกัดความเสี่ยงของการโดนแฮกเมื่อโปรแกรมใช้งานจริงใน Production</p>
</div>
<div class="ssdlc-card">
<div class="ssdlc-title">📖 OWASP Coding Practices</div>
<p class="ssdlc-desc">นักพัฒนาสามารถใช้อ้างอิงมาตรฐานระดับโลก เช่น <strong>OWASP Secure Coding Practices Quick Reference Guide</strong> และ <strong>OWASP Developer Guide</strong> เพื่อเป็นแนวทางปฏิบัติในการสแกนสิทธิ์ ตรวจสอบอินพุต และรับมือกับช่องโหว่ประเภทต่าง ๆ</p>
</div>
</div>"""
})

blocks_172.append({"type": "markdown", "value": "---"})

# Block 2: Vulnerability Catalog
blocks_172.append({
    "type": "markdown",
    "value": """### ☣️ Vulnerabilities from Insecure Design & Coding

ช่องโหว่ (Vulnerability) ในระดับโค้ดเกิดจากข้อผิดพลาดในการเขียนโปรแกรมและออกแบบตรรกะ ซึ่งแฮกเกอร์สามารถใช้เทคนิคและสคริปต์เฉพาะตัวดักโจมตีจุดบกพร่องเหล่านี้ได้ โดยช่องโหว่ระบบหลักที่พบบ่อยแบ่งออกเป็น 8 ประเภทหลัก:

<style>
.vuln-list-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:2rem auto;max-width:1050px;}
@media(max-width:900px){.vuln-list-grid{grid-template-columns:repeat(2,1fr);}}
@media(max-width:480px){.vuln-list-grid{grid-template-columns:1fr;}}
.vuln-list-card{background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.04);border-radius:8px;padding:14px;box-sizing:border-box;transition:all 0.15s ease;}
.vuln-list-card:hover{border-color:#ff007f;background:rgba(255,0,127,0.02);}
.vuln-list-title{font-size:0.78rem;font-weight:800;color:#ff007f;margin-bottom:4px;}
.vuln-list-desc{font-size:0.72rem;color:#94a3b8;line-height:1.5;margin:0;}
</style>

<div class="vuln-list-grid">
<div class="vuln-list-card">
<div class="vuln-list-title">1. Integer Overflow</div>
<p class="vuln-list-desc">การคำนวณทางคณิตศาสตร์เกินพิกัดความกว้างที่ตัวแปรเก็บได้ จนเกิดวงรอบกลับค่ากลับด้าน (Wrap-around)</p>
</div>
<div class="vuln-list-card">
<div class="vuln-list-title">2. Floating Point</div>
<p class="vuln-list-desc">ข้อจำกัดของการเก็บตัวเลขทศนิยมเป็นเลขฐานสอง ทำให้ประมวลผลทศนิยมบางคำคลาดเคลื่อน (Rounding error)</p>
</div>
<div class="vuln-list-card">
<div class="vuln-list-title">3. Arithmetic Side Effect</div>
<p class="vuln-list-desc">ผลลัพธ์คลาดเคลื่อนจากการหารด้วยศูนย์ (Division by zero) หรือการใช้ตัวเพิ่ม/ลดค่าที่ไม่แน่นอน</p>
</div>
<div class="vuln-list-card">
<div class="vuln-list-title">4. Autoboxing Leak</div>
<p class="vuln-list-desc">ความล่าช้าจากการแปลงออบเจกต์อัตโนมัติ หรือข้อผิดพลาด Reference จาก Integer Cache</p>
</div>
</div>

<div class="vuln-list-grid" style="margin-top:0;">
<div class="vuln-list-card">
<div class="vuln-list-title">5. String Operation</div>
<p class="vuln-list-desc">ปัญหาหน่วยความจำจากการแก้ข้อความบ่อยครั้ง หรือระบบกรองสตริงบกพร่อง (เช่น กรองอักษรออกไม่หมด)</p>
</div>
<div class="vuln-list-card">
<div class="vuln-list-title">6. Format String</div>
<p class="vuln-list-desc">การอนุญาตให้อินพุตของแฮกเกอร์ป้อนเข้าสู่ฟังก์ชันแสดงผลฟอร์แมตโดยตรง ส่งผลให้ดักสแกนหน่วยความจำได้</p>
</div>
<div class="vuln-list-card">
<div class="vuln-list-title">7. Buffer Overflow</div>
<p class="vuln-list-desc">การป้อนข้อความที่มีขนาดใหญ่เกินกว่าบัฟเฟอร์ เพื่อเขียนทับตัวแปรอื่นหรือกระโดดสั่งรันคำสั่งลับ</p>
</div>
<div class="vuln-list-card">
<div class="vuln-list-title">8. RNG Vulnerability</div>
<p class="vuln-list-desc">ความล้มเหลวของการสุ่มค่าที่ไม่สุ่มจริง (Pseudo-random) จนส่งผลให้เดาเด็ดพิกัดหรือคีย์ถัดไปได้</p>
</div>
</div>"""
})

blocks_172.append({"type": "markdown", "value": "---"})

# Block 3: Interactive Sandbox with 8 categories of vulnerability code
blocks_172.append({
    "type": "markdown",
    "value": """### 💻 Code Security Console (วิเคราะห์เจาะลึก 8 รูปแบบบั๊กและตรรกะระบบ)

คลิกหัวข้อด้านซ้ายมือเพื่อตรวจสอบช่องโหว่ความมั่นคงปลอดภัย (Code) และ **การวิเคราะห์การทำงานอย่างละเอียดในเชิงความปลอดภัยไซเบอร์ (Detailed Security Analysis)**:

<style>
.w-sandbox-main{display:flex;gap:20px;margin:2rem auto;max-width:1050px;}
@media(max-width:820px){.w-sandbox-main{flex-direction:column;}}

.w-sandbox-nav{width:220px;display:flex;flex-direction:column;gap:6px;flex-shrink:0;}
@media(max-width:820px){.w-sandbox-nav{width:100%;flex-direction:row;flex-wrap:wrap;}}
.w-nav-item{padding:8px 12px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.04);border-radius:6px;font-size:0.75rem;color:#cbd5e1;cursor:pointer;text-align:left;transition:all 0.15s ease;}
.w-nav-item:hover, .w-nav-item.active{border-color:#00f0ff;color:#ffffff;background:rgba(0,240,255,0.04);}
.w-nav-item.active{font-weight:bold;box-shadow:0 0 8px rgba(0,240,255,0.1);}

.w-sandbox-panels{flex:1;display:flex;flex-direction:column;gap:14px;}
.w-sand-panel{display:none;background:#05070f;border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:20px;box-shadow:0 8px 24px rgba(0,0,0,0.45);box-sizing:border-box;}
.w-sand-panel.active{display:block;}

.w-sand-hdr{font-size:0.95rem;font-weight:800;color:#ffffff;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:10px;margin-bottom:14px;display:flex;justify-content:between;align-items:center;}
.w-sand-hdr span.tag{font-size:0.65rem;padding:2px 8px;border-radius:4px;background:rgba(0,240,255,0.08);border:1px solid rgba(0,240,255,0.2);color:#00f0ff;font-family:'JetBrains Mono',monospace;}
.w-sand-code{font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#00f0ff;white-space:pre-wrap;margin:0 0 16px;background:rgba(0,0,0,0.2);padding:14px;border-radius:8px;border:1px solid rgba(255,255,255,0.02);}

.w-sand-expl{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:16px;font-size:0.83rem;color:#cbd5e1;line-height:1.65;}
.w-sand-expl h5{margin:0 0 8px;font-size:0.85rem;color:#fbbf24;font-weight:bold;}
.w-sand-expl p{margin:0 0 10px;}
.w-sand-expl p:last-child{margin-bottom:0;}
.w-sand-expl ul{margin:0;padding-left:20px;}
.w-sand-expl li{margin-bottom:6px;}
.w-sand-expl strong{color:#ffffff;}

.pwn-table{width:100%;border-collapse:collapse;font-family:'JetBrains Mono',monospace;font-size:0.75rem;background:rgba(15,17,26,0.4);margin-top:10px;}
.pwn-table th{background:rgba(0,240,255,0.05);color:#00f0ff;padding:8px;text-align:left;border-bottom:1px solid rgba(255,255,255,0.08);}
.pwn-table td{padding:8px;border-bottom:1px solid rgba(255,255,255,0.04);color:#cbd5e1;}
</style>

<div class="w-sandbox-main">
<!-- Navigation Left Side -->
<div class="w-sandbox-nav">
<button class="w-nav-item active" onclick="showSandboxItem('intoverflow', this)">1. Integer Overflow</button>
<button class="w-nav-item" onclick="showSandboxItem('floatprecision', this)">2. Floating Point Precision</button>
<button class="w-nav-item" onclick="showSandboxItem('arithside', this)">3. Arithmetic Side Effects</button>
<button class="w-nav-item" onclick="showSandboxItem('autoboxing', this)">4. Autoboxing Problems</button>
<button class="w-nav-item" onclick="showSandboxItem('strop', this)">5. String Operation Issues</button>
<button class="w-nav-item" onclick="showSandboxItem('formatstr', this)">6. Format String Vulnerabilities</button>
<button class="w-nav-item" onclick="showSandboxItem('bufoverflow', this)">7. Buffer Overflow Attacks</button>
<button class="w-nav-item" onclick="showSandboxItem('rngattack', this)">8. RNG Predictability</button>
</div>

<!-- Panel details right side -->
<div class="w-sandbox-panels">

<!-- 1. Integer Overflow -->
<div id="panel-intoverflow" class="w-sand-panel active">
<div class="w-sand-hdr"><span>1. Integer Overflow/Underflow</span> <span class="tag">C / Java</span></div>
<pre class="w-sand-code">// C Overflow Example
int x = INT_MAX; // 2147483647
x = x + 1;       // wraps to -2147483648

// Java Logic Exploit
int x = kb.nextInt(); // input: 2147483647
if (x > 0) {
    x = x + 1;
    if (x < 0) { System.out.println("You Win"); }</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>ความเสียหายของตัวแปรประเภทจำนวนเต็มเมื่อรันคณิตศาสตร์เกินขีดจำกัด:</p>
<ul>
<li><strong>Wrap-around</strong>: ในสถาปัตยกรรมคอมพิวเตอร์ ตัวแปร 32-bit signed integer มีค่าสูงที่สุดเท่ากับ <code>2147483647</code> เมื่อเราสั่งบวก 1 จะส่งผลลัพธ์หลุดขอบของข้อมูลและหมุนกลับมาเป็นค่าต่ำสุดคือ <code>-2147483648</code></li>
<li><strong>Security Exploit</strong>: แฮกเกอร์สามารถส่งค่าระดับสูงของตัวแปรเพื่อสั่งหลบเลี่ยงตัวกรองล็อกอินที่เปรียบเทียบค่าเลขบวกหรือลบ หรือส่งเงื่อนไขที่ขัดแย้งกันมาเอาชนะบั๊กของระบบ</li>
<li><strong>การป้องกัน</strong>: สแกนค่าตัวแปรก่อนบวก ลบ หรือดึงใช้งานฟังก์ชันสำเร็จรูปที่มีระบบเช็คความเสถียร เช่น <code>Math.addExact()</code> ในภาษาจาวา</li>
</ul>
</div>
</div>

<!-- 2. Floating Point Precision -->
<div id="panel-floatprecision" class="w-sand-panel">
<div class="w-sand-hdr"><span>2. Floating Point Precision</span> <span class="tag">Python / C</span></div>
<pre class="w-sand-code"># Example 1
if (0.1 + 0.2 == 0.3):
    print("Equal")
else:
    print("Not Equal") # Prints this!

# Example 2 (Ignore small additions)
double large = 1e16;
double small = 1.0;
double result = large + small; // Output: 10000000000000000 (1.0 is ignored!)</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>ข้อจำกัดของระบบการจดจำหมายเลขทศนิยมในสถาปัตยกรรม IEEE 754:</p>
<ul>
<li><strong>IEEE 754 Binary Representation</strong>: คอมพิวเตอร์เก็บข้อมูลทศนิยมในรูปของเลขฐานสอง ทำให้ค่าเช่น 0.1 หรือ 0.2 เป็นตัวเลขซ้ำทศนิยมไม่สิ้นสุด เมื่อต้องนำมาเปรียบเทียบแบบทศนิยมจึงส่งผลให้ค่าเบี่ยงเบนเล็กน้อย (เช่น 0.1 + 0.2 = 0.30000000000000004) และส่งผลให้สมการเช็คเท่ากับ (<code>==</code>) ล้มเหลว</li>
<li><strong>การป้องกัน</strong>: ห้ามนำทศนิยมมาทำสมการเปรียบเทียบ <code>==</code> โดยตรง ให้ใช้ค่าเบี่ยงเบนต่ำสุด (Epsilon) เช่น <code>abs(a - b) < 1e-9</code> หรือสลับเปลี่ยนไปรันด้วยไลบรารีความปลอดภัยสูง เช่น <code>Decimal</code> ในไพธอน หรือ <code>BigDecimal</code> ในจาวา</li>
</ul>
</div>
</div>

<!-- 3. Arithmetic Side Effects -->
<div id="panel-arithside" class="w-sand-panel">
<div class="w-sand-hdr"><span>3. Arithmetic Side Effects</span> <span class="tag">Java / C++ / Python</span></div>
<pre class="w-sand-code">// Division Truncation
int result = 5 / 2; // Output: 2 (not 2.5)

// nan comparison (Example of Python)
x = float('nan')
if x != x:
    print("You Win") # Prints this because NaN != NaN

// Undefined Increment C vs Java
int x = 5;
int y = ++x - --x + ++x - x--; // Undefined behavior in C!</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>ความคลาดเคลื่อนระดับบิตและพฤติกรรมที่ไม่พึงประสงค์จากการคำนวณ:</p>
<ul>
<li><strong>Division by Zero</strong>: ก่อความเสียหายรุนแรงระดับระบบ และทำให้รันไทม์ประมวลผลหยุดทำงานทันที (Crash)</li>
<li><strong>NaN (Not a Number)</strong>: ค่าเปรียบเทียบพิเศษของทศนิยม ซึ่งมีลักษณะเฉพาะตัวคือ <code>NaN != NaN</code> หากเขียนตรรกะระบบเช็คโดยไม่ป้องกัน แฮกเกอร์สามารถยิงค่าอินพุตนี้มาหลบตัวกรองการเปรียบเทียบสิทธิ์</li>
<li><strong>C Undefined Behavior</strong>: ในภาษา C ตัวดำเนินการปรับปรุงแบบ increment หลายตัวบนบรรทัดเดียวกันจะไม่มีผลลัพธ์ตายตัวขึ้นอยู่กับสเปกคอมไพเลอร์ จึงเปิดโอกาสให้เกิดช่องโหว่ความเสถียรข้อมูล</li>
</ul>
</div>
</div>

<!-- 4. Autoboxing Problems -->
<div id="panel-autoboxing" class="w-sand-panel">
<div class="w-sand-hdr"><span>4. Autoboxing Problems</span> <span class="tag">Java</span></div>
<pre class="w-sand-code">// NullPointerException through Unboxing
Integer value = null;
int primitiveValue = value; // CRASH!

// Integer Cache comparison (== checks reference)
Integer a = 127; Integer b = 127; // a == b is True (Cached)
Integer c = 128; Integer d = 128; // c == d is False (New objects)

// Autoboxing logic bypass
Integer x = kb.nextInt(); Integer y = kb.nextInt();
if (x > y || x < y || x == y) { System.out.println("Lose"); }
else { System.out.println("You Win"); } // Win if input >= 128 and ==</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>ความเสียหายจากระบบแปลงตัวแปรอัตโนมัติระว่างคลาสออบเจกต์และตัวแปรพื้นฐานใน Java:</p>
<ul>
<li><strong>Integer Cache Limit</strong>: Java แคชออบเจกต์ของตัวเลขอัตโนมัติเฉพาะในช่วง <code>-128</code> ถึง <code>127</code> หากตัวแปรมีค่า 128 ขึ้นไป ตัวเปรียบเทียบ <code>==</code> จะเป็นการเช็คตรรกะพิกัดออบเจกต์ (Reference Address) แทนการเทียบค่าข้างใน ซึ่งไม่เท่ากันเด็ดขาด</li>
<li><strong>Logic Bypass</strong>: หากแฮกเกอร์ป้อนข้อมูล x = 128 และ y = 128 ทั้ง x และ y จะถูกสร้างเป็นคนละออบเจกต์ ทำให้เงื่อนไข <code>x > y</code>, <code>x < y</code> และ <code>x == y</code> (เทียบพิกัดออบเจกต์) เป็นเท็จทั้งหมด ส่งผลให้หลุดเข้าเงื่อนไข Else (You Win) ได้ทันที</li>
<li><strong>การป้องกัน</strong>: ใช้ฟังก์ชัน <code>.equals()</code> แทนการใช้เครื่องหมาย <code>==</code> ในการเช็คเปรียบเทียบค่าของออบเจกต์ทุกครั้ง</li>
</ul>
</div>
</div>

<!-- 5. String Operation Issues -->
<div id="panel-strop" class="w-sand-panel">
<div class="w-sand-hdr"><span>5. String Operation Issues</span> <span class="tag">Python / Java</span></div>
<pre class="w-sand-code"># Memory Waste
result = ""
for i in range(10000):
    result += "Hello" # BAD: creates 10,000 new objects in memory

# Filter evasion through replace
s = input('Enter s: ')      # Input: &lt;?&lt;?phpphp
s = s.replace('&lt;?php', '')  # Output: &lt;?php
if '&lt;?php' in s:
    print('You Win') # Prints this because inner replacement left one</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>ข้อจำกัดของโครงสร้าง String ที่ไม่สามารถแก้ไขค่าเดิมในตำแหน่งเดิมได้ (Immutability):</p>
<ul>
<li><strong>Immutability Cost</strong>: ทุกครั้งที่ใช้คำสั่งบวกข้อความ (<code>+=</code>) ตัวแปรไพธอนหรือจาวาจะสั่งเคลียร์จองหน่วยความจำเพื่อสร้างชุดข้อมูลขึ้นมาใหม่ ส่งผลให้ระบบทำงานอืดช้าลงมาก</li>
<li><strong>Filter Evasion Bug</strong>: การเขียนฟังก์ชันลบข้อความอันตรายออกเพียงแค่รอบเดียวแบบผิวเผิน (เช่น <code>replace('<?php', '')</code>) จะเปิดช่องโหว่ความปลอดภัยระดับรุนแรง เพราะถ้าแฮกเกอร์ป้อน <code><?<?phpphp</code> เมื่อระบบลบคำดักตรงกลางออก อักษรซ้ายและขวาจะเลื่อนมาชิดกันเกิดเป็นคำเดิมเป้าหมายอีกครั้ง</li>
<li><strong>การป้องกัน</strong>: ใช้ฟังก์ชันตรวจกรองแบบวนลูปต่อเนื่อง หรือปรับปรุงมาใช้ระเบียบตรวจสอบรูปประโยคแบบ Regular Expression</li>
</ul>
</div>
</div>

<!-- 6. Format String Vulnerabilities -->
<div id="panel-formatstr" class="w-sand-panel">
<div class="w-sand-hdr"><span>6. Format String Vulnerabilities</span> <span class="tag">C / Python</span></div>
<pre class="w-sand-code">// Insecure C Code
char input[100];
fgets(input, sizeof(input), stdin);
printf(input); // Vulnerable: If user enters "%x %x %x" it dumps stack

// Format String Injection in Python
user_input = input("Enter your name: ")
message = "Hello, {}".format(user_input)
# Vulnerable if user injects formatting directives dynamically</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>ความเสียหายจากการวางตำแหน่งตัวแปรให้อินพุตควบคุมฟังก์ชันแสดงผลฟอร์แมตโดยตรง:</p>
<ul>
<li><strong>Format Specifier Dump</strong>: ในภาษา C ฟังก์ชัน <code>printf(user_input)</code> เปิดโอกาสให้แฮกเกอร์ป้อนรหัสฟอร์แมตระบุตำแหน่ง เช่น <code>%x</code> หรือ <code>%p</code> เพื่อดึงข้อมูลสถานะในหน่วยความจำ Stack ออกมาทั้งหมด (Dump) หรือป้อนค่า <code>%n</code> เขียนทับตำแหน่งของสิทธิ์แอปพลิเคชัน</li>
<li><strong>การป้องกัน</strong>: ห้ามส่งตัวแปรตรงผ่าน printf ให้ครอบฟอร์แมตคงที่ตลอดเวลา เช่น <code>printf("%s", user_input)</code></li>
</ul>
</div>
</div>

<!-- 7. Buffer Overflow Attacks -->
<div id="panel-bufoverflow" class="w-sand-panel">
<div class="w-sand-hdr"><span>7. Buffer Overflow Attacks</span> <span class="tag">C Code</span></div>
<pre class="w-sand-code">#include&lt;stdio.h&gt;
int main() {
    char s[28]; // Buffer
    int a = 0;  // Target variable
    printf("Enter Your Name: ");
    scanf("%s", &s); // Vulnerable to overwrite a
    if (a == 12345) { printf("You Win\\n"); }</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การป้อนข้อมูลเกินขอบเขตบัฟเฟอร์ในหน่วยความจำเพื่อเปลี่ยนแปลงค่าตัวแปรใกล้เคียง:</p>
<ul>
<li><strong>Memory Layout Overwrite</strong>: ตัวแปรอาเรย์ <code>s</code> มีขนาด 28 ไบต์ และอยู่ติดกับตัวแปร <code>a</code> ใน Stack หากรับอินพุตยาวเกิน 28 ไบต์ ข้อมูลที่ล้นจะเข้าไปเขียนทับหน่วยความจำของตัวแปร <code>a</code> ทันที</li>
<li><strong>Little-Endian Target</strong>: เลข 12345 เท่ากับ <code>0x3039</code> ในฐานสิบหก หากแฮกเกอร์ป้อนอักษร 28 ไบต์ และตามด้วย <code>\\x39\\x30\\x00\\x00</code> (แบบ Little-Endian) ตัวแปร <code>a</code> จะได้รับค่า 12345 และทำให้ควบคุมสมการเงื่อนไขได้สำเร็จ</li>
<li><strong>การป้องกัน</strong>: บังคับใช้ฟังก์ชันจัดการข้อความจำกัดขอบเขตความกว้างที่ปลอดภัย เช่น <code>fgets()</code> แทนการใช้ <code>gets()</code> หรือ <code>scanf()</code> แบบธรรมดา</li>
</ul>
</div>
</div>

<!-- 8. RNG Predictability -->
<div id="panel-rngattack" class="w-sand-panel">
<div class="w-sand-hdr"><span>8. RNG Predictability</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import random
from randcrack import RandCrack

rc = RandCrack()
# Mersenne Twister PRNG state recovery
for _ in range(624):
    rc.submit(random.getrandbits(32))

# Predict next output
predicted = rc.predict_getrandbits(32)</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>ความเปราะบางของระบบสร้างเลขสุ่มเสียมารยาท (Pseudo-Random Number Generator):</p>
<ul>
<li><strong>PRNG State Recovery</strong>: โมดูล <code>random</code> ของไพธอนใช้อัลกอริทึม Mersenne Twister ซึ่งเป็นเครื่องสร้างสุ่มเทียมที่ไม่ปลอดภัยในเชิงความลับ หากแฮกเกอร์ดักเก็บข้อมูลสุ่มก่อนหน้าครบ <code>624</code> ค่า จะสามารถจำลองสร้างโครงสร้างภายในของสุ่มตัวถัดไปได้อย่างแม่นยำ 100%</li>
<li><strong>การป้องกัน</strong>: สำหรับงานความปลอดภัยไซเบอร์ ระบบการเข้ารหัสลับ หรือการสุ่มโทเคนล็อกอิน บังคับเปลี่ยนไปใช้ฟังก์ชัน Cryptographically Secure PRNG (CSPRNG) เช่น โมดูล <code>secrets</code> ของ Python หรือ <code>java.security.SecureRandom</code> ใน Java เท่านั้น</li>
</ul>

<table class="pwn-table">
<thead>
<tr>
<th>สุ่มเทียมไม่ปลอดภัย (PRNG)</th>
<th>สุ่มปลอดภัยสูง (CSPRNG)</th>
</tr>
</thead>
<tbody>
<tr><td>random.seed(12345)</td><td>secrets.token_hex(16)</td></tr>
<tr><td>java.util.Random</td><td>java.security.SecureRandom</td></tr>
<tr><td>rand() % 100</td><td>/dev/urandom หรือ hardware entropy</td></tr>
</tbody>
</table>
</div>
</div>

</div>
</div>

<script>
window.showSandboxItem = function(itemKey, element) {
  const items = document.querySelectorAll('.w-sandbox-nav .w-nav-item');
  items.forEach(i => i.classList.remove('active'));
  element.classList.add('active');

  const panels = document.querySelectorAll('.w-sand-panel');
  panels.forEach(p => {
    p.style.setProperty('display', 'none', 'important');
  });

  const targetPanel = document.getElementById('panel-' + itemKey);
  if (targetPanel) {
    targetPanel.style.setProperty('display', 'block', 'important');
  }
}
</script>"""
})

# Block 4: Interactive Mini-Quiz 2 questions with Neon Gauge Bar
blocks_172.append({
    "type": "markdown",
    "value": """### ✏️ Lesson Quick Quiz (แบบทดสอบทบทวนความรู้ท้ายบทเรียน)

ตอบคำถามประเมินความรู้ 2 ข้อด้านล่างนี้ให้ถูกต้องครบถ้วนเพื่อทำการผ่านบทเรียนย่อยนี้ (Lesson Clear):

<style>
.mini-quiz-box{width:100%;max-width:1050px;margin:2rem auto;background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:24px;box-shadow:0 8px 32px rgba(0,0,0,0.3);box-sizing:border-box;}
.mq-q{margin-bottom:20px;}
.mq-title{font-size:0.9rem;font-weight:800;color:#e2e8f0;margin-bottom:10px;}
.mq-title span{color:#00f0ff;font-family:'JetBrains Mono',monospace;margin-right:6px;}
.mini-opts{display:flex;flex-direction:column;gap:6px;}
.mini-opt{display:flex;align-items:center;gap:10px;padding:10px 14px;background:rgba(255,255,255,0.015);border:1px solid rgba(255,255,255,0.05);border-radius:8px;cursor:pointer;transition:all 0.15s ease;user-select:none;font-size:0.83rem;color:#cbd5e1;}
.mini-opt:hover{border-color:rgba(0,240,255,0.2);background:rgba(0,240,255,0.02);}
.mini-opt.selected{border-color:#00f0ff;background:rgba(0,240,255,0.08);color:#ffffff;}
.mini-opt.correct{border-color:#3ddc84;background:rgba(61,220,132,0.08);color:#ffffff;}
.mini-opt.incorrect{border-color:#ff007f;background:rgba(255,0,127,0.08);color:#ffffff;}
.mini-bullet{width:15px;height:15px;border:1px solid rgba(255,255,255,0.3);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:0.58rem;font-weight:bold;}
.mini-opt.selected .mini-bullet{border-color:#00f0ff;background:#00f0ff;color:#070910;}

/* Neon Gauge Progress Bar styling */
.mq-progress-container{width:100%;background:rgba(7,9,16,0.8);border:1px solid rgba(255,255,255,0.08);height:26px;border-radius:13px;position:relative;overflow:hidden;margin:20px 0;display:flex;align-items:center;box-shadow:inset 0 2px 8px rgba(0,0,0,0.6);}
.mq-progress-bar{width:0%;height:100%;background:linear-gradient(90deg, #ff007f 0%, #fbbf24 50%, #00f0ff 100%);transition:all 0.35s cubic-bezier(0.4, 0, 0.2, 1);box-shadow:0 0 12px rgba(0,240,255,0.2);}
.mq-progress-text{position:absolute;width:100%;text-align:center;font-family:'JetBrains Mono',monospace;font-size:0.75rem;font-weight:800;color:#ffffff;text-shadow:0 1px 3px rgba(0,0,0,0.9);z-index:2;letter-spacing:0.05em;}

.mq-btn-check{padding:10px 20px;background:#00f0ff;border:none;border-radius:6px;font-family:'JetBrains Mono',monospace;font-size:0.82rem;font-weight:800;color:#070910;cursor:pointer;box-shadow:0 0 10px rgba(0,240,255,0.25);transition:all 0.15s ease;}
.mq-btn-check:hover{background:#ffffff;box-shadow:0 0 15px rgba(255,255,255,0.4);transform:translateY(-1px);}
.mq-status-bar{display:none;padding:12px 16px;border-radius:8px;font-size:0.85rem;margin-top:16px;font-weight:700;line-height:1.5;}
</style>

<div id="mq-box-348" class="mini-quiz-box">
<!-- Question 1 -->
<div class="mq-q" data-correct="B">
<div class="mq-title"><span>Q1.</span> ในภาษา Java เหตุใดสมการเงื่อนไขออบเจกต์เปรียบเทียบ `Integer a = 128; Integer b = 128; a == b` จึงได้ผลลัพธ์การประมวลผลความปลอดภัยเป็นเท็จ (False)?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A" onclick="updateMiniProgress(348)"><span class="mini-bullet">A</span> เพราะค่า 128 เกินขีดจำกัดขนาดความกว้างแบบล้นค่า wrap-around ติดลบทันที</div>
<div class="mini-opt" data-val="B" onclick="updateMiniProgress(348)"><span class="mini-bullet">B</span> เพราะ Java จะทำการแคชออบเจกต์เฉพาะช่วง -128 ถึง 127 ทำให้ตัวเลข 128 เป็นออบเจกต์คนละพิกัดในหน่วยความจำ</div>
<div class="mini-opt" data-val="C" onclick="updateMiniProgress(348)"><span class="mini-bullet">C</span> เพราะเบราว์เซอร์ส่งข้อความเป็นรหัส ASCII ที่ไม่เสถียรใน JVM</div>
</div>
</div>

<!-- Question 2 -->
<div class="mq-q" data-correct="C">
<div class="mq-title"><span>Q2.</span> หากผู้ทดสอบใช้ซอฟต์แวร์ RandCrack สแกนและพยากรณ์ค่าสุ่มถัดไปของโมดูล random ใน Python ได้สำเร็จ จะต้องดักจับข้อมูลและส่งค่าประวัติสุ่มก่อนหน้าปริมาณเท่าใด?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A" onclick="updateMiniProgress(348)"><span class="mini-bullet">A</span> 128 ค่า (หรือ 128 บิต)</div>
<div class="mini-opt" data-val="B" onclick="updateMiniProgress(348)"><span class="mini-bullet">B</span> 256 ค่า</div>
<div class="mini-opt" data-val="C" onclick="updateMiniProgress(348)"><span class="mini-bullet">C</span> 624 ค่า</div>
</div>
</div>

<!-- Neon Gauge Bar Progress -->
<div class="mq-progress-container">
<div id="mq-progress-bar-348" class="mq-progress-bar"></div>
<span id="mq-progress-text-348" class="mq-progress-text">Lesson Progress: 0% (ยังไม่ผ่าน)</span>
</div>

<button class="mq-btn-check" onclick="checkMiniQuiz(348)">Check Answers / ตรวจคำตอบ</button>
<div id="mq-status-348" class="mq-status-bar"></div>
</div>

<script>
// Attach click listeners to manage selection state
document.querySelectorAll('#mq-box-348 .mini-opt').forEach(opt => {
  opt.addEventListener('click', function() {
    const parent = this.closest('.mq-q');
    parent.querySelectorAll('.mini-opt').forEach(o => o.classList.remove('selected'));
    this.classList.add('selected');
  });
});

function updateMiniProgress(lnum) {
  const box = document.getElementById('mq-box-' + lnum);
  const qGroups = box.querySelectorAll('.mq-q');
  let answeredCount = 0;
  
  qGroups.forEach(g => {
    if (g.querySelector('.mini-opt.selected')) {
      answeredCount++;
    }
  });

  const pct = Math.round((answeredCount / qGroups.length) * 100);
  const pbar = document.getElementById('mq-progress-bar-' + lnum);
  const ptext = document.getElementById('mq-progress-text-' + lnum);

  if (pct > 0) {
    pbar.style.width = pct + '%';
    pbar.style.background = 'linear-gradient(90deg, #ff007f 0%, #fbbf24 100%)';
    ptext.textContent = 'Lesson Progress: ' + pct + '% (ตอบคำถามค้างอยู่)';
  }
}

function checkMiniQuiz(lnum) {
  const box = document.getElementById('mq-box-' + lnum);
  const groups = box.querySelectorAll('.mq-q');
  let score = 0;
  let allAnswered = true;

  groups.forEach(g => {
    const selected = g.querySelector('.mini-opt.selected');
    if (!selected) allAnswered = false;
  });

  if (!allAnswered) {
    alert("กรุณาตอบคำถามท้ายบทให้ครบถ้วนทั้ง 2 ข้อก่อนส่งตรวจคำตอบครับ!");
    return;
  }

  groups.forEach(g => {
    const correctVal = g.getAttribute('data-correct');
    const selected = g.querySelector('.mini-opt.selected');
    const selectedVal = selected.getAttribute('data-val');

    g.querySelectorAll('.mini-opt').forEach(o => {
      o.classList.remove('correct', 'incorrect');
      const val = o.getAttribute('data-val');
      if (val === correctVal) {
        o.classList.add('correct');
      } else if (o.classList.contains('selected')) {
        o.classList.add('incorrect');
      }
    });

    if (selectedVal === correctVal) score++;
  });

  const pbar = document.getElementById('mq-progress-bar-' + lnum);
  const ptext = document.getElementById('mq-progress-text-' + lnum);
  const status = document.getElementById('mq-status-' + lnum);
  status.style.display = 'block';

  if (score === 2) {
    pbar.style.width = '100%';
    pbar.style.background = '#3ddc84';
    pbar.style.boxShadow = '0 0 15px rgba(61,220,132,0.6)';
    ptext.textContent = 'Lesson Progress: 100% (ผ่านเรียบร้อย)';
    
    status.style.background = 'rgba(61,220,132,0.08)';
    status.style.border = '1px solid rgba(61,220,132,0.25)';
    status.style.color = '#3ddc84';
    status.innerHTML = '🏆 <strong>LESSON CLEARED!</strong> คุณผ่านการประเมินความรู้ท้ายบทเรียนย่อยนี้เรียบร้อย (คะแนน 2/2) สามารถเดินทางไปศึกษาบทเรียนถัดไปได้ครับ!';
  } else {
    const errorPct = Math.round((score / groups.length) * 100);
    pbar.style.width = errorPct + '%';
    pbar.style.background = '#ff007f';
    pbar.style.boxShadow = '0 0 15px rgba(255,0,127,0.6)';
    ptext.textContent = 'Lesson Progress: ' + errorPct + '% (ไม่ผ่าน - ทำไม่จบ)';

    status.style.background = 'rgba(255,0,127,0.08)';
    status.style.border = '1px solid rgba(255,0,127,0.25)';
    status.style.color = '#ff007f';
    status.innerHTML = '❌ <strong>ยังไม่ผ่าน!</strong> คุณได้คะแนน ' + score + '/2 (ทำข้อสอบไม่จบตาม Gauge Bar Progress) กรุณาทบทวนบทเรียนและตรวจเลือกคำตอบใหม่อีกครั้ง';
  }
}
</script>"""
})

# ─── 2. Save and Commit the Restructured Lesson 172 to Database ───
l172.content = json.dumps(blocks_172, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=172).update({"content": l172.content})
db.session.commit()
print("Lesson 172 content completely redesigned and committed!")
ctx.pop()
