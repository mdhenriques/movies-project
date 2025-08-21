# routes/import.py
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from app import models
from app.database import get_db
from app.services.movie_importer import MovieImporter, import_sample_data

router = APIRouter(prefix="/import", tags=["import"])

@router.post("/sample")
async def import_sample_movies(
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    """Import a sample set of movies (for testing)"""
    def run_import():
        importer = MovieImporter(db)
        return importer.import_popular_movies(page_limit=2)
    
    # Run in background to avoid timeout
    background_tasks.add_task(run_import)
    
    return {
        "message": "Movie import started in background",
        "expected_count": "~40 movies"
    }

@router.post("/popular")
async def import_popular_movies(
    pages: int = 5,
    background_tasks: BackgroundTasks = None,
    db: Session = Depends(get_db)
):
    """Import popular movies with pagination"""
    if pages > 20:  # Safety limit
        pages = 20
    
    def run_import():
        importer = MovieImporter(db)
        return importer.import_popular_movies(page_limit=pages)
    
    if background_tasks:
        background_tasks.add_task(run_import)
        return {
            "message": f"Importing {pages} pages of popular movies in background",
            "expected_count": f"~{pages * 20} movies"
        }
    else:
        # Run synchronously for immediate feedback
        count = run_import()
        return {
            "message": "Import completed",
            "imported_count": count
        }

@router.get("/status")
async def import_status(db: Session = Depends(get_db)):
    """Get current import status"""
    movie_count = db.query(models.Movie).count()
    genre_count = db.query(models.Genre).count()
    
    return {
        "movies_in_database": movie_count,
        "genres_in_database": genre_count
    }