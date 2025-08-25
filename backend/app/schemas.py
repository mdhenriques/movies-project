from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import List, Optional, Dict, Any


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
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    is_public: bool = False
    list_type: str = Field("custom", pattern="^(watchlist|favorites|custom)$")

class ListCreate(ListBase):
    pass

class ListUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    is_public: Optional[bool] = None

class ListResponse(ListBase):
    id: int
    user_id: int
    movie_count: int = 0  # Make it optional with default value
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
# ListMovie Schemas
class ListMovieBase(BaseModel):
    movie_id: int
    notes: Optional[str] = Field(None, max_length=1000)
    position: Optional[int] = Field(0, ge=0)

class ListMovieCreate(ListMovieBase):
    pass

class ListMovieResponse(ListMovieBase):
    id: int
    list_id: int
    added_at: datetime
    movie_title: str
    movie_poster: Optional[str]

    class Config:
        from_attributes = True

# Movie with list context
class MovieWithListContext(BaseModel):
    movie: Dict[str, Any]
    in_watchlist: bool
    in_favorites: bool
    custom_lists: List[str]


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

