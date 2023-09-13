```python
from datetime import datetime
from notepad_app.models.notepad import Notepad

class NotepadService:
    @staticmethod
    def create_notepad(title, content):
        notepad = Notepad(
            title=title,
            content=content,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        notepad.save()
        return notepad

    @staticmethod
    def get_notepad(id):
        notepad = Notepad.query.get(id)
        if not notepad:
            raise Exception("Notepad not found")
        return notepad

    @staticmethod
    def update_notepad(id, title, content):
        notepad = NotepadService.get_notepad(id)
        notepad.title = title
        notepad.content = content
        notepad.updated_at = datetime.now()
        notepad.save()
        return notepad

    @staticmethod
    def delete_notepad(id):
        notepad = NotepadService.get_notepad(id)
        notepad.delete()

    @staticmethod
    def list_notepads():
        return Notepad.query.all()
```