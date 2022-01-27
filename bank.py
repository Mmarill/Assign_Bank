import re
from customer import Customer
from account import Account

class Bank():
    
    customers = []
    id = []
    ctxt = "customers.txt"
    customer_data = []
    accounts = []
    accountNo = []
    acc = []

    def __init__(self):
        self.name = "MyBank" 
        self.customers = []
        self._load()
        self.get_customers()

    def _load(self):
        self.customer_data = []

        with open (self.ctxt) as txtFile:
            for x in txtFile:
                self.customer_data.append(x.strip())
        return self.customer_data

    def get_customers(self):

        for i in self.customer_data:
            x = re.sub("#", ":", str(i))
            y = x.split(":")
            cstmr = Customer(y[0], y[1], y[2])
            self.customers.append(cstmr)

        return self.customers
    
    def get_customers_test(self):
        
        for cstmr in self.customers:
            print(cstmr.name, cstmr.id, cstmr.pnr)


    def get_customer(self, pnr):

        Bank.get_accounts(self)
        Bank.get_customers(self)
        
        for i in self.customers:
            if pnr in repr(i):
                x = str(i).split()
                y = x[0], x[1], x[2], x[3]
                id = y[0]
                for line in self.accounts:
                    if id in str(line):
                            self.acc.append(line)
                            z = re.sub(",", ":", str(self.acc))
                            t = str(z).strip().split(":")
                            if len(t) > 3:
                                firstacc = (f"First account:\n\tAccount no: {t[0]}\n\tAccount type: {t[1]}\n\tBalance: {t[2]}\n")
                                secondacc = (f"Second account: \n\tAccount no: {t[3]}\n\tAccount type: {t[4]}\n\tBalance: {t[5]}")
                            elif len(t) == 3:
                                firstacc = (f"First account:\n\tAccount no: {t[0]}\n\tAccount type: {t[1]}\n\tBalance: {t[2]}\n")
                                secondacc = (f"Second account: \n\tAccount no: {None}\n\tAccount type: {None}\n\tBalance: {None}")
    
        print(f"Customer id: {y[0]}\nName: {y[1]} {y[2]}\nSocial security number: {y[3]}\n{firstacc}{secondacc}")

    def get_accounts(self):

        self.accounts = []
        self.accountNo = []

        Bank._load(self)
        account_data = {}

        for i in self.customer_data:
            x = i.split(":")
            account_data[x[0]] = x[3:]

        for x, y in account_data.items():
            if len(y) > 3:
                first_account = Account(int(x), int(y[0]), y[1], float(y[2].split("#")[0]))
                second_account = Account(int(x), int(y[2].split("#")[1]), y[3], float(y[4]))
                self.accounts.append(first_account)
                self.accounts.append(second_account)
                self.accountNo.append(y[0])
                self.accountNo.append(y[2].split("#")[1])
            elif len(y) == 3:
                first_account = Account(int(x), int(y[0]), y[1], float(y[2]))
                self.accounts.append(first_account)
                self.accountNo.append(y[0])
            else:
                pass

    def get_account(self, pnr, id):
        Bank.get_accounts(self)
        Bank.get_customers(self)
        temp = 0
        if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
            print("Sorry wrong format, please enter personal number as xxxxxx-xxxx")
        else:
            for i in self.customers:
                if pnr in repr(i):
                    x = str(i).split()
                    cstm_id = x[0]
                    for line in self.accounts:
                        if cstm_id + id in str(line):
                            linelist = str(line).split(" ")
                            return f"Account number: {linelist[1]}, account type: {linelist[2]} {linelist[3]}, balance: {linelist[4]}"
                        else:
                            temp += 2
                    if temp == len(self.accounts)*2:
                        print(f"This customer doesnt have an account with this id: {id}")
                elif pnr not in repr(i):
                    temp += 1
            if temp==len(self.customers): 
                print(f"No customer with either social security number: {pnr} or with account number: {id}")
    
    def add_customer(self, name, pnr):

        Bank._load(self)
      
        if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
            print("Sorry wrong format, please enter personal number as xxxxxx-xxxx")
            return False
        elif any(pnr in s for s in self.customer_data):
            print("Customer with same social security number already exists")
            return False
        else:
            textfile = open("customers.txt","a")
            textfile.write('\n' + Bank.get_new_id(self) + f':{name}:{pnr}:' + Bank.get_top_account(self) + f':debit account:0.0')
            textfile.close()
            return True

    def change_customer_name(self, newname, pnr):
        Bank._load(self)

        for line in self.customer_data:
            if str(pnr) in line:
                index = self.customer_data.index(line)
                name = line.split(":")[1]
                new_line = line.replace(name, newname)
                self.customer_data[index] = new_line

     
        with open(self.ctxt, "w") as f:
            f.writelines("%s\n" % l for l in self.customer_data)
    
    def remove_customer(self, pnr):

        Bank._load(self)

        if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
            print("Sorry wrong format, please enter personal number as xxxxxx-xxxx")
            return False
        else:   
            for line in self.customer_data:
                if str(pnr) in line:
                    index = self.customer_data.index(line)
                    print(index)
                    self.customer_data.pop(index)

        print(self.customer_data)

        with open(self.ctxt, "w") as f:
            f.writelines("%s\n" % l for l in self.customer_data)

    def get_new_id(self):

        Bank._load(self)

        for i in self.customer_data:
            x = i.strip().split(":")
            self.id.append(x[0])
        
        new_id = int(self.id[-1]) + 1
        
        return str(new_id)

    def get_top_account(self):
        self.accountNo = []

        Bank.get_accounts(self)    
        print(self.accountNo)
        newAccount = int(max(self.accountNo)) + 1

        return str(newAccount)

