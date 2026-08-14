import json
import re
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

# Query lesson 164
lesson = db.session.query(TutorialLesson).filter_by(id=164).first()
if not lesson:
    print("Lesson not found!")
    exit(1)

blocks = json.loads(lesson.content)

# We know the diagram is in block index 1
block = blocks[1]
val = block['value']

# Define the HTML/CSS replacement content
html_replacement = """
<style>
/* Scoped styles for the computer system component hierarchy diagram */
.sys-tree-wrapper {
  margin: 2.5rem 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}

.sys-tree-scroll {
  width: 100%;
  overflow-x: auto;
  padding: 24px 12px;
  background: rgba(15, 17, 26, 0.4);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.05);
  box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.4);
  scrollbar-width: thin;
  scrollbar-color: rgba(0, 240, 255, 0.3) rgba(15, 17, 26, 0.5);
}

.sys-tree-scroll::-webkit-scrollbar {
  height: 6px;
}
.sys-tree-scroll::-webkit-scrollbar-track {
  background: rgba(15, 17, 26, 0.5);
  border-radius: 3px;
}
.sys-tree-scroll::-webkit-scrollbar-thumb {
  background: rgba(0, 240, 255, 0.3);
  border-radius: 3px;
}
.sys-tree-scroll::-webkit-scrollbar-thumb:hover {
  background: rgba(0, 240, 255, 0.6);
}

.sys-tree-container {
  min-width: 820px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.sys-tree-row {
  display: flex;
  justify-content: center;
  position: relative;
  width: 100%;
}

/* Vertical line helper */
.sys-line-v {
  width: 2px;
  height: 24px;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.25) 100%);
}

/* Branches row style */
.sys-branches-row {
  display: flex;
  justify-content: space-between;
  width: 100%;
  position: relative;
  padding-top: 24px;
}

/* Level 2 connection line */
.sys-branches-row.level-2::before {
  content: '';
  position: absolute;
  top: 0;
  left: 16.666%;
  right: 16.666%;
  height: 2px;
  background: rgba(255, 255, 255, 0.15);
}

/* Level 3 connection line for Hardware */
.sys-sub-branches.level-3-hw::before {
  content: '';
  position: absolute;
  top: 0;
  left: 16.666%;
  right: 16.666%;
  height: 2px;
  background: rgba(255, 255, 255, 0.15);
}

/* Level 3 connection line for Software */
.sys-sub-branches.level-3-sw::before {
  content: '';
  position: absolute;
  top: 0;
  left: 25%;
  right: 25%;
  height: 2px;
  background: rgba(255, 255, 255, 0.15);
}

.sys-branch-col {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex: 1;
  position: relative;
}

/* Vertical connection line above branch columns */
.sys-branch-col::before {
  content: '';
  position: absolute;
  top: -24px;
  left: 50%;
  width: 2px;
  height: 24px;
  background: rgba(255, 255, 255, 0.15);
  transform: translateX(-50%);
}

/* Sub-branches layout */
.sys-sub-branches {
  display: flex;
  justify-content: center;
  gap: 16px;
  width: 100%;
  position: relative;
  padding-top: 24px;
}

.sys-sub-branch-col {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex: 1;
  position: relative;
}

.sys-sub-branch-col::before {
  content: '';
  position: absolute;
  top: -24px;
  left: 50%;
  width: 2px;
  height: 24px;
  background: rgba(255, 255, 255, 0.15);
  transform: translateX(-50%);
}

/* Cards / Nodes Base */
.sys-node {
  background: rgba(255, 255, 255, 0.02);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 10px;
  padding: 12px 20px;
  color: #cbd5e1;
  text-align: center;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  user-select: none;
}

.sys-node:hover {
  transform: translateY(-4px);
  color: #ffffff;
}

.sys-node .node-icon {
  font-size: 1.3rem;
  margin-bottom: 6px;
  transition: all 0.3s ease;
}

.sys-node .node-title {
  font-weight: 600;
  font-size: 0.95rem;
  letter-spacing: 0.03em;
}

/* Node Variants */
/* Root: Computer */
.sys-node.type-computer {
  background: linear-gradient(135deg, rgba(0, 240, 255, 0.1) 0%, rgba(171, 32, 253, 0.1) 100%);
  border: 1.5px solid rgba(0, 240, 255, 0.3);
  box-shadow: 0 0 20px rgba(0, 240, 255, 0.08);
  width: 160px;
}
.sys-node.type-computer .node-icon {
  color: #00f0ff;
  text-shadow: 0 0 10px rgba(0, 240, 255, 0.5);
}
.sys-node.type-computer:hover {
  border-color: #00f0ff;
  box-shadow: 0 0 25px rgba(0, 240, 255, 0.3), 0 0 35px rgba(171, 32, 253, 0.2);
}

/* Hardware */
.sys-node.type-hardware {
  border: 1px solid rgba(0, 240, 255, 0.25);
  background: rgba(0, 240, 255, 0.03);
  width: 140px;
}
.sys-node.type-hardware .node-icon {
  color: #00f0ff;
}
.sys-node.type-hardware:hover {
  border-color: #00f0ff;
  box-shadow: 0 0 15px rgba(0, 240, 255, 0.25);
  background: rgba(0, 240, 255, 0.08);
}

/* Software */
.sys-node.type-software {
  border: 1px solid rgba(171, 32, 253, 0.25);
  background: rgba(171, 32, 253, 0.03);
  width: 140px;
}
.sys-node.type-software .node-icon {
  color: #ab20fd;
}
.sys-node.type-software:hover {
  border-color: #ab20fd;
  box-shadow: 0 0 15px rgba(171, 32, 253, 0.25);
  background: rgba(171, 32, 253, 0.08);
}

/* Peopleware */
.sys-node.type-peopleware {
  border: 1px solid rgba(251, 191, 36, 0.25);
  background: rgba(251, 191, 36, 0.03);
  width: 140px;
}
.sys-node.type-peopleware .node-icon {
  color: #fbbf24;
}
.sys-node.type-peopleware:hover {
  border-color: #fbbf24;
  box-shadow: 0 0 15px rgba(251, 191, 36, 0.25);
  background: rgba(251, 191, 36, 0.08);
}

/* Sub-nodes: CPU, Memory, I/O */
.sys-node.type-sub {
  padding: 8px 14px;
  min-width: 90px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.06);
}
.sys-node.type-sub:hover {
  background: rgba(255, 255, 255, 0.06);
  border-color: rgba(255, 255, 255, 0.2);
}

.sys-node.type-sub.sub-hw {
  border-color: rgba(0, 240, 255, 0.15);
}
.sys-node.type-sub.sub-hw:hover {
  border-color: rgba(0, 240, 255, 0.6);
  box-shadow: 0 0 10px rgba(0, 240, 255, 0.15);
}

.sys-node.type-sub.sub-sw-sys {
  border-color: rgba(171, 32, 253, 0.25);
}
.sys-node.type-sub.sub-sw-sys:hover {
  border-color: #ab20fd;
  box-shadow: 0 0 10px rgba(171, 32, 253, 0.2);
}

.sys-node.type-sub.sub-sw-app {
  border-color: rgba(244, 114, 182, 0.25);
}
.sys-node.type-sub.sub-sw-app:hover {
  border-color: #f472b6;
  box-shadow: 0 0 10px rgba(244, 114, 182, 0.2);
}

/* Operating System node */
.sys-node.type-os {
  border: 1px solid rgba(255, 0, 127, 0.3);
  background: rgba(255, 0, 127, 0.03);
  width: 155px;
}
.sys-node.type-os .node-icon {
  color: #ff007f;
}
.sys-node.type-os:hover {
  border-color: #ff007f;
  box-shadow: 0 0 18px rgba(255, 0, 127, 0.3);
  background: rgba(255, 0, 127, 0.08);
}

/* Info Panel */
.sys-desc-panel {
  margin-top: 1.5rem;
  background: rgba(15, 17, 26, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 10px;
  padding: 14px 20px;
  width: 100%;
  max-width: 820px;
  min-height: 80px;
  display: flex;
  align-items: center;
  gap: 16px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
}

.sys-desc-badge {
  font-weight: 800;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: #8a94a6;
  border-right: 2px solid rgba(255, 255, 255, 0.1);
  padding-right: 16px;
  height: 100%;
  display: flex;
  align-items: center;
  white-space: nowrap;
  transition: color 0.3s ease;
}

.sys-desc-text {
  font-size: 0.95rem;
  color: #94a3b8;
  line-height: 1.6;
  transition: color 0.3s ease;
}

/* Scroll indicator on mobile */
.sys-scroll-hint {
  display: none;
  font-size: 0.75rem;
  color: #8a94a6;
  margin-bottom: 8px;
  align-items: center;
  gap: 6px;
}

@media (max-width: 850px) {
  .sys-scroll-hint {
    display: flex;
  }
}
</style>

<div class="sys-tree-wrapper">
  <div class="sys-scroll-hint">
    <i class="fas fa-arrows-alt-h"></i> <span>เลื่อนในแนวนอนเพื่อดูโครงสร้างระบบทั้งหมด</span>
  </div>
  
  <div class="sys-tree-scroll">
    <div class="sys-tree-container">
      <!-- Level 1: Root -->
      <div class="sys-tree-row">
        <div class="sys-node type-computer" 
             onmouseover="updateSysDesc('Computer', 'ระบบคอมพิวเตอร์โดยรวม ประกอบไปด้วยส่วนสำคัญ 3 ส่วนคือ Hardware, Software และ Peopleware ทำงานร่วมกันเพื่อประมวลผลข้อมูล', '#00f0ff')" 
             onmouseout="resetSysDesc()">
          <div class="node-icon"><i class="fas fa-desktop"></i></div>
          <div class="node-title">Computer</div>
        </div>
      </div>
      
      <!-- Connect 1 -> 2 -->
      <div class="sys-line-v"></div>
      
      <!-- Level 2: Main Branches -->
      <div class="sys-branches-row level-2">
        
        <!-- Column 1: Hardware -->
        <div class="sys-branch-col">
          <div class="sys-node type-hardware" 
               onmouseover="updateSysDesc('Hardware', 'อุปกรณ์ทางกายภาพหรือชิ้นส่วนคอมพิวเตอร์ที่สัมผัสได้ เช่น เมนบอร์ด อุปกรณ์ประมวลผล หน่วยความจำ และอุปกรณ์เชื่อมต่อภายนอก', '#00f0ff')" 
               onmouseout="resetSysDesc()">
            <div class="node-icon"><i class="fas fa-microchip"></i></div>
            <div class="node-title">Hardware</div>
          </div>
          
          <!-- Connect 2 -> 3 for Hardware -->
          <div class="sys-line-v"></div>
          
          <div class="sys-sub-branches level-3-hw">
            <div class="sys-sub-branch-col">
              <div class="sys-node type-sub sub-hw" 
                   onmouseover="updateSysDesc('CPU (Central Processing Unit)', 'หน่วยประมวลผลกลาง ทำหน้าที่เสมือนสมองของคอมพิวเตอร์ในการคำนวณและประมวลผลคำสั่งต่าง ๆ', '#00f0ff')" 
                   onmouseout="resetSysDesc()">
                <div class="node-title">CPU</div>
              </div>
            </div>
            
            <div class="sys-sub-branch-col">
              <div class="sys-node type-sub sub-hw" 
                   onmouseover="updateSysDesc('Memory (หน่วยความจำ)', 'อุปกรณ์สำหรับเก็บข้อมูลและโปรแกรมคำสั่ง แบ่งเป็นหน่วยความจำหลักชั่วคราว (RAM) และหน่วยความจำถาวร (ROM)', '#00f0ff')" 
                   onmouseout="resetSysDesc()">
                <div class="node-title">Memory</div>
              </div>
            </div>
            
            <div class="sys-sub-branch-col">
              <div class="sys-node type-sub sub-hw" 
                   onmouseover="updateSysDesc('I/O (Input/Output)', 'อุปกรณ์นำข้อมูลเข้าและแสดงผล เช่น คีย์บอร์ด เมาส์ หน้าจอ เพื่อให้คอมพิวเตอร์สื่อสารกับผู้ใช้งานได้', '#00f0ff')" 
                   onmouseout="resetSysDesc()">
                <div class="node-title">I/O</div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Column 2: Software -->
        <div class="sys-branch-col">
          <div class="sys-node type-software" 
               onmouseover="updateSysDesc('Software', 'ชุดคำสั่งหรือชุดคำสั่งโปรแกรมที่ควบคุมการทำงานของฮาร์ดแวร์ แบ่งเป็นระบบปฏิบัติการควบคุมระบบ และแอปพลิเคชันใช้งานเฉพาะด้าน', '#ab20fd')" 
               onmouseout="resetSysDesc()">
            <div class="node-icon"><i class="fas fa-code"></i></div>
            <div class="node-title">Software</div>
          </div>
          
          <!-- Connect 2 -> 3 for Software -->
          <div class="sys-line-v"></div>
          
          <div class="sys-sub-branches level-3-sw">
            <!-- System SW -->
            <div class="sys-sub-branch-col">
              <div class="sys-node type-sub sub-sw-sys" 
                   onmouseover="updateSysDesc('System Software', 'ซอฟต์แวร์ระบบที่ควบคุมการทำงานพื้นฐานของเครื่องและประสานงานอุปกรณ์ เช่น ระบบปฏิบัติการ (OS) ไดรเวอร์อุปกรณ์ และยูทิลิตี้ต่าง ๆ', '#ab20fd')" 
                   onmouseout="resetSysDesc()">
                <div class="node-title">System SW</div>
              </div>
              
              <!-- Connect 3 -> 4 for System SW to OS -->
              <div class="sys-line-v"></div>
              
              <div class="sys-node type-os" 
                   onmouseover="updateSysDesc('Operating System (OS)', 'ระบบปฏิบัติการที่จัดการฮาร์ดแวร์ จัดสรรทรัพยากร และเป็นตัวกลางให้บริการแก่แอปพลิเคชัน เช่น Windows, Linux, macOS', '#ff007f')" 
                   onmouseout="resetSysDesc()">
                <div class="node-icon"><i class="fas fa-cogs"></i></div>
                <div class="node-title">Operating System</div>
              </div>
            </div>
            
            <!-- Application SW -->
            <div class="sys-sub-branch-col">
              <div class="sys-node type-sub sub-sw-app" 
                   onmouseover="updateSysDesc('Application Software', 'ซอฟต์แวร์ประยุกต์หรือโปรแกรมที่พัฒนาขึ้นมาเพื่อการใช้งานเฉพาะทาง เช่น เว็บเบราว์เซอร์ โปรแกรมพิมพ์งาน เกม เครื่องมือแฮกต่าง ๆ', '#f472b6')" 
                   onmouseout="resetSysDesc()">
                <div class="node-title">Application SW</div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Column 3: Peopleware -->
        <div class="sys-branch-col">
          <div class="sys-node type-peopleware" 
               onmouseover="updateSysDesc('Peopleware', 'บุคลากรที่เกี่ยวข้องกับการทำงานของคอมพิวเตอร์ ตั้งแต่ผู้พัฒนาซอฟต์แวร์ นักวิเคราะห์ระบบ ผู้ดูแลความปลอดภัย ไปจนถึงผู้ใช้งานทั่วไป', '#fbbf24')" 
               onmouseout="resetSysDesc()">
            <div class="node-icon"><i class="fas fa-users"></i></div>
            <div class="node-title">Peopleware</div>
          </div>
        </div>
        
      </div>
    </div>
  </div>
  
  <!-- Info Display Panel -->
  <div class="sys-desc-panel">
    <div class="sys-desc-badge" id="sys-badge-el">System Info</div>
    <div class="sys-desc-text" id="sys-desc-el">เลื่อนเมาส์ไปชี้ที่แต่ละส่วนประกอบของระบบคอมพิวเตอร์ เพื่ออ่านรายละเอียดเพิ่มเติม</div>
  </div>
</div>

<script>
function updateSysDesc(title, text, color) {
  const badge = document.getElementById('sys-badge-el');
  const desc = document.getElementById('sys-desc-el');
  if (badge && desc) {
    badge.textContent = title;
    badge.style.color = color;
    desc.textContent = text;
    desc.style.color = '#ffffff';
  }
}

function resetSysDesc() {
  const badge = document.getElementById('sys-badge-el');
  const desc = document.getElementById('sys-desc-el');
  if (badge && desc) {
    badge.textContent = 'System Info';
    badge.style.color = '#8a94a6';
    desc.textContent = 'เลื่อนเมาส์ไปชี้ที่แต่ละส่วนประกอบของระบบคอมพิวเตอร์ เพื่ออ่านรายละเอียดเพิ่มเติม';
    desc.style.color = '#94a3b8';
  }
}
</script>
"""

# Regex search for the ```text ... ``` ASCII diagram block and replace it.
# We will match the code block precisely.
pattern = r"```text\n\s*┌──────────────┐\n.*?\n\s*└──────────────────┘\n```"
modified_val = re.sub(pattern, html_replacement, val, flags=re.DOTALL)

if modified_val == val:
    # If the exact pattern above didn't match (due to minor character differences), let's use a simpler match
    print("Warning: Precise regex pattern did not match. Trying fallback regex pattern...")
    fallback_pattern = r"```text\n\s*┌──────────────┐\n.*?Operating System.*?\n```"
    modified_val = re.sub(fallback_pattern, html_replacement, val, flags=re.DOTALL)

if modified_val == val:
    print("Error: Could not locate the ASCII diagram in the lesson content!")
    exit(1)

block['value'] = modified_val
blocks[1] = block

lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.commit()
print("Lesson diagram updated successfully!")
