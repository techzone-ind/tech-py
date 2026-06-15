
# -----------------------------------------------------------------------------
# Script Name: main.py
# Author:      Animesh Sinha
# Description: FastAPI app.
# --

# Lib imports
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from .middleware.token_processor_middleware import TokenProcessorMiddleware
from .routers import  users

app = FastAPI(title="FastAPI demo");

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(TokenProcessorMiddleware)

app.include_router(users.router)


@app.get("/")
def get_welcome_msg():
    return {'msg' : 'Welcome to FastAPI'}

