
# -----------------------------------------------------------------------------
# Script Name: main.py
# Author:      Animesh Sinha
# Description: FastAPI app.
# --

# Lib imports
from fastapi import FastAPI

from .routers import  users

app = FastAPI(title="FastAPI demo");

app.include_router(users.router)


@app.get("/")
def get_welcome_msg():
    return {'msg' : 'Welcome to FastAPI'}

