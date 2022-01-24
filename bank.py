import re
from customer import Customer
from account import Account

class Bank():
    
    customers = []
    cstmrtxt = "customers.txt"
    id = []

    def __init__(self):
        self.customer_data = []
        self.name = "MyBank" 
    
    def _load(self):
        self.customer_data = []
      
        with open (self.cstmrtxt) as txtFile:
            for x in txtFile:
                self.customer_data.append(x.strip())
        return self.customer_data

    def get_customers(self):
        
        Bank._load(self)

        for i in self.customer_data:
            cust = i.strip().split(":")
            cstmr = Customer(cust[1], cust[2], cust[3])
            self.customers.append(cstmr)

        return self.customers

    def add_customer(self, name, pnr):

        Bank._load(self)
        
        id = Bank.get_last_id(self)


        if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
            print("Sorry wrong format, please enter personal number as xxxxxx-xxxx")
            return False
        elif any(pnr in s for s in self.customer_data):
            return False
        else:
            textfile = open("customers.txt","a")
            textfile.write(f'\n{id}:{name}:{pnr}' )
            textfile.close()
            return True

    def get_customer(self, pnr):

        Bank._load(self)

        for i in self.customer_data:
            x = i.strip().split(":")
            str1 = ": "
            if x[2] == pnr:
                print(f"Name: {x[1]}\nPersonal number: {x[2]}\nAccountNumber: {str1.join(x[3:])}")

    def change_customer_name(name, pnr):

        textfil = Bank._load()
        for i in textfil:
            x = re.sub("#",":",str(i))
            y = x.split(":")
            if y[2] == pnr:
                y[1] = name
                print(y)
    
    def get_last_id(self):

        Bank._load(self)

        for i in self.customer_data:
            x = i.strip().split(":")
            self.id.append(x[0])
        
        last_id = int(self.id[-1]) + 1

        return last_id
