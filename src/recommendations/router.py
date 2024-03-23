from typing import List, Optional
from datetime import datetime

from fastapi import APIRouter, Depends, Body, Path, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from recommendations.schemas import RecommendationRequest, RecommendationResponse, BookmarkBase
from recommendations.service import get_recommendations_service

router = APIRouter(
    prefix="/recommendations",
    tags=["recommendations"],
    responses={404: {"description": "Not found"}}
)


@router.post(
    "/",
    response_model=RecommendationResponse,
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
    # 사용자 정보를 가지고 구글 드라이브에 접속한다
    # content_id를 가지고 온다
    # 수정 사항을 embedding한다
    # vector db에서 가장 가까운 n개의 문서를 가지고 온다
    # n 개의 문서 중 유사도가 일정 수치 이하인 문서는 제외한다
    # 가지고 온 문서들을 사용자에게 보여준다

    return get_recommendations_service(request, db)
