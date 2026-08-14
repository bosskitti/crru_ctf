import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()
ctx = app.app_context()
ctx.push()
db = app.db

# Query lesson 165
lesson = db.session.query(TutorialLesson).filter_by(id=165).first()
if not lesson:
    print("Lesson not found!")
    exit(1)

blocks = json.loads(lesson.content)

# Define the HTML System Architecture Stack for block 5 (flat HTML)
html_arch_stack = """<style>
.arch-stack-wrapper{margin:2.5rem 0;display:flex;flex-direction:column;align-items:center;width:100%;}
.arch-stack-container{width:100%;max-width:550px;background:rgba(15,17,26,0.4);border:1px solid rgba(255,255,255,0.05);border-radius:12px;padding:24px;box-shadow:inset 0 0 20px rgba(0,0,0,0.4);display:flex;flex-direction:column;align-items:center;gap:12px;}
.arch-layer-card{width:100%;background:rgba(255,255,255,0.02);backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:16px 20px;color:#cbd5e1;display:flex;align-items:center;gap:16px;transition:all 0.3s cubic-bezier(0.4,0,0.2,1);cursor:pointer;box-shadow:0 4px 15px rgba(0, 0, 0, 0.3);user-select:none;}
.arch-layer-card:hover{transform:translateY(-2px) scale(1.02);color:#ffffff;}
.arch-layer-icon{font-size:1.5rem;width:40px;height:40px;display:flex;align-items:center;justify-content:center;border-radius:8px;background:rgba(255,255,255,0.03);transition:all 0.3s ease;}
.arch-layer-details{display:flex;flex-direction:column;text-align:left;}
.arch-layer-title{font-weight:700;font-size:1.05rem;letter-spacing:0.02em;}
.arch-layer-subtitle{font-size:0.75rem;color:#8a94a6;text-transform:uppercase;margin-top:2px;}
.arch-layer-card.type-app{border-color:rgba(251,191,36,0.25);}
.arch-layer-card.type-app .arch-layer-icon{color:#fbbf24;background:rgba(251,191,36,0.05);}
.arch-layer-card.type-app:hover{border-color:#fbbf24;box-shadow:0 0 15px rgba(251,191,36,0.25);}
.arch-layer-card.type-shell{border-color:rgba(171,32,253,0.25);}
.arch-layer-card.type-shell .arch-layer-icon{color:#ab20fd;background:rgba(171,32,253,0.05);}
.arch-layer-card.type-shell:hover{border-color:#ab20fd;box-shadow:0 0 15px rgba(171,32,253,0.25);}
.arch-layer-card.type-kernel{border-color:rgba(255,0,127,0.3);}
.arch-layer-card.type-kernel .arch-layer-icon{color:#ff007f;background:rgba(255,0,127,0.05);}
.arch-layer-card.type-kernel:hover{border-color:#ff007f;box-shadow:0 0 18px rgba(255,0,127,0.3);}
.arch-layer-card.type-hw{border-color:rgba(0,240,255,0.25);}
.arch-layer-card.type-hw .arch-layer-icon{color:#00f0ff;background:rgba(0,240,255,0.05);}
.arch-layer-card.type-hw:hover{border-color:#00f0ff;box-shadow:0 0 15px rgba(0,240,255,0.25);}
.arch-desc-panel{margin-top:1.5rem;background:rgba(15,17,26,0.7);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:14px 20px;width:100%;max-width:550px;min-height:80px;display:flex;align-items:center;gap:16px;box-shadow:0 6px 20px rgba(0,0,0,0.4);transition:all 0.3s ease;}
.arch-desc-badge{font-weight:800;font-size:0.75rem;text-transform:uppercase;letter-spacing:0.12em;color:#8a94a6;border-right:2px solid rgba(255,255,255,0.1);padding-right:16px;height:100%;display:flex;align-items:center;white-space:nowrap;transition:color 0.3s ease;}
.arch-desc-text{font-size:0.95rem;color:#94a3b8;line-height:1.6;transition:color 0.3s ease;}
</style>
<div class="arch-stack-wrapper">
<div class="arch-stack-container">
<div class="arch-layer-card type-app" onmouseover="updateArchDesc('Applications', 'โปรแกรมประยุกต์และยูทิลิตี้ต่าง ๆ เช่น Web Browser, text editor, compiler และเครื่องมือตรวจสอบความปลอดภัยระบบ', '#fbbf24')" onmouseout="resetArchDesc()">
<div class="arch-layer-icon"><i class="fas fa-terminal"></i></div>
<div class="arch-layer-details">
<div class="arch-layer-title">Applications / Utilities</div>
<div class="arch-layer-subtitle">โปรแกรมใช้งาน / เครื่องมืออำนวยความสะดวก</div>
</div>
</div>
<div class="arch-layer-card type-shell" onmouseover="updateArchDesc('Shells', 'ตัวอินเตอร์เฟซรับคำสั่งจากผู้ใช้เพื่อส่งไปรันฟังก์ชันใน Kernel มีความสำคัญในการควบคุมระบบและเขียนสคริปต์อัตโนมัติ', '#ab20fd')" onmouseout="resetArchDesc()">
<div class="arch-layer-icon"><i class="fas fa-code"></i></div>
<div class="arch-layer-details">
<div class="arch-layer-title">Shells</div>
<div class="arch-layer-subtitle">ตัวกลางรับคำสั่ง (Bash, Zsh, GUI)</div>
</div>
</div>
<div class="arch-layer-card type-kernel" onmouseover="updateArchDesc('Kernel', 'แกนกลางของระบบปฏิบัติการ Linux ทำหน้าที่จัดการทรัพยากรเครื่องทั้งหมด เช่น CPU, Memory, Disk และการเข้าถึงอุปกรณ์เครือข่าย', '#ff007f')" onmouseout="resetArchDesc()">
<div class="arch-layer-icon"><i class="fas fa-cogs"></i></div>
<div class="arch-layer-details">
<div class="arch-layer-title">Kernel</div>
<div class="arch-layer-subtitle">ส่วนควบคุมระบบหลัก (แกนกลาง OS)</div>
</div>
</div>
<div class="arch-layer-card type-hw" onmouseover="updateArchDesc('Hardware', 'อุปกรณ์กายภาพที่เป็นตัวขับเคลื่อนการคำนวณและประมวลผลคำสั่งจริง เช่น CPU, RAM, Network Interface Card และ Hard Drive', '#00f0ff')" onmouseout="resetArchDesc()">
<div class="arch-layer-icon"><i class="fas fa-microchip"></i></div>
<div class="arch-layer-details">
<div class="arch-layer-title">Hardware</div>
<div class="arch-layer-subtitle">ฮาร์ดแวร์เครื่อง / อุปกรณ์กายภาพ</div>
</div>
</div>
</div>
<div class="arch-desc-panel" id="arch-panel-el">
<div class="arch-desc-badge" id="arch-badge-el">Arch Info</div>
<div class="arch-desc-text" id="arch-desc-el">เลื่อนเมาส์ไปชี้ที่แต่ละชั้นสถาปัตยกรรม เพื่ออ่านคำอธิบายหน้าที่</div>
</div>
</div>
<script>
function updateArchDesc(title, text, color) {
  const badge = document.getElementById('arch-badge-el');
  const desc = document.getElementById('arch-desc-el');
  const panel = document.getElementById('arch-panel-el');
  if (badge && desc) {
    badge.textContent = title;
    badge.style.color = color;
    desc.textContent = text;
    desc.style.color = '#ffffff';
    if (panel) {
      panel.style.borderColor = color;
      panel.style.boxShadow = '0 0 20px ' + color + '40, 0 6px 20px rgba(0, 0, 0, 0.4)';
    }
  }
}
function resetArchDesc() {
  const badge = document.getElementById('arch-badge-el');
  const desc = document.getElementById('arch-desc-el');
  const panel = document.getElementById('arch-panel-el');
  if (badge && desc) {
    badge.textContent = 'Arch Info';
    badge.style.color = '#8a94a6';
    desc.textContent = 'เลื่อนเมาส์ไปชี้ที่แต่ละชั้นสถาปัตยกรรม เพื่ออ่านคำอธิบายหน้าที่';
    desc.style.color = '#94a3b8';
    if (panel) {
      panel.style.borderColor = 'rgba(255, 255, 255, 0.08)';
      panel.style.boxShadow = '0 6px 20px rgba(0, 0, 0, 0.4)';
    }
  }
}
</script>"""

