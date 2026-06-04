
# -----------------------------------------------------------------------------
# Script Name: main.py
# Author:      Animesh Sinha
# Description: FastAPI app.
# --

# Lib imports
from fastapi import FastAPI

app = FastAPI(title="FastAPI demo");

@app.get("/")
def get_welcome_msg():
    return {'msg' : 'Welcome to FastAPI'}

