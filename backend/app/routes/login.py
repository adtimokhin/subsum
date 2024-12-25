from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException,status
from datetime import datetime, timedelta, timezone
from sqlmodel import select
from app.core.db import SessionDep
from app.models import User, UserBase, UserCreate, UserPublic, UserUpdate
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(tags=["login"])

from app.core.security import Token, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, CurrentUser


@router.post("/token/access-token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: SessionDep,
) -> Token:
    """
    Creates a JWT token for registered user
    """
    user = authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.post("/login/test-token", response_model=UserPublic)
def test_token(current_user: CurrentUser) -> Any:
    """
    Test access token
    """
    return current_user