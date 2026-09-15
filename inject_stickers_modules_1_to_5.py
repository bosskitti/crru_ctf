# -*- coding: utf-8 -*-
import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

def make_sticker_box(sticker_fn, title, message, theme="cyan"):
    themes = {
        "cyan": {
            "bg": "rgba(0, 240, 255, 0.03)",
            "border": "rgba(0, 240, 255, 0.18)",
            "title_color": "#00f0ff",
            "shadow": "rgba(0, 240, 255, 0.25)"
        },
        "green": {
            "bg": "rgba(34, 197, 94, 0.03)",
            "border": "rgba(34, 197, 94, 0.2)",
            "title_color": "#4ade80",
            "shadow": "rgba(34, 197, 94, 0.25)"
        },
        "amber": {
            "bg": "rgba(251, 191, 36, 0.03)",
            "border": "rgba(251, 191, 36, 0.2)",
            "title_color": "#fbbf24",
            "shadow": "rgba(251, 191, 36, 0.25)"
        },
        "red": {
            "bg": "rgba(239, 68, 68, 0.04)",
            "border": "rgba(239, 68, 68, 0.22)",
            "title_color": "#f87171",
            "shadow": "rgba(239, 68, 68, 0.25)"
        }
    }
    t = themes.get(theme, themes["cyan"])
    
    return f"""<div style="display: flex; align-items: center; gap: 20px; background: {t['bg']}; border: 1px solid {t['border']}; border-radius: 12px; padding: 16px 20px; margin: 1.8rem 0; box-shadow: 0 4px 18px rgba(0,0,0,0.25); flex-wrap: wrap;">
<div style="text-align: center; flex-shrink: 0; margin: 0 auto;">
<img src="/themes/core/static/img/stickers/{sticker_fn}" alt="{title}" style="width: 105px; height: auto; filter: drop-shadow(0 4px 12px {t['shadow']}); transition: transform 0.25s ease;" onmouseover="this.style.transform='scale(1.06)'" onmouseout="this.style.transform='scale(1)'">
</div>
<div style="flex: 1; min-width: 250px;">
<strong style="color: {t['title_color']}; font-size: 0.98rem; display: block; margin-bottom: 5px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">{title}</strong>
<p style="margin: 0; color: #cbd5e1; font-size: 0.88rem; line-height: 1.6;">{message}</p>
</div>
</div>"""

