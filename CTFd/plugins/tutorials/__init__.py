import os
from flask import Blueprint, render_template, request, redirect, url_for, abort, jsonify
from CTFd.models import db, Challenges
from CTFd.utils.decorators import admins_only, authed_only
from CTFd.utils.user import is_admin
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
                    if isinstance(cells, list):
                        for cell in cells:
                            if cell.get("type") == "question":
                                if not cell.get("hash"):
                                    import hashlib
                                    ans = cell.get("answer", "").strip()
                                    cell["hash"] = hashlib.sha256(ans.encode("utf-8")).hexdigest()
                                if cell.get("hash"):
                                    hashes.append(cell["hash"])
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


# --- PLUGIN INITALIZATION ---

def load(app):
    # Dynamically create the plugin tables if they don't exist
    db.create_all()

    # Register blueprints
    app.register_blueprint(tutorials_bp)

    # Register menu bar items
    register_admin_plugin_menu_bar(title="Tutorials", route="/admin/tutorials")
    register_user_page_menu_bar(title="Tutorials", route="/tutorials")
