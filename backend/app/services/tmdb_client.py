import requests
import os
from typing import List, Dict, Optional
from dotenv import load_dotenv

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/original"

class TMDbClient:
    def __init__(self):
        self.api_key = TMDB_API_KEY
        self.session = requests.Session()

    def test_connection(self) -> Dict:
        """
        Test the connection to TMDb API with a simple request
        Returns basic API status and configuration info
        """
        url = f"{BASE_URL}/configuration"
        params = {
            "api_key": self.api_key
        }
        
        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            # If we get here, the connection is successful
            data = response.json()
            return {
                "status": "success",
                "message": "TMDb API connection successful",
                "images_base_url": data.get("images", {}).get("base_url", "N/A"),
                "secure_base_url": data.get("images", {}).get("secure_base_url", "N/A")
            }
            
        except requests.exceptions.ConnectionError:
            return {
                "status": "error",
                "message": "Failed to connect to TMDb API - network issue"
            }
        except requests.exceptions.Timeout:
            return {
                "status": "error", 
                "message": "TMDb API request timed out"
            }
        except requests.exceptions.HTTPError as e:
            if response.status_code == 401:
                return {
                    "status": "error",
                    "message": "Invalid TMDb API key - check your TMDB_API_KEY environment variable",
                    "status_code": response.status_code
                }
            return {
                "status": "error",
                "message": f"TMDb API HTTP error: {str(e)}",
                "status_code": response.status_code
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Unexpected error: {str(e)}"
            }
    
    def search_movies(self, query: str, page: int = 1) -> Dict:
        """Search movies by title"""
        url = f"{BASE_URL}/search/movie"
        params = {
            "api_key": self.api_key,
            "query": query,
            "page": page,
            "language": "pt-BR"  # or "en-US"
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_movie_details(self, movie_id: int) -> Dict:
        """Get complete movie details"""
        url = f"{BASE_URL}/movie/{movie_id}"
        params = {
            "api_key": self.api_key,
            "language": "pt-BR",
            "append_to_response": "credits"  # Gets cast and crew
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_popular_movies(self, page: int = 1) -> Dict:
        """Get currently popular movies"""
        url = f"{BASE_URL}/movie/popular"
        params = {
            "api_key": self.api_key,
            "page": page,
            "language": "pt-BR"
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_movie_recommendations(self, movie_id: int, page: int = 1) -> Dict:
        """Get recommendations based on a specific movie"""
        url = f"{BASE_URL}/movie/{movie_id}/recommendations"
        params = {
            "api_key": self.api_key,
            "page": page,
            "language": "pt-BR"
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_genres(self) -> Dict:
        """Get list of all available genres"""
        url = f"{BASE_URL}/genre/movie/list"
        params = {
            "api_key": self.api_key,
            "language": "pt-BR"
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

# Create a global instance
tmdb_client = TMDbClient()