from datetime import datetime

from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import null

# from models import
# from schemas import
# from utils import


class ExampleCreate():
    pass


def create_or_get_example(db: Session, example: ExampleCreate, user_id: int = None, anonymous_user_id: int = None):
    response = []
    return response