# Define manual replacements for directory/file tables
manual_replacements = {
    5: "### 💻 Linux System Architecture\n\nKernel is the core part of the operating system, which is responsible for all the major activities of the Linux operating system.\n\nShells are an interface which takes commands from user and executes kernel’s functions. Shells are present in different types of operating systems: command-line shells and graphical shells.\n\nApplications/Utilities are programs that are liable to do the user and specialized-level task.\n\n" + html_arch_stack,
    
    11: """### 📂 Linux Directory Structure

- The base of the Linux file system hierarchy begins at the root and everything starts with the root directory

- The path is the route that starts from the root to the destination files or directories such as `/home/wongyos/rpca/data.txt`

- These are the special directories in Linux system:

| Directory | Description |
|---|---|
| `/` | the root directory (the origin of file system hierarchy) |
| `.` | the current directory |
| `..` | the parent directory of the current directory |""",

    13: """### 📂 Linux Directory Structure (Cont)

- These are the common top-level directories associated with the root directory:

| Directory | Description |
|---|---|
| `/bin` | the binary directory contains the essential programs for all users |
| `/etc` | the etcetera directory contains the configuration files |
| `/home` | the home directory contains the default current (home) directories of users |
| `/opt` | the optional directory contains the add-on application packages and the third-party software |""",

    15: """### 📂 Linux Directory Structure (Cont)

| Directory | Description |
|---|---|
| `/tmp` | the temporary directory contains the temporary files that typically cleared when rebooting |
| `/usr` | the user directory contains the user related programs (should be shareable and read-only) |
| `/var` | the variable directory contains the log files, spool files, temporary e-mail files, etc. |""",

    17: """### 📂 Linux Directory Structure (Cont)

- These are some other top-level directories in the Linux system:

| Directory | Description |
|---|---|
| `/boot` | the boot loader directory contains all the boot-related information files and folders such as conf, grub, kernels, initrd, etc. |
| `/dev` | the device directory contains the location files of the device files such as `/dev/sda1`, `/dev/null`, etc. |
| `/lib` | the library directory contains essential libraries such as shared libraries and kernel modules |""",

    19: """### 📂 Linux Directory Structure (Cont)

| Directory | Description |
|---|---|
| `/media` | the media directory contains subdirectories where removable media devices are inserted such as USB Drive, CD-ROMs |
| `/mnt` | the mount directory contains temporary mount files and directories for mounting the file system |
| `/proc` | the process directory contains a virtual and pseudo-file system for the running processes, they are automatically generated and populated by the system |""",

    21: """### 📂 Linux Directory Structure (Cont)

| Directory | Description |
|---|---|
| `/root` | the root home directory for root user |
| `/run` | the runtime directory stores volatile runtime data or runtime variable data |
| `/sbin` | the system binary directory contains the essential system binaries and executable programs for admin |
| `/srv` | the server directory contains server-related files |
| `/sys` | the system directory contains information about devices, drivers, and some kernel features |""",

    23: """### 📂 Important Files and Directories in Linux

- Linux system stores some well-defined configuration files, binaries, man pages information files such as kernel files, device files, log files, etc.

- **Kernel file:**

| Path | Description |
|---|---|
| `/boot/vmlinux` | the kernel file |

- **Device files:**

| Path | Description |
|---|---|
| `/dev/hda` | the device file for the first IDE HDD |
| `/dev/hdc` | the pseudo-device file that outputs the garbage |""",

    25: """### 📂 Important Files and Directories in Linux (Cont)

- **System configuration files:**

| Path | Description |
|---|---|
| `/etc/bashrc` | the system defaults and aliases used by the bash shell |
| `/etc/crontab` | the shell script to run specified commands |
| `/etc/exports` | the information of file system available on the network |
| `/etc/group` | the text file to define information of security group |
| `/etc/init.d` | the service startup script |
| `/etc/hosts` | the information of IP and corresponding hostnames |
| `/etc/hosts.allow` | the list of hosts allowed to access services |""",

    27: """### 📂 Important Files and Directories in Linux (Cont)

| Path | Description |
|---|---|
| `/etc/host.deny` | the list of hosts denied to access services |
| `/etc/issue` | the pre-login message |
| `/etc/motd` | the message of the day |
| `/etc/passwd` | the username of the system, users in a shadow file |
| `/etc/printcap` | the printer information |
| `/etc/profile` | the bash shell defaults |
| `/etc/profile.d` | the scripts that are executed after login |
| `/etc/re.conf` | the configuration file for interfaces and services |
| `/etc/rc.d` | the scripts used to start, stop, and restart commands |""",

    29: """### 📂 Important Files and Directories in Linux (Cont)

| Path | Description |
|---|---|
| `/etc/rc.d/init.d` | the initialization script |
| `/etc/security` | the name of terminals where root login is possible |
| `/etc/shadow` | the encrypted user passwords |
| `/etc/skel` | the script that initiates new user home directory |
| `/etc/X11` | the configuration files for X-window (version 11) |""",

    31: """### 📂 Important Files and Directories in Linux (Cont)

- **User related files:**

| Path | Description |
|---|---|
| `/usr/bin` | the most executable files |
| `/usr/include` | the standard include files used by C program |
| `/usr/share` | the shareable text files |
| `/usr/lib` | the object files and libraries |
| `/usr/sbin` | the commands for super user and system administration |""",

    33: """### 📂 Important Files and Directories in Linux (Cont)

- **Log files:**

| Path | Description |
|---|---|
| `/var/log/httpd-access.log` | the web access information |
| `/var/log/lastlog` | the user last login information |
| `/var/log/maillog` | the e-mail usage information |
| `/var/log/messages` | the global system messages |
| `/var/log/userlog` | the user add/remove information |
| `/var/log/wtmp` | the history of login and logout information |""",

    35: """### 📂 Important Files and Directories in Linux (Cont)

- **Home files and directories under `/home/$USER`:**

| Path | Description |
|---|---|
| `~/.bashrc` | the BASH configuration file (when user logs in) |
| `~/.cache` | the cache directory stores the user cache files |
| `~/.dmrc` | the initialization file during session login |
| `~/.history` | the list of command usage history |
| `~/.local/share/Trash` | the trash directory stores the deleted files |
| `~/.profile` | the user profile file |
| `~/.zshrc` | the ZSH configuration file (when user logs in) |""",

    37: """### 📂 Important Files and Directories in Linux (Cont)

| Path | Description |
|---|---|
| `~/Desktop` | the desktop directory |
| `~/Documents` | the document directory |
| `~/Downloads` | the download directory |
| `~/Music` | the music directory |
| `~/Pictures` | the picture directory |
| `~/Public` | the directory for public file sharing |
| `~/Videos` | the video directory |"""
}

# Apply replacements
for idx, new_val in manual_replacements.items():
    blocks[idx]['value'] = new_val

# Save and Commit database
lesson.content = json.dumps(blocks, ensure_ascii=False)
db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
db.session.commit()
print("Lesson 2 visual upgrades completed successfully!")