# Mapping of lesson_id to list of sticker tips to inject
# Each tip has: position ("start", "end"), sticker_fn, title, message, theme
lesson_stickers_map = {
    # === MODULE 32: Chapter 01 ===
    160: [
        ("start", "robot_03_waving_hello.png", "🤖 ยินดีต้อนรับสู่ Chapter 1: Introduction to Cybersecurity", "สวัสดีครับผู้เรียนทุกท่าน! ในบทนี้เราจะมาปูพื้นฐานความเข้าใจเกี่ยวกับภัยคุกคามทางไซเบอร์ รูปแบบการโจมตี และหลักการคิดเพื่อการป้องกันระบบอย่างถูกต้องครับ", "green"),
        ("end", "fox_06_guide_point.png", "🦊 คำแนะนำจากจิ้งจอกสายรุก: การประเมินพื้นที่การโจมตี (Attack Surface)", "ก่อนจะเจาะระบบหรือป้องกัน เราต้องมองเห็นภาพรวมของระบบทั้งหมดให้ได้ก่อนว่ามีช่องทางใดบ้างที่คนภายนอกสามารถติดต่อเข้ามาได้ นั่นคือจุดเริ่มต้นของการเป็นนักวิเคราะห์ความปลอดภัยที่ดีครับ!", "cyan")
    ],
    161: [
        ("start", "robot_01_shield.png", "🛡️ เสาหลักความปลอดภัย (The Security Triad: CIA)", "หัวใจสำคัญของความมั่นคงปลอดภัยไซเบอร์ประกอบด้วย Confidentiality (การรักษาความลับ), Integrity (ความถูกต้องสมบูรณ์), และ Availability (ความพร้อมใช้งาน) ท่องจำ 3 เสาหลักนี้ให้ขึ้นใจเลยครับ!", "green"),
        ("end", "fox_05_thumbs_up.png", "🦊 บทบาทของ Red Team vs Blue Team", "Red Team คือผู้จำลองการโจมตีเพื่อหาจุดบกพร่อง ส่วน Blue Team คือผู้สร้างกำแพงและเฝ้าระวัง ทั้งสองฝ่ายต้องทำงานประสานกันเพื่อให้ระบบปลอดภัยสูงสุดครับ!", "cyan")
    ],
    162: [
        ("start", "fox_01_terminal.png", "🦊 ก้าวแรกสู่ Kali Linux: คลังแสงนักเจาะระบบ", "Kali Linux คือระบบปฏิบัติการที่รวบรวมเครื่องมือทดสอบเจาะระบบไว้มากที่สุดในโลก การฝึกใช้ Terminal จะช่วยให้คุณสั่งการเครื่องมือเหล่านี้ได้อย่างรวดเร็วและทรงพลังครับ", "cyan"),
        ("end", "robot_07_wrench_repair.png", "🤖 เคล็ดลับการดูแลเครื่อง Virtual Machine (VM)", "ก่อนจะเริ่มติดตั้งโปรแกรมหรือรันแล็บทดลอง แนะนำให้ทำ Snapshot เครื่อง VM ไว้เสมอ เพื่อให้สามารถย้อนกลับคืนสู่สถานะเดิมได้ทันทีหากระบบเกิดความเสียหายครับ!", "amber")
    ],
    
    # === MODULE 33: Chapter 02 ===
    164: [
        ("start", "robot_03_waving_hello.png", "🤖 ก้าวสู่โลกของระบบปฏิบัติการ Linux", "ยินดีต้อนรับสู่ Chapter 2! Linux คือกระดูกสันหลังของระบบเซิร์ฟเวอร์ คลาวด์ และอุปกรณ์ IoT ทั่วโลก การเข้าใจโครงสร้าง Kernel และ Shell จะทำให้คุณควบคุมระบบได้อย่างแท้จริงครับ", "green"),
        ("end", "fox_01_terminal.png", "🦊 ทำไมแฮกเกอร์ถึงชอบ Linux?", "เพราะ Linux เป็นระบบเปิด (Open Source) มีความยืดหยุ่นสูง และจัดการระบบผ่าน Command Line Interface (CLI) ได้อย่างมีประสิทธิภาพ ช่วยให้เขียนสคริปต์อัตโนมัติได้ง่ายดายครับ!", "cyan")
    ],
    165: [
        ("start", "fox_02_inspect_file.png", "🦊 สำรวจระบบไฟล์ Linux Filesystem Hierarchy (FHS)", "ในระบบ Linux 'Everything is a file' ทุกสิ่งทุกอย่างในระบบมองเห็นเป็นไฟล์ทั้งหมด ไม่ว่าจะเป็นฮาร์ดแวร์ ไดรฟ์ หรือโปรเซส เริ่มต้นสำรวจจากรูทไดเรกทอรี <code>/</code> กันเลยครับ!", "cyan"),
        ("end", "robot_05_guardian_stance.png", "🛡️ กฎเหล็กของไดเรกทอรีสำคัญ", "โฟลเดอร์อย่าง <code>/etc</code> เก็บไฟล์คอนฟิกทั้งระบบ ส่วน <code>/var/log</code> เก็บบันทึกเหตุการณ์ การตรวจสอบสองโฟลเดอร์นี้สม่ำเสมอจะช่วยตรวจจับผู้บุกรุกได้อย่างรวดเร็วครับ", "green")
    ],
    167: [
        ("start", "fox_08_checklist.png", "🦊 เทคนิคการใช้ Regular Expressions (Regex) ในงานสืบค้น", "Regex คืออาวุธระดับเทพในการสกัดข้อมูล! เช่น การค้นหา IP Address ด้วย pattern <code>[0-9]{1,3}\\.[0-9]{1,3}</code> หรือการดักจับอีเมลและรหัสผ่านจาก Log ขนาดยักษ์ครับ", "cyan"),
        ("end", "robot_06_warning_alert.png", "⚠️ ระวังตัวแปรสภาพแวดล้อมที่มีข้อมูลสำคัญ (Environment Variables)", "ตัวแปรอย่าง <code>$PATH</code> หรือตัวแปร API Key ใน <code>.env</code> มักตกเป็นเป้าหมายของผู้โจมตี ต้องตั้งค่าสิทธิ์การเข้าถึงให้อ่านได้เฉพาะเจ้าของเท่านั้นครับ!", "red")
    ],
    168: [
        ("start", "robot_01_shield.png", "🛡️ ระบบความปลอดภัยและสิทธิ์บน Windows", "Windows ใช้ระบบ Access Control Lists (ACLs) และ Security Identifiers (SIDs) ในการควบคุมสิทธิ์อย่างละเอียด ซึ่งแตกต่างจากระบบ rwx ของ Linux อย่างสิ้นเชิงครับ", "green"),
        ("end", "fox_04_root_key.png", "🦊 สิทธิ์ระดับสูงสุด: Administrator vs NT AUTHORITY\\SYSTEM", "บน Windows สิทธิ์สูงสุดที่แฮกเกอร์ต้องการไม่ใช่แค่ Administrator ทั่วไป แต่คือ 'SYSTEM' ซึ่งเป็นสิทธิ์ระดับแกนกลางที่สามารถควบคุมเซอร์วิสทั้งหมดได้ครับ!", "amber")
    ],
    195: [
        ("start", "fox_06_guide_point.png", "🦊 ท่องโลกคำสั่ง Windows: CMD และ PowerShell", "PowerShell มีความสามารถเชิง Object-oriented สูงมาก คำสั่งจำพวก <code>Get-Process</code> หรือ <code>Get-Service</code> ให้ข้อมูลเชิงลึกที่เหมาะต่อการทำ Threat Hunting ครับ", "cyan"),
        ("end", "robot_04_double_thumbs.png", "🤖 หมั่นตรวจสอบ Startup Programs และ Task Scheduler", "มัลแวร์ส่วนใหญ่มักสร้างความคงทน (Persistence) ผ่านการตั้งเวลาใน Windows Task Scheduler หรือ Registry Run keys การใช้คำสั่งตรวจเช็คเป็นประจำจะช่วยป้องกันได้ครับ!", "green")
    ],
    196: [
        ("start", "fox_05_thumbs_up.png", "🦊🆚🤖 Linux vs Windows: เลือกใช้ให้ถูกงาน", "ทั้ง Linux และ Windows มีจุดเด่นต่างกัน Linux เหมาะสำหรับงานเซิร์ฟเวอร์ เครือข่าย และเครื่องมือทดสอบเจาะระบบ ส่วน Windows เป็นระบบปฏิบัติการของผู้ใช้ปลายทางและองค์กรส่วนใหญ่ครับ", "cyan"),
        ("end", "robot_09_celebrate_star.png", "🎉 ยินดีด้วย! คุณจบหลักสูตรระบบปฏิบัติการ Chapter 2 เรียบร้อยแล้ว", "ตอนนี้คุณเข้าใจทั้งโครงสร้าง Linux และ Windows พร้อมสำหรับการก้าวเข้าสู่การเขียนโปรแกรมเจาะระบบใน Chapter 3 ต่อไปแล้วครับ!", "amber")
    ],

    # === MODULE 34: Chapter 03 ===
    169: [
        ("start", "fox_01_terminal.png", "🦊 เริ่มต้นเขียนโปรแกรมเพื่อความมั่นคงปลอดภัยไซเบอร์", "ภาษาโปรแกรมมิ่งคือเครื่องมือขยายขีดความสามารถของแฮกเกอร์! Python โดดเด่นด้านความรวดเร็วและไลบรารีมากมาย ส่วน C ให้ความเข้าใจการทำงานของหน่วยความจำระดับต่ำครับ", "cyan"),
        ("end", "robot_03_waving_hello.png", "🤖 แนะนำแนวทางการเรียนรู้โค้ดดิ้ง", "ไม่ต้องกลัวการเขียนโค้ดครับ เริ่มต้นจากการเขียนสคริปต์สั้นๆ ช่วยทำงานซ้ำซาก เช่น การยิงคำขอ HTTP หรือการค้นหาคำในไฟล์ แล้วค่อยๆ พัฒนาสู่เครื่องมือระดับสูงครับ!", "green")
    ],
    170: [
        ("start", "fox_08_checklist.png", "🦊 การสร้างสคริปต์อัตโนมัติ (Automation Scripts)", "งานเจาะระบบและการตรวจสอบช่องโหว่ต้องทำซ้ำๆ นับพันครั้ง การใช้ลูป (Loop) และการจัดการข้อผิดพลาด (Exception Handling) ใน Python จะช่วยประหยัดเวลาได้มหาศาลครับ", "cyan")
    ],
    198: [
        ("start", "fox_02_inspect_file.png", "🦊 ส่องข้อมูลเครือข่ายด้วย Socket Programming", "การสร้าง Socket ใน Python ช่วยให้เราสามารถเปิดการเชื่อมต่อไปยังพอร์ตเป้าหมาย ส่งข้อมูลไบนารี และสร้างตัวสแกนพอร์ต (Port Scanner) ของเราเองขึ้นมาได้จากศูนย์ครับ!", "cyan"),
        ("end", "robot_08_firewall_wall.png", "🛡️ การตั้งค่า Firewall ป้องกันการสแกนพอร์ต", "ไฟร์วอลล์สมัยใหม่สามารถตรวจจับการสแกนแบบ SYN Scan หรือ Connect Scan ได้อย่างรวดเร็ว และจะทำลายเซสชันหรือบล็อก IP ต้นทางชั่วคราวโดยอัตโนมัติครับ", "green")
    ],
    171: [
        ("start", "robot_01_shield.png", "🛡️ การพัฒนาซอฟต์แวร์อย่างปลอดภัย (SSDLC)", "ความปลอดภัยต้องเริ่มต้นตั้งแต่วันแรกที่ออกแบบซอฟต์แวร์ (Security by Design) ไม่ใช่มาแก้ไขหลังจากโปรแกรมถูกเจาะระบบแล้วครับ!", "green"),
        ("end", "fox_07_confused_error.png", "🦊 จุดที่โปรแกรมเมอร์มักพลาดบ่อยที่สุด", "การเชื่อถือข้อมูลที่ส่งมาจากฝั่งผู้ใช้ (User Input) โดยไม่มีการ Validate หรือ Sanitize คือสาเหตุอันดับ 1 ของช่องโหว่อย่าง SQL Injection และ XSS ครับ!", "red")
    ],
    199: [
        ("start", "fox_04_root_key.png", "🔑 วิทยาการรหัสลับ: กุญแจสมมาตรและอสมมาตร", "การเข้ารหัสแบบ Symmetric (เช่น AES) ใช้กุญแจดอกเดียวเข้ารหัสและถอดรหัส รวดเร็วและเหมาะกับข้อมูลขนาดใหญ่ ส่วน Asymmetric (เช่น RSA) ใช้กุญแจคู่ Public/Private Key ครับ", "amber"),
        ("end", "robot_02_chmod_755.png", "🤖 การแฮช (Hashing) ไม่ใช่การเข้ารหัส (Encryption)!", "การแฮช (เช่น SHA-256) เป็นฟังก์ชันทางเดียวที่ไม่สามารถถอดรหัสกลับได้ นิยมใช้สำหรับเก็บรหัสผ่านและตรวจสอบความถูกต้องของไฟล์ ห้ามจำสับสนกันเด็ดขาดนะครับ!", "green")
    ],
    200: [
        ("start", "fox_02_inspect_file.png", "🔍 ถอดรหัสไส้ในโปรแกรมด้วย Reverse Engineering", "การวิเคราะห์ย้อนกลับทำให้เราเห็นว่าซอฟต์แวร์ทำงานอย่างไร แปลงโค้ดไบนารีกลับมาเป็น Assembly หรือ Bytecode เพื่อค้นหาช่องโหว่หรือตรวจสอบพฤติกรรมของมัลแวร์ครับ", "cyan")
    ],
    201: [
        ("start", "fox_01_terminal.png", "🦊 การพัฒนาโค้ดเจาะระบบ (Exploit Development)", "Exploit คือโค้ดที่ถูกสร้างขึ้นเพื่อใช้ประโยชน์จากช่องโหว่ของโปรแกรม ทำให้โปรแกรมทำงานผิดเพี้ยนไปจากเดิมตามคำสั่งของผู้โจมตีครับ", "cyan"),
        ("end", "fox_03_ctf_flag.png", "🚩 ชูธงแห่งชัยชนะในการทดสอบเจาะระบบ!", "เมื่อเขียน Exploit รันผ่านและสามารถควบคุมโปรแกรมเป้าหมายได้ คุณจะได้รับสิทธิ์เข้าถึงระบบและคว้า Flag มาครองได้สำเร็จครับ!", "amber")
    ],
    172: [
        ("start", "robot_06_warning_alert.png", "⚠️ อันตรายจาก Buffer Overflow", "การเขียนโปรแกรมด้วยภาษาที่จัดการหน่วยความจำด้วยตนเองอย่าง C/C++ หากไม่มีการจำกัดขนาดข้อมูลที่รับเข้า อาจทำให้ข้อมูลล้นทับ Return Address บน Stack และเปิดช่องให้รันโค้ดอันตรายได้ครับ!", "red"),
        ("end", "fox_07_confused_error.png", "🦊 กลไกความปลอดภัยสมัยใหม่: ASLR & DEP", "ระบบปฏิบัติการปัจจุบันมีระบบสุ่มตำแหน่งหน่วยความจำ (ASLR) และป้องกันการรันโค้ดบน Stack (DEP/NX) เพื่อป้องกันไม่ให้การโจมตีสำเร็จได้ง่ายๆ ครับ", "cyan")
    ],

    # === MODULE 35: Chapter 04 ===
    173: [
        ("start", "fox_02_inspect_file.png", "🦊 ตรวจจับเป้าหมายด้วย Network Scanning & Enumeration", "ขั้นตอนแรกของการทดสอบเจาะระบบคือการสำรวจ (Reconnaissance) เครื่องมืออย่าง Nmap ช่วยให้เรารู้ว่าเป้าหมายเปิดพอร์ตอะไร รันเซอร์วิสเวอร์ชันไหน และมีระบบปฏิบัติการอะไรครับ", "cyan"),
        ("end", "robot_08_firewall_wall.png", "🛡️ การป้องกันการสแกนด้วย IDS/IPS", "ระบบตรวจจับการบุกรุก (Intrusion Detection System) จะคอยเฝ้าระวังแพ็กเก็ตที่ผิดปกติ หากพบการยิงพอร์ตสแกนอย่างรวดเร็ว ระบบจะแจ้งเตือนผู้ดูแลความปลอดภัยทันทีครับ", "green")
    ],
    174: [
        ("start", "robot_06_warning_alert.png", "⚠️ การประเมินช่องโหว่ความปลอดภัย (Vulnerability Assessment)", "การค้นหาช่องโหว่ที่มีการเปิดเผยต่อสาธารณะ (CVE) และการจัดระดับความรุนแรงตามมาตรฐาน CVSS จะช่วยให้องค์กรจัดลำดับความสำคัญในการอัปเดตแพตช์ได้ถูกต้องครับ", "amber"),
        ("end", "fox_08_checklist.png", "🦊 เช็คลิสต์ก่อนลงมือเจาะระบบ", "ต้องตรวจสอบขอบเขตงาน (Scope) สัญญาอนุญาต และเวลาในการทดสอบให้ชัดเจนเสมอ ห้ามทำการทดสอบเจาะระบบนอกขอบเขตที่ได้รับอนุญาตโดยเด็ดขาดครับ!", "cyan")
    ],
    175: [
        ("start", "fox_04_root_key.png", "⚡ ปฏิบัติการกับ Metasploit Framework", "Metasploit คือแพลตฟอร์มทดสอบเจาะระบบอันดับหนึ่งของโลก ที่รวบรวมช่องโหว่ (Exploit) และเพย์โหลด (Payload) ไว้อย่างเป็นหมวดหมู่ ช่วยให้ผู้ทดสอบทำงานได้อย่างเป็นมืออาชีพครับ", "amber"),
        ("end", "fox_03_ctf_flag.png", "🚩 พิชิตเครื่องเป้าหมายและยกระดับสิทธิ์", "เมื่อเปิดเซสชัน Meterpreter ได้สำเร็จ สเต็ปถัดไปคือการเก็บรวบรวมหลักฐานและส่งรหัส Flag เพื่อยืนยันความสำเร็จของการทดสอบเจาะระบบครับ!", "cyan")
    ],

    # === MODULE 36: Chapter 05 ===
    177: [
        ("start", "robot_01_shield.png", "🛡️ 10 อันดับภัยคุกคามเว็บแอปพลิเคชัน (OWASP Top 10)", "OWASP Top 10 คือมาตรฐานสากลที่ชี้บอกว่าช่องโหว่บนเว็บอะไรที่พบบ่อยและสร้างความเสียหายมากที่สุดในปัจจุบัน นักพัฒนาและนักเจาะระบบทุกคนต้องรู้ครับ!", "green"),
        ("end", "fox_06_guide_point.png", "🦊 การวิเคราะห์โครงสร้างคำขอ HTTP (Request & Response)", "เว็บแอปพลิเคชันสื่อสารกันผ่าน HTTP Methods (GET, POST, PUT, DELETE) การใช้เครื่องมือตรวจสอบ Headers และ Body จะช่วยให้เราพบพารามิเตอร์ที่แอบแฝงอยู่ได้ครับ", "cyan")
    ],
    178: [
        ("start", "fox_01_terminal.png", "🦊 เจาะลึกช่องโหว่เว็บขั้นสูง (Advanced Web Exploitations)", "SQL Injection, Cross-Site Scripting (XSS), และ Command Injection คือกลุ่มช่องโหว่ร้ายแรงที่สามารถทำให้ผู้โจมตีเข้าถึงฐานข้อมูลหรือสั่งรันคำสั่งบนเซิร์ฟเวอร์ได้โดยตรง!", "cyan"),
        ("end", "robot_06_warning_alert.png", "⚠️ การป้องกัน SQL Injection ที่ถูกต้อง", "วิธีป้องกัน SQLi ที่ดีที่สุดคือการใช้ **Prepared Statements / Parameterized Queries** เสมอ ห้ามนำข้อความที่ผู้ใช้กรอกมาต่อสตริงเข้ากับคำสั่ง SQL โดยตรงเด็ดขาดครับ!", "red")
    ],
    179: [
        ("start", "fox_07_confused_error.png", "🦊 ช่องโหว่ CSRF & การข้ามระบบตรวจสอบสิทธิ์", "Cross-Site Request Forgery (CSRF) หลอกให้เบราว์เซอร์ของเหยื่อที่ล็อกอินอยู่ ส่งคำสั่งอันตรายไปยังเว็บปลายทาง เช่น การโอนเงินหรือเปลี่ยนรหัสผ่านโดยที่เหยื่อไม่รู้ตัวครับ!", "amber"),
        ("end", "robot_09_celebrate_star.png", "🎉 ยินดีด้วย! คุณสำเร็จหลักสูตร Web Exploitations เรียบร้อยแล้ว", "คุณได้เรียนรู้และฝึกฝนตั้งแต่พื้นฐานเว็บแอปไปจนถึงเทคนิคการเจาะระบบขั้นสูง ขอให้นำความรู้ที่ได้ไปใช้ปกป้องระบบเว็บให้ปลอดภัยนะครับ!", "green")
    ]
}

