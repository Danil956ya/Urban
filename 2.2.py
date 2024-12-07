def main_program(first, second, third):
    value = 0
    if first == second and second == third:
        print(3)
    elif first == second or second == third or first == third:
        print(2)
    else:
        print(0)

main_program(int(input()), int(input()), int(input()))
