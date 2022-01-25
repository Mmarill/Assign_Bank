import re
from customer import Customer
from account import Account

class Bank():
    
    customers = []
    id = []
    ctxt = "customers.txt"
    customer_data = []
    accounts = []

    def __init__(self):
        self.name = "MyBank" 
            
    
    def _load(self):
        self.customer_data = []

        with open (self.ctxt) as txtFile:
            for x in txtFile:
                self.customer_data.append(x.strip())
        return self.customer_data

    def get_customers(self):
        
        Bank._load(self)

        for i in self.customer_data:
            x = re.sub("#", ":", str(i))
            y = x.split(":")
            cstmr = Customer(y[1], y[2], y[3])
            self.customers.append(cstmr)
        return self.customers

    def get_accounts(self):
        account_data = []
        for x in self.customer_data:
            account_data[x[0]] = x[3:]
        for x, y in account_data:
            if len(y) > 3:
                first_account = Account(int(x), int(y[0]), y[1], float(y[2].split("#")[0]))
                second_account = Account(int(x), int(y[2].split("#")[1]), y[3], float(y[4]))
                self.accounts.append(first_account)
                self.accounts.append(second_account)
            elif len(y) == 3:
                first_account = Account(int(x), int(y[0]), y[1], float(y[2]))
                self.accounts.append(first_account)
            else:
                pass

           

    def add_customer(self, name, pnr):

        Bank._load(self)
      
        if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
            print("Sorry wrong format, please enter personal number as xxxxxx-xxxx")
            return False
        elif any(pnr in s for s in self.customer_data):
            print("Customer with same socail security number already exists")
            return False
        else:
            textfile = open("customers.txt","a")
            textfile.write(f'\n{id}:{name}:{pnr}' )
            textfile.close()
            return True

    def get_customer(pnr):
        customers = Bank._load()

        for i in customers:
            x = re.sub("#", ":", str(i))
            y = x.split(":")
            str1 = ": "
            if y[2] == pnr:
                print(f"Name: {y[1]}\nPersonal number: {y[2]}\nAccountNumber: {str1.join(y[3:])}")

    def get_last_id(self):

        Bank._load(self)

        for i in self.customer_data:
            x = i.strip().split(":")
            self.id.append(x[0])
        
        last_id = int(self.id[-1]) + 1

        return last_id

    def change_customer_name(self, newname, pnr):
        Bank._load(self)

        for line in self.customer_data:
            if str(pnr) in line:
                index = self.customer_data.index(line)
                name = line.split(":")[1]
                new_line = line.replace(name, newname)
                self.customer_data[index] = new_line

        print(self.customer_data)
        with open(self.ctxt, "w") as f:
            f.writelines("%s\n" % l for l in self.customer_data)

# class Bank():

#     customers = []
#     cstmrtxt = "customers.txt"
#     id = []

#     def __init__(self):
#         self.customer_data = []
#         self.name = "MyBank" 
    
#     def _load(self):
      
#         with open(self.cstmrtxt) as textfil:
#             for line in textfil:
#                 a = re.sub("#",":", str(line))
#                 b = a.split(":")
#                 customer = {"customer":Customer( b[0], b[1], b[2]), "id":b[0], "pnr":b[2]}
#                 number_of_accounts = int((len(b)-3)/3)
#                 accounts = []
#                 while number_of_accounts > 0:
#                     x = 3+3*(number_of_accounts - 1)
#                     accountobj = Account(b[x],b[x+1],b[x+2])
#                     number_of_accounts-=1
#                     accounts.append(accountobj)
#                     customer["accounts"] = accounts
#                     self.customer_data.append(customer)
#         return self.customer_data

#     def get_customers(self):
        
#         Bank._load(self)

#         for i in self.customer_data:
#             cstmr = i["customer"]
#             self.customers.append(cstmr)

#         return self.customers

#     def add_customer(self, name, pnr):

#         Bank._load(self)
        
#         id = Bank.get_last_id(self)


#         if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
#             print("Sorry wrong format, please enter personal number as xxxxxx-xxxx")
#             return False
#         elif any(pnr in s for s in self.customer_data):
#             print("Customer with same socail security number already exists")
#             return False
#         else:
#             textfile = open("customers.txt","a")
#             textfile.write(f'\n{id}:{name}:{pnr}' )
#             textfile.close()
#             return True

#     def get_customer(self, pnr):

#         Bank._load(self)

#         for i in self.customer_data:
#             if any(pnr in s for s in self.customer_data):
#                 print(i["customer"])
#             break
        

#         # for i in self.customers:
#         #     if pnr == 

#         # for i in self.customer_data:
#         #     x = i.strip().split(":")
#         #     str1 = ": "
#         #     if x[2] == pnr:
#         #         print(f"Name: {x[1]}\nPersonal number: {x[2]}\nAccountNumber: {str1.join(x[3:])}")

#     def change_customer_name(self, pnr, name):

#         # Bank._load(self)

#         # Bank.get_customers(self)

#         # pnr = input("Enter social security number for the customer whose name you want to change: ")
#         # name = input("Enter the new name for the customer: ")

#         # for line in self.customer_data:
#         #     # x = line.strip().split(":")
#         #     if pnr in line:
#         #         index = lines.index(line)
#         #         new_line = line
#         #         lines[index] = new_line
#         #         f = open(self.cstmrtxt, "w")
#         #         f.writelines(line)
#         #         f.close()

#         # f = open(self.cstmrtxt, "r")
#         # lines = f.readlines()
#         # f.close()

#         # for line in lines:
#         #     if str(pnr) in line:
#         #         print(line[1])
#         #         index = lines.index(line)
#         #         new_line = line.replace(line[1], newname)
#         #         lines[index] = new_line
    

#         # f = open(self.cstmrtxt, "w")
#         # f.writelines(lines)
#         # f.close()

#         Bank._load(self)

#         for i in self.customer_data:
#             x = i.strip().split(":")
#             str1 = ": "
#             if x[2] == pnr:
#                 index = self.customer_data.index(x)
#                 new_line =(f"Name: {name}\nPersonal number: {x[2]}\nAccountNumber: {str1.join(x[3:])}")
#                 self.customer_data[index] = new_line

#         f = open(self.cstmrtxt, "w")
#         f.writelines(new_line)
#         f.close

#     def get_last_id(self):

#         Bank._load(self)

#         for i in self.customer_data:
#             self.id.append(i["id"])
        
#         last_id = int(self.id[-1]) + 1

#         return last_id

#     def print_cust(self):

#         Bank.get_customers(self)

#         for i in self.customers:
#             print(i)

#     def get_account(self):

#         Bank._load(self)

#         print(self.accounts)
    
    