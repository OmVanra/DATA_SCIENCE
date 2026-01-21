cities = ['Ahmedabad', 'Surat', 'Vadodara', 'Rajkot', 'Gandhinagar']

for city in cities:
    print(f'i want to work in {city}')
    
for i in range(5):
    print(f'Iteration number: {i}')
    
for i in range(1,11):
    print(f'Square of {i} is {i*i}')
    
for i in range(0,11,2):
    print(f'Even number: {i}')
                

# while loop

count = 1
while count <= 100:
    if count % 3 == 0 and count % 5 == 0:
        print('FizzBuzz')
    elif count % 3 == 0:
        print('Fizz')
    elif count % 5 == 0:
        print('Buzz')
    else:
        print(count)
    count += 1                                                
    
    
def add_all(*numbers):
    return sum(numbers)
add_all(1, 2, 3, 4)  # works with any number