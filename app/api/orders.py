from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from ..database import get_session
from .. import crud, models, schemas

router = APIRouter(tags=["Orders"])

@router.post("/orders", response_model=schemas.OrderRead, status_code=201)
def create_order(order: schemas.OrderCreate, session: Session = Depends(get_session)):
    db_order, error = crud.create_order(session, models.Order(**order.dict()))
    if error:
        raise HTTPException(409, error)
    return db_order

@router.get("/orders/{order_id}", response_model=schemas.OrderRead)
def get_order(order_id: int, session: Session = Depends(get_session)):
    db_order = crud.get_order(session, order_id)
    if not db_order:
        raise HTTPException(404, "Order not found")
    return db_order
