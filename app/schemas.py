from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductCreate(BaseModel):
    sku: str
    name: str
    price: float
    stock: int

class ProductRead(ProductCreate):
    id: int

class ProductUpdate(BaseModel):
    sku: Optional[str]
    name: Optional[str]
    price: Optional[float]
    stock: Optional[int]

class OrderCreate(BaseModel):
    product_id: int
    quantity: int

class OrderRead(BaseModel):
    id: int
    product_id: int
    quantity: int
    status: str
    created_at: datetime
