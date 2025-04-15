from fastapi import FastAPI
from fastapi.testclient import TestClient

# Create a simple test app
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 