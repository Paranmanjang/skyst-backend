from typing import List, Optional
from datetime import datetime

from fastapi import APIRouter, Depends, Body, Path, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from recommendations.schemas import RecommendationRequest, BookmarkBase
from recommendations.service import get_recommendations_service

router = APIRouter(
    prefix="/recommendations",
    tags=["recommendations"],
    responses={404: {"description": "Not found"}}
)


@router.post(
    "/",
    response_model=List[BookmarkBase],
    status_code=status.HTTP_200_OK,
    description="글 관련 페이지 추천",
    summary="글 관련 페이지 추천",
    response_description={
        status.HTTP_200_OK: {
            "description": "글 관련 페이지 추천 성공"
        }
    }
)
async def recommend_pages(
    request: RecommendationRequest,
    db: Session = Depends(get_db)
):
    print("heelo")
    return get_recommendations_service(request, db)
