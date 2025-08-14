# Store Orders & Products API

A simple **FastAPI** project to manage store orders, products, and payments.  
This project also processes webhook events to update order payment status.  
Uses **SQLite** for database storage and **SQLModel** ORM for clean, beginner-friendly code.

--- 
## Live Demo
[Click here to view the deployed API](https://your-deployed-link.com)

---

## Features
- **Products Management**
  - Create new products
  - View products 
  - Update product details
  - Delete products
- **Orders Management**
  - Create new orders
  - View orders
- **Payments**
  - Handle payment status updates via webhooks

---

## Tech Stack
- **FastAPI** – Web framework
- **SQLite** – Lightweight database
- **SQLModel** – ORM for database operations
- **Uvicorn** – ASGI server

--- 

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/tanishra/store-orders-products-api.git
cd store-orders-products-api
```

### 2. Create a virtual environment & activate it
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
uvicorn app.main:app --reload
```

---

## 📌 API Endpoints

### 🛍️ Products
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/products/`             | Create a new product |
| GET    | `/products/`             | Get all products |
| GET    | `/products/{product_id}` | Get details of a specific product |
| PUT    | `/products/{product_id}` | Update a product |
| DELETE | `/products/{product_id}` | Delete a product |

---

### 📦 Orders
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/orders/`             | Create a new order |
| GET    | `/orders/`             | Get all orders |
| GET    | `/orders/{order_id}`   | Get details of a specific order |

---

### 🔔 Webhooks
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/webhooks/payment` | Update order status after payment |

---

## 🤝 Open Contribution
We’d love your help to make this project even better!  
Whether you’re fixing a bug, adding a cool feature, or just improving documentation — every contribution counts. 💡

Here’s how you can join in:
1. 🍴 **Fork** this repository  
2. 🌱 **Create** a new branch for your change  
3. 💻 **Make** your improvements  
4. 📬 **Open** a pull request and share your awesome work with us!