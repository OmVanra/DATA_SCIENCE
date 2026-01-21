#create a tuple to store lag and long of ahmedabad
ahnedabad_cord = (23.0225, 72.5714)

# Try to change it it will give error (that's why we use tuple)
#ahnedabad_cord[0] = 24  uncomment this to see the error

lan, long = ahnedabad_cord
print("Latitude:", lan, "Longitude:", long)

print(ahnedabad_cord[0])

tuple_example = (1, 2, 3, 4, 5)
print("Length of tuple:", len(tuple_example))
print("Sliced tuple (first three elements):", tuple_example[0:3])
print("Sliced tuple (last two elements):", tuple_example[-2:])
print("Max value in tuple:", max(tuple_example))
print("Min value in tuple:", min(tuple_example))
print("Sum of elements in tuple:", sum(tuple_example))
print("Tuple repeated twice:", tuple_example * 2)

def get_user_info():
    return 'om', 19, 'ahmedabad'  #returning multiple values as tuple
name, age, city = get_user_info()
print("Name:", name, "Age:", age, "City:", city)

#basic unpacking
a,b,c = (10,20,30)
print("Basic unpacking:", a, b, c)
#extended unpacking
x, *y, z = (1,2,3,4,5,6,7,8,9)
print("Extended unpacking:", x, y, z)