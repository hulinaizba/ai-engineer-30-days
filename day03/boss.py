from datetime import datetime
import os


def ask_int(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == "стоп":
            return "стоп"
        try:
            value = int(user_input)
            if value <= 0:
                print("Введите положительное число.")
                continue
            return value
        except ValueError:
            print("Ошибка: нужно ввести целое число или 'стоп'.")


print("=== Секундомер тренировок 2.0 ===\n")

# Показываем прошлый отчёт, если он есть
if os.path.exists("report.txt"):
    print("Вот что было в прошлый раз:")
    print("-" * 40)
    with open("report.txt", "r", encoding="utf-8") as f:
        print(f.read())
    print("-" * 40)
    print()

sessions = []

while True:
    result = ask_int("Сколько минут ты занимался? (или 'стоп'): ")

    if result == "стоп":
        break

    sessions.append(result)
    print(f"✅ Записано: {result} мин\n")

if not sessions:
    print("Вы не записали ни одной тренировки.")
else:
    total_minutes = sum(sessions)
    hours = total_minutes // 60
    minutes_left = total_minutes % 60
    max_session = max(sessions)
    avg_session = total_minutes / len(sessions)

    report = []
    report.append(f"Дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"Всего тренировок: {len(sessions)}")
    report.append(f"Общее время: {hours} ч {minutes_left} мин")
    report.append(f"Самая длинная тренировка: {max_session} мин")
    report.append(f"Среднее время: {avg_session:.1f} мин")

    report_text = "\n".join(report)

    print("\n" + "=" * 40)
    print("📊 ОТЧЁТ О ТРЕНИРОВКАХ")
    print("=" * 40)
    print(report_text)
    print("=" * 40)

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(report_text)

    print("\nОтчёт сохранён в report.txt")
