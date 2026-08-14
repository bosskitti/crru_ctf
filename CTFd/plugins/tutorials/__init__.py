import os
import re
from flask import Blueprint, render_template, request, redirect, url_for, abort, jsonify, make_response, send_file
from CTFd.models import db, Challenges, Users
from CTFd.utils.decorators import admins_only, authed_only
from CTFd.utils.user import is_admin, get_current_user
from CTFd.plugins import register_admin_plugin_menu_bar, register_user_page_menu_bar
from CTFd.utils.config.pages import build_markdown
from CTFd.utils import markdown
from CTFd.utils.uploads import upload_file

# Define database models
class TutorialModule(db.Model):
    __tablename__ = "tutorial_module"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(255))
    position = db.Column(db.Integer, default=0)
    hidden = db.Column(db.Boolean, default=False)
    level = db.Column(db.String(50), default="Basic")
    level_color = db.Column(db.String(50), default="#00f0ff")
    
    # Pre-test and Post-test configurations
    pre_test_lesson_id = db.Column(db.Integer, nullable=True)
    post_test_lesson_id = db.Column(db.Integer, nullable=True)
    
    # Cascade deletes to lessons
    lessons = db.relationship(
        "TutorialLesson",
        backref=db.backref("module", lazy="joined"),
        lazy="dynamic",
        cascade="all, delete-orphan",
        order_by="TutorialLesson.position.asc(), TutorialLesson.id.asc()"
    )

class TutorialLesson(db.Model):
    __tablename__ = "tutorial_lesson"
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey("tutorial_module.id", ondelete="CASCADE"), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text) # Markdown content
    challenge_id = db.Column(db.Integer, db.ForeignKey("challenges.id", ondelete="SET NULL"), nullable=True)
    position = db.Column(db.Integer, default=0)

class TutorialProgress(db.Model):
    __tablename__ = "tutorial_progress"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey("tutorial_lesson.id", ondelete="CASCADE"), nullable=False)
    type = db.Column(db.String(50)) # "quiz" or "question"
    item_key = db.Column(db.String(255)) # e.g. the question hash, or "quick_quiz"
    solved = db.Column(db.Boolean, default=False)
    score = db.Column(db.Integer, nullable=True)   # คะแนนที่ทำได้ (สำหรับ quiz)
    total = db.Column(db.Integer, nullable=True)   # คะแนนเต็ม (สำหรับ quiz)
    created_at = db.Column(db.DateTime, default=db.func.now())
    
    user = db.relationship("Users", backref=db.backref("tutorial_progress", lazy="dynamic"))
    lesson = db.relationship("TutorialLesson", backref=db.backref("progress_records", lazy="dynamic"))

class TutorialQuizAnswer(db.Model):
    """Stores correct answers for mini-quizzes server-side (never sent to browser)."""
    __tablename__ = "tutorial_quiz_answer"
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey("tutorial_lesson.id", ondelete="CASCADE"), nullable=False)
    q_index = db.Column(db.Integer, nullable=False)   # 0-based question index
    correct_val = db.Column(db.String(10), nullable=False)

    __table_args__ = (db.Index("idx_quiz_ans_lesson", "lesson_id"),)

# Create blueprint
tutorials_bp = Blueprint(
    "tutorials",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/tutorials/static",
    url_prefix=""
)

# --- USER ROUTES ---

@tutorials_bp.route("/tutorials")
@authed_only
def list_modules():
    if is_admin():
        modules = TutorialModule.query.order_by(TutorialModule.position.asc(), TutorialModule.id.asc()).all()
    else:
        modules = TutorialModule.query.filter_by(hidden=False).order_by(TutorialModule.position.asc(), TutorialModule.id.asc()).all()
    return render_template("plugins/tutorials/templates/modules.html", modules=modules)

@tutorials_bp.route("/tutorials/<int:module_id>")
@authed_only
def view_module_redirect(module_id):
    if is_admin():
        module = TutorialModule.query.filter_by(id=module_id).first_or_404()
    else:
        module = TutorialModule.query.filter_by(id=module_id, hidden=False).first_or_404()
        
    lessons = module.lessons.order_by(TutorialLesson.position.asc()).all()
    if not lessons:
        return redirect(url_for('tutorials.view_lesson', module_id=module_id, lesson_position=1))
        
    user = get_current_user()
    target_pos = 1
    
    # Robust check for first uncompleted lesson
    from CTFd.models import Solves
    for idx, l in enumerate(lessons):
        # 1. Parse content
        N_questions = 0
        question_hashes = []
        has_quiz = False
        challenge_ids = []
        if l.challenge_id:
            challenge_ids.append(l.challenge_id)
        if l.content:
            try:
                import json
                content_stripped = l.content.strip()
                if content_stripped.startswith("[") and content_stripped.endswith("]"):
                    cells = json.loads(content_stripped)
                    for cell in cells:
                        c_type = cell.get("type")
                        if c_type == "question":
                            N_questions += 1
                            if cell.get("hash"):
                                question_hashes.append(cell["hash"])
                        elif c_type == "challenge":
                            c_id = cell.get("challenge_id")
                            if c_id:
                                challenge_ids.append(int(c_id))
                        elif c_type == "markdown":
                            val = cell.get("value", "")
                            if any(kw in val for kw in ["mini-quiz-box", "w-quiz-option", "Lesson Quick Quiz"]):
                                has_quiz = True
                else:
                    if any(kw in l.content for kw in ["mini-quiz-box", "w-quiz-option", "Lesson Quick Quiz"]):
                        has_quiz = True
            except Exception:
                pass
                
        # 2. Check challenges
        challenges_completed = True
        if challenge_ids:
            for c_id in challenge_ids:
                solved = Solves.query.filter_by(user_id=user.id, challenge_id=c_id).first()
                if not solved:
                    challenges_completed = False
                    break
        if not challenges_completed:
            target_pos = idx + 1
            break
            
        # 3. Check quiz
        if has_quiz:
            quiz_prog = TutorialProgress.query.filter_by(
                user_id=user.id, lesson_id=l.id,
                type="quiz", item_key="quick_quiz", solved=True
            ).first()
            if not quiz_prog:
                target_pos = idx + 1
                break
                
        # 4. Check questions
        if N_questions > 0:
            solves = TutorialProgress.query.filter_by(
                user_id=user.id, lesson_id=l.id,
                type="question", solved=True
            ).all()
            solved_hashes = {s.item_key for s in solves}
            questions_completed = True
            for h in question_hashes:
                if h not in solved_hashes:
                    questions_completed = False
                    break
            if not questions_completed:
                target_pos = idx + 1
                break
                
    return redirect(url_for('tutorials.view_lesson', module_id=module_id, lesson_position=target_pos))

