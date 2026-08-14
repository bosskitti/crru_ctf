import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

# ─── 1. Shift Lesson 172 to Position 6 to make room for Lesson 199 ───
l172 = db.session.query(TutorialLesson).filter_by(id=172).first()
if l172:
    l172.position = 6
    l172.title = "06. การเขียนโค้ดที่ไม่มีความปลอดภัยและช่องโหว่ (Insecure Coding & Buffer Overflows)"
    db.session.commit()
    print("Lesson 172 shifted to Position 6.")

# ─── 2. Construct content blocks for Lesson 199 (05. Cryptography) ───
blocks_199 = []

# Block 0: Title & Header
blocks_199.append({
    "type": "markdown",
    "value": "## 🔐 ทักษะโปรแกรมมิ่งสำหรับการเข้ารหัสลับข้อมูล (Programming Skills for Cryptography)"
})

# Block 1: Cryptographic Concepts
blocks_199.append({
    "type": "markdown",
    "value": """### 🛡️ Core Cryptographic Concepts

การเขียนโปรแกรมและการจัดการระบบความปลอดภัยไซเบอร์ จำเป็นต้องเข้าใจแนวคิดคณิตศาสตร์ของวิทยาการรหัสลับ (Cryptography) 3 รูปแบบหลัก เพื่อนำไปใช้ป้องกันการเข้าถึงข้อมูลโดยมิชอบ:

<style>
.crypto-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:2rem auto;max-width:1050px;}
@media(max-width:820px){.crypto-grid{grid-template-columns:1fr;}}
.crypto-card{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:10px;padding:20px;box-sizing:border-box;transition:all 0.25s ease;display:flex;flex-direction:column;justify-content:between;}
.crypto-card:hover{border-color:#00f0ff;background:rgba(0,240,255,0.02);transform:translateY(-2px);box-shadow:0 0 15px rgba(0,240,255,0.25);}
.crypto-title{font-size:0.92rem;font-weight:800;color:#00f0ff;margin-bottom:8px;border-bottom:1px solid rgba(255,255,255,0.05);padding-bottom:6px;}
.crypto-desc{font-size:0.8rem;color:#94a3b8;line-height:1.65;margin:0 0 10px;}
.crypto-badge{font-size:0.68rem;font-weight:700;color:#fbbf24;font-family:'JetBrains Mono',monospace;}
</style>

<div class="crypto-grid">
<!-- Symmetric -->
<div class="crypto-card">
<div>
<div class="crypto-title">🔑 Symmetric Encryption</div>
<p class="crypto-desc">การเข้ารหัสแบบสมมาตรที่ใช้ <strong>กุญแจเดียวกัน (Same Key)</strong> ทั้งในการเข้ารหัสและถอดรหัสข้อมูล รวดเร็วและเหมาะกับข้อมูลขนาดใหญ่</p>
</div>
<span class="crypto-badge">Algorithms: AES, DES, 3DES</span>
</div>

<!-- Asymmetric -->
<div class="crypto-card">
<div>
<div class="crypto-title">🗝️ Asymmetric Encryption</div>
<p class="crypto-desc">การเข้ารหัสแบบอสมมาตรที่ใช้ <strong>คู่กุญแจ (KeyPair)</strong>: Public Key สำหรับให้ผู้อื่นเข้ารหัส และ Private Key สำหรับเจ้าของใช้ถอดรหัสลับ</p>
</div>
<span class="crypto-badge">Algorithms: RSA, ECC</span>
</div>

<!-- Hashing -->
<div class="crypto-card">
<div>
<div class="crypto-title">🔢 Cryptographic Hashing</div>
<p class="crypto-desc">การแปลงข้อมูลให้กลายเป็นค่าลายนิ้วมือข้อมูลที่มี <strong>ขนาดคงที่ (Fixed-size)</strong> แบบทางเดียว (One-way) ไม่สามารถย้อนรอยกลับเป็นข้อมูลจริงได้</p>
</div>
<span class="crypto-badge">Algorithms: SHA-256, MD5, bcrypt</span>
</div>
</div>"""
})

