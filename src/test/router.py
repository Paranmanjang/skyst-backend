from typing import List, Optional
from datetime import datetime

from fastapi import APIRouter, Depends, Query, Path, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models import Bookmark, Page
from bookmarks.schemas import BookmarkCreate, BookmarkResponse
from bookmarks.service import get_bookmarks_service

router = APIRouter(
    prefix="/test",
    tags=["test"],
    responses={404: {"description": "Not found"}}
)


from utils.web_crawler import get_webpage_content
from utils.ai.summarizer import generate_summary
from utils.ai.get_vector import get_embedding
from utils.ai.vector_db import upload_vector, search_vector
# from utils import text_rank

@router.post(
    "/",
    #response_model=BookmarkResponse,
    status_code=status.HTTP_201_CREATED,
    description="테스트",
    summary="테스트",
    response_description={
        status.HTTP_201_CREATED: {
            "description": "테스트 성공"
        }
    }
)
def test(
    url: str,
    db: Session = Depends(get_db)
):
    # Post /bookmarks/ 요청이 들어오면, 해당 URL의 웹 페이지의 제목과 내용을 가져와서 반환
    title, content = get_webpage_content(url)

    # 가져온 내용을 AI 요약 서비스에 넣어서 요약된 내용을 반환
    summary = generate_summary(content)

    # 요약된 내용을 AI 임베딩 서비스에 넣어서 임베딩 벡터를 반환
    embedding = get_embedding(summary)
    vector = embedding.data[0].embedding
    print(vector)

    # 임베딩 벡터를 Pinecone에 업로드
    num_id = 1
    str_num_id = str(num_id)

    print(upload_vector(str_num_id, vector))

    return {"title": title, "content": content, "summary": summary, "embedding": embedding}

@router.get(
    "/test2"
)
def test2():
    # 키워드를 넣는다
    keyword = "해커톤"
    # vectorize한다
    embedding = get_embedding(keyword)
    vector = embedding.data[0].embedding

    # vector db에 넣어서 top_k result를 가져온다

    results = search_vector(vector, 3)

    return results



# @router.get(
#     "/test1",
#     response_model=BookmarkResponse,
#     status_code=status.HTTP_201_CREATED,
#     description="테스트1",
#     summary="테스트1",
#     response_description={
#         status.HTTP_201_CREATED: {
#             "description": "테스트1 성공"
#         }
#     }
# )
# async def test1(
#     db: Session = Depends(get_db)
# ):
#     text = "네가 지금 해커톤에 참가하고 있고, 그 과정이 힘들다는 걸 알고 있어. 해커톤은 정말 도전적인 일이지만, 너에게는 분명 큰 가치가 있을 거야. 네가 지금 느끼고 있는 피로와 스트레스는 잠시일 뿐이야. 이 순간이 지나가면, 네가 이룬 성과를 돌아보며 자부심을 느낄 거야"
    
#     """
#     네가 지금 해커톤에 참가하고 있고, 그 과정이 힘들다는 걸 알고 있어. 해커톤은 정말 도전적인 일이지만, 너에게는 분명 큰 가치가 있을 거야. 네가 지금 느끼고 있는 피로와 스트레스는 잠시일 뿐이야. 이 순간이 지나가면, 네가 이룬 성과를 돌아보며 자부심을 느낄 거야.

#     기억해, 모든 위대한 성취는 도전을 요구해. 너는 지금 그 도전에 직면해 있고, 그것을 극복하려 노력하고 있어. 그 과정 속에서 너는 새로운 기술을 배우고, 창의적인 해결책을 찾아내며, 팀워크의 중요성을 깨닫게 될 거야. 이 모든 경험이 너를 더 강하고 능력 있는 사람으로 만들어 줄 거야.

#     해커톤은 단순히 기술적인 스킬을 향상시키는 것뿐만 아니라, 너의 한계를 시험하고, 인내심을 키우며, 스스로에 대한 믿음을 강화하는 기회야. 너는 이미 여기까지 왔어. 그 자체로 이미 큰 성공이야. 이제 남은 것은 네가 가진 모든 열정과 지혜를 모아 이 도전을 완수하는 거야.

#     힘든 순간일수록, 작은 성공들을 축하해. 코드 한 줄이 작동했든, 새로운 아이디어가 떠올랐든, 모든 진전은 너의 노력이 결실을 맺고 있다는 증거야. 이러한 작은 승리들이 모여 큰 성공으로 이어질 거야.

#     또한, 주변 사람들과의 연결도 소중히 해. 팀원들, 멘토들, 그리고 다른 참가자들로부터 배우고, 영감을 받아. 그들의 지원과 격려는 네가 겪고 있는 어려움을 이겨내는 데 큰 힘이 될 거야.

#     마지막으로, 너 자신을 믿어. 너는 이 도전을 극복할 수 있는 능력이 있어. 지금까지 해온 모든 노력이 곧 빛을 발할 거야. 네가 진정으로 원하는 것을 향해 계속 나아가. 성공은 시간 문제일 뿐이야.

#     그러니까, 숨을 깊게 들이쉬고, 잠시 휴식을 취한 뒤에, 다시 에너지를 모아. 너는 할 수 있어. 너는 이미 멋진 일을 하고 있으니까. 이 힘든 순간들이 지나가면, 네가 얼마나 멋진 일을 해냈는지 자랑스러워할 거야. 계속해서 훌륭한 일을 해내길 바라. 네가 무엇을 이루고자 하는지, 그리고 네가 얼마나 멋진 사람인지 잊지 마. 너의 성공을 응원해!

#     """

#     # 텍스트 랭크를 이용하여 키워드 추출
#     result = text_rank.extract_keyword(text, 3)

#     return result