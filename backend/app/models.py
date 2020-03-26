from app import db
import enum


class SexEnum(enum.Enum):
    female = "female"
    male = "male"


class Student(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    clss = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    sex = db.Column(db.Enum(SexEnum), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    siblings = db.Column(db.Integer, nullable=False)
    gpa = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Student {}>'.format(self.id)
