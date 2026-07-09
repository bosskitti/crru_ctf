import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l199 = db.session.query(TutorialLesson).filter_by(id=199).first()
blocks = json.loads(l199.content)

# ─── Upgrade Block 2 of Lesson 199 to include Live Flow Terminal Simulation ───
blocks[2]['value'] = """### 💻 Cryptography Coding Sandbox (วิเคราะห์เจาะลึก 5 ตัวอย่างโค้ดรหัสลับ)

คลิกหัวข้อด้านซ้ายมือเพื่อตรวจสอบตัวอย่างโค้ดระบบวิทยาการรหัสลับ และ **กดปุ่มรันจำลองการทำงานจริง (Run Simulation)** เพื่อดูผลลัพธ์ผ่านเทอร์มินัลระบบ:

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
.w-sand-panel.active{display:block !important;}

.w-sand-hdr{font-size:0.95rem;font-weight:800;color:#ffffff;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:10px;margin-bottom:14px;display:flex;justify-content:between;align-items:center;}
.w-sand-hdr span.tag{font-size:0.65rem;padding:2px 8px;border-radius:4px;background:rgba(0,240,255,0.08);border:1px solid rgba(0,240,255,0.2);color:#00f0ff;font-family:'JetBrains Mono',monospace;}
.w-sand-code{font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#00f0ff;white-space:pre-wrap;margin:0 0 12px;background:rgba(0,0,0,0.2);padding:14px;border-radius:8px;border:1px solid rgba(255,255,255,0.02);}

/* Terminal box */
.w-sand-term-container{position:relative;background:#02040a;border:1px solid rgba(255,255,255,0.06);border-radius:8px;margin-bottom:16px;box-shadow:inset 0 2px 8px rgba(0,0,0,0.9);overflow:hidden;}
.w-sand-term-bar{background:rgba(255,255,255,0.03);padding:6px 12px;border-bottom:1px solid rgba(255,255,255,0.05);display:flex;justify-content:space-between;align-items:center;}
.w-sand-term-title{font-size:0.65rem;color:#64748b;font-weight:800;letter-spacing:0.06em;font-family:'JetBrains Mono',monospace;}
.w-sand-term-btn{background:rgba(0,240,255,0.1);border:1px solid rgba(0,240,255,0.3);border-radius:4px;color:#00f0ff;font-size:0.68rem;padding:3px 8px;cursor:pointer;font-family:'JetBrains Mono',monospace;font-weight:700;transition:all 0.15s ease;display:flex;align-items:center;gap:4px;}
.w-sand-term-btn:hover{background:#00f0ff;color:#02040a;box-shadow:0 0 8px rgba(0,240,255,0.4);}
.w-sand-term{font-family:'JetBrains Mono',monospace;font-size:0.76rem;color:#a7f3d0;padding:12px 16px;white-space:pre-wrap;min-height:90px;}
.w-sand-term span.prompt{color:#3ddc84;}
.w-sand-term span.cmd{color:#ffffff;font-weight:bold;}

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
<button id="nav-item-logicflag" class="w-nav-item active" onclick="showSandboxItem('logicflag', this)">1. Logic Flag (C++)</button>
<button id="nav-item-xorflag" class="w-nav-item" onclick="showSandboxItem('xorflag', this)">2. XOR Flag Helper (Python)</button>
<button id="nav-item-aesmode" class="w-nav-item" onclick="showSandboxItem('aesmode', this)">3. AES CBC Symmetric</button>
<button id="nav-item-rsaasym" class="w-nav-item" onclick="showSandboxItem('rsaasym', this)">4. RSA Asymmetric (2048-bit)</button>
<button id="nav-item-hashpass" class="w-nav-item" onclick="showSandboxItem('hashpass', this)">5. SHA-256 Password Hash</button>
</div>

<!-- Panel details right side -->
<div class="w-sandbox-panels">

<!-- 1. Logic Flag (C++) -->
<div id="panel-logicflag" class="w-sand-panel">
<div class="w-sand-hdr"><span>1. Logic Flag Example</span> <span class="tag">C++ Code</span></div>
<pre class="w-sand-code" style="color:#3ddc84;">#include &lt;iostream&gt;
#include &lt;string&gt;
using namespace std;
int main() {
    unsigned int flag[] = { 754, 708, 734, ... };
    unsigned int key, code, i;
    cout &lt;&lt; "Key: ";
    cin &gt;&gt; key;
    for(i = 0; i &lt; 53; i++) {
        code = flag[i] ^ key;
        cout &lt;&lt; (char) code;
    }
    cout &lt;&lt; endl;
    return 0;
}</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startCryptoSim('logicflag')">▶ Run Simulation</button>
</div>
<div id="term-logicflag" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation ด้านขวาบนเพื่อจำลองการเรียกใช้งาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>โปรแกรมภาษา C++ ในการถอดรหัส Flag ออกจากอาร์เรย์ตัวเลขด้วยตัวดำเนินการบิต XOR:</p>
<ul>
<li><strong>XOR Operator (^)</strong>: การบวกลบข้อมูลแบบบิตผันกลับได้ หากไขคีย์ถูกต้องจะได้รับรหัสอักขระดั้งเดิม</li>
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
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startCryptoSim('xorflag')">▶ Run Simulation</button>
</div>
<div id="term-xorflag" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation ด้านขวาบนเพื่อจำลองการเรียกใช้งาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>ฟังก์ชัน Python สำหรับการทำ Repeating XOR ปิดท้ายด้วยการเข้ารหัสข้อความเลขฐานสิบหก:</p>
<ul>
<li><strong>i%len(key)</strong>: การขยายขนาดกุญแจให้ยาวเท่ากับข้อความแบบคาบซ้ำ</li>
</ul>
</div>
</div>

<!-- 3. AES CBC -->
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
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startCryptoSim('aesmode')">▶ Run Simulation</button>
</div>
<div id="term-aesmode" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation ด้านขวาบนเพื่อจำลองการเรียกใช้งาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>สคริปต์ความปลอดภัยแบบเข้ารหัสลับ AES ในโหมด CBC (Cipher Block Chaining):</p>
<ul>
<li><strong>IV (Initialization Vector)</strong>: ตัวสุ่มตั้งค่าเริ่มบล็อกแรกเพื่อรับมือกับภัยคุกคามสืบแกะรอยประโยค</li>
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
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startCryptoSim('rsaasym')">▶ Run Simulation</button>
</div>
<div id="term-rsaasym" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation ด้านขวาบนเพื่อจำลองการเรียกใช้งาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การเข้ารหัสลับด้วยคู่กุญแจคู่ขนานเพื่อใช้แลกเปลี่ยนกุญแจหรือส่งข้อมูลลับ:</p>
<ul>
<li><strong>KeyPair RSA 2048</strong>: กุญแจสาธารณะ (Public Key) สำหรับเข้ารหัส และกุญแจส่วนตัว (Private Key) สำหรับถอดรหัส</li>
</ul>
</div>
</div>

<!-- 5. SHA-256 Hash -->
<div id="panel-hashpass" class="w-sand-panel">
<div class="w-sand-hdr"><span>5. SHA-256 Password Hash</span> <span class="tag">Python</span></div>
<pre class="w-sand-code">import hashlib
password = "mysecretpassword"
hash_object = hashlib.sha256(password.encode())
hex_dig = hash_object.hexdigest()
print("Hash:", hex_dig)</pre>
<div class="w-sand-term-container">
<div class="w-sand-term-bar">
<span class="w-sand-term-title">🐚 Terminal Console</span>
<button class="w-sand-term-btn" onclick="startCryptoSim('hashpass')">▶ Run Simulation</button>
</div>
<div id="term-hashpass" class="w-sand-term"><span class="prompt">kali@kali:~/Desktop$</span> [กดปุ่ม Run Simulation ด้านขวาบนเพื่อจำลองการเรียกใช้งาน]</div>
</div>
<div class="w-sand-expl">
<h5>🔒 Security & Code Analysis</h5>
<p>การบันทึกจัดเก็บความปลอดภัยของรหัสผ่านผู้เรียนโดยเปลี่ยนเป็นรหัส SHA-256 Hash:</p>
<ul>
<li><strong>One-way Hashing</strong>: การแปลงลายนิ้วมือข้อมูลทางเดียวที่ไม่สามารถแปลงย้อนกลับหาข้อความจริงได้</li>
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

// Auto render
setTimeout(() => {
  const activeBtn = document.querySelector('.w-sandbox-nav .w-nav-item.active');
  if (activeBtn) { activeBtn.click(); }
}, 100);

// Crypto Terminal Simulation
window.startCryptoSim = function(itemKey) {
  const term = document.getElementById('term-' + itemKey);
  if (!term) return;

  term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">Processing cryptographic keys...</span>\\n[.] Loading algorithms\\n[.] Compiling/Executing...';

  setTimeout(() => {
    if (itemKey === 'logicflag') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">g++ logic_flag.cpp && ./a.out</span>\\nKey: 712\\n<span style="color:#3ddc84; font-weight:bold;">flag{xor_logic_gate_passed}</span>';
    } else if (itemKey === 'xorflag') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 xor_helper.py</span>\\nHex Encoded Output: 0b153e091a09536e0c4b6b4f09175b1f6c0a025b536d5f43';
    } else if (itemKey === 'aesmode') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 aes_cbc.py</span>\\nCiphertext: b\\'\\\\x82\\\\xf9\\\\x02\\\\x8e\\\\x1a\\\\xb0\\\\x94\\\\xef\\\\x1c\\\\x19\\\\xd3\\\\xee\\\\xa1\\\\xcc\\\\xfa\\\\x8e\\'\\n<span style="color:#3ddc84;">Decrypted: Hello, World!</span>';
    } else if (itemKey === 'rsaasym') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 rsa_test.py</span>\\n[+] Generating RSA 2048 keys...\\nCiphertext (Hex): 9e32fc2bda40391bde4c399a...\\n<span style="color:#3ddc84;">Decrypted with Private Key: Hello, World!</span>';
    } else if (itemKey === 'hashpass') {
      term.innerHTML = '<span class="prompt">kali@kali:~/Desktop$</span> <span class="cmd">python3 sha256_hash.py</span>\\nHash Digest (Hex): <span style="color:#fbbf24;">8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918</span>';
    }
  }, 1000);
}
</script>"""

l199.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=199).update({"content": l199.content})
db.session.commit()
print("Lesson 199 Live Terminal Simulation successfully integrated!")
ctx.pop()
