import sys

cents = 0
coins = 0
quarters = 25
dimes = 10
nickels = 5
pennies = 1


def test(dollars):  # Creating a function to test wether the user input is composed of numbers only or not
    while True:
        try:
            val = float(dollars)  # If this is true, call the function 'charge' which will do the calculations
            charge(dollars)
            break
        except ValueError:  # If false, recursively call the test function forever until the user contributes
            test(dollars=input("Charge: $ "))


def charge(dollars):
    # Define all variables as global to avoid problems
    global cents
    global coins
    global quarters
    global dimes
    global nickels
    global pennies
    # As in here the input is guaranteed to be numeric, transform it to float type
    dollars = float(dollars)
    if dollars > 0:  # Finally, with all tests done, the program can run normaly
        if dollars == 0.00:  # If the informed value is zero
            print(f"{coins}")  # Automatically the number of coins will be zero as well

        # Converting the dollars value to cents
        cents = round(dollars * 100)
        # While cents are greater than 25, do the following:
        while cents >= 25:
            cents = cents - quarters
            coins = coins + 1

        # While cents are simultaneously greater than dimes and lesser than quarters, do the following:
        while cents < 25 and cents >= 10:
            cents = cents - dimes
            coins += 1

        # While cents are simultaneously greater than nickels and lesser than dimes, do the following:
        while cents < 10 and cents >= 5:
            cents = cents - nickels
            coins += 1

        # While cents are simultaneously greater than pennies and lesser than nickels, do the following:
        while cents < 5 and cents >= 1:
            cents = cents - pennies
            coins += 1

        # Print the number os coins in the screen
        print(f"{coins}")
        sys.exit(0)

    if dollars < 0:
        print("Invalid input.")
        dollars = charge(input("Charge: $ "))


# Get raw user input, so we can test later if it's a number or not
dollars = input("Charge: $ ")
test(dollars)