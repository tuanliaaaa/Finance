from BaseRepo import BaseRepo
class UserRepo(BaseRepo):
    def add_user(self, user_id: int, username: str, email: str, role: str = "user"):
        user = {
            'user_id': user_id,
            'username': username,
            'email': email,
            'role': role
        }
        self.add(user)

    def update_user(self, user_id: int, username: str = None, email: str = None, role: str = None):
        updates = {}
        if username is not None:
            updates['username'] = username
        if email is not None:
            updates['email'] = email
        if role is not None:
            updates['role'] = role

        self.update('user_id', user_id, updates)

    def delete_user(self, user_id: int):
        self.delete('user_id', user_id)


