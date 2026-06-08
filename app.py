from flask import Flask,render_template,redirect
from flask import session,request

import mysql.connector

import os

from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER



app.secret_key = "mysecretkey"

conn = mysql.connector.connect(

    host="localhost",

    user="root",

    password="Root@123",

    database="ecommerce"

)

cursor = conn.cursor(dictionary=True)

@app.route("/")
def home():

    cart = session.get("cart", [])

    user = session.get("user")

    cursor.execute("""

    SELECT

    products.*,

    categories.name AS category_name

    FROM products

    LEFT JOIN categories

    ON products.category_id = categories.id

    """)

    products = cursor.fetchall()

    cursor.execute(

        "SELECT * FROM categories"

    )

    categories = cursor.fetchall()

    return render_template(

        "index.html",

        products=products,

        categories=categories,

        cart_count=len(cart),

        user=user

    )


@app.route("/product/<int:id>")
def product_details(id):

    query = """

    SELECT *

    FROM products

    WHERE id=%s

    """

    cursor.execute(query, (id,))

    product = cursor.fetchone()

    cursor.execute("""

    SELECT *

    FROM reviews

    WHERE product_id=%s

    ORDER BY id DESC

    """, (id,))

    reviews = cursor.fetchall()

    cursor.execute("""

    SELECT AVG(rating)
    AS average_rating

    FROM reviews

    WHERE product_id=%s

    """, (id,))

    avg = cursor.fetchone()

    if avg["average_rating"] is None:
        avg["average_rating"] = 0

    cart = session.get("cart", [])

    user = session.get("user")

    return render_template(

        "product.html",

        product=product,

        reviews=reviews,

        average_rating=avg,

        cart_count=len(cart),

        user=user,

        id=id

    )












@app.route("/add_to_cart/<int:id>")
def add_to_cart(id):

    if "user" not in session:
        return redirect("/login")

    query = "SELECT * FROM products WHERE id=%s"

    cursor.execute(query, (id,))

    product = cursor.fetchone()

    cart = session.get("cart", [])

    cart.append(product)

    session["cart"] = cart

    return redirect("/cart")


@app.route("/cart")
def cart():
    cart_items = session.get("cart",[])

    total = 0
    
    for item in cart_items:
        total += item["price"]
    
    user = session.get("user")

    return render_template("cart.html",cart=cart_items,total=total,user=user)




@app.route("/remove/<int:index>")
def remove(index):
    cart = session.get("cart",[])

    cart.pop(index)

    session["cart"] = cart

    return redirect("/cart")


@app.route("/register",methods=['GET','POST'])
def register():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        query = """
        INSERT INTO users(username,password) VALUES(%s,%s)

        """
        values = (username,password)

        cursor.execute(query,values)

        conn.commit()

        return redirect("/login")
    
    return render_template("register.html")



@app.route("/login",methods=['GET','POST'])
def login():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        query = """
        SELECT * FROM users
        WHERE username=%s AND password=%s
        """

        values = (username, password)

        cursor.execute(query, values)

        user = cursor.fetchone()

        if user:

            session["user"] = username

            return redirect("/")


        
        else:

            return "Invalid Username and Passsword"
    
    return render_template("login.html")




@app.route("/logout")
def logout():

    session.pop("user",None)

    return redirect("/")







@app.route("/admin")
def admin():

    query = "SELECT * FROM products"

    cursor.execute(query)

    products = cursor.fetchall()

    return render_template("admin.html",products=products)


@app.route("/add_product", methods=["GET", "POST"])
def add_products():

    if request.method == "POST":

        name = request.form["name"]
        price = request.form["price"]
        description = request.form["description"]
        category_id = request.form["category_id"]

        image = request.files["image"]

        filename = secure_filename(
            image.filename
        )

        image.save(
            os.path.join(
                app.config["UPLOAD_FOLDER"],
                filename
            )
        )

        query = """INSERT INTO products
                (name, price, image, description, category_id)
                VALUES(%s,%s,%s,%s,%s)"""

        values = (
            name,
            price,
            filename,
            description
            ,category_id
        )

        cursor.execute(query, values)

        conn.commit()

        return redirect("/admin")

    cursor.execute("SELECT * FROM categories")

    categories = cursor.fetchall()

    return render_template("add_product.html",categories=categories)
    
    




@app.route("/edit_product/<int:id>",
methods=["GET", "POST"])

