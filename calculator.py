print("Simple Calculator - conflict-b change")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Addition Result: ", num1 + num2)
    elif choice == 2:
        print("Subtraction Result: ", num1 - num2)
    elif choice == 3:
        print("Multiplication Result: ", num1 * num2)
    else:
        print("Invalid Choice")

except ValueError:
    print("Please enter valid numbers for calculation")
