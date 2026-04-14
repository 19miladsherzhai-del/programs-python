print("=== Simple Calculator ===")

while True:
    try:
        num1 = float(input("Enter first number: "))
    except:
        print("Please enter a valid number")
        continue

    operator = input("Enter operator (+, -, *, /): ")

    try:
        num2 = float(input("Enter second number: "))
    except:
        print("Please enter a valid number")
        continue

    if operator == "+":
        print("Result:", num1 + num2)
    elif operator == "-":
        print("Result:", num1 - num2)
    elif operator == "*":
        print("Result:", num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operator")

    again = input("Do you want to calculate again? (yes/no): ")
    if again.lower() != "yes":
        print("Goodbye!")
        break
