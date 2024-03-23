from typing import List, Optional
from datetime import datetime

from fastapi import APIRouter, Depends, Query, Path, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models import Bookmark, Page
from bookmarks.schemas import BookmarkCreate, BookmarkResponse
from bookmarks.service import get_bookmarks_service

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
    response_model=BookmarkResponse,
    status_code=status.HTTP_201_CREATED,
    description="북마크 추가",
    summary="북마크 추가",
    response_description={
        status.HTTP_201_CREATED: {
            "description": "북마크 추가 성공"
        }
    }
)
def create_bookmark(
    bookmark: BookmarkCreate,
    db: Session = Depends(get_db)
):
    page = db.query(Page).filter(Page.url == bookmark.url).first()
    if not page:
        # Page 만들기
        page = Page(
            title="temporay title",
            url=bookmark.url,
            summary="temporay summary",
            created_at=datetime.now(),
            state=1
        )
        db.add(page)
        db.commit()
        db.refresh(page)

    page = db.query(Page).filter(Page.url == bookmark.url).first()

    db_bookmark = Bookmark(
        page_id=page.page_id,
        user_id=bookmark.user_id,
        created_at=datetime.now(),
        state=1
    )
    db.add(db_bookmark)
    db.commit()
    db.refresh(db_bookmark)

    db_bookmark = db.query(Bookmark).filter(Bookmark.bookmark_id == db_bookmark.bookmark_id).first()

    response = BookmarkResponse(
        user_id=db_bookmark.user_id,
        url=bookmark.url,
        bookmark_id=db_bookmark.bookmark_id,
        page_id=db_bookmark.page_id,
        created_at=db_bookmark.created_at,
        title=page.title,
        summary=page.summary
    )

    return response

@router.get(
    "/newest",
    response_model=List[BookmarkResponse],
    status_code=status.HTTP_200_OK,
    description="""
    - Query Parameter는 아래와 같음.
    - offset은 몇 번째부터 데이터를 가져올지 결정. default 값은 0임. 값을 입력하지 않으면 default 값이 적용됨.
    - limit은 최대 몇 개의 데이터를 가져올지 결정. default 값은 10임. 값을 입력하지 않으면 default 값이 적용됨.
    - 테스트는 어느 정도 진행했지만, 더 많은 테스트가 필요함! db에도 더 많은 데이터를 넣어서 테스트 진행해야 함.
    """,
    summary="최신순으로 북마크 목록 조회",
    response_description={
        status.HTTP_200_OK: {
            "description": "최신순으로 북마크 목록 조회 성공"
        }
    }
)
async def get_bookmarks(
    db: Session = Depends(get_db),
    user_id: int = Query(None, description="User ID", gt=0, example=1),
    offset: int = Query(0, description="Offset of the first item to return", ge=0, example=0),
    limit: int = Query(10, description="Maximum number of items to return", ge=1, le=100, example=10),
):
    return get_bookmarks_service(db, user_id, offset, limit)


@router.get(
    "/frequent",
    response_model=List[BookmarkResponse],
    status_code=status.HTTP_200_OK,
    description="""
    - Query Parameter는 아래와 같음.
    - offset은 몇 번째부터 데이터를 가져올지 결정. default 값은 0임. 값을 입력하지 않으면 default 값이 적용됨.
    - limit은 최대 몇 개의 데이터를 가져올지 결정. default 값은 10임. 값을 입력하지 않으면 default 값이 적용됨.
    - 테스트는 어느 정도 진행했지만, 더 많은 테스트가 필요함! db에도 더 많은 데이터를 넣어서 테스트 진행해야 함.
    """,
    summary="빈도순으로 북마크 목록 조회",
    response_description={
        status.HTTP_200_OK: {
            "description": "빈도순으로 북마크 목록 조회 성공"
        }
    }
)
async def get_bookmarks(
    db: Session = Depends(get_db),
    user_id: int = Query(None, description="User ID", gt=0, example=1),
    offset: int = Query(0, description="Offset of the first item to return", ge=0, example=0),
    limit: int = Query(10, description="Maximum number of items to return", ge=1, le=100, example=10),
):
    return get_bookmarks_service(db, user_id, offset, limit)

@router.get(
    "/forgotten",
    response_model=List[BookmarkResponse],
    status_code=status.HTTP_200_OK,
    description="""
    - Query Parameter는 아래와 같음.
    - offset은 몇 번째부터 데이터를 가져올지 결정. default 값은 0임. 값을 입력하지 않으면 default 값이 적용됨.
    - limit은 최대 몇 개의 데이터를 가져올지 결정. default 값은 10임. 값을 입력하지 않으면 default 값이 적용됨.
    - 테스트는 어느 정도 진행했지만, 더 많은 테스트가 필요함! db에도 더 많은 데이터를 넣어서 테스트 진행해야 함.
    """,
    summary="망각했을 가능성이 높은 순서로 북마크 목록 조회",
    response_description={
        status.HTTP_200_OK: {
            "description": "망각했을 가능성이 높은 순서로 북마크 목록 조회 성공"
        }
    }
)
async def get_bookmarks(
    db: Session = Depends(get_db),
    user_id: int = Query(None, description="User ID", gt=0, example=1),
    offset: int = Query(0, description="Offset of the first item to return", ge=0, example=0),
    limit: int = Query(10, description="Maximum number of items to return", ge=1, le=100, example=10),
):
    return get_bookmarks_service(db, user_id, offset, limit)