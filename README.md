# Flask E-Commerce Website

## Overview

This project is a full-stack E-Commerce web application developed using Python Flask and MySQL. The application simulates the core functionality of a modern online shopping platform, including user authentication, product browsing, shopping cart management, order placement, and product administration.

The goal of this project was to gain practical experience in backend development, database integration, session management, CRUD operations, and building complete web applications using Flask.

---

## Key Features

### User Features

* User Registration
* User Login & Logout
* Browse Products
* View Product Details
* Add Products to Cart
* Remove Products from Cart
* Checkout Process
* Place Orders
* View Order History

### Admin Features

* View All Products
* Add New Products
* Edit Existing Products
* Delete Products
* Manage Product Catalog

---

## Technology Stack

| Layer              | Technology             |
| ------------------ | ---------------------- |
| Backend            | Python                 |
| Framework          | Flask                  |
| Frontend           | HTML, CSS              |
| Template Engine    | Jinja2                 |
| Database           | MySQL                  |
| Database Connector | mysql-connector-python |
| Session Management | Flask Session          |

---

## System Architecture

The application follows a simple three-layer architecture.

```text
┌─────────────────────┐
│     Web Browser     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│     Flask App       │
│      app.py         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      MySQL DB       │
│     ecommerce       │
└─────────────────────┘
```

The browser sends requests to Flask routes. Flask processes the request, communicates with the MySQL database when necessary, and renders HTML templates back to the user.

---

## Application Workflow

### Customer Journey

```text
Home Page
    │
    ▼
View Products
    │
    ▼
Product Details
    │
    ▼
Add To Cart
    │
    ▼
Cart Page
    │
    ▼
Checkout
    │
    ▼
Place Order
    │
    ▼
Orders Table
    │
    ▼
My Orders
```

---

## Authentication Workflow

```text
Register
   │
   ▼
Users Table
   │
   ▼
Login
   │
   ▼
Session Created
   │
   ▼
Access Protected Features
```

The application uses Flask sessions to maintain login state.

After successful authentication:

```python
session["user"] = username
```

The session remains active until logout.

---

## Shopping Cart Workflow

Unlike permanent database storage, the shopping cart is stored temporarily in the Flask session.

```text
Product Selected
       │
       ▼
Add To Cart
       │
       ▼
session["cart"]
       │
       ▼
Cart Page
       │
       ▼
Checkout
```

This allows users to add products without immediately storing them in the database.

---

## Database Design

### Users Table

Stores customer login information.

Fields:

* id
* username
* password

---

### Products Table

Stores all product information displayed on the website.

Fields:

* id
* name
* price
* image
* description

---

### Orders Table

Stores completed orders placed by users.

Fields:

* id
* username
* product_name
* price
* order_date

---

## Database Relationship Overview

```text
Users
  │
  │ places
  ▼
Orders
  ▲
  │ contains
  │
Products
```

A user places orders, and each order contains product information at the time of purchase.

---

## Project Structure

```text
ecommerce_website/

├── app.py

├── templates/
│   ├── index.html
│   ├── product.html
│   ├── cart.html
│   ├── checkout.html
│   ├── orders.html
│   ├── login.html
│   ├── register.html
│   ├── admin.html
│   ├── add_product.html
│   └── edit_product.html

├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── images/
│       ├── laptop.jpg
│       ├── phone.jpg
│       ├── shoes.jpg
│       └── watch.jpg

└── README.md
```

---

## What I Learned

While developing this project, I gained hands-on experience with:

* Flask Routing
* Template Rendering
* Jinja2
* Session Management
* Authentication Systems
* CRUD Operations
* SQL Queries
* MySQL Integration
* Database Design
* E-Commerce Application Flow
* Admin Panel Development
* Order Processing Systems

---

## Future Improvements

The current implementation focuses on learning core concepts. Future enhancements could include:

* Password Hashing
* Product Categories
* Search Functionality
* Stock Management
* Product Reviews
* Wishlist Feature
* Payment Gateway Integration
* Order Tracking
* Email Notifications
* REST API Development
* JWT Authentication
* Role-Based Access Control

---

