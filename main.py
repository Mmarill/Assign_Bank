import bank

myBank = bank.Bank()

# ans=True
# while ans:
#     print ("1.Add a customer \n2.Delete a Student \n3.Look Up Student Record \n4.Exit/Quit")
#     ans=input("What would you like to do? ") 
#     if ans=="1": 
#       name = input("Please enter customers name: ")
#       pnr = input("Please enter customers personal number: ")
#       bank.Bank.add_customer(name,pnr)
#       break
#     elif ans=="2":
#       print("\n Student Deleted") 
#     elif ans=="3":
#         value = input("Please enter a valid id: ")
#         with open("customers.txt","r") as fi:
#             id = []
#             for ln in fi:
#                 if ln.startswith(value):
#                     id.append(ln[2:])
#         print(id)
#     elif ans=="4":
#       print("\n Goodbye") 
#     elif ans !="":
#       print("\n Not Valid Choice Try again") 