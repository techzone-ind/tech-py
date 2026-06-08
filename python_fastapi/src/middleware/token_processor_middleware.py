# -----------------------------------------------------------------------------
# Author:      Animesh Sinha
# Description: FastAPI app middleware example.
# --

from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import time

class TokenProcessorMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Process-Token"] = str("test")
        
        return response

