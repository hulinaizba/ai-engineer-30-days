# day03/block1.py
# Дима Еженков — День 3, Блок 1: Списки и словари
# Дата: 23.07.2026

# === Задача 1 ===
grades = [4, 5, 3, 5, 4, 2, 5, 3]

# 1. Количество пятёрок
fives = grades.count(5)
print("Количество пятёрок:", fives)

# 2. Отсортированный список
sorted_grades = sorted(grades)
print("Отсортированный список:", sorted_grades)

# 3. Новый список без двоек
no_twos = []
for grade in grades:
    if grade != 2:
        no_twos.append(grade)

print("Список без двоек:", no_twos)


# === Задача 2 ===
student = {
    "name": "Дима",
    "age": 30,
    "skills": ["Python", "Git"],
    "grades": {
        "math": 5,
        "python": 4
    }
}

# Добавляем новый навык
student["skills"].append("Docker")

# Меняем оценку
student["grades"]["python"] = 5

# Выводим все ключи и значения
print("\n=== Данные студента ===")
for key, value in student.items():
    print(key, "→", value)


   # === Задача 3 ===
text = "apple banana apple cherry banana apple"
words = text.split()

freq = {}
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("\n=== Частота слов ===")
print(freq)




# === Задача 4 ===
names = ["Аня", "Макс", "Лена"]
scores = [85, 92, 78]

# Создаём словарь через zip
students = dict(zip(names, scores))
print("\n=== Словарь студентов ===")
print(students)

# Находим имя с максимальным баллом
max_score = 0
best_student = ""

for name, score in students.items():
    if score > max_score:
        max_score = score
        best_student = name

print(f"Лучший студент: {best_student} с баллом {max_score}")




# === Задача 5 ===
products = [
    {"name": "Ноутбук", "price": 4500, "in_stock": True},
    {"name": "Мышь", "price": 150, "in_stock": True},
    {"name": "Клавиатура", "price": 300, "in_stock": False},
    {"name": "Монитор", "price": 1200, "in_stock": True}
]

print("\n=== Товары в наличии ===")
for product in products:
    if product["in_stock"]:
        print(product["name"], "-", product["price"])

# Самый дорогой товар
most_expensive = products[0]
for product in products:
    if product["price"] > most_expensive["price"]:
        most_expensive = product

print("\nСамый дорогой товар:", most_expensive["name"], "-", most_expensive["price"])

# Средняя цена
total_price = 0
for product in products:
    total_price += product["price"]

average_price = total_price / len(products)
print("Средняя цена:", round(average_price, 2))