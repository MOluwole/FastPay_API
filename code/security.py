from werkzeug.security import safe_str_cmp
from models.user import User

def authenticate(user_id, password):
    user = User.find_by_user_id(user_id)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
