# day09/boss.py
# Дима Еженков — День 9, Босс: Визуализация дерева решений
# Дата: 02.08.2026

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

# === Подготовка данных Титаника ===
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

features = ["Pclass", "Sex", "Age", "Fare", "SibSp", "Parch"]
data = df[features + ["Survived"]].copy()

data["Sex"] = data["Sex"].map({"male": 0, "female": 1})
data["Age"] = data["Age"].fillna(data["Age"].mean())

X = data[features]
y = data["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# === 1. Обучаем дерево глубиной 3 (читаемое) ===
model_shallow = DecisionTreeClassifier(max_depth=3, random_state=42)
model_shallow.fit(X_train, y_train)

# === 2. Рисуем дерево ===
plt.figure(figsize=(20, 10))
plot_tree(
    model_shallow,
    feature_names=features,
    class_names=["Погиб", "Выжил"],
    filled=True,
    rounded=True,
    fontsize=10
)
plt.savefig("day09/tree.png", dpi=150, bbox_inches="tight")
print("Дерево сохранено в day09/tree.png")

# === 3. Важность признаков ===
print("\n=== Важность признаков (feature_importances_) ===")
for name, importance in zip(features, model_shallow.feature_importances_):
    print(f"{name:10}: {importance:.3f}")

# === 4. Сравнение глубин (переобучение) ===
model_deep = DecisionTreeClassifier(max_depth=10, random_state=42)
model_deep.fit(X_train, y_train)

acc_shallow_train = accuracy_score(y_train, model_shallow.predict(X_train))
acc_shallow_test = accuracy_score(y_test, model_shallow.predict(X_test))

acc_deep_train = accuracy_score(y_train, model_deep.predict(X_train))
acc_deep_test = accuracy_score(y_test, model_deep.predict(X_test))

print("\n=== Сравнение глубины деревьев ===")
print(f"max_depth=3  | Train: {acc_shallow_train:.3f} | Test: {acc_shallow_test:.3f}")
print(f"max_depth=10 | Train: {acc_deep_train:.3f} | Test: {acc_deep_test:.3f}")
print("\nЕсли Train сильно выше Test — это переобучение.")
