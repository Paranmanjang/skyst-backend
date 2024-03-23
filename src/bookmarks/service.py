from typing import List
from datetime import datetime

from fastapi import HTTPException, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import null

from models import Page, Bookmark
# from schemas import
# from utils import

def get_bookmarks_service(db, user_id: int, offset: int, limit: int) -> List[dict]:
    query = db.query(Page).join(Bookmark, Page.page_id == Bookmark.page_id).filter(Bookmark.user_id == user_id)
    query = query.filter(Page.state == 1).offset(offset).limit(limit)

    db_pages = query.all()

    response = []
    for db_page in db_pages:
        db_bookmark = db.query(Bookmark).filter(Bookmark.page_id == db_page.page_id).first()

        if db_bookmark:
            response.append({
                "user_id": db_bookmark.user_id,
                "url": db_page.url,
                "title": db_page.title,
                "page_id": db_page.page_id,
                "bookmark_id": db_bookmark.bookmark_id,
                "created_at": db_bookmark.created_at,
                "summary": db_page.summary
            })

    return response