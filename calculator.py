"""
Calculator CLI App
======================
A Simple Command Line Calculator supporting basic operations.
Author: Awais Syed
Email: awaissyed1212@gmail.com
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Error: Division by zero is not allowed!")
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def display_menu():
    print("\n" + "="*50)
    print("        COMMAND-LINE CALCULATOR")
    print("="*50)
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("-"*50)

def get_operation_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice in [1, 2, 3, 4, 5]:
                return choice
            else:
                print("Invalid choice! Please select from 1-5.")
        except ValueError:
            print("Invalid input! Please enter a number between 1-5.")

def perform_calculation(choice, num1, num2):
    operations = {
        1: (add, "+"),
        2: (subtract, "-"), 
        3: (multiply, "*"),
        4: (divide, "/")
    }
    
    func, symbol = operations[choice]
    
    try:
        result = func(num1, num2)
        print(f"\nResult: {num1} {symbol} {num2} = {result}")
        print("-"*50)
        return result
    except ValueError as e:
        print(f"\n{e}")
        print("-"*50)
        return None

def main():
    print("Welcome to the Command-Line Calculator!")
    
    while True:
        display_menu()
        choice = get_operation_choice()

        if choice == 5:
            print("\nThank you for using the calculator!")
            print("Goodbye! 👋")
            break
        
        print(f"\nYou selected: {['', 'Addition', 'Subtraction', 'Multiplication', 'Division'][choice]}")
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        
        perform_calculation(choice, num1, num2)
        
        while True:
            continue_calc = input("\nDo you want to perform another calculation? (y/n): ").lower().strip()
            if continue_calc in ['y', 'yes']:
                break
            elif continue_calc in ['n', 'no']:
                print("\nThank you for using the calculator!")
                return
            else:
                print("Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    main()