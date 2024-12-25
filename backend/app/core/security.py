import os

from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from pydantic import BaseModel
from pydantic import ValidationError

from sqlmodel import select
from app.core.db import SessionDep
from app.models import User, UserBase, UserCreate, UserPublic, UserUpdate


# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    sub: str | None = None


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/access-token")


TokenDep = Annotated[str, Depends(oauth2_scheme)]

# ============= Password Encryption =============

def verify_password(plain_password, hashed_password):
    """
    Verify a plaintext password against a hashed password.
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """
    Hash a plaintext password.
    """
    return pwd_context.hash(password)


# ============= User Authentication =============

def get_user(session: SessionDep, username: str):
    user = session.exec(select(User).where(User.username == username)).first()
    return user


def authenticate_user(session: SessionDep, username: str, password: str):
    user = get_user(session=session, username=username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


# ============= JWT =============

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    Create a JWT token with an optional expiration.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



def get_current_user(session: SessionDep, token: TokenDep) -> User:
    """
    Finds the user by the JWT token provided
    """
    try:
        payload = jwt.decode(
            token, SECRET_KEY, algorithms=[ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (InvalidTokenError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = get_user(session=session, username=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


CurrentUser = Annotated[User, Depends(get_current_user)] # Singleton for a current session user