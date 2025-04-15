# Run script for PowerShell
Write-Host "Activating virtual environment..."
. .\venv\Scripts\Activate.ps1

Write-Host "Starting FastAPI application..."
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload 