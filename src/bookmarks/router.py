from typing import List, Optional
from datetime import datetime

from fastapi import APIRouter, Depends, Query, Path, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models import Bookmark, Page
from bookmarks.schemas import BookmarkCreate, BookmarkResponse

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
        summarization=page.summary
    )

    return response