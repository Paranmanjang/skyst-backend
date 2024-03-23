from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel, Field


class BookmarkBase(BaseModel):
    user_id: int = Field(..., title="user_id", description="북마크한 사용자의 user_id", example=1, ge=0)
    url: str = Field(..., title="url", description="북마크한 페이지의 url", example="https://mindorizip.tistory.com")

class BookmarkCreate(BookmarkBase):
    pass


class BookmarkResponse(BookmarkBase):
    bookmark_id: int = Field(..., title="bookmark_id", description="북마크 id", example=1, ge=1)
    page_id: int = Field(..., title="page_id", description="북마크한 페이지의 page_id", example=1, ge=1)
    created_at: datetime = Field(..., title="created_at", description="북마크 생성일", example="2024-10-16 00:00:00")
    title: Optional[str] = Field(default=None, title="title", description="북마크한 페이지의 title", example="마음의 소리")
    summarization: Optional[str] = Field(default=None, title="summarization", description="북마크한 페이지의 summarization", example="마음의 소리")

class BookmarkList(BaseModel):
    bookmarks: List[BookmarkResponse]
