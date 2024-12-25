from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query, Path
from sqlmodel import select
from app.core.db import SessionDep
from app.models import Subscription, SubscriptionBase, SubscriptionCreate, SubscriptionFrequency, SubscriptionPublic, SubscriptionUpdate, User
from app.core.security import CurrentUser

router = APIRouter(prefix="/subscriptions", tags=["subscriptions"])


@router.post("/", response_model=SubscriptionPublic)
def create_subscription(subscription: SubscriptionCreate, session: SessionDep, current_user: CurrentUser,):
    """
    Creates subscription and adds it to the database.
    """

    #Check if the user in the object is the same as the user in the session
    if current_user.id != subscription.user_id:
        raise HTTPException(status_code=403, detail="Unauthorized to post to this user_id")

    # Check if the user exists
    user = session.exec(select(User).where(User.id == subscription.user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    
    # Check if a subscription with the same name exists for the user
    existing_subscription = session.exec(
        select(Subscription).where(
            (Subscription.user_id == subscription.user_id) &
            (Subscription.name == subscription.name)
        )
    ).first()
    if existing_subscription:
        raise HTTPException(status_code=400, detail="Subscription with this name already exists for the user.")
    
    # Adding subscription to the database
    db_subscription = Subscription.model_validate(subscription)
    session.add(db_subscription)
    session.commit()
    session.refresh(db_subscription)

    return db_subscription


@router.get("/", response_model=list[SubscriptionPublic])
def get_user_subscriptions(session: SessionDep, current_user: CurrentUser):
    """
    Retrieve all subscriptions for a given user using a query parameter.
    """

    # Get user_id from the CurrentUser

    # Validate that the user exists
    user = session.exec(select(User).where(User.id == current_user.id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")

    # Query for all subscriptions of the user
    subscriptions = session.exec(select(Subscription).where(Subscription.user_id == current_user.id)).all()

    return subscriptions


@router.patch("/{subscription_id}", response_model=SubscriptionPublic)
def update_hero(subscription_id: Annotated[int, Path(title="The ID of the item to update")], subscription: SubscriptionUpdate, session: SessionDep, current_user: CurrentUser):
    """
    Update details of a subscription by ID.
    """
        
    # Retrieve the subscription by ID
    subscription_db = session.get(Subscription, subscription_id)
    if not subscription_db:
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    # Check if the current user actually owns the item
    if current_user.id != subscription_db.user_id:
        raise HTTPException(status_code=403, detail="Unauthorized to edit")
    

    # Updating the instance 
    subscription_data = subscription.model_dump(exclude_unset=True)
    subscription_db.sqlmodel_update(subscription_data)
    session.add(subscription_db)
    session.commit()
    session.refresh(subscription_db)

    return subscription_db


@router.delete("/{subscription_id}")
def delete_hero(subscription_id: Annotated[int, Path(title="The ID of the item to delete")], session: SessionDep, current_user: CurrentUser):

    # Retrieve the subscription by ID
    subscription_db = session.get(Subscription, subscription_id)
    if not subscription_db:
        raise HTTPException(status_code=404, detail="Hero not found")
    
    # Check if the current user actually owns the item
    if current_user.id != subscription_db.user_id:
        raise HTTPException(status_code=403, detail="Unauthorized to edit")
        
    # Delete the instance
    session.delete(subscription_db)
    session.commit()
    return {"ok": True}