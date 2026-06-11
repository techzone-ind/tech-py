from ..model.users import User

users =[{"username": "Ram","email": "ram@gmail.com"}, {"username": "Mohan", "email": "mohan@gmail.com"}]

async def get_users():
    return users

async def save_users(user: User):
     users.append(user)
     return user

async def find_user_by_username(username: str):
    for user in users:
        if user['username'] == username:
            return user
        
async def find_user_by_email(email: str):
    for user in users:
        if user['email'] == email:
            return user
    