from ..model.users import User

users =[{"username": "Ram","email": "ram@gmail.com"}, {"username": "Mohan", "email": "mohan@gmail.com"}]

async def get_users():
    return users

async def save_users(user: User):
    return users.append(user)

async def find_user_by_username(username: str):
    for user in users:
        print(user)
        if user['username'] == username:
            return user