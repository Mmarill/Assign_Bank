class Account():
    def __init__(self, user_id, balance, accountType, accountNo):
        self.user_id = user_id
        self.balance = balance
        self.accountType = accountType
        self.accountNo = accountNo
    
    def __str__(self):
        return self.user_id + " " + self.balance + " " + self.accountType + " " + self.accountNo

    def __repr__(self):
        return "{} {} {} {}".format(self.user_id, self.balance, self.accountType, self.accountNo)
