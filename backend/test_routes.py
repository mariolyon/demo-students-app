import json


class TestRoutes:
    student_attributes = {
        "age": 1,
        "class": 3,
        "gpa": 3.1,
        "name": "Jose",
        "sex": "male",
        "siblings": 3,
    }

    def test_undefined_route(self, client):
        """
        Undefined route
        """
        response = client.get("/undefined")
        assert response.status_code == 404

    def test_list_students(self, client):
        """
        List students
        """
        add_response = self.add_student(client)
        print(type(add_response.json))
        uuid = add_response.json.get("uuid")

        students_url = "/students"
        list_response = client.get(students_url)
        assert list_response.status_code == 200
        assert list_response.content_type == "application/json"
        expected_body = self.student_attributes.copy()
        expected_body["uuid"] = uuid
        expected_body_json = json.loads(json.dumps([expected_body]))
        assert list_response.json == expected_body_json

    def test_list_students_empty(self, client):
        """
        List students when none exist
        """
        students_url = "/students"
        list_response = client.get(students_url)
        assert list_response.status_code == 200
        assert list_response.content_type == "application/json"
        expected_body_json = json.loads("[]")
        assert list_response.json == expected_body_json

    def test_add_student_not_json(self, client):
        """
        Add student when content-type is not application/json
        """
        add_response = client.post("/student", data=json.dumps(TestRoutes.student_attributes))

        assert add_response.status_code == 422
        assert add_response.content_type == "application/json"
        assert add_response.json == json.loads('{"error": "Malformed data"}')

    def test_add_student(self, client):
        """
        Add student
        """
        add_response = self.add_student(client)
        assert add_response.status_code == 201
        assert add_response.content_type == "application/json"

        expected_body = self.student_attributes.copy()
        expected_body["uuid"] = add_response.json.get("uuid")
        expected_body_json = json.loads(json.dumps(expected_body))
        assert add_response.json == expected_body_json

    def test_get_student(self, client):
        """
        Get student
        """
        add_response = self.add_student(client)
        uuid = add_response.json.get("uuid")
        student_url = "/student/%s" % uuid
        response1 = client.get(student_url)
        assert response1.status_code == 200
        assert response1.content_type == "application/json"

    def test_get_student_unknown(self, client):
        """
        Get unknown student
        """
        response = client.get("/student/123")
        assert response.status_code == 422
        assert response.content_type == "application/json"
        assert response.json == json.loads('{"error": "Unknown student"}')

    def test_delete_student(self, client):
        """
        Delete student
        """
        add_response = self.add_student(client)
        uuid = add_response.json.get("uuid")
        student_url = "/student/%s" % uuid
        delete_response = client.delete(student_url)
        assert delete_response.status_code == 200
        assert delete_response.content_type == "application/json"
        assert add_response.json == delete_response.json

    def test_delete_student_unknown(self, client):
        """
        Delete unknown student
        """
        response = client.delete("/student/123")
        assert response.status_code == 422
        assert response.content_type == "application/json"
        assert response.json == json.loads('{"error": "Unknown student"}')

    def test_update_student_not_json(self, client):
        """
        Update student when content-type is not application/json
        """
        add_response = client.post("/student", data=json.dumps(TestRoutes.student_attributes))

        assert add_response.status_code == 422
        assert add_response.content_type == "application/json"
        assert add_response.json == json.loads('{"error": "Malformed data"}')

        add_response = self.add_student(client)
        uuid = add_response.json.get('uuid')
        request_body = {
            "class": "4",
            "name": "Joan",
            "sex": "female",
            "age": "2",
            "siblings": "4",
            "gpa": "4.1"
        }

        update_url = "/student/%s" % uuid
        update_response = client.put(update_url, data=json.dumps(request_body))

        assert update_response.status_code == 422
        assert update_response.content_type == "application/json"
        assert update_response.json == json.loads('{"error": "Malformed data"}')

    def test_update_student(self, client):
        """
        Update Student
        """
        add_response = self.add_student(client)
        uuid = add_response.json.get('uuid')
        request_body = {
            "class": "4",
            "name": "Joan",
            "sex": "female",
            "age": "2",
            "siblings": "4",
            "gpa": "4.1"
        }

        update_url = "/student/%s" % uuid
        update_response = client.put(update_url, json=request_body)
        assert update_response.status_code == 200
        assert update_response.content_type == "application/json"
        expected_response_body = {
            "uuid": uuid,
            "class": 4,
            "name": "Joan",
            "sex": "female",
            "age": 2,
            "siblings": 4,
            "gpa": 4.1
        }

        assert update_response.json == json.loads(json.dumps(expected_response_body))

    def test_update_student_unknown(self, client):
        """
        Update unknown student
        """
        request_body = {
            "class": "4",
            "name": "Joan",
            "sex": "female",
            "age": "2",
            "siblings": "4",
            "gpa": "4.1"
        }

        update_url = "/student/123"
        update_response = client.put(update_url, json=request_body)
        assert update_response.status_code == 422
        assert update_response.content_type == "application/json"

    @staticmethod
    def add_student(client):
        request_body = TestRoutes.student_attributes
        response = client.post("/student", json=request_body)
        return response
