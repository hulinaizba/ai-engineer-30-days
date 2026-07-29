# day05/block2.py
# Дима Еженков — День 5, Блок 2: Вложенный JSON
# Дата: 29.07.2026

import requests



print("=== Пользователи ===\n")

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    
    if response.status_code == 200:
        users = response.json()   # это список словарей
        
        for user in users:
            name = user["name"]
            email = user["email"]
            city = user["address"]["city"]
            company = user["company"]["name"]
            
            print(f"Имя: {name}")
            print(f"Email: {email}")
            print(f"Город: {city}")
            print(f"Компания: {company}")
            print("-" * 40)
    else:
        print("Ошибка API:", response.status_code)
except Exception as e:
    print("Ошибка:", e)