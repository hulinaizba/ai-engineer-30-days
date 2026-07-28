# day04/block1.py
# Дима Еженков — День 4, Блок 1: Первые классы
# Дата: 28.07.2026

class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return f"{self.name} говорит: Гав!"

    def info(self):
        return f"Имя: {self.name}, Порода: {self.breed}, Возраст: {self.age}"


# Создаём двух собак
dog1 = Dog("Бобик", "Лабрадор", 3)
dog2 = Dog("Рекс", "Овчарка", 5)

print(dog1.bark())
print(dog1.info())
print(dog2.bark())
print(dog2.info())



# === Задача 2 ===
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Внесено {amount}. Новый баланс: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств!")
            return
        self.balance -= amount
        print(f"Снято {amount}. Новый баланс: {self.balance}")

    def __str__(self):
        return f"Счёт {self.owner}: {self.balance} руб"


# Проверка
account = BankAccount("Дима")
account.deposit(1000)
account.withdraw(300)
account.withdraw(5000)   # должно выдать предупреждение
print(account)



# === Задача 3 ===
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height


# Проверка
rect1 = Rectangle(5, 10)
rect2 = Rectangle(7, 7)

print("\nПрямоугольник 5x10:")
print("Площадь:", rect1.area())
print("Периметр:", rect1.perimeter())
print("Квадрат?", rect1.is_square())

print("\nКвадрат 7x7:")
print("Площадь:", rect2.area())
print("Периметр:", rect2.perimeter())
print("Квадрат?", rect2.is_square())





