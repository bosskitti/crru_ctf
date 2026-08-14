import json
from CTFd import create_app
from CTFd.plugins.tutorials import TutorialLesson

app = create_app()

with app.app_context():
    db = app.db
    # Query lesson 165
    lesson = db.session.query(TutorialLesson).filter_by(id=165).first()
    if lesson:
        blocks = json.loads(lesson.content)
        
        # Update Block 3 with beautiful Tux & colorful information panel
        blocks[3]['value'] = (
            "### 📌 ทำความรู้จักกับ Linux (Overview of Linux)\n\n"
            "<div style=\"background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 12px; padding: 24px; margin: 1.5rem 0; width: 100%; box-shadow: 0 4px 15px rgba(0,0,0,0.2);\">\n"
            "<div style=\"display: flex; gap: 24px; align-items: center; flex-wrap: wrap;\">\n"
            "<div style=\"flex: 1; min-width: 150px; text-align: center; background: rgba(251, 191, 36, 0.04); border: 1px solid rgba(251, 191, 36, 0.15); border-radius: 12px; padding: 20px;\">\n"
            "<i class=\"fab fa-linux\" style=\"font-size: 4.5rem; color: #fbbf24; filter: drop-shadow(0 0 10px rgba(251,191,36,0.3));\"></i>\n"
            "<div style=\"font-weight: 700; color: #fbbf24; font-size: 0.95rem; margin-top: 8px;\">Tux the Penguin</div>\n"
            "<div style=\"font-size: 0.75rem; color: #8a94a6; margin-top: 2px;\">Mascot ของระบบ Linux</div>\n"
            "</div>\n"
            "<div style=\"flex: 2; min-width: 250px; display: flex; flex-direction: column; gap: 10px; text-align: left;\">\n"
            "<div style=\"font-weight: 700; color: #00f0ff; font-size: 1.05rem; display: flex; align-items: center; gap: 8px; margin-bottom: 6px;\">\n"
            "<span>🚀</span> ข้อมูลน่ารู้เกี่ยวกับ Linux\n"
            "</div>\n"
            "<div style=\"display: flex; flex-direction: column; gap: 8px; width: 100%;\">\n"
            "<div style=\"background: rgba(251, 191, 36, 0.02); border-left: 4px solid #fbbf24; border-radius: 4px; padding: 10px 14px; display: flex; align-items: center; gap: 12px;\">\n"
            "<i class=\"fas fa-calendar-alt\" style=\"color: #fbbf24; font-size: 1.2rem; width: 20px; text-align: center;\"></i>\n"
            "<span style=\"color: #cbd5e1; font-size: 0.88rem;\">ถือกำเนิดขึ้นเมื่อวันที่ <strong style=\"color: #fbbf24;\">17 กันยายน 1991</strong> โดยนักศึกษาชาวฟินแลนด์ชื่อ <strong style=\"color: #fbbf24;\">Linus Torvalds</strong></span>\n"
            "</div>\n"
            "<div style=\"background: rgba(96, 165, 250, 0.02); border-left: 4px solid #60a5fa; border-radius: 4px; padding: 10px 14px; display: flex; align-items: center; gap: 12px;\">\n"
            "<i class=\"fas fa-code\" style=\"color: #60a5fa; font-size: 1.2rem; width: 20px; text-align: center;\"></i>\n"
            "<span style=\"color: #cbd5e1; font-size: 0.88rem;\">เขียนขึ้นมาด้วยภาษา <strong style=\"color: #60a5fa;\">C และ Assembly</strong> เป็นหลัก ทำให้มันทำงานเร็วและน้ำหนักเบามาก</span>\n"
            "</div>\n"
            "<div style=\"background: rgba(61, 220, 132, 0.02); border-left: 4px solid #3ddc84; border-radius: 4px; padding: 10px 14px; display: flex; align-items: center; gap: 12px;\">\n"
            "<i class=\"fas fa-unlock-alt\" style=\"color: #3ddc84; font-size: 1.2rem; width: 20px; text-align: center;\"></i>\n"
            "<span style=\"color: #cbd5e1; font-size: 0.88rem;\">เป็นระบบ <strong style=\"color: #3ddc84;\">Open Source (รหัสเปิด)</strong> ที่เปิดให้ผู้พัฒนาทั่วโลกร่วมกันพัฒนาได้อย่างอิสระ</span>\n"
            "</div>\n"
            "<div style=\"background: rgba(168, 85, 247, 0.02); border-left: 4px solid #a855f7; border-radius: 4px; padding: 10px 14px; display: flex; align-items: center; gap: 12px;\">\n"
            "<i class=\"fas fa-boxes\" style=\"color: #a855f7; font-size: 1.2rem; width: 20px; text-align: center;\"></i>\n"
            "<span style=\"color: #cbd5e1; font-size: 0.88rem;\">มีรุ่นย่อยๆ ยอดนิยม (Distributions) เช่น <strong style=\"color: #a855f7;\">Debian, Ubuntu, Fedora, RedHat</strong></span>\n"
            "</div>\n"
            "<div style=\"background: rgba(255, 0, 127, 0.02); border-left: 4px solid #ff007f; border-radius: 4px; padding: 10px 14px; display: flex; align-items: center; gap: 12px;\">\n"
            "<i class=\"fas fa-shield-alt\" style=\"color: #ff007f; font-size: 1.2rem; width: 20px; text-align: center;\"></i>\n"
            "<span style=\"color: #cbd5e1; font-size: 0.88rem;\"><strong style=\"color: #ff007f;\">Kali Linux</strong> คือ Distribution ยอดฮิตที่นักเจาะระบบและแฮกเกอร์ทั่วโลกนิยมใช้งานในการทดสอบระบบความปลอดภัย!</span>\n"
            "</div>\n"
            "</div>\n"
            "</div>\n"
            "</div>\n"
            "</div>"
        )
        
        lesson.content = json.dumps(blocks, ensure_ascii=False)
        db.session.query(TutorialLesson).filter_by(id=165).update({"content": lesson.content})
        db.session.commit()
        print("Lesson 165 Block 3 facts updated successfully with colorful boxes!")
    else:
        print("Error: Lesson 165 not found in database!")
