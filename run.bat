@echo off
echo Starting Decision Journal Mock Environment...

echo [1/3] Setting up Python Virtual Environment...
python -m venv venv
call venv\Scripts\activate.bat

echo [2/3] Installing Backend Dependencies...
pip install -r backend\requirements.txt

echo [3/3] Starting FastAPI Server...
start cmd /k "call venv\Scripts\activate.bat & cd backend & uvicorn main:app --reload --port 8000"

echo Waiting for server to start...
timeout /t 5 /nobreak > NUL

echo Seeding database with mock data...
curl -X POST http://localhost:8000/seed

echo.
echo ==================================================
echo Setup Complete!
echo 1. Start MongoDB: Make sure MongoDB is running locally (e.g., using "docker-compose up -d")
echo 2. Open frontend: Just double-click on "frontend\index.html" in your browser.
echo 3. API Docs: http://localhost:8000/docs
echo ==================================================
pause
