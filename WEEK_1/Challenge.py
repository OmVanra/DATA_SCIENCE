# Mini Challenge – Log Writer (very important!)
# Write a small program/script called log_writer.py that:

# Asks user for: Day number, Topic studied, Hours spent, One short note
# Appends this as a new row to my_learning_log.csv (with header on first run if file doesn't exist)
# Then reads the entire file and prints a nice summary table (just using print)

import os
import csv
def log_study_session():
    filename = 'my_learning_log.csv'
    file_exists = os.path.isfile(filename)
    day = input("Enter Day number: ")
    topic = input("Enter Topic studied: ")
    hours = input("Enter Hours spent: ")
    note = input("Enter One short note: ")
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Day', 'Topic', 'Hours', 'Note']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({'Day': day, 'Topic': topic, 'Hours': hours, 'Note': note})
    print("\nLearning Log Summary:")
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        print(f"{'Day':<10}{'Topic':<30}{'Hours':<10}{'Note'}")
        print("-" * 70)
        for row in reader:
            print(f"{row['Day']:<10}{row['Topic']:<30}{row['Hours']:<10}{row['Note']}") 
log_study_session()
            