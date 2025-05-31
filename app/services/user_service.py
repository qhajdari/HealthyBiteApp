from app.models.user_models import RegularUser, PremiumUser, AdminUser

# DB simulation
users = {
    "regular": {"user": RegularUser("regular"), "password": "123456"},
    "premium": {"user": PremiumUser("premium"), "password": "123456"},
    "admin": {"user": AdminUser("admin"), "password": "123456"},
}

def authenticate(username, password):
    record = users.get(username)
    if record and record['password'] == password:
        return record['user']
    return None
