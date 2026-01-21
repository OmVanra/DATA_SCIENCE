def greet(name):
    print(f'hello {name}')
    
greet('om')

def add_numbers(a, b):
    return a + b
result = add_numbers(5,10)
print('sum:', result)

def calculate_salary(base, bonus=5000, tax_rate=0.12):
    gross = base + bonus
    tax = gross * tax_rate
    net = gross - tax
    return gross, net, tax

# Different ways to call
print(calculate_salary(50000))                    # using default bonus & tax
print(calculate_salary(60000, bonus=10000))       # keyword arg
gross, net, tax = calculate_salary(45000, 8000, 0.15)
print(f"Gross: ₹{gross}, Net: ₹{net}, Tax: ₹{tax}")

# *args example - it accepts variable number of positional arguments and returns their sum and tuple of numbers
def add_all(*numbers):
    return sum(numbers)
result1 = add_all(1,2,3,4)
print('Sum of all numbers:', result1)    

# **kwargs example - it accepts variable number of keyword arguments and prints them and dictionary of arguments
def print_info(**info):
    for key, value in info.items():
        print(f'{key}: {value}')
        
print_info(name='om', age=19 , city= 'ahmedabad')       