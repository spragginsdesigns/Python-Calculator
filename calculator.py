# Terminal Python Calculator
# Author: Austin Spraggins
# Date: 11/09/2023
# Version: 1.1
# Purpose: To create a calculator that can add, subtract, multiply, and divide two numbers

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    else:
        return x / y

def get_number(input_prompt):
    while True:
        try:
            return float(input(input_prompt))
        except ValueError:
            print("That is not a number. Please enter a valid number.")

def main():
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    while True:
        print("\nOptions:")
        for op in operations:
            print(f"Enter '{op}' to {op} two numbers.")
        print("Enter 'quit' to end the program.")

        user_input = input(": ").lower()

        if user_input == "quit":
            print("Thank you for using the calculator. Goodbye!")
            break
        elif user_input in operations:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            result = operations[user_input](num1, num2)
            print(f"The result is {result}\n")
        else:
            print("Unknown input. Please enter one of the options provided.\n")

if __name__ == "__main__":
    main()
