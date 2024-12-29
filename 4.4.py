# Ввод возраста Тани и Мити
tanya_age = float(input("Введите возраст Тани (в годах): "))
mitya_age = float(input("Введите возраст Мити (в годах): "))

# Вычисление среднего возраста
average_age = (tanya_age + mitya_age) / 2

# Разница между возрастами детей и средним возрастом
tanya_difference = abs(tanya_age - average_age)
mitya_difference = abs(mitya_age - average_age)

# Вывод результатов
print("\nРезультаты:")
print(f"Средний возраст: {average_age:.2f} лет")
print(f"Разница между возрастом Тани и средним возрастом: {tanya_difference:.2f} лет")
print(f"Разница между возрастом Мити и средним возрастом: {mitya_difference:.2f} лет")
