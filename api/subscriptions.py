from fastapi import APIRouter, HTTPException, status, Query
from typing import List
from pydantic import BaseModel
import logging

router = APIRouter()

class Subscription(BaseModel):
    id: int
    user_id: int
    level: str

subscriptions_db = {}

@router.post("/", response_model=Subscription, status_code=status.HTTP_201_CREATED)
async def create_subscription(subscription: Subscription):
    if subscription.id in subscriptions_db:
        logging.warning(f"Subscription creation failed: ID {subscription.id} already exists")
        raise HTTPException(status_code=400, detail="Subscription already exists")
    subscriptions_db[subscription.id] = subscription
    logging.info(f"Subscription created: {subscription.id}")
    return subscription

@router.get("/", response_model=List[Subscription])
async def list_subscriptions(skip: int = 0, limit: int = Query(100, le=100)):
    logging.debug(f"Listing subscriptions: skip {skip}, limit {limit}")
    return list(subscriptions_db.values())[skip:skip+limit]

@router.get("/{subscription_id}", response_model=Subscription)
async def get_subscription(subscription_id: int):
    subscription = subscriptions_db.get(subscription_id)
    if not subscription:
        logging.warning(f"Subscription not found: ID {subscription_id}")
        raise HTTPException(status_code=404, detail="Subscription not found")
    return subscription
