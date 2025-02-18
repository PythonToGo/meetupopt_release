from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MeetingAvailability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50), nullable=False)
    time_slot = db.Column(db.String(10), nullable=False)  # ex) "09:00"
