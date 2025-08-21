# services/movie_importer.py
import time
from datetime import datetime
from typing import List, Dict, Optional
from sqlalchemy.orm import Session
from app.services.tmdb_client import tmdb_client
from app.models import Movie, Genre, Base
from app.database import engine, get_db

class MovieImporter:
    def __init__(self, db: Session):
        self.db = db
        self.genre_cache = {}  # Cache genre lookups
    
    def get_or_create_genre(self, genre_data: Dict) -> Genre:
        """Get existing genre or create new one"""
        genre = self.db.query(Genre).filter(
            Genre.tmdb_id == genre_data["id"]
        ).first()
        
        if not genre:
            genre = Genre(
                tmdb_id=genre_data["id"],
                name=genre_data["name"]
            )
            self.db.add(genre)
            self.db.flush()  # Flush to get ID without committing
        
        self.genre_cache[genre_data["id"]] = genre
        return genre
    
    def import_movie(self, movie_data: Dict) -> Optional[Movie]:
        """Import a single movie from TMDb data"""
        try:
            # Check if movie already exists
            existing_movie = self.db.query(Movie).filter(
                Movie.tmdb_id == movie_data["id"]
            ).first()
            
            if existing_movie:
                print(f"Movie already exists: {movie_data['title']}")
                return existing_movie
            
            # Get full movie details
            full_details = tmdb_client.get_movie_details(movie_data["id"])
            
            # Create movie
            movie = Movie(
                tmdb_id=full_details["id"],
                title=full_details["title"],
                description=full_details.get("overview"),
                release_date=datetime.strptime(full_details["release_date"], "%Y-%m-%d") if full_details.get("release_date") else None,
                poster_path=full_details.get("poster_path"),
                backdrop_path=full_details.get("backdrop_path"),
                imdb_id=full_details.get("imdb_id"),
                popularity=full_details.get("popularity", 0),
                vote_average=full_details.get("vote_average", 0),
                vote_count=full_details.get("vote_count", 0),
                runtime=full_details.get("runtime"),
                original_language=full_details.get("original_language"),
                original_title=full_details.get("original_title"),
                status=full_details.get("status"),
                budget=full_details.get("budget"),
                revenue=full_details.get("revenue")
            )
            
            # Add genres
            for genre_data in full_details.get("genres", []):
                genre = self.get_or_create_genre(genre_data)
                movie.genres.append(genre)
            
            self.db.add(movie)
            return movie
            
        except Exception as e:
            print(f"Error importing movie {movie_data.get('title')}: {e}")
            return None
    
    def import_popular_movies(self, page_limit: int = 5, delay: float = 0.1):
        """Import popular movies with pagination"""
        imported_count = 0
        
        for page in range(1, page_limit + 1):
            print(f"Fetching page {page} of popular movies...")
            
            try:
                # Get popular movies from TMDb
                result = tmdb_client.get_popular_movies(page)
                movies_data = result.get("results", [])
                
                for movie_data in movies_data:
                    movie = self.import_movie(movie_data)
                    if movie:
                        imported_count += 1
                        if imported_count % 10 == 0:
                            print(f"Imported {imported_count} movies...")
                
                # Commit after each page
                self.db.commit()
                print(f"Page {page} completed. Total imported: {imported_count}")
                
                # Respect TMDb rate limits (40 requests/10 seconds)
                time.sleep(delay)
                
            except Exception as e:
                print(f"Error on page {page}: {e}")
                self.db.rollback()
                time.sleep(2)  # Longer delay on error
        
        return imported_count
    
    def import_by_genre(self, genre_id: int, page_limit: int = 3):
        """Import movies by specific genre"""
        # You can implement genre-based import later
        pass

# Utility function for easy importing
def import_sample_data():
    """Import a sample set of movies for testing"""
    db = next(get_db())
    try:
        importer = MovieImporter(db)
        count = importer.import_popular_movies(page_limit=2)  # ~40 movies
        print(f"Successfully imported {count} movies!")
        return count
    finally:
        db.close()