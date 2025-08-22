# services/search_service.py
from typing import List, Optional, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import or_, func
from app.models import Movie
from app.schemas import MovieSearchResult, SearchResponse

class SearchService:
    def __init__(self, db: Session):
        self.db = db
    
    def search_movies(
        self, 
        search_query: str, 
        page: int = 1, 
        limit: int = 20
    ) -> SearchResponse:
        """
        Search movies by title with pagination
        Returns movies that contain the search query in title (case-insensitive)
        """
        # Calculate offset for pagination
        offset = (page - 1) * limit
        
        # Build the search query
        search_pattern = f"%{search_query}%"
        
        # Get total count for pagination
        total_count = self.db.query(Movie).filter(
            or_(
                Movie.title.ilike(search_pattern),
                Movie.original_title.ilike(search_pattern)
            )
        ).count()
        
        # Calculate total pages
        total_pages = (total_count + limit - 1) // limit
        
        # Get paginated results
        movies = self.db.query(Movie).filter(
            or_(
                Movie.title.ilike(search_pattern),
                Movie.original_title.ilike(search_pattern)
            )
        ).order_by(
            Movie.vote_count.desc(),  # Sort by popularity first
            Movie.vote_average.desc()  # Then by rating
        ).offset(offset).limit(limit).all()
        
        # Convert to Pydantic models
        results = [
            MovieSearchResult(
                id=movie.id,
                title=movie.title,
                description=movie.description,
                release_date=movie.release_date,
                poster_path=movie.poster_path,
                vote_average=movie.vote_average,
                vote_count=movie.vote_count
            )
            for movie in movies
        ]
        
        return SearchResponse(
            results=results,
            total_count=total_count,
            page=page,
            total_pages=total_pages
        )
    
    def advanced_search(
        self,
        search_query: str,
        genre: Optional[str] = None,
        min_rating: Optional[float] = None,
        max_rating: Optional[float] = None,
        min_year: Optional[int] = None,
        max_year: Optional[int] = None,
        page: int = 1,
        limit: int = 20
    ) -> SearchResponse:
        """
        Advanced search with filters (for future enhancement)
        """
        # Start with base query
        query = self.db.query(Movie)
        
        # Text search
        if search_query:
            search_pattern = f"%{search_query}%"
            query = query.filter(
                or_(
                    Movie.title.ilike(search_pattern),
                    Movie.original_title.ilike(search_pattern),
                    Movie.description.ilike(search_pattern)
                )
            )
        
        # Genre filter (you'll need to implement genre relationships first)
        if genre:
            pass  # Implement genre filtering later
        
        # Rating filters
        if min_rating is not None:
            query = query.filter(Movie.vote_average >= min_rating)
        if max_rating is not None:
            query = query.filter(Movie.vote_average <= max_rating)
        
        # Year filters
        if min_year is not None:
            query = query.filter(Movie.release_date >= f"{min_year}-01-01")
        if max_year is not None:
            query = query.filter(Movie.release_date <= f"{max_year}-12-31")
        
        # Get total count
        total_count = query.count()
        total_pages = (total_count + limit - 1) // limit
        offset = (page - 1) * limit
        
        # Get paginated results
        movies = query.order_by(
            Movie.vote_count.desc(),
            Movie.vote_average.desc()
        ).offset(offset).limit(limit).all()
        
        # Convert to response format
        results = [
            MovieSearchResult(
                id=movie.id,
                title=movie.title,
                description=movie.description,
                release_date=movie.release_date,
                poster_path=movie.poster_path,
                vote_average=movie.vote_average,
                vote_count=movie.vote_count
            )
            for movie in movies
        ]
        
        return SearchResponse(
            results=results,
            total_count=total_count,
            page=page,
            total_pages=total_pages
        )

# Utility function for easy searching
def search_movies_db(query: str, page: int = 1, limit: int = 20):
    """Quick search function for testing"""
    from app.database import get_db
    db = next(get_db())
    try:
        service = SearchService(db)
        return service.search_movies(query, page, limit)
    finally:
        db.close()