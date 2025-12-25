@echo off
REM run-launcher.bat
REM Launch the local-experiments launcher without a visible console when possible

SET SCRIPT_DIR=%~dp0

WHERE pythonw >nul 2>&1
IF ERRORLEVEL 1 (
    echo pythonw not found on PATH; launching with python (console may appear)
    python "%SCRIPT_DIR%local-experiments\launcher.py"
) ELSE (
    start "" pythonw "%SCRIPT_DIR%local-experiments\launcher.py"
)
