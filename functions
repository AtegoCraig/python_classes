def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a / b

print("This module provides basic arithmetic functions.")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Choose an operation: add, subtract, multiply, divide")
if __name__ == "__main__":
    operation = input("Enter operation: +, -, *, /: ").strip().lower()
    if operation == "+":
        print(f"Result: {add(num1, num2)}")
    elif operation == "-":
        print(f"Result: {subtract(num1, num2)}")
    elif operation == "*":
        print(f"Result: {multiply(num1, num2)}")
    elif operation == "/":
        result = divide(num1, num2)
        if result is not None:
            print(f"Result: {result}")
    else:
        print("Invalid operation selected.")