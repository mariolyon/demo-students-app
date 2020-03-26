from flask import request, make_response, jsonify

from app import app
from app import service
from app.dto import StudentData, dto_for_student


@app.route('/students')
def list_students():
    students = service.list_students()
    student_jsons = [dto_for_student(student).to_dict() for student in students]
    return jsonify(student_jsons)


@app.route('/student', methods=['POST'])
def add_student():
    student_data = get_student_data_from_request()
    if student_data is None:
        return make_response(dict(error="Malformed data"), 422)
    else:
        student = service.add_student(student_data)
        resp_body = dto_for_student(student).to_dict()
        return make_response(resp_body, 201)


@app.route('/student/<uuid>')
def get_student(uuid):
    student = service.get_student(uuid)
    if student is None:
        return make_response(dict(error="Unknown student"), 422)
    else:
        resp_body = dto_for_student(student).to_dict()
        return make_response(resp_body, 200)


@app.route('/student/<uuid>', methods=['DELETE'])
def delete_student(uuid):
    student = service.delete_student(uuid)
    if student is None:
        return make_response(dict(error="Unknown student"), 422)
    else:
        resp_body = dto_for_student(student).to_dict()
        return make_response(resp_body, 200)


@app.route('/student/<uuid>', methods=['PUT'])
def update_student(uuid):
    student_data = get_student_data_from_request()
    if student_data is None:
        return make_response(dict(error="Malformed data"), 422)
    else:
        student = service.update_student(uuid, student_data)
        if student is None:
            return make_response(dict(error="Unknown student"), 422)
        else:
            resp_body = dto_for_student(student).to_dict()
            return make_response(resp_body, 200)


def get_student_data_from_request():
    if request.is_json:
        request_json = request.get_json()
        return StudentData.from_dict(request_json)
    else:
        return None
