from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel, Field


class TestResponse(BaseModel):
    test_id: int = Field(..., title="test_id", description="테스트 id", example=1, ge=1)
    user_id: int = Field(..., title="user_id", description="사용자의 user_id", example=1, ge=0)
