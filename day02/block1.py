# 1. Базовые типы
int_var = 10
float_var = 3.14
complex_var = 2 + 5j
bool_var = True
str_var = "hello"
none_var = None

print(int_var, type(int_var))
print(float_var, type(float_var))
print(complex_var, type(complex_var))
print(bool_var, type(bool_var))
print(str_var, type(str_var))
print(none_var, type(none_var))

# 2. Работа со строкой "Machine Learning Engineer"
text = "Machine Learning Engineer"
print(len(text))
print(text.upper())
print(text[:7])
print(text[-8:])
print(" ".join(text.split()[::-1]))

# 3. Ввод двух чисел и арифметические операции
first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
print("Сумма:", first_number + second_number)
print("Разность:", first_number - second_number)
print("Произведение:", first_number * second_number)
print("Деление:", format(first_number / second_number, ".2f"))
print("Остаток:", first_number % second_number)

# 4. "42" и число 7 - сложение как числа и как строки
string_number = "42"
number = 7
print("Сложение как числа:", int(string_number) + number)
print("Сложение как строки:", string_number + str(number))
