# routes/lists.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.auth.dependencies import get_current_user
from app import models, schemas
from app.services.list_service import ListService

router = APIRouter(prefix="/lists", tags=["lists"])

# routes/lists.py
@router.get("/", response_model=List[schemas.ListResponse])
def get_user_lists(
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all lists for the current user"""
    service = ListService(db)
    lists = service.get_user_lists(current_user.id)
    
    response = []
    for list_obj in lists:
        # Convert to dict and add movie_count
        list_dict = {
            "id": list_obj.id,
            "name": list_obj.name,
            "description": list_obj.description,
            "is_public": list_obj.is_public,
            "list_type": list_obj.list_type,
            "user_id": list_obj.user_id,
            "movie_count": len(list_obj.list_movies),
            "created_at": list_obj.created_at,
            "updated_at": list_obj.updated_at
        }
        response.append(schemas.ListResponse.model_validate(list_dict))
    
    return response

@router.post("/", response_model=schemas.ListResponse)
def create_list(
    list_data: schemas.ListCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create a new list"""
    service = ListService(db)
    try:
        new_list = service.create_list(current_user.id, list_data)
        # Create response manually
        return schemas.ListResponse(
            id=new_list.id,
            name=new_list.name,
            description=new_list.description,
            is_public=new_list.is_public,
            list_type=new_list.list_type,
            user_id=new_list.user_id,
            movie_count=0,  # New list has 0 movies
            created_at=new_list.created_at,
            updated_at=new_list.updated_at
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{list_id}", response_model=schemas.ListResponse)
def get_list(
    list_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get a specific list"""
    service = ListService(db)
    list_obj = service.get_list_by_id(list_id, current_user.id)
    
    if not list_obj:
        raise HTTPException(status_code=404, detail="List not found")
    
    # Create response manually
    return schemas.ListResponse(
        id=list_obj.id,
        name=list_obj.name,
        description=list_obj.description,
        is_public=list_obj.is_public,
        list_type=list_obj.list_type,
        user_id=list_obj.user_id,
        movie_count=len(list_obj.list_movies),
        created_at=list_obj.created_at,
        updated_at=list_obj.updated_at
    )

@router.put("/{list_id}", response_model=schemas.ListResponse)
def update_list(
    list_id: int,
    list_data: schemas.ListUpdate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update a list"""
    service = ListService(db)
    updated_list = service.update_list(list_id, current_user.id, list_data)
    
    if not updated_list:
        raise HTTPException(status_code=404, detail="List not found")
    
    # Create response manually
    return schemas.ListResponse(
        id=updated_list.id,
        name=updated_list.name,
        description=updated_list.description,
        is_public=updated_list.is_public,
        list_type=updated_list.list_type,
        user_id=updated_list.user_id,
        movie_count=len(updated_list.list_movies),
        created_at=updated_list.created_at,
        updated_at=updated_list.updated_at
    )

@router.delete("/{list_id}")
def delete_list(
    list_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Delete a list"""
    service = ListService(db)
    success = service.delete_list(list_id, current_user.id)
    
    if not success:
        raise HTTPException(status_code=404, detail="List not found")
    
    return {"message": "List deleted successfully"}

@router.post("/{list_id}/movies", response_model=schemas.ListMovieResponse)
def add_movie_to_list(
    list_id: int,
    movie_data: schemas.ListMovieCreate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Add a movie to a list"""
    service = ListService(db)
    try:
        list_movie = service.add_movie_to_list(list_id, current_user.id, movie_data)
        
        # Get movie details for response
        movie = db.query(models.Movie).filter(models.Movie.id == movie_data.movie_id).first()
        
        response = schemas.ListMovieResponse(
            id=list_movie.id,
            list_id=list_movie.list_id,
            movie_id=list_movie.movie_id,
            notes=list_movie.notes,
            position=list_movie.position,
            added_at=list_movie.added_at,
            movie_title=movie.title if movie else "Unknown Movie",
            movie_poster=movie.poster_path if movie else None
        )
        
        return response
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{list_id}/movies/{movie_id}")
def remove_movie_from_list(
    list_id: int,
    movie_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Remove a movie from a list"""
    service = ListService(db)
    success = service.remove_movie_from_list(list_id, current_user.id, movie_id)
    
    if not success:
        raise HTTPException(status_code=404, detail="Movie not found in list")
    
    return {"message": "Movie removed from list"}

@router.get("/{list_id}/movies", response_model=List[schemas.ListMovieResponse])
def get_list_movies(
    list_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all movies in a list"""
    service = ListService(db)
    list_movies = service.get_list_movies(list_id, current_user.id)
    
    if list_movies is None:
        raise HTTPException(status_code=404, detail="List not found")
    
    response = []
    for list_movie in list_movies:
        movie = db.query(models.Movie).filter(models.Movie.id == list_movie.movie_id).first()
        
        response.append(schemas.ListMovieResponse(
            id=list_movie.id,
            list_id=list_movie.list_id,
            movie_id=list_movie.movie_id,
            notes=list_movie.notes,
            position=list_movie.position,
            added_at=list_movie.added_at,
            movie_title=movie.title if movie else "Unknown Movie",
            movie_poster=movie.poster_path if movie else None
        ))
    
    return response
