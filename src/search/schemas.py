from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel, Field

# 아래는 모두 example


class ExampleBase(BaseModel):
    url_example: str = Field(..., title="url", description="북마크한 페이지의 url", example="https://mindorizip.tistory.com")
    user_id: Optional[int] = Field(default=None, title="user_id", description="북마크한 사용자의 user_id", example=1, ge=0)
    anonymous_user_id: Optional[int] = Field(default=None, title="anonymous_user_id", description="북마크한 사용자의 익명 user_id", example=1, ge=0)


class ExampleCreate(ExampleBase):
    pass


class ExampleResponse(ExampleBase):
    bookmark_id: int = Field(..., title="bookmark_id", description="북마크 id", example=1, ge=1)
    page_id: int = Field(..., title="page_id", description="북마크한 페이지의 page_id", example=1, ge=1)
    created_at: datetime = Field(..., title="created_at", description="북마크 생성일", example="2024-10-16 00:00:00")
    updated_at: datetime = Field(..., title="updated_at", description="북마크 수정일", example="2024-10-16 00:00:00")
    title: Optional[str] = Field(default=None, title="title", description="북마크한 페이지의 title", example="마음의 소리")
    summarization: Optional[str] = Field(default=None, title="summarization", description="북마크한 페이지의 summarization", example="마음의 소리")


class ExampleList(BaseModel):
    bookmarks: List[ExampleResponse]


class ExampleUpdate(ExampleBase):
    pass


class ExampleDelete(BaseModel):
    bookmark_id: int = Field(..., title="bookmark_id", description="북마크 id", example=1, ge=1)
