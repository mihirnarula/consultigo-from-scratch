@echo off
echo Setting up frontend...

REM Create necessary directories
mkdir frontend
cd frontend
mkdir src
mkdir src\components
mkdir src\components\auth

REM Create package.json
echo {
echo   "name": "guesstimate-frontend",
echo   "private": true,
echo   "version": "0.1.0",
echo   "type": "module",
echo   "scripts": {
echo     "dev": "vite",
echo     "build": "tsc && vite build",
echo     "lint": "eslint src --ext ts,tsx --report-unused-disable-directives --max-warnings 0",
echo     "preview": "vite preview"
echo   },
echo   "dependencies": {
echo     "@types/node": "^20.11.24",
echo     "@types/react": "^18.2.56",
echo     "@types/react-dom": "^18.2.19",
echo     "@vitejs/plugin-react": "^4.2.1",
echo     "axios": "^1.6.7",
echo     "react": "^18.2.0",
echo     "react-dom": "^18.2.0",
echo     "react-router-dom": "^6.22.1",
echo     "typescript": "^5.2.2",
echo     "vite": "^5.1.4"
echo   },
echo   "devDependencies": {
echo     "@typescript-eslint/eslint-plugin": "^7.0.2",
echo     "@typescript-eslint/parser": "^7.0.2",
echo     "autoprefixer": "^10.4.17",
echo     "eslint": "^8.56.0",
echo     "eslint-plugin-react-hooks": "^4.6.0",
echo     "eslint-plugin-react-refresh": "^0.4.5",
echo     "postcss": "^8.4.35",
echo     "tailwindcss": "^3.4.1"
echo   }
echo } > package.json

REM Create tsconfig.json
echo {
echo   "compilerOptions": {
echo     "target": "ES2020",
echo     "useDefineForClassFields": true,
echo     "lib": ["ES2020", "DOM", "DOM.Iterable"],
echo     "module": "ESNext",
echo     "skipLibCheck": true,
echo     "esModuleInterop": true,
echo     "moduleResolution": "bundler",
echo     "allowImportingTsExtensions": true,
echo     "resolveJsonModule": true,
echo     "isolatedModules": true,
echo     "noEmit": true,
echo     "jsx": "react-jsx",
echo     "strict": true,
echo     "noUnusedLocals": true,
echo     "noUnusedParameters": true,
echo     "noFallthroughCasesInSwitch": true
echo   },
echo   "include": ["src"],
echo   "references": [{ "path": "./tsconfig.node.json" }]
echo } > tsconfig.json

REM Create tsconfig.node.json
echo {
echo   "compilerOptions": {
echo     "composite": true,
echo     "skipLibCheck": true,
echo     "module": "ESNext",
echo     "moduleResolution": "bundler",
echo     "allowSyntheticDefaultImports": true
echo   },
echo   "include": ["vite.config.ts"]
echo } > tsconfig.node.json

REM Create vite.config.ts
echo import { defineConfig } from 'vite'
echo import react from '@vitejs/plugin-react'
echo 
echo export default defineConfig({
echo   plugins: [react()],
echo   server: {
echo     port: 3000,
echo   },
echo }) > vite.config.ts

REM Create tailwind.config.js
echo /** @type {import('tailwindcss').Config} */
echo export default {
echo   content: [
echo     "./index.html",
echo     "./src/**/*.{js,ts,jsx,tsx}",
echo   ],
echo   theme: {
echo     extend: {},
echo   },
echo   plugins: [],
echo } > tailwind.config.js

REM Create postcss.config.js
echo export default {
echo   plugins: {
echo     tailwindcss: {},
echo     autoprefixer: {},
echo   },
echo } > postcss.config.js

REM Create index.html
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

REM Create main.tsx
echo import React from 'react'
echo import ReactDOM from 'react-dom/client'
echo import { BrowserRouter as Router } from 'react-router-dom'
echo import App from './App'
echo import './index.css'
echo 
echo ReactDOM.createRoot(document.getElementById('root')!).render(
echo   ^<React.StrictMode^>
echo     ^<Router^>
echo       ^<App /^>
echo     ^</Router^>
echo   ^</React.StrictMode^>,
echo ) > src/main.tsx

REM Create index.css
echo @tailwind base;
echo @tailwind components;
echo @tailwind utilities; > src/index.css

REM Create App.tsx
echo import React from 'react';
echo import { Routes, Route, Navigate } from 'react-router-dom';
echo import Dashboard from './components/Dashboard';
echo import GuesstimateDashboard from './components/Guesstimate';
echo import SignIn from './components/auth/SignIn';
echo import SignUp from './components/auth/SignUp';
echo 
echo const App: React.FC = () => {
echo   return (
echo     ^<Routes^>
echo       ^<Route path="/signin" element={^<SignIn /^>} /^>
echo       ^<Route path="/signup" element={^<SignUp /^>} /^>
echo       ^<Route path="/dashboard" element={^<Dashboard /^>} /^>
echo       ^<Route path="/guesstimates" element={^<GuesstimateDashboard /^>} /^>
echo       ^<Route path="/" element={^<Navigate to="/signin" replace /^>} /^>
echo     ^</Routes^>
echo   );
echo };
echo 
echo export default App; > src/App.tsx

echo Frontend setup complete!
echo Running npm install...
npm install
echo Starting development server...
npm run dev 