# day04/boss.py
# Дима Еженков — День 4, Босс: Менеджер задач
# Дата: 28.07.2026

class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def complete(self):
        self.done = True


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, title):
        self.tasks.append(Task(title))

    def complete(self, index):
        try:
            self.tasks[index].complete()
        except IndexError:
            print(f"Ошибка: задачи с номером {index} не существует")

    def show(self):
        if not self.tasks:
            print("Список задач пуст")
            return
        for i, task in enumerate(self.tasks):
            status = "[x]" if task.done else "[ ]"
            print(f"{i}. {status} {task.title}")

    def stats(self):
        total = len(self.tasks)
        done = sum(1 for task in self.tasks if task.done)
        percent = (done / total * 100) if total > 0 else 0
        print(f"Всего задач: {total}")
        print(f"Выполнено: {done}")
        print(f"Процент: {percent:.0f}%")


# === Рабочий сценарий ===
manager = TaskManager()

manager.add("Изучить ООП")
manager.add("Сделать блок 3")
manager.add("Написать босса")
manager.add("Отправить отчёт")

manager.complete(0)
manager.complete(2)
manager.complete(99)

print("\n=== Список задач ===")
manager.show()

print("\n=== Статистика ===")
manager.stats()
