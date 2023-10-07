from app import db
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import JSON

Base = declarative_base

class WorksModel(db.Model):
    __tablename__ = 'works'

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String)
    position = db.Column(db.String)
    date_ini = db.Column(db.DateTime)
    date_end = db.Column(db.DateTime)
    activities = db.Column(JSON)
    technologies = db.Column(JSON)
    extra_data = db.Column(JSON)

    def __init__(self, position):
        self.position = position

    def __repr__(self):
        return f"<Work {self.position}>"