# 1 Возраст > школьник / подросток / взрослый / на пенсии
age = int(input("Введите ваш возраст: "))
if age < 14:
    print("школьник")
elif 14 <= age <= 17:
    print("подросток")
elif 18 <= age <= 65:
    print("взрослый")
else:
    print("на пенсии")

# 2 Число > четкое/нечеткое + знак
num = int(input("Введите число: "))
if num == 0:
    print("0 - это ноль")
else:
    parity = "четное" if num % 2 == 0 else "нечетное"
    sign = "положительное" if num > 0 else "отрицательное"
    print(f"{num} - {parity} {sign}")

# 3 Vysokosnyy god
year = int(input("Введите год: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("високосный")
else:
    print("не високосный")

# 4 Калькулятор (+ - * /)
try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    op = input("Введите операцию (+, -, *, /): ")

    if op == "+":
        print("Результат:", a + b)
    elif op == "-":
        print("Результат:", a - b)
    elif op == "*":
        print("Результат:", a * b)
    elif op == "/":
        if b == 0:
            print("Ошибка: деление на ноль невозможно")
        else:
            print("Результат:", a / b)
    else:
        print("Неизвестная операция.")
except ValueError:
    print("Ошибка: нужно вводить числа.")
