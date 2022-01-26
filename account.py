class Account():
    def __init__(self, user_id, accountNo, accountType, balance):
        
        self.id = user_id
        self.balance = balance
        self.accountType = accountType
        self.accountNo = accountNo
    
    def __str__(self):
        return str(self.user_id) + " " + str(self.accountNo) + " " + str(self.accountType) + " " + str(self.balance)

    def __repr__(self):
        return "{}:{}:{}".format(self.accountNo, self.accountType, self.balance)