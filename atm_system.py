#ATM SYSTEM

balance = 1000
transactions = []
deposit = []
withdrawn = []

print("\n======Welcome to the ATM system======")
print("Your current balance is: ",balance )

#loop

while True:
    print("\n=====ATM Menu=====")
    print("1.Check Balance")
    print("2.Deposit ")
    print("3.Withdraw")
    print("4.Transaction History")
    print("5.Exit")

    option = input("\nEnter option: ")

    if option=="1":
        print("Your current balance is: ",balance)
#deposit
    elif option=="2":
        amount = float(input("Enter amount to deposit: "))
        
        if amount<=0:
            print("Error: Amount must be greater than 0. ")
        
        else:
            balance+=amount
            transactions.append(amount)
            deposit.append(amount)
            print("Deposit Successful!!")
            print("New Balance: ",balance)
#withdraw

    elif option=="3":

        amount=float(input("Enter amount to withdraw: "))

        if amount<=0:
            print("Error: withdrawl amount must be greater than 0. ")

        elif amount>balance:
            print("Error: Insufficient balance!! ")
        else:
            balance-=amount
            transactions.append(-amount)
            withdrawn.append(amount)
            print("Withdrawn Successful.. ")
            print("Remaining balance: ",balance)

#transaction history
    elif option== "4":
        print("\n======Transaction History======")

        if len(transactions)==0:
            print("There is no transactions yet.")

        else:
            i=1

            for t in transactions:
                if t>0:
                    print(i,". Deposited: ",t)
                else:
                    print(i,". Withdrawn: ",-t)
                i+=1

#report 
        total_deposited=0
        for d in deposit:
            total_deposited= total_deposited + d

        total_withdraw=0
        for w in withdrawn:
            total_withdraw= total_withdraw + w

        print("Total Deposited: ",total_deposited)
        print("Total Withdrawn: ",total_withdraw)
        print("Current Balance: ",balance)
#exit    
    elif option=="5":
        print("\nThank you for using ATM. Have a nice day!")
        break

    else:
        print("Invalid Input! Please select a number between (1-5)")
                


        
        


