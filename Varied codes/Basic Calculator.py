# Make a program which simulates a calculator

n1 = int(input("Enter the first int number: "))
n2 = int(input("Enter the second int number: "))

# op = operation
op = int(input("Type: 1 for Sum, 2 for Subtraction, 3 for Multiplication, 4 for Division. "))

result = 0

if op == 1:
    result = n1+n2

if op == 2:
    result = n1-n2

if op == 3:
    result = n1*n2

if op == 4:
    result = n1/n2

print("The result of your operation is: ", result)
