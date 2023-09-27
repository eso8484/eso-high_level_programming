''''year = int(input("enter a given a year: "))

if(year % 4 == 0):
    if(year % 100 != 0 or year % 400 == 0):
        print("It's a leap year")
    else:
        print("It's not a leap year")
else:
    print("It's not a leap year")
'''

year = int(input("enter a given a year: "))

if(year % 4 == 0):
    if(year % 100 == 0 and year % 400 == 0):
        print("It's a leap year")
    elif year % 100 == 0:
        print("It's not a leap year")
    else:
        print("It's leap year")
else:
    print("It's not a leap year")

