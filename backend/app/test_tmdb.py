# Simple test script
from services.tmdb_client import tmdb_client

result = tmdb_client.test_connection()
print("TMDb Connection Test:")
print(f"Status: {result['status']}")
print(f"Message: {result['message']}")

if result['status'] == 'success':
    print(f"Images Base URL: {result['images_base_url']}")