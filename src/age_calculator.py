# Simple Age Calculator
# Author: Alwaleed Alahmadi
# Calculates age based on birth date

import datetime

num_of_people = int(input("Enter how many people you want to calc their age: "))

people = []

for _ in range(num_of_people):
    name = input("Enter the name: ")
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    day = int(input("Enter the day: "))

    birth_date = datetime.date(year, month, day)
    today = datetime.date.today()

    age = today.year - birth_date.year - (
        (today.month, today.day) < (birth_date.month, birth_date.day)
    )

    people.append([name, birth_date, age])

for person in people:
    print(f"{person[0]} is {person[2]} years old and was born on {person[1].strftime('%A, %d %B %Y')}")
















