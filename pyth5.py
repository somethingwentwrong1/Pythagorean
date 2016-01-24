# Import system and use strings.
import sys
import string
# It is running.
running = True
# When it is running, do this.
while running:
    print("1 = Find Hypotenuse")
    print("2 = Find Base or Height")
    print("3 = Quit")
# Insert the numbers of the user to my equation setting.
# Finding Hypotenuse is square root Base**2 + Height**2
    cmd = int(input("Enter number : "))
    if cmd == 1:
        print("Find Hypotenuse")
        first = int(input("Enter Base :"))
        second = int(input("Enter Height :"))
        result = (first**2 + second**2)**(0.5)
        print(first, '+', second, '=', result)
# Insert the numbers of the user to my equation setting.
# Finding Base or Height is square roo Hypotenuse**2 - Base or Height**2
    elif cmd == 2:
        print("Find Base or Height")
        first = int(input("Enter Hypotenuse :"))
        second = int(input("Enter the other Base or Height you know:"))
        result = (first**2 - second**2)**(0.5)
        print(first, '-', second, '=', result)
# Quit if the user selects 3.
    elif cmd == 3:
        print 'Good Bye:)'
        sys.exit(0)
