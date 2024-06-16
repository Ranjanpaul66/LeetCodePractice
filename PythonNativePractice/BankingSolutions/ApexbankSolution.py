""" Develop a class that will represent a bank account.- The class must support the methods deposit, withdraw, and total_balance.-
The currency has coins in these denominations: 1, 5, 10, 25, 100 (penny, nickel, dime, quarter, and dollar).- Total balance method:
* Returns the total balance in terms of cents.- Deposit method:	* Must allow multiple coins of multiple denominations to be deposited in one deposit.
* For example, you can deposit 3 dollars, 7 quarters, and 11 nickels in one call to deposit. That would increase the balance by 530 cents.- Withdraw method:
* Input is the total amount to withdraw (in cents). 	* Return value is the coins that will make up the total withdraw, using the fewest number of coins required.
* Assume that the bank has an unlimited number of each denomination of coin available for withdrawals.
* For example, if withdraw is passed the number 562, the return should be 5 dollars, 2 quarters, 1 dime, and 2 pennies.
- Include appropriate error handling- You need to write code that validates the functionality of the class.

with native python"""


class BankAccount:
    def __init__(self):
        # Initialize the balance to 0 cents
        self.balance = 0

    def deposit(self, coins):
        """
        Deposit coins into the account. `coins` is a dictionary with coin denominations as keys
        and the number of those coins as values.
        """
        for denomination, count in coins.items():
            if denomination not in [1, 5, 10, 25, 100]:
                raise ValueError(f"Invalid coin denomination: {denomination}")
            if count < 0:
                raise ValueError("Cannot deposit a negative number of coins")
            self.balance += denomination * count

    def withdraw(self, amount):
        """
        Withdraw the specified amount in cents using the fewest number of coins.
        Returns a dictionary with coin denominations as keys and the number of those coins as values.
        """
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        if amount < 0:
            raise ValueError("Cannot withdraw a negative amount")

        self.balance -= amount
        denominations = [100, 25, 10, 5, 1]
        result = {}
        for denomination in denominations:
            count, amount = divmod(amount, denomination)
            if count > 0:
                result[denomination] = count
        return result

    def total_balance(self):
        """
        Returns the total balance in cents.
        """
        return self.balance


# Validate the functionality of the class

# Create a new bank account
account = BankAccount()

# Deposit some coins
account.deposit({100: 7, 25: 7, 5: 11})  # 3 dollars, 7 quarters, and 11 nickels
print("Total balance after deposit:", account.total_balance())  # Should be 530 cents

# Withdraw some amount
withdrawn_coins = account.withdraw(562)
print("Withdrawn coins:", withdrawn_coins)  # Should be 5 dollars, 2 quarters, 1 dime, and 2 pennies

# # Check the balance after withdrawal
print("Total balance after withdrawal:",
      account.total_balance())  # Should be less 530 - 562 = -32 (shouldn't happen due to error handling)
#
# # Error handling
try:
    account.deposit({3: 1})  # Invalid denomination
except ValueError as e:
    print(e)

try:
    account.deposit({5: -1})  # Negative deposit
except ValueError as e:
    print(e)

try:
    account.withdraw(1000)  # Insufficient balance
except ValueError as e:
    print(e)

try:
    account.withdraw(-100)  # Negative withdrawal
except ValueError as e:
    print(e)

