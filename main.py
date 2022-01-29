from bank import Bank

myBank = Bank()
myBank.get_customer("876954-7547")

ans = True
while ans:
    print("1.Add a customer \n2.Get customer by social security number \n3.Delete customer \n4.withdraw some cash "
          "\n5.Exit/Quit")
    ans = input("What would you like to do? ")
    if ans == "1":
        name = input("Please enter customers name: ")
        pnr = input("Please enter customers personal number: ")
        myBank.add_customer(name, pnr)
    elif ans == "2":
        pnr = input("Please enter customers social security number: ")
        myBank.get_customer(pnr)
    elif ans == "3":
        pnr = input("Please enter social security number of customer you want to delete")
        myBank.remove_customer(pnr)
    elif ans == "4":
        pnr = input("Please enter your social security number: ")
        myBank.get_customer(pnr)
        acc_id = input("Enter from which account you wish to withdraw: ")
        amount = input("Enter amount to withdraw: ")
        myBank.withdraw(pnr, acc_id, amount)
    elif ans == "4":
        print("\n Goodbye")
        ans = False
    elif ans != "":
        print("\n Not Valid Choice Try again")
