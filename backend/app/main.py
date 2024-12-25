from fastapi import FastAPI

from app.routes import users
from project_startup import pre_start_tasks

# Run pre-start tasks
pre_start_tasks()


api_router = FastAPI()
api_router.include_router(users.router)
