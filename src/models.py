from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, SmallInteger, BigInteger
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Page(Base):
    __tablename__ = 'Page'
    page_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    url = Column(String(2083), nullable=False)
    summary = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    state = Column(SmallInteger, nullable=False, default=1)

class User(Base):
    __tablename__ = 'User'
    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    auth_id = Column(BigInteger, nullable=False)
    email = Column(String(255), nullable=False)
    user_name = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    state = Column(SmallInteger, nullable=False, default=1)
    access_token = Column(String(255))
    token_type = Column(String(255))
    expires_in = Column(String(255))
    refresh_token = Column(String(255))
    scope = Column(String(255))
    id_token = Column(String(255))

class Bookmark(Base):
    __tablename__ = 'Bookmark'
    bookmark_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    page_id = Column(Integer, ForeignKey('Page.page_id'), nullable=False)
    user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    state = Column(SmallInteger, nullable=False, default=1)
    page = relationship("Page")
    user = relationship("User")

class Content(Base):
    __tablename__ = 'Content'
    content_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.user_id'), default=0)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    state = Column(SmallInteger, nullable=False, default=1)
    user = relationship("User")
