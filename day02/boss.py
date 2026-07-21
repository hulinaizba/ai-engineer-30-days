# -----------------------------
# 1. Функция приветствия
# -----------------------------
def greet(name):
	return f"Привет, {name}! Добро пожаловать в программу."


# -----------------------------
# 2. FizzBuzz
# -----------------------------
def fizzbuzz(n):
	for i in range(1, n + 1):
		if i % 15 == 0:
			print("FizzBuzz")
		elif i % 3 == 0:
			print("Fizz")
		elif i % 5 == 0:
			print("Buzz")
		else:
			print(i)


# -----------------------------
# 3. Таблица умножения
# -----------------------------
def multiplication_table(n):
	for i in range(1, 11):
		print(f"{n} × {i} = {n * i}")


# -----------------------------
# 4. Проверка простого числа
# -----------------------------
def is_prime(n):
	if n < 2:
		return False
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
	return True


# -----------------------------
# 5. Конвертер температур
# -----------------------------
def c_to_f(c):
	return c * 9/5 + 32

def f_to_c(f):
	return (f - 32) * 5/9


# -----------------------------
# 6. Оценка сложности пароля
# -----------------------------
def password_strength(pwd):
	score = 0

	if len(pwd) >= 8:
		score += 1
	if any(c.isdigit() for c in pwd):
		score += 1
	if any(c.isupper() for c in pwd):
		score += 1
	if any(c.islower() for c in pwd):
		score += 1
	if any(c in "!@#$%^&*()-_=+[]{}" for c in pwd):
		score += 1

	if score <= 2:
		return "Слабый"
	elif score == 3:
		return "Средний"
	else:
		return "Сильный"


# -----------------------------
# 7. Главное меню
# -----------------------------
def show_menu():
	print("\nВыберите действие:")
	print("1 — FizzBuzz")
	print("2 — Таблица умножения")
	print("3 — Проверка числа на простоту")
	print("4 — Конвертер температур")
	print("5 — Оценка сложности пароля")
	print("0 — Выход")


# -----------------------------
# 8. Основной цикл программы
# -----------------------------
def main():
	name = input("Введите ваше имя: ")
	print(greet(name))

	while True:
		show_menu()
		choice = input("Ваш выбор: ")

		if choice == "1":
			n = int(input("Введите число N: "))
			fizzbuzz(n)

		elif choice == "2":
			n = int(input("Введите число: "))
			multiplication_table(n)

		elif choice == "3":
			n = int(input("Введите число: "))
			print("Простое" if is_prime(n) else "Не простое")

		elif choice == "4":
			print("1 — C → F")
			print("2 — F → C")
			sub = input("Выбор: ")
			if sub == "1":
				c = float(input("Введите °C: "))
				print("°F:", c_to_f(c))
			elif sub == "2":
				f = float(input("Введите °F: "))
				print("°C:", f_to_c(f))

		elif choice == "5":
			pwd = input("Введите пароль: ")
			print("Сложность:", password_strength(pwd))

		elif choice == "0":
			print("Выход из программы...")
			break

		else:
			print("Неверный выбор. Попробуйте снова.")


# Запуск программы
# main()

