# -----------------------------------------------------------------------------
# Author:      Animesh Sinha
# Description: FastAPI app dependencies example.
# --

from fastapi import Request, Header, HTTPException

async def get_header_token(request: Request):
    if request.headers.get('X-Process-Token') != "test":
        raise HTTPException(status_code=400, detail="No Process-Token provided")