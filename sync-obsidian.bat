@echo off
cd /d D:\Obsidian
echo ============================================
echo   Obsidian Sync  %date% %time%
echo ============================================
echo.
echo [1/5] git add ...
git add -A
echo.
echo [2/5] checking sensitive files ...
git diff --cached --name-only | findstr /I "git-credentials .env .key .pem" >nul && (echo   !! SENSITIVE FILE FOUND - ABORT !! & git reset & pause & exit /b 1)
echo   ok
echo.
echo [3/5] commit ...
git diff --cached --quiet && (echo   no local changes) || git commit -m "chore(notes): auto sync %date%"
echo.
echo [4/5] pull --rebase ...
git pull --rebase --autostash origin main || (echo   !! REBASE FAILED - please fix manually !! & if exist .git\rebase-merge git rebase --abort & if exist .git\rebase-apply git rebase --abort & pause & exit /b 1)
echo.
echo [5/5] push ...
git push origin main || (echo   !! PUSH FAILED !! & pause & exit /b 1)
echo.
echo ============================================
echo   DONE OK
echo   commit:
git log -1 --pretty=format:"   %%h  %%s  (%%ci)"
echo.
echo ============================================
pause
