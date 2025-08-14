from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import get_db
from app import models

router = APIRouter(tags=["Webhooks"])

class PaymentEvent(BaseModel):
    order_id: int
    event: str

VALID_EVENTS = ["payment.succeeded", "Paid", "PAID"]

@router.post("/webhooks/payment")
async def payment_webhook(payload: PaymentEvent, db: Session = Depends(get_db)):
    if payload.event not in VALID_EVENTS:
        raise HTTPException(400, "Invalid event")

    # Fetch the order from DB
    order = db.query(models.Order).filter(models.Order.id == payload.order_id).first()
    if not order:
        raise HTTPException(404, f"Order {payload.order_id} not found")

    # Update status
    order.status = "PAID"
    db.commit()
    db.refresh(order)

    return {"detail": f"Order {order.id} marked as PAID"}
