```python
from flask import Flask
from .config import Config
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    from .routes import notepad as notepad_blueprint
    app.register_blueprint(notepad_blueprint)

    return app
```