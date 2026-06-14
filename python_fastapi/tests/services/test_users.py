# -----------------------------------------------------------------------------
# Author:      Animesh Sinha
# Description: FastAPI services unit test example.
# --
import pytest
from unittest.mock import MagicMock
from src.services.users import get_users

# 1. Pure Unit Test for Service Layer (No Server required)
@pytest.mark.asyncio
async def test_create_user_success():
    result = await get_users()
    assert result[0] == {"username": "Ram","email": "ram@gmail.com"}

