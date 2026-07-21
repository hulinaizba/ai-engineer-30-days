# day02/block3.py
# Дима Еженков — День 2, Блок 3: Циклы
# Дата: 22.07.2026





# 9. FizzBuzz
print("=== FizzBuzz ===")
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)





# 10. Сумма всех чётных чисел от 1 до 1000
even_sum = 0
for i in range(2, 1001, 2):
    even_sum += i
print(f"\nСумма всех чётных чисел от 1 до 1000: {even_sum}")





# 11. Таблица умножения
print("\n=== Таблица умножения ===")
try:
    n = int(input("Введите число N: "))
except ValueError:
    print("Введено не целое число. Используется N = 1")
    n = 1
for i in range(1, 11):
    print(f"{n} × {i} = {n * i}")





# 12. Игра «Угадай число"
import random

print("\n=== Игра 'Угадай число' ===")
secret = random.randint(1, 100)
attempts = 0
print("Я загадал число от 1 до 100. Попробуй угадать!")

while True:
    try:
        guess = int(input("Твой вариант: "))
        attempts += 1

        if guess < secret:
            print("Больше")
        elif guess > secret:
            print("Меньше")
        else:
            print(f"🎉 Угадал! Число было {secret}. Попыток: {attempts}")
            break
    except ValueError:
        print("Пожалуйста, введите целое число!")





# 13. Max, min, average без встроенных функций
print("\n=== Статистика списка ===")
numbers = [3, 41, 12, 9, 74, 15]
max_val = numbers[0]
min_val = numbers[0]
total = 0

for num in numbers:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num
    total += num

average = total / len(numbers)

print("Максимум:", max_val)
print("Минимум:", min_val)
print("Среднее:", round(average, 2))
