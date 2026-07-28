# day04/block2.py
# Дима Еженков — День 4, Блок 2: Наследование
# Дата: 28.07.2026


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Cat(Animal):
    def speak(self):
        return "Мяу"


class Cow(Animal):
    def speak(self):
        return "Му"


# Создаём список разных животных
animals = [
    Cat("Мурка"),
    Cow("Зорька"),
    Cat("Барсик"),
    Animal("Неизвестно")
]

print("=== Полиморфизм ===")
for animal in animals:
    print(f"{animal.name} говорит: {animal.speak()}")




# === Задача 5 ===
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)  # вызываем конструктор родителя
        self.bonus = bonus

    def annual_salary(self):
        return super().annual_salary() + self.bonus


# Проверка
emp = Employee("Аня", 50000)
mgr = Manager("Дима", 80000, 100000)

print("\n=== Зарплаты ===")
print(f"{emp.name}: {emp.annual_salary()} руб/год")
print(f"{mgr.name}: {mgr.annual_salary()} руб/год")



