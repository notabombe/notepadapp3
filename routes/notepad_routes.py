```python
from flask import Blueprint, request, jsonify
from notepad_app.services.notepad_service import NotepadService
from notepad_app.utils.auth import authenticate

notepad_routes = Blueprint('notepad_routes', __name__)

@notepad_routes.route('/api/v1/notepad/create', methods=['POST'])
@authenticate
def create_notepad():
    data = request.get_json()
    result = NotepadService.create_notepad(data)
    return jsonify(result), 201

@notepad_routes.route('/api/v1/notepad/read/<id>', methods=['GET'])
@authenticate
def read_notepad(id):
    result = NotepadService.read_notepad(id)
    return jsonify(result), 200

@notepad_routes.route('/api/v1/notepad/update/<id>', methods=['PUT'])
@authenticate
def update_notepad(id):
    data = request.get_json()
    result = NotepadService.update_notepad(id, data)
    return jsonify(result), 200

@notepad_routes.route('/api/v1/notepad/delete/<id>', methods=['DELETE'])
@authenticate
def delete_notepad(id):
    result = NotepadService.delete_notepad(id)
    return jsonify(result), 200

@notepad_routes.route('/api/v1/notepad/list', methods=['GET'])
@authenticate
def list_notepads():
    result = NotepadService.list_notepads()
    return jsonify(result), 200
```