from bank import Bank

myBank = Bank()

ans = True
while ans:
    print('*' * 20)
    print("1.Add a customer \n2.Get customer \n3.Delete customer \n4.Withdraw \n5.Deposit"
          "\n6.Get account \n7.Add account \n8.Delete account \n9.Get all customers"
          "\nE.Exit/Quit")
    print('*' * 20)

    ans = input("What would you like to do? ")
    print('*' * 20)
    if ans == "1":
        name = input("Please enter customers name: ")
        pnr = input("Please enter customers personal number: ")
        myBank.add_customer(name, pnr)
        print('*' * 20)
    elif ans == "2":
        pnr = input("Please enter customers social security number: ")
        myBank.get_customer(pnr)
        print('*' * 20)
    elif ans == "3":
        pnr = input("Please enter social security number of customer you want to delete: ")
        myBank.remove_customer(pnr)
        print('*' * 20)
    elif ans == "4":
        pnr = input("Please enter your social security number: ")
        myBank.get_customer(pnr)
        acc_id = input("Enter from which account you wish to withdraw: ")
        amount = input("Enter amount to withdraw: ")

        myBank.withdraw(pnr, acc_id, amount)
        print('*' * 20)
    elif ans == "5":
        pnr = input("Please enter your social security number: ")
        myBank.get_customer(pnr)
        acc_id = input("Enter from which account you wish to withdraw: ")
        amount = input("Enter amount to withdraw: ")
        myBank.deposit(pnr, acc_id, amount)
        print('*' * 20)
    elif ans == "6":
        pnr = input("Please enter your social security number: ")
        acc_no = input("Please enter account number: ")
        print(myBank.get_account(pnr, acc_no))
        print('*' * 20)
    elif ans == "7":
        pnr = input("Please enter social security number for whom you wish to add an account")
        myBank.add_account(pnr)
        print('*' * 20)
    elif ans == "8":
        pnr = input("Please enter social security number for whom you wish to remove an account")
        myBank.get_customer(pnr)
        acc_no = input("Please enter account number: ")
        myBank.close_account(pnr, acc_no)
        print('*' * 20)
    elif ans == "9":
        myBank.get_customers()
        print('*' * 20)
    elif ans == "E":
        print("\n Goodbye")
        ans = False
    elif ans != "":
        print("\n Not a Valid Choice Try again")
