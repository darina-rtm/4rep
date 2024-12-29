numbers = []
for i in range(4):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Сложить первые два и отдельно вторые два числа
sum1 = numbers[0] + numbers[1]
sum2 = numbers[2] + numbers[3]

# Вывод с двумя знаками после запятой
print(f"First sum: {sum1:.2f}")
print(f"Second sum: {sum2:.2f}")
