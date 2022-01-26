class Account():
    def __init__(self, id, balance, accountType, accountNo):
        
        self.id = id
        self.balance = balance
        self.accountType = accountType
        self.accountNo = accountNo
    
    def __str__(self):
        return str(self.id) + " " + str(self.balance) + " " + str(self.accountType) + " " + str(self.accountNo)

    def __repr__(self):
        return "{}:{}:{}".format(self.balance, self.accountType, self.accountNo)