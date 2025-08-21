from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional


# ======================
# USER
# ======================
class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# ======================
# MOVIE
# ======================
class MovieBase(BaseModel):
    title: str
    description: Optional[str] = None
    release_year: Optional[int] = None


class MovieCreate(MovieBase):
    pass


class MovieResponse(MovieBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# ======================
# LIST
# ======================
class ListBase(BaseModel):
    name: str
    description: Optional[str] = None


class ListCreate(ListBase):
    pass


class ListResponse(ListBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True


# ======================
# RATING
# ======================
class RatingBase(BaseModel):
    rating: int
    comment: Optional[str] = None


class RatingCreate(RatingBase):
    movie_id: int


class RatingResponse(RatingBase):
    id: int
    user_id: int
    movie_id: int
    created_at: datetime

    class Config:
        from_attributes = True


# ======================
# LIST_MOVIE (Pivot)
# ======================
class ListMovieBase(BaseModel):
    list_id: int
    movie_id: int


class ListMovieCreate(ListMovieBase):
    pass


class ListMovieResponse(ListMovieBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
