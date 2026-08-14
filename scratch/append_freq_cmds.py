import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

lesson = db.session.query(TutorialLesson).filter_by(id=166).first()
if not lesson:
    print("Lesson 166 not found!")
    exit(1)

blocks = json.loads(lesson.content)

# ─── Block 10: Separator + Heading ───
b_sep3 = """---

### ⚡ Frequently Used Commands"""

# ─── Block 11: Command Reference Grid ───
b_cmd_grid = """#### 📚 รายการคำสั่งที่ใช้บ่อยใน Linux / Unix

<style>
.freq-wrap{width:100%;max-width:1050px;margin:2rem auto;}
.freq-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;}
@media(max-width:700px){.freq-grid{grid-template-columns:repeat(2,1fr);}}
@media(max-width:460px){.freq-grid{grid-template-columns:1fr;}}
.freq-card{background:rgba(15,17,26,0.5);border:1px solid rgba(255,255,255,0.05);border-radius:10px;padding:14px 16px;transition:all 0.2s ease;cursor:default;}
.freq-card:hover{background:rgba(255,255,255,0.03);border-color:rgba(0,240,255,0.15);transform:translateY(-2px);box-shadow:0 6px 20px rgba(0,0,0,0.3);}
.freq-card:hover .freq-cmd{color:#00f0ff;text-shadow:0 0 8px rgba(0,240,255,0.4);}
.freq-cmd{font-family:'JetBrains Mono',monospace;font-size:0.95rem;font-weight:800;color:#e2e8f0;margin-bottom:4px;transition:all 0.2s;}
.freq-en{font-size:0.74rem;color:#64748b;line-height:1.4;margin-bottom:4px;font-style:italic;}
.freq-th{font-size:0.8rem;color:#94a3b8;line-height:1.45;}
</style>

<div class="freq-wrap">
<div class="freq-grid">
<div class="freq-card"><div class="freq-cmd">cal</div><div class="freq-en">report the calendar</div><div class="freq-th">แสดงปฏิทินของเดือนหรือปีที่ระบุ</div></div>
<div class="freq-card"><div class="freq-cmd">clear</div><div class="freq-en">clear the screen</div><div class="freq-th">ลบข้อความทั้งหมดออกจากหน้าจอ Terminal</div></div>
<div class="freq-card"><div class="freq-cmd">date</div><div class="freq-en">report the current date and time</div><div class="freq-th">แสดงวันที่และเวลาปัจจุบันของระบบ</div></div>
<div class="freq-card"><div class="freq-cmd">df</div><div class="freq-en">report disk free and used summary</div><div class="freq-th">แสดงสรุปพื้นที่ดิสก์ที่ใช้และว่างอยู่</div></div>
<div class="freq-card"><div class="freq-cmd">du</div><div class="freq-en">report disk space in use</div><div class="freq-th">แสดงขนาดพื้นที่ดิสก์ที่ไฟล์หรือ directory ใช้อยู่</div></div>
<div class="freq-card"><div class="freq-cmd">exit</div><div class="freq-en">leave the shell</div><div class="freq-th">ออกจาก Shell หรือปิด Terminal session</div></div>
<div class="freq-card"><div class="freq-cmd">finger</div><div class="freq-en">list users on local network</div><div class="freq-th">แสดงรายชื่อผู้ใช้ที่ login อยู่บนเครือข่ายท้องถิ่น</div></div>
<div class="freq-card"><div class="freq-cmd">groups</div><div class="freq-en">show groups user belongs to</div><div class="freq-th">แสดงกลุ่มที่ผู้ใช้ปัจจุบันเป็นสมาชิกอยู่</div></div>
<div class="freq-card"><div class="freq-cmd">head</div><div class="freq-en">show the first 10 lines of a file</div><div class="freq-th">แสดง 10 บรรทัดแรกของไฟล์ (กำหนดจำนวนเองได้)</div></div>
<div class="freq-card"><div class="freq-cmd">history</div><div class="freq-en">show history of previous commands</div><div class="freq-th">แสดงประวัติคำสั่งที่เคยพิมพ์ใน Shell</div></div>
<div class="freq-card"><div class="freq-cmd">hostname</div><div class="freq-en">display the hostname</div><div class="freq-th">แสดงชื่อ hostname ของเครื่องปัจจุบัน</div></div>
<div class="freq-card"><div class="freq-cmd">id</div><div class="freq-en">show user and group names/IDs</div><div class="freq-th">แสดง UID, GID และกลุ่มของผู้ใช้ปัจจุบัน</div></div>
<div class="freq-card"><div class="freq-cmd">ifconfig</div><div class="freq-en">show and set IP addresses</div><div class="freq-th">แสดงและตั้งค่า IP address ของ network interface</div></div>
<div class="freq-card"><div class="freq-cmd">kill</div><div class="freq-en">send a signal to kill process (pid)</div><div class="freq-th">ส่ง signal เพื่อหยุด process ตาม PID ที่ระบุ</div></div>
<div class="freq-card"><div class="freq-cmd">last</div><div class="freq-en">show history of system logins</div><div class="freq-th">แสดงประวัติการ login เข้าสู่ระบบที่ผ่านมา</div></div>
<div class="freq-card"><div class="freq-cmd">less</div><div class="freq-en">improved pagination for text files</div><div class="freq-th">แสดงเนื้อหาไฟล์ทีละหน้า เลื่อนได้ทั้งขึ้น-ลง (ดีกว่า more)</div></div>
<div class="freq-card"><div class="freq-cmd">logout</div><div class="freq-en">leave the system</div><div class="freq-th">ออกจากระบบและปิด session ของผู้ใช้</div></div>
<div class="freq-card"><div class="freq-cmd">man</div><div class="freq-en">display the user manual of any command</div><div class="freq-th">แสดงคู่มือการใช้งานอย่างละเอียดของคำสั่งที่ระบุ</div></div>
<div class="freq-card"><div class="freq-cmd">nl</div><div class="freq-en">read file and write to standard output</div><div class="freq-th">อ่านไฟล์และแสดงพร้อมหมายเลขบรรทัดกำกับ</div></div>
<div class="freq-card"><div class="freq-cmd">passwd</div><div class="freq-en">set or change your password</div><div class="freq-th">ตั้งค่าหรือเปลี่ยน password ของผู้ใช้</div></div>
<div class="freq-card"><div class="freq-cmd">poweroff</div><div class="freq-en">shut down or power off the system</div><div class="freq-th">ปิดระบบปฏิบัติการและตัดไฟเครื่อง</div></div>
<div class="freq-card"><div class="freq-cmd">ps</div><div class="freq-en">show status of active processes</div><div class="freq-th">แสดงรายการ process ที่กำลังทำงานอยู่</div></div>
<div class="freq-card"><div class="freq-cmd">reboot</div><div class="freq-en">ungraceful reboot (without stopping services)</div><div class="freq-th">รีสตาร์ทเครื่องทันทีโดยไม่หยุด OS services</div></div>
<div class="freq-card"><div class="freq-cmd">rmdir</div><div class="freq-en">remove empty directories</div><div class="freq-th">ลบ directory ที่ว่างเปล่า (ถ้ามีไฟล์ให้ใช้ rm -R)</div></div>
<div class="freq-card"><div class="freq-cmd">set</div><div class="freq-en">display environment variables</div><div class="freq-th">แสดง Environment Variable ทั้งหมดของระบบ</div></div>
<div class="freq-card"><div class="freq-cmd">su</div><div class="freq-en">switch user</div><div class="freq-th">สลับไปใช้งานในฐานะ user อื่น (default: root)</div></div>
<div class="freq-card"><div class="freq-cmd">sudo</div><div class="freq-en">run commands with superuser privileges</div><div class="freq-th">รันคำสั่งด้วยสิทธิ์ root โดยไม่ต้อง login เป็น root</div></div>
<div class="freq-card"><div class="freq-cmd">tail</div><div class="freq-en">show the last 10 lines of a file</div><div class="freq-th">แสดง 10 บรรทัดสุดท้ายของไฟล์ (กำหนดจำนวนเองได้)</div></div>
<div class="freq-card"><div class="freq-cmd">talk</div><div class="freq-en">send multi-line message to another user</div><div class="freq-th">ส่งข้อความแบบหลายบรรทัดแบบ real-time ไปยัง user อื่น</div></div>
<div class="freq-card"><div class="freq-cmd">tar</div><div class="freq-en">create archive, add or extract files</div><div class="freq-th">บีบอัดหรือแตกไฟล์ archive (.tar, .tar.gz)</div></div>
<div class="freq-card"><div class="freq-cmd">top</div><div class="freq-en">show tasks and system status (live)</div><div class="freq-th">แสดง process และสถานะระบบแบบ real-time (กด q เพื่อออก)</div></div>
<div class="freq-card"><div class="freq-cmd">uname</div><div class="freq-en">display the name of current machine/OS</div><div class="freq-th">แสดงชื่อและข้อมูลของระบบปฏิบัติการปัจจุบัน</div></div>
<div class="freq-card"><div class="freq-cmd">uptime</div><div class="freq-en">find out how long system has been up</div><div class="freq-th">แสดงระยะเวลาที่ระบบทำงานต่อเนื่องมาโดยไม่ restart</div></div>
<div class="freq-card"><div class="freq-cmd">w</div><div class="freq-en">display system load and logged-in users</div><div class="freq-th">แสดงผู้ใช้ที่ login อยู่และสิ่งที่แต่ละคนกำลังทำ</div></div>
<div class="freq-card"><div class="freq-cmd">who</div><div class="freq-en">find out who is logged into the system</div><div class="freq-th">แสดงรายชื่อผู้ใช้ที่กำลัง login อยู่ในระบบขณะนี้</div></div>
<div class="freq-card"><div class="freq-cmd">whoami</div><div class="freq-en">report current username</div><div class="freq-th">แสดงชื่อ user ที่กำลังใช้งาน Terminal อยู่ขณะนี้</div></div>
<div class="freq-card"><div class="freq-cmd">write</div><div class="freq-en">send one-line message to another user</div><div class="freq-th">ส่งข้อความบรรทัดเดียวไปยัง user อื่นที่ login อยู่</div></div>
</div>
</div>"""

