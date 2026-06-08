# -----------------------------------------------------------------------------
# Author:      Animesh Sinha
# Description: FastAPI app router example.
# --
from fastapi import APIRouter, Depends
from ..model.users import UserRequest, UserResponse
from ..services.users import get_users, save_users, find_user_by_username, find_user_by_email

from ..dependencies.token_validator import get_header_token

router = APIRouter()



@router.get("/users/", tags=["users"])
async def read_users():
    return await get_users()


@router.post("/users/", tags=["users"])
async def create_user(user: UserRequest):
    return await save_users(user.model_dump())


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    user = await find_user_by_username(username)
    userRes = UserResponse(username=user['username'],email=user['email'])
    return userRes

@router.get("/users/profile/{email}", tags=["users"],
    dependencies=[Depends(get_header_token)])
async def read_user(email: str):
    user = await find_user_by_email(email)
    userRes = UserResponse(username=user['username'],email=user['email'])
    return userRes

