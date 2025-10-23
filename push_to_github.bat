@echo off
echo ============================================
echo  Twicky - Push to GitHub Script
echo ============================================
echo.

REM Change to the project directory
cd /d "%~dp0"

echo Current directory: %CD%
echo.

REM Check if git is initialized
if not exist ".git" (
    echo Initializing Git repository...
    git init
    echo.
)

REM Show current status
echo Checking git status...
git status
echo.

REM Add all files
echo Adding all files...
git add .
echo.

REM Commit changes
echo Enter commit message (or press Enter for default):
set /p commit_msg="Commit message: "

if "%commit_msg%"=="" (
    set commit_msg=feat: MongoDB integration, Vercel deployment, and professional UI redesign
)

echo.
echo Committing with message: %commit_msg%
git commit -m "%commit_msg%"
echo.

REM Check if remote exists
git remote -v > nul 2>&1
if errorlevel 1 (
    echo No remote repository found!
    echo Please enter your GitHub repository URL:
    echo Example: https://github.com/YOUR_USERNAME/twicky.git
    set /p repo_url="Repository URL: "
    
    if not "%repo_url%"=="" (
        echo Adding remote origin...
        git remote add origin %repo_url%
        echo.
    ) else (
        echo ERROR: No repository URL provided!
        echo Please add remote manually using:
        echo git remote add origin YOUR_GITHUB_URL
        pause
        exit /b 1
    )
)

REM Set branch to main
echo Setting branch to main...
git branch -M main
echo.

REM Push to GitHub
echo Pushing to GitHub...
echo.
git push -u origin main

if errorlevel 1 (
    echo.
    echo ============================================
    echo  Push failed! Possible solutions:
    echo ============================================
    echo 1. If divergent branches error:
    echo    git pull origin main --allow-unrelated-histories
    echo    git push -u origin main
    echo.
    echo 2. If authentication error:
    echo    - Use Personal Access Token as password
    echo    - Or configure SSH keys
    echo.
    echo 3. If remote already exists error:
    echo    git remote remove origin
    echo    git remote add origin YOUR_GITHUB_URL
    echo    git push -u origin main
    echo ============================================
    echo.
) else (
    echo.
    echo ============================================
    echo  SUCCESS! Code pushed to GitHub!
    echo ============================================
    echo.
    echo Your code is now on GitHub!
    echo.
    echo Next steps:
    echo 1. Visit your GitHub repository
    echo 2. Verify all files are uploaded
    echo 3. Deploy to Vercel (see DEPLOYMENT.md)
    echo ============================================
    echo.
)

pause

