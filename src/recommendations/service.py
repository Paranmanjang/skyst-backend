from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import null

from models import Bookmark, Content
from recommendations.schemas import RecommendationRequest


def get_recommendations_service(request: RecommendationRequest, db: Session):

    content = request.content

    response = {
        "recommended_pages": [
            {
                "url": "https://mindorizip.tistory.com",
                "user_id": 1,
                "title": "Mindorizip",
                "page_id": 1,
                "bookmark_id": 1,
                "summary": "마음의 소리"
            },
            {
                "url": "https://www.google.com",
                "user_id": 1,
                "title": "Google",
                "page_id": 2,
                "bookmark_id": 2,
                "summary": "구글"
            },
            {
                "url": "https://www.naver.com",
                "user_id": 1,
                "title": "Naver",
                "page_id": 3,
                "bookmark_id": 3,
                "summary": "네이버"
            },
            {
                "url": "https://www.daum.net",
                "user_id": 1,
                "title": "Daum",
                "page_id": 4,
                "bookmark_id": 4,
                "summary": "다음"
            }
        ]
    }

    return response
