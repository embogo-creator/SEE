def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Welcome to the Python Calculator!")
    print("-------------------------------")
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please select a valid option (1-5).")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")

# R
