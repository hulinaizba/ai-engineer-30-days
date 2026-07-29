# day06/block2.py
# Дима Еженков — День 6, Блок 2: Pandas DataFrame
# Дата: 29.07.2026

import pandas as pd

# === Задача 5 ===
data = {
    "name": ["Аня", "Борис", "Вика", "Глеб", "Даша"],
    "age": [28, 35, 24, 41, 30],
    "department": ["IT", "HR", "IT", "Sales", "HR"],
    "salary": [85000, 55000, 72000, 48000, 61000]
}

df = pd.DataFrame(data)

print("=== Вся таблица ===")
print(df)

print("\n=== head(3) ===")
print(df.head(3))

print("\n=== info() ===")
print(df.info())

print("\n=== describe() ===")
print(df.describe())

# === Задача 6 ===
print("\n=== Только зарплаты ===")
print(df["salary"])

print("\n=== Зарплата > 50000 ===")
print(df[df["salary"] > 50000])

print("\nСредний возраст:", df["age"].mean())

# === Задача 7 ===
print("\n=== Сортировка по зарплате (убывание) ===")
print(df.sort_values("salary", ascending=False))

# === Задача 8 ===
print("\n=== Средняя зарплата по департаментам ===")
print(df.groupby("department")["salary"].mean())