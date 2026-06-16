# Flask E-Commerce Website

## Project Overview

This project is a beginner-to-intermediate E-Commerce Website built using Flask and MySQL.

The main purpose of this project was to learn how a real online shopping website works and how frontend, backend, and database communicate with each other.

Users can register, login, view products, add products to cart, place orders, add reviews, and save products to wishlist.

---

# Technologies Used

* Python
* Flask
* MySQL
* HTML
* CSS
* Jinja2
* Session Management

---

# Project Features

## 1. User Registration

Users can create a new account.

Route:

```python
/register
```

Data is stored in:

```text
users table
```

Purpose:

Allows new users to use the website.

---

## 2. User Login

Users can login using username and password.

Route:

```python
/login
```

After successful login:

```python
session["user"] = username
```

Purpose:

Identifies the current logged-in user.

---

## 3. Product Listing

Homepage displays all products from the database.

Route:

```python
/
```

Query Used:

```sql
SELECT * FROM products
```

Purpose:

Shows all available products to customers.

---

## 4. Product Details Page

Users can click on a product to view complete details.

Route:

```python
/product/<id>
```

Information displayed:

* Product Name
* Price
* Image
* Description
* Reviews
* Average Rating

Purpose:

Allows users to see complete information before purchasing.

---

## 5. Shopping Cart

Users can add products to cart.

Route:

```python
/add_to_cart/<id>
```

Cart is stored in Flask Session.

Example:

```python
session["cart"]
```

Purpose:

Temporarily stores products selected by the user.

---

## 6. Cart Management

Users can:

* View Cart
* Remove Items
* Calculate Total Price

Routes:

```python
/cart
/remove/<index>
```

Purpose:

Manage products before checkout.

---

## 7. Checkout System

Users can review products before placing an order.

Route:

```python
/checkout
```

Purpose:

Final confirmation page before order placement.

---

## 8. Order Management

When a user places an order, product details are stored in the orders table.

Routes:

```python
/place_order
/orders
```

Purpose:

Keeps purchase history of users.

---

## 9. Product Categories

Products are grouped by category.

Examples:

* Electronics
* Fashion
* Footwear
* Books

Route:

```python
/category/<id>
```

Purpose:

Makes product browsing easier.

---

## 10. Product Reviews

Users can submit ratings and reviews.

Route:

```python
/add_review/<product_id>
```

Stored In:

```text
reviews table
```

Fields:

* username
* rating
* review
* created_at

Purpose:

Allows customers to share product experiences.

---

## 11. Average Rating

Average rating is calculated using:

```sql
SELECT AVG(rating)
```

Purpose:

Shows overall customer satisfaction.

Example:

```text
Average Rating: 4.8 ⭐
```

---

## 12. Wishlist System

Users can save products for later.

Routes:

```python
/add_wishlist/<product_id>
/wishlist
```

Purpose:

Users can keep favorite products without adding them to cart.

---

## 13. Duplicate Wishlist Protection

Before adding a product to wishlist, the application checks whether it already exists.

Query:

```sql
SELECT *
FROM wishlist
WHERE username=%s
AND product_id=%s
```

Purpose:

Prevents the same product from being added multiple times.

---

# Database Tables

## users

Stores user accounts.

Fields:

* id
* username
* password

---

## products

Stores product information.

Fields:

* id
* name
* price
* image
* description
* category_id

---

## categories

Stores product categories.

Fields:

* id
* name

---

## orders

Stores placed orders.

Fields:

* id
* username
* product_name
* price

---

## reviews

Stores product reviews.

Fields:

* id
* product_id
* username
* rating
* review
* created_at

---

## wishlist

Stores favorite products.

Fields:

* id
* username
* product_id

---

# Project Flow

```text
Register
   ↓
Login
   ↓
View Products
   ↓
Product Details
   ↓
Add To Cart
   ↓
Checkout
   ↓
Place Order
   ↓
Orders
```

---

# What I Learned

During this project I learned:

* Flask Routing
* HTML Forms
* Jinja2 Templates
* Session Management
* CRUD Operations
* MySQL Queries
* File Upload
* Product Management
* User Authentication
* Shopping Cart Logic
* Order Processing
* Reviews System
* Wishlist System
* Category Filtering