with app.app_context():
    db = app.db
    updated_count = 0
    for lid, tips in lesson_stickers_map.items():
        lesson = db.session.query(TutorialLesson).filter_by(id=lid).first()
        if not lesson:
            continue
            
        blocks = json.loads(lesson.content) if lesson.content else []
        if not blocks:
            continue
            
        # Check if already injected
        has_stickers = any("themes/core/static/img/stickers/" in str(b.get("value", "")) for b in blocks)
        if has_stickers:
            print(f"Lesson {lid} already has stickers, skipping injection.")
            continue
            
        # Inject start tips into first markdown block or as new block
        for pos, s_fn, title, msg, theme in tips:
            box_html = make_sticker_box(s_fn, title, msg, theme)
            if pos == "start":
                # Prepend to first block
                if blocks[0]["type"] == "markdown":
                    blocks[0]["value"] = box_html + "\n\n" + blocks[0]["value"]
                else:
                    blocks.insert(0, {"type": "markdown", "value": box_html})
            elif pos == "end":
                # Append to last block
                last_idx = len(blocks) - 1
                if blocks[last_idx]["type"] == "markdown":
                    blocks[last_idx]["value"] = blocks[last_idx]["value"] + "\n\n" + box_html
                else:
                    blocks.append({"type": "markdown", "value": box_html})
                    
        lesson.content = json.dumps(blocks, ensure_ascii=False)
        db.session.commit()
        updated_count += 1
        print(f"✓ Lesson {lid} ({lesson.title[:40]}) injected with {len(tips)} stickers!")
        
    print(f"\n==========================================")
    print(f"Successfully decorated {updated_count} lessons across Modules 1 to 5 with Mascot Stickers!")
    print(f"==========================================")
