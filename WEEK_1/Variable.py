name = "om"
age = 22
height = 5.7
is_student = True

scores = [85, 90, 78, 92]
hands = ('left', 'right')
marks = [98, 87, 92, 85, 87]
data_marks = set(marks) # Remove duplicates by converting to a set or you can create set directly using curly braces: data_marks = {98, 87, 92, 85}
person_info = {'city': 'New York', 'country': 'USA'}
nothing = None


print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(scores))
print(type(hands))
print(type(data_marks))
print(type(person_info))
print(type(nothing))

print('name:',name,'age:', age,'height:', height,'is student? ', is_student)
print('scores:',scores)
print('hands:',hands)
print(data_marks)
print(person_info)
print(nothing)

