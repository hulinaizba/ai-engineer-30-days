# 1️⃣ FizzBuzz от 1 до 100
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 2️⃣ Сумма всех чётных чисел от 1 до 1000
even_sum = 0
for i in range(2, 1001, 2):  # шаг 2 — сразу только чётные
    even_sum += i
print("Сумма чётных чисел:", even_sum)

# 3️⃣ Таблица умножения на N
n = int(input("Введите число N: "))
for i in range(1, 11):
    print(f"{n} × {i} = {n * i}")

# 4️⃣ Игра «Угадай число»
import random
secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Ваш вариант: "))
    attempts += 1

    if guess < secret:
        print("Больше")
    elif guess > secret:
        print("Меньше")
    else:
        print(f"Угадал! Число попыток: {attempts}")
        break

# 5️⃣ Максимум, минимум и среднее без max(), min(), sum()
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
print("Среднее:", average)
