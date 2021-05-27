#Defining the function to print full name that receives 2 arguments as inputs (first_name and last_name)
def print_full_name(a, b):
    print('Hello', a, b +'! You just delved into python.')

if __name__ == '__main__':
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    #Calling the function
    print_full_name(first_name, last_name)
