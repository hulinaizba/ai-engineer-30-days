# day02/block4.py
# Дима Еженк — День 2, Блок 4: Функции
# Дата: 22.07.2026





def greet(name):
    """Возвращает приветствие"""
    return f"Привет, {name}!"





def is_prime(n):
    """Проверяет, является ли число простым"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True





def count_vowels(text):
    """Подсчитывает гласные буквы (рус + англ)"""
    vowels = "aeiouаеёиоуыэюяAEIOUАЕЁИОУЫЭЮЯ"
    return sum(1 for char in text if char in vowels)




def fahrenheit(celsius):
    """Переводит °C в °F"""
    return celsius * 9/5 + 32

def celsius(fahrenheit_temp):
    """Переводит °F в °C"""
    return (fahrenheit_temp - 32) * 5/9





def password_strength(pwd):
    """Оценивает силу пароля"""
    if len(pwd) < 8:
        return "слабый"
    
    has_letter = any(c.isalpha() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    
    if has_letter and has_digit:
        return "сильный"
    return "средний"





# === Тесты ===
if __name__ == "__main__":
    print(greet("Дима"))
    print("is_prime(17):", is_prime(17))
    print("is_prime(100):", is_prime(100))
    print("is_prime(97):", is_prime(97))
    print("Гласных в 'Привет, world!':", count_vowels("Привет, world!"))
    print("25°C в °F:", fahrenheit(25))
    print("Обратно:", celsius(fahrenheit(25)))
    print("Сила пароля 'hello':", password_strength("hello"))
    print("Сила пароля 'hello123':", password_strength("hello123"))
