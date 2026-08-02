import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# === Подготовка данных (как в дне 8) ===
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

print("Данные готовы. Размер X:", X.shape)

# === Обучаем три классификатора ===
models = {
    "LogisticRegression": LogisticRegression(max_iter=1000),
    "KNeighbors": KNeighborsClassifier(n_neighbors=5),
    "DecisionTree": DecisionTreeClassifier(max_depth=4, random_state=42)
}

results = []

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    
    results.append({
        "Модель": name,
        "Accuracy": round(acc, 3)
    })
    print(f"{name}: Accuracy = {acc:.3f}")

# Таблица сравнения
df_results = pd.DataFrame(results)
print("\n=== Таблица сравнения ===")
print(df_results)

# Находим лучшую модель
best_name = df_results.loc[df_results["Accuracy"].idxmax(), "Модель"]
print(f"\nЛучшая модель по Accuracy: {best_name}")

# === Кросс-валидация для лучшей модели ===
best_model = models[best_name]
cv_scores = cross_val_score(best_model, X, y, cv=5)

print("\n=== Кросс-валидация (5 фолдов) ===")
print("Оценки по фолдам:", [round(s, 3) for s in cv_scores])
print(f"Среднее: {cv_scores.mean():.3f}")
print(f"Разброс (std): {cv_scores.std():.3f}")