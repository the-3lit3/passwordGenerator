import random
import time
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def simplePass():
    #Function to generate a simple password
    password = ""
    for char in range(1, nr_letters + 1):
        password += random.choice(letters)
    for char in range(1, nr_symbols + 1):
        password += random.choice(symbols)
    for char in range(1, nr_numbers + 1):
        password += random.choice(numbers)
    print("Password : " + password)

def advPass():
    #function definition to generate a more complex password
    password_list = []
    for char in range(1, nr_letters + 1):
        password_list += random.choice(letters)
    for char in range(1, nr_symbols + 1):
        password_list += random.choice(symbols)
    for char in range(1, nr_numbers + 1):
        password_list += random.choice(numbers)

    #print(password_list) password before randomized
    random.shuffle(password_list)
    #print(password_list) password after randomization

    password = ""

    for char in range(0, len(password_list)):
        password += password_list[char]

    print(f"\nYour password is : {password}" )


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
choice = 0
while choice != 3:
    print("1 = Simple Password\n2 = Advanced Password\n3 = Exit")
    choice = int(input("Enter Choice : "))

    if choice == 1:
        simplePass()
        break
    elif choice == 2:
        advPass()
        break
    elif choice == 3:
        exit(1)
        break
    if choice > 3 or choice < 0:
        print("Invalid option...")
        time.sleep(3)