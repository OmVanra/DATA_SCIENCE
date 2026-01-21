#file modules in python

# "W" - opens files for writing only. 
# Creates a new file if not exist. 
# Completely erases content if file exists. 
# File pointer at beginning.
with open('testfile.txt', 'w', encoding='utf-8') as file:
    file.write("This is a test file. \n")
    file.write('This file is created using "w" mode.\n')
    file.write("by")

with open('testfile.txt', 'w', encoding='utf-8') as file:
    file.write("New content overwrites old content.\n")
    file.write("File mode 'w' used again.\n")
    
# "r" - opens files for reading only. 
# File pointer at beginning.
# Raises error if file does not exist.
with open('testfile.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print("Reading from file:")
    print(content)    
    
# reading line by line and processing
with open('groceries.txt', 'w', encoding='utf-8') as file:
    file.write("Apples\nBananas\nCarrots\nDates\nEggs\n")
    
with open('groceries.txt', 'r', encoding='utf-8') as file:
    print('Grocery List:')
    for line in file:
        cleaned = line.strip()
        if cleaned:
            print("-", cleaned.upper())
        
# "a" (append) - Opens file for writing only
# Creates new file if it doesn't exist
# Preserves existing content and adds new data at the end
# File pointer starts at the end of file

with open('groceries.txt', 'a', encoding='utf-8') as file:
    file.write("Fish\nGrapes\nHoney\n")