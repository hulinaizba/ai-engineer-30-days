# day08/block2.py
# Дима Еженков — День 8, Блок 2: Классификация
# Дата: 30.07.2026

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# === 6–7. Загружаем ирисы и делим на train/test ===
iris = load_iris()

X = iris.data          # признаки (длина/ширина чашелистиков и лепестков)
y = iris.target        # классы (0, 1, 2)
target_names = iris.target_names

print("Классы ирисов:", target_names)
print("Размер данных:", X.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

print(f"Train: {X_train.shape[0]} образцов")
print(f"Test:  {X_test.shape[0]} образцов")

# === 8–10. Обучаем KNN и оцениваем ===
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Accuracy — доля правильных ответов
acc = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {acc:.3f}")

# Подробный отчёт по каждому классу
print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred, target_names=target_names))

# Confusion Matrix — какие классы путает модель
print("=== Confusion Matrix ===")
print(confusion_matrix(y_test, y_pred))
