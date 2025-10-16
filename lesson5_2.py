answer = True
while answer == True:
    user_input1 = input("Введите первое число:")
    digital1 = int(user_input1)
    operation = input ("Введите операцию:")
    user_input2 = input("Введите второе число:")
    digital2 = int(user_input2)
    if operation == "+":
        result = digital1 + digital2
        print("результат:", result)
        answer = input("Хотите продолжить вычисления?")
    elif operation == "-":
        result = digital1 - digital2
        print("результат:", result)
        answer = input("Хотите продолжить вычисления?")
    elif operation == "*":
        result = digital1 * digital2
        print("результат:", result)
        answer = input("Хотите продолжить вычисления?")
    elif operation == "/":
        if digital2 != 0:
            result = digital1 / digital2
            print("результат:", result)
            answer = input("Хотите продолжить вычисления?")
        else:
            print("ошибка деления на ноль!")
            answer = input("Хотите продолжить вычисления?")
    else:
        print("неизвестный знак!")
        answer = input("Хотите продолжить вычисления?")
    if answer == "y" or answer == "yes" or answer == "YES" or answer == "Y" or answer == "Yes":
        answer = True
    else:
        answer = False