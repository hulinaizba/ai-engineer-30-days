# day05/boss.py
# Дима Еженков — День 5, Босс: Первый разговор с Claude
# Дата: 29.07.2026

import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

print("=== Мини-чат с Claude ===")
print("Напиши вопрос. Для выхода введи: выход\n")

while True:
    user_question = input("Ты: ").strip()
    
    if user_question.lower() in ["выход", "exit", "quit"]:
        print("Чат завершён.")
        break
    
    if not user_question:
        continue
    
    try:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=400,
            messages=[
                {"role": "user", "content": user_question}
            ]
        )
        
        answer = response.content[0].text
        print("\nClaude:", answer)
        print("-" * 50)
        
    except Exception as e:
        print(f"\nОшибка: {e}")
        print("-" * 50)