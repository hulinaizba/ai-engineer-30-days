
# day05/block1.py
# Дима Еженков — День 5, Блок 1: requests и JSON
# Дата: 29.07.2026

import requests


# === Задача 1: Случайная шутка ===
print("=== Случайная шутка ===")

try:
	response = requests.get("https://official-joke-api.appspot.com/random_joke")
    
	if response.status_code == 200:
		joke = response.json()
		print("Setup:", joke["setup"])
		print("Punchline:", joke["punchline"])
	else:
		print("Ошибка: API вернул код", response.status_code)
except Exception as e:
	print("Не удалось получить шутку:", e)




# === Задача 2: Погода в Москве ===
print("\n=== Погода в Москве ===")

try:
    url = "https://api.open-meteo.com/v1/forecast?latitude=55.75&longitude=37.62&current=temperature_2m"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temperature = data["current"]["temperature_2m"]
        print(f"Сейчас в Москве: {temperature}°C")
    else:
        print("Ошибка: API вернул код", response.status_code)
except Exception as e:
    print("Не удалось получить погоду:", e)



    # === Задача 4: Курс валют ===
print("\n=== Курс валют ===")

try:
    url = "https://api.frankfurter.app/latest?from=USD&to=RUB,EUR"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        rates = data["rates"]
        print(f"1 USD = {rates['RUB']} RUB")
        print(f"1 USD = {rates['EUR']} EUR")
    else:
        print("Ошибка: API вернул код", response.status_code)
except Exception as e:
    print("Не удалось получить курс валют:", e)