from enum import Enum
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


# --- Enum for Subscription Frequency ---
class SubscriptionFrequency(str, Enum):
    """
    Enum to represent subscription frequency options.
    """
    MONTHLY = "monthly"
    ANNUALLY = "annually"


# --- User Models ---

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

# --- Subscription Models ---

class SubscriptionBase(SQLModel):
    """
    Shared fields for subscription models.
    """
    name: str
    cost: float
    frequency: SubscriptionFrequency  # Using the Enum for frequency
    next_billing_date: datetime
    ends_at: Optional[datetime] = None  # Optional end date


class Subscription(SubscriptionBase, table=True):
    """
    Represents the subscriptions table in the database.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")


class SubscriptionPublic(SubscriptionBase):
    """
    Used for public-facing subscription data in API responses.
    """
    id: int
    user_id: int

    class Config:
        orm_mode = True  # Ensures compatibility with ORM objects


class SubscriptionCreate(SQLModel):
    """
    Model for creating a subscription.
    """
    name: str
    cost: float
    user_id: int
    frequency: SubscriptionFrequency  # Using the Enum for frequency
    next_billing_date: datetime
    ends_at: Optional[datetime] = None  # Optional end date


class SubscriptionUpdate(SQLModel):
    """
    Model for updating subscription data.
    """
    name: Optional[str] = None
    cost: Optional[float] = None
    frequency: Optional[SubscriptionFrequency] = None  # Optional Enum for updates
    next_billing_date: Optional[datetime] = None
    ends_at: Optional[datetime] = None