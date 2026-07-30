# day08/boss.py
# Дима Еженков — День 8, Босс: ML на Титанике
# Дата: 30.07.2026

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# === 1. Загружаем данные ===
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("Размер исходных данных:", df.shape)

# === 2. Подготовка данных ===
# Выбираем нужные признаки
features = ["Pclass", "Sex", "Age", "Fare", "SibSp", "Parch"]
data = df[features + ["Survived"]].copy()

# Sex: текст → числа
data["Sex"] = data["Sex"].map({"male": 0, "female": 1})

# Age: заполняем пропуски средним
data["Age"] = data["Age"].fillna(data["Age"].mean())

print("\nПропуски после обработки:")
print(data.isnull().sum())

# Отделяем признаки и целевую переменную
X = data[features]
y = data["Survived"]

print("\nПризнаки (X):", X.shape)
print("Целевая переменная (y):", y.shape)

# === 3. Делим на train/test ===
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# === 4. Обучаем LogisticRegression ===
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# === 5. Предсказываем и считаем метрики ===
y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print(f"\nAccuracy модели: {acc:.3f}")

print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred))

print("=== Confusion Matrix ===")
print(confusion_matrix(y_test, y_pred))

# === 6. Сравнение с наивной моделью (baseline) ===
# Если всегда предсказывать "не выжил" (0)
baseline_acc = (y_test == 0).mean()
print(f"\nAccuracy наивной модели (всегда 0): {baseline_acc:.3f}")
print(f"Наша модель лучше baseline на: {acc - baseline_acc:.3f}")

# === 7. Важность признаков ===
print("\n=== Важность признаков (коэффициенты) ===")
for name, coef in zip(features, model.coef_[0]):
    print(f"{name:10}: {coef:+.3f}")

# Какой признак влияет сильнее всего (по модулю)
most_important = features[abs(model.coef_[0]).argmax()]
print(f"\nСамый важный признак: {most_important}")