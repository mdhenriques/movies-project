from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import List, Optional, Dict, Any
from app import models, schemas

class ListService:
    def __init__(self, db: Session):
        self.db = db

    def get_user_lists(self, user_id: int) -> List[models.List]:
        """Get all lists for a user"""
        return self.db.query(models.List).filter(
            models.List.user_id == user_id
        ).order_by(models.List.created_at.desc()).all()

    def get_list_by_id(self, list_id: int, user_id: int) -> Optional[models.List]:
        """Get a specific list by ID (user must own it)"""
        return self.db.query(models.List).filter(
            and_(
                models.List.id == list_id,
                models.List.user_id == user_id
            )
        ).first()

    def create_list(self, user_id: int, list_data: schemas.ListCreate) -> models.List:
        """Create a new list for a user"""
        # Check if user already has a list with this name
        existing = self.db.query(models.List).filter(
            and_(
                models.List.user_id == user_id,
                models.List.name == list_data.name
            )
        ).first()
        
        if existing:
            raise ValueError("You already have a list with this name")
        
        db_list = models.List(
            **list_data.dict(),
            user_id=user_id
        )
        
        self.db.add(db_list)
        self.db.commit()
        self.db.refresh(db_list)
        return db_list

    def update_list(self, list_id: int, user_id: int, update_data: schemas.ListUpdate) -> Optional[models.List]:
        """Update a list"""
        db_list = self.get_list_by_id(list_id, user_id)
        if not db_list:
            return None
        
        for key, value in update_data.dict(exclude_unset=True).items():
            setattr(db_list, key, value)
        
        self.db.commit()
        self.db.refresh(db_list)
        return db_list

    def delete_list(self, list_id: int, user_id: int) -> bool:
        """Delete a list and all its movies"""
        db_list = self.get_list_by_id(list_id, user_id)
        if not db_list:
            return False
        
        self.db.delete(db_list)
        self.db.commit()
        return True

    def add_movie_to_list(self, list_id: int, user_id: int, movie_data: schemas.ListMovieCreate) -> Optional[models.ListMovie]:
        """Add a movie to a list"""
        # Verify list exists and belongs to user
        db_list = self.get_list_by_id(list_id, user_id)
        if not db_list:
            return None
        
        # Check if movie is already in the list
        existing = self.db.query(models.ListMovie).filter(
            and_(
                models.ListMovie.list_id == list_id,
                models.ListMovie.movie_id == movie_data.movie_id
            )
        ).first()
        
        if existing:
            raise ValueError("Movie is already in this list")
        
        # Create new list movie entry
        db_list_movie = models.ListMovie(
            **movie_data.dict(),
            list_id=list_id
        )
        
        self.db.add(db_list_movie)
        self.db.commit()
        self.db.refresh(db_list_movie)
        return db_list_movie

    def remove_movie_from_list(self, list_id: int, user_id: int, movie_id: int) -> bool:
        """Remove a movie from a list"""
        # Verify list exists and belongs to user
        db_list = self.get_list_by_id(list_id, user_id)
        if not db_list:
            return False
        
        # Find the list movie entry
        db_list_movie = self.db.query(models.ListMovie).filter(
            and_(
                models.ListMovie.list_id == list_id,
                models.ListMovie.movie_id == movie_id
            )
        ).first()
        
        if not db_list_movie:
            return False
        
        self.db.delete(db_list_movie)
        self.db.commit()
        return True

    def get_list_movies(self, list_id: int, user_id: int) -> List[models.ListMovie]:
        """Get all movies in a list"""
        db_list = self.get_list_by_id(list_id, user_id)
        if not db_list:
            return []
        
        return self.db.query(models.ListMovie).filter(
            models.ListMovie.list_id == list_id
        ).order_by(models.ListMovie.position, models.ListMovie.added_at.desc()).all()

    def get_user_special_lists(self, user_id: int) -> Dict[str, Optional[models.List]]:
        """Get user's watchlist and favorites lists"""
        watchlist = self.db.query(models.List).filter(
            and_(
                models.List.user_id == user_id,
                models.List.list_type == "watchlist"
            )
        ).first()
        
        favorites = self.db.query(models.List).filter(
            and_(
                models.List.user_id == user_id,
                models.List.list_type == "favorites"
            )
        ).first()
        
        return {
            "watchlist": watchlist,
            "favorites": favorites
        }

    def create_default_lists(self, user_id: int) -> None:
        """Create default lists for a new user"""
        default_lists = [
            models.List(
                name="Watchlist",
                description="Movies I want to watch",
                list_type="watchlist",
                user_id=user_id,
                is_public=False
            ),
            models.List(
                name="Favorites", 
                description="My favorite movies",
                list_type="favorites",
                user_id=user_id,
                is_public=False
            )
        ]
        
        self.db.add_all(default_lists)
        self.db.commit()