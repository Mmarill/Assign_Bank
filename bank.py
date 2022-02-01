import re

from customer import Customer
from account import Account


class Bank:

    account_id = []
    ctxt = "customers.txt"
    accounts = []
    accountNo = []
    acc = []

    def __init__(self):

        self.name = "MyBank"
        self.customers = []
        self.acc_list = []
        self._load()
        self.load_customers()
        self.load_accounts()

    def _load(self):

        self.customer_data = []

        with open(self.ctxt) as txtFile:
            for x in txtFile:
                self.customer_data.append(x.strip())
        return self.customer_data

    def load_customers(self):

        self.customers = []

        Bank._load(self)

        for i in self.customer_data:
            x = re.sub("#", ":", str(i))
            y = x.split(":")
            customer = Customer(y[0], y[1], y[2])
            self.customers.append(customer)

        return self.customers

    def get_customers(self):

        for customer in self.customers:
            print(customer.name, customer.pnr)

    def get_customer(self, pnr):

        for i in self.customers:
            if pnr == i.pnr:
                customer = f'Customer id: {i.id}\nName: {i.name}\nSocial security number: {i.pnr}\n'
                acc = ""
                for line in self.accounts:
                    if i.id == line.id:
                        acc += f'\n\tAccount no: {line.accountno}\n\tAccount type: {line.accounttype}\n' \
                               f'\tBalance: {line.balance}\n '

                print(f'{customer}Accounts:{acc}')

    def add_customer(self, name, pnr):

        if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
            print("Sorry wrong format, please enter personal number as xxxxxx-xxxx")
            return False
        elif any(pnr in s for s in self.customer_data):
            print(f'Customer with social security number: {pnr} already exists')
            return False
        else:
            textfile = open("customers.txt", "a")
            textfile.write(
               "\n" + Bank.get_top_id(self) + f':{name}:{pnr}:' + Bank.get_top_account(self) + f':debit account:0.0')
            textfile.close()

        print(f'New Customer {name}: {pnr} created')

        Bank.load_accounts(self)
        Bank.load_customers(self)

    def change_customer_name(self, newname, pnr):

        if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
            print("Sorry wrong format, please enter personal number as xxxxxx-xxxx")
            return False
        elif any(pnr in s for s in self.customer_data):
            for line in self.customer_data:
                if str(pnr) in line:
                    index = self.customer_data.index(line)
                    name = line.split(":")[1]
                    new_line = line.replace(name, newname)
                    self.customer_data[index] = new_line
                    print(f'Name changed from {name} to {newname}')
        else:
            print(f'No customer with {pnr} exists')

        with open(self.ctxt, "w") as f:
            f.writelines("%s\n" % line for line in self.customer_data)

    def remove_customer(self, pnr):

        if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
            print("Sorry wrong format, please enter personal number as xxxxxx-xxxx")
            return False
        else:
            for line in self.customer_data:
                if pnr in line:
                    index = self.customer_data.index(line)
                    self.customer_data.pop(index)
                    for i in self.customers:
                        if pnr == i.pnr:
                            acc = ""
                            customer = f'Customer id: {i.id}\nName: {i.name}\nSocial security number: {i.pnr}\n'
                            for x in self.accounts:
                                if x.id == i.id:
                                    acc += f'\n\tAccount no: {x.accountno}\n\tAccount type: {x.accounttype}\n' \
                                           f'\tBalance: {x.balance}\n '

                            print(f'{customer}\nAccount closed with balance: {acc}')

        with open(self.ctxt, "w") as f:
            f.writelines("%s\n" % line for line in self.customer_data)

    def load_accounts(self):

        Bank._load(self)
        self.accounts = []
        account_data = {}

        for i in self.customer_data:
            x = i.replace("#", ":").split(":")
            account_data[x[0]] = x[3:]

        for x, y in account_data.items():
            nr_acc = len(y) / 3
            while nr_acc > 0:
                first_account = Account(str(x), y.pop(0), y.pop(0), y.pop(0))
                self.accounts.append(first_account)
                self.accountNo.append(first_account.accountno)
                nr_acc -= 1

    def get_accounts(self):

        for i in self.accounts:
            account = str(i.id) + " " + str(i.accountno) + " " + i.accounttype + " " + str(i.balance)
            self.acc_list.append(account)
            print(account)

    def get_account(self, pnr, acc_no):

        if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
            print("Sorry wrong format, please enter personal number as xxxxxx-xxxx")
        else:
            for x in self.customers:
                if pnr == x.pnr:
                    for y in self.accounts:
                        if acc_no == y.accountno and x.id == y.id:
                            return f'{y.accountno}:{y.accounttype}:{y.balance}'
                    return print(f"No account found with account number {acc_no}.")
            return print(f"No customer found with {pnr} in list")

    def add_account(self, pnr):

        if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
            print("Sorry wrong format, please enter personal number as xxxxxx-xxxx")
            return False
        else:
            for i in self.customer_data:
                if pnr in repr(i):
                    index = self.customer_data.index(i)
                    line = f'{i}#{Bank.get_top_account(self)}:debit account:0.0'
                    new_line = i.replace(i, line)
                    self.customer_data[index] = new_line

        with open(self.ctxt, "w") as f:
            f.writelines("%s\n" % line for line in self.customer_data)

        print("New account added!")

        Bank.load_accounts(self)
        Bank.load_customers(self)

    def close_account(self, pnr, acc_no):

        if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
            print("Sorry wrong format, please enter personal number as xxxxxx-xxxx")
            return False
        else:
            for line in self.customer_data:
                if pnr and acc_no in line:
                    index = self.customer_data.index(line)
                    for i in self.accounts:
                        for x in self.customers:
                            if x.id == i.id and pnr == x.pnr and acc_no == i.accountno:
                                c_account = f'\n\tAccount no: {i.accountno}\n\tAccount type: {i.accounttype}\n' \
                                           f'\tBalance: {i.balance}\n '
                                if line.count("#") == 0:
                                    Bank.remove_customer(self, pnr)
                                elif line.count("#") >= 1:
                                    acc = Bank.get_account(self, pnr, acc_no)
                                    new_line = line.replace("#" + acc, "").replace(acc + "#", "")
                                    self.customer_data[index] = new_line

                                    print(f'\nAccount closed with balance: {c_account}')

        with open(self.ctxt, "w") as f:
            f.writelines("%s\n" % line for line in self.customer_data)
        Bank._load(self)
        Bank.load_customers(self)
        Bank.load_accounts(self)

    def get_top_id(self):

        Bank._load(self)

        for i in self.customer_data:
            x = i.strip().split(":")
            self.account_id.append(x[0])

        new_id = int(self.account_id[-1]) + 1

        return str(new_id)

    def get_top_account(self):

        newaccount = int(max(self.accountNo)) + 1

        return str(newaccount)

    def withdraw(self, pnr, acc_no, amount):

        if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
            print("\nSorry wrong format, please enter social security number as xxxxxx-xxxx")
            return False
        else:
            for i in self.customer_data:
                if pnr in repr(i):
                    index = self.customer_data.index(i)
                    r1 = i.replace("#", ":").split(":")
                    if acc_no not in r1:
                        return print("\nCustomer does not have account with that account number")
                    index2 = r1.index(acc_no)
                    old_bal = r1[index2 + 2]
                    new_bal = float(old_bal) - float(amount)
                    if new_bal < 0:
                        print("\nNot enough money in account")
                        return False
                    new_line = i.replace(old_bal, str(new_bal))
                    self.customer_data[index] = new_line
                    print(f"\nWithdraw successful! \nOld balance: {old_bal} \nNew balance: {str(new_bal)}")
                    with open(self.ctxt, "w") as f:
                        f.writelines("%s\n" % line for line in self.customer_data)
                    return True

    def deposit(self, pnr, acc_no, amount):

        if re.match('[0-9]{6}-[0-9]{4}', pnr) is None:
            print("\nSorry wrong format, please enter social security number as xxxxxx-xxxx")
            return False
        else:
            for i in self.customer_data:
                if pnr in repr(i):
                    index = self.customer_data.index(i)
                    r1 = i.replace("#", ":").split(":")
                    if acc_no not in r1:
                        return print("\nCustomer does not have account with that account number")
                    nyindex = r1.index(acc_no)
                    old_bal = r1[nyindex + 2]
                    new_bal = float(old_bal) + float(amount)
                    new_line = i.replace(old_bal, str(new_bal))
                    self.customer_data[index] = new_line
                    print(f"\nDeposit successful! \nOld balance: {old_bal} \nNew balace: {new_bal}")
                    with open(self.ctxt, "w") as f:
                        f.writelines("%s\n" % l for l in self.customer_data)
                    return True

