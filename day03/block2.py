# day03/block2.py
# Дима Еженков — День 3, Блок 2: Файлы
# Дата: 23.07.2026


# === Задача 6 ===
# Записываем список покупок
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Молоко\n")
    f.write("Хлеб\n")
    f.write("Яйца\n")

# Читаем и выводим с номерами
print("=== Содержимое notes.txt ===")
with open("notes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for i, line in enumerate(lines, 1):
        print(f"{i}. {line.strip()}")




# === Задача 7 ===
print("\n=== Анализ words.txt ===")

with open("words.txt", "r", encoding="utf-8") as f:
    words = [line.strip() for line in f if line.strip()]

print("Количество слов:", len(words))

# Самое длинное слово
longest = words[0]
for word in words:
    if len(word) > len(longest):
        longest = word
print("Самое длинное слово:", longest)

# Слова длиннее 5 букв
print("Слова длиннее 5 букв:")
for word in words:
    if len(word) > 5:
        print("-", word)



# === Задача 8 ===
from datetime import datetime

print("\n=== Дневник ===")
entry = input("Напиши запись в дневник: ")

with open("diary.txt", "a", encoding="utf-8") as f:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"[{now}] {entry}\n")

print("Запись добавлена в diary.txt")





# === Задача 9 ===
print("\n=== Копирование words.txt в верхний регистр ===")

with open("words.txt", "r", encoding="utf-8") as source:
    words = source.readlines()

with open("words_upper.txt", "w", encoding="utf-8") as target:
    for word in words:
        target.write(word.upper())

print("Файл words_upper.txt создан")
