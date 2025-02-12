# personal_account.py
from amount import Amount  # Import the Amount class from amount.py

class PersonalAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        transaction = Amount(amount, 'DEPOSIT')
        self.transactions.append(transaction)
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds for withdrawal.")
        else:
            transaction = Amount(amount, 'WITHDRAWAL')
            self.transactions.append(transaction)
            self.balance -= amount

    def print_transaction_history(self):
        if not self.transactions:
            print("No transactions available.")
        for transaction in self.transactions:
            print(transaction)

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_account_holder(self):
        return self.account_holder

    def set_account_holder(self, account_holder):
        self.account_holder = account_holder

    def __str__(self):
        return f"Account {self.account_number} - {self.account_holder}: Balance = {self.balance}"

    def __add__(self, amount):
        self.deposit(amount)
        return self

    def __sub__(self, amount):
        self.withdraw(amount)
        return self
