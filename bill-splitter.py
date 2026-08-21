bill = float(input("enter your total bill "))
people = int(input("enter total people "))
tip = float(input("enter tip amount "))

total_bill = bill + tip
each_person = total_bill/people

print("total_bill:" , total_bill)
print("each prson pays:", each_person)