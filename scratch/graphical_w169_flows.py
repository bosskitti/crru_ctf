import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

l169 = db.session.query(TutorialLesson).filter_by(id=169).first()
blocks = json.loads(l169.content)

# ─── Replace Block 4 with High-Fidelity Visual Flow Diagrams for Language Processing ───
blocks[4]['value'] = """### ⚙️ Language Processing Workflows (การประมวลผลรันซอร์สโค้ด)

คลิกสลับแท็บภาษาเพื่อดูภาพกราฟิกโฟลว์แผนผังการประมวลผล (Processing Flow) ของแต่ละภาษา ตั้งแต่ซอร์สโค้ดเริ่มรันจนกระบวนการเสร็จสิ้นปลายทาง:

<style>
.w-proc-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:18px;}
.w-proc-tabs{display:flex;gap:10px;justify-content:center;}
.w-proc-tab-btn{padding:8px 14px;background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.06);border-radius:6px;font-family:'JetBrains Mono',monospace;font-size:0.8rem;color:#94a3b8;cursor:pointer;transition:all 0.15s ease;}
.w-proc-tab-btn:hover, .w-proc-tab-btn.active{border-color:#00f0ff;color:#ffffff;background:rgba(0,240,255,0.05);box-shadow:0 0 10px rgba(0,240,255,0.2);}

/* High-Fidelity Flow Box */
.w-proc-flow-box{background:rgba(15,17,26,0.45);border:1px solid rgba(255,255,255,0.06);border-radius:12px;padding:28px;min-height:380px;display:flex;flex-direction:column;align-items:center;box-sizing:border-box;}
.w-flow-title{font-size:1.05rem;font-weight:800;color:#ffffff;margin:0 0 20px;border-bottom:1px solid rgba(255,255,255,0.06);padding-bottom:10px;width:100%;text-align:center;}

/* Visual Flow Styles */
.w-flow-canvas{display:flex;align-items:center;justify-content:center;gap:16px;width:100%;margin:20px 0;flex-wrap:wrap;min-height:120px;}

/* Graphical Nodes */
.g-node{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:12px 18px;border-radius:10px;border:1px solid;font-family:'JetBrains Mono',monospace;font-size:0.75rem;font-weight:800;text-align:center;box-shadow:0 4px 15px rgba(0,0,0,0.3);position:relative;min-width:110px;box-sizing:border-box;transition:all 0.25s ease;}
.g-node .g-icon{font-size:1.8rem;margin-bottom:6px;}
.g-node .g-lbl{font-size:0.65rem;text-transform:uppercase;color:#8a94a6;margin-top:2px;font-weight:700;letter-spacing:0.04em;}

/* Theme Colors */
.g-node.theme-src{border-color:#fbbf24;background:rgba(251,191,36,0.04);color:#fbbf24;}
.g-node.theme-proc{border-color:#00f0ff;background:rgba(0,240,255,0.04);color:#00f0ff;}
.g-node.theme-interm{border-color:#ab20fd;background:rgba(171,32,253,0.04);color:#ab20fd;}
.g-node.theme-out{border-color:#3ddc84;background:rgba(61,220,132,0.04);color:#3ddc84;}

/* Pulse glow effect on hover */
.g-node:hover{transform:translateY(-2px);box-shadow:0 8px 25px rgba(255,255,255,0.1);}
.g-node.theme-src:hover{box-shadow:0 0 15px rgba(251,191,36,0.35);border-color:#fbbf24;}
.g-node.theme-proc:hover{box-shadow:0 0 15px rgba(0,240,255,0.35);border-color:#00f0ff;}
.g-node.theme-interm:hover{box-shadow:0 0 15px rgba(171,32,253,0.35);border-color:#ab20fd;}
.g-node.theme-out:hover{box-shadow:0 0 15px rgba(61,220,132,0.35);border-color:#3ddc84;}

/* Neon Connectors */
.g-arrow{display:flex;flex-direction:column;align-items:center;color:#64748b;}
.g-arrow-line{width:36px;height:2px;background:rgba(255,255,255,0.15);position:relative;}
.g-arrow-line::after{content:"";position:absolute;right:0;top:-3px;width:0;height:0;border-top:4px solid transparent;border-bottom:4px solid transparent;border-left:6px solid rgba(255,255,255,0.35);}
.g-arrow-lbl{font-size:0.6rem;margin-top:4px;font-family:'JetBrains Mono',monospace;}

.w-flow-desc-box{background:rgba(255,255,255,0.02);border:1px solid rgba(255,255,255,0.05);border-radius:8px;padding:16px;width:100%;box-sizing:border-box;}
.w-flow-desc-box p{margin:0 0 8px;font-size:0.86rem;color:#94a3b8;line-height:1.7;}
.w-flow-desc-box p:last-child{margin-bottom:0;}
.w-flow-desc-box strong{color:#fbbf24;}
</style>

<div class="w-proc-wrap">
<div class="w-proc-tabs">
<button class="w-proc-tab-btn active" onclick="showProcFlow('python', this)">Python</button>
<button class="w-proc-tab-btn" onclick="showProcFlow('java', this)">Java</button>
<button class="w-proc-tab-btn" onclick="showProcFlow('cpp', this)">C / C++</button>
<button class="w-proc-tab-btn" onclick="showProcFlow('assembly', this)">Assembly</button>
</div>

<div class="w-proc-flow-box">
<h4 id="proc-title" class="w-flow-title">Python Language Processing (ระบบแปลแบบเรียลไทม์)</h4>
<div id="proc-canvas" class="w-flow-canvas">
<!-- Node 1 -->
<div class="g-node theme-src">
<span class="g-icon">📄</span>
<span>Source Code</span>
<span class="g-lbl">Test.py</span>
</div>
<!-- Arrow -->
<div class="g-arrow">
<div class="g-arrow-line"></div>
<span class="g-arrow-lbl">Read</span>
</div>
<!-- Node 2 -->
<div class="g-node theme-proc">
<span class="g-icon">⚙️</span>
<span>Interpreter</span>
<span class="g-lbl">Line-by-line</span>
</div>
<!-- Arrow -->
<div class="g-arrow">
<div class="g-arrow-line"></div>
<span class="g-arrow-lbl">Execute</span>
</div>
<!-- Node 3 -->
<div class="g-node theme-out">
<span class="g-icon">🖥️</span>
<span>Output</span>
<span class="g-lbl">Hello World</span>
</div>
</div>
<div class="w-flow-desc-box">
<p id="proc-desc">ระบบการประมวลผลของ Python ใช้แนวคิด **Interpretation** โดยตัวโปรแกรมจะส่งซอร์สโค้ดเข้าสู่ <strong>Interpreter</strong> เพื่อแปลและทำงานทีละบรรทัดจากบนลงล่างทันทีโดยไม่ต้องทำการแปลงโค้ดทั้งหมดเป็นไฟล์อื่นล่วงหน้า ช่วยให้นักวิเคราะห์สคริปต์แก้ไขและทดสอบสคริปต์เจาะระบบได้ยืดหยุ่นและรวดเร็ว</p>
</div>
</div>
</div>

<script>
const procFlowData = {
  'python': {
    title: 'Python Language Processing (ระบบแปลแบบเรียลไทม์)',
    canvas: `
      <div class="g-node theme-src">
        <span class="g-icon">📄</span>
        <span>Source Code</span>
        <span class="g-lbl">Test.py</span>
      </div>
      <div class="g-arrow">
        <div class="g-arrow-line"></div>
        <span class="g-arrow-lbl">Read</span>
      </div>
      <div class="g-node theme-proc">
        <span class="g-icon">⚙️</span>
        <span>Interpreter</span>
        <span class="g-lbl">Line-by-line</span>
      </div>
      <div class="g-arrow">
        <div class="g-arrow-line"></div>
        <span class="g-arrow-lbl">Execute</span>
      </div>
      <div class="g-node theme-out">
        <span class="g-icon">🖥️</span>
        <span>Output</span>
        <span class="g-lbl">Hello World</span>
      </div>
    `,
    desc: 'ระบบการประมวลผลของ Python ใช้แนวคิด **Interpretation** โดยตัวโปรแกรมจะส่งซอร์สโค้ดเข้าสู่ <strong>Interpreter</strong> เพื่อแปลและทำงานทีละบรรทัดจากบนลงล่างทันทีโดยไม่ต้องทำการแปลงโค้ดทั้งหมดเป็นไฟล์อื่นล่วงหน้า ช่วยให้นักวิเคราะห์สคริปต์แก้ไขและทดสอบสคริปต์เจาะระบบได้ยืดหยุ่นและรวดเร็ว'
  },
  'java': {
    title: 'Java Language Processing (ระบบรันข้ามแพลตฟอร์มด้วย JVM)',
    canvas: `
      <div class="g-node theme-src">
        <span class="g-icon">📄</span>
        <span>Source Code</span>
        <span class="g-lbl">Test.java</span>
      </div>
      <div class="g-arrow">
        <div class="g-arrow-line"></div>
        <span class="g-arrow-lbl">javac</span>
      </div>
      <div class="g-node theme-proc">
        <span class="g-icon">📦</span>
        <span>Compiler</span>
        <span class="g-lbl">Code Translate</span>
      </div>
      <div class="g-arrow">
        <div class="g-arrow-line"></div>
        <span class="g-arrow-lbl">Write</span>
      </div>
      <div class="g-node theme-interm">
        <span class="g-icon">🪙</span>
        <span>Byte Code</span>
        <span class="g-lbl">Test.class</span>
      </div>
      <div class="g-arrow">
        <div class="g-arrow-line"></div>
        <span class="g-arrow-lbl">Load</span>
      </div>
      <div class="g-node theme-proc">
        <span class="g-icon">🌐</span>
        <span>JVM</span>
        <span class="g-lbl">Virtual Machine</span>
      </div>
      <div class="g-arrow">
        <div class="g-arrow-line"></div>
        <span class="g-arrow-lbl">Run</span>
      </div>
      <div class="g-node theme-out">
        <span class="g-icon">🖥️</span>
        <span>Output</span>
        <span class="g-lbl">Hello World</span>
      </div>
    `,
    desc: 'ระบบของ Java ใช้แนวคิด **Hybrid Compilation**: ขั้นแรกจะทำการคอมไพล์โค้ดดั้งเดิมด้วยคำสั่ง <code>javac</code> ให้กลายเป็นไฟล์ระดับกลางที่เรียกว่า <strong>Byte Code (.class)</strong> ซึ่งไม่ใช่ภาษาเครื่องของซีพียูโดยตรง แต่เป็นภาษาของ <strong>Java Virtual Machine (JVM)</strong> ทำให้เมื่อนำไฟล์ Byte Code นี้ไปเปิดรันบนเครื่องใดๆ ที่ติดตั้ง JVM (เช่น Android OS หรือเซิร์ฟเวอร์องค์กร) จะทำงานได้เหมือนกันทันที'
  },
  'cpp': {
    title: 'C / C++ Language Processing (ระบบแปลภาษาเครื่องตรงประสิทธิภาพสูง)',
    canvas: `
      <div class="g-node theme-src">
        <span class="g-icon">📄</span>
        <span>Source Code</span>
        <span class="g-lbl">Test.c / .cpp</span>
      </div>
      <div class="g-arrow">
        <div class="g-arrow-line"></div>
        <span class="g-arrow-lbl">Compile</span>
      </div>
      <div class="g-node theme-proc">
        <span class="g-icon">📦</span>
        <span>Compiler</span>
        <span class="g-lbl">gcc / g++</span>
      </div>
      <div class="g-arrow">
        <div class="g-arrow-line"></div>
        <span class="g-arrow-lbl">Output</span>
      </div>
      <div class="g-node theme-interm">
        <span class="g-icon">⚙️</span>
        <span>Object Code</span>
        <span class="g-lbl">Test.o / .obj</span>
      </div>
      <div class="g-arrow">
        <div class="g-arrow-line"></div>
        <span class="g-arrow-lbl">Link</span>
      </div>
      <div class="g-node theme-proc">
        <span class="g-icon">🔗</span>
        <span>Linker</span>
        <span class="g-lbl">Include Libs</span>
      </div>
      <div class="g-arrow">
        <div class="g-arrow-line"></div>
        <span class="g-arrow-lbl">Generate</span>
      </div>
      <div class="g-node theme-out">
        <span class="g-icon">🚀</span>
        <span>Executable</span>
        <span class="g-lbl">a.out / .exe</span>
      </div>
    `,
    desc: 'ระบบของ C/C++ ใช้การ **Compile สู่ภาษาเครื่องโดยตรง (Native Compilation)**: ซอร์สโค้ดทั้งหมดจะถูกส่งให้คอมไพเลอร์ (เช่น <code>gcc</code> หรือ <code>g++</code>) แปลงรวดเดียวให้กลายเป็นไฟล์ <strong>Object Code</strong> จากนั้นโปรแกรม <strong>Linker</strong> จะทำการนำไลบรารีระบบและ Object Code มาผูกรวมกันกลายเป็นไฟล์รันระบบที่สมบูรณ์ (เช่น <code>a.out</code> ใน Linux หรือ <code>.exe</code> ใน Windows) ส่งรันบนดิสก์และแรมได้อย่างรวดเร็วถึงขีดสุด'
  },
  'assembly': {
    title: 'Assembly Language Processing (ระบบแปลชุดคำสั่งซีพียูระดับล่าง)',
    canvas: `
      <div class="g-node theme-src">
        <span class="g-icon">📄</span>
        <span>Source Code</span>
        <span class="g-lbl">Test.asm</span>
      </div>
      <div class="g-arrow">
        <div class="g-arrow-line"></div>
        <span class="g-arrow-lbl">nasm</span>
      </div>
      <div class="g-node theme-proc">
        <span class="g-icon">🛠️</span>
        <span>Assembler</span>
        <span class="g-lbl">Translate CPU</span>
      </div>
      <div class="g-arrow">
        <div class="g-arrow-line"></div>
        <span class="g-arrow-lbl">Output</span>
      </div>
      <div class="g-node theme-interm">
        <span class="g-icon">⚙️</span>
        <span>Object Code</span>
        <span class="g-lbl">Test.o</span>
      </div>
      <div class="g-arrow">
        <div class="g-arrow-line"></div>
        <span class="g-arrow-lbl">Link (ld)</span>
      </div>
      <div class="g-node theme-proc">
        <span class="g-icon">🔗</span>
        <span>Linker</span>
        <span class="g-lbl">ld tool</span>
      </div>
      <div class="g-arrow">
        <div class="g-arrow-line"></div>
        <span class="g-arrow-lbl">Output</span>
      </div>
      <div class="g-node theme-out">
        <span class="g-icon">🚀</span>
        <span>Executable</span>
        <span class="g-lbl">a.out</span>
      </div>
    `,
    desc: 'ระบบของ Assembly ทำการแปลตัวย่อคำสั่งระดับต่ำ (เช่น <code>mov</code>, <code>push</code>) ขึ้นตรงกับชิปสถาปัตยกรรมซีพียู ผ่านโปรแกรมแปลภาษาเครื่องระดับต่ำที่เรียกว่า <strong>Assembler (เช่น nasm)</strong> จนได้ Object Code แล้วส่งให้ตัวเชื่อมโยงระบบ <strong>Linker (ld)</strong> ทำการชี้ตำแหน่งเซกเตอร์ความปลอดภัยและจุดเริ่มต้น <code>_start</code> ของโปรแกรม ออกมาเป็นไฟล์รันสิทธิ์ระบบตรงโดยไม่มีระบบครอบแทรกแซง'
  }
};

function showProcFlow(key, element) {
  const buttons = document.querySelectorAll('.w-proc-tab-btn');
  buttons.forEach(b => b.classList.remove('active'));
  element.classList.add('active');

  const data = procFlowData[key];
  if (!data) return;

  document.getElementById('proc-title').textContent = data.title;
  document.getElementById('proc-canvas').innerHTML = data.canvas;
  document.getElementById('proc-desc').innerHTML = data.desc;
}
</script>"""

l169.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=169).update({"content": l169.content})
db.session.commit()
print("High-Fidelity Graphical processing flow diagrams updated in Block 4 of Lesson 169!")
ctx.pop()
