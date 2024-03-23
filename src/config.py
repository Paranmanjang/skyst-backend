# global configs

from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings

dotenv_path_1 = "../.env"
dotenv_path_2 = ".env"
load_dotenv(dotenv_path_1)
load_dotenv(dotenv_path_2)


class DB_Settings(BaseSettings):
    db_db: str = os.getenv("DB_DB")
    db_host: str = os.getenv("DB_HOST")
    db_password: str = os.getenv("DB_PASSWORD")
    db_port: int = os.getenv("DB_PORT")
    db_user: str = os.getenv("DB_USER")

class GenAI_Settings(BaseSettings):
    openai_api_key: str = os.getenv("OPENAI_API_KEY")
    pinecone_api_key: str = os.getenv("PINECONE_API_KEY")


class Google_Settings(BaseSettings):
    google_client_id: str = os.getenv("TEST_GOOGLE_CLIENT_ID")
    google_client_secret: str = os.getenv("TEST_CLIENT_SECRET")
    google_project_id: str = os.getenv("TEST_PROJECT_ID")
    google_auth_uri: str = os.getenv("TEST_AUTH_URI")
    google_token_uri: str = os.getenv("TEST_TOKEN_URI")
    google_auth_provider_x509_cert_url: str = os.getenv(
        "TEST_AUTH_PROVIDER_X509_CERT_URL")
    google_redirect_uris: str = os.getenv("TEST_REDIRECT_URIS")


# # access token
# class JWT_Settings(BaseSettings):
#     jwt_secret_key: str = os.getenv("JWT_SECRET_KEY")
#     jwt_algorithm: str = os.getenv("JWT_ALGORITHM")
#     access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
#     refresh_token_expire_minutes: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES"))

# class OPENAI_Settings(BaseSettings):
#     openai_api_key: str = os.getenv("OPENAI_API_KEY")

# class DAJEONG_Settings(BaseSettings):
#     dajeong_api_key: str = os.getenv("DAJEONG_API_KEY")
#     test_api_key : str = os.getenv("TEST_API_KEY")


# https://medium.com/@mohit_kmr/production-ready-fastapi-application-from-0-to-1-part-3-a1ff8c700d9c
# https://www.linkedin.com/pulse/dotenv-files-app-security-fastapi-prince-odoi/
