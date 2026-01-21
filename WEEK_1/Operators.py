print("-----------------------WELCOME---------------------------")
name = input("enter your name :")
age = input("enter your age :")
print('Hello ',name,'next year you will be',(int(age)+1),'years old!')

num1 = input("enter num1:")
num2 = input("enter num2:")
sum = int(num1) + int(num2)
print("Sum:", sum)

price = int(input("enter price :"))
quantity = int(input("enter quantity:")) 
total = price * quantity
print("total is:", total)

total_marks = int(input("enter total marks:"))
subjects = int(input("enter total subjects:"))
Average = total_marks/ subjects
print("Average is ",Average)


#calculate simple interest rate
P = 300000
R = 4
T = 2
SI = (P*R*T)/100
print("simple interest:", SI)

#find square and qube of number
num = int(input("enter number to find square and qube:"))
print('square: ', num*num)
print('qube: ',num*num*num)

#find even and odd
number = int(input("enter number to find the number is even or odd"))
print('num is even',number%2==0)
print('num is odd',num%2!=0)

#find celcius and fehrenheit
print('welcome to Fehrenheit calculator')
Calcius = int(input("enter calcius to calculate F:"))
F = (Calcius*9/5)+ 32
print("Fehrenheit:",F)

print("welcome to Celcius calculator")
Fehrenheit = int(input('enter Fehrenheit to calculate C:'))
C = (Fehrenheit-32)*5/9
print("Celcius: ",C)
