from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

# Base model with shared fields
class UserBase(SQLModel):
    """
    Shared fields for user models.
    """
    username: str
    email: str

# Table model for the database
class User(UserBase, table=True):
    """
    Represents the users table in the database.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    password: str = Field(nullable=False)

# Public model for API responses
class UserPublic(UserBase):
    """
    Used for public-facing user data in API responses.
    """
    id: int

    class Config:
        orm_mode = True  # Ensures compatibility with ORM objects

# Create model for user creation
class UserCreate(SQLModel):
    """
    Model for creating a user.
    """
    username: str
    email: str
    password: str  # Plaintext password for hashing during creation

# Update model for partial updates
class UserUpdate(SQLModel):
    """
    Model for updating user data.
    """
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None  # Plaintext password for hashing if updated

