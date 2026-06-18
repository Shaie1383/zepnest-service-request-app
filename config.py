import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-me")
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "service_request_app")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = str(BASE_DIR / "uploads")
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
    ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

    WTF_CSRF_TIME_LIMIT = None


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
