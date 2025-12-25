@echo off
REM run-chaos-test.bat
REM Runs chaos-test-simple.py and writes output to chaos-test-report.txt (console visible)

cd /d %~dp0
echo Running chaos-test-simple.py ...
python "%~dp0chaos-test-simple.py" > "%~dp0chaos-test-report.txt" 2>&1
if exist "%~dp0chaos-test-report.txt" (
    start notepad "%~dp0chaos-test-report.txt"
)
pause