# ─── Block 12: Terminal Examples ───
b_term_examples = """#### 💻 ตัวอย่าง Output ของคำสั่งที่ใช้บ่อย

<style>
.ex-wrap{width:100%;max-width:1050px;margin:2rem auto;display:flex;flex-direction:column;gap:0;}
.ex-terminal{background:#070910;border-radius:10px;overflow:hidden;border:1px solid rgba(255,255,255,0.08);box-shadow:0 8px 32px rgba(0,0,0,0.5);}
.ex-titlebar{background:rgba(28,30,44,0.98);padding:9px 16px;display:flex;align-items:center;gap:8px;border-bottom:1px solid rgba(255,255,255,0.05);}
.ex-dot{width:11px;height:11px;border-radius:50%;}
.ex-dot.r{background:#ff5f57;}.ex-dot.y{background:#ffbd2e;}.ex-dot.g{background:#28c840;}
.ex-title{flex:1;text-align:center;font-size:0.75rem;color:#8a94a6;font-family:'JetBrains Mono',monospace;letter-spacing:0.06em;}
.ex-body{padding:20px 24px 24px;font-family:'JetBrains Mono','Courier New',monospace;font-size:0.83rem;line-height:1.75;}
.ex-prompt{color:#00f0ff;}.ex-cmd{color:#ffffff;font-weight:600;}
.ex-out{color:#94a3b8;white-space:pre;}
.ex-out-g{color:#3ddc84;white-space:pre;}
.ex-out-y{color:#fbbf24;white-space:pre;}
.ex-out-c{color:#00f0ff;white-space:pre;}
.ex-out-dim{color:#475569;white-space:pre;}
.ex-divider{border:none;border-top:1px solid rgba(255,255,255,0.05);margin:12px 0;}
</style>

<div class="ex-wrap">
<div class="ex-terminal">
<div class="ex-titlebar">
<span class="ex-dot r"></span><span class="ex-dot y"></span><span class="ex-dot g"></span>
<span class="ex-title">bash — root@kali:~</span>
</div>
<div class="ex-body">
<div><span class="ex-prompt">└─#</span> <span class="ex-cmd">cal</span></div>
<div class="ex-out-y">   February 2023      
Su Mo Tu We Th Fr Sa  
          1  2  3  4  
 5  6  7  8  9 10 11  
12 13 14 15 16 17 18  
19 20 21 22 23 24 25  
26 27 28              </div>
<hr class="ex-divider"/>
<div><span class="ex-prompt">└─#</span> <span class="ex-cmd">date</span></div>
<div class="ex-out-g">Wed Feb  8 11:01:41 PM EST 2023</div>
<hr class="ex-divider"/>
<div><span class="ex-prompt">└─#</span> <span class="ex-cmd">finger</span></div>
<div class="ex-out">Login     Name       Tty      Idle  Login Time   Office     Office Phone
root      root       tty7       32  Feb  8 22:30 (:0)</div>
<hr class="ex-divider"/>
<div><span class="ex-prompt">└─#</span> <span class="ex-cmd">df</span></div>
<div class="ex-out">Filesystem     1K-blocks     Used Available Use% Mounted on
udev              968484        0    968484   0% /dev
tmpfs             202160     1176    200984   1% /run
/dev/sda1       81000912 13730336  63109964  18% /
tmpfs            1010784       84   1010700   1% /dev/shm
tmpfs               5120        0      5120   0% /run/lock
tmpfs             202156       68    202088   1% /run/user/0</div>
<hr class="ex-divider"/>
<div><span class="ex-prompt">└─#</span> <span class="ex-cmd">groups</span></div>
<div class="ex-out-c">root</div>
<div><span class="ex-prompt">└─#</span> <span class="ex-cmd">hostname</span></div>
<div class="ex-out-c">kali</div>
<div><span class="ex-prompt">└─#</span> <span class="ex-cmd">id</span></div>
<div class="ex-out-g">uid=0(root) gid=0(root) groups=0(root)</div>
<hr class="ex-divider"/>
<div><span class="ex-prompt">└─#</span> <span class="ex-cmd">ps -l</span></div>
<div class="ex-out">F S   UID     PID    PPID  C PRI  NI ADDR SZ WCHAN  TTY          TIME CMD
0 S     0    1216    1213  0  80   0 -  3390 -      pts/0    00:00:02 zsh
4 R     0    1665    1216  0  80   0 -  2439 -      pts/0    00:00:00 ps</div>
<hr class="ex-divider"/>
<div><span class="ex-prompt">└─#</span> <span class="ex-cmd">uname</span></div>
<div class="ex-out-c">Linux</div>
<div><span class="ex-prompt">└─#</span> <span class="ex-cmd">uptime</span></div>
<div class="ex-out"> 23:10:51 up 40 min,  1 user,  load average: <span style="color:#fbbf24">0.12, 0.11, 0.09</span></div>
<hr class="ex-divider"/>
<div><span class="ex-prompt">└─#</span> <span class="ex-cmd">w</span></div>
<div class="ex-out"> 23:10:59 up 40 min,  1 user,  load average: 0.10, 0.10, 0.09
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
root     tty7     :0               22:30   40:26  24.44s 24.44s /usr/lib/xorg/Xorg :0</div>
<hr class="ex-divider"/>
<div><span class="ex-prompt">└─#</span> <span class="ex-cmd">who</span></div>
<div class="ex-out-g">root     tty7         2023-02-08 22:30 (:0)</div>
<div><span class="ex-prompt">└─#</span> <span class="ex-cmd">whoami</span></div>
<div class="ex-out-g">root</div>
<hr class="ex-divider"/>
<div><span class="ex-prompt">└─#</span> <span class="ex-cmd">last</span></div>
<div class="ex-out">root     tty7         :0               Wed Feb  8 22:30   <span style="color:#3ddc84">still logged in</span>
reboot   system boot  5.16.0-kali7-amd Wed Feb  8 22:30   <span style="color:#3ddc84">still running</span>
root     tty7         :0               Sat Oct 29 01:09 - 14:23 (1+13:14)
reboot   system boot  5.16.0-kali7-amd Sat Oct 29 01:08 - 14:23 (1+13:14)
root     tty7         :0               Fri Oct 14 22:28 - 08:37  (10:09)
reboot   system boot  5.16.0-kali7-amd Fri Oct 14 22:26 - 08:37  (10:11)
root     tty7         :0               Mon Sep 26 10:31 - 01:31 (10+15:00)
reboot   system boot  5.16.0-kali7-amd Mon Sep 26 10:30 - 01:31 (10+15:01)</div>
</div>
</div>
</div>"""

# Append new blocks
new_blocks = [
    {"type": "markdown", "value": b_sep3},
    {"type": "markdown", "value": b_cmd_grid},
    {"type": "markdown", "value": b_term_examples},
]
blocks.extend(new_blocks)

lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=166).update({"content": lesson.content})
db.session.commit()

print(f"Frequently Used Commands appended! Total blocks: {len(blocks)}")
for i, b in enumerate(blocks[-4:], start=len(blocks)-4):
    print(f"  Block {i}: {len(b['value'])} chars")
