import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l172 = db.session.query(TutorialLesson).filter_by(id=172).first()
blocks = json.loads(l172.content)

# ─── Update Block 3 of Lesson 172 to include Terminal Outputs ───
blocks[3]['value'] = """### 💻 Code Security Console (วิเคราะห์เจาะลึก 8 รูปแบบบั๊กและตรรกะระบบ)

คลิกหัวข้อด้านซ้ายมือเพื่อตรวจสอบช่องโหว่ความมั่นคงปลอดภัย (Code) และ **ตัวอย่างการรันโปรแกรมพร้อมผลลัพธ์ทางเทอร์มินัล (Terminal Run & Output)** และความมั่นคงปลอดภัยเชิงระบบ:

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
.w-sand-code{font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#00f0ff;white-space:pre-wrap;margin:0 0 12px;background:rgba(0,0,0,0.2);padding:14px;border-radius:8px;border:1px solid rgba(255,255,255,0.02);}

/* Terminal Output Box Styling */
.w-sand-term{font-family:'JetBrains Mono',monospace;font-size:0.76rem;color:#a7f3d0;background:#02040a;border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:12px 16px;margin-bottom:16px;box-shadow:inset 0 2px 6px rgba(0,0,0,0.85);white-space:pre-wrap;position:relative;}
.w-sand-term::before{content:"🐚 Terminal Output";display:block;font-size:0.65rem;color:#64748b;margin-bottom:6px;text-transform:uppercase;font-weight:800;letter-spacing:0.06em;}
.w-sand-term span.prompt{color:#3ddc84;}
.w-sand-term span.cmd{color:#ffffff;font-weight:bold;}

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
<div class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">./integer_overflow_test</span>
Before: 2147483647
After: -2147483648 (wrap-around)

<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">java TestJava</span>
Enter x: 2147483647
You Win</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>ความเสียหายของตัวแปรประเภทจำนวนเต็มเมื่อรันคณิตศาสตร์เกินขีดจำกัด:</p>
<ul>
<li><strong>Wrap-around</strong>: ในสถาปัตยกรรมคอมพิวเตอร์ ตัวแปร 32-bit signed integer มีค่าสูงที่สุดเท่ากับ <code>2147483647</code> เมื่อเราสั่งบวก 1 จะส่งผลลัพธ์หลุดขอบของข้อมูลและหมุนกลับมาเป็นค่าต่ำสุดคือ <code>-2147483648</code></li>
<li><strong>Security Exploit</strong>: แฮกเกอร์สามารถส่งค่าระดับสูงของตัวแปรเพื่อสั่งหลบเลี่ยงตัวกรองล็อกอินที่เปรียบเทียบค่าเลขบวกหรือลบ หรือส่งเงื่อนไขที่ขัดแย้งกันมาเอาชนะบั๊กของระบบ</li>
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
<div class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 float_test.py</span>
Not Equal

<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">./precision_loss_c</span>
Result: 10000000000000000 (1.0 is ignored!)</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>ข้อจำกัดของระบบการจดจำหมายเลขทศนิยมในสถาปัตยกรรม IEEE 754:</p>
<ul>
<li><strong>IEEE 754 Binary Representation</strong>: คอมพิวเตอร์เก็บข้อมูลทศนิยมในรูปของเลขฐานสอง ทำให้ค่าเช่น 0.1 หรือ 0.2 เป็นตัวเลขซ้ำทศนิยมไม่สิ้นสุด เมื่อต้องนำมาเปรียบเทียบแบบทศนิยมจึงส่งผลให้ค่าเบี่ยงเบนเล็กน้อย (เช่น 0.1 + 0.2 = 0.30000000000000004) และส่งผลให้สมการเช็คเท่ากับ (<code>==</code>) ล้มเหลว</li>
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
    print("You Win") # Prints this because NaN != NaN</pre>
<div class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 nan_test.py</span>
You Win

<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 -c "print(10 / 0)"</span>
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ZeroDivisionError: division by zero</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>ความคลาดเคลื่อนระดับบิตและพฤติกรรมที่ไม่พึงประสงค์จากการคำนวณ:</p>
<ul>
<li><strong>Division by Zero</strong>: ก่อความเสียหายรุนแรงระดับระบบ และทำให้รันไทม์ประมวลผลหยุดทำงานทันที (Crash)</li>
<li><strong>NaN (Not a Number)</strong>: ค่าเปรียบเทียบพิเศษของทศนิยม ซึ่งมีลักษณะเฉพาะตัวคือ <code>NaN != NaN</code> หากเขียนตรรกะระบบเช็คโดยไม่ป้องกัน แฮกเกอร์สามารถยิงค่าอินพุตนี้มาหลบตัวกรองการเปรียบเทียบสิทธิ์</li>
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
else { System.out.println("You Win"); }</pre>
<div class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">java TestJavaCache</span>
a == b: true
c == d: false

<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">java TestJavaBypass</span>
Enter x: 128
Enter y: 128
You Win</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>ความเสียหายจากระบบแปลงตัวแปรอัตโนมัติระว่างคลาสออบเจกต์และตัวแปรพื้นฐานใน Java:</p>
<ul>
<li><strong>Integer Cache Limit</strong>: Java แคชออบเจกต์ของตัวเลขอัตโนมัติเฉพาะในช่วง <code>-128</code> ถึง <code>127</code> หากตัวแปรมีค่า 128 ขึ้นไป ตัวเปรียบเทียบ <code>==</code> จะเป็นการเช็คตรรกะพิกัดออบเจกต์ (Reference Address) แทนการเทียบค่าข้างใน ซึ่งไม่เท่ากันเด็ดขาด</li>
<li><strong>Logic Bypass</strong>: หากแฮกเกอร์ป้อนข้อมูล x = 128 และ y = 128 ทั้ง x และ y จะถูกสร้างเป็นคนละออบเจกต์ ทำให้เงื่อนไข <code>x > y</code>, <code>x < y</code> และ <code>x == y</code> (เทียบพิกัดออบเจกต์) เป็นเท็จทั้งหมด ส่งผลให้หลุดเข้าเงื่อนไข Else (You Win) ได้ทันที</li>
</ul>
</div>
</div>

<!-- 5. String Operation Issues -->
<div id="panel-strop" class="w-sand-panel">
<div class="w-sand-hdr"><span>5. String Operation Issues</span> <span class="tag">Python / Java</span></div>
<pre class="w-sand-code"># Filter evasion through replace
s = input('Enter s: ')      # Input: &lt;?&lt;?phpphp
s = s.replace('&lt;?php', '')  # Output: &lt;?php
if '&lt;?php' in s:
    print('You Win') # Prints this because inner replacement left one</pre>
<div class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 replacement_test.py</span>
Enter s: <?<?phpphp
You Win</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>ข้อจำกัดของโครงสร้าง String ที่ไม่สามารถแก้ไขค่าเดิมในตำแหน่งเดิมได้ (Immutability):</p>
<ul>
<li><strong>Filter Evasion Bug</strong>: การเขียนฟังก์ชันลบข้อความอันตรายออกเพียงแค่รอบเดียวแบบผิวเผิน (เช่น <code>replace('<?php', '')</code>) จะเปิดช่องโหว่ความปลอดภัยระดับรุนแรง เพราะถ้าแฮกเกอร์ป้อน <code><?<?phpphp</code> เมื่อระบบลบคำดักตรงกลางออก อักษรซ้ายและขวาจะเลื่อนมาชิดกันเกิดเป็นคำเดิมเป้าหมายอีกครั้ง</li>
</ul>
</div>
</div>

<!-- 6. Format String Vulnerabilities -->
<div id="panel-formatstr" class="w-sand-panel">
<div class="w-sand-hdr"><span>6. Format String Vulnerabilities</span> <span class="tag">C / Python</span></div>
<pre class="w-sand-code">// Insecure C Code
char input[100];
fgets(input, sizeof(input), stdin);
printf(input); // Vulnerable: If user enters "%x %x %x" it dumps stack</pre>
<div class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">./format_string_test</span>
Guess: %x %x %x %x
ffe012ac 0 4012ba4d ffe012c4
You Lose</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>ความเสียหายจากการวางตำแหน่งตัวแปรให้อินพุตควบคุมฟังก์ชันแสดงผลฟอร์แมตโดยตรง:</p>
<ul>
<li><strong>Format Specifier Dump</strong>: ในภาษา C ฟังก์ชัน <code>printf(user_input)</code> เปิดโอกาสให้แฮกเกอร์ป้อนรหัสฟอร์แมตระบุตำแหน่ง เช่น <code>%x</code> หรือ <code>%p</code> เพื่อดึงข้อมูลสถานะในหน่วยความจำ Stack ออกมาทั้งหมด (Dump) หรือป้อนค่า <code>%n</code> เขียนทับตำแหน่งของสิทธิ์แอปพลิเคชัน</li>
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
<div class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 -c "print('A'*28 + '\\x39\\x30\\x00\\x00')" | ./buffer_overflow</span>
Enter Your Name: You Win</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การป้อนข้อมูลเกินขอบเขตบัฟเฟอร์ในหน่วยความจำเพื่อเปลี่ยนแปลงค่าตัวแปรใกล้เคียง:</p>
<ul>
<li><strong>Memory Layout Overwrite</strong>: ตัวแปรอาเรย์ <code>s</code> มีขนาด 28 ไบต์ และอยู่ติดกับตัวแปร <code>a</code> ใน Stack หากรับอินพุตยาวเกิน 28 ไบต์ ข้อมูลที่ล้นจะเข้าไปเขียนทับหน่วยความจำของตัวแปร <code>a</code> ทันที</li>
<li><strong>Little-Endian Target</strong>: เลข 12345 เท่ากับ <code>0x3039</code> ในฐานสิบหก หากแฮกเกอร์ป้อนอักษร 28 ไบต์ และตามด้วย <code>\\x39\\x30\\x00\\x00</code> (แบบ Little-Endian) ตัวแปร <code>a</code> จะได้รับค่า 12345 และทำให้ควบคุมสมการเงื่อนไขได้สำเร็จ</li>
</ul>
</div>
</div>

<!-- 8. RNG Predictability -->
<div id="panel-rngattack" class="w-sand-panel">
<div class="w-sand-hdr"><span>8. RNG Predictability</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import random
random.seed(12345)
for i in range(10):
    print(random.randint(1, 100), end=' ')</pre>
<div class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 Test.py</span>
54 94 2 39 48 25 35 73 56 21
<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 Test.py</span>
54 94 2 39 48 25 35 73 56 21
<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 Test.py</span>
54 94 2 39 48 25 35 73 56 21</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>ความเปราะบางของระบบสร้างเลขสุ่มเสียมารยาท (Pseudo-Random Number Generator):</p>
<ul>
<li><strong>PRNG State Recovery</strong>: โมดูล <code>random</code> ของไพธอนใช้อัลกอริทึม Mersenne Twister ซึ่งเป็นเครื่องสร้างสุ่มเทียมที่ไม่ปลอดภัยในเชิงความลับ หากแฮกเกอร์ดักเก็บข้อมูลสุ่มก่อนหน้าครบ <code>624</code> ค่า จะสามารถจำลองสร้างโครงสร้างภายในของสุ่มตัวถัดไปได้อย่างแม่นยำ 100%</li>
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

l172.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=172).update({"content": l172.content})
db.session.commit()
print("Lesson 172 Terminal Outputs successfully integrated!")
ctx.pop()
