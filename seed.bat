@echo off
echo Seeding Decision Journal Data...
powershell -Command "try { $r = Invoke-RestMethod -Uri 'http://localhost:8000/seed' -Method POST -UseBasicParsing; Write-Host '✅ SEED SUCCESS:' $r.message } catch { Write-Host '❌ Backend not running? Start run.bat first!' }"
echo.
echo Open frontend/index.html to see the dashboard!
pause
