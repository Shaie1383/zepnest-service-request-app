from models import db


class ServiceRequest(db.Model):
    __tablename__ = "service_requests"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    preferred_date = db.Column(db.Date, nullable=False)
    preferred_time = db.Column(db.Time, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Pending")
    image_path = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.func.now(),
        onupdate=db.func.now(),
    )

    def __repr__(self):
        return f"ServiceRequest({self.title}, {self.status})"
