a = int(input("enter your first number: "))
d = int(input("enter your common difference: "))
n = int(input("which n-th term do you want: "))

for i in range(1,n+1):
    an = a + (i-1)*d
    print(an)

sn = n/2*(2*a+(n-1)*d)
print("sum of all number=", sn)