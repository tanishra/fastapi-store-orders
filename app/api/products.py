from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from ..database import get_session
from .. import crud, models, schemas

router = APIRouter(tags=["Products"])

@router.post("/products", response_model=schemas.ProductRead, status_code=201)
def create_product(product: schemas.ProductCreate, session: Session = Depends(get_session)):
    if crud.get_product_by_sku(session, product.sku):
        raise HTTPException(409, "SKU already exists")
    return crud.create_product(session, models.Product(**product.dict()))

@router.get("/products", response_model=list[schemas.ProductRead])
def list_products(session: Session = Depends(get_session)):
    return crud.list_products(session)

@router.get("/products/{product_id}", response_model=schemas.ProductRead)
def get_product(product_id: int, session: Session = Depends(get_session)):
    db_product = crud.get_product(session, product_id)
    if not db_product:
        raise HTTPException(404, "Product not found")
    return db_product

@router.put("/products/{product_id}", response_model=schemas.ProductRead)
def update_product(product_id: int, updates: schemas.ProductUpdate, session: Session = Depends(get_session)):
    db_product = crud.get_product(session, product_id)
    if not db_product:
        raise HTTPException(404, "Product not found")
    return crud.update_product(session, db_product, updates.dict(exclude_unset=True))

@router.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: int, session: Session = Depends(get_session)):
    db_product = crud.get_product(session, product_id)
    if not db_product:
        raise HTTPException(404, "Product not found")
    crud.delete_product(session, db_product)
