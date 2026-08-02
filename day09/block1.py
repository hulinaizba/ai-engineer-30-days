# day09/block1.py
# Дима Еженков — День 9, Блок 1: Сравнение регрессоров
# Дата: 02.08.2026

import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Загружаем реальные данные о жилье в Калифорнии
data = fetch_california_housing()
X, y = data.data, data.target   # y — медианная цена дома (в $100k)

print("Признаки:", data.feature_names)
print("Размер X:", X.shape)
print("Размер y:", y.shape)

# Делим на train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# === Обучаем три модели ===
models = {
    "LinearRegression": LinearRegression(),
    "Ridge": Ridge(alpha=1.0),
    "DecisionTree": DecisionTreeRegressor(max_depth=5, random_state=42)
}

results = []

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    results.append({
        "Модель": name,
        "MAE": round(mae, 3),
        "R2": round(r2, 3)
    })
    
    print(f"{name}: MAE={mae:.3f}, R²={r2:.3f}")

# Таблица сравнения
df_results = pd.DataFrame(results)
print("\n=== Таблица сравнения ===")
print(df_results)

# Выводы
print("\n=== Выводы ===")
best = df_results.loc[df_results["R2"].idxmax()]
print(f"Победитель по R²: {best['Модель']} (R² = {best['R2']})")
print("Дерево решений ловит нелинейные зависимости,")
print("а линейные модели ищут прямую линию. Поэтому результаты часто отличаются.")

