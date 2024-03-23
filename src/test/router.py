from typing import List, Optional
from datetime import datetime

from fastapi import APIRouter, Depends, Query, Path, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models import Test
from test.schemas import TestResponse
# from serivce import

from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/test",
    tags=["test"],
    responses={404: {"description": "Not found"}}
)

"""
메모 적는 곳
"""


@router.get(
    "/db-test",
    response_model=List[TestResponse],
    status_code=status.HTTP_201_CREATED,
    description="DB 테스트",
    summary="DB 테스트",
    response_description={
        status.HTTP_201_CREATED: {
            "description": "DB 테스트 성공"
        }
    }
)
async def function_name(
    db: Session = Depends(get_db)
):
    # 전부 가져오기
    tests = db.query(Test).all()

    response = []
    for test in tests:
        response.append({
            "test_id": test.test_id,
            "user_id": test.user_id
        }
        )

    return response
