from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel, Field


class UserInfo(BaseModel):
    pass


class RecommendationRequest(BaseModel):
    content: str = Field(..., title="content", description="content", example="contentcontentcontentcontent")


class BookmarkBase(BaseModel):
    user_id: Optional[int] = Field(default=None, title="user_id", description="북마크한 사용자의 user_id", example=1, ge=0)
    url: str = Field(..., title="url", description="북마크한 페이지의 url", example="https://mindorizip.tistory.com")
    title: Optional[str] = Field(default=None, title="title", description="북마크한 페이지의 title", example="마음의 소리")
    page_id: int = Field(..., title="page_id", description="북마크한 페이지의 page_id", example=1, ge=1)
    bookmark_id: int = Field(..., title="bookmark_id", description="북마크 id", example=1, ge=1)
    summary: Optional[str] = Field(default=None, title="summary", description="북마크한 페이지의 summary", example="마음의 소리")


class RecommendationResponse(BaseModel):
    recommended_pages: List[BookmarkBase]
