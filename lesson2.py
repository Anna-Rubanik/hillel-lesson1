print("Завдання 1")
user_input = input("input a four-digital number:")
number = int (user_input)
digital1 = number // 1000
digital2 = (number // 100) % 10
digital3 = (number // 10) % 10
digital4 = number % 10
print (digital1)
print(digital2)
print(digital3)
print(digital4)
print("Завдання 2")

user_input2 = input("input a 5-digital number:")
number2 = int(user_input2)
digital1 = number2 % 10
digital2 = (number2 % 100) // 10
digital3 = (number2 % 1000) // 100
digital4 = (number2 % 10000) // 1000
digital5 = number2 // 10000
print(digital1, digital2, digital3, digital4, digital5)