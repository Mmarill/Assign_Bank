class Customer():

    def __init__(self, user_id, name, pnr):
        self.id = user_id
        self.name = name
        self.pnr = pnr
        
    def __str__(self):
        return self.user_id + " " + self.name + " " + self.pnr

    def __repr__(self):
        return "{} {}".format(self.name, self.pnr)