import sqlite3

# Создание и подключение к базе данных hw.db
conn = sqlite3.connect('hw.db')
cursor = conn.cursor()

# 1. Создание таблицы products
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title TEXT NOT NULL,
        price REAL NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    )
''')
conn.commit()

# 2. Функция для добавления 15 различных товаров в БД
def add_products():
    products = [
        ('Мыло детское', 50.00, 20),
        ('Жидкое мыло с запахом ванили', 120.00, 10),
        ('Шампунь', 200.50, 15),
        ('Зубная паста', 85.00, 30),
        ('Туалетная бумага', 30.50, 50),
        ('Гель для душа', 150.75, 25),
        ('Крем для рук', 65.00, 40),
        ('Бритва одноразовая', 45.00, 60),
        ('Пена для бритья', 99.99, 22),
        ('Лосьон после бритья', 110.00, 10),
        ('Шампунь для сухих волос', 250.00, 8),
        ('Тканевые маски для лица', 80.00, 30),
        ('Крем для лица', 150.00, 12),
        ('Салфетки влажные', 25.00, 100),
        ('Гель для умывания', 70.00, 18)
    ]
    
    cursor.executemany('''
        INSERT INTO products (product_title, price, quantity) 
        VALUES (?, ?, ?)
    ''', products)
    
    conn.commit()

# 3. Функция для изменения количества товара по id
def update_quantity(product_id, new_quantity):
    cursor.execute('''
        UPDATE products
        SET quantity = ?
        WHERE id = ?
    ''', (new_quantity, product_id))
    conn.commit()

# 4. Функция для изменения цены товара по id
def update_price(product_id, new_price):
    cursor.execute('''
        UPDATE products
        SET price = ?
        WHERE id = ?
    ''', (new_price, product_id))
    conn.commit()

# 5. Функция для удаления товара по id
def delete_product(product_id):
    cursor.execute('''
        DELETE FROM products
        WHERE id = ?
    ''', (product_id,))
    conn.commit()

# 6. Функция для выбора всех товаров из БД и вывода их в консоль
def select_all_products():
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    for product in products:
        print(product)

# 7. Функция для выбора товаров, которые дешевле 100 сомов и количество которых больше 5
def select_products_under_price_and_quantity(price_limit=100, quantity_limit=5):
    cursor.execute('''
        SELECT * FROM products 
        WHERE price < ? AND quantity > ?
    ''', (price_limit, quantity_limit))
    products = cursor.fetchall()
    for product in products:
        print(product)

# 8. Функция для поиска товара по названию
def search_product_by_name(search_term):
    cursor.execute('''
        SELECT * FROM products 
        WHERE product_title LIKE ?
    ''', ('%' + search_term + '%',))
    products = cursor.fetchall()
    for product in products:
        print(product)

# Тестирование всех функций
if __name__ == "__main__":
    # 1. Добавляем 15 товаров в таблицу
    add_products()

    # 2. Изменяем количество товара с id = 1
    update_quantity(1, 50)
    
    # 3. Изменяем цену товара с id = 2
    update_price(2, 99.99)
    
    # 4. Удаляем товар с id = 3
    delete_product(3)
    
    # 5. Выводим все товары
    print("Все товары:")
    select_all_products()

    # 6. Выводим товары, которые дешевле 100 сомов и количество которых больше 5
    print("\nТовары дешевле 100 сомов и с количеством больше 5:")
    select_products_under_price_and_quantity()
    
    # 7. Ищем товары по названию "мыло"
    print("\nТовары с названием, содержащим 'мыло':")
    search_product_by_name("мыло")

# Закрываем соединение
conn.close()