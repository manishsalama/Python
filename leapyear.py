<<<<<<< HEAD
year = int(input("Enter a year: "))

# Check the leap year conditions
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
=======
year = int(input("Enter a year: "))

# Check the leap year conditions
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
>>>>>>> 813ba899763f67ca7c4c4aa841c8ea7ba1636e9c
    print(year, "is not a leap year")