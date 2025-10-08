user_input1 = input("Введите первое число:")
digital1 = int(user_input1)
operation = input ("Введите операцию:")
user_input2 = input("Введите второе число:")
digital2 = int(user_input2)
if operation == "+":
    result = digital1 + digital2
    print("результат:", result)
elif operation == "-":
    result = digital1 - digital2
    print("результат:", result)
elif operation == "*":
    result = digital1 * digital2
    print("результат:", result)
elif operation == "/":
    if digital2 != 0:
        result = digital1 / digital2
        print("результат:", result)
    else:
        print("ошибка деления на ноль!")
else:
    print("неизвестный знак!")






