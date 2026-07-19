import datetime

name = input("Какое твое имя? ")

while True:

    age_input = input("Сколько тебе лет? ")
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Пожалуйста, введите число.")

year_now = datetime.date.today().year
age_in_2030 = age + (2030 - year_now)

today = datetime.date.today()
end_date = today + datetime.date(2026, 8, 17)
days_left = (end_date - today).days

print("_" * 40)
print(f"Привет, {name}!")
print(f"В 2030 году тебе будет {age_in_2030} лет.")
print(f"До конца курса осталось {days_left} дней.") 
print("_" * 40)