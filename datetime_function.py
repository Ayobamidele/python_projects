from datetime import datetime , timedelta

p
def age():
    today = datetime.now()
    print("what is your birth year:")
    birthYear = input()
    year = datetime.strptime(birthYear, '%Y')
    print(f"you are {today.year - year.year} years old")

# yesterday = timedelta(weeks=2)

# print(today - yesterday)

# print(today.year - 2004)

# print(today.year - str(year))

# print(type(year))
# print(year)
# print(today.year - year.year)

age()