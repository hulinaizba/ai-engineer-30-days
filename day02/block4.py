# 1 функция приветствия

def green(name):
    return f"Привет, {name}!"

print(green("Дима"))


# 2 проверка числа на простоту
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))      # True
print(is_prime(12))     # False


# 3 подсчёт гласных в строке
def count_vowels(text):
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Machine Learning Engineer"))


# 4 конвертер температур
def c_to_f(c):
    return c * 9/5 + 32

def f_to_c(f):
    return (f - 32) * 5/9

print(c_to_f(0))     # 32
print(f_to_c(32))    # 0


# 5 оценка сложности пароля
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

print(password_strength("Qwerty123!"))
