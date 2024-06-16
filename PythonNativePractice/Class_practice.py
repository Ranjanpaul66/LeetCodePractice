class Account:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def full_name(self):
        return self.first_name+" " + self.last_name

class SavingAccount(Account):
    def __init__(self, first, last, type):
        super().__init__(first, last)
        self.acc_type = type
    def acc_type(self):
        print(self.acc_type)
acc = SavingAccount("Ranjan", "Paul", "Saving acc")

print(acc.full_name())
# acc.acc_type