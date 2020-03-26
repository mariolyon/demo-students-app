import unittest

from app.models import Student
from app import service
from app.service import StudentData


class TestService(unittest.TestCase):
    s = StudentData(clss=3,
                    name="Jose",
                    sex="male",
                    age=1,
                    siblings=3,
                    gpa=3.1)

    def test_add_student(self):
        """
        Add student
        """
        result = service.add_student(self.s)
        self.assertEqual(result.clss, self.s.clss)
        self.assertEqual(result.name, self.s.name)
        self.assertEqual(result.sex._name_, self.s.sex)
        self.assertEqual(result.age, self.s.age)
        self.assertEqual(result.siblings, self.s.siblings)
        self.assertEqual(result.gpa, self.s.gpa)

    def test_get_student(self):
        """
        Get student
        """
        added = service.add_student(self.s)
        result = service.get_student(added.id)

        self.assertEqual(result.id, added.id)
        self.assertEqual(result.clss, self.s.clss)
        self.assertEqual(result.name, self.s.name)
        self.assertEqual(result.sex._name_, self.s.sex)
        self.assertEqual(result.age, self.s.age)
        self.assertEqual(result.siblings, self.s.siblings)
        self.assertEqual(result.gpa, self.s.gpa)

    def test_delete_student(self):
        """
        Delete student
        """
        s = StudentData(clss=3,
                        name="Jose",
                        sex="male",
                        age=1,
                        siblings=3,
                        gpa=3.1)

        added = service.add_student(s)
        service.delete_student(added.id)
        self.assertIsNone(Student.query.get(added.id))

    def test_update_student(self):
        """
        Delete student
        """

        added = service.add_student(self.s)

        new_data = StudentData(clss=4,
                               name="Joan",
                               sex="female",
                               age=2,
                               siblings=4,
                               gpa=4.1)

        result = service.update_student(added.id, new_data)
        self.assertEqual(result.id, added.id)
        self.assertEqual(result.clss, new_data.clss)
        self.assertEqual(result.name, new_data.name)
        self.assertEqual(result.sex._name_, new_data.sex)
        self.assertEqual(result.age, new_data.age)
        self.assertEqual(result.siblings, new_data.siblings)
        self.assertEqual(result.gpa, new_data.gpa)
        self.assertEqual(result, Student.query.get(added.id))


if __name__ == '__main__':
    unittest.main()
