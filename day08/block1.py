# day08/block1.py
# Дима Еженков — День 8, Блок 1: Регрессия
# Дата: 30.07.2026

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Создаём синтетические данные
np.random.seed(42)
area = np.random.uniform(20, 150, 100)  # площадь в м²
price = area * 1000 + np.random.normal(0, 5000, 100) + 50000  # цена с шумом

# Превращаем в 2D-массив (sklearn требует таблицу признаков)
X = area.reshape(-1, 1)
y = price

# Разделяем на train и test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === 3. Обучаем модель ===
model = LinearRegression()
model.fit(X_train, y_train)

# Что происходит:
# Модель ищет лучшую прямую линию вида: цена = a * площадь + b
# .fit() подбирает коэффициенты a и b на обучающих данных


# === 4. Предсказываем на тесте и считаем метрики ===
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("=== Метрики на тесте ===")
print(f"MAE  (средняя абсолютная ошибка): {mae:.0f} руб")
print(f"MSE  (средняя квадратичная ошибка): {mse:.0f}")
print(f"R²   (коэффициент детерминации): {r2:.3f}")

# Что означают метрики:
# MAE  — в среднем модель ошибается на столько-то рублей
# R²   — насколько хорошо модель объясняет данные (1.0 = идеально, 0 = как среднее)


# === 5. Предсказываем цену новой квартиры ===
new_area = np.array([[75]])  # 75 м² (обязательно 2D!)
predicted_price = model.predict(new_area)[0]

print(f"\nПредсказанная цена квартиры 75 м²: {predicted_price:.0f} руб")

# Комментарий: зачем нужен test-сет?
# Мы обучаем модель на train, а проверяем на test (невидимых данных),
# чтобы понять, насколько хорошо она обобщает, а не просто запоминает.