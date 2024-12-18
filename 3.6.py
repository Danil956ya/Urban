a = int(input("Первое число? :\n"))
char = str(input("Ваш оператор? :\n"))
b = int(input("Второе число? :\n"))

def calculate(a, char, b):
    result = None
    if char == "+":
        result = a + b
    elif char == "-":
        result =  a-b
    elif char == "/":
            try:
                a / b
            except ZeroDivisionError:
                print("Не делим на ноль.")
    elif char == "*":
        result = a*b
    else:
        print("Попробуйте ещё раз.")

    if result != None:
        print(f"Ваш результат: {result}")

calculate(a, char, b)