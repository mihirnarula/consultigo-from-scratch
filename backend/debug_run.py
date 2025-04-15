import sys
import traceback

try:
    from app.main import app
    print("Successfully imported the FastAPI app")
    
    # List all routes
    for route in app.routes:
        print(f"Route: {route.path}, Methods: {route.methods}")
    
    print("\nApp settings:")
    from app.core.config import settings
    print(f"- Database URL: {settings.DATABASE_URL}")
    print(f"- API prefix: {settings.API_V1_STR}")
    
    print("\nTrying to start the server...")
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, log_level="debug")
    
except Exception as e:
    print(f"Error: {e}")
    traceback.print_exc() 