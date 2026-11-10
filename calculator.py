print("Simple Calculator")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("1. Addition")
    print("2. Subtraction")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Addition Result: ", num1 + num2)
    if choice == 2:
        print("Subtraction Result: ", num1 - num2)
    else:
        print("Invalid Choice")

except ValueError:
    print("Please enter valid numbers for calculation")
