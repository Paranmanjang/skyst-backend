from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, UniqueConstraint, Index, BigInteger, SmallInteger
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

# TODO: 양방향 관계로 수정


class Test(Base):
    __tablename__ = 'Test'
    test_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)


class Page(Base):
    __tablename__ = 'Page'
    page_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=True)
    english_title = Column(String(255), nullable=True)
    url = Column(String(512), nullable=False, unique=True)
    summarization = Column(Text, nullable=False)
    created_at = Column(DateTime(3), nullable=False, server_default=func.current_timestamp(3))
    state = Column(SmallInteger, nullable=False, default=1)
    view_count = Column(Integer, nullable=True, default=0)  # Unused
    favicon = Column(String(255), nullable=True)  # Unused
    category = Column(Integer, nullable=True)  # Unused


class User(Base):
    __tablename__ = 'User'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False, unique=True)
    user_name = Column(String(255), nullable=True)
    auth_type = Column(SmallInteger, nullable=False, default=1)
    auth_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime(3), nullable=False, server_default=func.current_timestamp(3))
    state = Column(SmallInteger, nullable=False, default=1)
    __table_args__ = (UniqueConstraint('auth_type', 'auth_id'), Index('auth_index', 'auth_type', 'auth_id'))


class AnonymousUser(Base):
    __tablename__ = 'AnonymousUser'
    anonymous_user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_ip = Column(String(255), nullable=False, unique=True)
    created_at = Column(DateTime(3), nullable=False, server_default=func.current_timestamp(3))
    state = Column(SmallInteger, nullable=False, default=1)


class Bookmark(Base):
    __tablename__ = 'Bookmark'
    bookmark_id = Column(Integer, primary_key=True, autoincrement=True)
    page_id = Column(Integer, ForeignKey('Page.page_id'), nullable=False, default=0)
    user_id = Column(Integer, ForeignKey('User.user_id'), nullable=True, default=0)
    anonymous_user_id = Column(Integer, ForeignKey('AnonymousUser.anonymous_user_id'), nullable=True, default=0)
    state = Column(SmallInteger, nullable=False, default=1)
    created_at = Column(DateTime(3), nullable=False, server_default=func.current_timestamp(3))
    updated_at = Column(DateTime(3), nullable=False, server_default=func.current_timestamp(3), onupdate=func.current_timestamp(3))
    notes = Column(Text, nullable=False)
    page = relationship("Page")
    user = relationship("User")
    anonymous_user = relationship("AnonymousUser")


class Content(Base):
    __tablename__ = 'Content'
    content_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.user_id'), nullable=True, default=0)
    anonymous_user_id = Column(Integer, ForeignKey('AnonymousUser.anonymous_user_id'), nullable=True, default=0)
    title = Column(String(255), nullable=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(3), nullable=False, server_default=func.current_timestamp(3))
    updated_at = Column(DateTime(3), nullable=False, server_default=func.current_timestamp(3), onupdate=func.current_timestamp(3))
    state = Column(SmallInteger, nullable=False, default=1)
    doc_id = Column(String(255), nullable=True, default=None)

    # 새로 추가
    token_type = Column(String(255), nullable=True, default=None)
    expires_in = Column(String(255), nullable=True, default=None)
    refresh_token = Column(String(255), nullable=True, default=None)
    scope = Column(String(255), nullable=True, default=None)
    id_token = Column(String(255), nullable=True, default=None)
    ######

    user = relationship("User")
    anonymous_user = relationship("AnonymousUser")
