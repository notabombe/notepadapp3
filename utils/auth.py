```python
from flask import request, g
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired
from notepad_app.models.notepad import User
from notepad_app import app

def generate_auth_token(user_id, expiration=600):
    s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({'id': user_id})

def verify_auth_token(token):
    s = Serializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except SignatureExpired:
        return None    # valid token, but expired
    except BadSignature:
        return None    # invalid token
    user = User.query.get(data['id'])
    return user

def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Missing token'}), 403
        user = verify_auth_token(token)
        if not user:
            return jsonify({'message': 'Invalid token'}), 403
        g.user = user
        return f(*args, **kwargs)
    return decorated_function
```