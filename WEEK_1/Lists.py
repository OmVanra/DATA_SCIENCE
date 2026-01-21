cities = ['Ahmedabad', 'Surat', 'Vadodara', 'Rajkot', 'Gandhinagar']

# Print the list of cities
print("List of cities:", cities)

# Add a new city to the list
new_city = input("Enter a new city to add: ")
cities.append(new_city)

print("Updated list of cities:", cities)

#print first , last and therd city
print(cities[0], cities[-1], cities[2])

# Find the number of cities in the list
print("Number of cities in the list:", len(cities))

#Slice the list to get the first three cities
print("First three cities:", cities[0:3])
#Slice the list to get the last two cities
print("Last two cities:", cities[-2:])

#insert a city at secound position
cities.insert(1, 'Bhavnagar')
print("List after inserting a city at second position:", cities)

#remove a city from the list
city_to_remove = input("Enter a city to remove: ")
cities.remove(city_to_remove)
print("List after removing the city:", cities)

