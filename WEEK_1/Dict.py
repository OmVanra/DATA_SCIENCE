student = {
    'name': 'om',
    'age': 19,
    'city': 'ahmedabad',
    'skills': ['python', 'java', 'c++'],
    'is_working': False
}

print("Student Dictionary:", student)
print('Name:', student['name'])
#safe access using get method
print('Age:', student.get('age'))

student['target_job'] = 'data scientist'
print("Updated Student Dictionary:", student)
student['skills'].append('machine learning')
print("Skills after adding new skill:", student['skills'])
#remove is_working key
student.pop('is_working')

#update age
student['age'] = 20
print("Final Student Dictionary:", student)

#loop through dictionary
for key, value in student.items():
    print(f'{key}: {value}')
    
    