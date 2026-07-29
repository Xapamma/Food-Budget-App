import sqlite3

def get_connection():
    connection = sqlite3.connect("database/products.db")

    connection.row_factory = sqlite3.Row  # This allows us to access columns by name
    return connection

def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        price REAL NOT NULL,
        calories REAL NOT NULL,
        protein REAL NOT NULL
    )
    ''')

    connection.commit()
    connection.close()

def add_product(product_name, price, calories, protein):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
    INSERT INTO products (product_name, price, calories, protein)
    VALUES (?, ?, ?, ?)
    ''', (product_name, price, calories, protein))

    connection.commit()
    connection.close()

def get_products():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
        SELECT * 
        FROM products
        ORDER BY id DESC
    ''')
    products = cursor.fetchall()

    connection.close()
    return products

print(get_products())