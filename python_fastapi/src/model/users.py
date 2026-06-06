# -----------------------------------------------------------------------------
# Author:      Animesh Sinha
# Description: FastAPI app pydantic model example.
# --

from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    sport: str
    location: str | None = None

class UserRequest(User):
    password: str

class UserResponse(BaseModel):
    username: str
    email: str