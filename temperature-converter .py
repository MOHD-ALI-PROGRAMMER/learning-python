number = float(input("ENTER YOUR TEMPERATURE: "))

print("1. fahrenheit → celsius")
print("2. celsius → fahrenheit")

choice = int(input("ENTER YOUR OPERATION:"))

if choice == 1:
    celsius = (number-32)*5/9
    print("YOUR TEMP. IN CELSIUS IS:", celsius,"°C")

elif choice == 2:
    fahrenheit = (number*1.8)+32
    print("YOUR TEMP.IN FAHRENHEIT IS:", fahrenheit,"°F")

else:("INVALID OPERATION SIR")