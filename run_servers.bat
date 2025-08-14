@echo off
echo Starting Django SSO Servers...
echo ========================================
echo.
echo 1. Starting SSO Server (mtfa) on port 8000
echo    - This will handle authentication
echo    - Access at: http://127.0.0.1:8000
echo.
echo 2. Starting SSO Client on port 8001
echo    - This will redirect to SSO server for login
echo    - Access at: http://127.0.0.1:8001
echo.
echo Press Ctrl+C to stop all servers
echo ========================================
echo.

REM Start SSO Server in background
start "SSO Server" cmd /k "cd mtfa && python manage.py runserver 127.0.0.1:8000"

REM Wait a moment for server to start
timeout /t 3 /nobreak > nul

REM Start SSO Client
start "SSO Client" cmd /k "cd sso_client && python manage.py runserver 127.0.0.1:8001"

echo.
echo Both servers are starting...
echo Close the command windows to stop the servers
pause
