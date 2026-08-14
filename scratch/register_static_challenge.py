import sys
from CTFd import create_app
from CTFd.models import Challenges, Flags, db

app = create_app()

description_html = """<div class="p-4 mb-3" style="background: rgba(12, 15, 29, 0.85); border-left: 4px solid #3ddc84; border-radius: 4px; font-family: 'Outfit', sans-serif;">
    <h3 style="color: #3ddc84; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem;">
        Lab: Web Source Code Inspection (F12)
    </h3>
    <p style="color: #c8d1e0; font-size: 1.05rem; line-height: 1.6;">
        นักพัฒนามักทิ้งข้อมูลสำคัญหรือรหัสผ่านจำลองไว้ในหน้าซอร์สโค้ด (Source Code) หรือคอมเมนต์ของเว็บไซต์โดยไม่ได้ตั้งใจ
    </p>
    <div class="mt-4 p-3" style="background: rgba(61, 220, 132, 0.08); border: 1px dashed rgba(61, 220, 132, 0.3); border-radius: 4px;">
        <h5 style="color: #3ddc84; font-weight: 700; margin-bottom: 0.5rem; text-transform: uppercase;">
            Objective:
        </h5>
        <p class="mb-0" style="color: #fff; font-size: 0.95rem; line-height: 1.5;">
            ให้ทำการตรวจสอบซอร์สโค้ด (Inspect Page / View Source) ของหน้าบทเรียนย่อย <strong>Lesson 177 (Web Application Security & OWASP)</strong> เพื่อค้นหาความลับที่นักพัฒนาทิ้งไว้ ทำการถอดรหัส (Decode) ข้อมูลนั้นเพื่อดึง Flag ที่แท้จริงมาส่งในแล็บนี้
        </p>
    </div>
</div>"""

with app.app_context():
    chall = Challenges.query.filter_by(name="Web Source Code Inspection (F12)").first()
    if not chall:
        # Create standard static challenge
        chall = Challenges(
            name="Web Source Code Inspection (F12)",
            description=description_html,
            category="Tutorial",
            type="standard",
            state="visible",
            value=100
        )
        db.session.add(chall)
        db.session.commit()
        print(f"SUCCESS: Challenge registered with ID {chall.id}")
        
        # Create static flag
        flag_val = "flag{f12_view_source_page_obfuscation_successful_98a4c3ad2e9}"
        flag_obj = Flags(
            challenge_id=chall.id,
            type="static",
            content=flag_val,
            data=""
        )
        db.session.add(flag_obj)
        db.session.commit()
        print(f"SUCCESS: Created static flag: {flag_val}")
    else:
        chall.description = description_html
        chall.category = "Tutorial"
        db.session.commit()
        print(f"SUCCESS: Challenge updated with ID {chall.id}")
        
        # Check flag
        flag_obj = Flags.query.filter_by(challenge_id=chall.id).first()
        if flag_obj:
            flag_obj.content = "flag{f12_view_source_page_obfuscation_successful_98a4c3ad2e9}"
            db.session.commit()
            print("SUCCESS: Updated flag in database.")
