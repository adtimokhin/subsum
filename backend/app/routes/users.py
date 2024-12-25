from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import select
from app.core.db import SessionDep
from app.models import User, UserBase, UserCreate, UserPublic, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserPublic)
def create_user(user: UserCreate, session: SessionDep):
    """
    Creates user and adds it to the database.
    """

    db_user = User.model_validate(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@router.get("/", response_model=list[UserPublic])
def read_users(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    
    """
    Reads up to 100 users
    """

    # FIXME: Remove this method for production
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users