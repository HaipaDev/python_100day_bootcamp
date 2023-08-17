print("Welcome to the leap year checker!")
yearInput=int(input("Enter the year: "))
leapYear=False

if yearInput%4==0 and yearInput%100!=0 or yearInput%400==0:
    leapYear=True
else: leapYear=False

if leapYear==True: print("The year is a leap year!")
else: print("The year is not a leap year.")