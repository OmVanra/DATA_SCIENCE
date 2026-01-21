# Basic if - only executes when condition is true
a = 10
if a > 5:
    print(f'{a} is greater than 5')
    
    
# Basic if - else - executes one block if condition is true, another if false
age = 19
if age >= 18:
    print('You are eligible to vote')
else:
    print('You are not eligible to vote')
    
# if-elif-else - multiple conditions
marks = 75
if marks >= 90:
    print('Grade: A++')
elif marks >= 80:
    print('Grade: A+')
elif marks >= 70:
    print('Grade: B')
else:
    print('Grade: C or below')                
    
    
# Nested if
city = 'Ahmedabad'
is_working = True

if city == 'Ahmedabad' or city == 'Surat':
    if is_working:
        print('You are working in Gujrat')
    else:
        print('You are not working in Gujrat')        
else:
    print('You are not in Gujrat')
    
                
    
    