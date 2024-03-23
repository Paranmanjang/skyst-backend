from typing import List, Optional
from datetime import datetime

from fastapi import APIRouter, Depends, Query, Path, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
# from models import
# from schemas import
# from serivce import

router = APIRouter(
    prefix="/bookmarks",
    tags=["bookmarks"],
    responses={404: {"description": "Not found"}}
)

"""
메모 적는 곳
"""


@router.post(
    "/",
    # response_model=model,
    # status_code=status.HTTP_201_CREATED,
    description="""
    - ★user_id 또는 anonymous_user_id 둘 중 하나는 반드시 입력해야 함
    - ★user_id와 anonymous_user_id 둘 다 입력할 수 없음. 둘 중 하나만 입력해야 함!!!
    - chains 폴더에 있는 파일들 완성시켜야 함
    """,
    # summary="북마크 추가",
    response_description={
        status.HTTP_201_CREATED: {
            "description": "북마크 추가 성공"
        }
    }
)
async def function_name(
    # bookmark: BookmarkCreate,
    db: Session = Depends(get_db)
):
    # return create_bookmark_service(bookmark, db)
    pass
