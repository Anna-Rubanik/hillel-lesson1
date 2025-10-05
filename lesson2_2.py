print("Завдання 2")
user_input2 = input("input a 5-digital number:")
number2 = int(user_input2)
digital1 = number2 % 10
digital2 = (number2 % 100) // 10
digital3 = (number2 % 1000) // 100
digital4 = (number2 % 10000) // 1000
digital5 = number2 // 10000
print(digital1, digital2, digital3, digital4, digital5)