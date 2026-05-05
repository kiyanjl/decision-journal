@echo off
title Decision Journal Launcher
color 0A
cls

echo.
echo ===========================================
echo     DECISION JOURNAL DASHBOARD v2.0
echo ===========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found! Install Python 3.8+
    pause
    exit /b 1
)

cd /d "%~dp0backend"

REM Create virtual environment if missing
if not exist "venv" (
    echo [1/4] Creating virtual environment...
    python -m venv venv
)

REM Activate and install deps
echo [2/4] Activating environment...
call venv\Scripts\activate.bat
echo [3/4] Installing dependencies...
pip install -r requirements.txt -q

echo [4/4] Building Frontend UI...
cd /d "%~dp0"
python build_frontend.py
cd backend

REM Start backend in new window
echo.
echo Starting Backend API on port 8000...
start "Decision Journal API" cmd /k "cd /d %~dp0backend & call venv\Scripts\activate.bat & uvicorn main:app --host 0.0.0.0 --port 8000 --reload"

REM Wait for backend to be ready
echo Waiting 5 seconds for backend to start...
timeout /t 5 /nobreak >nul

REM Open the DASHBOARD (not API docs!)
echo.
echo Opening DASHBOARD in browser...
start "" "http://localhost:8000/"


echo.
echo ===========================================
echo  ✅ BACKEND:  http://localhost:8000
echo  ✅ DASHBOARD: http://localhost:8000/

echo ===========================================
echo.
echo Run 'seed.bat' next to add demo data!
pause
