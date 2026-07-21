
# day02/block2.py
# Дима Еженков — День 2, Блок 2: Условия (if-elif-else)
# Дата: 22.07.2026




# 5. Возрастные категории
age = int(input("Сколько тебе лет? "))

if age < 14:
	print("школьник")
elif 14 <= age <= 17:
	print("подросток")
elif 18 <= age <= 65:
	print("взрослый")
else:
	print("на пенсии")
	




# 6. Чётное/нечётное + знак
num = int(input("Введите число: "))
parity = "чётное" if num % 2 == 0 else "нечётное"

if num > 0:
	sign = "положительное"
elif num < 0:
	sign = "отрицательное"
else:
	sign = "ноль"

print(f"{num} — {parity} {sign}")




# 7. Високосный год
year = int(input("Введите год: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
	print(f"{year} — високосный год")
else:
	print(f"{year} — не високосный год")
	

    

# 8. Калькулятор
print("\n=== Простой калькулятор ===")
a = float(input("Первое число: "))
op = input("Операция (+ - * /): ").strip()
b = float(input("Второе число: "))

if op == "+":
	result = a + b
elif op == "-":
	result = a - b
elif op == "*":
	result = a * b
elif op == "/":
	if b == 0:
		print("Ошибка: деление на ноль!")
		result = None
	else:
		result = a / b
else:
	print("Неизвестная операция!")
	result = None

if result is not None:
	print(f"Результат: {result:.2f}")
