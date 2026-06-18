import os

from dotenv import load_dotenv


load_dotenv()

from config import Config
from flask import Flask, render_template, send_from_directory

from models import db, login_manager


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please log in to continue."
    login_manager.login_message_category = "warning"

    from routes.auth import auth_bp
    from routes.requests import requests_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(requests_bp)

    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/uploads/<path:filename>")
    def uploaded_file(filename):
        return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template("404.html"), 404

    @app.errorhandler(403)
    def forbidden_error(error):
        return render_template("403.html"), 403

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template("500.html"), 500

    with app.app_context():
        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
        db.create_all()

    return app

application = create_app()

if __name__ == "__main__":
    application.run(debug=True)