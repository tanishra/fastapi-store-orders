from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sku: str = Field(index=True, unique=True)
    name: str
    price: float = Field(gt=0)
    stock: int = Field(ge=0)

class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="product.id")
    quantity: int = Field(gt=0)
    status: str = Field(default="PENDING")  # PENDING, PAID, SHIPPED, CANCELED
    created_at: datetime = Field(default_factory=datetime.utcnow)
