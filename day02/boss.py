# day02/boss.py
# Дима Еженк — День 2, Босс: Секундомер тренировок
# Дата: 22.07.2026



print("=== Секундомер тренировок ===")
print("Вводи количество минут после каждой тренировки.")
print("Напиши 'стоп', когда закончишь.\n")




sessions = []  # список продолжительности тренировок

while True:
    user_input = input("Сколько минут ты занимался? (или 'стоп'): ").strip().lower()
    
    if user_input == "стоп":
        break
    
    try:
        minutes = float(user_input)
        if minutes <= 0:
            print("Пожалуйста, введите положительное число.")
            continue
        sessions.append(minutes)
        print(f"✅ Записано: {minutes} мин\n")
    except ValueError:
        print("❌ Ошибка: введите число или 'стоп'\n")





# === Отчёт ===
if not sessions:
    print("Вы не записали ни одной тренировки.")
else:
    total_minutes = sum(sessions)
    hours = int(total_minutes // 60)
    minutes_left = int(total_minutes % 60)
    
    max_session = max(sessions)
    avg_session = total_minutes / len(sessions)
    
    print("\n" + "="*40)
    print("📊 ОТЧЁТ О ТРЕНИРОВКАХ")
    print("="*40)
    print(f"Всего тренировок: {len(sessions)}")
    print(f"Общее время: {hours} ч {minutes_left} мин")
    print(f"Самая длинная тренировка: {max_session} мин")
    print(f"Среднее время: {avg_session:.1f} мин")
    print("="*40)
