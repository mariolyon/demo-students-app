from app import db
from app.models import Student
from dataclasses import asdict

from app.dto import StudentData, StudentDto
import uuid


def add_student(data: StudentData):
    student = Student(id=str(uuid.uuid4()),
                clss=data.clss,
                name=data.name,
                sex=data.sex,
                age=data.age,
                siblings=data.siblings,
                gpa=data.gpa)
    db.session.add(student)
    db.session.commit()
    return get_student(student.id)


def update_student(id: str, data: StudentData):
    search_result = db.session.query(Student).filter_by(id=id)
    if search_result.count() == 1:
        search_result.update(asdict(data), synchronize_session=False)
        db.session.commit()
        return Student.query.get(id)
    else:
        return None


def delete_student(id):
    student = get_student(id)
    if student is not None:
        db.session.delete(student)
        db.session.commit()
    return student


def get_student(id: str):
    return Student.query.get(id)


def list_students():
    return Student.query.all()
