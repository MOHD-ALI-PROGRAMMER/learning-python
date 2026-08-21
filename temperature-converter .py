temperature= float(input("ENTER YOUR TEMPERATURE: "))

print("1. fahrenheit → celsius")
print("2. celsius → fahrenheit")
print("3. fahrenheit → kelvin")
print("4. kelvin → fahrenheit")
print("5. celsius → kelvin")
print("6. kelvin → celsius")

choice = int(input("ENTER YOUR OPERATION:"))

if choice == 1:
    celsius = (temperature-32)*5/9
    print("YOUR TEMP. IN CELSIUS IS:", celsius,"°C")

elif choice == 2:
    fahrenheit = (temperature*1.8)+32
    print("YOUR TEMP.IN FAHRENHEIT IS:", fahrenheit,"°F")

elif choice ==3:
    kelvin = ((temperature -32)*5/9)+273.15
    print("YOUR TEMP. IN KELVIN IS:", kelvin,"K")

elif choice == 4:
    fahrenheit = ((temperature-273.15)*9/5)+32
    print("YOUR TEMP. IN FAHRENHEIT IS:",fahrenheit,"°F")

elif choice == 5:
    kelvin = temperature + 273.15
    print("YOUR TEMP. IN KELVIN IS:",kelvin,"K")

elif choice == 6:
    celsius = temperature - 273.15
    print("YOUR TEMP. IN CELSIUS IS:", celsius,"°C")

else:
    print("INVALID OPERATION SIR ")
    
    print("TRY AGAIN")