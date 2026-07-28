
# day03/block3.py
# Дима Еженков — День 3, Блок 3: Исключения
# Дата: 24.07.2026



# === Задача 10 ===
def safe_divide(a, b):
	try:
		result = a / b
		return result
	except ZeroDivisionError:
		print("Предупреждение: деление на ноль!")
		return None

if __name__ == "__main__":
	print("10 / 2 =", safe_divide(10, 2))
	print("10 / 0 =", safe_divide(10, 0))



# === Задача 11 ===
print("\n=== Чтение файла ===")
filename = input("Введите имя файла: ")

try:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print("Содержимое файла:")
        print(content)
except FileNotFoundError:
    print(f"Файл '{filename}' не найден. Проверьте имя и попробуйте снова.")



 # === Задача 12 ===
def ask_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ошибка: нужно ввести целое число. Попробуйте ещё раз.")

# Проверка работы функции
print("\n=== Проверка ask_int ===")
number = ask_int("Введите целое число: ")
print("Вы ввели:", number)



# === Задача 13 ===
print("\n=== Пример try / except / else / finally ===")

try:
    num = int(input("Введите число для деления 100: "))
    result = 100 / num
except ValueError:
    print("Это не число!")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
else:
    # else выполняется ТОЛЬКО если ошибки не было
    print("Всё прошло успешно. Результат:", result)
finally:
    # finally выполняется ВСЕГДА — и при ошибке, и без ошибки
    print("Этот блок finally выполнился в любом случае.")





    



