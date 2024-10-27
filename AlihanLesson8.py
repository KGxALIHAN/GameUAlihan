import sqlite3

# Шаг 1: Создание базы данных и таблицы countries
def create_database():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area REAL DEFAULT 0,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries(id)
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities(id)
    )''')

    conn.commit()
    conn.close()

# Шаг 2: Добавление стран
def add_countries():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    countries = [('Кыргызстан',), ('Германия',), ('Китай',)]
    cursor.executemany('INSERT INTO countries (title) VALUES (?)', countries)

    conn.commit()
    conn.close()

# Шаг 3: Добавление городов
def add_cities():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    cities = [
        ('Бишкек', 160, 1),
        ('Ош', 182, 1),
        ('Берлин', 891, 2),
        ('Мюнхен', 310, 2),
        ('Пекин', 16410, 3),
        ('Шанхай', 6340, 3),
        ('Гуанчжоу', 7434, 3)
    ]
    cursor.executemany('INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)', cities)

    conn.commit()
    conn.close()

# Шаг 4: Добавление учеников
def add_students():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    students = [
        ('Айдар', 'Иванов', 1),
        ('Алина', 'Петрова', 2),
        ('Бермет', 'Сидорова', 3),
        ('Алекс', 'Смирнов', 4),
        ('Майя', 'Ким', 5),
        ('Елена', 'Ли', 6),
        ('Чжан', 'Ван', 7),
        ('Иван', 'Сергеев', 1),
        ('Михаил', 'Антонов', 2),
        ('Жанна', 'Сабирова', 3),
        ('Лю', 'Ван', 4),
        ('Ли', 'Парк', 5),
        ('Дмитрий', 'Кузнецов', 6),
        ('Сергей', 'Иванов', 7),
        ('Мария', 'Соколова', 1)
    ]
    cursor.executemany('INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)', students)

    conn.commit()
    conn.close()

# Шаг 5: Основная программа для отображения списка учеников по городу
def show_students():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id, title FROM cities')
    cities = cursor.fetchall()

    print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

    for city in cities:
        print(f"{city[0]}. {city[1]}")

    while True:
        try:
            city_id = int(input("Введите id города: "))
            if city_id == 0:
                print("Выход из программы.")
                break

            cursor.execute('''
                SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
                FROM students
                JOIN cities ON students.city_id = cities.id
                JOIN countries ON cities.country_id = countries.id
                WHERE cities.id = ?
            ''', (city_id,))
            students = cursor.fetchall()

            if students:
                for student in students:
                    print(f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь города: {student[4]}")
            else:
                print("В этом городе нет учеников.")

        except ValueError:
            print("Пожалуйста, введите числовое значение id.")
        except Exception as e:
            print(f"Ошибка: {e}")

    conn.close()

# Инициализация и запуск всех функций
create_database()
add_countries()
add_cities()
add_students()
show_students()
