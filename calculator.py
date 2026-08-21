number1 = float(input("enter your number: "))
number2= float(input("enter your number: "))

print("1. multiply")
print("2. divide")
print("3. add")
print("4. substract")

choice = int(input("choose Your Operation: "))

if choice == 1:
    multiply = number1 * number2
    print("YOUR ANSWER IS:", multiply)

elif choice == 2:
     divide = number1 / number2
     print("YOUR ANSWER IS:", divide)

elif choice == 3:
     add = number1 + number2
     print("YOUR ANSWER IS:", add)
 
elif choice == 4:
     substract = number1 - number2
     print("YOUR ANSWER IS:", substarct)

else:
     print("INVALID OPTION")