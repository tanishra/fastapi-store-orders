from fastapi import FastAPI
from .database import init_db
from .api import products, orders, webhooks

app = FastAPI(
    title="Store Orders API",
    version="1.0",
    description="A FastAPI service to manage store orders, process payments, and handle webhooks."
)

app.include_router(products.router)
app.include_router(orders.router)
app.include_router(webhooks.router)

@app.on_event("startup")
def on_startup():
    init_db()