@tutorials_bp.route("/tutorials/<int:module_id>/<int:lesson_position>")
@authed_only
def view_lesson(module_id, lesson_position):
    if is_admin():
        module = TutorialModule.query.filter_by(id=module_id).first_or_404()
    else:
        module = TutorialModule.query.filter_by(id=module_id, hidden=False).first_or_404()

    lessons = module.lessons.all()
    
    if not lessons:
        return render_template(
            "plugins/tutorials/templates/lesson.html",
            module=module,
            lesson=None,
            lessons=lessons,
            lesson_position=0,
            prev_position=None,
            next_position=None,
            challenge=None
        )

    if lesson_position < 1 or lesson_position > len(lessons):
        return abort(404)

    lesson = lessons[lesson_position - 1]
    
    prev_position = lesson_position - 1 if lesson_position > 1 else None
    next_position = lesson_position + 1 if lesson_position < len(lessons) else None

    # Parse block cells or fallback to legacy markdown
    import json
    lesson_blocks = []
    is_json = False
    
    if lesson.content:
        try:
            content_stripped = lesson.content.strip()
            if content_stripped.startswith("[") and content_stripped.endswith("]"):
                data = json.loads(content_stripped)
                if isinstance(data, list):
                    lesson_blocks = data
                    is_json = True
        except Exception:
            pass

    if not is_json:
        lesson_blocks = [{"type": "markdown", "value": lesson.content or ""}]

    # Compile markdown to HTML for each block (bypassing sanitization to allow custom CSS/JS interactive elements)
    for block in lesson_blocks:
        b_type = block.get("type", "markdown")
        b_val = block.get("value", "")
        if b_type == "markdown":
            block["html"] = markdown(b_val)
        elif b_type == "code":
            b_title = block.get("title", "Python Code Block")
            block["title"] = b_title
            
            # Detect language based on the custom title
            title_lower = b_title.lower()
            if any(x in title_lower for x in ["bash", "sh", "cmd", "terminal", "command", "sudo", "pip"]):
                lang = "bash"
            elif any(x in title_lower for x in ["js", "javascript"]):
                lang = "javascript"
            elif "html" in title_lower:
                lang = "html"
            elif "css" in title_lower:
                lang = "css"
            elif "php" in title_lower:
                lang = "php"
            else:
                lang = "python"
                
            block["html"] = markdown(f"```{lang}\n{b_val}\n```")
        elif b_type == "question":
            block["html"] = markdown(b_val)
            # Secure correct answer value: delete cleartext answer from JSON before rendering to users
            if "answer" in block:
                del block["answer"]
        elif b_type == "challenge":
            c_id = block.get("challenge_id")
            if c_id:
                try:
                    block["challenge"] = Challenges.query.filter_by(id=int(c_id)).first()
                except Exception:
                    block["challenge"] = None
        else:
            block["html"] = markdown(b_val)

    # Fetch associated challenge if exists
    challenge = None
    if lesson.challenge_id:
        challenge = Challenges.query.filter_by(id=lesson.challenge_id).first()

    # Parse module questions metadata for student progress tracking
    module_questions = {}
    for l in lessons:
        hashes = []
        if l.content:
            try:
                content_stripped = l.content.strip()
                if content_stripped.startswith("[") and content_stripped.endswith("]"):
                    import json
                    cells = json.loads(content_stripped)
                    has_quick_quiz = False
                    if isinstance(cells, list):
                        for cell in cells:
                            if cell.get("type") == "question":
                                if not cell.get("hash"):
                                    import hashlib
                                    ans = cell.get("answer", "").strip()
                                    cell["hash"] = hashlib.sha256(ans.encode("utf-8")).hexdigest()
                                if cell.get("hash"):
                                    hashes.append(cell["hash"])
                            elif cell.get("type") == "challenge":
                                c_id = cell.get("challenge_id")
                                if c_id:
                                    hashes.append(f"challenge_{c_id}")
                            elif cell.get("type") == "markdown":
                                val = cell.get("value", "")
                                import re
                                embedded_cids = re.findall(r"challenge_id:\s*(\d+)", val)
                                for cid_str in embedded_cids:
                                    hashes.append(f"challenge_{cid_str}")
                                if "mini-quiz-box" in val or "w-quiz-option" in val or "Lesson Quick Quiz" in val:
                                    has_quick_quiz = True
                    if has_quick_quiz:
                        hashes.append("quick_quiz")
                if l.challenge_id:
                    hashes.append(f"challenge_{l.challenge_id}")
            except Exception:
                pass
        module_questions[l.id] = hashes

    return render_template(
        "plugins/tutorials/templates/lesson.html",
        module=module,
        lesson=lesson,
        lesson_blocks=lesson_blocks,
        lessons=lessons,
        lesson_position=lesson_position,
        prev_position=prev_position,
        next_position=next_position,
        challenge=challenge,
        module_questions=module_questions
    )

