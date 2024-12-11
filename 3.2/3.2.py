from MyMath import fake_math
from MyMath import true_math

first_number = int(input())
second_number = int(input())

# Обычное деленение на ноль
print(true_math.divide(first_number, second_number))

# Необычное деление на ноль
print(fake_math.divide(first_number, second_number))

result1 = fake_math.divide(69, 3)
result2 = fake_math.divide(3, 0)
result3 = true_math.divide(49, 7)
result4 = true_math.divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)