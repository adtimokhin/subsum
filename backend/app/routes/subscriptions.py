from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from app.core.db import SessionDep
from app.models import Subscription, SubscriptionBase, SubscriptionCreate, SubscriptionFrequency, SubscriptionPublic, SubscriptionUpdate

router = APIRouter(prefix="/subscriptions", tags=["subscriptions"])


@router.post("/", response_model=SubscriptionPublic)
def create_subscription(subscription: SubscriptionCreate, session: SessionDep):
    """
    Creates subscription and adds it to the database.
    """
    # TODO: Implement
    pass