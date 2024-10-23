import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title TEXT NOT NULL,
        price REAL NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    )
''')
conn.commit()

def add_products():
    products = [
        ('Хлеб пшеничный', 40.00, 100),
        ('Молоко пастеризованное', 55.50, 50),
        ('Сыр голландский', 300.75, 30),
        ('Йогурт клубничный', 75.00, 60),
        ('Масло сливочное', 450.99, 20),
        ('Кофе молотый', 250.00, 40),
        ('Чай черный', 120.00, 80),
        ('Шоколад молочный', 180.00, 25),
        ('Мука высшего сорта', 90.00, 100),
        ('Макароны спагетти', 65.00, 75),
        ('Сахар белый', 60.00, 90),
        ('Соль поваренная', 25.00, 200),
        ('Куриное филе', 400.00, 15),
        ('Яйца куриные', 75.00, 150),
        ('Томатная паста', 125.00, 35)
    ]
    
    cursor.executemany('''
        INSERT INTO products (product_title, price, quantity) 
        VALUES (?, ?, ?)
    ''', products)
    
    conn.commit()

def update_quantity(product_id, new_quantity):
    cursor.execute('''
        UPDATE products
        SET quantity = ?
        WHERE id = ?
    ''', (new_quantity, product_id))
    conn.commit()

def update_price(product_id, new_price):
    cursor.execute('''
        UPDATE products
        SET price = ?
        WHERE id = ?
    ''', (new_price, product_id))
    conn.commit()

def delete_product(product_id):
    cursor.execute('''
        DELETE FROM products
        WHERE id = ?
    ''', (product_id,))
    conn.commit()

def select_all_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    for product in products:
        print(product)

def select_products_under_price_and_quantity(price_limit=100, quantity_limit=5):
    cursor.execute('''
        SELECT * FROM products 
        WHERE price < ? AND quantity > ?
    ''', (price_limit, quantity_limit))
    products = cursor.fetchall()
    for product in products:
        print(product)

def search_product_by_name(search_term):
    cursor.execute('''
        SELECT * FROM products 
        WHERE product_title LIKE ?
    ''', ('%' + search_term + '%',))
    products = cursor.fetchall()
    for product in products:
        print(product)

if __name__ == "__main__":
    add_products()
    update_quantity(1, 50)
    update_price(2, 99.99)
    delete_product(3)
    
    print("Все товары:")
    select_all_products()

    print("\nТовары дешевле 100 сомов и с количеством больше 5:")
    select_products_under_price_and_quantity()
    
    print("\nТовары с названием, содержащим 'молоко':")
    search_product_by_name("молоко")

conn.close()