def process_lesson_content(content):
    if not content:
        return content
    try:
        content_stripped = content.strip()
        if content_stripped.startswith("[") and content_stripped.endswith("]"):
            import json
            import hashlib
            cells = json.loads(content_stripped)
            if isinstance(cells, list):
                for cell in cells:
                    if cell.get("type") == "question":
                        ans = cell.get("answer", "").strip()
                        cell["hash"] = hashlib.sha256(ans.encode("utf-8")).hexdigest()
                return json.dumps(cells)
    except Exception:
        pass
    return content


@tutorials_bp.route("/vpn", methods=["GET"])
def openvpn_guide_page():
    user = get_current_user()
    username = user.name if user else "student"
    safe_username = re.sub(r'[^a-zA-Z0-9_]', '_', username)
    return render_template("plugins/tutorials/templates/vpn_guide.html", username=username, safe_username=safe_username)

@tutorials_bp.route("/vpn/download", methods=["GET"])
def download_vpn_config():
    try:
        user = get_current_user()
        username = user.name if user else "student"
        safe_username = re.sub(r'[^a-zA-Z0-9_]', '_', username)

        ovpn_path = "/var/uploads/crrulearnctf_student.ovpn"
        if not os.path.exists(ovpn_path):
            ovpn_path = "/home/kali/crru_ctf/openvpn/crrulearnctf_student.ovpn"
        
        if os.path.exists(ovpn_path):
            with open(ovpn_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            
            # Ensure OpenVPN connects directly to unproxied server IP instead of Cloudflare proxy (104.21.6.103)
            content = re.sub(r'remote\s+\S+\s+1194', 'remote 192.168.238.128 1194', content)
            
            custom_content = f"# Dedicated OpenVPN Client Profile for CRRU CTF User: {safe_username}\n" + content
            response = make_response(custom_content)
            response.headers["Content-Type"] = "application/x-openvpn-profile"
            response.headers["Content-Disposition"] = f"attachment; filename=crrulearnctf_{safe_username}.ovpn"
            return response
    except Exception as e:
        print(f"Error in download_vpn_config: {e}")
    
    return jsonify({"success": False, "message": "OpenVPN profile configuration file not found on server."}), 404

@tutorials_bp.route("/vpn/target_ip", methods=["GET"])
def get_vpn_target_ip():
    try:
        user = get_current_user()
        if not user:
            return jsonify({"success": False, "message": "Unauthorized"}), 401
        
        import docker
        client = docker.from_env()
        containers = client.containers.list()
        
        target_ip = None
        for c in containers:
            if c.name.startswith(f"{user.id}-"):
                nets = c.attrs.get("NetworkSettings", {}).get("Networks", {})
                if "vpn_target_net" in nets:
                    target_ip = nets["vpn_target_net"].get("IPAddress")
                    if target_ip:
                        break
        
        if not target_ip:
            target_ip = "10.100.0.3"
            
        return jsonify({"success": True, "ip": target_ip})
    except Exception as e:
        return jsonify({"success": False, "message": str(e), "ip": "10.100.0.3"})

try:
    register_user_page_menu_bar("🛡️ OpenVPN Config", "/vpn")
except Exception:
    pass

# --- ADMIN ROUTES ---

@tutorials_bp.route("/admin/tutorials")
@admins_only
def admin_list_modules():
    modules = TutorialModule.query.order_by(TutorialModule.position.asc(), TutorialModule.id.asc()).all()
    return render_template("plugins/tutorials/templates/admin/admin_modules.html", modules=modules)

@tutorials_bp.route("/admin/tutorials/module/new", methods=["GET", "POST"])
@admins_only
def admin_create_module():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        category = request.form.get("category")
        position = int(request.form.get("position") or 0)
        hidden = bool(request.form.get("hidden"))
        level = request.form.get("level") or "Basic"
        level_color = request.form.get("level_color") or "#00f0ff"

        module = TutorialModule(
            title=title,
            description=description,
            category=category,
            position=position,
            hidden=hidden,
            level=level,
            level_color=level_color
        )
        db.session.add(module)
        db.session.commit()
        return redirect(url_for("tutorials.admin_list_modules"))

    return render_template("plugins/tutorials/templates/admin/admin_module_edit.html", module=None)

@tutorials_bp.route("/admin/tutorials/module/<int:module_id>/edit", methods=["GET", "POST"])
@admins_only
def admin_edit_module(module_id):
    module = TutorialModule.query.filter_by(id=module_id).first_or_404()

    if request.method == "POST":
        module.title = request.form.get("title")
        module.description = request.form.get("description")
        module.category = request.form.get("category")
        module.position = int(request.form.get("position") or 0)
        module.hidden = bool(request.form.get("hidden"))
        module.level = request.form.get("level") or "Basic"
        module.level_color = request.form.get("level_color") or "#00f0ff"
        
        db.session.commit()
        return redirect(url_for("tutorials.admin_list_modules"))

    lessons = module.lessons.all()
    return render_template("plugins/tutorials/templates/admin/admin_module_edit.html", module=module, lessons=lessons)

@tutorials_bp.route("/admin/tutorials/module/<int:module_id>/delete", methods=["POST"])
@admins_only
def admin_delete_module(module_id):
    module = TutorialModule.query.filter_by(id=module_id).first_or_404()
    db.session.delete(module)
    db.session.commit()
    return redirect(url_for("tutorials.admin_list_modules"))

@tutorials_bp.route("/admin/tutorials/module/<int:module_id>/lesson/new", methods=["GET", "POST"])
@admins_only
def admin_create_lesson(module_id):
    module = TutorialModule.query.filter_by(id=module_id).first_or_404()
    challenges = Challenges.query.all()

    if request.method == "POST":
        title = request.form.get("title")
        content = process_lesson_content(request.form.get("content"))
        challenge_id = request.form.get("challenge_id")
        position = int(request.form.get("position") or 0)

        # Parse challenge_id to int or None
        challenge_id = int(challenge_id) if challenge_id else None

        lesson = TutorialLesson(
            module_id=module_id,
            title=title,
            content=content,
            challenge_id=challenge_id,
            position=position
        )
        db.session.add(lesson)
        db.session.commit()
        return redirect(url_for("tutorials.admin_edit_module", module_id=module_id))

    return render_template(
        "plugins/tutorials/templates/admin/admin_lesson_edit.html",
        module=module,
        lesson=None,
        challenges=challenges
    )

@tutorials_bp.route("/admin/tutorials/lesson/<int:lesson_id>/edit", methods=["GET", "POST"])
@admins_only
def admin_edit_lesson(lesson_id):
    lesson = TutorialLesson.query.filter_by(id=lesson_id).first_or_404()
    module = lesson.module
    challenges = Challenges.query.all()

    if request.method == "POST":
        lesson.title = request.form.get("title")
        lesson.content = process_lesson_content(request.form.get("content"))
        challenge_id = request.form.get("challenge_id")
        lesson.challenge_id = int(challenge_id) if challenge_id else None
        lesson.position = int(request.form.get("position") or 0)

        db.session.commit()
        return redirect(url_for("tutorials.admin_edit_module", module_id=module.id))

    return render_template(
        "plugins/tutorials/templates/admin/admin_lesson_edit.html",
        module=module,
        lesson=lesson,
        challenges=challenges
    )

@tutorials_bp.route("/admin/tutorials/lesson/<int:lesson_id>/delete", methods=["POST"])
@admins_only
def admin_delete_lesson(lesson_id):
    lesson = TutorialLesson.query.filter_by(id=lesson_id).first_or_404()
    module_id = lesson.module_id
    db.session.delete(lesson)
    db.session.commit()
    return redirect(url_for("tutorials.admin_edit_module", module_id=module_id))


@tutorials_bp.route("/admin/tutorials/upload", methods=["POST"])
@admins_only
def admin_upload_file():
    if "file" not in request.files:
        return jsonify({"success": False, "message": "No file uploaded"}), 400
    
    file_obj = request.files["file"]
    if file_obj.filename == "":
        return jsonify({"success": False, "message": "No filename"}), 400
        
    try:
        from werkzeug.utils import secure_filename
        filename = secure_filename(file_obj.filename)
        
        # Save directly to the static/uploads folder inside the repository
        plugin_dir = os.path.dirname(__file__)
        static_uploads_dir = os.path.join(plugin_dir, "static", "uploads")
        if not os.path.exists(static_uploads_dir):
            os.makedirs(static_uploads_dir)
            
        save_path = os.path.join(static_uploads_dir, filename)
        file_obj.save(save_path)
        
        # Generate blueprint static URL
        file_url = url_for("tutorials.static", filename="uploads/" + filename)
        return jsonify({"success": True, "location": file_url})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


# --- HELPERS FOR PRE/POST TEST STATISTICS ---

def get_default_tests(module):
    lessons = module.lessons.all()
    assessment_lessons = []
    for l in lessons:
        has_assessment = False
        if l.content:
            try:
                import json
                if l.content.strip().startswith("["):
                    cells = json.loads(l.content)
                    for c in cells:
                        if c.get("type") == "question":
                            has_assessment = True
                        elif c.get("type") == "markdown" and any(kw in c.get("value", "") for kw in ["mini-quiz-box", "w-quiz-option", "Lesson Quick Quiz"]):
                            has_assessment = True
            except Exception:
                pass
        if has_assessment:
            assessment_lessons.append(l)
            
    pre_id = assessment_lessons[0].id if assessment_lessons else None
    post_id = assessment_lessons[-1].id if len(assessment_lessons) > 1 else None
    return pre_id, post_id

def get_lesson_score(user_id, lesson_id):
    """Returns a tuple (solved_count, total, percent) or None if no questions found."""
    if not lesson_id:
        return None
    lesson = TutorialLesson.query.filter_by(id=lesson_id).first()
    if not lesson or not lesson.content:
        return None

    import json
    N = 0
    hashes = []
    has_quiz = False
    try:
        if lesson.content.strip().startswith("["):
            cells = json.loads(lesson.content)
            for cell in cells:
                if cell.get("type") == "question":
                    N += 1
                    if cell.get("hash"):
                        hashes.append(cell["hash"])
                elif cell.get("type") == "markdown":
                    val = cell.get("value", "")
                    if "mini-quiz-box" in val or "w-quiz-option" in val or "Lesson Quick Quiz" in val:
                        has_quiz = True
        else:
            # Plain markdown lesson — check for mini-quiz keywords
            if ("mini-quiz-box" in lesson.content or
                    "w-quiz-option" in lesson.content or
                    "Lesson Quick Quiz" in lesson.content):
                has_quiz = True
    except Exception:
        pass

    # Check for quiz progress stored with score/total
    if has_quiz:
        quiz_prog = TutorialProgress.query.filter_by(
            user_id=user_id, lesson_id=lesson_id,
            type="quiz", item_key="quick_quiz", solved=True
        ).first()
        if quiz_prog is None:
            # User has not submitted the quiz yet
            if N == 0:
                return None  # lesson has no questions at all
            # fall through to count regular questions only
        else:
            if quiz_prog.score is not None and quiz_prog.total is not None and quiz_prog.total > 0:
                # We have a real per-question score
                quiz_solved = quiz_prog.score
                quiz_total = quiz_prog.total
            else:
                # Old record without score — treat as 1/1
                quiz_solved = 1
                quiz_total = 1

            # Combine with regular question cells if any
            solves = TutorialProgress.query.filter_by(user_id=user_id, lesson_id=lesson_id, solved=True).all()
            solved_keys = {s.item_key for s in solves}
            q_solved = sum(1 for h in hashes if h in solved_keys)
            total_solved = q_solved + quiz_solved
            total_N = len(hashes) + quiz_total
            if total_N == 0:
                return None
            percent = round((total_solved / total_N) * 100)
            return (total_solved, total_N, percent)

    if N == 0:
        return None

    solves = TutorialProgress.query.filter_by(user_id=user_id, lesson_id=lesson_id, solved=True).all()
    solved_keys = {s.item_key for s in solves}

    solved_count = 0
    for h in hashes:
        if h in solved_keys:
            solved_count += 1

    percent = round((solved_count / N) * 100)
    return (solved_count, N, percent)


# --- PROGRESS TRACKING API ---

from CTFd.utils.user import get_current_user

@tutorials_bp.route("/api/v1/tutorials/progress", methods=["GET"])
@authed_only
def get_user_progress():
    user = get_current_user()
    all_progress = TutorialProgress.query.filter_by(user_id=user.id).all()
    
    solved_questions = {}
    solved_lessons = []
    solved_answers = {}
    quiz_attempts = {}
    quiz_scores = {}
    
    # Identify exam lessons (pre-test and post-test) across all modules
    exam_lessons = set()
    modules = TutorialModule.query.all()
    for m in modules:
        if m.pre_test_lesson_id:
            exam_lessons.add(m.pre_test_lesson_id)
        if m.post_test_lesson_id:
            exam_lessons.add(m.post_test_lesson_id)
            
    for s in all_progress:
        if s.solved:
            if s.type == "question":
                solved_questions[s.item_key] = "SOLVED"
            elif s.type == "quiz":
                if s.lesson_id not in solved_lessons:
                    solved_lessons.append(s.lesson_id)
                    # Fetch answer key securely for this solved lesson, but ONLY if NOT an exam!
                    if s.lesson_id not in exam_lessons:
                        answers = TutorialQuizAnswer.query.filter_by(lesson_id=s.lesson_id).order_by(TutorialQuizAnswer.q_index.asc()).all()
                        if answers:
                            solved_answers[s.lesson_id] = [a.correct_val for a in answers]
        
        # Track quiz scores for completed exams
        if s.type == "quiz" and s.lesson_id in exam_lessons:
            quiz_scores[str(s.lesson_id)] = {
                "score": s.score,
                "total": s.total
            }
        
        # Build quiz attempts from DB (all attempts for exam lessons, only correct ones for normal lessons)
        if s.type == "quiz_answer":
            is_exam = s.lesson_id in exam_lessons
            if s.solved or is_exam:
                parts = s.item_key.split("_")
                if len(parts) == 3 and parts[0] == "q":
                    try:
                        idx = int(parts[1])
                        letter = parts[2]
                        lid = str(s.lesson_id)
                        if lid not in quiz_attempts:
                            quiz_attempts[lid] = {}
                        
                        if is_exam:
                            quiz_attempts[lid][idx] = {
                                "val": letter,
                                "correct": s.solved
                            }
                        else:
                            quiz_attempts[lid][idx] = {
                                "val": letter,
                                "correct": s.solved
                            }
                    except ValueError:
                        pass
                    
    # Fetch user's solved challenges securely
    from CTFd.models import Solves
    user_solves = Solves.query.filter_by(user_id=user.id).all()
    solved_challenges = [s.challenge_id for s in user_solves]
                
    return jsonify({
        "success": True,
        "solved_questions": solved_questions,
        "solved_lessons": solved_lessons,
        "solved_answers": solved_answers,
        "solved_challenges": solved_challenges,
        "quiz_attempts": quiz_attempts,
        "quiz_scores": quiz_scores
    })

@tutorials_bp.route("/api/v1/tutorials/progress", methods=["POST"])
@authed_only
def save_user_progress():
    user = get_current_user()
    data = request.get_json() or {}
    
    lesson_id = data.get("lesson_id")
    b_type = data.get("type")
    item_key = data.get("item_key")
    solved = bool(data.get("solved", True))
    score = data.get("score")   # int or None
    total = data.get("total")   # int or None
    
    if not lesson_id or not b_type or not item_key:
        return jsonify({"success": False, "message": "Missing required fields"}), 400
        
    existing = TutorialProgress.query.filter_by(
        user_id=user.id,
        lesson_id=lesson_id,
        type=b_type,
        item_key=item_key
    ).first()
    
    if existing:
        existing.solved = solved
        if score is not None:
            existing.score = int(score)
        if total is not None:
            existing.total = int(total)
    else:
        new_progress = TutorialProgress(
            user_id=user.id,
            lesson_id=lesson_id,
            type=b_type,
            item_key=item_key,
            solved=solved,
            score=int(score) if score is not None else None,
            total=int(total) if total is not None else None,
        )
        db.session.add(new_progress)
        
    db.session.commit()
    return jsonify({"success": True})


@tutorials_bp.route("/api/v1/tutorials/quiz/submit", methods=["POST"])
@authed_only
def quiz_submit():
    """Server-side quiz checker — correct answers never leave the server."""
    user = get_current_user()
    data = request.get_json() or {}
    lesson_id = data.get("lesson_id")
    answers = data.get("answers")  # list of selected values, e.g. ["A", "C", "B", ...]

    if not lesson_id or not isinstance(answers, list):
        return jsonify({"success": False, "message": "Missing lesson_id or answers"}), 400

    # Load correct answers from DB in order
    correct_rows = (
        TutorialQuizAnswer.query
        .filter_by(lesson_id=lesson_id)
        .order_by(TutorialQuizAnswer.q_index)
        .all()
    )
    if not correct_rows:
        return jsonify({"success": False, "message": "No answer key found for this lesson"}), 404

    total = len(correct_rows)
    results = []
    score = 0
    for i, row in enumerate(correct_rows):
        submitted = answers[i].strip().upper() if i < len(answers) and answers[i] else ""
        is_correct = submitted == row.correct_val.strip().upper()
        results.append(is_correct)
        if is_correct:
            score += 1

    # Save progress: solved is True only if score is 100%
    is_solved = (score == total)
    existing = TutorialProgress.query.filter_by(
        user_id=user.id, lesson_id=lesson_id,
        type="quiz", item_key="quick_quiz"
    ).first()
    if existing:
        existing.solved = is_solved
        existing.score = score
        existing.total = total
    else:
        db.session.add(TutorialProgress(
            user_id=user.id,
            lesson_id=lesson_id,
            type="quiz",
            item_key="quick_quiz",
            solved=is_solved,
            score=score,
            total=total,
        ))
        
    # Save detailed attempts for each question to DB
    for i, row in enumerate(correct_rows):
        submitted = answers[i].strip().upper() if i < len(answers) and answers[i] else ""
        is_correct = results[i]
        
        # Check if an attempt already exists for this question index
        existing_q = TutorialProgress.query.filter_by(
            user_id=user.id, lesson_id=lesson_id,
            type="quiz_answer"
        ).filter(TutorialProgress.item_key.like(f"q_{i}_%")).first()
        
        item_key = f"q_{i}_{submitted}"
        if existing_q:
            existing_q.item_key = item_key
            existing_q.solved = is_correct
        else:
            db.session.add(TutorialProgress(
                user_id=user.id,
                lesson_id=lesson_id,
                type="quiz_answer",
                item_key=item_key,
                solved=is_correct,
            ))
            
    db.session.commit()

    return jsonify({
        "success": True,
        "score": score,
        "total": total,
        "results": results,
    })


@tutorials_bp.route("/api/v1/tutorials/quiz/submit_single", methods=["POST"])
@authed_only
def quiz_submit_single():
    """Check a single quiz question and save it.
    If it's an exam (pre-test/post-test):
      - We lock it: they cannot submit if they have already submitted this question before.
      - We save the attempt (solved = is_correct) whether it is correct or not.
      - Once all questions are answered, we mark the main quiz as solved.
    If it's a normal lesson:
      - We only save when they get it correct (solved = True).
      - If they answer incorrectly, we don't save, so they can keep trying.
    """
    user = get_current_user()
    data = request.get_json() or {}
    lesson_id = data.get("lesson_id")
    q_index = data.get("q_index")
    submitted = data.get("answer")
    
    if lesson_id is None or q_index is None or not submitted:
        return jsonify({"success": False, "message": "Missing lesson_id, q_index, or answer"}), 400
        
    row = TutorialQuizAnswer.query.filter_by(lesson_id=lesson_id, q_index=q_index).first()
    if not row:
        return jsonify({"success": False, "message": "Question not found"}), 404
        
    is_correct = submitted.strip().upper() == row.correct_val.strip().upper()
    
    # Check if this lesson is registered as pre-test or post-test in any module
    module_with_pre = TutorialModule.query.filter_by(pre_test_lesson_id=lesson_id).first()
    module_with_post = TutorialModule.query.filter_by(post_test_lesson_id=lesson_id).first()
    is_exam = (module_with_pre is not None) or (module_with_post is not None)
    
    if is_exam:
        # Check if they have already answered this question index
        existing_attempt = TutorialProgress.query.filter_by(
            user_id=user.id, lesson_id=lesson_id,
            type="quiz_answer"
        ).filter(TutorialProgress.item_key.like(f"q_{q_index}_%")).first()
        
        item_key = f"q_{q_index}_{submitted.strip().upper()}"
        if existing_attempt:
            existing_attempt.item_key = item_key
            existing_attempt.solved = is_correct
        else:
            db.session.add(TutorialProgress(
                user_id=user.id,
                lesson_id=lesson_id,
                type="quiz_answer",
                item_key=item_key,
                solved=is_correct
            ))
        
        # Calculate progress for exam
        total_answers = TutorialQuizAnswer.query.filter_by(lesson_id=lesson_id).count()
        
        # Commit to flush the new row, then query unique answered questions
        db.session.commit()
        
        answered_rows = TutorialProgress.query.filter_by(
            user_id=user.id, lesson_id=lesson_id,
            type="quiz_answer"
        ).all()
        
        answered_indices = set()
        correct_count = 0
        for s in answered_rows:
            parts = s.item_key.split("_")
            if len(parts) == 3 and parts[0] == "q":
                try:
                    q_idx = int(parts[1])
                    answered_indices.add(q_idx)
                    if s.solved:
                        correct_count += 1
                except ValueError:
                    pass
                    
        if len(answered_indices) >= total_answers:
            existing_main = TutorialProgress.query.filter_by(
                user_id=user.id, lesson_id=lesson_id,
                type="quiz", item_key="quick_quiz"
            ).first()
            if existing_main:
                existing_main.solved = True
                existing_main.score = correct_count
                existing_main.total = total_answers
            else:
                db.session.add(TutorialProgress(
                    user_id=user.id,
                    lesson_id=lesson_id,
                    type="quiz",
                    item_key="quick_quiz",
                    solved=True,
                    score=correct_count,
                    total=total_answers
                ))
        db.session.commit()
        
    else:
        # Normal quiz logic
        if is_correct:
            existing = TutorialProgress.query.filter_by(
                user_id=user.id, lesson_id=lesson_id,
                type="quiz_answer"
            ).filter(TutorialProgress.item_key.like(f"q_{q_index}_%")).first()
            
            item_key = f"q_{q_index}_{submitted.strip().upper()}"
            if existing:
                existing.item_key = item_key
                existing.solved = True
            else:
                db.session.add(TutorialProgress(
                    user_id=user.id,
                    lesson_id=lesson_id,
                    type="quiz_answer",
                    item_key=item_key,
                    solved=True
                ))
                
            total_answers = TutorialQuizAnswer.query.filter_by(lesson_id=lesson_id).count()
            solved_rows = TutorialProgress.query.filter_by(
                user_id=user.id, lesson_id=lesson_id,
                type="quiz_answer", solved=True
            ).all()
            
            solved_indices = set()
            for s in solved_rows:
                parts = s.item_key.split("_")
                if len(parts) == 3 and parts[0] == "q":
                    try:
                        solved_indices.add(int(parts[1]))
                    except ValueError:
                        pass
                        
            if len(solved_indices) >= total_answers:
                existing_main = TutorialProgress.query.filter_by(
                    user_id=user.id, lesson_id=lesson_id,
                    type="quiz", item_key="quick_quiz"
                ).first()
                if existing_main:
                    existing_main.solved = True
                    existing_main.score = total_answers
                    existing_main.total = total_answers
                else:
                    db.session.add(TutorialProgress(
                        user_id=user.id,
                        lesson_id=lesson_id,
                        type="quiz",
                        item_key="quick_quiz",
                        solved=True,
                        score=total_answers,
                        total=total_answers
                    ))
            db.session.commit()
            
    return jsonify({
        "success": True,
        "correct": is_correct,
        "correct_val": row.correct_val
    })



@tutorials_bp.route("/admin/tutorials/config_tests", methods=["POST"])
@admins_only
def admin_config_tests():
    data = request.form
    module_id = int(data.get("module_id"))
    pre_id = data.get("pre_test_lesson_id")
    post_id = data.get("post_test_lesson_id")
    
    module = TutorialModule.query.filter_by(id=module_id).first_or_404()
    module.pre_test_lesson_id = int(pre_id) if pre_id else None
    module.post_test_lesson_id = int(post_id) if post_id else None
    
    db.session.commit()
    return redirect(url_for("tutorials.admin_view_statistics"))

@tutorials_bp.route("/admin/tutorials/statistics", methods=["GET"])
@admins_only
def admin_view_statistics():
    modules = TutorialModule.query.order_by(TutorialModule.position.asc(), TutorialModule.id.asc()).all()
    students = Users.query.filter_by(type="user").all()
    
    module_configs = []
    for m in modules:
        pre_id = m.pre_test_lesson_id
        post_id = m.post_test_lesson_id
        default_pre, default_post = get_default_tests(m)
        
        lessons = m.lessons.all()
        
        pre_scores = []
        post_scores = []
        for s in students:
            pre_score = get_lesson_score(s.id, pre_id or default_pre)
            post_score = get_lesson_score(s.id, post_id or default_post)
            if pre_score is not None:
                pre_scores.append(pre_score[2])  # percent
            if post_score is not None:
                post_scores.append(post_score[2])  # percent
                
        avg_pre = round(sum(pre_scores) / len(pre_scores)) if pre_scores else "-"
        avg_post = round(sum(post_scores) / len(post_scores)) if post_scores else "-"
        
        module_configs.append({
            "module": m,
            "lessons": lessons,
            "pre_id": pre_id or default_pre,
            "post_id": post_id or default_post,
            "avg_pre": avg_pre,
            "avg_post": avg_post,
        })
        
    student_scores = []
    for s in students:
        row = {
            "student": s,
            "modules": []
        }
        for m in modules:
            pre_id = m.pre_test_lesson_id
            post_id = m.post_test_lesson_id
            default_pre, default_post = get_default_tests(m)
            
            pre_score = get_lesson_score(s.id, pre_id or default_pre)
            post_score = get_lesson_score(s.id, post_id or default_post)
            
            gain = "-"
            if pre_score is not None and post_score is not None:
                diff = post_score[2] - pre_score[2]
                gain = f"{diff:+d}%"
                
            row["modules"].append({
                "module_id": m.id,
                "pre": f"{pre_score[0]}/{pre_score[1]} ({pre_score[2]}%)" if pre_score is not None else "-",
                "post": f"{post_score[0]}/{post_score[1]} ({post_score[2]}%)" if post_score is not None else "-",
                "gain": gain
            })
        student_scores.append(row)
        
    return render_template(
        "plugins/tutorials/templates/admin/admin_statistics.html",
        module_configs=module_configs,
        student_scores=student_scores,
        modules=modules
    )

@tutorials_bp.route("/admin/tutorials/statistics/export", methods=["GET"])
@admins_only
def admin_export_statistics():
    import csv
    from io import StringIO
    
    modules = TutorialModule.query.order_by(TutorialModule.position.asc(), TutorialModule.id.asc()).all()
    students = Users.query.filter_by(type="user").all()
    
    si = StringIO()
    cw = csv.writer(si)
    
    headers = ["Username", "Email"]
    for m in modules:
        headers.extend([f"{m.title} (Pre-test)", f"{m.title} (Post-test)", f"{m.title} (Gain)"])
    cw.writerow(headers)
    
    for s in students:
        row = [s.name, s.email]
        for m in modules:
            pre_id = m.pre_test_lesson_id
            post_id = m.post_test_lesson_id
            default_pre, default_post = get_default_tests(m)
            
            pre_score = get_lesson_score(s.id, pre_id or default_pre)
            post_score = get_lesson_score(s.id, post_id or default_post)
            
            gain = "-"
            if pre_score is not None and post_score is not None:
                diff = post_score[2] - pre_score[2]
                gain = f"{diff:+d}%"
                
            row.extend([
                f"{pre_score[0]}/{pre_score[1]} ({pre_score[2]}%)" if pre_score is not None else "-",
                f"{post_score[0]}/{post_score[1]} ({post_score[2]}%)" if post_score is not None else "-",
                gain
            ])
        cw.writerow(row)
        
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=tutorial_statistics.csv"
    output.headers["Content-type"] = "text/csv; charset=utf-8"
    return output


# --- PLUGIN INITALIZATION ---

def load(app):
    # Dynamically create the plugin tables if they don't exist
    db.create_all()

    # Run manual migration to add pre/post test columns if missing
    try:
        from sqlalchemy import text
        engine = db.engine
        with engine.connect() as conn:
            result = conn.execute(text("SHOW COLUMNS FROM tutorial_module LIKE 'pre_test_lesson_id'"))
            if not result.fetchone():
                print("Adding pre_test_lesson_id and post_test_lesson_id to tutorial_module table...")
                conn.execute(text("ALTER TABLE tutorial_module ADD COLUMN pre_test_lesson_id INT NULL"))
                conn.execute(text("ALTER TABLE tutorial_module ADD COLUMN post_test_lesson_id INT NULL"))
    except Exception as e:
        print(f"Error running database alter migration: {e}")

    # Register blueprints
    app.register_blueprint(tutorials_bp)

    # Register menu bar items
    register_admin_plugin_menu_bar(title="Tutorials", route="/admin/tutorials")
    register_user_page_menu_bar(title="Tutorials", route="/tutorials")



# =================================================================
# 🌐 WEB MAZE API ENDPOINT FOR LESSON 4 CTF PRACTICE LAB
# =================================================================
@tutorials_bp.route("/api/v1/maze/room/<int:room_id>", methods=["GET"])
def maze_room_endpoint(room_id):
    if room_id < 1 or room_id > 30:
        return jsonify({"success": False, "message": "Invalid room ID. Choose between 1 and 30."}), 400
    
    if room_id == 22:
        return jsonify({
            "success": True,
            "room": 22,
            "status": "SECRET_CHEST",
            "message": "🎉 [SUCCESS] You found the secret chest in Room 22!",
            "flag": "flag{web_maze_runner_automation_master_8821}"
        })
    else:
        return jsonify({
            "success": True,
            "room": room_id,
            "status": "EMPTY",
            "message": f"Empty room {room_id}... Just cobwebs and dust!"
        })
