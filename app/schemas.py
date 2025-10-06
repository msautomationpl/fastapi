from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint


# ======================
# USER
# ======================
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


# ======================
# POST
# ======================
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes = True


# model dla response z liczbą głosów
class PostOut(BaseModel):
    post: Post
    votes: int

    class Config:
        from_attributes = True


# ======================
# AUTH
# ======================
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


# ======================
# VOTE
# ======================
class Vote(BaseModel):
    post_id: int
    dir: conint(ge=0, le=1)   # 0 = usuń głos, 1 = dodaj głos
