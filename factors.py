def number(a:int):

    for i in range(1,a+1):
        if a % i == 0:
            print(i)

a = int(input("Enter your number: "))
number(a)