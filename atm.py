balance = 5000
pin = 1234

user_pin = int(input("Enter your PIN: "))

if user_pin == pin:
    print("Login successfully")

    print("1. Check balance")
    print("2. Deposit amount")mohd_ali@mohd-linux:~$ cd Doc

    print("3. Withdraw amount")

    choice = int(input("Choose an option: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        deposit = float(input("Enter deposit amount: "))

        if deposit > 0:
            balance = balance + deposit
            print("Deposit successfully")
            print("Your new balance is:", balance)
        else:
            print("Invalid deposit amount")

    elif choice == 3:
        withdraw = float(input("Enter withdrawal amount: "))

        if withdraw > 0 and withdraw <= balance:
            balance = balance - withdraw
            print("Withdrawal successfully")
            print("Your new balance is:", balance)
        else:
            print("Invalid withdrawal amount")

    else:
        print("Invalid option")

else:
    print("Invalid PIN")

        