rev = 0
num = int(input("Enter your number; "))

while num > 0:
    digit = num % 10
    num = num // 10
    rev = (rev*10)+digit
print(rev)