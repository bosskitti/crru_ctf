"""
Step 1: Create table + migrate answers from HTML to DB + strip data-correct
"""
import sys, re, json
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app
app = create_app()

with app.app_context():
    from CTFd.models import db
    from CTFd.plugins.tutorials import TutorialLesson

    # Create table
    try:
        db.engine.execute("""
            CREATE TABLE IF NOT EXISTS tutorial_quiz_answer (
                id          INT AUTO_INCREMENT PRIMARY KEY,
                lesson_id   INT NOT NULL,
                q_index     INT NOT NULL,
                correct_val VARCHAR(10) NOT NULL,
                INDEX idx_lesson (lesson_id)
            )
        """)
        print("Table created/verified")
    except Exception as e:
        print(f"Table: {e}")

    lessons = TutorialLesson.query.all()
    lesson_count = 0
    answer_count = 0

    for lesson in lessons:
        if not lesson.content:
            continue
        raw = lesson.content
        if not raw.strip().startswith('['):
            continue
        try:
            cells = json.loads(raw)
        except Exception:
            continue

        changed = False
        for cell in cells:
            if cell.get('type') != 'markdown':
                continue
            val = cell.get('value', '')
            if 'data-correct' not in val:
                continue

            # Extract answers in order
            answers = re.findall(r'data-correct=["\'](\w+)["\']', val)
            if not answers:
                continue

            # Delete old, insert new
            db.engine.execute(
                "DELETE FROM tutorial_quiz_answer WHERE lesson_id=%s", (lesson.id,)
            )
            for idx, ans in enumerate(answers):
                db.engine.execute(
                    "INSERT INTO tutorial_quiz_answer (lesson_id, q_index, correct_val) VALUES (%s,%s,%s)",
                    (lesson.id, idx, ans)
                )
                answer_count += 1

            # Remove data-correct from HTML
            cell['value'] = re.sub(r'\s*data-correct=["\'][^"\']*["\']', '', val)
            changed = True
            print(f"  Lesson {lesson.id}: {len(answers)} answers stored, data-correct removed")

        if changed:
            lesson.content = json.dumps(cells, ensure_ascii=False)
            lesson_count += 1

    db.session.commit()
    print(f"\nDone: {answer_count} answers from {lesson_count} lessons migrated to DB")
