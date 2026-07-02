@echo off
cd /d D:\Obsidian
set "LOG=D:\Obsidian\claude-memory\sync-log.txt"
echo. >> "%LOG%"
echo [%date% %time%] ==== start ==== >> "%LOG%"
git add -A >> "%LOG%" 2>&1
git diff --cached --name-only | findstr /I "git-credentials .env .key .pem" >nul && (echo [%date% %time%] SENSITIVE FILE - ABORT >> "%LOG%" & git reset >> "%LOG%" 2>&1 & exit /b 1)
git diff --cached --quiet || git commit -m "chore(notes): auto sync %date%" >> "%LOG%" 2>&1
git fetch --prune >> "%LOG%" 2>&1
git pull --rebase origin main >> "%LOG%" 2>&1 || (echo [%date% %time%] REBASE FAILED >> "%LOG%" & git rebase --abort >> "%LOG%" 2>&1 & exit /b 1)
git push origin main >> "%LOG%" 2>&1 || (echo [%date% %time%] PUSH FAILED >> "%LOG%" & exit /b 1)
echo [%date% %time%] ==== done OK ==== >> "%LOG%"
