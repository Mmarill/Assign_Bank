class Account:
    def __init__(self, id, accountno, accounttype, balance):
        self.id = id
        self.balance = balance
        self.accounttype = accounttype
        self.accountno = accountno

    def __str__(self):
        return str(self.id) + " " + str(self.accountno) + " " + str(self.accounttype) + " " + str(self.balance)

    def __repr__(self):
        return "{}:{}:{}".format(self.accountno, self.accounttype, self.balance)
