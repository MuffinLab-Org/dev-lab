num_1 = input("Enter the first number: ")
operation = input("Enter the operation (+, -, *, /): ")
num_2 = input("Enter the second number: ")

try:
    num_1 = float(num_1)
    num_2 = float(num_2)
    
    if operation == "+":
        result = num_1 + num_2
    elif operation == "-":
        result = num_1 - num_2
    elif operation == "*":
        result = num_1 * num_2
    elif operation == "/":
        if num_2 != 0:
            result = num_1 / num_2
        else:
            print("Error: Division by zero is not allowed.")
            exit()
    else:
        print("Invalid operation. Please enter +, -, *, or /.")
        exit()
    print(f"{num_1} {operation} {num_2} = {result}")
except ValueError:
    print("Please enter valid numbers.")