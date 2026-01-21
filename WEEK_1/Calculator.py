def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error : Division by zero"
    return x / y

def calculator():
    print("Welcome to the Calculator!")
    print('operators: (+, -, *, /)')
    while True:
       try:
    
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
    
            if operator == '+':
                print('result:', add(num1, num2))
            elif operator == '-':
                print('result:', subtract(num1, num2))
            elif operator == '*':
                print('result:', multiply(num1, num2))
            elif operator == '/':
                print('result:', divide(num1, num2))
            else:
                print("Invalid operator!")
            
            again = input("Do you want to exit? (y/n): ").lower()
            if again == 'y':
                print("Thank you for using the calculator. Goodbye!")
                break
       except ValueError:
            print("Invalid input! Please enter numeric values for numbers.")
calculator()                    
        
                        