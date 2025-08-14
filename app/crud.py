from sqlmodel import Session, select
from .models import Product, Order

# Product operations
def create_product(session: Session, product: Product):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

def get_product(session: Session, product_id: int):
    return session.get(Product, product_id)

def get_product_by_sku(session: Session, sku: str):
    return session.exec(select(Product).where(Product.sku == sku)).first()

def list_products(session: Session):
    return session.exec(select(Product)).all()

def update_product(session: Session, db_product: Product, updates: dict):
    for key, value in updates.items():
        setattr(db_product, key, value)
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product

def delete_product(session: Session, db_product: Product):
    session.delete(db_product)
    session.commit()

# Order operations
def create_order(session: Session, order: Order):
    product = session.get(Product, order.product_id)
    if not product:
        return None, "Product not found"
    if product.stock < order.quantity:
        return None, "Insufficient stock"
    product.stock -= order.quantity
    session.add(order)
    session.commit()
    session.refresh(order)
    return order, None

def get_order(session: Session, order_id: int):
    return session.get(Order, order_id)
