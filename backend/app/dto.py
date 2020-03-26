from dataclasses import dataclass, asdict, field
from dataclasses_json import dataclass_json, config


@dataclass_json
@dataclass
class StudentData:
    '''Class for describing information about a student, except for id'''
    clss: int = field(metadata=config(field_name="class"))
    name: str
    sex: str
    age: int
    siblings: int
    gpa: float


@dataclass_json
@dataclass
class StudentDto:
    '''Class for Representing a Student'''
    id: str = field(metadata=config(field_name="uuid"))
    clss: int = field(metadata=config(field_name="class"))
    name: str
    sex: str
    age: int
    siblings: int
    gpa: float


def dto_for_student(student):
    return StudentDto(
        id=student.id,
        clss=student.clss,
        name=student.name,
        sex=student.sex._value_,
        age=student.age,
        siblings=student.siblings,
        gpa=student.gpa)
