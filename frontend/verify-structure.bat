@echo off
echo Verifying frontend structure...

REM Check and create necessary directories
if not exist src mkdir src
if not exist src\components mkdir src\components
if not exist src\components\auth mkdir src\components\auth

REM Check and create necessary files
if not exist src\main.tsx (
  echo Creating main.tsx...
  echo import React from 'react'
  echo import ReactDOM from 'react-dom/client'
  echo import { BrowserRouter as Router } from 'react-router-dom'
  echo import App from './App'
  echo import './index.css'
  echo.
  echo ReactDOM.createRoot(document.getElementById('root')!).render(
  echo   ^<React.StrictMode^>
  echo     ^<Router^>
  echo       ^<App /^>
  echo     ^</Router^>
  echo   ^</React.StrictMode^>,
  echo ) > src\main.tsx
)

if not exist src\index.css (
  echo Creating index.css...
  echo @tailwind base;
  echo @tailwind components;
  echo @tailwind utilities; > src\index.css
)

if not exist index.html (
  echo Creating index.html...
  echo ^<!DOCTYPE html^>
  echo ^<html lang="en"^>
  echo   ^<head^>
  echo     ^<meta charset="UTF-8" /^>
  echo     ^<link rel="icon" type="image/svg+xml" href="/vite.svg" /^>
  echo     ^<meta name="viewport" content="width=device-width, initial-scale=1.0" /^>
  echo     ^<title^>Guesstimate App^</title^>
  echo   ^</head^>
  echo   ^<body^>
  echo     ^<div id="root"^>^</div^>
  echo     ^<script type="module" src="/src/main.tsx"^>^</script^>
  echo   ^</body^>
  echo ^</html^> > index.html
)

echo Structure verification complete! 