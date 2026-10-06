@echo off
rem Genera los PDFs de todas las presentaciones en esta computadora (Windows).
rem Doble clic, o desde cmd:   generar-pdfs.bat                todos los cursos
rem                            generar-pdfs.bat python         solo ppts\python
rem Corre generar-pdfs.ps1 sin cambiar la politica de ejecucion de PowerShell del equipo.
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0generar-pdfs.ps1" %*
set "CODIGO=%ERRORLEVEL%"
echo.
pause
exit /b %CODIGO%
