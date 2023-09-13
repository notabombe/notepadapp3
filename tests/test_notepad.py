```python
import unittest
from notepad_app.main import app
from notepad_app.models.notepad import Notepad
from notepad_app.services.notepad_service import NotepadService

class TestNotepad(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.notepad_service = NotepadService()

    def test_create_notepad(self):
        response = self.app.post('/api/v1/notepad/create', json={"title": "Test", "content": "This is a test"})
        self.assertEqual(response.status_code, 200)

    def test_read_notepad(self):
        notepad = self.notepad_service.create_notepad("Test", "This is a test")
        response = self.app.get(f'/api/v1/notepad/read/{notepad.id}')
        self.assertEqual(response.status_code, 200)

    def test_update_notepad(self):
        notepad = self.notepad_service.create_notepad("Test", "This is a test")
        response = self.app.put(f'/api/v1/notepad/update/{notepad.id}', json={"title": "Updated", "content": "This is an updated test"})
        self.assertEqual(response.status_code, 200)

    def test_delete_notepad(self):
        notepad = self.notepad_service.create_notepad("Test", "This is a test")
        response = self.app.delete(f'/api/v1/notepad/delete/{notepad.id}')
        self.assertEqual(response.status_code, 200)

    def test_list_notepads(self):
        response = self.app.get('/api/v1/notepad/list')
        self.assertEqual(response.status_code, 200)

    def test_unsuccessful_operations(self):
        response = self.app.post('/api/v1/notepad/create', json={"title": "", "content": ""})
        self.assertEqual(response.status_code, 400)

        response = self.app.get('/api/v1/notepad/read/123')
        self.assertEqual(response.status_code, 404)

        response = self.app.put('/api/v1/notepad/update/123', json={"title": "Updated", "content": "This is an updated test"})
        self.assertEqual(response.status_code, 404)

        response = self.app.delete('/api/v1/notepad/delete/123')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
```