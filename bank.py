import re
from collections import Counter
from itertools import count

from customer import Customer
from account import Account


class Bank:
    id = []
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

        for i in self.customer_data:
            x = re.sub("#", ":", str(i))
            y = x.split(":")
            cstmr = Customer(y[0], y[1], y[2])
            self.customers.append(cstmr)

        return self.customers

    def get_customers(self):

        for cstmr in self.customers:
            print(cstmr.name, cstmr.pnr)

    def get_customer(self, pnr):

        for i in self.customers:
            if pnr == i.pnr:
                for line in self.accounts:
                    if i.id == line.id:
                        self.acc.append(line)
                        z = re.sub(",", ":", str(self.acc))
                        t = str(z).strip().split(":")
                        if len(t) > 3:
                            firstacc = (
                                f"First account:\n\tAccount no: {t[0]}\n\tAccount type: {t[1]}\n\tBalance: {t[2]}\n")
                            secondacc = (
                                f"Second account: \n\tAccount no: {t[3]}\n\tAccount type: {t[4]}\n\tBalance: {t[5]}")
                        elif len(t) == 3:
                            firstacc = (
                                f"First account:\n\tAccount no: {t[0]}\n\tAccount type: {t[1]}\n\tBalance: {t[2]}\n")
                            secondacc = (
                                f"Second account: \n\tAccount no: {None}\n\tAccount type: {None}\n\tBalance: {None}")

                print(f"Customer id: {i.id}\nName: {i.name}\nSocial security number: {i.pnr}\n{firstacc}{secondacc}")

    def load_accounts(self):
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

        Bank.load_accounts(self)
        self.acc_list = []

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

        print(f'Account number: \n\t {y.accountno}\nAccount type: \n\t{y.accounttype}\nBalance: \n\t{y.balance}')

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
                '\n' + Bank.get_new_id(self) + f':{name}:{pnr}:' + Bank.get_top_account(self) + f':debit account:0.0')
            textfile.close()
            return print(f'New Customer {name}: {pnr} created')

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
                    print(index)
                    self.customer_data.pop(index)

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

        newaccount = int(max(self.accountNo)) + 1

        return str(newaccount)

    def withdraw(self, pnr, acc_id, amount):

        for i in self.customer_data:
            if pnr in repr(i):
                index = self.customer_data.index(i)
                x = i.replace("#", ":").split(":")
                newindex = x.index(acc_id)
                old_bal = x[newindex + 2]
                new_bal = float(old_bal[:-2]) - float(amount)
                if new_bal < 0:
                    return "Not enough money in account"
                new_line = i.replace(old_bal, str(new_bal))
                self.customer_data[index] = new_line

        with open(self.ctxt, "w") as f:
            f.writelines("%s\n" % line for line in self.customer_data)

        print(f'You have withdrawn ${amount} from {acc_id} new balance: ${new_bal}')

    def deposit(self, pnr, acc_id, amount):

        for i in self.customer_data:
            if pnr in repr(i):
                index = self.customer_data.index(i)
                x = i.replace("#", ":").split(":")
                newindex = x.index(acc_id)
                old_bal = x[newindex + 2]
                new_bal = float(old_bal[:-2]) + float(amount)
                if new_bal < 0:
                    return "Not enough money in account"
                new_line = i.replace(old_bal, str(new_bal))
                self.customer_data[index] = new_line

        with open(self.ctxt, "w") as f:
            f.writelines("%s\n" % line for line in self.customer_data)

        print(f'You have deposited ${amount} to {acc_id} new balance: ${new_bal}')

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
                            if x.id == i.id:
                                if line.count("#") == 0:
                                    Bank.remove_customer(self, pnr)
                                elif line.count("#") == 1:
                                    acc = Bank.get_account(self, pnr, acc_no)
                                    new_line = line.replace("#" + acc, "").replace(acc + "#", "")
                                    self.customer_data[index] = new_line

        with open(self.ctxt, "w") as f:
            f.writelines("%s\n" % line for line in self.customer_data)


m = Bank()
m.close_account("460383-3555", "1003")
