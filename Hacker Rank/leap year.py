#: This program verifies if a year is leap or not
# A leap year (also known as an intercalary year or bissextile year) is a calendar year that contains
# an additional day added to keep the calendar year synchronized with the astronomical year or seasonal year.

def leap_year(y):
    leap = False  # declaring leap = False prior to tests

#: Logic to calculate if the year have an additional day
    if y % 400 == 0:
        leap = True
    elif y % 100 == 0:
        leap = False
    elif y % 4 == 0:
        leap = True

    return leap


#: Get user input and call function
year = int(input("Enter a year: "))
print(leap_year(year))
