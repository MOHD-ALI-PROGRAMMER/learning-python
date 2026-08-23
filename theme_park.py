age = int(input("enter your age: "))
height = float(input("enter your height in (cm: )"))
user = input("are you accompanied by an adult (yes/or): ")


if age <= 10:
    print("SORRY, you are too young to ride")
else:
    if height <= 120:
        if user == 'yes':
            print("you are able to ride sir")
        else:
            print('you are not able to ride sir')
    else:
        print("you are able to ride sir ")
