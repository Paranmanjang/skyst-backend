from typing import List
from datetime import datetime

from fastapi import HTTPException, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import null

from models import Page, Bookmark
from bookmarks.schemas import BookmarkResponse, BookmarkCreate
from utils.web_crawler import get_webpage_content
from utils.ai.summarizer import generate_summary
from utils.ai.get_vector import get_embedding
from utils.ai.vector_db import upload_vector
from utils.ai.vector_db import search_vector

def post_bookmarks_service(db, bookmark: BookmarkCreate) -> dict:

    try:
        # 웹 페이지 정보 가져오기
        title, content = get_webpage_content(bookmark.url)
    except Exception as e:
        # 웹 페이지를 가져오는 데 실패한 경우
        raise HTTPException(status_code=404, detail="웹 사이트를 찾을 수 없습니다.") from e


    # content를 AI 요약 서비스에 넣어서 요약된 내용을 반환
    summary = generate_summary(content)

    # page에 page 내용이 있는지 확인
    page = db.query(Page).filter(Page.url == bookmark.url).first()
    
    # page가 없으면 page를 만든다
    if not page:
        # Page 만들기
        page = Page(
            title=title,
            url=bookmark.url,
            summary=summary,
            created_at=datetime.now(),
            state=1
        )
        db.add(page)
        db.commit()
        db.refresh(page)

        embedding = get_embedding(summary)
        vector = embedding.data[0].embedding
    
    # 사용자가 북마크한 페이지인지 확인
    db_bookmark = db.query(Bookmark).filter(Bookmark.page_id == page.page_id, Bookmark.user_id == bookmark.user_id).first()
    if db_bookmark:
        raise HTTPException(status_code=400, detail="이미 북마크한 페이지입니다.")
    
    # 북마크 추가
    db_bookmark = Bookmark(
        page_id=page.page_id,
        user_id=bookmark.user_id,
        created_at=datetime.now(),
        state=1
    )
    db.add(db_bookmark)
    db.commit()
    db.refresh(db_bookmark)

    # 북마크 정보 반환
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

def get_bookmarks_service(db, user_id: int, offset: int, limit: int) -> List[dict]:
    query = db.query(Page).join(Bookmark, Page.page_id == Bookmark.page_id).filter(Bookmark.user_id == user_id)
    query = query.filter(Page.state == 1)

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
    
    # created_at 최근 순으로 정렬
    response = sorted(response, key=lambda x: x["created_at"], reverse=True)

    # offset, limit 적용
    response = response[offset:offset+limit]

    return response







def get_related_bookmarks(keyword: str, db: Session, user_id: int, offset: int, limit: int) -> List[dict]:

    # 사용자가 작성한 글의 내용을 가져온다
    content = keyword

    # 글을 embedding 한다
    embedding = get_embedding(content)
    vector = embedding.data[0].embedding

    # vector db에 넣어서 top_k result를 가져온다
    results = search_vector(vector, 10)

    # results에는 page_id가 들어있다
    # page_id를 이용해서 page 정보와 bookmark 정보를 가져온다
    recommended_pages = []
    for result in results:
        page = db.query(Page).filter(Page.page_id == result).first()
        bookmark = db.query(Bookmark).filter(Bookmark.page_id == result).first()

        recommended_pages.append({
            "bookmark_id": bookmark.bookmark_id,
            "page_id": page.page_id,
            "created_at": bookmark.created_at,
            "title": page.title,
            "summary": page.summary,
            "url": page.url,
            "user_id": bookmark.user_id
        })

    # offset, limit 적용
    recommended_pages = recommended_pages[offset:offset+limit]

    return recommended_pages