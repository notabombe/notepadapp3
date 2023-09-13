```python
from flask import Blueprint
from .notepad_routes import notepad_blueprint

def register_routes(app):
    app.register_blueprint(notepad_blueprint, url_prefix='/api/v1/notepad')
```