blocks_199.append({"type": "markdown", "value": "---"})

# Block 2: Interactive Cryptography Code Console with Detailed Line-by-Line analysis
blocks_199.append({
    "type": "markdown",
    "value": """### 💻 Cryptography Coding Sandbox (วิเคราะห์เจาะลึก 5 ตัวอย่างโค้ดรหัสลับ)

คลิกหัวข้อด้านซ้ายมือเพื่อตรวจสอบตัวอย่างโค้ดระบบวิทยาการรหัสลับ (Code) และ **การวิเคราะห์การทำงานอย่างละเอียดในเชิงความปลอดภัยไซเบอร์ (Detailed Security Analysis)**:

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
</style>

<div class="w-sandbox-main">
<!-- Navigation Left Side -->
<div class="w-sandbox-nav">
<button class="w-nav-item active" onclick="showSandboxItem('logicflag', this)">1. Logic Flag (C++)</button>
<button class="w-nav-item" onclick="showSandboxItem('xorflag', this)">2. XOR Flag Helper (Python)</button>
<button class="w-nav-item" onclick="showSandboxItem('aesmode', this)">3. AES CBC Symmetric</button>
<button class="w-nav-item" onclick="showSandboxItem('rsaasym', this)">4. RSA Asymmetric (2048-bit)</button>
<button class="w-nav-item" onclick="showSandboxItem('hashpass', this)">5. SHA-256 Password Hash</button>
</div>

<!-- Panel details right side -->
<div class="w-sandbox-panels">

<!-- 1. Logic Flag (C++) -->
<div id="panel-logicflag" class="w-sand-panel active">
<div class="w-sand-hdr"><span>1. Logic Flag Example</span> <span class="tag">C++ Code</span></div>
<pre class="w-sand-code" style="color:#3ddc84;">#include &lt;iostream&gt;
#include &lt;string&gt;
using namespace std;
int main() {
    unsigned int flag[] = { 754, 708, 734, ... };
    unsigned int key, code, i;
    cout << "Key: ";
    cin >> key;
    for(i = 0; i < 53; i++) {
        code = flag[i] ^ key;
        cout << (char) code;
    }
    cout << endl;
    return 0;
}</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>โปรแกรมภาษา C++ ในการถอดรหัส Flag ออกจากอาร์เรย์ตัวเลขด้วยตัวดำเนินการบิต XOR:</p>
<ul>
<li><strong>unsigned int flag[]</strong>: อาร์เรย์เก็บตัวเลขเลขฐานสิบที่เกิดจากการเข้ารหัสตัวอักษรของ Flag</li>
<li><strong>flag[i] ^ key</strong>: ตัวดำเนินการบิต XOR (Exclusive OR) ซึ่งในวิทยาการรหัสลับถือเป็นสมการที่ผันกลับได้ หากนำข้อมูลเข้ารหัสมา XOR กับ Key เดิมจะนำไปสู่การถอดกลับเป็นค่าอักขระดั้งเดิม</li>
<li><strong>(char) code</strong>: การแปลงประเภทข้อมูล (Type Casting) จากตัวเลขอักขระรหัส ASCII กลับมาเป็นตัวอักษรธรรมดาพิมพ์ออกหน้าจอ</li>
</ul>
</div>
</div>

<!-- 2. XOR Flag (Python) -->
<div id="panel-xorflag" class="w-sand-panel">
<div class="w-sand-hdr"><span>2. XOR Flag Helper</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import codecs
def xor(flag, key):
    flag = flag.encode()
    key = key.encode()
    msg = flag + b'&&' + key
    s = b''
    for i in range(len(msg)):
        s += bytes([msg[i] ^ key[i%len(key)]])
    return codecs.encode(s, "hex").decode()</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>ฟังก์ชัน Python สำหรับการทำ XOR แบบสลับเปลี่ยนขนาดกุญแจซ้ำ (Repeating XOR):</p>
<ul>
<li><strong>key[i%len(key)]</strong>: คอนเซ็ปต์การหารเศษเหลือเพื่อนำมาขยายคีย์ให้มีความยาวเท่ากันกับข้อความ เหมาะกับการเดาเจาะรหัสประเภท XOR key ขนาดสั้น</li>
<li><strong>codecs.encode(s, "hex")</strong>: แปลงผลลัพธ์เป็นข้อความเลขฐานสิบหก (Hexadecimal format) เพื่อไม่ให้อักษรพิเศษที่เกิดจากการ XOR แสดงผลผิดเพี้ยนบนเบราว์เซอร์</li>
</ul>
</div>
</div>

<!-- 3. AES CBC Symmetric -->
<div id="panel-aesmode" class="w-sand-panel">
<div class="w-sand-hdr"><span>3. AES CBC Symmetric Example</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC)
plaintext = b"Hello, World!"
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

decipher = AES.new(key, AES.MODE_CBC, cipher.iv)
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>สคริปต์ความปลอดภัยแบบเข้ารหัสลับ AES ในโหมด CBC (Cipher Block Chaining):</p>
<ul>
<li><strong>get_random_bytes(16)</strong>: สุ่มคีย์ความยาว 128 บิต ซึ่งมีความซับซ้อนยากต่อการเดาสุ่มด้วยเครื่องคอมพิวเตอร์</li>
<li><strong>pad(plaintext, AES.block_size)</strong>: เนื่องจาก AES CBC กำหนดให้ข้อมูลมีขนาดคงตัวเป็นบล็อก 16 ไบต์ จึงจำเป็นต้องเสริมข้อมูลส่วนเติมเต็ม (Padding) ให้ครบขนาดบล็อกก่อนรันเข้ารหัส</li>
<li><strong>cipher.iv (Initialization Vector)</strong>: ค่ากำหนดตั้งต้นแบบสุ่มเพื่อป้องกันไม่ให้บล็อกข้อมูลที่เหมือนกันเข้ารหัสออกมาเป็นคำเหมือนกัน ช่วยตัดช่องโหว่ความมั่นคงปลอดภัยแบบ Pattern Analysis</li>
</ul>
</div>
</div>

<!-- 4. RSA Asymmetric -->
<div id="panel-rsaasym" class="w-sand-panel">
<div class="w-sand-hdr"><span>4. RSA Asymmetric (2048-bit)</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
ciphertext = cipher.encrypt(b"Hello, World!")

decipher = PKCS1_OAEP.new(RSA.import_key(private_key))
decrypted = decipher.decrypt(ciphertext)</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การสื่อสารแบบรักษาความปลอดภัยโดยใช้แนวคิดกุญแจสาธารณะ (Asymmetric Key Cryptography):</p>
<ul>
<li><strong>RSA.generate(2048)</strong>: สร้างกุญแจความยาว 2048 บิต ปลอดภัยต่อการเดารุ่นคอมพิวเตอร์ระดับสูงในปัจจุบัน</li>
<li><strong>PKCS1_OAEP</strong>: เป็นโปรโตคอลมาตรฐานที่ผสมผสาน Padding เพิ่มเติมเพื่อให้ RSA ทนต่อการเดาหรือดักถอดแบบคณิตศาสตร์</li>
<li><strong>Public/Private Key</strong>: ข้อมูลที่เข้ารหัสด้วย Public Key จะสามารถถูกไขแก้ออกได้โดย <strong>Private Key คู่อลเวงของตัวมันเอง</strong> เท่านั้น เหมาะกับงานแลกเปลี่ยนกุญแจ (Key Exchange) หรือลายเซ็นดิจิทัล</li>
</ul>
</div>
</div>

<!-- 5. SHA-256 Password Hash -->
<div id="panel-hashpass" class="w-sand-panel">
<div class="w-sand-hdr"><span>5. SHA-256 Password Hash</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import hashlib
password = "mysecretpassword"
hash_object = hashlib.sha256(password.encode())
hex_dig = hash_object.hexdigest()
print("Hash:", hex_dig)</pre>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การบันทึกจัดเก็บความปลอดภัยของรหัสผ่านผู้เรียนโดยเปลี่ยนเป็นรหัส SHA-256 Hash:</p>
<ul>
<li><strong>hashlib.sha256()</strong>: ประมวลผลลายนิ้วมือความปลอดภัยแบบทิศทางเดียว (One-way)</li>
<li><strong>hex_dig</strong>: ข้อความยาว 64 อักขระ ซึ่งเป็นค่าแฮชปลายทาง โดยแม้รหัสจะยาวต่างกันค่าแฮชก็จะเท่าเดิม การแปลงย้อนกลับแทบเป็นไปไม่ได้ ทำให้นักวิเคราะห์ล็อกอินนิยมใช้เก็บรหัสผ่านเปรียบเทียบในระบบฐานข้อมูล</li>
</ul>
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

# Block 3: Interactive Mini-Quiz 2 questions with Neon Gauge Bar
blocks_199.append({
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

<div id="mq-box-345" class="mini-quiz-box">
<!-- Question 1 -->
<div class="mq-q" data-correct="B">
<div class="mq-title"><span>Q1.</span> โหมดและเครื่องมือเข้ารหัสลับข้อมูลประเภทสมมาตร (Symmetric Encryption) ยอดนิยมข้อใดที่ใช้กุญแจเดี่ยว (Same Key) ในการไขรหัสเข้ารหัสข้อมูล?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A" onclick="updateMiniProgress(345)"><span class="mini-bullet">A</span> RSA</div>
<div class="mini-opt" data-val="B" onclick="updateMiniProgress(345)"><span class="mini-bullet">B</span> AES</div>
<div class="mini-opt" data-val="C" onclick="updateMiniProgress(345)"><span class="mini-bullet">C</span> ECC</div>
</div>
</div>

<!-- Question 2 -->
<div class="mq-q" data-correct="A">
<div class="mq-title"><span>Q2.</span> การทำแฮชชิ่งรหัสลับ (Cryptographic Hashing) มีคุณสมบัติเด่นที่ต่างจากการเข้ารหัสทั่วไปอย่างไร?</div>
<div class="mini-opts">
<div class="mini-opt" data-val="A" onclick="updateMiniProgress(345)"><span class="mini-bullet">A</span> เป็นข้อมูลทางเดียว (One-way) มีขนาดคงที่ และไม่สามารถดึงย้อนกลับมาหาคำดั้งเดิมแบบปกติได้</div>
<div class="mini-opt" data-val="B" onclick="updateMiniProgress(345)"><span class="mini-bullet">B</span> สามารถถอดรหัสออกมาได้โดยใช้คีย์ที่สั้นที่สุดผ่านฟังก์ชัน XOR modulo</div>
<div class="mini-opt" data-val="C" onclick="updateMiniProgress(345)"><span class="mini-bullet">C</span> ต้องได้รับการประมวลผลผ่าน JVM และใช้งานเฉพาะบนมือถือฝั่งแอนดรอยด์</div>
</div>
</div>

<!-- Neon Gauge Bar Progress -->
<div class="mq-progress-container">
<div id="mq-progress-bar-345" class="mq-progress-bar"></div>
<span id="mq-progress-text-345" class="mq-progress-text">Lesson Progress: 0% (ยังไม่ผ่าน)</span>
</div>

<button class="mq-btn-check" onclick="checkMiniQuiz(345)">Check Answers / ตรวจคำตอบ</button>
<div id="mq-status-345" class="mq-status-bar"></div>
</div>

<script>
// Attach click listeners to manage selection state
document.querySelectorAll('#mq-box-345 .mini-opt').forEach(opt => {
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

# ─── 3. Save and Commit the New Lesson 199 into Database ───
new_lesson = TutorialLesson(
    id=199,
    module_id=34,
    title="05. ทักษะโปรแกรมมิ่งสำหรับการเข้ารหัสลับข้อมูล (Programming Skills for Cryptography)",
    content=json.dumps(blocks_199, ensure_ascii=False),
    position=5,
    challenge_id=None
)

db.session.add(new_lesson)
db.session.commit()
print("New Lesson 199 (05. Cryptography) successfully created and committed!")
ctx.pop()
