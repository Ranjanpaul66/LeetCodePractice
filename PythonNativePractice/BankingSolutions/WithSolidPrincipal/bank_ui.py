class BankUI:
    def __init__(self, bank_service):
        self.bank_service = bank_service

    def display_menu(self):
        while True:
            print("\nWelcome to Simple Bank")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. Exit")

            choice = input("Enter your choice: ")

            try:
                if choice == '1':
                    self.create_account()
                elif choice == '2':
                    self.deposit_money()
                elif choice == '3':
                    self.withdraw_money()
                elif choice == '4':
                    self.check_balance()
                elif choice == '5':
                    print("Thank you for using Simple Bank. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError as e:
                print(f"Error: {e}")

    def create_account(self):
        account_number = input("Enter account number: ")
        account_holder = input("Enter account holder name: ")
        message = self.bank_service.create_account(account_number, account_holder)
        print(message)

    def deposit_money(self):
        account_number = input("Enter account number: ")
        account = self.bank_service.get_account(account_number)
        amount = float(input("Enter amount to deposit: "))
        message = account.deposit(amount)
        print(message)

    def withdraw_money(self):
        account_number = input("Enter account number: ")
        account = self.bank_service.get_account(account_number)
        amount = float(input("Enter amount to withdraw: "))
        message = account.withdraw(amount)
        print(message)

    def check_balance(self):
        account_number = input("Enter account number: ")
        account = self.bank_service.get_account(account_number)
        message = account.check_balance()
        print(message)
