from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional


# ======================
# TOKEN
# ======================
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: int
    email: str
# ======================
# USER
# ======================
class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime
    access_token: str  # Add this field
    token_type: str = "bearer"

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
# SEARCH_MOVIE
# ======================
class MovieSearchResult(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    release_date: Optional[datetime] = None
    poster_path: Optional[str] = None
    vote_average: Optional[float] = None
    vote_count: Optional[int] = None
    
    class Config:
        from_attributes = True

class SearchResponse(BaseModel):
    results: List[MovieSearchResult]
    total_count: int
    page: int
    total_pages: int

class SearchQuery(BaseModel):
    query: str
    page: int = 1
    limit: int = 20

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
