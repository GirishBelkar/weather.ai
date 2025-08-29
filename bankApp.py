bankaccounts = []

while True:
    print("1. Create New Account")
    print("2. Show Acccounts")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")

    choice = int(input("Enter Choice :"))

    match choice:
        case 1:
            accno = int(input("Enter account number = "))
            accname = input("Enter account name = ")
            balance = float(input("Enter balance = "))

            bankaccounts.append([accno, accname, balance])
            print("New Account Created Successfully")
        case 2:
            if len(bankaccounts)==0:
                print("No bank accounts")
            else:
                for item in bankaccounts:
                    print(item)
            
        case 3:
            if len(bankaccounts) == 0:
                print("No bank accounts to deposit into.")
                continue

            accno = int(input("Enter account number to deposit into: "))
            pos = -1
            for i in range(len(bankaccounts)):
                if bankaccounts[i][0] == accno:
                    pos = i
                    break

            if pos == -1:
                print("Invalid account number.")
            else:
                add = float(input("Enter amount to deposit: "))
                if add <= 0:
                    print("Invalid deposit amount.")
                else:
                    bankaccounts[pos][2] += add
                    print(f"INR {add} deposited successfully to account {accno}.")

        case 4:
            if len(bankaccounts) == 0:
                print("No bank accounts available.")
                continue

            accno = int(input("Enter account number to withdraw from: "))
            pos = -1
            for i in range(len(bankaccounts)):
                if bankaccounts[i][0] == accno:
                    pos = i
                    break

            if pos == -1:
                print("Invalid account number.")
            else:
                amount = float(input("Enter withdrawal amount: "))
                if amount <= 0:
                    print("Invalid amount entered.")
                elif amount > bankaccounts[pos][2]:
                    print("Insufficient balance.")
                else:
                    bankaccounts[pos][2] -= amount
                    print(f"INR {amount} withdrawn from account {accno}.")

        case 5:
            break