from fastapi import FastAPI

from app.routes import users, subscriptions, login
from project_startup import pre_start_tasks

# Run pre-start tasks
pre_start_tasks()


api_router = FastAPI()
api_router.include_router(users.router)
api_router.include_router(subscriptions.router)
api_router.include_router(login.router)
