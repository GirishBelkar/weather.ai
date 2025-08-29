loan_applications = []

while True:
    print("1. Apply for Loan")
    print("2. Show Loan Applications")
    print("3. Pay Loan EMI")
    print("4. Exit")

    choice = int(input("Enter choice :"))

    match choice:
        case 1:
            acc_number = int(input("Enter Account number = "))
            acc_name = input("Enter accont name = ")
            loan_amount = float(input("Enter loan amount = "))
            rate_of_interest = float(input("Enter rate of interest = "))
            period = int(input("Enter number of months = "))

            loan_applications.append([acc_number, acc_name, loan_amount, rate_of_interest, period, loan_amount + loan_amount*rate_of_interest*(period/12)/100,  "NEW"])
        
        case 2:
            if len(loan_applications) == 0:
                print("No Loan Applications")
            else:
                for item in loan_applications:
                    print(item)
        
        case 3:
            if len(loan_applications) == 0:
                print("No loan applications to show.")
            else:
                loan_acc_number = int(input("Enter loan account number to pay EMI :"))
                
                pos=-1
                for i in range(0, len(loan_applications)):
                    if loan_applications[i][0]==loan_acc_number:
                        pos = i

                if pos==-1:
                    print("Invalid Account number")
                else:
                    emi_amount = int(input("Enter emi amount = "))
                    loan_applications[pos][5]-=emi_amount
                    print(f"INR {emi_amount} debited from your loan account")
                
                    if emi_amount > loan_applications[pos][5]:
                        print("please check loan amount")
                    
        case 4:
            break

        case _:
            print("Invalid choice")