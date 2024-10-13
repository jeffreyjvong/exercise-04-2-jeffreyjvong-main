#!/usr/bin/env python3
# GitHub 04.2: Days in a Month

# Define Main Program
def main():
    # Task 1. Take User Input
    month = int(input("> "))

    if (month != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]):
        if (month == 1):
            print(31)
        elif (month == 2):
            print(29)
        elif (month == 3):
            print(31)
        elif (month == 4):
            print(30)
        elif (month == 5):
            print(31)
        elif (month == 6):
            print(30)
        elif (month == 7):
            print(31)
        elif (month == 8):
            print(31)
        elif (month == 9):
            print(30)
        elif (month == 10):
            print(31)
        elif (month == 11):
            print(30)
        elif (month == 12):
            print(31)
        else:
            print('Invalid month')
    else:
            print('Invalid month')

# DO NOT MODIFY BELOW
if __name__ == "__main__":
    # Call Main Program
    main()