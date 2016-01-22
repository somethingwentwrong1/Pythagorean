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
# The equation for finding Hypotenuse
    cmd = int(input("Enter number : "))
    if cmd == 1:
        print("Find Hypotenuse")
        first = int(input("Enter Base :"))
        second = int(input("Enter Height :"))
        result = (first**2 + second**2)**(0.5)
        print(first, '+', second, '=', result)
# The equation for finding Base or Height.
    elif cmd == 2:
        print("Find Base or Height")
        first = int(input("Enter Hypotenuse :"))
        second = int(input("Enter the other Base or Height you know:"))
        result = (first**2 - second**2)**(0.5)
        print(first, '-', second, '=', result)
# Quit.
    elif cmd == 3:
        print 'Good Bye:)'
        sys.exit(0)
