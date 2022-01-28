from bank import Bank

myBank = Bank()
myBank.get_account("401132-0676", "1005")

# ans = True
# while ans:
#     print("1.Add a customer \n2.Delete a Student \n3.withdraw some cash \n4.Exit/Quit")
#     ans = input("What would you like to do? ")
#     if ans == "1":
#         name = input("Please enter customers name: ")
#         pnr = input("Please enter customers personal number: ")
#         myBank.add_customer(name, pnr)
#         break
#     elif ans == "2":
#         print("\n Student Deleted")
#     elif ans == "3":
#         myBank.get_accounts()
#         pnr = input("Please enter your social security number: ")
#         acc_id = input("Enter from which account you wish to withdraw: ")
#         amount = input("Enter amount to withdraw: ")
#         myBank.withdraw(pnr, acc_id, amount)
#         myBank.get_accounts()
#     elif ans == "4":
#         print("\n Goodbye")
#         ans = False
#     elif ans != "":
#         print("\n Not Valid Choice Try again")