---

# Future Improvements

Features planned for future versions:

* Password Hashing
* Product Search
* Payment Gateway
* Admin Authentication
* Order Tracking
* REST API
* JWT Authentication
* Email Notifications
* Stock Management

---








## Day 30 - Coupon & Payment System

### Features Added

- Coupon Code System
- Discount Calculation
- Payment Method Selection (COD / Online)
- Payment Status
- Payment Success Page
- Order Tracking Status
- Admin Order Management

### Technologies Used

- Python
- Flask
- MySQL
- HTML
- CSS
- Jinja2

### New Pages

- checkout.html
- payment_success.html
- orders.html

### Database Changes

orders table:
- total_amount
- discount
- payment_method
- payment_status
- order_status
















# Day 31 - Order Tracking & Admin Order Management

## Features Added

### 1. Order Status Tracking

Users can now see the current status of their orders.

Possible Status Values:

* Pending
* Shipped
* Delivered

Example:

| Product | Status    |
| ------- | --------- |
| Laptop  | Pending   |
| Mobile  | Shipped   |
| Watch   | Delivered |

---

### 2. Color-Based Status Display

Order status is displayed with different colors.

* 🔴 Pending = Red
* 🟠 Shipped = Orange
* 🟢 Delivered = Green

Implemented in:

```html
orders.html
```

Using:

```jinja2
{% if order.order_status == "Pending" %}
<span style="color:red;">
Pending
</span>

{% elif order.order_status == "Shipped" %}
<span style="color:orange;">
Shipped
</span>

{% elif order.order_status == "Delivered" %}
<span style="color:green;">
Delivered
</span>
{% endif %}
```

---

### 3. Admin Order Management

New Route:

```python
/admin/orders
```

Admin can view all customer orders.

Query:

```python
SELECT *
FROM orders
ORDER BY id DESC
```

Purpose:

Allows admin to manage and track all orders.

---

### 4. Update Order Status

New Route:

```python
/update_order_status/<id>/<status>
```

Admin can update order status.

Examples:

```text
Pending
Shipped
Delivered
```

Purpose:

Simulates real e-commerce order tracking.

---

### 5. Navigation Update

Added new navigation link:

```html
<a href="/admin/orders">
Manage Orders
</a>
```

Purpose:

Quick access to admin order management page.

---

## Database Changes

Added Column:

```sql
ALTER TABLE orders
ADD order_status VARCHAR(50);
```

Default Values:

```text
Pending
Shipped
Delivered
```

---

## What I Learned

* Order Tracking System
* Admin Order Management
* Status Updates
* Dynamic Jinja2 Conditions
* Database Table Alteration
* Real-World E-Commerce Workflow
* Order Lifecycle Management







+--------------------------------------------------+
|            FLASK E-COMMERCE WEBSITE              |
+--------------------------------------------------+
                        |
                        ▼
+------------------+
| User Register    |
+------------------+
        |
        ▼
+------------------+
| User Login       |
+------------------+
        |
        ▼
+------------------+
| Home Page        |
| View Products    |
+------------------+
        |
        ▼
+------------------+
| Product Details  |
+------------------+
        |
        ├─────────────► Add Review
        |
        ├─────────────► Add Wishlist
        |
        ▼
+------------------+
| Add To Cart      |
+------------------+
        |
        ▼
+------------------+
| Cart Page        |
| Remove Products  |
| Calculate Total  |
+------------------+
        |
        ▼
+------------------+
| Checkout         |
+------------------+
        |
        ├─────────────► Apply Coupon
        |
        ├─────────────► Select Payment
        |              (COD / Online)
        |
        ▼
+------------------+
| Place Order      |
+------------------+
        |
        ▼
+------------------+
| Payment Success  |
+------------------+
        |
        ▼
+------------------+
| My Orders        |
+------------------+
        |
        ▼
+------------------+
| Order Tracking   |
| Pending          |
| Shipped          |
| Delivered        |
+------------------+
        |
        ▼
+------------------+
| Admin Panel      |
+------------------+
        |
        ├─────────────► Add Product
        |
        ├─────────────► Edit Product
        |
        ├─────────────► Delete Product
        |
        ▼
+------------------+
| Manage Orders    |
| Update Status    |
+------------------+