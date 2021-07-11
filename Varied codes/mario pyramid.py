import sys  # So I can use 'sys.exit()'


def pyramid(height):
    # if the inputed value respect the size of our pyramid, do
    if height > 0 and height <= 8:
        # for rows in range height
        for i in range(height):
            # and columns in range height (as it's always a block)
            for j in range(height):
                # say height = 8
                # 1st iteration: i = 0, j = 0, 0 + 0 = 0. 0 >= 8 - 1? No, so go to else in line 30
                # 2nd iteration: i = 0, j = 1, 0 + 1 = 1. 1 >= 7? No, so go to else in line 30
                # 3rd iteration: i = 0, j = 2, 0 + 2 = 2. 2 >= 7? No, so go to else in line 30
                # 4th iteration: i = 0, j = 3, 0 + 3 = 3. 3 >= 7? No, so go to else in line 30
                # 5th iteration: i = 0, j = 4, 0 + 4 = 4. 4 >= 7? No, so go to else in line 30
                # 6th iteration: i = 0, j = 5, 0 + 5 = 5. 5 >= 7? No, so go to else in line 30
                # 7th iteration: i = 0, j = 6, 0 + 6 = 6. 6 >= 7? No, so go to else in line 30
                # 8th iteration: i = 0, j = 7, 0 + 7 = 7. 7 >= 7? Yes, so print "#"
                if (i + j) >= (height - 1):
                    print("#", end="")
                # 1st iteration, 0 is < than 8 - 1, so, print a " "
                # 2nd iteration, 1 is < 7, so, print a " "
                # 3rd iteration, 2 is < 7, so, print a " "
                # 4th iteration, 3 is < 7, so, print a " "
                # 5th iteration, 4 is < 7, so, print a " "
                # 6th iteration, 5 is < 7, so, print a " "
                # 7th iteration, 6 is < 7, so, print a " "
                # 8th iteration, 7 is not < 7, so the first row is complete, and finally this nested for ends it's first loop
                else:
                    print(" ", end="")
            # ends each round of the loop with a new line, and finally i get's i + 1
            print()
        sys.exit(0)

    else:
        pyramid(height=int(input("What is the height of the half-pyramid?\n")))


# Forcing the user input to be an integer
num = False
while type(num) is not int:

    try:
        height = int(input("What is the height of the half-pyramid?\n"))
        pyramid(height)

    except ValueError:
        print('Incorrect format. You need to input an Integer.')
