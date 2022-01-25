class Account():
    def __init__(self, balance, accountType, accountNo):
    
        self.balance = balance
        self.accountType = accountType
        self.accountNo = accountNo
    
    # def __str__(self):
    #     return self.balance + " " + self.accountType + " " + self.accountNo

    def __repr__(self):
        return "{} {} {}".format(self.balance, self.accountType, self.accountNo)
