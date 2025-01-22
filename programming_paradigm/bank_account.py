class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        else:
            self.account_balance -= amount
            return True
    def display_balance(self):
        current_balance = "%0.2f" % self.account_balance
        print(f"Current Balance: ${current_balance}")

