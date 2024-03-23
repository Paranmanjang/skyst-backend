#  RUN ::
#  uvicorn main:app --reload
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from auth.router import router as auth_router
from auth.router import router as auth_router
from bookmarks.router import router as bookmarks_router
from contents.router import router as contents_router
from keywords.router import router as keywords_router
from search.router import router as search_router
from users.router import router as users_router
from test.router import router as test_router

app = FastAPI(
    title="GALPY",
    description="파란만장 팀의 SKYST 프로젝트의 API 문서",
    version="0.1.0",
    terms_of_service="",
    contact={
        "name": "mjkweon17",
        "url": "https://github.com/mjkweon17",
        "email": "mjkweon17@gmail.com"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT"
    }
)

# 라우터 등록
# app.include_router(auth_router)
# app.include_router(bookmarks_router)
# app.include_router(contents_router)
# app.include_router(keywords_router)
# app.include_router(search_router)
# app.include_router(users_router)
app.include_router(test_router)

# CORS 설정
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://127.0.0.1:8000/",
    "https://love-skyst.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # allow cookie  (JWT)
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    result = {"파란만장 화이팅!"}
    return result