def edit_product(id):

    if request.method == "POST":

        name = request.form["name"]

        price = request.form["price"]

        image = request.form["image"]

        description = request.form["description"]

        query = """
        UPDATE products

        SET

        name=%s,
        price=%s,
        image=%s,
        description=%s

        WHERE id=%s
        """

        values = (
            name,
            price,
            image,
            description,
            id
        )

        cursor.execute(query, values)

        conn.commit()

        return redirect("/admin")

    query = "SELECT * FROM products WHERE id=%s"

    cursor.execute(query, (id,))

    product = cursor.fetchone()

    return render_template(
        "edit_product.html",
        product=product
    )







@app.route("/delete_product/<int:id>")
def delete_product(id):

    query = "DELETE FROM products WHERE id=%s"

    cursor.execute(query,(id,))

    conn.commit()

    return redirect("/admin")











@app.route("/checkout")
def checkout():
    
    cart = session.get('cart',[])
    
    total = 0

    for item in cart:
        total += item['price']

    return render_template("checkout.html",cart=cart,total=total)




@app.route("/place_order")
def place_order():

    username = session.get("user")

    cart = session.get("cart", [])

    if not username:

        return redirect("/login")

    for item in cart:

        query = """

        INSERT INTO orders

        (username, product_name, price)

        VALUES(%s,%s,%s)

        """

        values = (

            username,

            item["name"],

            item["price"]

        )

        cursor.execute(query, values)

    conn.commit()

    session["cart"] = []

    return redirect("/orders")






@app.route("/orders")
def orders():

    username = session.get("user")

    if not username:

        return redirect("/login")

    query = """

    SELECT *

    FROM orders

    WHERE username=%s

    ORDER BY id DESC

    """

    cursor.execute(

        query,

        (username,)

    )

    orders = cursor.fetchall()

    return render_template(

        "orders.html",

        orders=orders

    )


@app.route("/category/<int:id>")
def category_products(id):

    cursor.execute("""

    SELECT
    products.*,
    categories.name AS category_name

    FROM products

    LEFT JOIN categories

    ON products.category_id = categories.id

    WHERE products.category_id=%s

    """, (id,))

    products = cursor.fetchall()

    cursor.execute(
        "SELECT * FROM categories"
    )

    categories = cursor.fetchall()

    cart = session.get("cart", [])

    user = session.get("user")

    return render_template(
        "index.html",
        products=products,
        categories=categories,
        cart_count=len(cart),
        user=user
    )















@app.route("/add_review/<int:product_id>",methods=["POST"])
def add_review(product_id):

    username = session.get("user")

    if not username:
        return redirect("/login")
    
    rating = request.form["rating"]

    review = request.form["review"]

    query = "INSERT INTO reviews (product_id,username,rating,review) VALUES(%s,%s,%s,%s)"

    values = (product_id,username,rating,review)

    cursor.execute(query,values)

    conn.commit()

    return redirect(f"/product/{product_id}")









@app.route("/add_wishlist/<int:product_id>")
def add_wishlist(product_id):

    username = session.get("user")

    if not username:
        return redirect("/login")

    # Check existing wishlist item

    check_query = """

    SELECT *

    FROM wishlist

    WHERE username=%s

    AND product_id=%s

    """

    cursor.execute(
        check_query,
        (username, product_id)
    )

    existing = cursor.fetchone()

    if existing:

        return redirect(
            f"/product/{product_id}"
        )

    # Insert only if not exists

    query = """

    INSERT INTO wishlist

    (username,product_id)

    VALUES(%s,%s)

    """

    values = (
        username,
        product_id
    )

    cursor.execute(
        query,
        values
        
    )

    conn.commit()

    return redirect(
        f"/product/{product_id}"
    )












@app.route("/wishlist")
def wishlist():

    username = session.get("user")

    if not username:

        return redirect("/login")

    query = """

    SELECT

    products.*,

    wishlist.id AS wishlist_id

    FROM wishlist

    JOIN products

    ON wishlist.product_id = products.id

    WHERE wishlist.username=%s

    """

    cursor.execute(

        query,

        (username,)

    )

    products = cursor.fetchall()

    return render_template(

        "wishlist.html",

        products=products

    )







@app.route(
"/remove_wishlist/<int:id>"
)
def remove_wishlist(id):

    query = """

    DELETE FROM wishlist

    WHERE id=%s

    """

    cursor.execute(

        query,

        (id,)

    )

    conn.commit()

    return redirect(
        "/wishlist"
    )




if __name__ == "__main__":
    app.run(debug=True)