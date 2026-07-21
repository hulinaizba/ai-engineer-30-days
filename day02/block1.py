# day02/block1.py
# Дима Еженк — День 2, Блок 1: Типы и строки
# Дата: 22.07.2026


# 1. Базовые типы
# Создай переменные и выведи их + type()

int_var = 42
float_var = 3.14
str_var = "Hello, Python!"
bool_var = True
list_var = [1, 2, 3, "four"]
dict_var = {"name": "Дима", "age": 30, "city": "Tel Aviv"}

print("int:", int_var, type(int_var))
print("float:", float_var, type(float_var))
print("str:", str_var, type(str_var))
print("bool:", bool_var, type(bool_var))
print("list:", list_var, type(list_var))
print("dict:", dict_var, type(dict_var))


# 2. Работа со строками
s = "Machine Learning Engineer"

print(len(s))                    # длина
print(s.upper())                 # верхний регистр
print(s[:7])                     # первые 7 символов
print(s[-8:])                    # последние 8
print(s.split()[::-1])           # слова в обратном порядке


# 3. Арифметические операции с вводом
a = float(input("Первое число: "))
b = float(input("Второе число: "))

print("Сумма:", a + b)
print("Разность:", a - b)
print("Произведение:", a * b)
print(f"Деление: {a / b:.2f}")   # важно: 2 знака после запятой


# 4. Преобразование типов
s = "42"
num = 7

print(int(s) + num)        # как числа → 49
print(s + str(num))        # как строки → "427"
