# Terminal Python Calculator
# Author: Austin Spraggins
# Date: 11/09/2023
# Version: 1.0
# Purpose: To create a calculator that can add, subtract, multiply, and divide two numbers

# Step 1 - Create the functions for each arithmatic operation

# I will create 'Add', 'Subtract', 'Multiply', and 'Divide' functions
# Each function will take two parameters, 'x' and 'y'and return the result of the operation


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    # We need to check if y is not 0 to avoid division by zero error.
    if y == 0:
        return "Error: Cannot divide by zero"

    else:
        return x / y

    # Step 2 - Write a function to take user input and validate it

    # Now we will write a function that asks user for input, makes sure it is a valid number, and then returns that number.
    # If the user enters something that is not a number, the function will keep asking until a valid number is entered.


def get_number(input_prompt):
    while True:
        try:
            user_input = float(input(input_prompt))
            return user_input
        except ValueError:
            print("That is not a number. Please enter a valid number and try again.")


# Step 4 - Write a main loop that lets the user perform calculations repeatedly

# Now we will create a loop that continues to ask the user what operation they want to perform and then calls the corresponding function based on the user's choice.
# After performing the calculation, it will display the result and then ask the user if they want to perform another calculation.

# Main Caluclation


def main():
    while True:
        # Display the options to the user
        print("\nOptions:")
        print("Enter 'add' to add two numbers.")
        print("Enter 'subtract' to subtract two numbers.")
        print("Enter 'multiply' to multiply two numbers.")
        print("Enter 'divide' to divide two numbers.")
        print("Enter 'quit' to end the program.")
        user_input = input(": ")

        if user_input == "quit":
            print("Thank you for using the calculator. Goodbye!")
            break  # This will exit the while loop and end the program
        elif user_input in ("add", "subtract", "multiply", "divide"):
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            if user_input == "add":
                print(f"The result is {add(num1, num2)}\n")
            elif user_input == "subtract":
                print(f"The result is {subtract(num1, num2)}\n")
            elif user_input == "multiply":
                print(f"The result is {multiply(num1, num2)}\n")
            elif user_input == "divide":
                result = divide(num1, num2)
                print(f"The result is {result}\n")
        else:
            print("Unknown input. Please enter one of the options provided.\n")


# Make sure the main function is called when the script is executed
if __name__ == "__main__":
    main()
