```python
from flask import Flask
from notepad_app.config import Config
from notepad_app.routes import notepad_routes

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(notepad_routes.bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
```