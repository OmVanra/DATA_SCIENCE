# ----------------------
# Math module
# ----------------------
import math

print("Pi ≈", math.pi)
print("Square root of 144:", math.sqrt(144))
print("Ceiling of 4.2:", math.ceil(4.2))
print("Floor of 4.8:", math.floor(4.8))
print("5 to the power 3:", math.pow(5, 3))

# ----------------------
# Random module
# ----------------------
import random

print("Random float 0-1:", random.random())
print("Random integer 1-100:", random.randint(1, 100))

cities = ["Surat", "Ahmedabad", "Mumbai", "Bangalore", "Delhi"]
print("Random city for next job:", random.choice(cities))

# Shuffle list
random.shuffle(cities)
print("Shuffled cities:", cities)

# ----------------------
# Mini Challenge
# ----------------------
# Write a function that:
# 1. Asks user for a number
# 2. Calculates square root (handle errors)
# 3. If successful → also show ceiling and floor of the result
# 4. Use math module + proper error handling

def safe_sqrt():
    try:
        num = float(input("Enter a number to find square root: "))
        if num < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        
        root = math.sqrt(num)
        print(f"Square root: {root}")
        print(f"Ceiling: {math.ceil(root)}")
        print(f"Floor: {math.floor(root)}")
        
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Operation complete.")

safe_sqrt()