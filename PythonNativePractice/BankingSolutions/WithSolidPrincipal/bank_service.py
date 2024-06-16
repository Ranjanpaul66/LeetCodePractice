from bank_account import BankAccount
class BankService:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder):
        if account_number in self.accounts:
            raise ValueError("Account number already exists.")
        else:
            self.accounts[account_number] = BankAccount(account_number, account_holder)
            return f"Account created for {account_holder} with account number {account_number}."

    def get_account(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account not found.")
        return self.accounts[account_number]
