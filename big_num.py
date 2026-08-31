def num(a:float,b:float):
    if a > b:
        print("your big number is:", a)
    
    elif b > a:
        print("your big number is:", b)

    else:
        print("both are equal")

a = float(input("enter your number: "))
b = float(input("enter your number: "))

num(a,b)