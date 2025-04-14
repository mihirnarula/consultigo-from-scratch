# Consultigo - LeetCode for Consulting Prep

A full-stack web application for practicing consulting case studies, guesstimates, and frameworks with AI-powered evaluation.

## Tech Stack

### Frontend
- Next.js
- TypeScript
- Tailwind CSS
- React Query for API data fetching

### Backend
- FastAPI (Python)
- MongoDB
- JWT Authentication
- OpenAI API for solution evaluation

## Project Structure
```
consultigo/
├── frontend/          # Next.js frontend
│   ├── app/          # Next.js 13+ app directory
│   ├── components/   # React components
│   └── lib/         # Utilities and API client
└── backend/
    ├── app/          # FastAPI application
    │   ├── models/   # Pydantic models
    │   ├── routes/   # API endpoints
    │   ├── core/     # Core functionality
    │   └── services/ # Business logic
    └── tests/        # Backend tests
```

## Backend Implementation

### Models (Pydantic)
```python
# app/models/user.py
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class SolutionBase(BaseModel):
    problem_id: str
    solution: str
    submitted_at: datetime

class UserBase(BaseModel):
    name: str
    email: EmailStr
    problem_solved: int = 0
    solutions: List[SolutionBase] = []

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    hashed_password: str

# app/models/case_study.py
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class Difficulty(str, Enum):
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"

class CaseStudy(BaseModel):
    title: str
    difficulty: Difficulty
    description: str
    questions: List[str]
    sample_solution: Optional[str] = None
```

### API Routes
```python
# app/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate):
    # Implementation

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Implementation

# app/routes/cases.py
@router.get("/case-studies")
async def get_cases():
    # Implementation

@router.post("/case-studies/{case_id}/submit")
async def submit_solution(case_id: str, solution: str):
    # Implementation with AI evaluation
```

### AI Evaluation Service
```python
# app/services/evaluator.py
from openai import AsyncOpenAI

class SolutionEvaluator:
    def __init__(self):
        self.client = AsyncOpenAI()

    async def evaluate_solution(self, problem: str, solution: str):
        response = await self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are evaluating a consulting case solution."},
                {"role": "user", "content": f"Problem: {problem}\nSolution: {solution}"}
            ]
        )
        return response.choices[0].message.content
```

## Environment Setup
```env
# .env
MONGODB_URI=mongodb://localhost:27017/consultigo
JWT_SECRET=your-secret-key
OPENAI_API_KEY=your-openai-key
```

## Key Features
- JWT-based authentication
- Password hashing with bcrypt
- AI-powered solution evaluation
- Rate limiting and CORS
- Input validation with Pydantic
- Comprehensive error handling
- MongoDB integration with Motor (async)

## Security
- HTTPS enforcement
- JWT token management
- Input validation and sanitization
- Rate limiting
- Secure headers
- CORS configuration

## Deployment
- Docker containerization
- Environment configuration
- Database backups
- Logging with Python logging
- Monitoring with Prometheus
- CI/CD with GitHub Actions

## Getting Started

1. Clone the repository
2. Set up environment variables
3. Install dependencies:
   ```bash
   # Frontend
   cd frontend
   npm install

   # Backend
   cd backend
   pip install -r requirements.txt
   ```
4. Run development servers:
   ```bash
   # Frontend
   npm run dev

   # Backend
   uvicorn app.main:app --reload
   ```

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.
