year = int(input("Enter your year: "))

if year % 400 == 0:
    print("It's leap year")

elif year % 100 == 0:
    print("It's not leap year")

elif year % 4 == 0:
     print("It's leap year")

else:
    print("It's not a leap year")