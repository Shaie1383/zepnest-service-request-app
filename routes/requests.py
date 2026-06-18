import os
from uuid import uuid4

from flask import Blueprint, abort, current_app, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from PIL import Image
from sqlalchemy import or_
from werkzeug.utils import secure_filename

from forms.request_form import RequestForm
from models import db
from models.service_request import ServiceRequest


requests_bp = Blueprint("requests", __name__)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in current_app.config["ALLOWED_EXTENSIONS"]


def save_image(file_storage):
    if not file_storage or not file_storage.filename:
        return None

    if not allowed_file(file_storage.filename):
        raise ValueError("Only JPG, JPEG, and PNG images are allowed.")

    filename = secure_filename(file_storage.filename)
    file_ext = filename.rsplit(".", 1)[1].lower()
    unique_filename = f"{uuid4().hex}.{file_ext}"
    upload_path = os.path.join(current_app.config["UPLOAD_FOLDER"], unique_filename)

    try:
        file_storage.stream.seek(0)
        image = Image.open(file_storage.stream)
        image.verify()
        file_storage.stream.seek(0)
        file_storage.save(upload_path)
    except Exception as exc:
        raise ValueError("Uploaded file is not a valid image.") from exc

    return unique_filename


def delete_image(filename):
    if not filename:
        return

    file_path = os.path.join(current_app.config["UPLOAD_FOLDER"], filename)
    if os.path.exists(file_path):
        os.remove(file_path)


@requests_bp.route("/dashboard")
@login_required
def dashboard():
    search_term = request.args.get("q", "").strip()
    sort_key = request.args.get("sort", "created_desc")
    page = request.args.get("page", 1, type=int)

    query = ServiceRequest.query.filter_by(user_id=current_user.id)

    if search_term:
        like_term = f"%{search_term}%"
        query = query.filter(
            or_(
                ServiceRequest.title.ilike(like_term),
                ServiceRequest.category.ilike(like_term),
            )
        )

    sort_map = {
        "created_desc": ServiceRequest.created_at.desc(),
        "created_asc": ServiceRequest.created_at.asc(),
        "status_asc": ServiceRequest.status.asc(),
        "status_desc": ServiceRequest.status.desc(),
        "date_asc": ServiceRequest.preferred_date.asc(),
        "date_desc": ServiceRequest.preferred_date.desc(),
    }
    query = query.order_by(sort_map.get(sort_key, ServiceRequest.created_at.desc()))

    pagination = query.paginate(page=page, per_page=6, error_out=False)
    requests_list = pagination.items

    total_requests = ServiceRequest.query.filter_by(user_id=current_user.id).count()
    pending_count = ServiceRequest.query.filter_by(user_id=current_user.id, status="Pending").count()
    in_progress_count = ServiceRequest.query.filter_by(user_id=current_user.id, status="In Progress").count()
    completed_count = ServiceRequest.query.filter_by(user_id=current_user.id, status="Completed").count()

    return render_template(
        "dashboard.html",
        requests_list=requests_list,
        pagination=pagination,
        search_term=search_term,
        sort_key=sort_key,
        total_requests=total_requests,
        pending_count=pending_count,
        in_progress_count=in_progress_count,
        completed_count=completed_count,
    )


@requests_bp.route("/requests/create", methods=["GET", "POST"])
@login_required
def create_request():
    form = RequestForm()
    if form.validate_on_submit():
        image_file = request.files.get("image")
        try:
            image_path = save_image(image_file) if image_file and image_file.filename else None
        except ValueError as exc:
            form.image.errors.append(str(exc))
            return render_template("create_request.html", form=form)

        service_request = ServiceRequest(
            user_id=current_user.id,
            title=form.title.data.strip(),
            description=form.description.data.strip(),
            category=form.category.data,
            address=form.address.data.strip(),
            preferred_date=form.preferred_date.data,
            preferred_time=form.preferred_time.data,
            status="Pending",
            image_path=image_path,
        )
        db.session.add(service_request)
        db.session.commit()
        flash("Service request created successfully.", "success")
        return redirect(url_for("requests.dashboard"))

    return render_template("create_request.html", form=form)


@requests_bp.route("/requests/<int:request_id>")
@login_required
def request_details(request_id):
    service_request = ServiceRequest.query.get_or_404(request_id)
    if service_request.user_id != current_user.id:
        abort(403)

    return render_template("request_details.html", service_request=service_request)


@requests_bp.route("/requests/<int:request_id>/edit", methods=["GET", "POST"])
@login_required
def edit_request(request_id):
    service_request = ServiceRequest.query.get_or_404(request_id)
    if service_request.user_id != current_user.id:
        abort(403)

    form = RequestForm(obj=service_request)
    if form.validate_on_submit():
        old_image = service_request.image_path
        image_file = request.files.get("image")
        if image_file and image_file.filename:
            try:
                new_image_path = save_image(image_file)
            except ValueError as exc:
                form.image.errors.append(str(exc))
                return render_template("edit_request.html", form=form, service_request=service_request)

            if old_image and new_image_path:
                delete_image(old_image)
            service_request.image_path = new_image_path

        service_request.title = form.title.data.strip()
        service_request.description = form.description.data.strip()
        service_request.category = form.category.data
        service_request.address = form.address.data.strip()
        service_request.preferred_date = form.preferred_date.data
        service_request.preferred_time = form.preferred_time.data
        service_request.status = form.status.data or service_request.status

        db.session.commit()
        flash("Service request updated successfully.", "success")
        return redirect(url_for("requests.request_details", request_id=service_request.id))

    return render_template("edit_request.html", form=form, service_request=service_request)


@requests_bp.route("/requests/<int:request_id>/delete", methods=["POST"])
@login_required
def delete_request(request_id):
    service_request = ServiceRequest.query.get_or_404(request_id)
    if service_request.user_id != current_user.id:
        abort(403)

    delete_image(service_request.image_path)
    db.session.delete(service_request)
    db.session.commit()
    flash("Service request deleted successfully.", "info")
    return redirect(url_for("requests.dashboard"))
