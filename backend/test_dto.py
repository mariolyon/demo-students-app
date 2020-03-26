import json
import unittest
import uuid

from app.dto import dto_for_student, StudentData
from app.models import Student, SexEnum


class TestDto(unittest.TestCase):

    def test_student_dto(self):
        """
        Convert Student to StudentDto and then to Json
        """
        s = Student(id=str(uuid.uuid4()), clss=3, name="Jose", sex=SexEnum.male, age=1, siblings=3, gpa=3.1)
        student_dto = dto_for_student(s)

        result = student_dto.to_json()
        expected = json.dumps(json.loads("""
        {"uuid": "%s", "class": 3, "name": "Jose", "sex": "male", "age": 1, "siblings": 3, "gpa": 3.1}
        """ % s.id))

        self.assertEqual(expected, result)

    def test_student_data(self):
        """
        Convert StudentData to Json
        """
        student_data = StudentData(clss=3, name="Jose", sex="male", age=1, siblings=3, gpa=3.1)
        result = student_data.to_json()
        expected = json.dumps(json.loads("""
        {"class": 3, "name": "Jose", "sex": "male", "age": 1, "siblings": 3, "gpa": 3.1}
        """))
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
