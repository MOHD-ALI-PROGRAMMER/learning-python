weight = float(input("ENTER YOUR WEIGHT IN (KG): "))
height = float(input("ENTER YOUR HEIGHT IN (meter): ")) 

bmi = weight /( height**2)
print("YOUR BMI IS:", round(bmi,2))

if bmi < 18:
    print("category: underweight")

elif bmi < 24.9:
    print("category: normal/healthy")

elif bmi < 29.9:
    print("category: overweight")

else:
    print("category: obesity")