from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from app.core.db import SessionDep
from app.models import User

router = APIRouter(prefix="/users", tags=["users"])
