total = 0.0
shopping = True

while shopping:

    amount = float(input("Enter product amount: ₹"))
    total = total + amount

    product = input("Add another product? yes/no: ")

    if product == "yes":
        shopping = True

    elif product == "no":
        shopping = False

    else:
        print("Invalid choice")
        shopping = False


print("Your total product amount:", total)


# DISCOUNT

if total >= 5000:
    discount = total * 20 / 100
    print("You got a 20% discount")

elif total >= 2000:
    discount = total * 10 / 100
    print("You got a 10% discount")

else:
    discount = 0
    print("Sorry, no discount")


print("Your discount amount:", discount)


# PRICE AFTER DISCOUNT

price_after_discount = total - discount


# GST

if total >= 5000:
    print("You pay 10% GST")
    gst = price_after_discount * 10 / 100

elif total >= 2000:
    print("You pay 5% GST")
    gst = price_after_discount * 5 / 100

else:
    print("No GST")
    gst = 0


print("Your GST amount:", gst)


# FINAL TOTAL

final_total = price_after_discount + gst

print("Your final total:", final_total)

print("Thank you for shopping!")