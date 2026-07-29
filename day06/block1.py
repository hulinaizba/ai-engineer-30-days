# day06/block1.py
# Дима Еженков — День 6, Блок 1: NumPy
# Дата: 29.07.2026

import numpy as np

# === Задача 1 ===
arr = np.array([10, 20, 30, 40, 50])

print("Массив:", arr)
print("Сумма:", arr.sum())
print("Среднее:", arr.mean())
print("Максимум:", arr.max())
print("Минимум:", arr.min())
print("Стандартное отклонение:", arr.std())
# === Задача 2 ===
arr2 = np.arange(1, 21)
print("\nЧётные числа от 1 до 20:", arr2[arr2 % 2 == 0])

# === Задача 3 ===
temps_c = np.array([15.5, 18.0, 21.3, 19.8, 16.2])
temps_f = temps_c * 9/5 + 32
print("\nТемпературы в °F:", temps_f)

# === Задача 4 ===
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("\nМатрица:")
print(matrix)
print("Форма (shape):", matrix.shape)
print("Сумма по столбцам:", matrix.sum(axis=0))
print("Сумма по строкам:", matrix.sum(axis=1))