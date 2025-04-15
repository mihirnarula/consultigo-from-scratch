from fastapi import FastAPI
import uvicorn

# Create simple app
app = FastAPI(title="Test App")

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/test")
def test():
    return {"status": "working"}

# Run directly when script is executed
if __name__ == "__main__":
    print("Starting server on port 5000...")
    uvicorn.run(app, host="127.0.0.1", port=5000) 