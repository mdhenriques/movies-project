# routes/search.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from app.database import get_db
from app.schemas import SearchResponse, SearchQuery
from app.services.search_service import SearchService

router = APIRouter(prefix="/search", tags=["search"])

@router.get("/movies", response_model=SearchResponse)
async def search_movies(
    q: str = Query(..., min_length=1, description="Search query"),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(20, ge=1, le=100, description="Results per page"),
    db: Session = Depends(get_db)
):
    """
    Search movies by title
    
    - **q**: Search query (minimum 1 character)
    - **page**: Page number (default: 1)
    - **limit**: Results per page (max: 100)
    """
    if len(q.strip()) == 0:
        raise HTTPException(
            status_code=400, 
            detail="Search query cannot be empty"
        )
    
    service = SearchService(db)
    return service.search_movies(q, page, limit)

@router.post("/movies", response_model=SearchResponse)
async def search_movies_post(
    search_query: SearchQuery,
    db: Session = Depends(get_db)
):
    """
    Search movies using POST request with JSON body
    """
    if len(search_query.query.strip()) == 0:
        raise HTTPException(
            status_code=400, 
            detail="Search query cannot be empty"
        )
    
    service = SearchService(db)
    return service.search_movies(
        search_query.query, 
        search_query.page, 
        search_query.limit
    )

@router.get("/movies/advanced", response_model=SearchResponse)
async def advanced_search(
    q: Optional[str] = Query(None, description="Search query"),
    min_rating: Optional[float] = Query(None, ge=0, le=10, description="Minimum rating"),
    max_rating: Optional[float] = Query(None, ge=0, le=10, description="Maximum rating"),
    min_year: Optional[int] = Query(None, ge=1900, le=2100, description="Minimum release year"),
    max_year: Optional[int] = Query(None, ge=1900, le=2100, description="Maximum release year"),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(20, ge=1, le=100, description="Results per page"),
    db: Session = Depends(get_db)
):
    """
    Advanced movie search with filters
    
    - **q**: Search query (optional)
    - **min_rating**: Minimum rating (0-10)
    - **max_rating**: Maximum rating (0-10)
    - **min_year**: Minimum release year
    - **max_year**: Maximum release year
    - **page**: Page number
    - **limit**: Results per page
    """
    service = SearchService(db)
    return service.advanced_search(
        search_query=q or "",
        min_rating=min_rating,
        max_rating=max_rating,
        min_year=min_year,
        max_year=max_year,
        page=page,
        limit=limit
    )

@router.get("/movies/test")
async def test_search():
    """
    Test endpoint to verify search is working
    Returns sample search results without database query
    """
    return {
        "results": [
            {
                "id": 1,
                "title": "Test Movie",
                "description": "This is a test movie for search functionality",
                "release_date": "2023-01-01T00:00:00",
                "poster_path": "/test-poster.jpg",
                "vote_average": 8.5,
                "vote_count": 1000
            }
        ],
        "total_count": 1,
        "page": 1,
        "total_pages": 1
    }