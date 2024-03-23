from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import null

from models import Bookmark, Page, Content
from recommendations.schemas import RecommendationRequest
from utils.ai.get_vector import get_embedding
from utils.ai.vector_db import search_vector


def get_recommendations_service(request: RecommendationRequest, db: Session):

    # 사용자가 작성한 글의 내용을 가져온다
    content = request.essay

    # 글을 embedding 한다
    embedding = get_embedding(content)
    vector = embedding.data[0].embedding

    # vector db에 넣어서 top_k result를 가져온다
    results = search_vector(vector, 3)

    # results에는 page_id가 들어있다
    # page_id를 이용해서 page 정보와 bookmark 정보를 가져온다
    recommended_pages = []
    for result in results:
        page = db.query(Page).filter(Page.page_id == result).first()
        bookmark = db.query(Bookmark).filter(Bookmark.page_id == result).first()

        recommended_pages.append({
            "url": page.url,
            "user_id": bookmark.user_id,
            "title": page.title,
            "page_id": page.page_id,
            "bookmark_id": bookmark.bookmark_id,
            "summary": page.summary
        })

    return recommended_pages
